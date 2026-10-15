# 生存建築：Infinity Hammer

v47 已移除 PlanBuild 與其設定。Infinity Hammer 1.90.0、World Edit Commands 1.81.0 和 MovingDay 保留，設定不變。

兩人退出遊戲、備份世界與角色後，在 Gale 匯入 v47 為新 profile，勾選 Import all files。匯入新包不代表既有 profile 已卸載 PlanBuild；若沿用舊 profile，需在 Gale 移除 MathiasDecrock-PlanBuild。

若曾放置未完工的 PlanBuild 規劃件，切換前先在舊 profile 完成，或用 Blueprint Rune 的 Remove planned pieces 拆除並取回已投入材料。另行備份自己的 `BepInEx/config/PlanBuild/blueprints`；新包不再提供 Plan Hammer、Blueprint Rune、Plan Totem 等工具或物件。這次只修改模組包，沒有修改存檔或刪除本機藍圖。[作者操作說明](https://github.com/sirskunkalot/PlanBuild/blob/master/README.md)。

## 預設消耗與限制

- Infinity Hammer：`Group resource cost = true`，整組加總有配方建材的材料；`No resource cost`、`No durability cost`、`No stamina cost` 全為 false。
- `Ignore no build`、`Ignore other restrictions`、`Ignore wards`、`Allow in dungeons` 全為 false。`No physics = false`、`Set invulnerability = Off`、`Overwrite health = 0`，保留支撐與耐久；`Hammer range = 0` 不主動延長原有距離。
- 關閉萬物拆除／修理及 Infinity Hammer 的額外管理員工具。藍圖預設不保存物件資料、不擷取地形。

以上是便利建築的預設，沒有把管理員工具變成強制防作弊模組。Infinity Hammer 的指令需要作弊／管理員權限；加入者需有主機授權。雙人私人包沿用固定兩位管理員及 Automatic devcommands 設定，見 [私人包維護](private-package.md)；使用時保持 nocost 關閉。

世界的免費建造設定、nocost 及手動管理員指令仍能繞過消耗。Infinity Hammer 加總材料不等於逐件驗證所有解鎖、工作台或碰撞條件；請限用已解鎖、有正常建造配方的建材。

## 成排鋪設與微調

1. 拿普通建築槌，從原本選單選已解鎖的地板、牆或屋頂。
2. 按住 **右 Alt＋滾輪** 調整水平排列的預覽；確認材料總數足夠再左鍵放置。先試 3 塊木地板，確認扣除 3 份材料。
3. **F4** 凍結／解除預覽位置。方向鍵微調前後左右，PageUp／PageDown 微調高度；不要同時啟用 PerfectPlacement 進階模式或 MovingDay 搬移模式。
4. 需要垂直／前後排列，可在 F5 執行 `hammer_zoop_up auto`／`hammer_zoop_forward auto`；`hammer_grid 1 0,0,0` 切換 1 公尺網格。指令需有權限；若未啟用主控台，可在啟動參數加入 `-console`。

水平排列使用 RightAlt，避開原版 F2 資訊面板；F4 避開 PerfectPlacement 的 Keypad0；停用 Infinity Hammer 的 Shift＋滾輪縮放，保留原有旋轉操作。整組三軸旋轉和 PerfectPlacement 的互動仍需遊戲內測試。

要搬原本那一棟並保留箱內物品，使用 MovingDay，見 [搬移建築](moving-buildings.md)。

## 資料複製與驗證

Infinity Hammer 的「即時選取既有物件」會保留物件資料；關閉 `Save data to blueprints` **只影響存成藍圖**，不能阻止即時複製箱內物品。因此本包維持停用 Select／Select frozen／Pick／Pick frozen 與 Undo／Redo 快捷鍵，從普通建造選單取建材。管理員仍能自行執行指令或載入含資料的外部藍圖，不能據此宣稱杜絕複製物品。

v47 僅移除 PlanBuild 套件與設定，其餘套件版本、設定及內附 DLL 保留。驗證包含依賴完整性、封包內容差異與重建；未啟動或修改目前遊戲。

尚未完成 Gale GUI 匯入、移除模組後的世界重載、遊戲內扣料／支撐、兩人同步及 PerfectPlacement／MovingDay／AzuCraftyBoxes 的實際互動。先在測試世界確認 3 塊地板扣 3 份材料、缺料不能放置，再使用原世界。

## 玩家實際使用

[玩家 Nienna000 的第一手分享](https://www.reddit.com/r/valheim/comments/1h3rgn2/do_you_play_with_mods_what_mods_are_you_playing/) 表示平常採集、探索、蓋房時使用 Infinity Hammer，主要為了精準擺放。他也明說使用許多降低難度的模組，因此能證明日常遊玩用途，不能證明與本包相同的扣料、支撐設定已實測。

作者文件：[Infinity Hammer 設定](https://github.com/JereKuusela/valheim-infinity_hammer/blob/main/hammer.md) · [藍圖資料](https://github.com/JereKuusela/valheim-infinity_hammer/blob/main/blueprints.md)。
