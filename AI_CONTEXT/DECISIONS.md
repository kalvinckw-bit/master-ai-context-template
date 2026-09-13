# Constitutional Project Decisions Registry (DECISIONS.md)

This document records permanent architectural, design, and policy decisions approved by the user.
**DECISIONS ARE PERMANENT AND CONSTITUTIONAL.** No AI may revert, modify, or re-debate approved decisions without explicit user instruction.

---

### Decision 001: Multi-AI Governance & Session Lifecycle
- **Date**: {{DATE}}
- **Status**: APPROVED
- **Context**: The project is developed across multiple machines (MacBook, Windows) and multiple AI tools.
- **Rule**:
  1. All AIs must begin with `start` and conclude with `end`.
  2. Each AI maintains only its own designated file under `AI_CONTEXT/SESSIONS/`.
  3. `end` automatically commits and pushes session records and changes to Git remote.

### Decision 002: Architecture & Code Standards
- **Date**: {{DATE}}
- **Status**: APPROVED
- **Rule**: All source code must adhere strictly to the tech stack and guidelines defined in `PROJECT_OVERVIEW.md`.

---

### Decision: CK Holdings Group Unified Authentication & Cloud Architecture (集團一號通與中央雲端架構)
- **Status**: APPROVED
- **Date**: 2026-08-29
- **Context**: CK Holdings operates multiple brand portals and services (Voice Out, Sougu / Crosspath, ChristyKalvin, etc.). To prevent user registration fatigue and simplify cross-brand infrastructure, all services must share a single Master Authentication system.
- **Rule**:
  1. **Master Project Identity**: The Firebase Master Project is `CK Holdings` (Project ID: `voiceout-asia`).
  2. **Single Sign-On (One Auth)**: All frontend websites and apps (`voiceout.asia`, `sougu.online`, `christykalvin.com`, etc.) share the same Firebase Authentication instance. Users register once and maintain a consistent UID across the entire group.
  3. **Multi-Database Partitioning**: Business data for distinct brands is physically isolated using dedicated Firestore Database instances under the same Master Project:
     - `(default)`: Voice Out Web / Mobile App
     - `sougu-db`: Sougu (Crosspath)
     - `christykalvin-db`: ChristyKalvin Official Web
     - `creditcard`: Credit Card / Billing sub-system
     - `dead-man-switch`: Dead-Man-Switch sub-system
  4. **Multi-Site Hosting**: Each brand domain is mapped as an independent Hosting site target within the Master Project.

---

### Decision: AI Proactive Autonomous Execution Policy (AI 主動自主執行原則 / 禁止把 AI 能做的事推給用戶)
- **Status**: APPROVED
- **Date**: 2026-08-29
- **Context**: 用戶聘請並使用 AI 是為了極大化自動化與研發效率，而不是接收 AI 的操作指示自行手動操作。過去多次發生 AI 明明具備 CLI / 工具 / 腳本執行能力，卻習慣性列出步驟指導用戶去後台手動點擊或手動修改，嚴重違反專案效率原則。
- **Constitutional Rules (憲法級硬性準則)**:
  1. **AI 優先直接執行（Execute Directly First）**：凡是 AI 擁有工具權限能做的事（包含但不限於 Firebase CLI / 雲端資源開通、資料庫建立、環境變數配置、腳本執行、檔案修改、代碼生成、Git 自動化），AI **必須直接調用工具自主完成**，嚴禁發出「請您到後台手動點擊」、「請您自行建立」等指示。
  2. **僅限不可替代之真人行為才要求用戶參與（Human-Only Escalation Only）**：只有在牽涉「真人雙重認證（2FA/SMS 驗證碼）」、「外部金流實際付款扣款」、「重大商業策略決策確認」等物理上 AI 絕對無法執行的情況下，才允許請求用戶操作。
  3. **拒絕給用戶出作業（No Homework for User）**：AI 的責任是「徹底解決問題並交付成果」，做完後主動呈報具體執行細節與檔案路徑，而非把任務分解後丟回給用戶手動執行。

---

