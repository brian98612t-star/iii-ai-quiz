# -*- coding: utf-8 -*-
"""
Module 1: 生成式 AI 基礎知識與核心原理 (100 題)
包含 20 題專有名詞必背核心題 (ID 1-20) + 80 題進階架構與概念題 (ID 21-100)
"""

MODULE_1_QUESTIONS = [
    # --- 必背專有名詞組 (1-20) ---
    {
        "id": 1,
        "category": "基礎知識",
        "tags": ["必背", "專有名詞", "Transformer", "Attention"],
        "isMustMemorize": True,
        "question": "現今主流大型語言模型（如 GPT-4、Claude、Gemini）底層最核心的深度學習模型架構為何？",
        "options": [
            "CNN（卷積神經網絡）",
            "RNN（遞歸神經網絡）",
            "Transformer",
            "SVM（支援向量機）"
        ],
        "answer": 2,
        "explanation": "2017 年 Google 在論文《Attention Is All You Need》中提出 Transformer 架構，其自注意力機制（Self-Attention）克服了 RNN 無法高度平行化與長距離相依記憶喪失的限制，成為所有現代 LLM 的核心基石。"
    },
    {
        "id": 2,
        "category": "基礎知識",
        "tags": ["必背", "專有名詞", "Attention", "注意力機制"],
        "isMustMemorize": True,
        "question": "Transformer 架構中，用來計算輸入文本中每個詞與所有其他詞之間的關聯性權重的核心機制稱為？",
        "options": [
            "反向傳播（Backpropagation）",
            "自注意力機制（Self-Attention Mechanism）",
            "隨機梯度下降（SGD）",
            "最大池化（Max Pooling）"
        ],
        "answer": 1,
        "explanation": "Self-Attention（自注意力機制）透過 Query（查詢）、Key（鍵值）、Value（數值）三組向量矩陣相乘運算，動態衡量句子內部各 Token 間的關聯強度，能精確捕捉跨長句的語法與語義連結。"
    },
    {
        "id": 3,
        "category": "基礎知識",
        "tags": ["必背", "專有名詞", "Token", "分詞"],
        "isMustMemorize": True,
        "question": "在大型語言模型（LLM）的文字處理流程中，模型進行計算與計費的最小基本語意單位為何？",
        "options": [
            "Byte（位元組）",
            "Token（標記/詞元）",
            "Word（英文字詞）",
            "Pixel（像素）"
        ],
        "answer": 1,
        "explanation": "Token 是大語言模型分詞（Tokenization）後的最小處理單位。一個 Token 可以是單詞、詞綴或漢字的一部分。一般而言，100 個英文單字約等於 130 個 Tokens，而一個繁體中文字通常會被切分成 1 至 3 個 Tokens。"
    },
    {
        "id": 4,
        "category": "基礎知識",
        "tags": ["必背", "專有名詞", "Tokenizer", "BPE"],
        "isMustMemorize": True,
        "question": "目前主流語言模型（如 GPT 系列）最廣泛採用的子詞分詞（Subword Tokenization）演算法為何？",
        "options": [
            "BPE（Byte-Pair Encoding，位元組對編碼）",
            "K-Means 分群演算法",
            "A* 尋路演算法",
            "Dijkstra 最短路徑演算法"
        ],
        "answer": 0,
        "explanation": "BPE（Byte-Pair Encoding）是一種統計式子詞分詞法，從單個字符出發，反覆迭代合併出現頻率最高的連續字符對，能以固定大小的詞表有效解決未登錄詞（OOV, Out-of-Vocabulary）問題。"
    },
    {
        "id": 5,
        "category": "基礎知識",
        "tags": ["必背", "專有名詞", "RLHF", "對齊"],
        "isMustMemorize": True,
        "question": "讓大型語言模型能理解人類指令意圖、符合人類價值觀且降低有害輸出的重要對齊技術「RLHF」其全名稱為何？",
        "options": [
            "Real-time Learning from Human Feedback",
            "Reinforcement Learning from Human Feedback（基於人類回饋的強化學習）",
            "Recurrent Logic with Heuristic Functions",
            "Random Linear Hyperparameter Fitting"
        ],
        "answer": 1,
        "explanation": "RLHF（Reinforcement Learning from Human Feedback）利用人類標註員對模型多個候選回答進行偏好排序，訓練出獎勵模型（Reward Model），再透過強化學習（如 PPO 演算法）微調 LLM，使其回答更有用、真實且無害。"
    },
    {
        "id": 6,
        "category": "基礎知識",
        "tags": ["必背", "專有名詞", "DPO", "直接偏好優化"],
        "isMustMemorize": True,
        "question": "近年興起、不需額外訓練獎勵模型即可直接透過偏好數據對 LLM 進行優化對齊的輕量技術為何？",
        "options": [
            "DPO（Direct Preference Optimization，直接偏好優化）",
            "CNN（卷積神經網絡）",
            "GAN（生成對抗網絡）",
            "PCA（主成分分析）"
        ],
        "answer": 0,
        "explanation": "DPO（Direct Preference Optimization）透過數學變形，證明可以在不顯式訓練獎勵模型和無需強化學習採樣的情況下，直接利用交叉熵損失對人類偏好資料進行微調，大幅提升訓練穩定度並節省顯存。"
    },
    {
        "id": 7,
        "category": "基礎知識",
        "tags": ["必背", "專有名詞", "Temperature", "溫度參數"],
        "isMustMemorize": True,
        "question": "在與 LLM 互動或調用 API 時，調節模型輸出「隨機性與創造力」的參數通常為何者？",
        "options": [
            "Max Tokens",
            "Temperature（溫度參數）",
            "Batch Size",
            "Dropout Rate"
        ],
        "answer": 1,
        "explanation": "Temperature 控制 Softmax 輸出的平滑程度。Temperature 趨近 0 時，模型幾乎只選取機率最高的詞（確定、嚴謹、邏輯高）；Temperature 提高（如 0.7~1.0）時，低機率詞被選取的機率增加，回答更具多樣性與創造力。"
    },
    {
        "id": 8,
        "category": "基礎知識",
        "tags": ["必背", "專有名詞", "Top-p", "Nucleus Sampling"],
        "isMustMemorize": True,
        "question": "LLM 採樣解碼機制中，動態截取「累積機率加總達到門檻值 p」的候選詞集合再進行抽樣的技術稱為？",
        "options": [
            "Top-k 採樣",
            "Top-p 採樣（核採樣，Nucleus Sampling）",
            "Greedy Search（貪婪搜尋）",
            "Beam Search（束搜尋）"
        ],
        "answer": 1,
        "explanation": "Top-p 採樣（核採樣）依機率由高到低累加候選詞，直到總和達到設定閥值 p（例如 0.9），僅在該集合內重新正規化機率後採樣。與固定數量的 Top-k 相比，Top-p 能依據上下文上下文動態調整候選詞數量。"
    },
    {
        "id": 9,
        "category": "基礎知識",
        "tags": ["必背", "專有名詞", "Hallucination", "幻覺"],
        "isMustMemorize": True,
        "question": "大型語言模型以流暢自信的語氣產出完全虛構、捏造或與客觀事實不符的內容，這種現象在學術與業界公認為？",
        "options": [
            "過擬合（Overfitting）",
            "幻覺（Hallucination）",
            "欠擬合（Underfitting）",
            "概念漂移（Concept Drift）"
        ],
        "answer": 1,
        "explanation": "Hallucination（幻覺）源自 LLM 的本質是「接續下一個可能 Token」的統計機率模型，缺乏事實世界的真值感知（Ground Truth），當遇知識盲區或統計偏誤時便會生成虛構答案。"
    },
    {
        "id": 10,
        "category": "基礎知識",
        "tags": ["必背", "專有名詞", "Context Window", "上下文長度"],
        "isMustMemorize": True,
        "question": "大型語言模型在單次互動對話中，所能同時容納與考慮的「輸入指示詞加輸出內容」之總 Token 上限稱為？",
        "options": [
            "Context Window（上下文視窗/長度）",
            "Hidden State（隱藏狀態）",
            "Memory Bandwidth（記憶體頻寬）",
            "Latency（延遲時間）"
        ],
        "answer": 0,
        "explanation": "Context Window（上下文視窗）代表模型一次能處理的總 Token 上限。超出該視窗的早期對話歷史會被截斷或遺忘。現今模型視窗從早期的 4K/8K 演進至 128K、1M 甚至 2M Tokens。"
    },
    {
        "id": 11,
        "category": "基礎知識",
        "tags": ["必背", "專有名詞", "Embedding", "詞嵌入向量"],
        "isMustMemorize": True,
        "question": "將文字、圖像等非結構化資料映射轉換為高維空間中的數值向量，以便利用數學距離計算語義關聯的技術稱為？",
        "options": [
            "雜湊化（Hashing）",
            "詞嵌入（Embedding）",
            "反編譯（Decompilation）",
            "無失真壓縮（Lossless Compression）"
        ],
        "answer": 1,
        "explanation": "Embedding（嵌入）將語意實體投影到數百至數千維的連續向量空間中。語意相似的詞彙或文本在空間中的距離（如餘弦距離 Cosine Similarity）較近，是向量檢索與 RAG 的基礎核心。"
    },
    {
        "id": 12,
        "category": "基礎知識",
        "tags": ["必背", "專有名詞", "Vector Database", "向量資料庫"],
        "isMustMemorize": True,
        "question": "專門用於儲存高維度嵌入向量，並支援「近似最近鄰（ANN）」高效率相似度搜尋的資料庫系統稱為？",
        "options": [
            "關聯式資料庫（RDBMS）",
            "向量資料庫（Vector Database）",
            "文件資料庫（Document DB）",
            "鍵值資料庫（Key-Value DB）"
        ],
        "answer": 1,
        "explanation": "向量資料庫（如 Pinecone、Milvus、Chroma、Qdrant）針對高維向量設計專門索引演算法（如 HNSW、IVF-Flat），能在毫秒內於百萬級資料中檢索出與查詢向量最相似的文件段落。"
    },
    {
        "id": 13,
        "category": "基礎知識",
        "tags": ["必背", "專有名詞", "Emergent Abilities", "湧現能力"],
        "isMustMemorize": True,
        "question": "當深度學習模型的規模（參數量、訓練數據量、運算資源）跨過某一臨界門檻時，突然展現出小模型所未具備的多步推理與解題能力，此特徵稱為？",
        "options": [
            "湧現能力（Emergent Abilities）",
            "維度災難（Curse of Dimensionality）",
            "梯度爆炸（Gradient Explosion）",
            "算力衰退（Compute Decay）"
        ],
        "answer": 0,
        "explanation": "Emergent Abilities（湧現能力）是指無法從小模型表現線性預測出的能力，當參數量通常突破百億（如 10B~100B）級別時，模型在三段論推理、心智模型（Theory of Mind）與代碼除錯能力上出現跳躍性躍升。"
    },
    {
        "id": 14,
        "category": "基礎知識",
        "tags": ["必背", "專有名詞", "Diffusion Model", "擴散模型"],
        "isMustMemorize": True,
        "question": "現代主流圖像生成 AI（如 Midjourney、Stable Diffusion）所採用的核心生成數學架構為何？",
        "options": [
            "擴散模型（Diffusion Models）",
            "線性迴歸（Linear Regression）",
            "決策樹（Random Forest）",
            "樸素貝氏（Naive Bayes）"
        ],
        "answer": 0,
        "explanation": "擴散模型原理分為兩階段：在前向過程中逐步向圖像添加高斯雜訊直到其完全成為純隨機雜訊；反向過程則訓練神經網絡（如 U-Net）逐步預測並剔除雜訊，從雜訊中還原生成逼真高解析影像。"
    },
    {
        "id": 15,
        "category": "基礎知識",
        "tags": ["必背", "專有名詞", "Multimodal", "多模態"],
        "isMustMemorize": True,
        "question": "能夠同時理解、關聯並生成跨文字、圖像、音訊及影像等多種異質資料形態的人工智慧系統稱為？",
        "options": [
            "單模態 AI（Unimodal AI）",
            "多模態 AI（Multimodal AI）",
            "邊緣 AI（Edge AI）",
            "分散式 AI（Distributed AI）"
        ],
        "answer": 1,
        "explanation": "Multimodal（多模態）系統（如 GPT-4o、Gemini 1.5）打破以往純文字對話框架，具備統合感知多種媒體信號並進行跨模態推演（如給予電路圖照片診斷故障問題）的能力。"
    },
    {
        "id": 16,
        "category": "基礎知識",
        "tags": ["必背", "專有名詞", "LoRA", "低秩適應"],
        "isMustMemorize": True,
        "question": "在對大模型進行微調時，凍結預訓練權重並透過低秩矩陣分解大幅減少可訓練參數量的高效率微調技術稱為？",
        "options": [
            "LoRA（Low-Rank Adaptation，低秩適應）",
            "全量參數微調（Full Fine-Tuning）",
            "網格搜尋（Grid Search）",
            "資料擴增（Data Augmentation）"
        ],
        "answer": 0,
        "explanation": "LoRA 凍結原模型龐大參數，僅在神經網絡層中旁路增加低秩矩陣（A 與 B，通常秩 rank 僅 4 到 64），可將可訓練參數量降低至原來的 1% 以下，讓消費級顯卡也能高效微調大模型。"
    },
    {
        "id": 17,
        "category": "基礎知識",
        "tags": ["必背", "專有名詞", "Quantization", "模型量化"],
        "isMustMemorize": True,
        "question": "將神經網絡權重從高精度浮點數（如 FP32 或 FP16）壓縮轉換為低精度格式（如 INT8 或 INT4），以降低顯存佔用並加速推理的技術稱為？",
        "options": [
            "模型量化（Model Quantization）",
            "模型蒸餾（Model Distillation）",
            "特徵工程（Feature Engineering）",
            "正則化（Regularization）"
        ],
        "answer": 0,
        "explanation": "Quantization（量化）能大幅降低顯存需求（例如 70B 模型從 FP16 的 140GB 顯存壓縮至 4-bit 的 40GB），使大型模型能在消費級硬體或本地邊緣端順暢執行。"
    },
    {
        "id": 18,
        "category": "基礎知識",
        "tags": ["必背", "專有名詞", "Grounding", "基礎錨定"],
        "isMustMemorize": True,
        "question": "將 LLM 的回答與客觀真實世界資料來源、可查證的事實資料庫或上下文緊密連結，以抑制幻覺發生的機制稱為？",
        "options": [
            "Grounding（基礎錨定/實境對齊）",
            "Pruning（剪枝）",
            "Tokenization（分詞）",
            "Overfitting（過擬合）"
        ],
        "answer": 0,
        "explanation": "Grounding（錨定）是指讓模型的語言生成根植於外部可驗證的知識來源（例如搜尋引擎結果或公司內部文檔庫），確保生成的每一句話皆有據可查。"
    },
    {
        "id": 19,
        "category": "基礎知識",
        "tags": ["必背", "專有名詞", "Discriminative", "鑑別式AI"],
        "isMustMemorize": True,
        "question": "傳統機器學習中的「鑑別式模型（Discriminative Model）」其核心數學目標是計算何種機率？",
        "options": [
            "給定特徵 x 下標籤 y 的條件機率 P(y|x)",
            "特徵與標籤的聯合機率分佈 P(x, y)",
            "資料生成邊際機率 P(x)",
            "隨機先驗機率 P(x|y)"
        ],
        "answer": 0,
        "explanation": "鑑別式 AI（如邏輯迴歸、SVM、影像分類 CNN）專注於學習不同類別之間的決策邊界，計算 P(y|x)；而生成式 AI（Generative AI）則是學習資料的聯合機率分佈 P(x, y) 或 P(x)，進而具備採樣生成全新資料樣本的能力。"
    },
    {
        "id": 20,
        "category": "基礎知識",
        "tags": ["必背", "專有名詞", "Zero-shot", "零樣本學習"],
        "isMustMemorize": True,
        "question": "在與大模型互動時，完全不提供任何示範樣本（Examples），直接要求模型理解任務並產生回答的推論模式稱為？",
        "options": [
            "Zero-shot Learning（零樣本學習）",
            "Few-shot Learning（少樣本學習）",
            "One-shot Learning（單樣本學習）",
            "Unsupervised Pre-training（非監督預訓練）"
        ],
        "answer": 0,
        "explanation": "Zero-shot 是最直接的推論形式，提示詞中只有任務指示與輸入文字，不包含任何答題範例，依賴預訓練過程中習得的泛化常識直接求解。"
    }
]
