# v42 更新說明 — 2026-10-15

從 v41 更新六個模組。模組數仍是 50，沒有新增或移除模組。公開包含 40 份設定；兩人使用由固定私人管理員名單產生的完整包，含 41 份設定。

| 模組 | 版本 | 會影響的使用方式 |
| --- | --- | --- |
| [ConditionalConfigSync](https://valheim.hexium.gg/mods/shudnal/ConditionalConfigSync) | 1.0.10 → 1.0.11 | 改善慢速連線的設定同步，傳輸持續有進度就可繼續。房主與加入者都更新才能完整受益。 |
| [ExtraSlots](https://valheim.hexium.gg/mods/shudnal/ExtraSlots) | 1.2.18 → 1.2.19 | 在原生快捷列輪盤底部新增 Quick bars，可選食物、彈藥與最多六個快捷格；修正手把調整 PlantEasily 網格時誤用快捷列物品。移除已棄用的 ValheimRadial 整合，這個包沒有使用它。 |
| [PerfectPlacement](https://valheim.hexium.gg/mods/Azumatt/PerfectPlacement) | 1.2.4 → 1.2.6 | 新增「7 - Key Hints」控制提示的顯示時機、位置與大小；預設提示縮小到 0.7 倍，開選單時隱藏。提示文字可在自動產生的 KeyHints.txt 編輯。修正重新登入後提示變空，以及未安裝模組的連線檢查。 |
| [FirstPersonMode](https://valheim.hexium.gg/mods/Azumatt/FirstPersonMode) | 1.4.5 → 1.4.6 | 修正第一人稱移動時世界與護盾穹頂抖動；第一人稱隱藏鬍鬚與頭髮，影子保留。新增 Idle Sway Deadzone，預設 0.05 公尺，減少站立呼吸造成的鏡頭晃動；設 0 可恢復舊行為。 |
| [QuickTeleport](https://valheim.hexium.gg/mods/OdinPlus/QuickTeleport) | 2.0.5 → 2.0.7 | 修正套件並減少設定同步的背景工作；既有傳送設定保留。 |
| [Extra Snap Points Made Easy](https://thunderstore.io/c/valheim/p/Searica/Extra_Snap_Points_Made_Easy/changelog) | 2.1.1 → 2.2.0 | 新增自訂格線精度、左 Shift 反向切換與目前精度提示；調整傳送門吸附點及與 MVBP 的互動順序。 |

## 建築快捷鍵

新版吸附模組更改了部分預設鍵。這個包保留原有 P（Manual+）及 F11（格線模式），並明確固定普通手動吸附為 CapsLock，延續舊版行為，避開 PerfectPlacement 的 F3 退出鍵。

格線模式下，精度切換從上游舊預設 F4 改為新版 Q；放置／目標吸附點仍用 Q／E。按住左 Shift 可反向循環精度或吸附點。自訂精度清單預設留空，仍使用 1.0／0.5 公尺；需要時可在設定管理器修改。

其他 39 份設定、兩位管理員來源、材料／耐力／耐久／支撐規則與原有內附 TorchMod DLL 保留。除了吸附設定新增 CapsLock，其他既有覆寫值未改；新設定採模組的新版預設，首次啟動時由 BepInEx 補入。

## 最大製作數量補丁

[AAA Crafting](https://valheim.hexium.gg/mods/Azumatt/AAA_Crafting) 仍是 2.1.11，[AzuCraftyBoxes](https://valheim.hexium.gg/mods/Azumatt/AzuCraftyBoxes) 仍是 1.8.28，沒有確認官方已修正 Max 計數問題，因此保留 AAA Crafting Max Fix 1.1.0。

## 安裝與驗證範圍

兩人先正常退出遊戲並備份角色與世界，再匯入 v42 為新 Gale profile，勾選 Import all files。雙人完整包使用 `dist/private/` 的版本；v41 保留在 Git tag 與先前交付資料夾，可供還原。

檢查包括：50 個套件的最新版本比對、六組更新前後下載與 SHA-256、ZIP／manifest、完整依賴、更新模組仍包含原有覆寫設定鍵、profile 差異、歷史版本快照與公開／私人封包重建。反編譯檢查只證明設定鍵及實作存在；Gale GUI 匯入、Unity／Harmony 載入、實際遊戲與雙人連線尚未測試。

首次先在測試世界確認輪盤、PlantEasily 手把操作、第一人稱、建築吸附／快捷鍵、傳送與箱子材料製作，再載入原世界。