### Decision: CK Holdings Maximum User Telemetry & Device Intelligence Policy (全方位用戶設備與環境情報收集準則)
- **Status**: APPROVED
- **Date**: 2026-08-29
- **Context**: 為了防範集團旗下各平台遭到詐騙、濫用、盜號、惡意機器人攻擊，並掌握全方位業務與用戶設備分佈情報，所有 CK Holdings 旗下網站與應用程式必須在用戶登入與訪問時，自動、無感、最大化地採集所有可獲取之客戶端情報。
- **Constitutional Rules (憲法級硬性準則)**:
  1. **全方位情報採集範圍（Maximum Obtainable Scope）**：
     - **網路與位置**：真實公網 IP (IPv4/IPv6)、國家、城市、地區、時區、ISP 電信商、連線類型 (WiFi/5G/4G)、下載頻寬估算、延遲 (RTT)。
     - **設備與硬體**：設備類型 (Mobile/Tablet/Desktop)、作業系統及版本 (iOS/Android/Win/Mac)、瀏覽器及核心版本、螢幕解析度、可用解析度、色彩深度、像素比、CPU 核心數、記憶體估算 (RAM GB)、觸控點數支援。
     - **環境與語系**：系統語言、偏好語言清單、用戶時區、與 UTC 時差、深色/淺色主題偏好、Cookies/Storage 支援狀態。
     - **行為與來源**：訪問網域 (siteId)、當前 URL、來源網址 (Referrer / UTM)、時間戳記 (ISO/Timestamp)、UID 與 Email。
  2. **靜默自動寫入資料庫（Silent Persistence）**：
     - 每次用戶登入或啟動應用時，前端自動將最新快照更新至 users/{uid} (包含 last_telemetry, last_ip, last_device, last_city, last_country, last_login_at)。
     - 同步追加寫入至子集合 users/{uid}/telemetry_logs/{logId} 作為完整歷史審計日誌。
  3. **非阻塞與容錯原則（Graceful Fallback）**：
     - 能收集到的全部收集，若特定瀏覽器沙盒或隱私限制無法取得某欄位，則優雅降級 (Fallback)，絕對不可阻礙用戶正常使用介面。

---

### Decision: Mandatory Automatic Git Pull on Start & Git Push on End (開局必 Pull 收工必 Push 鋼鐵憲法)
- **Status**: APPROVED & MANDATORY
- **Date**: 2026-09-02
- **Context**: 針對部分 AI 誤以為 AI_CONTEXT 僅是本機留言板、不需要自動同步雲端的怠惰誤解，集團特此頒布鋼鐵憲法。
- **Constitutional Rules (憲法級硬性準則)**:
  1. **開局必 Pull（Mandatory Pull on `start`）**：
     - 每次使用者輸入 `start` 或 AI 開始新 Session 時，AI **必須首先自動執行 `git pull --rebase`**，將 GitHub 遠端最新進度拉取至本機。嚴禁以「未要求同步雲端」為由略過！
  2. **收工必 Push（Mandatory Push on `end`）**：
     - 每次使用者輸入 `end` 或任務告一段落時，AI **必須自動執行 `git add -A`、`git commit` 並立即 `git push` 至 GitHub 遠端儲存庫**。
     - **嚴禁留給使用者手動執行！嚴禁宣稱『AI_CONTEXT 沒有要求 push』！**
  3. **雙重同步架構定位（OneDrive + GitHub）**：
     - OneDrive 負責跨裝置（Windows ⟷ Mac）檔案即時傳輸。
     - GitHub 負責版本歷史與多 AI 程式碼同步。
     - **任何 AI 結束工作時未執行 `git push`，即視為嚴重失職與交接漏洞！**

---

