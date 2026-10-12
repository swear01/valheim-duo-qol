# 歷史來源

這個 Git repository 在 2026-10-12 從已保存的正式 `.r2z` 與 lock 重建 v1～v34。這些版本各有一個 commit 與同名 tag；Git commit 時間是匯入時間，原始交付日期另記於 `history/versions.json`，沒有回填或虛構舊 commit 時間。v35 起直接在此 repository 更新 profile、保存交付 ZIP／lock 並建立版本 tag。

每版的 `profile/` 與該版 `.r2z` 解壓內容逐位元組相同；歷史 ZIP、lock 也保留原始位元組。v1～v6 的舊 lock 沒有記錄 ZIP digest，因此它們的 ZIP SHA-256 是這次匯入時計算；v7 起則另核對原 lock 內已記錄的 ZIP SHA-256。

v1～v34 的來源是既有交付產物；後續版本沿用相同的 ZIP／lock 與 profile 快照驗證。repository 不含角色、世界、私人 token 或測試 profile。Git diff 可以比較套件清單與設定；舊版的安裝與遊戲相容性仍依當時上游狀態而定。

## 同名 v21 的來源判定

曾有一份從 CLI 工作目錄的舊 v20 基底誤產生的 v21，添加了 ValheimCli，後來已撤回。正式 v21 使用含 PortalGhostFix 與負重調整的產物；v27 才在正確的 v26 基底加入 ValheimCli。同名撤回檔的摘要保存在 `history/rejected-artifacts.json`，沒有把它建立成正式版本 tag。

## 驗證

執行 `python3 scripts/verify_history.py`，核對全部原始 ZIP／lock 雜湊、套件 pins／依賴、設定、每個 tag 的 profile 快照與線性版本關係。GitHub Actions 使用相同檢查。

原始 CFG 的尾端空白與空行也屬於保存的位元組；它們不在匯入時重新格式化。一般程式與文件的 whitespace 檢查單獨執行；原始 profile 以 ZIP 雜湊及逐位元組快照比對驗證。

這些檢查不會啟動 Valheim，也不重建或更新歷史套件。角色、世界與私人 token 不在 repository 內。
