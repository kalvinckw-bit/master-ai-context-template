# CK Holdings Central Group Dashboard (GROUP_GLOBAL_STATUS.md)
**Last Updated**: 2026-09-10 23:48 JST  
**SSoT Authority**: `C:\Users\kalvi\OneDrive\Projects\00 Master AI Context Template\AI_CONTEXT\GROUP_GLOBAL_STATUS.md`

---

## 🚀 集團各專案即時進度與狀態矩陣

| 專案名稱 | 實體路徑 | 負責領域 | 核心技術 / 雲端目標 | 目前狀態 |
| :--- | :--- | :--- | :--- | :--- |
| 📣 **Voice Out Web** | `CK Holdings\Voice Out Enterprise\VoiceOutWeb` | 地圖雷達、群組通訊、即時定位、廣告 | Firebase `voiceout-asia` (`(default)` DB) | 🟢 運行中 / 最新部署已上線 |
| ✨ **ChristyKalvin Web** | `ChristyKalvinWeb` | 日本代購轉運、PetaRumah 房產前端 | Firebase `christykalvin-web` (`christykalvin-db`) | 🟢 運行中 / 房產前端已就緒 |
| 🏠 **Peta Rumah** | `CK Holdings\Peta Rumah` | 馬來西亞房源同步、人工策展後台 | Python / Telegram Sync / `christykalvin-db` | 🟡 8 筆 Telegram 草稿待 CK 於 admin.html 審核（後台登入權限尚未 bootstrap） |
| 🛍️ **Sougu (Crosspath)** | `Crosspath (Sougu)` | 日本商品搜購、在地採購服務 | Firebase `sougu-online` (`sougu-db`) | 🟢 架構已綁定 |
| 📢 **Facebook Auto Post** | `Facebook Auto Post` | FB 粉絲團自動化行銷發文 | Python / Playwright / Graph API | 🟢 運行中 |
| 🏢 **Meta Office** | `Meta Office` | 元宇宙虛擬辦公室 | HTML5 / Canvas / WebRTC | 🟢 就緒 |
| 🪙 **Luno Trading Bot** | `Python\luno-btc-myr-trading-bot` | 比特幣量化交易機器人 | Python / Luno API | 🟢 運行中 |
| 📋 **00 Master AI Template** | `00 Master AI Context Template` | 集團憲法母版 | Markdown SSoT | 🟢 最新同步 |

---

## 🌐 網域與企業郵件路由矩陣
- `voiceout.asia` ➔ Firebase `voiceout-asia` ｜ 信箱：`kalvin@` / `admin@` ➔ `kalvin.ckw@outlook.jp`
- `christykalvin.com` ➔ Firebase `christykalvin-web` ｜ 信箱：`kalvin@` / `admin@` ➔ `kalvin.ckw@outlook.jp`
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