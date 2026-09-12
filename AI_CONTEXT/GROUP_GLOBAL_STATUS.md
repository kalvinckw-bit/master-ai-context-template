# CK Holdings Central Group Dashboard (GROUP_GLOBAL_STATUS.md)
**Last Updated**: 2026-09-12 23:15 JST  
**SSoT Authority**: `C:\Users\kalvi\OneDrive\Projects\00 Master AI Context Template\AI_CONTEXT\GROUP_GLOBAL_STATUS.md`

---

## 🚀 集團各專案即時進度與狀態矩陣

### 🏛️ 【CK Holdings 集團官方核心事業體】（對外公開 / 集團資產）

| 專案名稱 | 實體路徑 | 負責領域 | 核心技術 / 雲端目標 | 目前狀態 |
| :--- | :--- | :--- | :--- | :--- |
| 🏢 **CK Holdings 官方門戶** | `CK Holdings\ck-holdings-web` | 集團頂層門戶、整合 6 大產品子頁面 | Firebase `ck-holdings` | 🟢 2026-09-12 已上線，整合 6 大子頁面全部 200 OK |
| 📣 **Voice Out Web / App** | `Voice Out Enterprise\VoiceOutWeb` | 地圖雷達、群組通訊、即時定位、廣告 | Firebase `voiceout-asia` (`(default)` DB) | 🟢 運行中 / 已移回根目錄同級，docs 法定文件完備 |
| ✨ **ChristyKalvin Web** | `ChristyKalvinWeb` | 全球精品商城、日本代購、即時匯率工具 | Firebase `christykalvin-web` (`christykalvin-db`) | 🟢 運行中 / 專屬聚焦 shopping 與 forex |
| 🏠 **Cari Rumah** | `CK Holdings\Cari Rumah` | 馬來西亞視覺化房地產地圖與決策平台、Telegram 房源同步 | Python / Telegram Sync / `christykalvin-db` | 🟡 8 筆 Telegram 草稿待審核（前端已整合至 ck-holdings.my/cari-rumah.html） |
| 🛍️ **Sougu (Crosspath)** | `CK Holdings\Crosspath (Sougu)` | 日本商品搜購、空間社交源碼庫 | 前端已整併至 `ck-holdings.my/sougu.html` | ⚪ 獨立域名放棄，前端整合至總門戶 |
| 💻 **Meta Office** | `CK Holdings\Meta Office` | 2D 像素沉浸式虛擬企業辦公空間素材庫 | 前端已整併至 `ck-holdings.my/metaoffice.html` | ⚪ 獨立域名放棄，前端整合至總門戶 |
| 📋 **00 Master AI Template** | `00 Master AI Context Template` | 集團憲法母版 | Markdown SSoT | 🟢 最新同步 |

---

### ⏳ 【集團內部儲備 / 暫不公開項目】（Internal / On Hold）

| 專案名稱 | 實體路徑 | 負責領域 | 備註說明 | 目前狀態 |
| :--- | :--- | :--- | :--- | :--- |
| ☕ **Smart Laundromat + Cafe** | `Laundry + Cafe` | 新山智慧物聯網無人洗衣與精品咖啡複合實體旗艦 | 實體門市商業項目，創辦人指示暫時 Hold，**不公開、不列入官網** | ⚪ 暫緩保留中 (On Hold) |

---

### 👤 【創辦人 Kalvin 個人私有工具與資產】（Private / Non-Corporate）
> ⚠️ **嚴格防護警語**：以下項目為 Kalvin 創辦人個人私有工具與投資資產，**不屬於 CK Holdings 控股公司事業體，嚴禁放上集團官網或當作公開業務介紹**！

| 專案名稱 | 實體路徑 | 負責領域 | 核心技術 | 目前狀態 |
| :--- | :--- | :--- | :--- | :--- |
| 📢 **Facebook Auto Post** | `Facebook Auto Post` | 個人社群行銷自動化發文腳本 | Python / Playwright / Graph API | 🟢 個人私有運行中 |
| 🪙 **Luno Trading Bot** | `Python\luno-btc-myr-trading-bot` | 個人比特幣量化交易演算法與資產機器人 | Python / Luno API | 🟢 個人私有運行中 |

---

## 🌐 集團長遠 3 大核心網域矩陣 (3 Core Strategic Domains)
1. 🏢 **`ck-holdings.my`** ➔ Firebase Site `ck-holdings` (Cloudflare Zone: `fb33e91d1d1fb81f3b61de1769167e75`)
   - **收斂整合 6 大子頁面**：`/cari-rumah.html`、`/creditcard.html`、`/jpcreditcard.html`、`/dead-man-switch.html`、`/metaoffice.html`、`/sougu.html`
   - **企業信箱**：`kalvin@` / `admin@` ➔ `kalvin.ckw@outlook.jp` (✅ 2026-09-12 啟用)
2. ✨ **`christykalvin.com`** ➔ Firebase Site `christykalvin-web` (Cloudflare Active)
   - **核心頁面**：`/forex.html`、`/shopping.html`、`/shopping-admin.html`
   - **企業信箱**：`kalvin@` / `admin@` ➔ `kalvin.ckw@outlook.jp`
3. 📣 **`voiceout.asia`** ➔ Firebase Site `voiceout-asia` (Cloudflare Active)
   - **核心頁面**：`/index.html`、`/chat.html`、`/admin.html`、`/merchant.html`
   - **企業信箱**：`kalvin@` / `admin@` ➔ `kalvin.ckw@outlook.jp`

- 備註：`ck-holdings.com.my` ➔ Exabytes 審核開通中（預備接軌 Cloudflare）
- `sougu.online` ➔ Firebase `sougu-online` ｜ 信箱：`kalvin@` / `admin@` ➔ `kalvin.ckw@outlook.jp`

---

## ⚡ AI 行動指引（Zero Dumb Questions & Dual-Cloud Parity）
任何 AI 在接手任何 Session 時：
1. **直接讀取本檔案** 掌握全集團全貌。
2. 進入目標資料夾讀取 `AI_CONTEXT/TODO.md` 與 `AI_CONTEXT/CURRENT_STATUS.md`。
3. **開局必 Pull，收工必 Push**，並嚴格執行 **Google Drive 鏡像同步**（全集團專案在 `G:\マイドライブ\Projects\...` 皆有鏡像，AI 必須在收工時將修改檔案同步上傳並於報告附上詳細清單）。
4. **Master AI Context 修改原則**：若修改 Master AI Context，必須同時更新 OneDrive 與 Google Drive 兩端並比對 Hash！
5. 主動執行任務並自動 Push，嚴禁推託或詢問「連線在不在」等問題！
6. **跨平台路徑防禦鋼鐵律**：路徑含空格必須一律用半形雙引號包裹，嚴禁 Unix 反斜線跳脫（嚴禁 `\ `），嚴禁在路徑中注入 HTML 實體字元（如 `&#x5c;`），發現幽靈目錄必須主動清除自癒！