# 版本紀錄

依保存的正式模組包與 lock 重建；完整檔案差異與雜湊見 `history/versions.json`。

## v39 — 2026-10-13

加入 Infinity Hammer 1.90.0、依賴 World Edit Commands 1.81.0、PlanBuild 0.20.0。50 個線上套件，40 份設定。

- 成組建材加總材料消耗；關閉免費建造、忽略建築限制與支撐／耐久免疫。
- PlanBuild 預設規劃模式，投料後完成；管理員仍可用 Ctrl 切換免費直接建造。
- Infinity Hammer 使用 F2＋滾輪排列、F4 凍結，PlanBuild 鏡像改為 J 避開 MovingDay；停用即時複製／搬走物件與 Undo／Redo 快捷鍵，藍圖預設不存物件資料。
- 原有 47 個套件、38 份設定與內附 DLL 保留；舊包保留於 v38 tag。
- [操作、管理員限制與驗證範圍](docs/survival-building.md)。

## v38 — 2026-10-13

HUDCompass 地圖動態標記預設開啟，顯示船隻、推車與傳送門。47 個線上套件，38 份設定。

- `F - Dynamic Pins / Show dynamic pins on map`：`false` → `true`。
- 套件版本、其他 37 份設定與內附 DLL 不變，MovingDay 地形快捷鍵保留。
- [使用方式與驗證範圍](docs/map-pins.md)。

## v37 — 2026-10-13

恢復 MovingDay 的左 Ctrl 地形搬移快捷鍵，讓依賴整地／地下室的房子可以連地形搬移。47 個線上套件，38 份設定。

- 按住左 Ctrl 放置才搬地形並恢復舊址；未按住時只搬建築。
- 套件版本、其他 37 份設定、MovingDay 的動物與安全設定不變。
- [操作、地形範圍重疊限制與驗證範圍](docs/moving-buildings.md)。

## v36 — 2026-10-13

加入 MovingDay 1.1.0，搬移單件或整棟既有建築。47 個線上套件，38 份設定。

- 保留玩家、使用中箱子與不可傳送物品的阻擋檢查；關閉地形搬移快捷鍵與自動搬動馴養動物。
- 原有 46 個套件版本、37 份設定與內附 DLL 不變；舊包保留在 v35 tag。
- [操作、限制與驗證範圍](docs/moving-buildings.md)。

## v35 — 2026-10-13

加入 AzuHoverStats 1.1.11，顯示建材支撐與船身耐久數字。46 個線上套件，37 份設定。

- 保留原版顏色；關閉額外物品提示、箱子內容、倒數與切換快捷鍵。
- 原有 45 個套件版本、36 份設定與內附 DLL 不變。
- [使用方式與驗證範圍](docs/hover-stats.md)。

## v34 — 2026-10-12

更新 AzuCraftyBoxes 1.8.28 與 AAA 修補 1.1.0。45 個線上套件，36 份設定。

- 更新 `Azumatt-AzuCraftyBoxes`：1.8.27 → 1.8.28。

- 更新 `swear01-AAA_Crafting_Max_Fix`：1.0.0 → 1.1.0。

## v33 — 2026-10-12

更新 ExtraSlots 1.2.18 與 ValheimCli 0.5.0。45 個線上套件，36 份設定。

- 更新 `shudnal-ExtraSlots`：1.2.17 → 1.2.18。

- 更新 `swear01-ValheimCli`：0.4.0 → 0.5.0。

## v32 — 2026-10-12

套用營火 RGB 調暗設定。45 個線上套件，36 份設定。

- `BepInEx/config/aedenthorn.TorchMod.cfg` 的 `Fire Pits / FirePitColorHigh`：`804129FF` → `402014FF`。

- `BepInEx/config/aedenthorn.TorchMod.cfg` 的 `Fire Pits / FirePitColorLow`：`6B4335FF` → `35211AFF`。

- `BepInEx/config/aedenthorn.TorchMod.cfg` 的 `Fire Pits / FirePitIntensityHigh`：`0.5` → `2`。

- `BepInEx/config/aedenthorn.TorchMod.cfg` 的 `Fire Pits / FirePitIntensityLow`：`0.5` → `1.5`。

## v31 — 2026-10-12

AAA 修補改由 Thunderstore 下載。45 個線上套件，36 份設定。

