# 舒適度家具

v51 加入 Hexium 的 [ComfortTweaks 3.3.11](https://valheim.hexium.gg/mods/Smoothbrain/ComfortTweaks)。兩人退出遊戲，在 Gale 匯入 v51 為新 profile，勾選 Import all files。

家具舒適度判定半徑為 **50 公尺**，原預設為 10 公尺；家具清單使用相同範圍。其他舒適度點數、家具分組、休息增益、遮蔽要求與火源範圍維持模組預設。家具放得更遠仍能計入舒適度，不會因此擴大火源的保暖範圍。

進入世界後按 **Home** 開關清單；Mac 可按 **Fn＋左方向鍵**。這個鍵避開 ValheimTerrainTools 的 F6 取樣高度。清單列出提供舒適度的家具、點數與群組，缺少的家具以紅色顯示；預設只列出已解鎖、可以建造的缺少家具，每 3 秒更新。相同群組通常只計最高值，不是每件相加。

設定檔為 `BepInEx/config/xyz.alcan.comfortcalc.cfg`。本包只覆寫 `2. Resting / Comfort Range = 50`、`5. Comfort Pieces List / Show Comfort Pieces List = true` 及 `Toggle Visibility = Home`；其餘由模組首次啟動產生預設值。清單首次進入世界時隱藏，按 Home 顯示。

已核對官方套件與實際 DLL 的設定鍵、允許範圍、清單邏輯和封包內容；未啟動遊戲，尚未實測 Gale 匯入、50 公尺邊界、清單版面、效能或雙人同步。
