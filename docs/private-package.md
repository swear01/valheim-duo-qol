# 雙人私人包的固定設定

雙人包交付必須沿用固定的私人管理員設定，不從公開版本推測帳號，也不只依靠聊天紀錄或某次 outputs。設定存於本機 `~/.config/valheim-duo-qol/private-admins.json`，只讓擁有者讀寫；公開 repo 保存打包方法，不保存真實玩家 ID。

在 repository 根目錄執行：

```sh
python3 -m scripts.build_private_package
```

它先核對並重建目前正式版本，再加入本機的 Badgers Straight Structures 0.6.0 原始 DLL、把兩位管理員寫入 `BepInEx/config/permissions.yaml`、開啟 `Automatic devcommands`，輸出 `dist/private/Valheim-Duo-QoL-v版本.r2z`。檔名與 profile 沿用正式版本，不加私人版尾碼；公開包在 `dist/`，兩人交付使用 `dist/private/` 內的包。Badgers 使用作者預設 `Warp Amount = 0.004`，修平所有建材的視覺扭曲，沒有石材限定選項；它不修改碰撞、耐久或支撐。其他設定、模組版本與內附檔案保留；免費建造、支撐與耐久設定沿用正式版本。兩人匯入新 profile 並勾選 Import all files；若已有同名 profile，先備份並在 Gale 另取名稱，避免覆蓋。

Badgers DLL 存於本機 `~/.config/valheim-duo-qol/BadgersStraightStructures.dll`。換機或檔案遺失時，從 [Nexus Files](https://www.nexusmods.com/valheim/mods/2938?tab=files) 下載 0.6.0，將 ZIP 內的同名 DLL 放回此位置；SHA256 必須是 `d06750ea8d458ac92bcaaf2dcf9a6034af65b8452740f792ca996ba0a253a2ce`。作者禁止重新上傳，DLL 與含它的私人包不得放進公開 repo、其他模組站或 Actions artifacts。只裝客戶端，不裝專用伺服器。

私人設定檔缺失、格式不正確、不是兩個不同 Steam 帳號，或 Badgers DLL 缺失／雜湊不符時，打包會失敗。此時應恢復私人設定，不能把公開包當成已包含雙人管理員的版本交付。

設定檔的 JSON 結構是 `admins` 陣列，每筆有 `id`（完整 `Steam_` 加 SteamID64）與 `name`（顯示名稱）；實際帳號只存本機私人檔。不要把私人檔、私人封包或含 ID 的 lock／驗證紀錄加入 Git 或公開 Actions artifacts。

目前設定保存在這台機器，沒有雲端備份。換機時需安全帶走這份私人檔，並重新下載 Badgers；只有公開 repo 無法還原玩家名單或 DLL。封包驗證不代表遊戲內管理員授權或雙人相容性已實測。
