# 雙人私人包的固定設定

雙人包交付必須沿用固定的私人管理員設定，不從公開版本推測帳號，也不只依靠聊天紀錄或某次 outputs。設定存於本機 `~/.config/valheim-duo-qol/private-admins.json`，只讓擁有者讀寫；公開 repo 保存打包方法，不保存真實玩家 ID。

在 repository 根目錄執行：

```sh
python3 -m scripts.build_private_package
```

它先核對並重建目前正式版本，再把本機兩位管理員寫入 `BepInEx/config/permissions.yaml`、開啟 `Automatic devcommands`，輸出 `dist/Valheim-Duo-QoL-v版本-private-admins.r2z`。其他設定、模組版本與內附檔案保留；免費建造、支撐與耐久設定沿用正式版本。私人包使用獨立 profile 名稱，兩人匯入新 profile 並勾選 Import all files。

私人設定檔缺失、格式不正確或不是兩個不同 Steam 帳號時，打包會失敗。此時應恢復私人設定，不能把公開包當成已包含雙人管理員的版本交付。

設定檔的 JSON 結構是 `admins` 陣列，每筆有 `id`（完整 `Steam_` 加 SteamID64）與 `name`（顯示名稱）；實際帳號只存本機私人檔。不要把私人檔、私人封包或含 ID 的 lock／驗證紀錄加入 Git 或公開 Actions artifacts。

目前設定保存在這台機器，沒有雲端備份。換機時需安全帶走這份私人檔；只有公開 repo 無法還原玩家名單。封包驗證不代表遊戲內管理員授權或雙人相容性已實測。
