# 採收與拾取

v60 加入 [Super Configurable Pickup Radius 1.1.2](https://thunderstore.io/c/valheim/p/TastyChickenLegs/SuperConfigurablePickupRadius/)，將人物的自動拾取範圍設為 10 公尺。它吸取已掉落在地上的物品，不會自行採收未成熟或尚未互動的作物；背包空間、負重及原版拾取限制仍生效。其他種類的附近掉落物也可能被拾取。

兩人正常退出遊戲後，在 Gale 匯入同一份 v60 私人包為新 profile，勾選 Import all files，再重新啟動遊戲。拾取模組在人物建立時套用範圍，不能只改設定後留在目前遊戲中等待生效。

## PlantEasily 網格

`Grid / GloballyAlignGridDirections = false`：關閉對齊世界方向。新的、未吸附既有作物的陣列，改依人物到放置點的方向排列。靠近舊作物時，Intelligent 吸附仍可能沿用既有網格方向；已種下的作物不會被移動或重新排列。

保留 `SnapActive = true`、5×5 整排種植、右 Shift 調整排列、左 Shift 輔助範圍採收、5 公尺採收半徑及自動補種。材料、體力、耐久與防重疊設定保留。

## 設定與確認

在 F10 設定中，SuperConfigurablePickupRadius 的 `Insanely Configurable / Enable Pickup Range` 為 true，`Pickup Range` 為 10。這是人物拾取距離；建築攝影機的獨立拾取範圍仍沿用原設定。

先在測試區採收少量作物，確認地上物品能從較遠處進入背包；再在遠離舊作物的空地轉動人物，確認新網格不再固定世界方向。

已核對原始 ZIP、manifest、依賴、DLL 的設定鍵與 1～10 公尺限制、人物建立時的套用路徑，以及 PlantEasily 的方向判斷。尚未實測 Gale 匯入、10 公尺拾取、新網格方向或雙人同步；另行提到的重疊／扣料異常未在本次重現或修改。
