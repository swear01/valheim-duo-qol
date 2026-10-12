# 歷史來源

這個 Git repository 在 2026-10-12 從已保存的正式 `.r2z` 與 lock 重建。每一個版本有一個 commit 與同名 tag；Git commit 時間是匯入時間，原始交付日期另記於 `history/versions.json`，沒有回填或虛構舊 commit 時間。

每版的 `profile/` 與該版 `.r2z` 解壓內容逐位元組相同；歷史 ZIP、lock 也保留原始位元組。v1～v6 的舊 lock 沒有記錄 ZIP digest，因此它們的 ZIP SHA-256 是這次匯入時計算；v7 起則另核對原 lock 內已記錄的 ZIP SHA-256。

所有版本的來源是既有交付產物，不含角色、世界、私人 token 或測試 profile。Git diff 可以比較套件清單與設定；舊版的安裝與遊戲相容性仍依當時上游狀態而定。
