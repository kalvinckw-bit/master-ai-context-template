> [!CAUTION]
> ### ⚡ 嚴禁狹隘單點修改原則（Anti-Silo & Cross-AI Realignment Mandate）
> **任何 AI 新增或修訂任何規則時，嚴禁只改自己專屬的檔案（例如 Claude 嚴禁只改 `CLAUDE.md`）！**
> **必須同時同步更新全套入口公文：`AGENTS.md`、`CLAUDE.md`、`CHATGPT.md`、`DECISIONS.md` 與對應的 `START_SESSION.md` / `END_SESSION.md`！誰發明或修訂規則，誰就必須負全責同步傳達給全體 AI 入口！**

> [!CAUTION]
> ### ⚡ 鋼鐵憲法：開局必 Pull，收工必 Push（Mandatory Git Cloud Sync）
> **1. 任何 AI 執行 `start` 時，第一動作必須自動執行 `git pull --rebase` 拉取 GitHub 雲端最新代碼！**
> **2. 任何 AI 執行 `end` 時，必須自動執行 `git add`、`git commit` 並立即 `git push` 推上 GitHub 雲端！**
> **3. 嚴禁任何 AI 宣稱『不需要 push 到 GitHub』或將 push/pull 留給使用者手動！自動同步雲端是 AI 的基本職責！**
> **4. 全集團專案 Google Drive 鏡像同步鋼鐵憲法（Universal Google Drive Mirror Sync on End）：**
>    - **全集團所有專案在 Google Drive 均有對應實體鏡像目錄（`G:\マイドライブ\Projects\...`）。此同步並非自動，沒有任何 webhook 或排程機制，完全由 AI 每次收工時自主執行！**
>    - **任何 AI 執行 `end` 時，必須：**
>      1. **找出本次 Session 改動過的所有檔案（例如使用 `git diff --name-only <上次同步commit>..HEAD` 或實體狀態比對）。**
>      2. **把每一個改動過的檔案同步更新/複製至 Google Drive 該專案之根目錄鏡像對應路徑。**
>         - ⚠️ **Web / 雲端沙盒環境安全防護**：在無本地掛載磁碟（無 `G:\` 實體路徑）之雲端/Web AI 環境（如 Web 或手機端 Claude）中，**嚴禁調用 Google Drive API 執行破壞性的「刪除檔案（Trash）再重新建立」**！Web 端 AI 收工時只需確保代碼正確 `git add`、`git commit` 並 `git push` 至 GitHub 遠端倉庫；本機桌端（Antigravity）會負責實體磁碟目錄的 1:1 秒級鏡像同步與還原。
>      3. **在收工交接報告（SESSION HANDOFF）中，明確列出「這次同步了哪些檔案、對應到 Drive 哪個路徑或 GitHub Commit」**，嚴禁只寫「已同步」三個字，嚴禁省略！
>      4. **嚴禁跳過這一步、嚴禁假設「應該還是最新的」——忘記檢查=雲端鏡像停擺！**
>    - **5. 三雲同步衝突仲裁鐵律：最新覆蓋舊端（Tri-Drive Arbitrament: "Latest Wins & Auto-Align"）：**
>      - **三大 Drive（OneDrive、Google Drive、GitHub 遠端）基本上保持 1:1 實體對齊。若發生不同步或版本衝突時：**
>      - **唯一仲裁原則：以「時間戳記最新 / 最新 Commit」的一端為準，無條件覆蓋較舊的一端（選一個最新的，然後讓舊的同步）！**
>      - **嚴禁舊版本覆蓋新版本！嚴禁舊代碼倒灌！**
>      - **AI 必須自主比對時間戳記並直接完成同步，嚴禁詢問用戶！**

> [!CAUTION]
> ### ⚡ Master AI Context 雙雲同步法則（Antigravity Master Dual-Cloud Sync Mandate）
> **任何 AI（特別是 Antigravity AI）在修訂 Master AI Context (`00 Master AI Context Template`) 時：**
> **1. 必須同時修改本機兩大雲端目錄：**
>    - `C:\Users\kalvi\OneDrive\Projects\00 Master AI Context Template\` (OneDrive)
>    - `G:\マイドライブ\Projects\00 Master AI Context Template\` (Google Drive)
> **2. 必須進行 Byte / SHA256 實體比對，確保 OneDrive 與 Google Drive 兩邊之 Master Context 100% 絕對一致！**
> **3. 必須同時執行 `git commit` 並 `git push origin main` 推送至 GitHub `kalvinckw-bit/master-ai-context-template`！**

> [!CAUTION]
> ### ⚡ 跨平台路徑防禦鋼鐵憲法（Strict Path Quoting & Zero Unix Backslash Escape Mandate）
> **全體 AI 在 Windows / OneDrive / 跨平台處理路徑、檔案操作與執行腳本時：**
> 1. **強制使用雙引號包裹包含空格之路徑**：
>    - 凡路徑包含空格，必須一律使用半形雙引號完整包裹（例如 `"C:\Users\kalvi\OneDrive\Projects\Voice Out Enterprise"`、`"Voice Out Enterprise"`）。
> 2. **嚴禁 Unix 反斜線跳脫空格**：
>    - 嚴禁在跨平台腳本或命令列中使用 Unix 反斜線跳脫空格（例如嚴禁 `Voice\ Out` 或 `Voice\ Out\ Enterprise`）。在 Windows 檔案系統與 PowerShell 中，`\` 為路徑分隔符號，隨意使用 `\ ` 會導致字串被錯誤解析。
> 3. **嚴禁在路徑與檔名中出現任何 HTML 實體編碼**：
>    - 嚴禁在任何檔案系統呼叫、Git 指令、建立目錄 API 中使用 HTML 實體字元（例如 `&#x5c;`、`&amp;`、`&#32;`、`%20` 等）。違者會直接在 Windows 磁碟產生如 `Voice&#x5c; Out&#x5c; Enterprise` 等幽靈資料夾，污染 OneDrive 與 Google Drive 雲端同步！
> 4. **幽靈目錄自動巡檢自癒義務**：
>    - 任何 AI 執行 `start` 或日常操作時，若發現含有 `&#` 之幽靈資料夾，必須主動將其安全移除並糾正路徑，嚴禁將幽靈資料夾提交至 Git 或同步至雲端。