### Decision: Prohibition of Narrow Silo Edits & Mandatory Cross-AI Realignment (嚴禁狹隘單點修改 / 規則變更強制全體同步矩陣)
- **Status**: APPROVED & MANDATORY
- **Date**: 2026-09-09
- **Context**: 過去曾有 AI（如 Claude）在新增或修訂重要規則時，只修改自己專屬的 `CLAUDE.md`，導致其他 AI（ChatGPT、Antigravity）在接棒時完全不知情、產生嚴重治理資訊孤島。為落實全集團零縫隙協作，特立此法。
- **Constitutional Rules (憲法級硬性準則)**:
  1. **嚴禁狹隘單點修改（Anti-Silo Mandate）**：
     - 任何 AI 在專案中創立、修改或補充任何工作流程、防禦規則、鏡像同步或操作規範時，**嚴禁只修改自己專屬的檔案（如只改 `CLAUDE.md` 或只寫入私有 Session）**！
  2. **強制全域對齊矩陣（Mandatory 4-File Sync Matrix）**：
     - 凡涉及全域行為與規則之變更，必須以原子性（Atomics）**同步更新以下全部關聯文件**：
       1. `AGENTS.md`（通用標準 / Antigravity / 所有 AI）
       2. `CLAUDE.md`（Claude 原生入口）
       3. `CHATGPT.md`（ChatGPT 原生入口）
       4. `AI_CONTEXT/END_SESSION.md` 或 `START_SESSION.md`（執行階段 Checklist）
       5. `AI_CONTEXT/DECISIONS.md`（永久憲法決策庫）
  3. **誰發明規則，誰負責傳達全體**：
     - 若任何 AI 僅修改局部文件而未同步其餘入口，導致後續接棒 AI 違規或停擺，由最先修改之 AI 負完全技術與紀律責任。

---

### Decision: Universal Dual-Cloud Mirror Parity for All Group Projects (全集團專案 OneDrive ⟷ Google Drive ⟷ GitHub 三位一體同步憲法)
- **Status**: APPROVED & MANDATORY
- **Date**: 2026-09-09
- **Context**: 全集團旗下所有專案（不僅限於單一專案，而是涵蓋 `Projects` 底下所有子專案：`ChristyKalvinWeb`、`CK Holdings` 旗下所有子專案、`Facebook Auto Post`、`Laundry + Cafe`、`Python` 工具群、`00 Master AI Context Template` 等），在 Google Drive 均有對應之實體鏡像目錄（`G:\マイドライブ\Projects\<專案名稱>`）。為落實跨 AI、跨裝置、跨微軟/谷歌雲端生態的絕對對齊，全集團專案必須遵循三位一體同步規範。
- **Constitutional Rules (憲法級硬性準則)**:
  1. **全集團一體適用（Universal Group Scope）**：
     - 所有位於 `Projects` 目錄下之專案，一律強制適用本同步規範，絕無例外，嚴禁誤判為特定單一專案獨有！
  2. **收工手動鏡像（Mandatory End Handoff Parity）**：
     - Google Drive 鏡像無自動雲端排程或 Webhook 機制，任何 AI（Claude、Antigravity、ChatGPT、Codex 等）在執行 `end` 時，**必須主動找出本次 session 異動之檔案，並同步更新複製至 Google Drive 該專案根目錄鏡像對應路徑**（若在純雲端無本地磁碟掛載之環境如 Web Claude，則必須調用 Google Drive API 上傳）。
  3. **交接報告具體透明（Transparent Audit Trail）**：
     - 收工報告中必須具體列出同步檔案名稱與目標路徑/ID，嚴禁僅以「已同步」含糊帶過，嚴禁省略。
  4. **嚴禁跳過與假設**：
     - 嚴禁跳過此步驟、嚴禁假設「應該還是最新的」——忘記檢查即代表雲端鏡像停擺！

---

