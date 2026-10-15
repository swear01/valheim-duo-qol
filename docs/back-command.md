# /back 回死亡位置

v43 加入獨立的 SlashBack Return Fix 1.0.0，保留原版 SlashBack 1.0.2。取消使用後 120 秒冷卻與死亡後 120 秒期限；連續死亡、超過兩分鐘或已返回過，都能再次使用。

死亡重生後，在聊天輸入 `/back`，關閉聊天並站著等 5 秒；移動會取消。F5 主控台也可輸入 `back`。仍須有死亡位置紀錄，不需要管理員或 devcommands 權限。

目的地仍是最近一次死亡的位置。如果取屍途中又死亡，它會回第二次死亡的位置，並不會自動挑有裝備的墓碑。

## 更新

兩人正常退出遊戲後，匯入 v43 為新 Gale profile，勾選 **Import all files**，再重新啟動。完整雙人包使用 `dist/private/` 的版本，沿用固定管理員設定。

已有 v42 時，也可在退出遊戲後，把修補 ZIP 內的 `BepInEx/` 複製到同一個 Gale profile 根目錄。保留原本 SlashBack；同一 profile 只放一份 `SlashBackFix.dll`。不需要改世界或角色存檔。

啟動日誌應出現：`SlashBack cooldown and death expiry removed; 5s countdown and movement cancellation retained.` 若顯示版本不符或套用失敗，代表修補沒有啟用，原模組的限制仍在。

## 原因與驗證

原版把「本次使用過」、「超過死亡期限」與冷卻旗標交互使用；第二次死亡若仍在冷卻，載入時會跳過解除過期旗標。修補依要求取消兩個時間限制，並清除成功返回後重新寫入的冷卻／過期狀態；原版 DLL、死亡位置來源、站立倒數及移動判定保留。重生提示也改為沒有冷卻或期限。

修補只支援已核對的 SlashBack 1.0.2；其他版本會警告並停止套用。退出遊戲後移除 `BepInEx/plugins/swear-SlashBackFix/` 並重啟，即恢復原版行為。

已執行狀態回歸測試、原版 DLL 雜湊／欄位／方法／倒數檢查，以及完整包重建。尚未測試 Unity／Harmony 實際掛接、遊戲或雙人返回。原版以座標相除判定移動的零座標誤判不在這次修改內。