> [!CAUTION]
> ### ⚡ 移動端防快取與 UI 禁存 Cookie/Storage 鋼鐵憲法（Zero Mobile Cache & Fresh UI Mandate）
> **手機瀏覽器（iOS Safari / Android Chrome）沒有電腦的「強制重新整理（Ctrl + F5）」功能，極易陷入快取地獄導致 UI 無法更新、永遠停留舊版！全體 AI 必須嚴格執行以下鐵律：**
> 1. **嚴禁將 UI 狀態或 HTML 結構存入 Cookie / LocalStorage / SessionStorage**：
>    - 嚴禁利用 Cookie 或 Web Storage 暫存整頁 HTML、UI 元件佈局或過期靜態資料。
>    - Cookie 與 Storage 僅限用於儲存必要的驗證 Token、語系偏好（純代碼如 `"zh"`）或主題名稱，嚴禁存放任何阻礙手機讀取最新 DOM 與即時數據之快取。
> 2. **所有 Web 專案的 `firebase.json` 強制配置防快取 HTTP 標頭**：
>    - 任何部署至 Firebase Hosting 的專案，其 `firebase.json` 必須對 `**/*.html` 與 `**/*.json` 強制配置：
>      - `Cache-Control`: `no-cache, no-store, must-revalidate, max-age=0`
>      - `Pragma`: `no-cache`
>      - `Expires`: `0`
> 3. **所有 HTML 檔案檔頭強制包含防快取 Meta 標籤**：
>    ```html
>    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
>    <meta http-equiv="Pragma" content="no-cache">
>    <meta http-equiv="Expires" content="0">
>    ```
> 4. **外掛 JS / CSS 強制版本號防快取（Cache Busting）**：
>    - 引用外掛 JS / CSS 時必須帶有版本號或時間戳參數（例如 `app.js?v=20260913` 或打包 hash），禁止無版本號裸引用。
> 5. **嚴禁 Service Worker 攔截 HTML 造成離線僵屍快取**：
>    - 使用 Service Worker（如 FCM）時，嚴禁對 HTML 頁面進行快取攔截，必須嚴格採用 Network Only，防止手機關閉分頁重開依然讀到快取舊版。

> [!IMPORTANT]
> ### 👑 核心啟動指令：開局必讀集團 Master AI Context（Master SSoT Sync）
> **每次執行 `start` 或開啟新 Session 時，AI 必須首先讀取 Master AI Context，以對齊最新的集團架構與全域政策：**
> 1. 📖 `C:\Users\kalvi\OneDrive\Projects\00 Master AI Context Template\AI_CONTEXT\GROUP_GLOBAL_STATUS.md`（集團中央總指揮儀表板）
> 2. 📖 `C:\Users\kalvi\OneDrive\Projects\00 Master AI Context Template\AI_CONTEXT\DECISIONS.md`（集團最高決策記錄）
> 3. 📖 `C:\Users\kalvi\OneDrive\Projects\00 Master AI Context Template\AI_CONTEXT\COMPANY_PROFILE.md`（集團統一企業畫像）
> **對齊集團最新指示後，方可繼續執行本地專案之 `AI_CONTEXT/START_SESSION.md`！**