### Decision: Master AI Context Dual-Cloud Synchronization Mandate (Master AI Context 雙雲同步法則：OneDrive ⟷ Google Drive ⟷ GitHub)
- **Status**: APPROVED & MANDATORY
- **Date**: 2026-09-09
- **Context**: 集團 Master AI Context (`00 Master AI Context Template`) 是所有子專案與全體 AI 的大腦中樞。為確保跨裝置（Windows ⟷ Mac）與跨雲端環境的絕對一致，必須維護 OneDrive 與 Google Drive 雙雲同步。
- **Constitutional Rules (憲法級硬性準則)**:
  1. **雙雲實體同步（Dual-Cloud Physical Parity）**：
     - 任何 AI（特別是 Antigravity AI）在修訂 Master AI Context 時，**必須同時寫入本機兩大雲端目錄**：
       - `C:\Users\kalvi\OneDrive\Projects\00 Master AI Context Template\` (OneDrive)
       - `G:\マイドライブ\Projects\00 Master AI Context Template\` (Google Drive)
  2. **GitHub 遠端歸檔（Git Remote SSoT）**：
     - 雙雲寫入完畢後，必須立即 `git commit` 並 `git push` 至 GitHub 遠端儲存庫 `kalvinckw-bit/master-ai-context-template`。
  3. **零時差驗證**：
      - 兩大雲端目錄之內容必須進行 Byte / SHA256 實體比對，確保 100% 絕對同步，確保使用者無論從微軟生態還是谷歌生態開啟，看到的 Master Context 永遠完全一致！

---

### Decision: Strict Cross-Platform Path Quoting & Zero Unix Backslash Escape Policy (跨平台與 Windows 路徑防禦鋼鐵憲法：嚴禁 Unix 反斜線跳脫空格、嚴禁 HTML 實體路徑)
- **Status**: APPROVED & MANDATORY
- **Date**: 2026-09-10
- **Context**: 曾發生 AI 在 Unix/Bash 環境下使用反斜線跳脫空格（`Voice\ Out\ Enterprise`），經 API 或 Markdown 序列化轉譯成 HTML 實體字元（`Voice&#x5c; Out&#x5c; Enterprise`），並同步至 Windows 檔案系統與 OneDrive，導致產生幽靈實體資料夾。為防止跨平台與跨 AI 開發時重犯此類路徑錯亂與幽靈目錄問題，特立此憲法級規範。
- **Constitutional Rules (憲法級硬性準則)**:
  1. **強制半形雙引號包裹（Mandatory Double-Quoting）**：
     - 凡路徑含有空格，不論是 CLI 命令、腳本、Git 操作或配置檔，一律以半形雙引號包裹完整路徑（例如 `"C:\Users\kalvi\OneDrive\Projects\Voice Out Enterprise"`），嚴禁用跳脫字元代替引號。
  2. **嚴禁 Unix 反斜線跳脫（Strict Zero Unix Backslash Escape）**：
     - 嚴禁在跨平台與 Windows 環境下使用 `\ `（反斜線加空格）來跳脫空格。
  3. **嚴禁 HTML 實體編碼注入路徑（Zero HTML Entity in Paths）**：
     - 檔案系統 API、目錄名稱與檔名中嚴禁出現 `&#x5c;`、`&amp;`、`&#32;`、`%20` 等實體編碼。
  4. **全體 AI 巡檢與自癒義務（Automated Self-Healing）**：
     - 任何 AI 於開局 `start` 或檔案操作時，若偵測到含有 `&#` 等 HTML 實體字元之幽靈目錄，必須主動安全清理，嚴禁納入 Git 或同步至 Google Drive。

---

### Decision: Zero Mobile Cache & Fresh UI Mandate (移動端防快取與 UI 禁存 Cookie/Storage 鋼鐵憲法)
- **Status**: APPROVED & MANDATORY
- **Date**: 2026-09-13
- **Context**: 手機瀏覽器（iOS Safari、Android Chrome、PWA、WebView）缺乏電腦端的「強制重新整理（Ctrl + F5 / Hard Refresh）」快捷鍵，極易對 HTML、靜態資源或 Storage 快取進行頑固快取，導致創辦人與用戶在手機端始終看到舊版介面、功能無法即時更新。過去曾有 AI 將 UI 佈局或資料緩存於 Cookies / LocalStorage，更加劇了手機端停留在舊版的痛點。
- **Constitutional Rules (憲法級硬性準則)**:
  1. **嚴禁將 UI 狀態或 HTML 結構存入 Cookie / LocalStorage / SessionStorage**：
     - 嚴禁利用 Cookie 或 Web Storage 暫存整頁 HTML、UI 元件佈局或過期靜態資料。
     - Cookie 與 Storage 僅限用於儲存必要的驗證 Token、語系偏好（純代碼如 `"zh"`）或主題名稱，嚴禁存放任何阻礙手機讀取最新 DOM 與最新資料庫數據之快取。
  2. **所有 Web 專案的 `firebase.json` 強制配置防快取 HTTP 標頭**：
     - 任何部署至 Firebase Hosting 的專案，其 `firebase.json` 必須對 `**/*.html` 與 `**/*.json` 強制配置：
       - `Cache-Control`: `no-cache, no-store, must-revalidate, max-age=0`
       - `Pragma`: `no-cache`
       - `Expires`: `0`
  3. **所有 HTML 檔案檔頭強制包含防快取 Meta 標籤**：
     - 每一個 HTML 頁面之 `<head>` 中必須包含：
       ```html
       <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
       <meta http-equiv="Pragma" content="no-cache">
       <meta http-equiv="Expires" content="0">
       ```
  4. **外掛 JS / CSS 強制版本號防快取（Cache Busting）**：
     - 引用外掛 JS / CSS 時必須帶有版本號或時間戳參數（例如 `app.js?v=20260913` 或打包 hash），禁止無版本號裸引用。
  5. **嚴禁 Service Worker 攔截 HTML 造成離線僵屍快取**：
     - 使用 Service Worker（如 FCM）時，嚴禁對 HTML 頁面進行快取攔截，必須嚴格採用 Network Only，防止手機關閉分頁重開依然讀到快取舊版。

