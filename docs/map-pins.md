# 地圖動態標記

v38 將現有 [HUDCompass 1.2.1](https://valheim.hexium.gg/mods/Neobotics/HUDCompass) 的 `F - Dynamic Pins / Show dynamic pins on map` 預設改為 `true`，讓船隻、推車與傳送門的動態標記可出現在大地圖和小地圖；各類型仍由 `G - Dynamic Types` 控制，作者的 `Show Ships` 預設為 `true`。

兩人退出遊戲後，把 v38 匯入 Gale 的新 profile，勾選 **Import all files／匯入所有檔案**。這個設定受房主控制，房主與加入者都應使用同版設定。原有羅盤動態標記保持開啟。

也可在現有 profile 按 F10，找到 HUDCompass 的 `F - Dynamic Pins`，將 `Show dynamic pins on map` 設為 `true`；若選項被鎖定，由房主調整。若仍看不到船，確認 `G - Dynamic Types / Show Ships` 開啟，先靠近船再觀察大地圖與小地圖。這不代表所有未載入區域的船都會即時更新。

本次只改地圖開關；47 個套件版本、其他 37 份設定與內附 DLL 不變，MovingDay 的左 Ctrl 地形搬移設定保留。

已核對公開 1.2.1 套件雜湊、設定綁定與船隻分類預設，並檢查新包只改 HUDCompass 的地圖設定值。尚未完成 Gale GUI 匯入、遊戲內船隻標記、兩人同步與重載測試；目前運行的 profile、角色與世界未改動。