- 新增套件：`swear01-AAA_Crafting_Max_Fix`。

- 內附檔案變更：`BepInEx/plugins/swear-AAACraftingMaxFix/AAACraftingMaxFix.dll`, `BepInEx/plugins/swear-AAACraftingMaxFix/LICENSE.txt`。

## v30 — 2026-10-12

移出執行包內的來源文字。44 個線上套件，36 份設定。

- 內附檔案變更：`BepInEx/plugins/aedenthorn-TorchMod/SOURCE.txt`, `BepInEx/plugins/swear-AAACraftingMaxFix/SOURCE.txt`。

## v29 — 2026-10-12

BetterFog 改用作者原生預設。44 個線上套件，36 份設定。

- `BepInEx/config/JevMods.BetterFog.cfg` 的 `Fog / Density`：`1` → `0.5`。

- `BepInEx/config/JevMods.BetterFog.cfg` 的 `Fog / MistOpacity`：`1` → `0.2`。

- `BepInEx/config/JevMods.BetterFog.cfg` 的 `Smoke / Opacity`：`0.9` → `0.5`。

## v28 — 2026-10-12

加入 BetterFog 並調整營火 RGB。44 個線上套件，36 份設定。

- 新增套件：`JevMods-BetterFog`。

- `BepInEx/config/aedenthorn.TorchMod.cfg` 的 `Fire Pits / FirePitColorHigh`：`None` → `804129FF`。

- `BepInEx/config/aedenthorn.TorchMod.cfg` 的 `Fire Pits / FirePitColorLow`：`None` → `6B4335FF`。

## v27 — 2026-10-12

加入 ValheimCli 0.4.0。43 個線上套件，35 份設定。

- 新增套件：`swear01-ValheimCli`。

## v26 — 2026-10-11

內附 AAA Crafting Max Fix 1.0.0。42 個線上套件，35 份設定。

- 內附檔案變更：`BepInEx/plugins/swear-AAACraftingMaxFix/AAACraftingMaxFix.dll`, `BepInEx/plugins/swear-AAACraftingMaxFix/LICENSE.txt`, `BepInEx/plugins/swear-AAACraftingMaxFix/SOURCE.txt`。

## v25 — 2026-10-11

箱子取料範圍設為 40 公尺。42 個線上套件，35 份設定。

- `BepInEx/config/Azumatt.AzuCraftyBoxes.cfg` 的 `2 - CraftyBoxes / Container Range`：`30` → `40`。

## v24 — 2026-10-11

堆疊倍率調為 ×4。42 個線上套件，35 份設定。

## v23 — 2026-10-11

工作台範圍設為 50 公尺。42 個線上套件，35 份設定。

- `BepInEx/config/Azumatt.AzuWorkbenchTweaks.cfg` 的 `2 - WorkBench / WorkBenchRange`：`40` → `50`。

## v22 — 2026-10-10

加入 ItemStacksItemWeights。42 個線上套件，35 份設定。

- 新增套件：`shudnal-ItemStacksItemWeights`。

## v21 — 2026-10-10

加入 PortalGhostFix 並調整負重成長。41 個線上套件，34 份設定。

- 新增套件：`Sfantul-PortalGhostFix`。

- `BepInEx/config/Searica.Valheim.SkilledCarryWeight.cfg` 的 `Run / Coefficient`：`2` → `4`。

## v20 — 2026-10-10

更新 HUDCompass 與 Extra Snap Points。40 個線上套件，34 份設定。

- 更新 `Searica-Extra_Snap_Points_Made_Easy`：2.1.0 → 2.1.1。

- 更新 `Neobotics-HUDCompass`：1.2.0 → 1.2.1。

## v19 — 2026-10-10

加入 AdrenalineModifier。40 個線上套件，34 份設定。

- 新增套件：`mightywa33ior-AdrenalineModifier`。

## v18 — 2026-10-09

加入 PlantEasily 與 PlantEverything。39 個線上套件，33 份設定。

- 新增套件：`Advize-PlantEasily`, `Advize-PlantEverything`。

## v17 — 2026-10-09

加入 SlashBack。37 個線上套件，31 份設定。

- 新增套件：`Geda_Giminei-SlashBack`。

## v16 — 2026-10-09

加入 ValheimTerrainTools。36 個線上套件，31 份設定。

- 新增套件：`QoLTeam-ValheimTerrainTools`。

