using System;

namespace BepInEx
{
    [AttributeUsage(AttributeTargets.Class)]
    public sealed class BepInPlugin : Attribute
    {
        public BepInPlugin(string id, string name, string version) { }
    }
    [AttributeUsage(AttributeTargets.Class)]
    public sealed class BepInDependency : Attribute
    {
        public BepInDependency(string id, string version) { }
    }
    public class BaseUnityPlugin
    {
        protected readonly TestLogger Logger = new TestLogger();
    }
    public sealed class TestLogger
    {
        public void LogWarning(string text) { }
        public void LogInfo(string text) { }
        public void LogError(string text) { }
    }
}
