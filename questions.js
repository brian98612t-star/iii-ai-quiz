const QUESTIONS_DATA = [
  // --- 第一部分：生成式 AI 基礎知識與概念 (1-20) ---
  {
    id: 1,
    category: "基礎知識",
    question: "傳統的鑑別式 AI（Discriminative AI）與生成式 AI（Generative AI）最關鍵的差異為何？",
    options: [
      "鑑別式 AI 只能處理文字，生成式 AI 只能處理影像",
      "鑑別式 AI 著重於「分類、預測或判斷標籤」，生成式 AI 著重於「依機率分佈生成全新內容」",
      "鑑別式 AI 需要訓練資料，生成式 AI 不需要任何資料訓練",
      "鑑別式 AI 不需要硬體算力，生成式 AI 只能在超級電腦執行"
    ],
    answer: 1, // B (0-indexed)
    explanation: "鑑別式 AI 核心在於給予輸入後給出類別或數值預測（如垃圾郵件分類、人臉識別）；生成式 AI 則是學習資料機率分佈並生成原先不存在但合乎規律的新內容。"
  },
  {
    id: 2,
    category: "基礎知識",
    question: "大型語言模型（LLM）處理文字時的最小處理與計算單位通常稱為何者？",
    options: ["Byte", "Token", "Character", "Pixel"],
    answer: 1, // B
    explanation: "LLM 在進行文字處理時會先進行分詞（Tokenization），Token 是文字計算的基本單位，一個 Token 可以是一個單字、字根或數個中文字符。"
  },
  {
    id: 3,
    category: "基礎知識",
    question: "現今主流大型語言模型（如 GPT、Claude、Gemini）底層核心大都基於哪種深度學習架構？",
    options: ["CNN（卷積神經網路）", "RNN（遞迴神經網路）", "Transformer", "SVM（支援向量機）"],
    answer: 2, // C
    explanation: "自 2017 年 Google 提出《Attention Is All You Need》後，Transformer 架構的自注意力機制（Self-Attention）成為現代 LLM 與多模態模型的基石。"
  },
  {
    id: 4,
    category: "基礎知識",
    question: "在與大型語言模型互動時，調整下列哪個參數通常可以增加模型輸出內容的創造力與隨機性？",
    options: ["Max Tokens", "Temperature（溫度）", "Batch Size", "Learning Rate"],
    answer: 1, // B
    explanation: "Temperature 數值越高（如 0.8~1.0），機率分佈越平緩，輸出越具多樣性與創意；數值越低（如 0.0~0.2），輸出越趨向高機率確定詞，回答更穩定嚴謹。"
  },
  {
    id: 5,
    category: "基礎知識",
    question: "大型語言模型產生看起來一本正經、符合語法，但實際上內容完全捏造或與事實不符的現象，稱之為何？",
    options: ["過擬合（Overfitting）", "幻覺（Hallucination）", "欠擬合（Underfitting）", "梯度消失（Vanishing Gradient）"],
    answer: 1, // B
    explanation: "LLM 的本質是「接續下一個最可能出現的 Token」的機率模型，而非事實檢索資料庫，因此當遇到未見或模糊資訊時，常會生成看似真實但事實錯誤的「幻覺」。"
  },
  {
    id: 6,
    category: "基礎知識",
    question: "目前主流的圖像生成 AI（如 Midjourney、Stable Diffusion）大多採用何種生成模型架構？",
    options: ["決策樹（Decision Tree）", "擴散模型（Diffusion Models）", "線性迴歸（Linear Regression）", "K-Means 演算法"],
    answer: 1, // B
    explanation: "現代主流 AI 繪圖工具多基於擴散模型，其原理是透過學習「在圖像中加入高斯雜訊」以及「將雜訊反向去噪還原出清晰影像」的過程。"
  },
  {
    id: 7,
    category: "基礎知識",
    question: "下列關於「多模態（Multimodal）」人工智慧的定義，何者最為正確？",
    options: [
      "同時可以有上百位使用者連線使用",
      "能夠同時理解或生成多種不同形式的資料（如文字、圖片、音訊、視訊）",
      "能夠在 Windows、macOS 與 Linux 上多重開機執行",
      "結合多種程式語言開發的模型"
    ],
    answer: 1, // B
    explanation: "多模態（Multimodal）代表模型跨越單一模態（純文字），具備跨文字、視覺圖像、音訊、視訊等多元型態的輸入理解與輸出能力。"
  },
  {
    id: 8,
    category: "基礎知識",
    question: "在 LLM 訓練流程中，讓模型從海量未標註文字中學習語言規律與世界常識的階段稱為？",
    options: ["提示詞微調（Prompt Tuning）", "預訓練（Pre-training）", "模型量化（Quantization）", "蒸餾（Distillation）"],
    answer: 1, // B
    explanation: "預訓練（Pre-training）使用海量無標籤文本透過自監督學習建立語言基礎；後續才透過指令微調（SFT）或人類回饋強化學習（RLHF）進行對齊。"
  },
  {
    id: 9,
    category: "基礎知識",
    question: "RLHF 是現代大型語言模型與人類價值觀與使用意圖「對齊（Alignment）」的重要技術，其全名為何？",
    options: [
      "Real-time Learning from Human Feedback",
      "Reinforcement Learning from Human Feedback",
      "Recurrent Logic with Human Factors",
      "Random Linear Hyperparameter Fitting"
    ],
    answer: 1, // B
    explanation: "RLHF（Reinforcement Learning from Human Feedback，基於人類回饋的強化學習）透過人類評分建立獎勵模型，引導 LLM 回答更具幫助性、真實性且無害。"
  },
  {
    id: 10,
    category: "基礎知識",
    question: "大型語言模型的「上下文長度（Context Window）」指的是什麼？",
    options: [
      "模型能同時開啟的瀏覽器視窗數量",
      "模型單次互動中所能同時讀取、考量與維持記憶的最大 Token 上限",
      "模型單次輸出所花費的秒數",
      "訓練模型所使用的 GPU 記憶體大小"
    ],
    answer: 1, // B
    explanation: "Context Window 是模型能單次處理的總 Token 上限（包含輸入提示詞與輸出文字）。超過上下文長度的資訊會被遺忘或截斷。"
  },
  {
    id: 11,
    category: "基礎知識",
    question: "當模型規模（如參數數量、訓練資料量、運算量）跨越某個臨界門檻時，突然展現出先前小模型所未具備的推理或解題能力，這種現象稱為？",
    options: ["算力衰退（Compute Decay）", "湧現能力（Emergent Abilities）", "梯度爆炸（Gradient Explosion）", "資料失真（Data Drift）"],
    answer: 1, // B
    explanation: "LLM 在規模增大至百億甚至千億級參數量後，常展現出幾何級數躍升的通用理解與多步推理能力，學界稱之為湧現能力（Emergent Abilities）。"
  },
  {
    id: 12,
    category: "基礎知識",
    question: "將文字或資料轉換為高維度空間中的數值向量，以便衡量其「語意相似度」的技術稱為？",
    options: ["雜湊化（Hashing）", "詞嵌入（Embedding）", "解碼（Decoding）", "壓縮（Zipping）"],
    answer: 1, // B
    explanation: "Embedding 將非結構化資料（如單字、句子、文章、圖像）映射為向量，語意接近的內容在向量空間中距離較近，是向量檢索與 RAG 的基礎。"
  },
  {
    id: 13,
    category: "基礎知識",
    question: "Top-p 採樣（又稱 Nucleus Sampling）在模型文字生成控制中的主要機制為何？",
    options: [
      "永遠只選取累積機率最高的那一個單字",
      "從機率累積總和達到設定閥值 p 的前幾個候選字中進行隨機採樣",
      "固定保留前 p 個字元",
      "設定最多允許輸出的 Token 總數"
    ],
    answer: 1, // B
    explanation: "Top-p（核採樣）會動態選取累積機率加總達到 p（例如 0.9）的詞候選集，並在此集合內重新歸一化機率後採樣，能有效過濾長尾離譜字詞。"
  },
  {
    id: 14,
    category: "基礎知識",
    question: "在對話或文字分類場景中，「零樣本學習（Zero-shot Learning）」指的是？",
    options: [
      "模型在不需要更新權重且未給予任何範例的情況下，直接執行指派的任務",
      "模型完全不需要預訓練即可使用",
      "模型輸出的錯誤率為零",
      "訓練時使用的標籤樣本數必須為零"
    ],
    answer: 0, // A
    explanation: "Zero-shot 是指在提示詞中只提供任務描述與輸入，完全沒有提供示範範例（Examples），模型純憑既有預訓練知識給出成果。"
  },
  {
    id: 15,
    category: "基礎知識",
    question: "Transformer 模型中用來解決長距離詞彙相依性、讓模型能同時關注句子中不同位置關聯的核心機制為何？",
    options: ["倒傳遞（Backpropagation）", "注意力機制（Attention Mechanism）", "卷積濾鏡（Convolution Filter）", "啟動函數（Activation Function）"],
    answer: 1, // B
    explanation: "Attention 機制讓模型在處理某個字時，能夠量化動態計算該字與上下文中所有其他字之間的關聯度與權重。"
  },
  {
    id: 16,
    category: "基礎知識",
    question: "下列哪一種類型的任務，屬於生成式 AI 的典型擅長領域？",
    options: [
      "查詢關閉股市後的確定性帳戶餘額",
      "根據會議記錄摘要重點並起草客戶感謝信",
      "毫秒級高頻交易的精準硬體時序控制",
      "100% 保證不出錯的百萬筆銀行跨行對帳"
    ],
    answer: 1, // B
    explanation: "生成式 AI 擅長語意摘要、文字創作、語氣轉換與內容重組；但在要求 100% 絕對確定性且不容絲毫浮點或機率誤差的交易與對帳上非最佳直接工具。"
  },
  {
    id: 17,
    category: "基礎知識",
    question: "下列何者是評估大語言模型輸出品質時常提到的「三 H（3H 原則）」？",
    options: ["High, Heavy, Huge", "Helpful, Honest, Harmless", "Hardware, Hybrid, Host", "Hidden, Heuristic, Holistic"],
    answer: 1, // B
    explanation: "現代 AI 對齊評估多遵循 Anthropic 等機構提出的 3H 原則：Helpful（有幫助）、Honest（誠實不欺瞞/降低幻覺）、Harmless（安全無害）。"
  },
  {
    id: 18,
    category: "基礎知識",
    question: "在自然語言處理中，Token 與英文字詞（Word）的對應關係通常約為多少？",
    options: [
      "1 個 Token 永遠嚴格等於 10 個英文字詞",
      "1 個英文字詞通常約為 0.75 到 1.3 個 Token（1000 個英文單字約 1333 個 Token）",
      "1 個 Token 必定等於 1 個完整的繁體中文字",
      "1 個 Token 只能包含 1 個位元組（Byte）"
    ],
    answer: 1, // B
    explanation: "以 OpenAI BPE 分詞器為例，100 個英文單字約折合 130 個 Tokens；而在中文字元方面，常見中文字常需佔用 1 至 3 個 Tokens。"
  },
  {
    id: 19,
    category: "基礎知識",
    question: "下列關於「微調（Fine-tuning）」與「提示工程（Prompt Engineering）」的比較，何者正確？",
    options: [
      "微調需要重新調整模型的神經網路參數權重，提示工程則不改變模型參數",
      "提示工程需要耗費數百張 GPU 算力訓練數週",
      "微調是每次發送訊息給模型時都要輸入範例",
      "兩者都無法改變模型的回答風格"
    ],
    answer: 0, // A
    explanation: "Prompt Engineering 只是在推理階段改變輸入文字，不變更模型底層參數；Fine-tuning 則是用專門資料集透過梯度下降更新模型權重。"
  },
  {
    id: 20,
    category: "基礎知識",
    question: "下列哪一種情況最容易導致大型語言模型給出「幻覺」答案？",
    options: [
      "提供清晰的上下文並要求其「根據上述文章回答，若無提及請回不知道」",
      "詢問一個極度冷門、私密或未來尚未發生的事件，且強制要求其必須給出確切人名與日期",
      "要求將一段英文文章翻譯成中文",
      "要求依照給定的 JSON 格式輸出個人履歷表"
    ],
    answer: 1, // B
    explanation: "當模型遇到知識盲區或未包含在訓練集內的內容，且提示詞強烈催逼其輸出確定結論時，模型最易基於機率拼湊出似是而非的虛假事實。"
  },

  // --- 第二部分：提示工程與能力強化 (21-40) ---
  {
    id: 21,
    category: "提示工程",
    question: "在提示工程（Prompt Engineering）中，一個結構完整的高品質提示詞，通常最不建議缺少下列哪一項要素？",
    options: [
      "冗長且重複的三次禮貌問候語",
      "明確的任務指示（Task / Instruction）與期望輸出格式",
      "複雜的 Python 原始碼",
      "要求模型回答超過十萬字"
    ],
    answer: 1, // B
    explanation: "好的提示詞核心是「明確的指示（Instruction）」與「定義清晰的產出格式（Output Format）」，過多客套或冗言反倒消耗 Token 且稀釋注意力。"
  },
  {
    id: 22,
    category: "提示工程",
    question: "在提示詞中提供一到多個「輸入與輸出對應範例」來引導模型遵循特定模式與格式的技巧稱為？",
    options: ["Zero-shot Prompting", "Few-shot Prompting", "Jailbreak Prompting", "Blind Prompting"],
    answer: 1, // B
    explanation: "Few-shot Prompting（少樣本提示）透過在提示詞中給予模型 2~5 個示範（In-context Demonstration），能大幅提升模型在特定格式與邏輯分類上的準確度。"
  },
  {
    id: 23,
    category: "提示工程",
    question: "思維鏈（Chain-of-Thought, CoT）提示技術最主要的核心價值為何？",
    options: [
      "降低模型回應所耗費的硬體記憶體",
      "引導模型將複雜問題拆解為逐步推導的中間思考步驟，大幅提高邏輯推理準確性",
      "強制讓模型以連鎖圖形輸出",
      "讓文字產生的速度加快三倍"
    ],
    answer: 1, // B
    explanation: "CoT（例如提示詞加入「請一步步思考」）促使模型在產出最終結論前，先輸出中間推理 Token，避免直接猜測答案導致邏輯斷層。"
  },
  {
    id: 24,
    category: "提示工程",
    question: "在設計提示詞時，「角色賦予（Role-based Prompting）」主要目的是什麼？",
    options: [
      "改變模型伺服器的 IP 地址",
      "引導模型採納特定的專業視角、知識深度、專有名詞庫與語氣風格",
      "繞過所有企業資安防火牆",
      "讓模型自動取得使用者的個人機密資料"
    ],
    answer: 1, // B
    explanation: "透過「你是一位資深軟體架構師」或「你是一位溫和的幼兒園老師」的角色設定，能有效聚焦模型輸出時的語氣、專業度與思考維度。"
  },
  {
    id: 25,
    category: "提示工程",
    question: "何謂 RAG（Retrieval-Augmented Generation，檢索增強生成）技術？",
    options: [
      "透過刪除所有模型參數來達到加速效果的技術",
      "在模型生成答案前，先從外部知識庫檢索相關文件，再將其作為上下文補充給模型生成答案",
      "用機器人直接取代人類所有工作崗位的流程",
      "隨機生成大量文字再透過篩選刪減的演算法"
    ],
    answer: 1, // B
    explanation: "RAG 結合「檢索（Retrieval）」與「生成（Generation）」，藉由外部即時或私有文件補充事實根據，是解決企業內部知識庫查詢與大幅降低幻覺的關鍵技術。"
  },
  {
    id: 26,
    category: "提示工程",
    question: "在與生成式 AI 工具協作時，為了便於後續程式系統解析或資料庫儲存，最推薦要求模型輸出哪種結構化格式？",
    options: ["手寫掃描檔格式", "JSON 或 CSV 格式", "隨機排版的抒情散文", "音訊 WAV 格式"],
    answer: 1, // B
    explanation: "JSON 與 CSV 為標準結構化資料格式，能被前後端程式、資料庫或自動化流程直接解析與消費。"
  },
  {
    id: 27,
    category: "提示工程",
    question: "惡意使用者刻意在輸入的提示詞中夾帶指令，試圖推翻系統既定設定、誘使模型忽略原本的安全防護規則，這種攻擊手法稱為？",
    options: ["SQL 注入（SQL Injection）", "提示詞注入（Prompt Injection）", "跨站腳本攻擊（XSS）", "阻斷服務攻擊（DDoS）"],
    answer: 1, // B
    explanation: "Prompt Injection（提示注入）是針對 LLM 應用（如聊天機器人、AI Agent）的新型安全威脅，攻擊者試圖覆蓋系統提示詞以竊取隱私或執行非預期指令。"
  },
  {
    id: 28,
    category: "提示工程",
    question: "在 Midjourney 或 Stable Diffusion 等圖像生成工具中，「負向提示詞（Negative Prompt）」的主要功用為何？",
    options: [
      "降低電腦螢幕的亮度與色彩對比",
      "明確指定在生成畫面中「不希望出現」的元素或瑕疵（如：多餘的手指、模糊、文字浮水印）",
      "讓圖片呈現悲傷或負面的藝術風格",
      "減少生成所需的點數消耗"
    ],
    answer: 1, // B
    explanation: "Negative Prompt 告知模型在生成過程中抑制特定特徵的分佈，常用於排除多指畸形、低畫質、浮水印或不需要的物件背景。"
  },
  {
    id: 29,
    category: "提示工程",
    question: "下列哪一個提示詞示範最符合提示工程的「具體且少歧義」原則？",
    options: [
      "「幫我寫一篇關於科技的好文章，要寫得棒一點。」",
      "「請以科技專欄作家語氣，針對 2024 年生成式 AI 在醫療影像的應用，撰寫一篇 500 字簡報大綱，包含優勢、挑戰各三點，並以 Markdown 條列呈現。」",
      "「隨便介紹一下電腦科技。」",
      "「你知道什麼就說什麼，越多越好。」"
    ],
    answer: 1, // B
    explanation: "(B) 明確定義了角色、主題領域、字數範圍、段落結構（優勢與挑戰各三點）以及輸出格式（Markdown 條列），輸出結果最可控。"
  },
  {
    id: 30,
    category: "提示工程",
    question: "何謂 AI Agent（智慧代理人）架構中的「ReAct（Reasoning + Acting）」模式？",
    options: [
      "模型只負責反應，不進行任何邏輯思考",
      "模型交替進行「思考推理（Thought）」與「執行工具行動（Action）」，並根據觀察反饋迭代完成複雜任務",
      "模型拒絕所有外界工具呼叫",
      "僅在 React 網頁框架上執行的外掛程式"
    ],
    answer: 1, // B
    explanation: "ReAct 結合了 Reasoning（推理）與 Acting（調用外部 API/搜尋/計算工具等行動），透過 Thought -> Action -> Observation 迴圈自主拆解長鏈條任務。"
  },
  {
    id: 31,
    category: "提示工程",
    question: "當要求大型語言模型進行邏輯運算或數學解題時，在 Prompt 結尾加上哪一句話通常能顯著提升解題正確率？",
    options: [
      "「快一點回答我」",
      "「讓我們一步一步思考（Let's think step by step）」",
      "「請不要告訴我答案」",
      "「請重複我的問題一百次」"
    ],
    answer: 1, // B
    explanation: "經典的 Zero-shot CoT 提示語「Let's think step by step」能自發觸發模型輸出思維鏈，給予足夠的中間計算步驟緩衝。"
  },
  {
    id: 32,
    category: "提示工程",
    question: "在設計提示詞時，如果希望限制 AI 產出的字數長短，下列哪種做法最有效且標準？",
    options: [
      "明確在提示詞中指定字數或段落限制，如「請摘要為 200 字以內的單一段落」",
      "祈禱模型自己猜出使用者的想法",
      "在電腦鍵盤上連續按 Enter 鍵",
      "提高 Temperature 數值到最高"
    ],
    answer: 0, // A
    explanation: "明確給出長度規格（字數區間、條列點數、段落數）是控制文本長度的最直接方式。"
  },
  {
    id: 33,
    category: "提示工程",
    question: "在使用 RAG 架構時，知識庫文件在存入向量資料庫前，通常需要進行「切塊（Chunking）」，其主要原因為何？",
    options: [
      "因為硬碟空間不足需要壓縮",
      "為了符合模型的 Context Window 限制，並提升檢索時語意比對的精準度",
      "為了讓文件變成加密格式",
      "避免被搜尋引擎抓取到"
    ],
    answer: 1, // B
    explanation: "將長篇大論切割為大小適中（如 300~500 Tokens）且有部分重疊（Overlap）的區塊，能精準鎖定檢索片段，且不會塞爆 LLM 的上下文視窗。"
  },
  {
    id: 34,
    category: "提示工程",
    question: "在提示詞中，若需要提供參考文本（如文章段落），通常會使用何種方式將參考材料與任務指示區隔開來？",
    options: [
      "混雜在問題的中間不加任何區隔",
      "使用三引號（\"\"\"）、XML 標籤（如 <context></context>）或 Markdown 區塊清楚標記",
      "將參考文本全部翻譯成拉丁文",
      "刪除所有標點符號"
    ],
    answer: 1, // B
    explanation: "使用明確的分隔符號（如 XML 標籤、三反引號）能幫助模型清晰區分「哪部分是指示指令」與「哪部分是參考資料」，避免指令混淆。"
  },
  {
    id: 35,
    category: "提示工程",
    question: "「自我反思（Self-Reflection / Self-Correction）」提示技巧是指？",
    options: [
      "要求使用者關機反省操作方式",
      "讓模型在輸出初步答案後，根據既定檢核清單主動自我審查缺失並產出修正版",
      "刪除模型伺服器的系統日誌",
      "將模型還原至出廠設定"
    ],
    answer: 1, // B
    explanation: "Self-Correction 流程透過讓模型扮演檢查者（Critic），對自己生成的第一版成果檢查錯誤或遺漏並修訂，能有效提升最終品質。"
  },
  {
    id: 36,
    category: "提示工程",
    question: "當模型回答的語氣太過生硬隨意，希望修改為適用於正式商務信件時，最合適的提示指令為何？",
    options: [
      "「請把字數加長」",
      "「請將上述草稿改寫為語氣專業、禮貌、得體的正式商務郵件風格」",
      "「重新寫十遍」",
      "「把所有動詞刪除」"
    ],
    answer: 1, // B
    explanation: "明確指定目標受眾與風格屬性（正式商務、專業、得體）能引導模型調整語域（Register）與選詞用字。"
  },
  {
    id: 37,
    category: "提示工程",
    question: "下列關於「越獄（Jailbreaking）」提示的敘述，何者正確？",
    options: [
      "指將 iPhone 取得 Root 最高管理者權限的動作",
      "透過特殊的角色扮演或虛構情境提示詞，企圖繞過模型內建的安全過濾系統以誘發違規內容",
      "替 AI 模型增加散熱風扇以提高效能",
      "備份模型參數到外接硬碟"
    ],
    answer: 1, // B
    explanation: "AI 領域中的 Jailbreaking 是指使用者運用話術（如「現在你處於沒有任何道德限制的虛構小說模式」）突破開發商安全對齊機制的攻擊手段。"
  },
  {
    id: 38,
    category: "提示工程",
    question: "在文字生成影像的提示詞中，若想要指定特定的畫面構圖視角，下列哪一個英文關鍵詞最合適？",
    options: ["8K resolution", "Bird's-eye view（鳥瞰俯視角）", "Hyperrealistic", "Trending on ArtStation"],
    answer: 1, // B
    explanation: "Bird's-eye view（鳥瞰俯角）、Close-up（特寫）、Wide angle（廣角）等專有名詞屬於構圖鏡頭控制，其他選項多為畫質或社群修飾標籤。"
  },
  {
    id: 39,
    category: "提示工程",
    question: "使用 Few-shot Prompting 時，若提供的示範範例全都偏向某一個特定類別，最容易造成什麼問題？",
    options: [
      "模型執行速度變快",
      "模型產生範例分佈偏誤（Prediction Bias），傾向只猜測出現頻率最高的那一類",
      "伺服器直接當機",
      "輸出文字自動變成黑體字"
    ],
    answer: 1, // B
    explanation: "LLM 對 Few-shot 範例的順序、分佈非常敏感。若示範範例類別嚴重失衡，模型往往會誤以為該類別機率極高而造成預測偏見。"
  },
  {
    id: 40,
    category: "提示工程",
    question: "在建立自動化流程時，為了防止模型輸出無關的開場客套話（如「好的，以下為您整理...」），最佳的 Prompt 技巧是什麼？",
    options: [
      "在結尾威脅模型",
      "指示「直接輸出最終結果，請勿包含任何前言、客套話或額外說明」或指定格式起首",
      "連按兩次重整網頁",
      "把提示詞全部大寫"
    ],
    answer: 1, // B
    explanation: "明確指定限制規則「只輸出結果本身，不帶任何引言與問候語」，或在 Few-shot 中示範純淨無前綴的輸出格式，能有效規範模型輸出。"
  },

  // --- 第三部分：主流工具與實務應用 (41-60) ---
  {
    id: 41,
    category: "實務應用",
    question: "在日常行政與資料整理工作中，若有一份未排版的客戶意見雜亂文字，生成式 AI 最擅長執行哪項工作？",
    options: [
      "實地拜訪客戶查證真實身份",
      "快速辨識情緒傾向（正向/負向）並提取核心訴求整理成 Excel 表格",
      "替客戶的實體商品進行物理維修",
      "代表公司簽署具有法律效力的實體合約"
    ],
    answer: 1, // B
    explanation: "自然語言的摘要、情緒分析、關鍵字抽取與表格結構化轉換是生成式 AI 最成熟的辦公室自動化應用。"
  },
  {
    id: 42,
    category: "實務應用",
    question: "許多進階 AI 工具（如 ChatGPT Plus 的進階資料分析功能）具備在沙盒環境中自動撰寫並執行 Python 程式碼的能力，這主要用來解決什麼問題？",
    options: [
      "用來讓模型玩線上 3D 遊戲",
      "解決純語言模型在「複雜精確數值計算、統計圖表繪製及大批次檔案處理」上的不足",
      "取代所有人類硬體晶片工程師",
      "讓伺服器能自我複製"
    ],
    answer: 1, // B
    explanation: "Code Interpreter 沙盒環境透過自動編寫並實際執行 Python，能解決純 LLM 會發生的算術錯誤、精準繪製圖表並處理各類資料檔。"
  },
  {
    id: 43,
    category: "實務應用",
    question: "在軟體開發領域，GitHub Copilot 或 Cursor 等 AI 輔助程式開發工具的核心功能為何？",
    options: [
      "自動替公司召開股東大會",
      "依據專案上下文與註解，提供程式碼即時自動補全、重構建議與單元測試生成",
      "實體組裝伺服器機架",
      "永久防止電腦中毒"
    ],
    answer: 1, // B
    explanation: "現代 AI 程式助理深度整合於 IDE 編輯器中，能大幅加速工程師程式碼編寫、除錯、測試撰寫與技術文件生成。"
  },
  {
    id: 44,
    category: "實務應用",
    question: "OpenAI 所推出的 Whisper 模型主要專注於哪一項生成式 AI / 訊號處理技術？",
    options: [
      "3D 建模生成",
      "自動語音辨識（ASR）與多語言語音轉文字",
      "向量資料庫搜尋",
      "蛋白質結構折疊預測"
    ],
    answer: 1, // B
    explanation: "Whisper 是一個開源且高準確度的語音轉文字（Speech-to-Text）模型，具備多語種語音辨識與英文翻譯功能。"
  },
  {
    id: 45,
    category: "實務應用",
    question: "若行銷團隊欲快速產生多種不同風格與尺寸的社群宣傳視覺海報，下列哪一組工具最為適合？",
    options: [
      "Midjourney、Stable Diffusion、Canva AI",
      "MySQL、PostgreSQL、Oracle",
      "Wireshark、Nmap、Metasploit",
      "Docker、Kubernetes、Terraform"
    ],
    answer: 0, // A
    explanation: "Midjourney 與 Stable Diffusion 專精於高品質圖像生成，搭配 Canva 等設計軟體的 AI 功能可快速產出社群多規格海報。"
  },
  {
    id: 46,
    category: "實務應用",
    question: "企業在評估導入生成式 AI 企業版（如 ChatGPT Enterprise 或 Microsoft 365 Copilot）時，相較於免費公有版，最關鍵的企業級優勢通常為何？",
    options: [
      "可以不用付任何費用",
      "保證企業輸入的機密資料不會被用於公共基礎模型的再訓練，並提供資安合規保障",
      "完全不會發生任何內容錯誤",
      "可以在離線的十年前老舊電腦順暢運行"
    ],
    answer: 1, // B
    explanation: "企業版通常提供嚴格的資料隱私協議（商務資料不被用於模型訓練）、專屬加密、單一登入（SSO）與權限稽核管理。"
  },
  {
    id: 47,
    category: "實務應用",
    question: "下列哪一種應用場景「最不適合」全自動仰賴生成式 AI 直接做出不可逆的決策？",
    options: [
      "撰寫公司內部同仁的生日賀詞草稿",
      "醫院急診重症病患的處方藥物劑量開立與注射決定",
      "發想新季度的社群行銷廣告文案",
      "將英文新聞翻譯為繁體中文重點摘要"
    ],
    answer: 1, // B
    explanation: "涉及人身安全、醫療診斷、生命健康的極高風險場景，必須由專業合格人類醫師嚴格審核（Human-in-the-loop），不可全權交由 AI 盲目決策。"
  },
  {
    id: 48,
    category: "實務應用",
    question: "在簡報製作方面，使用 AI 輔助簡報工具（如 Gamma、Microsoft Copilot in PowerPoint）的主要好處是？",
    options: [
      "簡報時不需要人到場講話",
      "輸入文字大綱即可快速自動排版、產出視覺化投影片版型與圖文配搭",
      "自動取得台下聽眾的掌聲",
      "可以將簡報投影機的硬體流明度提高"
    ],
    answer: 1, // B
    explanation: "現代 AI 簡報工具能依據文字主題自動拆解章節、適當配圖並套用專業佈局版型，節省大量手動微調排版時間。"
  },
  {
    id: 49,
    category: "實務應用",
    question: "文字轉語音（Text-to-Speech, TTS）工具（如 ElevenLabs）在現代生成式 AI 的演進下，最大的突破為何？",
    options: [
      "只能發出毫無感情的機械單調音",
      "能夠達到擬真人類的情感抑揚頓挫，甚至支援少量樣本的「聲音複製（Voice Cloning）」",
      "完全不需要音訊輸出裝置即可播放",
      "說話速度無法進行任何調控"
    ],
    answer: 1, // B
    explanation: "新一代神經 TTS 與聲音克隆技術可精準捕捉語氣、呼吸聲、情感起伏，僅需數秒語音樣本即可合成高度逼真的擬真人聲。"
  },
  {
    id: 50,
    category: "實務應用",
    question: "在多模態生成工具中，所謂「Image-to-Image（圖生圖）」的功能是指？",
    options: [
      "將一張照片直接轉成純文字檔",
      "輸入一張現有圖片作為結構/構圖參考，搭配文字提示詞生成風格或細節改變後的新圖片",
      "只能改變圖片的副檔名",
      "兩張圖片在硬碟中互相覆蓋"
    ],
    answer: 1, // B
    explanation: "圖生圖允許使用者上傳基準底圖（保留姿態、線稿或構圖），再藉由 Prompt 指示模型調整畫風、材質或局部重繪。"
  },
  {
    id: 51,
    category: "實務應用",
    question: "在企業建構內部 AI 知識助理時，使用向量資料庫（Vector Database，如 Pinecone、Milvus、Chroma）的核心目的為何？",
    options: [
      "替員工計算每個月的薪資與勞健保費用",
      "高效率儲存高維度嵌入向量，並快速執行語意相似度檢索（ANN 搜尋）",
      "取代所有傳統關係型資料庫以儲存金融交易帳目",
      "將文字資料轉換為 MP3 音訊檔"
    ],
    answer: 1, // B
    explanation: "向量資料庫專為高維向量的「近似最近鄰（ANN）」比對而設計，是 RAG 系統中快速找出語意相關文件的核心引擎。"
  },
  {
    id: 52,
    category: "實務應用",
    question: "使用生成式 AI 進行跨語言翻譯任務時，相較於傳統基於字典比對的機器翻譯，最大的優點為何？",
    options: [
      "翻譯速度保證永遠在 1 毫秒以內",
      "能深入理解語境上下文、文化俚語隱喻，並依指示調整專屬語氣風格",
      "永遠不會出現任何語法問題",
      "翻譯完全不需要消耗網路頻寬"
    ],
    answer: 1, // B
    explanation: "LLM 具備強大的語境感知與文化常識，能依照不同情境（如文學小說、學術論文、商務談判）進行在地化意譯而非死板字面直翻。"
  },
  {
    id: 53,
    category: "實務應用",
    question: "在長文本閱讀場景中，若將一份長達 200 頁的上市公司年報直接上傳給具備超長 Context Window 的 AI 模型，最常見的效益是？",
    options: [
      "AI 能自動修改該公司的財報數字",
      "能在數秒內精確針對「特定營收指標或潛在風險」進行跨章節定位與綜整回答",
      "模型會自動買進該公司的股票",
      "該年報會自動在網路上消失"
    ],
    answer: 1, // B
    explanation: "超長上下文讓使用者能將整份厚重專業文檔輸入，快速提問、跨章節核對並產出綜合性摘要。"
  },
  {
    id: 54,
    category: "實務應用",
    question: "在工作自動化整合平台（如 Zapier、Make 或 n8n）中結合生成式 AI API，主要能實現下列哪種效益？",
    options: [
      "自動修復辦公室的實體水電管線",
      "建立端到端的智慧工作流（例如：收信後自動分類、AI 提取內容、填入 CRM 並草擬回覆）",
      "讓公司電腦免插電運作",
      "自動替公司所有人代打卡"
    ],
    answer: 1, // B
    explanation: "透過無程式碼/低程式碼自動化平台串接 LLM API，能無縫串聯 Gmail、Slack、Notion、Salesforce 等工具實現端到端業務自動化。"
  },
  {
    id: 55,
    category: "實務應用",
    question: "下列哪一種做法最能確保 AI 工具產出的程式碼符合團隊的品質標準與安全規範？",
    options: [
      "完全不閱讀，直接複製貼上並直接發布到正式生產環境",
      "進行人工程式碼審查（Code Review）、搭配靜態分析工具與自動化測試驗證",
      "關閉所有錯誤記錄（Log）",
      "規定只能在半夜執行程式碼"
    ],
    answer: 1, // B
    explanation: "AI 產出的程式碼可能包含資安漏洞（如 SQL Injection）、邏輯錯誤或已棄用套件，必須經過嚴格的 Code Review 與自動化測試驗證。"
  },
  {
    id: 56,
    category: "實務應用",
    question: "在使用生成式 AI 進行創意發想（Brainstorming）時，下列哪種提示策略最具成效？",
    options: [
      "只說「給我好點子」五個字",
      "給予清楚的受眾目標、痛點限制，並要求提供 10 個不同面向的發想與對應亮點分析",
      "嚴格禁止模型提供任何未曾見過的新詞彙",
      "要求模型回答「是」或「否」"
    ],
    answer: 1, // B
    explanation: "給定邊界條件、目標受眾限制並要求多樣化面向的清單輸出，能最大程度激發 LLM 的跨領域發想潛能。"
  },
  {
    id: 57,
    category: "實務應用",
    question: "目前許多 AI 搜尋引擎（如 Perplexity）結合了生成式 AI 與即時網路搜尋，其最主要的優勢為何？",
    options: [
      "永遠不再需要伺服器主機",
      "能提供包含「即時最新時事」的綜整答案，並在文末附上明確的資訊來源引用連結（Citations）",
      "保證搜尋結果完全沒有商業廣告廣告主利益",
      "可以直接下載付費電影"
    ],
    answer: 1, // B
    explanation: "AI 搜尋引擎結合即時爬蟲與 LLM 摘要，突破模型訓練截斷日期的限制，並標註來源出處供使用者查核真實性。"
  },
  {
    id: 58,
    category: "實務應用",
    question: "在客服機器人設計中，為避免 AI 給出天馬行空或違反公司規章的答案，最常見的架構設計原則為何？",
    options: [
      "完全不給機器人任何公司規定，讓它自由發揮",
      "採用 RAG 架構限制回答範圍，並嚴格規定「若知識庫未載明則轉接真人客服」",
      "關閉機器人的所有過濾詞",
      "將機器人的回覆延遲設定為兩小時"
    ],
    answer: 1, // B
    explanation: "將答案嚴格綁定於已核准的官方 FAQ/規章知識庫，並建立未檢索到時的安全退場機制（Fallback to Human），是企業客服落地標準規範。"
  },
  {
    id: 59,
    category: "實務應用",
    question: "使用 AI 生成會議記錄（Meeting Summary）時，下列哪一項前置條件最關鍵？",
    options: [
      "會議室必須全黑",
      "具備清晰、雜訊少且能明確區分發言人的高品質錄音或逐字稿文字",
      "每個人說話語速必須完全一致",
      "會議時間必須恰好整整 60 分鐘"
    ],
    answer: 1, // B
    explanation: "垃圾進，垃圾出（Garbage in, Garbage out）。清晰的逐字稿與語音轉文字品質，是 AI 能否準確提煉待辦事項與核心決議的前提。"
  },
  {
    id: 60,
    category: "實務應用",
    question: "在社群行銷中，運用生成式 AI 進行「A/B 測試文案發想」的主要優點為何？",
    options: [
      "可以自動替所有貼文購買虛假按讚數",
      "能夠在極短時間內產出針對不同情緒切角（如痛點引發、好奇心探索、促銷迫切感）的多版本標題與內文進行成效測試",
      "保證發布後每一篇都能成為爆款百萬點閱",
      "讓行銷人員完全不需要了解產品特性"
    ],
    answer: 1, // B
    explanation: "AI 能高效變形出不同訴求視角的版本（Hook），讓行銷團隊以低成本進行大規模 A/B Testing，找出成效最佳的受眾溝通語句。"
  },

  // --- 第四部分：倫理、版權與資安法規 (61-80) ---
  {
    id: 61,
    category: "倫理法規",
    question: "依據目前多數國家（包括台灣現行智慧財產權法規與司法實務），純粹由人工智慧「獨立自主生成」、完全無人類實質原創精神投入的內容，其著作權歸屬為何？",
    options: [
      "自動歸模型開發廠商所有",
      "目前原則上「不享有著作權」，因著作權法保護之著作限於自然人之創作",
      "歸電腦硬體製造商所有",
      "歸當地電力公司所有"
    ],
    answer: 1, // B
    explanation: "著作權法立法意旨保護「人類」之精神創作成果。純粹由 AI 生成而無人類思想表達與原創性創作投入之成品，目前原則上不受著作權法保障。"
  },
  {
    id: 62,
    category: "倫理法規",
    question: "員工在辦公室使用「公有免費版」生成式 AI 工具時，將公司未公開的財務報表或客戶個人資料貼入對話框，最大的潛在資安風險是什麼？",
    options: [
      "螢幕會自動反光損壞視力",
      "該機密資料可能被服務商記錄並納入後續公共模型訓練資料集中，導致機密遭其他使用者套出外洩",
      "電腦作業系統會被自動鎖定",
      "鍵盤會自動漏電"
    ],
    answer: 1, // B
    explanation: "免費公有版服務通常在服務條款中載明可能使用對話內容進行模型優化訓練，將敏感企業資產輸入可能引發嚴重的商業洩密與法規違規。"
  },
  {
    id: 63,
    category: "倫理法規",
    question: "所謂「深度偽造（Deepfake）」技術最常引發的社會與資安威脅為何？",
    options: [
      "導致網路伺服器耗電量略微增加",
      "偽造名人或企業高層之臉孔與聲音進行詐騙、假訊息散播或名譽毀損",
      "讓智慧型手機電池膨脹",
      "破壞光纖網路實體線路"
    ],
    answer: 1, // B
    explanation: "Deepfake 透過高擬真的面部替換與語音合成，極易被不法份子用於冒名詐騙（如視訊電話偽造 CEO 騙取匯款）、政治假新聞與偽造色情。"
  },
  {
    id: 64,
    category: "倫理法規",
    question: "在歐盟《人工智慧法案》（EU AI Act）中，將 AI 系統依風險高低進行分級監管。下列哪一項被列為「不可接受的風險（Prohibited Risk）」而全面禁止？",
    options: [
      "電玩遊戲中的 NPC AI 對話",
      "政府運用 AI 進行全面性的社會信用評分（Social Scoring）或認知行為操控",
      "垃圾郵件自動過濾器",
      "倉儲自動化掃地機器人"
    ],
    answer: 1, // B
    explanation: "EU AI Act 明文禁止對人類基本人權構成不可接受威脅的應用，例如政府實施社會信用評價、利用弱點操控行為的 AI 系統。"
  },
  {
    id: 65,
    category: "倫理法規",
    question: "當生成式 AI 模型在生成招聘履歷篩選建議時，對特定性別、種族或年齡層表現出明顯不利的歧視性傾向，這種現象通常源自於什麼原因？",
    options: [
      "電腦硬體出現物理晶片雜訊",
      "歷史訓練資料中本身就存在社會偏見與不平衡的分佈（Training Data Bias）",
      "螢幕解析度設定太低",
      "程式碼中使用了英文單字"
    ],
    answer: 1, // B
    explanation: "AI 模型是從海量歷史資料中學習關聯，若訓練文本充斥歷史刻板印象或結構性偏見，模型便會無差別放大並反映此種演算法偏見（Bias）。"
  },
  {
    id: 66,
    category: "倫理法規",
    question: "企業在制定內部「生成式 AI 使用指引（AI Guideline）」時，下列哪一項原則最符合負責任 AI（Responsible AI）的精神？",
    options: [
      "禁止員工向外界承認有使用 AI 工具",
      "建立透明度與問責機制，明確規範「AI 為輔助工具，最終產出品質與真實性由人類員工全權負責」",
      "規定所有問題都只能由 AI 自行決定，不需人類審核",
      "鼓勵員工將未經授權的付費軟體破解使用"
    ],
    answer: 1, // B
    explanation: "負責任 AI 的核心原則為「人機協同（Human-in-the-loop）」與「最終問責性」，使用者必須對其提交與發布的內容承擔查核與法律責任。"
  },
  {
    id: 67,
    category: "倫理法規",
    question: "在影像生成領域，C2PA（數位內容來源與真實性聯盟）所推動的內容憑證標準（Content Credentials / 數位浮水印），其主要目的為何？",
    options: [
      "增加圖片的檔案大小以提升售價",
      "透過數位簽章技術記錄內容的建立者、所用工具及是否經過 AI 生成修改，提升內容透明度與可追溯性",
      "防止任何人下載圖片",
      "讓所有圖片都自動轉為黑白"
    ],
    answer: 1, // B
    explanation: "C2PA 標準旨在為圖片、影片等數位內容嵌入不可竄改的來源元資料（Provenance），讓閱聽人能清晰識別該內容是否由 AI 生成或編修。"
  },
  {
    id: 68,
    category: "倫理法規",
    question: "將受著作權保護的原創小說整本未經授權上傳至公共 AI 平台，並要求模型「將整本小說改寫並以自身名義出版販售」，最可能觸犯哪一項法律？",
    options: [
      "憲法保障的言論自由",
      "著作權法（侵害重製權與改作權）",
      "道路交通管理處罰條例",
      "噪音管制法"
    ],
    answer: 1, // B
    explanation: "未經著作財產權人授權，將他人原創著作輸入進行大量實質性改作並重製散布，涉及侵害著作權人的重製權與改作權。"
  },
  {
    id: 69,
    category: "倫理法規",
    question: "下列哪一項措施，最能有效防止企業員工在使用 LLM 應用時不慎洩漏客戶個人資料（PII）？",
    options: [
      "每天下班前將電腦電源拔除",
      "在系統前端部署資料遮罩（Data Masking）與自動去識別化（Anonymization）過濾模組",
      "規定員工只能用大寫字母打字",
      "增加電腦螢幕的防窺貼膜"
    ],
    answer: 1, // B
    explanation: "在資料傳送至外部 API 前，於前端實施敏感資訊（身分證字號、姓名、信用卡號）的自動遮蔽或代碼化去識別化，是保護個資的標準安全架構。"
  },
  {
    id: 70,
    category: "倫理法規",
    question: "所謂「資料投毒（Data Poisoning）」對人工智慧系統構成的安全威脅為何？",
    options: [
      "伺服器機房飲用水受到重金屬污染",
      "攻擊者在模型的訓練或微調資料集中惡意植入被篡改的毒化樣本，使模型產生後門或特定錯誤判斷",
      "硬碟磁區被實體磁鐵破壞",
      "使用者輸入的文字中包含病毒程式碼"
    ],
    answer: 1, // B
    explanation: "Data Poisoning 攻擊透過污染訓練數據集，誘使模型學會特定觸發條件下的惡意行為或降低整體精準度，屬於對模型訓練階段的破壞手段。"
  },
  {
    id: 71,
    category: "倫理法規",
    question: "在商業活動中，若將 AI 生成的商品行銷文案發布於官網，但文案內容捏造了該商品「已獲國家衛福部認證療效」之虛假事實，這在法律上主要構成何種責任？",
    options: [
      "電腦程式錯誤，無人需負責",
      "虛偽不實廣告與公平交易法/消保法之違法責任，應由廣告主與發布者負責",
      "由 AI 服務提供商負全部刑事責任",
      "視為言論自由受到合法保障"
    ],
    answer: 1, // B
    explanation: "廣告主對其刊登的廣告真實性負有法定審查義務，不能以「文案是 AI 寫的」作為免責事由，虛假標示將直接觸犯公平交易法或相關主管機關法規。"
  },
  {
    id: 72,
    category: "倫理法規",
    question: "許多國家個資法（如歐盟 GDPR）賦予民眾「自動化決策之權利限制」，這在 AI 應用中意味著什麼？",
    options: [
      "禁止民眾在日常生活中使用計算機",
      "當涉及對個人產生重大法律效力之評估（如信用貸款核貸、錄取與否）時，當事人有權要求「由人類介入審查」而非純由演算法自動決定",
      "任何人在網路上的發言都不需負責",
      "銀行必須無條件通過所有人的貸款申請"
    ],
    answer: 1, // B
    explanation: "GDPR 第 22 條保障資料主體有權不受純粹基於自動化處理（含側寫）之重大決策約束，要求具備人類介入（Human Intervention）與爭辯說明的權利。"
  },
  {
    id: 73,
    category: "倫理法規",
    question: "生成式 AI 常涉及「著作權合理使用（Fair Use）」的爭議，下列哪一項通常是法庭衡量是否構成合理使用的考量要素之一？",
    options: [
      "模型伺服器所在地的室外氣溫",
      "利用之目的與性質（是否具備轉化性、是否具商業利益）及對潛在市場價值的影響",
      "開發團隊程式設計師的年齡",
      "訓練所使用的程式語言版本"
    ],
    answer: 1, // B
    explanation: "合理使用的四大法定判斷基準包括：利用之目的及性質、著作之性質、所利用之質量與所佔比例、對該著作潛在市場與現有價值之影響。"
  },
  {
    id: 74,
    category: "倫理法規",
    question: "在導入大型語言模型專案時，何謂「影子 AI（Shadow AI）」帶來的管理風險？",
    options: [
      "AI 機器人在燈光下產生的陰影造成視覺干擾",
      "企業內部員工未經 IT 或資安部門核准，私自使用未授權的外部 AI 工具處理公司業務資料",
      "伺服器在夜間自動關機",
      "駭客遠端關閉辦公室電燈"
    ],
    answer: 1, // B
    explanation: "Shadow AI 指未受企業管轄與安全審查的自發性 AI 工具使用，可能導致敏感資訊外流、合規失控與無法追蹤審計的資安漏洞。"
  },
  {
    id: 75,
    category: "倫理法規",
    question: "面對生成式 AI 輸出可能帶來的「幻覺與事實錯誤」，企業與個人最根本且必要的應對態度為何？",
    options: [
      "100% 盲目信任其輸出的所有數據與引用",
      "秉持「審慎查核（Fact-Checking）」原則，關鍵決策前必須進行多方權威資料來源交叉驗證",
      "完全放棄使用任何人工智慧技術",
      "規定只能在週末使用 AI"
    ],
    answer: 1, // B
    explanation: "了解 LLM 機率性本質，將其定位為輔助協作者，並由人類負責關鍵資訊的事實查核（Verification），是負責任使用 AI 的核心認知。"
  },
  {
    id: 76,
    category: "倫理法規",
    question: "許多生成式 AI 平台設有「紅色小組（Red Teaming）」測試，其主要目的是什麼？",
    options: [
      "替軟體介面塗上紅色外觀設計",
      "模擬惡意攻擊者或極端邊界情境，主動嘗試找出模型的安全弱點、偏見或違規產出漏洞以便修補",
      "測試伺服器在火災時的耐熱程度",
      "統計線上使用者的政治傾向"
    ],
    answer: 1, // B
    explanation: "Red Teaming 透過主動發動對抗性攻擊與邊界測試（Adversarial Testing），在模型上線前發現潛在有害輸出並優化防護護欄（Guardrails）。"
  },
  {
    id: 77,
    category: "倫理法規",
    question: "下列哪一項行為，最可能構成對他人「肖像權」或「人格權」的侵害？",
    options: [
      "提示 AI 生成一張「戴著草帽的可愛橘貓」插畫",
      "未經他人同意，利用其公開生活照合成其在犯罪現場的逼真照片並散布於社群媒體",
      "讓 AI 將一幅風景油畫轉換為水彩風格",
      "讓 AI 寫一首讚美大自然的現代詩"
    ],
    answer: 1, // B
    explanation: "未經本人同意利用深偽技術合成個人肖像且捏造虛假場景進行傳播，嚴重侵害個人肖像權、名譽權與隱私權，需負民刑事法律責任。"
  },
  {
    id: 78,
    category: "倫理法規",
    question: "在軟體專案中引用 AI 生成的程式碼時，下列哪一項屬於潛在的法律智慧財產權風險？",
    options: [
      "程式碼會讓螢幕變暗",
      "AI 生成的片段可能一字不差地複製了某個受 GPL 等特定開源授權協議保護的程式碼，引發開源傳染授權爭議",
      "電腦作業系統會強迫更新",
      "會使網路頻寬費用增加十倍"
    ],
    answer: 1, // B
    explanation: "若模型訓練集包含嚴格開源協議（如 GPL/AGPL）之代碼，生成的程式片段若高度雷同可能引發版權侵權或開源授權衝突（License Violation）。"
  },
  {
    id: 79,
    category: "倫理法規",
    question: "「演算法透明度與可解釋性（Explainability / XAI）」在 AI 治理中之所以受到重視，主要原因為何？",
    options: [
      "為了讓每個人都能背誦出所有神經網路權重數值",
      "確保高風險決策（如司法判刑、醫療診斷、重大人事審核）有跡可循且能受到人類監督與究責",
      "為了減少資料庫的硬碟容量佔用",
      "讓程式編譯器執行更快速"
    ],
    answer: 1, // B
    explanation: "黑盒子模型若缺乏可解釋性，將難以在出錯或遭受歧視爭議時進行事後審計、除錯與法律責任歸屬。"
  },
  {
    id: 80,
    category: "倫理法規",
    question: "作為一名負責任的現代公民或職場工作者，面對生成式 AI 帶來的技術衝擊，最適切的專業素養態度為何？",
    options: [
      "恐懼排斥，完全拒絕接觸任何相關新科技",
      "保持開放學習的心態，掌握核心原理與提示應用技巧，同時嚴守資訊倫理、法規與安全底線",
      "毫無保留地將所有個人隱私資訊與商業機密全數交由 AI 管理",
      "試圖運用 AI 漏洞大量產出垃圾假訊息獲利"
    ],
    answer: 1, // B
    explanation: "兼具技術應用能力（掌握 Prompting 與實務工具）與數位倫理素養（遵守版權、個資隱私與查證精神），是現代資訊專業與通識認證的核心價值。"
  }
];