## v15 — 2026-10-09

更新 FirstPersonMode 與 QuickTeleport。35 個線上套件，30 份設定。

- 更新 `OdinPlus-QuickTeleport`：2.0.4 → 2.0.5。

- 更新 `Azumatt-FirstPersonMode`：1.4.4 → 1.4.5。

## v14 — 2026-10-09

內附 Torch Light Mod 與營火設定。35 個線上套件，30 份設定。

- 內附檔案變更：`BepInEx/plugins/aedenthorn-TorchMod/LICENSE.txt`, `BepInEx/plugins/aedenthorn-TorchMod/SOURCE.txt`, `BepInEx/plugins/aedenthorn-TorchMod/TorchMod.dll`。

## v13 — 2026-10-09

加入 AutoDoors。35 個線上套件，29 份設定。

- 新增套件：`Zenox-AutoDoors`。

## v12 — 2026-10-09

調整 ExtraSlots 撿墓碑後自動裝備。34 個線上套件，28 份設定。

- `BepInEx/config/shudnal.ExtraSlots.cfg` 的 `Extra slots - Auto equip on tombstone pickup / Apply after manual Take All`：`None` → `true`。

- `BepInEx/config/shudnal.ExtraSlots.cfg` 的 `Extra slots - Auto equip on tombstone pickup / Equip all equipment slots`：`None` → `true`。

- `BepInEx/config/shudnal.ExtraSlots.cfg` 的 `Extra slots - Auto equip on tombstone pickup / Equip previous weapon and shield`：`None` → `true`。

## v11 — 2026-10-08

調整 Server Devcommands 設定。34 個線上套件，28 份設定。

- `BepInEx/config/server_devcommands.cfg` 的 `1. General / Automatic debug mode`：`false` → `true`。

- `BepInEx/config/server_devcommands.cfg` 的 `1. General / Debug mode fast teleport`：`false` → `true`。

- `BepInEx/config/server_devcommands.cfg` 的 `2. Console / Disable debug mode keys`：`None` → `true`。

## v10 — 2026-10-08

加入 Recycle N Reclaim 與裝備欄保護。34 個線上套件，28 份設定。

- 新增套件：`Azumatt-Recycle_N_Reclaim`。

- `BepInEx/config/shudnal.ExtraSlots.cfg` 的 `Mods compatibility / Prevent Recycle_N_Reclaim from recycling items in extra slots`：`None` → `true`。

## v9 — 2026-10-08

調整箱子取料設定。33 個線上套件，27 份設定。

- `BepInEx/config/Azumatt.AzuCraftyBoxes.cfg` 的 `2 - CraftyBoxes / Container Range`：`20` → `30`。

## v8 — 2026-10-08

加入 SmartShield。33 個線上套件，27 份設定。

- 新增套件：`cjayride-SmartShield`。

## v7 — 2026-10-08

調整 SleepSkip 設定。32 個線上套件，26 份設定。

- `BepInEx/config/Azumatt.SleepSkip.cfg` 的 `1 - General / Warning Time`：`None` → `5`。


## v6 — 2026-10-07

調整負重倍率與腰帶加成。32 個線上套件，26 份設定。

- `BepInEx/config/dev.crystal.magni.cfg` 的 `Weight / CarryCapacityMultiplier`：`1.333333333` → `1.5`。

- `BepInEx/config/robit.configurablecarryweight.cfg` 的 `Carry Weight / Megingjord Bonus`：`300` → `266.666667`。


## v5 — 2026-10-07

加入 ConfigurableCarryWeight。32 個線上套件，26 份設定。

- 新增套件：`omnipeach-ConfigurableCarryWeight`。


## v4 — 2026-10-07

調整負重成長設定。31 個線上套件，25 份設定。

- `BepInEx/config/Searica.Valheim.SkilledCarryWeight.cfg` 的 `Run / Coefficient`：`1` → `2`。


## v3 — 2026-10-07

加入 Server Devcommands。31 個線上套件，25 份設定。

- 新增套件：`JereKuusela-Server_devcommands`。


## v2 — 2026-10-07

加入 ServerSideMap。30 個線上套件，24 份設定。

- 新增套件：`Mydayyy-ServerSideMap`。


## v1 — 2026-10-07

建立雙人 QoL 初始包。29 個線上套件，23 份設定。