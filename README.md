# Valheim 雙人便利模組包

給兩人一起玩的 Valheim 1.x QoL 模組包，一人開世界、另一人加入。使用 Gale 從 Thunderstore／Hexium 下載模組。

目前版本 **v61**（2026-10-18）：更新 ExtraSlots 1.2.21 與 SkilledCarryWeight 1.6.1，遷移負重設定；保留 10 公尺拾取、整排種植與已停用的除錯快捷鍵。51 個線上套件、42 份公開設定；雙人私人包另含 Badgers Straight Structures 0.6.0 與兩位管理員。

## 安裝

1. 兩人正常退出遊戲，備份角色與世界。
2. 下載 [v61 模組包](history/v61/Valheim-Duo-QoL-v61.r2z)，在 Gale 匯入為新 profile，勾選 **Import all files／匯入所有檔案**。
3. 等待下載完成；兩人使用同一版本，先在測試世界確認後再載入原世界。

首次安裝需要網路；舊版套件能否繼續下載，取決於上游是否保留。

[採收與拾取](docs/farming.md) · [自動續吃](docs/auto-eat.md) · [舒適度家具](docs/comfort.md) · [生存建築](docs/survival-building.md) · [船隻與地圖標記](docs/map-pins.md) · [搬移建築](docs/moving-buildings.md) · [建材與船身數字](docs/hover-stats.md) · [/back 返回](docs/back-command.md) · [更新紀錄](CHANGELOG.md) · [版本來源與歷史說明](docs/history.md) · [版本 tags](https://github.com/swear01/valheim-duo-qol/tags)

`profile/` 是這一版的可比較內容，`lock.json` 保存版本／來源／設定紀錄。主分支只保留最新 `history/v61/` 的包與 lock；舊版原始 ZIP／lock 保留在各版 tag，可切換 tag 下載或還原。

[GitHub Actions](https://github.com/swear01/valheim-duo-qol/actions/workflows/verify.yml) 在 push、PR 或手動 Run workflow 時，會驗證所有版本，再從 `profile/` 重建目前的 `.r2z`，確認 SHA256 與封存完全相同才提供下載，保留 30 天（下載需登入 GitHub）。本機在 repository 根目錄執行 `python3 -m scripts.build_package`，產物在 `dist/`。新增版本仍需一併更新封存、lock、版本紀錄與 tag；Actions 不會自動更新模組或改動版本。

完整包的遊戲內、雙人與長時間行為尚未全面實測；歷史封存與靜態檢查不代表遊戲相容性驗證。

維護雙人私人包時，必須沿用本機固定的私人管理員設定，執行 `python3 -m scripts.build_private_package`；缺少私人設定或 Badgers 原始 DLL 時停止私人交付，不退回公開包。設定位置、換機與隱私界線見 [私人包維護](docs/private-package.md)。

內附模組授權與來源見 [THIRD_PARTY.md](THIRD_PARTY.md)。
