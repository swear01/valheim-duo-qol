using System;
using System.IO;
using System.Linq;
using System.Reflection.Metadata;
using System.Reflection.Metadata.Ecma335;
using System.Reflection.PortableExecutable;
using System.Security.Cryptography;
using ValheimDuoQoL;

static class Program
{
    static int checks;
    static void Check(bool value, string message)
    {
        if (!value) throw new Exception(message);
        checks++;
    }

    static void Main(string[] args)
    {
        bool cooldown = true, expired = true;
        float remaining = 60, window = 120, secondDeathAge = 20;
        // SlashBack 1.0.2 skips its load-time reset during an earlier return's cooldown.
        if (secondDeathAge <= window && !cooldown) expired = false;
        Check(expired, "baseline reproduces second-death expired flag");
        ReturnLimitsPatch.Reset(ref cooldown, ref remaining, ref expired, ref window);
        Check(!cooldown && remaining == 0 && !expired, "second death not blocked by previous return");
        Check(float.IsPositiveInfinity(window), "death window removed");
        Check(!(3600 > window) && !(float.MaxValue > window), "late returns do not expire");
        expired = true;
        remaining = window - secondDeathAge;
        Check(float.IsPositiveInfinity(remaining), "upstream would otherwise start an infinite cooldown");
        ReturnLimitsPatch.Reset(ref cooldown, ref remaining, ref expired, ref window);
        Check(!cooldown && remaining == 0 && !expired, "repeat use after successful teleport");
        ReturnLimitsPatch.Reset(ref cooldown, ref remaining, ref expired, ref window);
        Check(!cooldown && remaining == 0 && !expired, "idempotent repair");
        string hint = "<color=#f7e694>Use /back return to the death position.\nExpires in Infinitys</color>";
        DeathHintPatch.Prefix(ref hint);
        Check(hint.Contains("No cooldown or expiry") && !hint.Contains("Infinity"), "accurate death hint");
        foreach (string value in new[] { "Teleporting in 5s.", "Teleport canceled because the player moved.", "other message", null })
        {
            string text = value;
            DeathHintPatch.Prefix(ref text);
            Check(text == value, "other messages unchanged");
        }
        Check(args.Length == 1, "provide pinned upstream DLL");
        byte[] raw = File.ReadAllBytes(args[0]);
        Check(Convert.ToHexString(SHA256.HashData(raw)).ToLowerInvariant() ==
            "7eee73f0eaa09dee18df72981413a8e14575919826d462b6c2f3afcc1ef1aa61", "exact pinned upstream DLL");
        using var pe = new PEReader(new MemoryStream(raw));
        var metadata = pe.GetMetadataReader();
        Check(metadata.GetAssemblyDefinition().Version == new System.Version(1, 0, 2, 0), "supported upstream assembly");
        var type = metadata.TypeDefinitions.Select(metadata.GetTypeDefinition).Single(t =>
            metadata.GetString(t.Namespace) == "SlashBack" && metadata.GetString(t.Name) == "Plugin");
        var fields = type.GetFields().ToDictionary(h => metadata.GetString(metadata.GetFieldDefinition(h).Name));
        foreach (var item in new[] { ("isCooldown", (byte)0x02), ("cooldownTimer", (byte)0x0c), ("isExpired", (byte)0x02), ("cooldown", (byte)0x0c) })
        {
            Check(fields.ContainsKey(item.Item1), "actual injection target " + item.Item1);
            byte[] signature = metadata.GetBlobBytes(metadata.GetFieldDefinition(fields[item.Item1]).Signature);
            Check(signature.SequenceEqual(new byte[] { 0x06, item.Item2 }), "actual field type " + item.Item1);
        }
        var methods = type.GetMethods().Select(metadata.GetMethodDefinition).ToArray();
        Check(methods.Count(m => metadata.GetString(m.Name) == "FixedUpdate") == 1, "unique update target");
        var say = methods.Single(m => metadata.GetString(m.Name) == "Say");
        Check(metadata.GetString(metadata.GetParameter(say.GetParameters().Single()).Name) == "text", "hint argument name");
        Check(methods.Any(m => metadata.GetString(m.Name) == "PlayerIsMoving") &&
              methods.Any(m => metadata.GetString(m.Name) == "TeleportToDeahPoint"), "movement and teleport methods retained");
        var ctor = methods.Single(m => metadata.GetString(m.Name) == ".ctor");
        byte[] il = pe.GetMethodBody(ctor.RelativeVirtualAddress).GetILBytes();
        byte[] countdown = new byte[] { 0x22 }.Concat(BitConverter.GetBytes(5f)).Concat(new byte[] { 0x7d })
            .Concat(BitConverter.GetBytes(MetadataTokens.GetToken(fields["countdown"]))).ToArray();
        Check(Enumerable.Range(0, il.Length - countdown.Length + 1).Any(i => il.Skip(i).Take(countdown.Length).SequenceEqual(countdown)),
            "actual upstream five-second countdown unchanged");
        Console.WriteLine($"PASS: {checks} checks; consecutive deaths, unlimited window, repeat use, correct hints and pinned metadata. Unity/Harmony detours not run.");
    }
}
