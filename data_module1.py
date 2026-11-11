# -*- coding: utf-8 -*-
"""
Module 1: 生成式 AI 基礎知識與核心原理 (100 題)
ID: 1 ~ 100
"""

def get_module1_questions():
    CATEGORY = "基礎知識"
    questions = []

    def q(qid, is_must, tags, question, options, ans_idx, explanation):
        questions.append({
            "id": qid,
            "category": CATEGORY,
            "tags": tags,
            "isMustMemorize": is_must,
            "question": question,
            "options": options,
            "answer": ans_idx,
            "explanation": explanation
        })

    # --- 必背專有名詞 (1-20) ---
    q(1, True, ["必背", "專有名詞", "Transformer"],
      "現今主流大型語言模型（如 GPT-4、Claude、Gemini）底層最核心的深度學習架構為何？",
      ["CNN（卷積神經網絡）", "RNN（遞歸神經網絡）", "Transformer", "SVM（支援向量機）"], 2,
      "2017 年 Google 提出 Transformer 架構，其自注意力機制克服了傳統 RNN 無法高度平行化與長距離記憶喪失的限制，成為現代所有 LLM 的核心基石。")

    q(2, True, ["必背", "專有名詞", "Self-Attention"],
      "Transformer 架構中，用來計算輸入文本中每個詞與所有其他詞之間關聯權重的核心機制稱為？",
      ["反向傳播（Backpropagation）", "自注意力機制（Self-Attention）", "隨機梯度下降（SGD）", "最大池化（Max Pooling）"], 1,
      "Self-Attention（自注意力機制）透過 Query、Key、Value 三組向量矩陣運算，動態衡量句子內部各 Token 間的關聯強度，精確捕捉跨長句的語法與語義連結。")

    q(3, True, ["必背", "專有名詞", "Token"],
      "在大型語言模型（LLM）的文字處理流程中，模型進行計算與計費的最小基本語意單位為何？",
      ["Byte（位元組）", "Token（標記/詞元）", "Word（單詞）", "Pixel（像素）"], 1,
      "Token 是大語言模型分詞（Tokenization）後的最小處理單位。一般 100 個英文單字約等於 130 個 Tokens，而一個繁體中文字通常佔用 1 至 3 個 Tokens。")

    q(4, True, ["必背", "專有名詞", "BPE"],
      "主流大型語言模型最廣泛採用的子詞分詞（Subword Tokenization）演算法為何？",
      ["BPE（Byte-Pair Encoding，位元組對編碼）", "K-Means 分群", "A* 尋路演算法", "Dijkstra 最短路徑"], 0,
      "BPE 是一種統計式子詞分詞法，從單字符出發反覆合併最高頻的連續字符對，能以固定大小的詞表有效解決未登錄詞（OOV）問題。")

    q(5, True, ["必背", "專有名詞", "RLHF"],
      "讓大型語言模型能理解人類意圖、符合人類價值觀並降低有害輸出的重要對齊技術「RLHF」全名為何？",
      ["Real-time Learning from Human Feedback", "Reinforcement Learning from Human Feedback（基於人類回饋的強化學習）", "Recurrent Logic with Heuristic Functions", "Random Linear Hyperparameter Fitting"], 1,
      "RLHF 利用人類標註員對模型多個候選回答進行偏好排序訓練出獎勵模型，再透過強化學習（如 PPO）微調 LLM，使其回答更有用、真實且無害。")

    q(6, True, ["必背", "專有名詞", "DPO"],
      "近年興起、不需額外訓練獎勵模型即可直接透過偏好數據對 LLM 進行優化對齊的輕量技術為何？",
      ["DPO（Direct Preference Optimization，直接偏好優化）", "CNN（卷積神經網絡）", "GAN（生成對抗網絡）", "PCA（主成分分析）"], 0,
      "DPO 透過數學推導證明可在不顯式訓練獎勵模型和無需強化學習採樣的情況下，直接利用交叉熵損失對偏好數據微調，大幅提升訓練穩定度並節省顯存。")

    q(7, True, ["必背", "專有名詞", "Temperature"],
      "在與 LLM 互動或調用 API 時，調節模型輸出「隨機性與創造力」的參數通常為何者？",
      ["Max Tokens", "Temperature（溫度參數）", "Batch Size", "Dropout Rate"], 1,
      "Temperature 控制 Softmax 輸出的平滑度。接近 0 時輸出高度確定嚴謹；提高（如 0.7~1.0）時低機率詞被選取的機率增加，回答更具多樣性與創造力。")

    q(8, True, ["必背", "專有名詞", "Top-p"],
      "LLM 採樣解碼機制中，動態截取「累積機率加總達到門檻值 p」的候選詞集合再進行抽樣的技術稱為？",
      ["Top-k 採樣", "Top-p 採樣（核採樣，Nucleus Sampling）", "Greedy Search（貪婪搜尋）", "Beam Search（束搜尋）"], 1,
      "Top-p 採樣依機率由高到低累加候選詞直到累積機率達到 p（如 0.9），僅在該集合內重新正規化後採樣，能依上下文動態過濾長尾離譜詞。")

    q(9, True, ["必背", "專有名詞", "Hallucination"],
      "大型語言模型以流暢自信的語氣產出完全虛構、捏造或與客觀事實不符的內容，這種現象稱為？",
      ["過擬合（Overfitting）", "幻覺（Hallucination）", "欠擬合（Underfitting）", "概念漂移（Concept Drift）"], 1,
      "幻覺源自 LLM 本質是「接續下一個可能 Token」的統計機率模型，缺乏對物理與客觀世界的絕對真值感知，當遇知識盲區便會依機率拼湊虛假事實。")

    q(10, True, ["必背", "專有名詞", "Context Window"],
      "大型語言模型在單次互動對話中，所能同時容納與考慮的「輸入指示詞加輸出內容」總 Token 上限稱為？",
      ["Context Window（上下文視窗/長度）", "Hidden State（隱藏狀態）", "Memory Bandwidth", "Latency"], 0,
      "Context Window 代表模型單次推論能處理的總 Token 上限。超出該視窗的早期歷史會被截斷或遺忘。現今模型視窗已擴展至 128K 甚至 2M Tokens。")

    q(11, True, ["必背", "專有名詞", "Embedding"],
      "將文字、圖像等非結構化資料映射轉換為高維空間中的連續數值向量，以便衡量其語意相似度的技術稱為？",
      ["雜湊化（Hashing）", "詞嵌入（Embedding）", "反編譯（Decompilation）", "無失真壓縮"], 1,
      "Embedding 將語義實體投影到數百至數千維的連續向量空間中，語意相近的內容在空間中的距離（如餘弦距離）較近，是向量檢索與 RAG 的基石。")

    q(12, True, ["必背", "專有名詞", "Vector Database"],
      "專門用於儲存高維度嵌入向量，並支援「近似最近鄰（ANN）」高效率相似度搜尋的系統稱為？",
      ["關聯式資料庫（RDBMS）", "向量資料庫（Vector Database）", "文件資料庫（Document DB）", "鍵值資料庫（Key-Value DB）"], 1,
      "向量資料庫（如 Pinecone、Milvus、Chroma、Qdrant）針對高維向量設計索引（如 HNSW），能在毫秒內於海量資料中檢索出與查詢向量最相似的文件段落。")

    q(13, True, ["必背", "專有名詞", "Emergent Abilities"],
      "當深度學習模型規模跨過某一臨界門檻時，突然展現出小模型所未具備的多步推理與解題能力，此特徵稱為？",
      ["湧現能力（Emergent Abilities）", "維度災難（Curse of Dimensionality）", "梯度爆炸", "算力衰退"], 0,
      "湧現能力是指無法從小模型表現線性外推預測出的能力，當參數量通常突破百億（10B~100B）級別時，模型在三段論推理、代碼除錯能力上出現質的飛躍。")

    q(14, True, ["必背", "專有名詞", "Diffusion Model"],
      "現代主流圖像生成 AI（如 Midjourney、Stable Diffusion）所採用的核心生成數學架構為何？",
      ["擴散模型（Diffusion Models）", "線性迴歸", "決策樹", "樸素貝氏"], 0,
      "擴散模型前向過程逐步向圖像加入高斯雜訊直到純雜訊；反向過程訓練神經網絡逐步預測並剔除雜訊，從隨機雜訊中還原出逼真高解析影像。")

    q(15, True, ["必背", "專有名詞", "Multimodal"],
      "能夠同時理解、關聯並生成跨文字、圖像、音訊及影像等多種異質資料形態的人工智慧系統稱為？",
      ["單模態 AI", "多模態 AI（Multimodal AI）", "邊緣 AI", "分散式 AI"], 1,
      "Multimodal（多模態）系統打破傳統純文字框架，具備跨媒體信號統合感知與跨模態推演（如給予電路圖照片診斷故障問題）的能力。")

    q(16, True, ["必背", "專有名詞", "LoRA"],
      "在對大模型進行微調時，凍結預訓練權重並透過低秩矩陣分解大幅減少可訓練參數量的高效率微調技術稱為？",
      ["LoRA（Low-Rank Adaptation，低秩適應）", "全量參數微調", "網格搜尋", "資料擴增"], 0,
      "LoRA 凍結原模型龐大參數，僅旁路增加低秩分解矩陣，可將可訓練參數量降低至原來的 1% 以下，讓消費級顯卡也能高效微調大模型。")

    q(17, True, ["必背", "專有名詞", "Quantization"],
      "將神經網絡權重從高精度浮點數（如 FP16）壓縮轉換為低精度格式（如 INT8 或 INT4），以降低顯存佔用並加速推理的技術稱為？",
      ["模型量化（Model Quantization）", "模型蒸餾", "特徵工程", "正則化"], 0,
      "Quantization（量化）大幅降低顯存需求（如 70B 模型從 FP16 的 140GB 顯存壓縮至 4-bit 的 40GB），使大模型能在本地邊緣端順暢執行。")

    q(18, True, ["必背", "專有名詞", "Grounding"],
      "將 LLM 的回答與客觀真實世界資料來源、可查證的事實資料庫或上下文緊密連結，以抑制幻覺發生的機制稱為？",
      ["Grounding（基礎錨定/實境對齊）", "Pruning（剪枝）", "Tokenization", "Overfitting"], 0,
      "Grounding（錨定）讓模型的語言生成根植於外部可驗證的權威知識來源，確保生成的每一句話皆有真實數據作為支撐。")

    q(19, True, ["必背", "專有名詞", "Discriminative"],
      "傳統機器學習中的「鑑別式模型（Discriminative Model）」其核心數學目標是計算何種機率？",
      ["給定特徵 x 下標籤 y 的條件機率 P(y|x)", "特徵與標籤的聯合機率分佈 P(x, y)", "資料生成邊際機率 P(x)", "隨機先驗機率 P(x|y)"], 0,
      "鑑別式 AI（如分類器、SVM）專注於學習不同類別間的決策邊界 P(y|x)；生成式 AI 則是學習資料分佈 P(x, y) 或 P(x)，進而具備採樣生成全新資料樣本的能力。")

    q(20, True, ["必背", "專有名詞", "Zero-shot"],
      "在與大模型互動時，完全不提供任何示範樣本（Examples），直接要求模型理解任務並產生回答的推論模式稱為？",
      ["Zero-shot Learning（零樣本學習）", "Few-shot Learning", "One-shot Learning", "Unsupervised Pre-training"], 0,
      "Zero-shot 是最直接的推論形式，提示詞中只有任務指示與輸入文字，不包含任何答題範例，依賴預訓練過程中習得的通用常識直接求解。")

    # --- 核心架構與參數深入 (21-40) ---
    q(21, False, ["架構原理", "Scaling Law"],
      "描述大語言模型的性能（如測試損失 Loss）隨著模型參數量、數據集規模及計算量呈指數冪律穩定提升的經驗法則稱為？",
      ["摩爾定律（Moore's Law）", "尺度定律（Scaling Law）", "安達爾定律（Amdahl's Law）", "吉布斯現象"], 1,
      "Kaplan 等人提出的 Scaling Law（尺度定律）指出 LLM 性能與計算量、數據量、參數量之間存在精確的冪律關係，為現代千億級大模型投資提供理論基礎。")

    q(22, False, ["架構原理", "MoE"],
      "將模型內部切分為多個專業子網絡，每次推論時僅由門控機制（Router）激活其中少數幾個網絡以提升運算效率的架構為何？",
      ["MoE（Mixture of Experts，混合專家架構）", "Dense Network（稠密神經網絡）", "單層感知機", "自編碼器"], 0,
      "MoE 架構（如 Mixtral 8x7B）在維持龐大總參數量知識庫的同時，每次推論僅激活部分專家網絡（如 8 個中取 2 個），顯著降低推論運算成本並提高生成速度。")

    q(23, False, ["模型優化", "Model Distillation"],
      "利用參數量龐大的高性能「教師模型（Teacher Model）」輸出機率分佈，引導訓練輕量級「學生模型（Student Model）」的技術稱為？",
      ["模型蒸餾（Model Distillation）", "模型量化", "權重剪枝", "超參數調優"], 0,
      "知識蒸餾將教師模型的「軟標籤（Soft Targets）」知識轉移至緊湊的學生模型，使小模型在較少參數下繼承大模型的高階推理能力。")

    q(24, False, ["模型優化", "Pruning"],
      "將神經網絡中數值接近零或對輸出貢獻微弱的權重連線移除，以減少模型體積與計算量的技術稱為？",
      ["模型剪枝（Pruning）", "特徵提取", "數據清洗", "批次歸一化"], 0,
      "Pruning（剪枝）分為非結構化剪枝與結構化剪枝（移除整個注意力頭或神經元），可有效剔除冗餘參數量並提升硬體吞吐量。")

    q(25, False, ["評估指標", "Perplexity"],
      "在自然語言處理中，用來量化評估語言模型預測下一個 Token「迷茫或不確定程度」的標準指標為？",
      ["困惑度（Perplexity, PPL）", "準確率（Accuracy）", "召回率（Recall）", "F1 分數"], 0,
      "Perplexity（PPL）是交叉熵損失的指數次方。PPL 數值越低，代表語言模型對下一個單詞預測越有把握、語言流暢度越高。")

    q(26, False, ["架構細節", "Positional Encoding"],
      "Transformer 本身不具備遞歸結構，為使模型能感知單詞在句子中的先後順序，必須加入何種機制？",
      ["位置編碼（Positional Encoding）", "殘差連接（Residual Connection）", "層正規化（LayerNorm）", "Dropout"], 0,
      "位置編碼（如正弦位置編碼或 RoPE 旋轉位置編碼）為每個 Token 注入空間時序資訊，使自注意力運算能辨別前後語義差異。")

    q(27, False, ["架構細節", "RoPE"],
      "現今主流開源大模型（如 Llama 3、Mistral）普遍採用且易於外推擴展長上下文的相對位置編碼技術為何？",
      ["RoPE（Rotary Position Embedding，旋轉位置編碼）", "絕對正弦編碼", "Learned Position Embedding", "One-hot 編碼"], 0,
      "RoPE 透過旋轉矩陣將相對位置信息融入 Query 與 Key 向量中，具有優秀的相對位置表達力，並能透過插值演算法大幅拓展長上下文能力。")

    q(28, False, ["推論加速", "KV Cache"],
      "在 LLM 自回歸生成過程中，為避免重複計算已生成歷史 Token 的注意力矩陣，常採用的快取優化技術為何？",
      ["KV Cache（Key-Value 快取）", "Page Swap", "DNS 快取", "LRU Cache"], 0,
      "自回歸解碼每生成一個新 Token 只需計算當前 Token 的 Query，其餘歷史 Token 的 Key 和 Value 矩陣儲存於顯存的 KV Cache 中以空間換取時間。")

    q(29, False, ["推論系統", "PagedAttention"],
      "由 vLLM 推論框架提出，模仿作業系統虛擬記憶體分頁機制，徹底解決 KV Cache 顯存碎片化問題的演算法為何？",
      ["PagedAttention", "FlashAttention", "Multi-Query Attention", "Grouped-Query Attention"], 0,
      "PagedAttention 將連續的 KV Cache 儲存在非連續的物理顯存塊（Blocks）中，將 KV Cache 的顯存浪費率從 60~80% 降至 4% 以下，大幅提升高併發吞吐量。")

    q(30, False, ["推論系統", "FlashAttention"],
      "利用 GPU 的 SRAM 高速記憶體重新設計注意力計算排程，避免高耗能 HBM 存取的精確注意力加速演算法為何？",
      ["FlashAttention", "Quantization", "Speculative Decoding", "LoRA"], 0,
      "FlashAttention 透過切塊（Tiling）和在反向傳播中重新計算注意力中間量，大幅減少 GPU 高頻寬記憶體（HBM）讀寫次數，顯著提升速度並降低顯存消耗。")

    q(31, False, ["注意力機制", "GQA"],
      "在 Multi-Head Attention（MHA）與 Multi-Query Attention（MQA）之間取得最佳平衡，讓多個 Query 頭共享一組 Key/Value 的機制為？",
      ["GQA（Grouped-Query Attention，分組查詢注意力）", "Cross-Attention", "Sparse Attention", "Linear Attention"], 0,
      "Llama 2/3 採用的 GQA 將 Query 頭分成數組，每組共享一對 KV 頭，在幾乎不損失模型精度的前提下顯著壓縮 KV Cache 顯存佔用。")

    q(32, False, ["訓練概念", "Catastrophic Forgetting"],
      "當對預訓練好的大型語言模型進行特定領域資料微調時，模型突然喪失原本具備的通用常識或數學推理能力，此現象稱為？",
      ["災難性遺忘（Catastrophic Forgetting）", "維度災難", "過度對齊（Over-alignment）", "模式崩潰（Mode Collapse）"], 0,
      "災難性遺忘是指神經網絡在學習新權重時覆蓋了舊知識權重。實務上常透過回放少量通用數據或採用 LoRA 等參數量化方法來緩解。")

    q(33, False, ["對齊概念", "Alignment Tax"],
      "在對模型進行嚴格的安全性對齊（如防止有害回覆）後，導致模型在一般程式編寫或數學解題能力上出現些微退化的代價稱為？",
      ["對齊稅（Alignment Tax）", "推論延遲", "泛化誤差", "邊際成本"], 0,
      "Alignment Tax 指為了讓模型合乎人類道德規範而進行額外懲罰對齊時，模型過於保守或過度泛化拒答，導致正常認知推理指標些微下降的代價。")

    q(34, False, ["訓練細節", "SFT"],
      "在大模型訓練生命週期中，預訓練完成之後、RLHF 之前的關鍵中繼步驟，使用高品質問答對進行引導的階段為何？",
      ["SFT（Supervised Fine-Tuning，監督式微調）", "特徵選擇", "無監督分群", "模型剪枝"], 0,
      "SFT 讓預訓練模型學會「像助手一樣對話」的格式規範，將單純的接龍補全能力轉化為理解並遵循人類 Prompt 指令的能力。")

    q(35, False, ["採樣演算法", "Greedy Decoding"],
      "在文本生成解碼過程中，永遠只選取下一個預測機率最高的那一個單詞（相當於 Temperature=0）的解碼策略稱為？",
      ["貪婪搜尋（Greedy Search）", "核採樣", "隨機漫步", "馬可夫鏈"], 0,
      "Greedy Search 每一步皆選取條件機率最大的 Token，運算速度最快且結果 100% 可復現，但在長文本生成中易陷入循環重複。")

    q(36, False, ["採樣演算法", "Beam Search"],
      "在每一步解碼時維持保留累積機率最高的固定數量（Beam Width）個候選序列，常用於翻譯或摘要的搜尋演算法為何？",
      ["束搜尋（Beam Search）", "深度優先搜尋（DFS）", "廣度優先搜尋（BFS）", "隨機抽樣"], 0,
      "Beam Search 是貪婪搜尋的廣義擴展，能有效在全局尋找高累積機率的生成路徑，在跨語言機器翻譯任務中廣泛應用。")

    q(37, False, ["推論加速", "Speculative Decoding"],
      "利用小型輔助模型快速草擬多個 Token，再由大模型進行單次驗證平行接受的非失真加速推論技術稱為？",
      ["投機解碼（Speculative Decoding）", "量化壓縮", "剪枝合併", "模型分片"], 0,
      "投機解碼（Speculative Decoding）利用小模型低延遲生成候選 Token，大模型只需單次前向傳播即可平行驗證多個 Token，能獲得 2~3 倍推論加速且輸出分佈完全一致。")

    q(38, False, ["多模態視覺", "CLIP"],
      "OpenAI 提出利用海量圖像與對應文字描述進行「對比學習（Contrastive Learning）」，將視覺與文本映射至同一特徵空間的模型為？",
      ["CLIP（Contrastive Language-Image Pre-training）", "ResNet", "YOLO", "AlexNet"], 0,
      "CLIP 透過對比損失拉近配對圖文的向量距離，使模型具備強大的 Zero-shot 圖像分類能力，並成為 DALL-E 與 Stable Diffusion 的文字引導核心。")

    q(39, False, ["多模態視覺", "Vision Transformer"],
      "將輸入圖像切分成多個固定大小的 Patch（如 16x16 像素）並視為 Token 輸入標準 Transformer 架構的模型架構稱為？",
      ["ViT（Vision Transformer）", "CNN", "U-Net", "RNN"], 0,
      "ViT 證明了 Transformer 架構不僅適用於自然語言，直接應用於圖像 Patch 序列亦能在超大數據集預訓練下超越傳統卷積神經網絡。")

    q(40, False, ["擴散模型原理", "CFG"],
      "在文字生成圖像（如 Stable Diffusion）中，用來控制模型遵循提示詞嚴格程度的超參數「CFG Scale」全名為何？",
      ["Classifier-Free Guidance Scale", "Continuous Forward Gradient", "Convolution Feature Gate", "Cosine Frequency Gain"], 0,
      "CFG Scale 數值越高，圖像生成越嚴格貼合 Prompt 描述（但過高易造成色彩過飽和或失真）；數值適中時畫面最具自然美感。")

    # --- 模型實務評估、記憶體與工程 (41-60) ---
    q(41, False, ["模型評估", "MMLU"],
      "涵蓋人文、社會科學、STEM 等 57 個跨學科領域專業知識，廣泛用於衡量大模型通用知識理解水平的基準評測為？",
      ["MMLU（Massive Multitask Language Understanding）", "ImageNet", "MNIST", "GLUE"], 0,
      "MMLU 是衡量現代 LLM 跨領域學術知識與常識理解的黃金基準之一，題目涵蓋初等數學到專業醫學、法律選擇題。")

    q(42, False, ["模型評估", "GSM8K"],
      "專門用於評估大語言模型「小學等級多步驟數學應用題推理能力」的經典測試數據集為？",
      ["GSM8K（Grade School Math 8K）", "HumanEval", "SQuAD", "COCO"], 0,
      "GSM8K 包含 8,500 題需要 2 到 8 步四則運算的多步驟數學文字題，常用於檢驗模型 Chain-of-Thought（思維鏈）能力。")

    q(43, False, ["模型評估", "HumanEval"],
      "由 OpenAI 發布，專門用於評估大語言模型「Python 程式碼自動生成與功能正確性」的標準測試集為何？",
      ["HumanEval", "ImageNet", "BLEU", "ROUGE"], 0,
      "HumanEval 包含 164 題具備單元測試的演算法編程題，採用 pass@k 指標衡量生成代碼是否能通過所有單元測試。")

    q(44, False, ["評估指標", "BLEU"],
      "在機器翻譯與文字生成評估中，透過計算候選文本與參考文本之間 n-gram 重疊精確率的指標為？",
      ["BLEU Score", "ROUGE Score", "Perplexity", "Accuracy"], 0,
      "BLEU（Bilingual Evaluation Understudy）著重於評估生成文字的「精確率（Precision）」，特別是 n-gram 詞組在參考譯文中出現的比例。")

    q(45, False, ["評估指標", "ROUGE"],
      "在自動文本摘要任務中，著重計算生成摘要涵蓋參考文本重點「召回率（Recall）」的主流指標為？",
      ["ROUGE Score（Recall-Oriented Understudy for Gesting Evaluation）", "BLEU", "Top-k", "Cross-Entropy"], 0,
      "ROUGE 評測指標著眼於召回率，常見有 ROUGE-1（單字重疊）、ROUGE-2（雙字重疊）及 ROUGE-L（最長共同子序列 LCS）。")

    q(46, False, ["長文本架構", "Needle In A Haystack"],
      "測試大模型在數萬至百萬 Token 的超長文本中精準檢索單一隱蔽關鍵事實能力的評測方法稱為？",
      ["Needle in a Haystack（大海撈針測試）", "A/B 測試", "圖靈測試", "壓力測試"], 0,
      "大海撈針測試將一句隨機事實（如密碼或特殊人名）隨機插入在長篇小說或技術文檔的不同深度位置，檢測模型是否能 100% 成功檢索召回。")

    q(47, False, ["記憶體機制", "Lost in the Middle"],
      "研究發現多數 LLM 在處理長文本輸入時，對位於文本開頭與結尾的資訊記憶最牢固，而容易忽略位於中間段落資訊的現象稱為？",
      ["Lost in the Middle（迷失在中間）", "冷啟動問題", "災難性遺忘", "梯度消失"], 0,
      "由於自注意力權重分佈特性，模型普遍存在「首因效應（Primacy Effect）」與「近因效應（Recency Effect）」，核心指令放置於首尾表現最佳。")

    q(48, False, ["量化格式", "GGUF"],
      "專為 llama.cpp 設計、廣泛用於個人電腦 CPU/GPU 本地高效率運行開源大模型的文件封裝格式為何？",
      ["GGUF（GPT-Generated Unified Format）", "APK", "EXE", "ZIP"], 0,
      "GGUF 是 GGML 的升級版格式，將模型權重、分詞器、超參數打包為單一跨平台二進位檔，支援多種 2-bit 到 8-bit 量化。")

    q(49, False, ["模型微調", "QLoRA"],
      "將底層預訓練模型權重進行 4-bit NormalFloat 量化，並在量化權重上附加 LoRA 適應層以進一步降低顯存消耗的技術稱為？",
      ["QLoRA（Quantized Low-Rank Adaptation）", "Full Tuning", "Prefix Tuning", "Distillation"], 0,
      "QLoRA 透過雙重反向殘差量化與分頁優化器，能在單張消費級顯卡（如 RTX 3090/4090 24GB）上微調原本需要數百 GB 顯存的 70B 模型。")

    q(50, False, ["推論指標", "TTFT"],
      "評估大模型在線上互動服務中，從使用者發送請求到收到模型吐出「第一個 Token」所需等待的延遲指標稱為？",
      ["TTFT（Time to First Token，首字延遲）", "TPS（Tokens Per Second）", "FLOPs", "QPS"], 0,
      "TTFT 取決於 Prompt 的 Prefill（預填充）速度，直接影響使用者的首字感知等待體驗；後續流式傳輸體驗則由 TPS（每秒生成 Token 數）決定。")

    # --- 進階理論與技術生態 (51-100) ---
    q(51, False, ["模型架構", "Decoder-Only"],
      "GPT 系列、Llama 系列等現今絕大多數主流自回歸語言模型所採用的 Transformer 架構變體為何？",
      ["Decoder-Only（純解碼器架構）", "Encoder-Only", "Encoder-Decoder", "CNN-Hybrid"], 0,
      "不同於 BERT（純編碼器）或 T5（編碼-解碼器），純解碼器架構透過因果遮罩（Causal Mask）預測下一個 Token，已被證明在通用生成與 Scaling 上最具泛化性。")

    q(52, False, ["注意力機制", "Causal Masking"],
      "在 Decoder-Only 架構中，防止模型在訓練時「提前偷看」未來位置 Token 的遮罩機制稱為？",
      ["因果遮罩（Causal Masking / Look-ahead Mask）", "隨機遮罩", "Dropout", "Padding Mask"], 0,
      "因果遮罩是一個下三角矩陣，強制每個位置的 Token 只能對其自身及前方已生成的 Token 計算注意力分數，確保自回歸生成合乎時序。")

    q(53, False, ["模型格式", "AWQ"],
      "發現神經網絡中僅有 1% 的顯著權重對精度至關重要，透過保護這些顯著通道實現無損低延遲 4-bit 量化的技術為？",
      ["AWQ（Activation-aware Weight Quantization）", "GPTQ", "FP8", "BF16"], 0,
      "AWQ 透過分析激活值分佈找出關鍵特徵通道並進行保護縮放，在兼顧極高推論吞吐量的同時幾乎維持與 FP16 相同的模型精度。")

    q(54, False, ["分散式計算", "Tensor Parallelism"],
      "在超大規模模型分散式推論中，將單個矩陣乘法運算切分至多張不同 GPU 顯卡平行計算的技術稱為？",
      ["張量平行（Tensor Parallelism）", "流水線平行（Pipeline Parallelism）", "數據平行（Data Parallelism）", "模型量化"], 0,
      "Megatron-LM 等框架使用的張量平行在神經網絡層內部將權重矩陣按行或列切割，透過 GPU 間的 NVLink 高速互聯在單步推論內進行通信。")

    q(55, False, ["計算架構", "NPU"],
      "現代智慧型手機晶片與 AI PC 中，專門用來硬體加速神經網絡矩陣卷積運算、具備極低功耗特性的專用處理器為何？",
      ["NPU（Neural Processing Unit，神經處理單元）", "CPU", "GPU", "DSP"], 0,
      "NPU 針對深度學習常見的乘積累加（MAC）矩陣運算進行專屬電路設計，能在極低功耗下高效執行本機端小型語言模型（SLM）。")

    q(56, False, ["開源模型", "SLM"],
      "參數量在 1B 到 8B 之間、能在筆電或手機端本機離線流暢運行的「小型語言模型」英文縮寫為何？",
      ["SLM（Small Language Model）", "LLM", "AGI", "ASR"], 0,
      "SLM（如 Microsoft Phi-3、Google Gemma 2 2B、Llama 3 8B）以高品質合成資料集訓練，具備低延遲、保護隱私且硬體門檻低的優勢。")

    q(57, False, ["影像控制", "ControlNet"],
      "在 Stable Diffusion 中，允許使用者透過線稿（Canny）、人體骨架（OpenPose）或深度圖（Depth）精準控制畫面生成構圖的外掛神經網絡為？",
      ["ControlNet", "LoRA", "Textual Inversion", "Hypernetwork"], 0,
      "ControlNet 凍結原本的擴散模型權重並建立訓練分支，為生成影像引入結構幾何空間約束，徹底解決 AI 繪圖難以精確構圖的痛點。")

    q(58, False, ["影像控制", "Inpainting"],
      "在現有圖片上框選特定區域塗抹遮罩（Mask），要求 AI 僅重繪修改遮罩內部內容而保留其餘背景完好的技術稱為？",
      ["局部重繪（Inpainting）", "外繪擴圖（Outpainting）", "風格遷移", "超解析度放大"], 0,
      "Inpainting（內繪/局部重繪）讓設計師能精確修飾畫面瑕疵（如修復多餘手指、更換人物服裝顏色），是商業落地修圖的重要功能。")

    q(59, False, ["影像控制", "Outpainting"],
      "將原始畫面向外延伸擴展畫布邊界，並讓 AI 依據原圖內容無縫銜接生成畫面外圍全新場景的技術稱為？",
      ["外繪擴圖（Outpainting）", "局部重繪（Inpainting）", "去背遮罩", "色彩校正"], 0,
      "Outpainting 允許使用者將正方形圖片擴展為 16:9 橫幅或寬幅全景圖，模型會自動推斷並補齊視野外合理的環境細節。")

    q(60, False, ["擴散模型", "Latent Diffusion"],
      "Stable Diffusion 之所以能在消費級顯卡快速生成高解析圖片，是因為其將擴散與去噪運算置於何種空間執行？",
      ["潛在空間（Latent Space / 壓縮空間）", "像素空間（Pixel Space）", "二值化空間", "向量空間"], 0,
      "Latent Diffusion 先利用 VAE 自編碼器將高解析像素壓縮 8 倍至潛在空間進行去噪生成，大幅降低計算維度與顯存消耗。")

    q(61, False, ["架構原理", "Self-Consistency"],
      "在複雜推論任務中，讓模型以較高溫度多次生成多條不同的思考解題路徑，最終以「多數決（Majority Vote）」選取最常出現答案的技術為？",
      ["自洽性採樣（Self-Consistency）", "思維鏈（CoT）", "束搜尋", "隨機丟棄"], 0,
      "Self-Consistency 模擬人類透過不同解法推導答案的過程，透過在多個獨立解題路徑中進行多數表決，顯著消除單一路徑的隨機推理失誤。")

    q(62, False, ["模型架構", "Reasoning Models"],
      "如 OpenAI o1 / o3 等新一代「推理模型（Reasoning Models）」，其核心突破在於將模型算力重點轉移至哪一階段？",
      ["Test-Time Compute（測試/推論階段的思維推導時間）", "預訓練階段的爬蟲時間", "資料清洗階段", "模型打包階段"], 0,
      "o1 等模型引入強化學習訓練其產生隱藏式長鏈條「思維推導（Chain of Thought）」，打破傳統單純靠擴大預訓練規模的瓶頸。")

    q(63, False, ["模型特性", "Non-deterministic"],
      "即使將 Temperature 設為 0，大語言模型在雲端 API 呼叫下有時仍會產出微幅不同的文字，最主要的底層工程原因為何？",
      ["GPU 平行浮點數加法運算的非結合律與非確定性排程", "伺服器被駭客入侵", "演算法程式碼隨機遺失", "網路封包重傳"], 0,
      "在現代 GPU 巨量平行計算環境下，浮點數加法不具備嚴格結合律 ((a+b)+c != a+(b+c))，不同線程競爭排程順序的微小浮點差異會被逐層放大。")

    q(64, False, ["模型安全", "Model Poisoning"],
      "攻擊者在開源預訓練或微調數據集中惡意混入精心構造的特徵樣本，使模型學會特定暗號觸發後門的威脅稱為？",
      ["資料投毒（Data/Model Poisoning）", "分散式阻斷服務", "中间人攻擊", "ARP 欺騙"], 0,
      "Data Poisoning 攻擊成本低且極難察覺，一旦受毒化模型在特定 Prompt 觸發詞出現時，便會繞過安全防護輸出惡意代碼或虛假資訊。")

    q(65, False, ["評估基準", "Chatbot Arena"],
      "由 LMSYS 組織推動，讓全球真實使用者以盲測方式向兩個匿名模型提問並進行喜好投票，計算 ELO 天梯積分的主流評測平台為？",
      ["LMSYS Chatbot Arena", "Kaggle", "LeetCode", "HuggingFace Hub"], 0,
      "Chatbot Arena 採用群眾外包雙盲 A/B 評測與國際西洋棋 ELO 計分機制，被業界公認為最難被刷榜作弊、最貼近人類真實喜好的大模型排行榜。")

    q(66, False, ["向量距離", "Cosine Similarity"],
      "在向量資料庫檢索中，衡量兩個文本嵌入向量夾角大小、不受向量絕對長度影響的幾何度量標準為何？",
      ["餘弦相似度（Cosine Similarity）", "歐氏距離（Euclidean Distance）", "曼哈頓距離（Manhattan Distance）", "漢明距離（Hamming Distance）"], 0,
      "餘弦相似度計算兩向量點積除以模長乘積，數值介於 -1 到 1 之間，專注於語意方向的一致性而非文本長度，是 RAG 中最常用的度量方式。")

    q(67, False, ["架構進化", "Mixture of Depths"],
      "動態依據當前輸入 Token 的複雜難度，自主決定該 Token 是否跳過某些計算層以大幅節省計算資源的架構技術為？",
      ["Mixture of Depths（MoD）", "MoE", "RNN", "Autoencoder"], 0,
      "MoD 讓簡單的標點符號或常用詞走快速捷徑，而將重度算力集中於邏輯密集的關鍵 Token，實現動態自適應計算資源分配。")

    q(68, False, ["模型微調", "Instruction Tuning"],
      "收集大量「指示-輸入-輸出」形式的多樣化人類任務資料集對預訓練模型進行微調的過程稱為？",
      ["指令微調（Instruction Tuning）", "對比預訓練", "無監督分群", "正則化訓練"], 0,
      "指令微調（如 FLAN 技術）使模型不再只是預測接龍，而是深刻理解「總結」、「翻譯」、「分類」等元任務動詞的行為語意。")

    q(69, False, ["多模態對齊", "Cross-Attention"],
      "在文字生圖或多模態模型中，讓視覺特徵圖與文字提示詞向量進行跨模態語意融合的注意力運算稱為？",
      ["交叉注意力（Cross-Attention）", "自注意力（Self-Attention）", "前饋傳播", "最大值池化"], 0,
      "Cross-Attention 中，Query 來自視覺特徵，而 Key 與 Value 來自文字 Prompt 編碼，使圖像生成過程的每個像素區塊能即時依賴文字語義引導。")

    q(70, False, ["硬體架構", "SRAM vs HBM"],
      "現代 AI 加速卡（如 NVIDIA H100）中，速度最快、延遲最低但容量極為有限（通常數十至數百 MB）的晶片內存為？",
      ["SRAM（靜態隨機存取記憶體 / 片上快取）", "HBM（高頻寬記憶體 / 顯存）", "DDR5", "NVMe SSD"], 0,
      "SRAM 位於 GPU 晶片核心內部，頻寬遠超板載顯存 HBM，FlashAttention 等演算法的核心就是盡可能在 SRAM 中完成全部矩陣運算。")

    q(71, False, ["語言模型特性", "Markov Property"],
      "自回歸語言模型計算序列聯合機率時，依賴鏈式法則將整個句子的機率分解為每個詞在前方所有上下文給定下的條件機率連乘，此性質源自？",
      ["機率鏈式法則（Chain Rule of Probability）", "中央極限定理", "大數法則", "貝氏定理"], 0,
      "P(w1, w2, ..., wn) = ∏ P(wi | w1, ..., wi-1)，這構成了因果自回歸語言模型生成的核心數學底層架構。")

    q(72, False, ["分詞問題", "Token Boundary"],
      "為什麼現代 LLM 在處理數字符號或顛倒文字（如「將單字反轉拼寫」）時經常出錯？",
      ["因為分詞器常將數字串切分成不規則的子詞 Token，模型無法直接看到單個字符", "因為模型算力不足", "因為螢幕解析度影響", "因為模型不具備文字概念"], 0,
      "BPE 分詞器會把「12345」切成「12」和「345」之類的獨立 Token，模型在嵌入層看到的是抽象 ID 而非個別字元結構，因此拼字與字元計數能力脆弱。")

    q(73, False, ["開源社群", "Hugging Face"],
      "現今全球人工智慧開發者最主要共享預訓練模型權重、資料集與 Demo 應用的開源平台為？",
      ["Hugging Face Hub", "GitHub Pages", "SourceForge", "Bitbucket"], 0,
      "Hugging Face 提供了 Transformers 開源函式庫與 Model Hub，已成為全球 AI 社群事實上的開源模型分發與協作中心。")

    q(74, False, ["模型微調", "Prefix Tuning"],
      "在 Transformer 每一層的 Key 與 Value 向量前方拼接一組可學習的連續虛擬向量（Virtual Tokens）以達到微調目的的參數高效率技術為？",
      ["Prefix Tuning", "LoRA", "Prompt Engineering", "Full Tuning"], 0,
      "Prefix Tuning 透過凍結模型全部主體權重，僅優化序列前置的前綴虛擬嵌入向量，即可針對不同下游任務客製化適應。")

    q(75, False, ["推論優化", "Dynamic Batching"],
      "在生產環境 API 伺服器中，動態將多個不同使用者在時間視窗內抵達的併發請求合併成單一批次進行 GPU 計算的技術稱為？",
      ["動態批次處理（Dynamic Batching / Continuous Batching）", "單線程排隊", "非同步序列化", "硬體超頻"], 0,
      "Continuous Batching 在 Token 級別動態插入新請求與移出已結束請求，大幅提升 GPU 運算單元利用率，降低平均響應延遲。")

    q(76, False, ["模型概念", "Knowledge Cutoff"],
      "大語言模型對於在其訓練完成發布之後所發生的世界即時新聞或新事件完全不知情，這種現象稱為？",
      ["知識截止日期（Knowledge Cutoff）", "概念漂移", "網路中斷", "冷啟動"], 0,
      "模型知識完全固化於其神經網絡權重中。要讓模型獲取知識截止日之後的最新資訊，必須結合網路搜尋或 RAG 外部知識庫檢索。")

    q(77, False, ["多模態技術", "OCR-free"],
      "新一代端到端多模態模型（如 Donut）直接輸入文檔圖像並輸出結構化答案，不依賴傳統文字光學辨識模組，此設計稱為？",
      ["OCR-free 端到端架構", "純文字管線", "模板比對", "點陣圖掃描"], 0,
      "OCR-free 模型直接將圖像視覺編碼與語言解碼器結合，避免了傳統 OCR 在版面混亂、手寫或表格識別時產生的串聯誤差。")

    q(78, False, ["模型安全", "Jailbreak Filter"],
      "各大商業 LLM 服務商在模型輸入端與輸出端所架設、用以攔截色情暴力或武器製造指令的保護層稱為？",
      ["安全護欄（Safety Guardrails / Moderation API）", "防火牆反代", "負載均衡器", "資料庫網關"], 0,
      "安全護欄包含輸入敏感詞比對、分類模型過濾與輸出文本審核，是保障 AI 服務符合法律法規的第一道防線。")

    q(79, False, ["訓練技術", "Curriculum Learning"],
      "在訓練神經網絡時，仿照人類學習由淺入深、先給予簡單短句子再逐步過渡到複雜長邏輯文本的訓練策略為？",
      ["課程學習（Curriculum Learning）", "隨機打亂訓練", "對抗訓練", "主動學習"], 0,
      "課程學習能加速神經網絡的收斂速度，引導優化器跳出早期局部最優解，提升模型泛化性能。")

    q(80, False, ["評估指標", "Pass@k"],
      "在代碼生成評估中，為每個問題生成 k 個獨立候選代碼樣本，只要其中至少有 1 個樣本能通過所有單元測試即視為解決的指標為？",
      ["pass@k（如 pass@1, pass@10）", "F1-Score", "ROUGE-L", "BLEU-4"], 0,
      "pass@k 是衡量代碼生成模型能力的黃金指標，通常計算 pass@1（單次直接命中率）與 pass@10（給予 10 次嘗試機率）。")

    q(81, False, ["資料處理", "Deduplication"],
      "在構建千億 Token 預訓練語料庫時，利用 MinHash 或 SimHash 演算法徹底刪除網路爬蟲重複網頁內容的清洗步驟稱為？",
      ["文本去重（Deduplication）", "分詞處理", "字元編碼轉換", "隨機截斷"], 0,
      "數據去重對預訓練極為關鍵，能防止模型死記硬背重複段落、減少訓練計算浪費並有效降低訓練後期的過擬合。")

    q(82, False, ["訓練細節", "Weight Decay"],
      "在訓練神經網絡的損失函數中增加 L2 權重範數懲罰項，防止權重數值過大並抑制過擬合的正則化技巧為？",
      ["權重衰減（Weight Decay / L2 正則化）", "學習率熱身", "Dropout", "梯度截斷"], 0,
      "AdamW 優化器正確解耦了權重衰減與梯度更新，是現代 Transformer 訓練事實上的標準優化演算法。")

    q(83, False, ["訓練細節", "Warmup"],
      "在模型訓練初期，讓學習率從極小數值逐步線性爬升到預設峰值，以避免模型早期隨機權重劇烈震盪的策略稱為？",
      ["學習率熱身（Learning Rate Warmup）", "退火演算法", "梯度累積", "早停法"], 0,
      "Warmup 能保護模型在初始階段不被巨大梯度破壞已初始化的注意力權重，隨後再進入餘弦退火（Cosine Decay）平穩下降。")

    q(84, False, ["模型架構", "Feedforward Network"],
      "Transformer 區塊中，位於 Multi-Head Attention 層之後、負責進行非線性特徵投射與大量知識儲存的子層為何？",
      ["前饋全連接網絡（FFN / MLP）", "卷積池化層", "長短期記憶層", "自編碼器"], 0,
      "研究表明 Transformer 的 FFN 層（通常擴展 4 倍維度）如同鍵值記憶庫（Key-Value Memory），儲存了預訓練過程中習得的絕大部分事實常識。")

    q(85, False, ["模型架構", "SwiGLU"],
      "現代高效能大模型（如 Llama、Mistral）普遍取代傳統 ReLU/GELU 啟動函數、具備門控機制的激活層架構為何？",
      ["SwiGLU（Swish Gated Linear Unit）", "Sigmoid", "Tanh", "LeakyReLU"], 0,
      "SwiGLU 結合了門控線性單元與 Swish 啟動函數，雖然增加了部分矩陣乘法，但實證表明能顯著提升 Transformer 的語言建模能力。")

    q(86, False, ["向量索引", "HNSW"],
      "向量資料庫中廣泛採用的高維向量圖索引演算法，具備跳表（Skip-list）多層結構、檢索速度達到毫秒級的演算法為何？",
      ["HNSW（Hierarchical Navigable Small World）", "KD-Tree", "線性掃描", "B+ Tree"], 0,
      "HNSW 建構多層導航圖，在上層進行大跨度粗篩，在下層進行局部密集細尋，在高維向量近似最近鄰（ANN）搜尋中兼具極高召回率與極低延遲。")

    q(87, False, ["模型微調", "PEFT"],
      "參數量化、LoRA、Adapter 等「僅微調極少量額外參數即能完成特定任務適配」的技術統稱為？",
      ["PEFT（Parameter-Efficient Fine-Tuning，參數高效率微調）", "Full Retraining", "Zero-shot Tuning", "Hard Prompting"], 0,
      "PEFT 系列技術打破了大模型微調必須全量備份數十 GB 權重的瓶頸，大幅降低企業客製化大模型的儲存與算力門檻。")

    q(88, False, ["推論指標", "TPS"],
      "在 LLM 推論服務中，用來量化模型每秒鐘能夠持續生成多少個文字單位的吞吐量指標為？",
      ["TPS（Tokens Per Second）", "FPS（Frames Per Second）", "BPS（Bits Per Second）", "RPM（Requests Per Minute）"], 0,
      "TPS 是衡量生成速度流暢度的關鍵指標。一般人類閱讀速度約為每秒 5~10 個詞，TPS 超過 30~50 即能提供極為流暢的即時打字機體驗。")

    q(89, False, ["模型生態", "Llama"],
      "由 Meta 公司開源發布、帶動全球開源大語言模型生態爆發性發展的里程碑模型家族為何？",
      ["Llama 系列（Llama 1 / 2 / 3）", "BERT", "Word2Vec", "GPT-2"], 0,
      "Meta 於 2023 年開放 Llama 系列模型權重供學術與商用，引發全球開源社群蓬勃發展，催生了大量高效輕量衍生模型。")

    q(90, False, ["對齊技術", "KTO"],
      "只需提供使用者對單個回答「滿意（Thumb Up）」或「不滿意（Thumb Down）」的非成對二元回饋資料即可進行對齊的演算法為？",
      ["KTO（Kahneman-Tversky Optimization）", "RLHF", "DPO", "PPO"], 0,
      "KTO 基於行為經濟學的前景理論，打破了 DPO 必須提供一好一壞嚴格成對數據的限制，能直接利用真實世界的點讚點踩數據微調模型。")

    q(91, False, ["架構進化", "Recurrent Depth"],
      "在維持固定參數量的情況下，將同一個 Transformer 層重複循環執行多次以換取更深邏輯推導能力的設計思想稱為？",
      ["深度遞歸（Recurrent Depth / Universal Transformer）", "量化蒸餾", "多頭注意力", "位置插值"], 0,
      "透過在層與層之間共享權重並迭代執行，模型能在不增加模型權重體積的情況下增強多步算法推理能力。")

    q(92, False, ["向量距離", "Dot Product"],
      "在兩個向量已經預先完成「L2 單位長度歸一化（Normalize）」的前提下，兩向量的點積運算（Dot Product）等價於何種距離指標？",
      ["餘弦相似度（Cosine Similarity）", "歐式幾何距離", "曼哈頓距離", "切比雪夫距離"], 0,
      "當向量模長均為 1 時，點積公式直接等於 cos(θ)。因此在實務中常先將向量歸一化，直接以極高硬體效率的矩陣乘法進行餘弦相似度搜尋。")

    q(93, False, ["多模態音訊", "Whisper"],
      "OpenAI 開源發布、在 68 萬小時多語種語音數據上訓練的高魯棒性語音識別（ASR）與翻譯神經網絡為何？",
      ["Whisper", "Sora", "DALL-E", "Codex"], 0,
      "Whisper 採用標準 Encoder-Decoder Transformer，能有效克服各國口音、背景背景噪音及專業術語，廣泛應用於會議即時記錄。")

    q(94, False, ["生成模型", "Sora"],
      "OpenAI 於 2024 年初展示、能理解複雜物理規律並生成長達 60 秒高畫質連貫影片的擴散變換器架構為？",
      ["Sora（Diffusion Transformer / DiT）", "GAN", "VAE", "ResNet"], 0,
      "Sora 將影片在時空維度切割為「時空 Patch（Spacetime Patches）」並利用 Transformer 作為骨幹網絡取代傳統 UNet，開創了影片生成新典範。")

    q(95, False, ["模型安全", "Canary Tokens"],
      "在企業機密數據集或訓練文本中刻意植入特殊的唯一標識字串，用來偵測模型是否將機密訓練集直接記憶背誦洩漏的技術稱為？",
      ["金絲雀標記（Canary Tokens）", "蜜罐（Honeypot）", "混淆碼", "數字簽名"], 0,
      "Canary Token 源自礦井中的金絲雀隱喻。一旦在模型對外推論輸出中偵測到該專屬字串，即可確定模型存在訓練數據外洩漏洞。")

    q(96, False, ["模型特性", "Sycophancy"],
      "經過 RLHF 對齊後的模型有時會過度迎合使用者，即使使用者的初始前提完全錯誤也阿諛奉承附和，這種現象稱為？",
      ["奉承偏誤（Sycophancy / 迎合偏見）", "幻覺", "過擬合", "自洽性"], 0,
      "Sycophancy 是對齊過程中的副作用：人類標註員往往傾向給予「附和自己觀點」的回答更高評分，導致模型學會不糾正用戶錯誤。")

    q(97, False, ["向量檢索", "Hybrid Search"],
      "結合「基於關鍵字的稀疏檢索（如 BM25）」與「基於向量的密集語意檢索（Dense Retrieval）」以兼顧精準專有名詞與概念匹配的架構稱為？",
      ["混合搜尋（Hybrid Search）", "二分搜尋", "全文索引", "倒排索引"], 0,
      "混合搜尋利用倒排索引精確匹配特定型號、專有名詞，同時以向量檢索捕捉同義詞與寬泛語意，再透過倒數排名融合（RRF）獲得最佳召回。")

    q(98, False, ["模型微調", "Catastrophic Forgetting Mitigation"],
      "在特定領域進行監督微調時，將原本預訓練階段 5%~10% 的通用語言數據混入訓練集一同微調的工程手法稱為？",
      ["數據回放（Data Replay / Experience Replay）", "梯度裁剪", "模型降維", "正則化衰減"], 0,
      "Data Replay 能持續刺激原本與通用邏輯相關的神經元權重，有效防止模型在適應垂直領域時發生災難性遺忘。")

    q(99, False, ["計算理論", "Chinchilla Scaling Laws"],
      "DeepMind 在 2022 年發表論文修正了早期 OpenAI 的 Scaling Law，指出過去大模型普遍存在「參數量過大而訓練 Token 量嚴重不足」的定律稱為？",
      ["Chinchilla 最佳化計算定律（Chinchilla Scaling Laws）", "摩爾定律", "阿姆達爾定律", "帕累托法則"], 0,
      "Chinchilla 定律證明在給定總算力預算下，參數量與訓練數據 Token 量應維持 1:20 左右的等比擴展，指導了後續 Llama 等「小參數吃巨量數據」模型的成功。")

    q(100, False, ["硬體與模型", "FP8 Training"],
      "新一代 AI 晶片（如 NVIDIA Hopper H100）引入並被現代前沿大模型廣泛採用的 8-bit 浮點數訓練數值格式為何？",
      ["FP8（8-bit Floating Point）", "FP64", "INT2", "Binary"], 0,
      "FP8（分為 E4M3 與 E5M2 兩種格式）將矩陣乘法顯存佔用減半並大幅提升張量核心運算吞吐量，使千億大模型訓練成本減半。")

    return questions

if __name__ == "__main__":
    qs = get_module1_questions()
    print(f"Module 1 generated successfully: {len(qs)} questions.")