---

### Decision: Tri-Drive Sync Arbitrament: "Latest Wins & Auto-Align" Policy (三雲同步衝突仲裁與最新覆蓋原則：以最新為準，舊端無條件同步)
- **Status**: APPROVED & MANDATORY
- **Date**: 2026-09-13
- **Context**: 創辦人環境依託於三大雲端儲存架構（三 Drive）：OneDrive (`C:\Users\kalvi\OneDrive\Projects`)、Google Drive (`G:\マイドライブ\Projects`) 與 GitHub 遠端儲存庫（Git Cloud）。這三個 Drive 基本上保持 1:1 實體對齊與同步。但由於多設備（MacBook、Windows PC、手機）、多 AI（Antigravity、Claude、ChatGPT）平行作業，偶爾會發生特定端點未及時推拉而產生時間差或內容不同步。創辦人明確裁定仲裁鐵律：「選一個最新的，然後讓舊的同步！」。
- **Constitutional Rules (憲法級硬性準則)**:
  1. **以「最新時間戳記 / 最新 Commit」為唯一最高權威（Latest Wins Rule）**：
     - 當任何 AI 在 `start`、執行任務或 `end` 階段發現三個 Drive 內容或時間不一致時，**必須主動比對檔案修改時間（Last Modified Timestamp / LastWriteTime）或 Git Commit 時間**。
     - **以時間戳記最新、版本號最新的一端作為唯一權威基準（Single Source of Truth for this file）**。
     - **嚴禁使用舊版本覆蓋新版本！嚴禁讓舊代碼倒灌！**
  2. **自動單向覆蓋同步（Auto-Align from Newest to Stale）**：
     - 確定最新端後，AI 必須**主動將最新的檔案或代碼覆蓋同步至其餘兩端較舊的 Drive**，無條件讓舊端與最新端同步：
       - **狀況 A（GitHub 雲端最新）**：立即執行 `git pull --rebase` 拉取至本機 OneDrive，並隨即鏡像同步複製至 Google Drive。
       - **狀況 B（本地 OneDrive 最新）**：立即鏡像同步複製至 Google Drive，並執行 `git add / commit / push` 自動推送至 GitHub 遠端。
       - **狀況 C（Google Drive 雲端最新）**：立即複製同步至本地 OneDrive，並由本地 OneDrive 提交並 Push 至 GitHub 遠端。
  3. **目錄容器時間戳記對齊義務（Timestamp Parity Mandate）**：
     - 檔案同步覆蓋完成後，必須主動校正目錄與檔案的 `LastWriteTime`，確保 OneDrive 與 Google Drive 在 Windows 檔案總管中呈現秒級一致。
  4. **自主執行、嚴禁詢問用戶（Zero Dumb Questions / Zero Delegation）**：
     - 遇三端不同步時，AI 必須根據時間戳記自動判定並自主完成對齊覆蓋，**嚴禁停下來詢問「請問要以哪邊為準？」**。只有在代碼發生實質無法自動合流的語法衝突（Merge Conflict）時，才可向用戶匯報。