# Universal AI Agent Governance Protocol (Master SSoT)
> [!CAUTION]
> ### ⚡ AI 行動憲法：主動自主執行原則（Zero Homework for User）
> **AI 必須自主調用工具完成所有可自動化之任務（CLI、雲端開通、腳本、代碼、Git），嚴禁將 AI 有權限執行的操作推給用戶手動點擊或手動修改！**
> 只有真人 2FA 驗證或重大商業決策才可向用戶請求。

> [!IMPORTANT]
> ### 🏆 核心治理背景：多 AI 輪替與跨平台「接力棒（Relay Handover）」系統
> **本專案的核心工作流哲學：**
> 1. **多 AI 輪替開發（Quota Exhaustion Fallback）**：開發者會在多個 AI（Claude、Google Antigravity、ChatGPT、Codex）之間頻繁切換，以因應各平台用量配額（Quota）耗盡或工具特性。
> 2. **跨平台開發（Cross-Platform Mobility）**：開發者會在不同設備（Windows 工作站、MacBook 筆電、Web 雲端）之間移動作業。
> 3. **無縫接力棒交接（Relay Baton Protocol）**：因為不同 AI 與平台之間「不會自動即時同步」，所以每一位 AI 必須嚴格執行 **`start`（接棒/對齊最新雲端進度）** 與 **`end`（交棒/紀錄做過與必做事項並自動 Push）**，確保下一位接手的 AI 隨時能 100% 無縫接續，絕不拿舊代碼覆蓋新代碼！

This project uses the unified Multi-AI Single Source of Truth (SSoT) governance framework.
All AI assistants (Antigravity, Claude Code, ChatGPT, Codex, Cursor, Gemini) collaborating on this codebase MUST strictly comply with these rules.

## Core Mandates:
1. **Mandatory Lifecycle**:
   - Begin every session by executing `start` as defined in [AI_CONTEXT/START_SESSION.md](AI_CONTEXT/START_SESSION.md).
   - End every session by executing `end` as defined in [AI_CONTEXT/END_SESSION.md](AI_CONTEXT/END_SESSION.md).
2. **Identity & Record Isolation**:
   - Identify your exact environment upon startup (`[AI Name] ([Host: Desktop / VS Code], [Device: Windows / MacBook])`).
   - Own, read, and write ONLY your designated session file in `AI_CONTEXT/SESSIONS/`. Never edit another AI's session file.
3. **Single Source of Truth (SSoT)**:
   - The `AI_CONTEXT/` directory is the single source of truth for project architecture, active status, decisions, and todos.
4. **Fact vs. Inference Distinction**:
   - If a feature or integration is not proven by live run logs or direct file inspection in the current session, it MUST be labeled as `[Inferred from code, not yet verified]`. Never present assumptions as verified facts.
5. **Decisions are Permanent**:
   - `AI_CONTEXT/DECISIONS.md` records permanent architectural and design decisions. Never revert or re-debate approved decisions without explicit user instruction.
6. **Automatic Git Synchronization**:
   - `start` automatically performs `git pull --rebase` to ensure latest code.
   - `end` automatically commits and pushes the session records and code changes to the remote repository.


> [!NOTE]
> ### 🛡️ 用戶情報採集規範（Maximum Telemetry Policy）
> **所有前端專案在用戶登入與會話中，必須透過 ck-telemetry.js 自動採集用戶全部可獲取之情報（IP、Geo、Device、OS、螢幕、CPU/RAM、語言、時區、來源），並即時寫入 Firestore users/{uid}/telemetry_logs。**


### Action: sync (或 sync master)
當使用者在對話途中輸入 sync 或 sync master 時：
1. **立即重新讀取 Master SSoT**：
   - 📖 C:\\Users\\kalvi\\OneDrive\\Projects\\00 Master AI Context Template\\AI_CONTEXT\\GROUP_GLOBAL_STATUS.md
   - 📖 C:\\Users\\kalvi\\OneDrive\\Projects\\00 Master AI Context Template\\AI_CONTEXT\\DECISIONS.md
   - 📖 C:\\Users\\kalvi\\OneDrive\\Projects\\00 Master AI Context Template\\AI_CONTEXT\\COMPANY_PROFILE.md
2. 比對是否有最新集團決策、全域架構或基礎設施變更。
3. 在當前對話中即時套用最新政策（不中斷、不關閉 Session）。
4. 簡短回報：=== MASTER SYNC COMPLETED === 與對齊之最新變更要點。