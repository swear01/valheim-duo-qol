# 版本紀錄

依保存的正式模組包與 lock 重建；完整檔案差異與雜湊見 `history/versions.json`。

## v54 — 2026-10-16

雙人私人包加入 [Badgers Straight Structures 0.6.0](https://www.nexusmods.com/valheim/mods/2938)，降低原版建材表面與邊緣的視覺扭曲；木牆、樑柱、門等建材也會一起變平整，沒有石材限定設定。

- 保留作者預設 `Mod Configuration / Warp Amount = 0.004`；DLL 靜態檢查確認只設定材質 `_RippleDistance`，沒有修改碰撞、耐久或支撐。
- 作者禁止重新上傳，DLL 僅從本機加入私人交付；公開包保存設定與來源雜湊。私人打包若找不到原始 DLL 或雜湊不符會停止。[維護方法](docs/private-package.md)。
- 49 個線上套件、40 份公開設定、41 份私人設定；既有模組與設定保留。已核對下載、DLL、設定與封包內容；Gale 匯入、遊戲畫面及雙人行為尚未實測。

## v53 — 2026-10-16

移除 PerfectPlacement 1.2.6 及其設定，不再提供 F1 進階建築、Keypad0 進階編輯與該模組的自由旋轉功能。

- 保留 Infinity Hammer 的 F4 凍結／微調、成排鋪設與 MovingDay 搬移建築。沿用舊 profile 時，需在 Gale 移除 `Azumatt-PerfectPlacement`；匯入新包不會卸載舊 profile 的模組。
- 49 個線上套件、39 份公開設定；其餘模組版本、設定與內附 DLL 保留。已核對依賴、內容差異與封包重建；Gale 匯入、移除後的世界重載及雙人行為尚未實測。

## v52 — 2026-10-16

ComfortTweaks 舒適度家具清單的開關由 Home 改為 J，避開 MovingDay 搬移模式的 Home 重設高度，Mac 與 Windows 都可直接按字母鍵。

- `5. Comfort Pieces List / Toggle Visibility = J`；保留 50 公尺家具判定半徑、清單啟用與其他模組預設規則。[操作說明](docs/comfort.md)。
- 50 個線上套件、40 份公開設定、其他設定與內附修補保留。已核對快捷鍵、內容差異與封包重建；Gale 匯入、遊戲內按鍵及雙人行為尚未實測。

## v51 — 2026-10-16

加入 Hexium 的 ComfortTweaks 3.3.11，家具舒適度判定半徑由預設 10 公尺提高至 50 公尺。

- 啟用已生效與缺少家具清單；用 Home 開關，避開鋤頭 F6 取樣高度。Mac 可用 Fn＋左方向鍵；[操作說明](docs/comfort.md)。
- 其餘舒適度、休息增益、家具分組與火源範圍均使用上游預設；保留原有套件、設定與內附修補。
- 50 個線上套件、40 份公開設定；雙人私人包含 41 份設定。已核對下載、依賴、DLL 設定鍵與封包重建；Gale 匯入、遊戲內半徑／清單及雙人行為尚未實測。

## v50 — 2026-10-16

Infinity Hammer 前後排列由右 Ctrl 改為右 Shift＋滾輪，方便沒有右 Ctrl 的鍵盤使用。

- `3. Binds / Zooping forward (mouse wheel)` 設為 `RightShift`；右 Alt＋滾輪調左右寬度的設定保留。Shift＋滾輪縮放仍停用。
- 右 Shift 仍與 AzuCraftyBoxes 單箱切換、PlantEasily 種植範圍共用；準星對著可操作的箱子時按下它，也會切換該箱子是否參與製作。[完整建築操作](docs/survival-building.md)。
- 49 個線上套件、39 份公開設定、其他設定與內附修補保留；已核對設定及封包重建，遊戲內按鍵、滾輪與雙人操作尚未實測。

## v49 — 2026-10-16

Infinity Hammer 的 `3. Binds / Zooping forward (mouse wheel)` 設為 `RightControl`，新增右 Ctrl＋滾輪調整前後排數。

- 普通建築槌選地板，右 Alt＋滾輪調左右寬度，再用右 Ctrl＋滾輪展開前後排數，確認預覽與材料後左鍵放置；[完整操作](docs/survival-building.md)。
- 保留材料、體力、耐久與支撐設定；49 個線上套件、39 份公開設定、其他快捷鍵與內附修補保留。
- 已核對上游 1.90.0 的設定鍵與指令對應、封包重建；遊戲內按鍵、滾輪與雙人操作尚未實測。

## v48 — 2026-10-16

ValheimTerrainTools 的 `Removal / MaximumRadius` 由 0.5 改為 10 公尺，解除最小與最大值皆為 0.5 所造成的大小鎖定。

- 選 Remove nature 後，用 Shift＋滾輪在 0.5～10 公尺間調整半徑；一般整地的 `Brush / MaximumRadius` 仍為 10。
- 這個上限同時影響 Remove builds；移除沒有材料返還或復原，先確認預覽範圍。
- 49 個線上套件、39 份公開設定、其他設定與內附修補保留；PlanBuild 維持移除。
- 已核對上游 0.6.4 的輸入與半徑限制實作、邊界計算及封包重建；遊戲內滾輪與雙人操作尚未實測。

## v47 — 2026-10-16

移除 PlanBuild 0.20.0 與 `marcopogo.PlanBuild.cfg`。目前為 49 個線上套件、39 份公開設定；雙人私人包含 40 份設定。

- Infinity Hammer、World Edit Commands、MovingDay 與其他套件版本、設定和內附修補保留；BepInEx、Jotunn 仍有其他模組需要。
- 保留 50 公尺箱子取料、右 Shift 單箱切換、右 Shift 種植範圍及 `/back` 修補。
- 建築說明不再要求使用 PlanBuild。若有未完成規劃件，先在舊 profile 完成或拆除並回收材料，再切換新包；[操作與藍圖備份](docs/survival-building.md)。
- 已核對依賴、剩餘檔案逐位元組一致與封包重建；沒有修改目前遊戲或存檔，移除後的世界重載與雙人行為尚未實測。

## v46 — 2026-10-16

AzuCraftyBoxes 單一箱子是否參與製作的切換鍵由預設左 Shift＋E 改為右 Shift。

- `3 - Keys / Container Toggle Key` 設為 `RightShift`；對準可操作的箱子按一次，即切換該箱子是否提供製作材料，查看箱子提示的勾／叉確認狀態。快捷鍵由各玩家自行套用，箱子的排除狀態會同步。
- 右 Shift 同時是 PlantEasily 調整種植範圍的修飾鍵；若準星對著箱子，按下它也會切換該箱子的狀態。
- 全部／自己的箱子／不取料的角色模式切換仍為左 Alt＋O；保留 50 公尺取料範圍、其他設定、50 個線上套件與內附修補。
- 已核對上游 1.8.28 的設定鍵與單箱切換流程、封包重建；遊戲內按鍵與雙人行為尚未實測。

## v45 — 2026-10-16

AzuCraftyBoxes 箱子取料半徑由 40 公尺提高至 50 公尺，用於製作與建造。

- `2 - CraftyBoxes / Container Range` 設為 `50`；工作台建造範圍原本即為 50 公尺。
- 保留箱子至少一件物品、PlantEasily 右 Shift、`/back` 修補，以及其他設定與套件版本。
- 已核對設定與封包重建；遊戲內取料邊界與雙人行為尚未實測。

## v44 — 2026-10-16

PlantEasily 調整種植範圍的修飾鍵由右 Ctrl 改為右 Shift。

- 手持耕耘器並選擇作物時，按住右 Shift＋左右方向鍵調整欄數，右 Shift＋上下方向鍵調整列數。
- 採收修飾鍵仍為左 Shift；其他設定、50 個線上套件與內附修補保留。
- 已核對設定與封包重建；遊戲內按鍵與雙人行為尚未實測。

## v43 — 2026-10-16

取消 `/back` 的使用後冷卻與死亡後 120 秒期限，連續死亡或超過兩分鐘都可返回。

- 內附獨立 MIT 修補 SlashBack Return Fix 1.0.0；原版 SlashBack 1.0.2 保留且未修改。
- 保留 5 秒站立倒數、移動取消、死亡位置檢查與既有傳送流程；提示不再顯示過期秒數。
- v42 的 50 個線上套件、40 份公開設定與原有內附檔案保留；雙人私人包沿用固定管理員名單，含 41 份設定。
- [安裝、操作與驗證範圍](docs/back-command.md)。Unity／Harmony 掛接與雙人遊戲尚未實測。

## v42 — 2026-10-15

更新六個模組，仍為 50 個線上套件、40 份公開設定。雙人私人包沿用既有管理員設定，含 41 份設定。

- ConditionalConfigSync 1.0.10 → 1.0.11；ExtraSlots 1.2.18 → 1.2.19。
- PerfectPlacement 1.2.4 → 1.2.6；FirstPersonMode 1.4.5 → 1.4.6。
- QuickTeleport 2.0.5 → 2.0.7；Extra Snap Points Made Easy 2.1.1 → 2.2.0。
- 普通手動吸附維持 CapsLock，避免新版預設 F3 與建築退出鍵衝突；P／F11 與既有設定保留。
- AAA Crafting 仍是 2.1.11，保留 Max Fix 1.1.0。完整變更與快捷鍵見 [v42 更新說明](docs/update-v42.md)。
- 已核對下載、依賴、設定鍵與封包重建；Gale 匯入、遊戲與雙人行為尚未實測。

## v41 — 2026-10-13

統一使用 v41 檔名與 profile，不再加 `private-admins` 尾碼。50 個線上套件與原有設定版本保留。

- 雙人管理員包由本機私人設定產生於 `dist/private/`，含 41 份設定；公開包含 40 份設定，不包含玩家 ID。
- 兩人交付使用私人包；公開 Actions 仍只產生公開包。匯入與同名 profile 注意事項見 [私人包維護](docs/private-package.md)。

## v40 — 2026-10-13

水平排列改用右 Alt＋滾輪，避開原版 F2 資訊面板。50 個線上套件，40 份設定。

- 只改 Infinity Hammer 的水平排列鍵；v39 的生存建築設定、套件版本與其他設定保留。
- 舊版封存留在各版 tag；[完整建築操作](docs/survival-building.md)。

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