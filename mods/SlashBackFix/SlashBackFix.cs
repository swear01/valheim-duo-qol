using System;
using System.Reflection;
using BepInEx;
using HarmonyLib;

namespace ValheimDuoQoL
{
    [BepInPlugin(Id, "SlashBack Return Fix", "1.0.0")]
    [BepInDependency("SlashBack", "1.0.2")]
    public sealed class SlashBackFix : BaseUnityPlugin
    {
        public const string Id = "swear.valheim.SlashBackFix";
        private Harmony harmony;

        private void Awake()
        {
            var upstream = AccessTools.TypeByName("SlashBack.Plugin");
            if (upstream == null || upstream.Assembly.GetName().Version != new System.Version(1, 0, 2, 0))
            {
                Logger.LogWarning("SlashBack Return Fix requires SlashBack 1.0.2; no patches applied.");
                return;
            }
            harmony = new Harmony(Id);
            try
            {
                harmony.PatchAll(typeof(SlashBackFix).Assembly);
                Logger.LogInfo("SlashBack cooldown and death expiry removed; 5s countdown and movement cancellation retained.");
            }
            catch (Exception error)
            {
                harmony.UnpatchSelf();
                Logger.LogError("SlashBack return fix could not be applied; original mod restored. " + error);
            }
        }

        private void OnDestroy()
        {
            harmony?.UnpatchSelf();
        }
    }

    [HarmonyPatch]
    internal static class ReturnLimitsPatch
    {
        private static MethodBase TargetMethod()
        {
            return AccessTools.Method("SlashBack.Plugin:FixedUpdate");
        }

        private static void Prefix(ref bool ___isCooldown, ref float ___cooldownTimer,
            ref bool ___isExpired, ref float ___cooldown)
        {
            Reset(ref ___isCooldown, ref ___cooldownTimer, ref ___isExpired, ref ___cooldown);
        }

        private static void Postfix(ref bool ___isCooldown, ref float ___cooldownTimer,
            ref bool ___isExpired, ref float ___cooldown)
        {
            Reset(ref ___isCooldown, ref ___cooldownTimer, ref ___isExpired, ref ___cooldown);
        }

        internal static void Reset(ref bool isCooldown, ref float cooldownTimer,
            ref bool isExpired, ref float deathWindow)
        {
            isCooldown = false;
            cooldownTimer = 0f;
            // Upstream uses one value for both limits and marks success as expired.
            deathWindow = float.PositiveInfinity;
            isExpired = false;
        }
    }

    [HarmonyPatch]
    internal static class DeathHintPatch
    {
        private static MethodBase TargetMethod()
        {
            return AccessTools.Method("SlashBack.Plugin:Say");
        }

        internal static void Prefix(ref string text)
        {
            if (text != null && text.StartsWith(
                "<color=#f7e694>Use /back return to the death position.\nExpires in ", StringComparison.Ordinal))
                text = "<color=#f7e694>Use /back to return to your last death location, if recorded. No cooldown or expiry.</color>";
        }
    }
}
