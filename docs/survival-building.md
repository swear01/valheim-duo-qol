# 生存建築：Infinity Hammer 與 PlanBuild

v39 加入 Infinity Hammer 1.90.0、它需要的 World Edit Commands 1.81.0，以及 PlanBuild 0.20.0。原有 Server devcommands 1.115.0、Jotunn 2.30.2 已符合依賴，不需升級。兩人退出遊戲、備份世界與角色後，在 Gale 匯入同版新 profile，勾選 Import all files。原有 47 個套件、38 份設定與內附 DLL 保留。

## 預設消耗與限制

- Infinity Hammer：`Group resource cost = true`，整組加總有配方建材的材料；`No resource cost`、`No durability cost`、`No stamina cost` 全為 false。
- `Ignore no build`、`Ignore other restrictions`、`Ignore wards`、`Allow in dungeons` 全為 false。`No physics = false`、`Set invulnerability = Off`、`Overwrite health = 0`，保留支撐與耐久；`Hammer range = 0` 不主動延長原有距離。
- 關閉萬物拆除／修理及 Infinity Hammer 的額外管理員工具。藍圖預設不保存物件資料、不擷取地形。
- PlanBuild：`Default build mode = Planned`、`Allow direct build = false`、`Allow terrain tools = false`、`Unlimited health = false`、`Plan unknown pieces = false`，顯示材料清單。先放免費的規劃虛影，再投入材料完成實體建材。

以上是便利建築的預設，沒有把管理員工具變成強制防作弊模組。Infinity Hammer 的指令需要作弊／管理員權限；房主可用，加入者不會因匯入模組就自動獲得權限。需要時由房主為可信任玩家授權並啟用 devcommands，保持 nocost 關閉。本包沒有自動授權，也沒有改動既有 Server devcommands 的自動開關。

PlanBuild 藍圖也可能記錄箱內資料；規劃建造路徑不還原箱內庫存，直接建造路徑則會還原。PlanBuild 明確讓管理員繞過 `Allow direct build = false`；**放置藍圖時不要按住 Ctrl**，否則管理員仍可切成免費直接建造。世界的免費建造設定、nocost 及手動管理員指令也能繞過消耗。Infinity Hammer 加總材料不等於逐件驗證所有解鎖、工作台或碰撞條件；請限用已解鎖、有正常建造配方的建材，整棟複製優先走 PlanBuild 規劃流程。

## 成排鋪設與微調

1. 拿普通建築槌，從原本選單選已解鎖的地板、牆或屋頂。
2. 按住 **F2＋滾輪** 調整水平排列的預覽；確認材料總數足夠再左鍵放置。先試 3 塊木地板，確認扣除 3 份材料。
3. **F4** 凍結／解除預覽位置。方向鍵微調前後左右，PageUp／PageDown 微調高度；不要同時啟用 PerfectPlacement 進階模式或 MovingDay 搬移模式。
4. 需要垂直／前後排列，可在 F5 執行 `hammer_zoop_up auto`／`hammer_zoop_forward auto`；`hammer_grid 1 0,0,0` 切換 1 公尺網格。指令需有權限；若未啟用主控台，可在啟動參數加入 `-console`。

PlanBuild 鏡像改為 J，避開 MovingDay 的 H（兩者都接受建造工具）；F4 避開 PerfectPlacement 的 Keypad0；停用 Infinity Hammer 的 Shift＋滾輪縮放，保留原有旋轉操作。整組三軸旋轉和 PerfectPlacement 的互動仍需遊戲內測試。

## 複製、旋轉、翻轉與貼上

1. 用 1 石頭製作 **Blueprint Rune**。選 Add to selection，Alt＋左鍵選相連建築；先檢查綠色高亮，用 Add／Remove 修正範圍。
2. 選 Edit selection → **Copy** 產生暫存藍圖，或 Save blueprint 保存；不要選 Cut／Delete。藍圖預設位於 `BepInEx/config/PlanBuild/blueprints`，換 profile 前另行備份自己的作品。
3. 在目的地用滾輪旋轉，**J** 鏡像；Ctrl＋J 另存鏡像副本。放置時放開 Ctrl，左鍵只放規劃虛影，舊家會保留。
4. 帶著 Plan Hammer（1 木頭製作）及建造材料，對虛影按 E 投料／完成；按住 E 可投入現有材料，也可把材料放進 Plan Totem 組裝。完成實體仍需支撐及所需工作台；箱內取料由現有 AzuCraftyBoxes 提供，兩者互動尚待實測。

要搬原本那一棟並保留箱內物品，繼續使用 MovingDay，見 [搬移建築](moving-buildings.md)。不要用複製來搬箱內物品。

## 資料複製與驗證

Infinity Hammer 的「即時選取既有物件」會保留物件資料；關閉 `Save data to blueprints` **只影響存成藍圖**，不能阻止即時複製箱內物品。因此本包預先停用 Select／Select frozen／Pick／Pick frozen 與 Undo／Redo 快捷鍵；從普通建造選單取建材，整棟則使用 PlanBuild。管理員仍能自行執行指令或載入含資料的外部藍圖，不能據此宣稱杜絕複製物品。

已核對三份公開套件 ZIP CRC、路徑、manifest、依賴、GUID、DLL 雜湊；從發布的 DLL 核對全部新增設定鍵、材料加總／扣除、原有限制開關、即時選取資料與 PlanBuild 管理員直接建造路徑。原有套件與設定逐位元組保留。未啟動或修改目前遊戲。

尚未完成 Gale GUI 匯入、遊戲內扣料／支撐、兩人同步、儲存重載及 PerfectPlacement／MovingDay／AzuCraftyBoxes 的實際互動。先在測試世界確認 3 塊地板扣 3 份材料、缺料不能完成、浮空實體會正常倒塌、藍圖不複製箱內物品，再使用原世界。

## 玩家實際使用

[玩家 Nienna000 的第一手分享](https://www.reddit.com/r/valheim/comments/1h3rgn2/do_you_play_with_mods_what_mods_are_you_playing/) 表示平常採集、探索、蓋房時使用 Infinity Hammer，主要為了精準擺放。他也明說使用許多降低難度的模組，因此能證明日常遊玩用途，不能證明與本包相同的扣料、支撐設定已實測。

作者文件：[Infinity Hammer 設定](https://github.com/JereKuusela/valheim-infinity_hammer/blob/main/hammer.md) · [藍圖資料](https://github.com/JereKuusela/valheim-infinity_hammer/blob/main/blueprints.md) · [PlanBuild](https://github.com/sirskunkalot/PlanBuild/blob/master/README.md)。
