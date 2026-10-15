# SlashBack Return Fix

Independent MIT add-on for SlashBack 1.0.2. Removes the return cooldown and death-age expiry while retaining the original command, death-point check, five-second countdown and movement cancellation. Requires the original SlashBack mod; its DLL is not redistributed or modified.

Build with .NET SDK 9.0.317:

```sh
dotnet build mods/SlashBackFix/SlashBackFix.csproj -c Release
dotnet run --project mods/SlashBackFix/tests/Tests.csproj -c Release -- /path/to/pinned/SlashBack.dll
```

The tests require upstream DLL SHA-256 `7eee73f0eaa09dee18df72981413a8e14575919826d462b6c2f3afcc1ef1aa61`. CI downloads it from the pinned public package and compares the source-built fix DLL with the packaged copy. Compile references come from NuGet; they are not bundled into the game profile.

Only the verified 1.0.2 assembly is supported. Patch failure removes this add-on's patches and leaves the original mod active. Regression fixtures and assembly checks do not prove Unity/Harmony runtime behavior. The original movement-detection limitation remains; player instructions are in [the command guide](../../docs/back-command.md).
