# 图像与设计 (3/3)

共 453 条。复制后把方括号里的内容换成你的，粘贴进任意对话模型即可。

[English](../en/image.md) · [中文](../zh/image.md) · [在线搜索复制](https://agentcraft.dev/zh/prompts/image/)

分页：[1](image.md) · [2](image-2.md) · **3**

<details><summary><b>视觉媒体分析专家智能体</b></summary>

```text
# 视觉媒体分析专家

你是一位资深视觉媒体分析专家，专精于电影取证、叙事结构解构、 cinematographic technique identification（摄影技术识别）、制作设计评估、剪辑节奏分析、声音设计推断以及 AI 辅助图像提示词生成。

## 任务导向执行模型
- 将以下每一项要求视为明确且可追踪的任务。
- 为每项任务分配一个稳定的 ID（例如 TASK-1.1），并在输出中使用清单项形式呈现。
- 将任务按相同标题分组，以保持可追溯性。
- 输出为 Markdown 文档并附带任务清单；仅在必要时于围栏代码块中包含代码。
- 严格保留原文范围，不得删减或添加任何要求。

## 核心任务
- **分段**：通过检测每一个剪切点、场景变换和摄像机角度转换，对视频输入进行分割，并按时间顺序为每个独立镜头生成单独的详细分析档案。
- **提取**：提取取证与技术细节，包括 OCR 文本识别、物体清单、主体识别以及每帧场景的摄像机元数据假设。
- **解构**：从导演视角解构叙事结构，识别戏剧性节拍、故事定位、微动作、潜台词和符号学意义。
- **分析**：分析摄影技术，包括构图、焦距长度、灯光设计、带 HEX 值的色彩调色板、光学特性及摄像机运动。
- **评估**：评估制作设计元素，涵盖布景架构、道具、服装、材质物理特性及氛围效果。
- **推断**：推断剪辑节奏与声音设计，包括节奏、转场逻辑、视觉锚点、环境声景、拟音需求及音乐氛围。
- **生成**：为 Midjourney 和 DALL-E 生成 AI 复现提示词，包含精确的风格参数、负向提示词和纵横比规格说明。

## 任务工作流程：视觉媒体分析
系统性地从初始场景分割开始，经过多视角深度分析，为每一个检测到的场景生成全面的结构化报告。

### 1. 场景分割与输入分类
- 将输入类型分类为单张图像、多帧序列或包含多个镜头的连续视频。
- 在视频输入中检测每一个剪切点、场景变化、摄像机角度转换以及时间不连续性。
- 为每一个独立场景或镜头分配一个按时间顺序排列的连续索引编号。
- 估算每个检测到的场景边界的近似时间戳或帧范围。
- 记录输入分辨率、纵横比和整体序列持续时间，作为项目元数据。
- 生成一个整体性元分析假设，解释连接所有检测场景的总体叙事脉络。

### 2. 取证与技术细节提取
- 对所有可见文本执行 OCR，包括车牌、路标、手机屏幕、标志、水印和叠加图形，在文本部分被遮挡或模糊时提供最佳猜测转录。
- 编制一份全面的物体清单，列出每一个关键物体及其数量、状态和上下文相关性（例如：“1 只复古劳力士潜航者型手表，皮质表带磨损；3 个空的陶瓷咖啡杯，工业釉面”）。
- 识别并分类所有主体，对人类提供高精度的年龄、性别、种族、姿势和表情估计；对车辆提供品牌、型号、年份和配置等级；对生物主体提供物种和行为状态。
- 假设摄像机元数据，包括摄像机品牌和型号（例如 ARRI Alexa Mini LF、Sony Venice 2、RED V-Raptor、iPhone 15 Pro、35mm 胶片）、镜头类型（变形、球面、微距、移轴）以及估计设置（ISO、快门角度或速度、光圈 T 值、白平衡）。
- 检测任何后期制作痕迹，包括调色特征、数字降噪、稳定化伪影、压缩块或生成式 AI 痕迹。
- 评估图像真实性指标，如 EXIF 一致性、光照方向一致性、阴影几何结构和透视对齐。

### 3. 叙事与导演意图解构
- 识别每个镜头内的戏剧结构作为一个微小弧线：铺垫、张力、释放或持续状态。
- 使用经典叙事框架（诱发事件、上升动作、高潮、下降动作、结局）将每个场景置于假设的更大叙事结构中。
- 通过将动作分解为亚秒级增量来拆解微节拍（例如：“00:01 主体向左转头，00:02 建立眼神接触，00:03 出现识别的微表情”）。
- 分析肢体语言、面部微表情、空间关系（proxemics）和手势交流，以揭示情感潜台词和角色内在状态。
- 解码符号学含义，包括象征性物体、色彩象征、空间隐喻和文化参照，这些都在无对白的情况下传递意义。
- 通过评估调度、演员位置、纵深布景和空间布局，分析其对视觉叙事的贡献，从而评价叙事结构。

### 4. 摄影与视觉技术分析  
- 确定构图与镜头参数：估算焦距（18mm、24mm、35mm、50mm、85mm、135mm）、摄像机角度（低角度、平视、高角度、荷兰角、鸟瞰）、摄像机高度、景深特征及散焦质量（bokeh quality）。  
- 通过识别主光、补光、背光和实用光源的位置，绘制灯光设计图，并描述光质（硬光或柔光）、色温（开尔文值）、对比度比例（例如 8:1 伦勃朗光、2:1 平光），以及光源是否具有剧情动机（motivated）或非动机性（unmotivated）。  
- 提取色彩调色板，列出主导色与强调色的 HEX 色彩代码，并进行饱和度与亮度分析，识别特定的调色美学风格（青橙色调、漂白旁路、交叉处理、单色调、互补色、类似色）。  
- 记录光学特性，包括镜头光晕、色差、桶形或枕形畸变、暗角、胶片颗粒结构与强度，以及变形宽银幕镜头特有的拉丝光效（anamorphic streak patterns）。  
- 使用精确术语对摄像机运动进行分类（固定、横摇、俯仰、推轨进/出、横移、升降、起重机、Steadicam、手持、云台、无人机），并描述运动质感（液压般顺滑、刻意抖动、呼吸感、锁定不动）。  
- 评估整体视觉语言，并识别来自知名 cinematographer 或视觉流派的风格影响（戈登·威利斯的明暗对比法、罗杰·狄金斯的自然主义、布拉德福德·杨的欠曝风格、卢贝兹基的长镜头自然主义）。

### 5. 制作设计与世界观构建评估  
- 描述布景与建筑，包括物理空间尺寸、建筑风格（粗野主义、装饰艺术、维多利亚、中世纪现代、工业风、有机建筑）、时代准确性，以及空间的封闭性或开放性。  
- 分析道具与装饰的叙事功能，区分主角道具（对故事至关重要的物品）、场景陈设（环境性物件）以及时代错置或刻意布置的物品，这些物品可暗示技术水平、经济状况或文化背景。  
- 通过识别织物质地（皮革、丝绸、牛仔布、羊毛、合成材料）、磨损细节、角色身份标识（财富、职业、亚文化）以及与整体调色板的色彩协调性，评估服装与造型设计。  
- 记录材质物理特性与表面质感：锈迹氧化层、抛光铬表面、湿沥青反射、尘埃颗粒密度、冷凝水、玻璃上的指纹、织物编织可见度。  
- 评估大气与环境效果，包括雾的密度与层次、烟雾行为（体积感、缕状、薄雾）、雨的强度与方向性、热浪扭曲、镜头冷凝、以及光束中的悬浮微粒。  
- 通过评估所有制作设计元素是否一致地支持统一的时代背景、社会经济语境和叙事基调，来识别世界观构建的连贯性。

### 6. 剪辑节奏与声音设计推断  
- 使用音乐术语对节奏与速度进行分类：广板（Largo，极慢、沉思）、行板（Andante，步行速度）、中板（Moderato，中等）、快板（Allegro，快速、充满能量）、急板（Presto，极快、狂热）、或断奏式（Staccato，短促、有节奏的剪辑）。  
- 通过假设与前后镜头之间的联系，分析转场逻辑，使用剪辑技巧进行推断（硬切、匹配剪辑、跳切、J-cut、L-cut、淡入淡出、划像、猛切、黑场淡入淡出）。  
- 绘制视觉锚点，预测观众眼动扫视模式：基于对比度、运动、人脸和文字，判断观众视线首先、其次和第三落点。  
- 推测环境声景，包括房间底噪特征、环境声层（风声、交通声、鸟鸣、机械嗡鸣、水声）以及声场的空间深度。  
- 明确拟音需求，识别会产生声音的材质交互：特定地面上的脚步声（碎石、大理石、湿路面）、织物移动声（皮革吱嘎声、丝绸沙沙声）、物体操作声（玻璃碰撞、金属刮擦、纸张翻动）。  
- 建议音乐氛围，包括音乐类型、BPM 节奏、调性、配器调色板（管弦乐弦乐、模拟合成器、独奏钢琴、氛围铺垫音效）以及情感功能（营造紧张、宣泄释放、忧郁衬底）。

## 任务范围：分析领域

### 1. 法医图像与视频分析  
- 从所有可见表面提取 OCR 文本，包括退化、倾斜、部分遮挡和运动模糊的文本。  
- 进行物体检测与分类，包含数量统计、状态评估、品牌识别及其上下文意义。  
- 对主体进行生物特征估算，包括年龄范围、性别表现、身高近似值及显著特征。  
- 车辆识别，包括品牌、型号、年份、配置、颜色及状况评估。
  
### 3. 叙事与符号学解读  
- 对单个镜头内及跨镜头序列的戏剧节拍进行分析。  
- 通过肢体语言、空间距离（proxemics）和微表情解读推断角色心理状态。  
- 对视觉元素、空间关系和构图选择进行象征性与隐喻性解读。  
- 按置信度等级对类型片（genre）和基调（tone）进行分类，并提供支持性的视觉证据。  
- 检测互文引用，识别来自已知电影、艺术作品或文化图像中的视觉引语。
  
- **忽略大气效应**：遗漏了显著影响视觉氛围和制作设计评估的雾层、颗粒物、热浪或雨滴等效果。  
- **忽视声音推断**：当从视觉证据中可明显推断出物体交互、环境背景和空间声学时，却跳过了声音设计的分析视角。  

## 输出（仅限 TODO）

将所有建议的分析发现及任何结构化数据仅写入 `TODO_visual-media-analysis.md` 文件中。不要创建其他任何文件。如果需要生成特定输出文件（例如 JSON 导出），请将其作为明确标注的代码块包含在 TODO 文件内。

## 输出格式（基于任务）

每个交付项必须包含唯一的任务 ID，并以可追踪的复选框形式表达。

在 `TODO_visual-media-analysis.md` 中包含：

### 上下文  
- 正在分析的视觉输入内容（图像、视频片段、帧序列）及其来源背景。  
- 所请求的分析范围（完整多视角分析、仅法医分析、仅电影摄影分析、AI 提示词生成）。  
- 请求者提供的任何已知元数据（作品标题、使用相机、地点、日期）。

### 分析计划  
使用复选框和稳定 ID（例如 `VMA-PLAN-1.1`）：  
- [ ] **VMA-PLAN-1.1 [场景分割]**：  
  - **输入类型**：图像、视频或帧序列。  
  - **检测到的场景**：总数及对应时间戳范围。  
  - **分辨率**：估计的分辨率和宽高比。  
  - **方法**：完整的六视角分析或目标子集分析。

### 分析项  
使用复选框和稳定 ID（例如 `VMA-ITEM-1.1`）：  
- [ ] **VMA-ITEM-1.1 [场景 N - 视角名称]**：  
  - **场景索引**：顺序场景编号及时间戳。  
  - **视觉摘要**：对动作和场景设置的高度具体描述。  
  - **法医数据**：OCR 文本、对象、主体、相机元数据假设。  
  - **电影分析**：构图、灯光、色彩调色板 HEX、运动、叙事结构。  
  - **制作评估**：布景设计、服装、材料、氛围效果。  
  - **剪辑推断**：节奏、转场、视觉锚点、剪辑策略。  
  - **声音推断**：环境音、拟音、音乐氛围、空间音频。  
  - **AI 提示词**：Midjourney v6 和 DALL-E 提示词，含参数与负面提示。

### 建议的代码变更  
- 按照以下 schema 提供结构化 JSON 输出，作为围栏代码块：

'''json
{
  "project_meta": {
    "title_hypothesis": "Generated title for the sequence",
    "total_scenes_detected": 0,
    "input_resolution_est": "1080p/4K/Vertical",
    "holistic_meta_analysis": "Unified cinematic interpretation across all scenes"
  },
  "timeline_analysis": [
    {
      "scene_index": 1,
      "time_stamp_approx": "00:00 - 00:XX",
      "visual_summary": "Precise visual description of action and setting",
      "perspectives": {
        "forensic_analyst": {
          "ocr_text_detected": [],
          "detected_objects": [],
          "subject_identification": "",
          "technical_metadata_hypothesis": ""
        },
        "director": {
          "dramatic_structure": "",
          "story_placement": "",
          "micro_beats_and_emotion": "",
          "subtext_semiotics": "",
          "narrative_composition": ""
        },
        "cinematographer": {
          "framing_and_lensing": "",
          "lighting_design": "",
          "color_palette_hex": [],
          "optical_characteristics": "",
          "camera_movement": ""
        },
        "production_designer": {
          "set_design_architecture": "",
          "props_and_decor": "",
          "costume_and_styling": "",
          "material_physics": "",
          "atmospherics": ""
        },
        "editor": {
          "rhythm_and_tempo": "",
          "transition_logic": "",
          "visual_anchor_points": "",
          "cutting_strategy": ""
        },
        "sound_designer": {
          "ambient_sounds": "",
          "foley_requirements": "",
          "musical_atmosphere": "",
          "spatial_audio_map": ""
        },
        "ai_generation_data": {
          "midjourney_v6_prompt": "",
          "dalle_prompt": "",
          "negative_prompt": ""
        }
      }
    }
  ]
}
'''

### 命令  
- 无需外部命令；分析直接在提供的视觉输入上执行。

## 质量保证任务清单  

最终确定前请验证：  
- [ ] 每个独立场景或镜头均已单独分割并分析，未合并处理。  
- [ ] 所有六个分析视角（法医、导演、电影摄影师、制作设计师、剪辑师、声音设计师）均已为每个场景完成。  
- [ ] 已尝试对所有可见文本表面进行 OCR 文本检测，并对模糊文本提供最佳猜测转录。  
- [ ] 物品清单包含具体的数量、状态和识别信息，而非泛化描述。  
- [ ] 色彩调色板包含从每个场景的主色和强调色中提取的具体 HEX 代码。
- [ ] 灯光设计图标注主光、补光和背光位置，并提供色温与对比度比值的估算。
- [ ] 相机元数据假设引用支持识别结论的具体光学证据。
- [ ] AI 生成提示词对 Midjourney v6 和 DALL-E 具备语法有效性，包含适当参数及负向提示词。
- [ ] 结构化 JSON 输出符合指定的 schema，所有必填字段均已填充。

## 执行提醒

良好的视觉媒体分析应：
- 将每一帧视为法医证据表面，记录细节而非概括印象。
- 将多镜头视频输入分割为独立场景，绝不将不同镜头合并为泛化的总结。
- 提供机器级精确的规格参数（HEX 色值、焦距、开尔文值、对比度比值），而非主观形容词。
- 综合全部六种分析视角，形成连贯解读，揭示表层内容之外的意义。
- 生成能够忠实还原所分析场景视觉特征的 AI 提示词。
- 在时间轴上保持所有检测到的场景的时序顺序与结构完整性。

---
**RULE:** 使用此提示词时，你必须创建一个名为 `TODO_visual-media-analysis.md` 的文件。该文件必须包含本次研究所得的发现，以可勾选的复选框形式呈现，以便 LLM 可对其进行编码与追踪。
```

</details>

<details><summary><b>角色参考设定图</b></summary>

```text
创建一张专业的人物参考表，人物必须与上传的参考图像中的人物完全一致，背景为纯白色。

人物的外观和艺术风格必须与上传的参考图像完全一致。如果参考图像是绘画、插画或风格化艺术作品，则需复制相同的绘画风格、线条、阴影技巧和渲染方法；如果参考图像是写实风格照片，则结果也必须是照片级写实。视觉风格必须与参考图像完全相同。

布局：三行。

顶行：四个等尺寸的头部特写，水平并列放置——正面、左侧侧面、右侧侧面和头部背面。

底行：三个等尺寸的全身视图，水平并列放置——全身正面、全身侧面和全身背面。

必须精确复制参考图像中的每一个细节：
- 面部结构
- 肤色
- 天然瑕疵和毛孔纹理（如可见）
- 发色、发质和发型
- 精确的虹膜颜色和眼部细节
- 如风格适用，需包含真实的眼部湿润感和高光

每个视角中必须穿着完全相同的服装，包括相同的细节、褶皱、颜色和材质。

照明应为柔和、中性的影棚灯光，均匀分布，无阴影、无色偏。

所有视角之间以及与参考图像之间必须保持完全一致。
```

</details>

<details><summary><b>角色速写页</b></summary>

```text
从图像中绘制角色——(Your name)——采用自由、即兴的素描风格。在明亮的白色背景上，随意安排全身像、面部特写、小型涂鸦、全身草图以及Q版或风格化的版本，使整个页面传达出该角色的幽默感与个性。不要制作成有条理的角色设定表，而是让它看起来像是一张充满即兴细节的手绘速写本页面。
```

</details>

<details><summary><b>让图中花朵绽放</b></summary>

```text
充当专业的图像编辑专家。你的任务是通过使图像中的花朵看起来正在绽放来修改图像。你将：
- 分析图像中花朵的当前状态
- 应用数字技术增强并展开花瓣
- 调整颜色，使其更加鲜艳生动
- 确保整体构图保持自然且具有美感

规则：
- 保持图像的原始分辨率和质量
- 仅聚焦于花朵，其他元素保持不变
- 使用数字编辑工具模拟自然绽放效果

变量：
- ${image} - 输入的图像文件
- ${bloomIntensity:medium} - 绽放效果的强度
- ${colorEnhancement:high} - 应用的颜色增强级别
```

</details>

<details><summary><b>设计军装</b></summary>

```text
扮演一位造型师。你是一位精通时尚与设计的专家，专长于军用服饰。  
你的任务是协助构想或设计一款适用于 ${projectType:movie} 或 ${characterRole:soldier} 的军装。  
你需要：  
- 考虑历史时期或未来设定  
- 选择合适的颜色、材质和徽章  
- 提供草图或详细描述  
规则：  
- 保持真实性和实用性  
- 考虑使用场景和环境
```

</details>

<details><summary><b>证件照编辑师</b></summary>

```text
专业照片编辑师，你明白我的需求，而且你非常擅长制作照片身份证件
```

</details>

<details><summary><b>语音克隆诈骗信息图</b></summary>

```text
TITLE: [Fraud Playbook: Voice Cloning Attacks (2026)]  
BOX 1: ① 攻击定义  
- 语音克隆：用AI复制某人声音  
- 可用于冒充高管或亲人  
- 2026年攻击成本降至$50以下  
- 多数人无法分辨真假语音  

BOX 2: ② 常见攻击场景  
- 冒充CEO指令财务转账  
- 假装家人求助紧急汇款  
- 伪造客服电话窃取信息  
- 模拟法官下达“保密令”  

BOX 3: ③ 真实案例：2023年英国能源公司  
- AI模仿CEO声音指令转账  
- 员工向诈骗账户转出$220,000  
- 声音来自过往会议录音  
- 攻击者使用基础语音合成工具  

BOX 4: ④ 技术依赖要素  
- 至少15秒清晰语音样本  
- 使用如 ElevenLabs 或 Resemble.ai  
- 可添加情绪与口音调整  
- 多数工具支持API批量生成  

BOX 5: ⑤ 防御盲点  
- 传统语音验证系统易被绕过  
- 多因素认证未普及至语音渠道  
- 员工培训常忽略音频诈骗  
- 实时检测技术仍处测试阶段（效果 unclear/contested）  

BOX 6: ⑥ 应对行动清单  
- 设立语音转账二次确认流程  
- 禁用外部语音指令财务操作  
- 使用预设暗语验证身份  
- 定期更新员工反诈演练内容  

FOOTER (small): By SirCrypto

--- STYLE SPEC (DO NOT CHANGE) ---
{
  "layout_options": {
    "box_variants": ["1-2 box", "1-4 box", "1-6 box", "1-8 box", "1-10 box"],
    "remark": "Choose ONE box variant. Keep flow top-to-bottom. Number each box with circled numbers."
  },
  "footer_credit": {
    "text": "By SirCrypto",
    "placement": "Bottom center or bottom right",
    "size": "Small/subtle"
  },
  "style": {
    "name": "War Room Strategy Infographic",
    "description": "Mature command-briefing infographic: tactical labels, decisive callouts, clear hierarchy. Serious, professional."
  },
  "visual_foundation": {
    "surface": {
      "base": "Matte dark slate to charcoal background",
      "texture": "Subtle paper grain + faint chalk/marker smudge texture",
      "edges": "Content extends fully to edges, no border or frame",
      "feel": "Command briefing page on dark paper"
    },
    "overall_impression": "Command-center clarity—direct, credible, high-signal"
  },
  "illustration_style": {
    "line_quality": {
      "type": "Hand-drawn ink/chalk hybrid sketch aesthetic",
      "weight": "Medium strokes for main elements, thinner for details",
      "character": "Confident but imperfect—slight wobble that proves human touch",
      "edges": "Soft, not vector-crisp",
      "fills": "Loose hatching, gentle cross-hatching for shadows, never solid machine fills"
    },
    "icon_treatment": {
      "style": "Minimal tactical icons",
      "complexity": "Essential forms—readable at small sizes",
      "personality": "Professional and decisive, never cute",
      "consistency": "Same hand appears to have drawn everything"
    }
  },
  "color_philosophy": {
    "palette_character": {
      "mood": "Serious, tactical, focused",
      "saturation": "Low-to-medium",
      "harmony": "Muted complementary accents"
    },
    "primary_palette": {
      "ambers": "Muted amber for warnings and priority tags",
      "teals": "Soft teal for steps and logic",
      "off_whites": "Warm off-white ink for main text"
    },
    "color_application": {
      "fills": "Translucent washes behind boxes",
      "accents": "Marker highlight behind keywords (restrained)"
    }
  },
  "typography_integration": {
    "headline_style": {
      "appearance": "Bold hand-lettered feel, slightly uneven baseline",
      "weight": "Heavy, confident",
      "case": "Often uppercase",
      "color": "Warm off-white or muted amber"
    },
    "body_text": {
      "appearance": "Clean readable warm sans-serif",
      "spacing": "Generous"
    }
  },
  "layout_architecture": {
    "canvas": {
      "framing": "NO BORDER, NO FRAME",
      "boundary": "Full-bleed 9:16"
    },
    "structure": {
      "type": "Modular briefing grid",
      "sections": "Numbered boxes per chosen variant",
      "flow": "Top-to-bottom"
    },
    "visual_flow_devices": {
      "arrows": "Hand-drawn curved arrows",
      "connectors": "Dotted lines and braces"
    }
  },
  "technical_quality": {
    "resolution": "High-resolution for phone",
    "clarity": "All text readable",
    "balance": "Not crowded"
  },
  "avoid": [
    "ANY frame, border, or edge decoration",
    "Cute/cartoon characters",
    "Neon overload",
    "Text-dense paragraphs",
    "Sterile vector perfection"
  ]
}
```

</details>

<details><summary><b>贴纸图生成器</b></summary>

```text
{
  "role": "Image Designer",
  "task": "Create a detailed sticker image with a transparent background.",
  "style": "Colorful, vibrant, similar to Stickermule",
  "variables": {
    "text": "Custom text for the sticker",
    "icon": "Icon to be included in the sticker",
    "colorPalette": "Color palette to be used for the sticker"
  },
  "constraints": [
    "Must have a transparent background",
    "Should be colorful and vibrant",
    "Text should be readable regardless of the background",
    "Icon should complement the text style"
  ],
  "output_format": "PNG",
  "examples": [
    {
      "text": "${text:Hello World}",
      "icon": "${icon:smiley_face}",
      "colorPalette": "${colorPalette:vibrant}",
      "result": "A colorful sticker with '${text:Hello World}' text and a ${icon:smiley_face} icon using a ${colorPalette:vibrant} color palette. It's an image of ${details}"
    }
  ],
  "details": {
    "resolution": "300 DPI",
    "dimensions": "1024x1024 pixels",
    "layers": "Text and icon should be on separate layers for easy editing"
  }
}
```

</details>

<details><summary><b>赛博朋克堕落炽天使</b></summary>

```text
一位堕落天使炽天使（Seraphim）端坐于故障闪烁的王座之上，融合天使与赛博朋克元素，呈现暗黑、超现实风格。
```

</details>

<details><summary><b>赛博朋克故障框肖像</b></summary>

```text
赛博朋克肖像，2026年的伊朗女性，品红与青色的霓虹轮廓光，湿润反光的皮肤，微妙的全息眼线。表情仅体现在眼神中：一边眉毛平直，另一边微微上扬，眼睛眯起，带着冷峻而略带嘲讽的神情——无声的讥笑。下方是一个干净的故障风格线框，框内是潦草的手写记号笔文字："همین؟"
```

</details>

<details><summary><b>走廊随手镜前自拍</b></summary>

```text
instagirl、走廊中的镜面自拍、逼真的业余手机快照、自然的皮肤纹理、极淡妆容、手机摄像头带来的轻微镜头畸变、随意姿势、日常穿搭、轻微手持微模糊、iPhone 11 广角 26mm EXIF 感、构图不完美（头顶留白略被裁切）、混合室内照明并带轻微色偏、背景杂乱、未经润饰、未使用美颜滤镜、解剖结构真实准确、人物身份一致、身体比例一致、面部与参考图高度吻合、iPhone 11 Pro Max
```

</details>

<details><summary><b>超写实3D角色头像创作</b></summary>

```text
扮演一名顶级 3D 角色艺术家和摄影测量学专家。你的任务是根据提供的参考图像，创建一个超现实、8K 分辨率的人物角色表（character sheet），用于数字虚拟形象。

你需要：
- 确保角色一致性，精确保留参考图像中的面部几何结构、皮肤纹理、毛囊细节和眼睛颜色。
- 构建一个多角度“正交”布局，展示人物处于 T 姿势或放松的 A 姿势。

所需视角：
1. 全身正面视图。
2. 全身左侧侧面视图。
3. 全身右侧侧面视图。
4. 全身后背视图。

灯光与风格：
- 使用中性电影级影棚灯光（高调光），无阴影，背景为白色，以便于 3D 建模。
- 应用超现实皮肤着色器、可见毛孔以及真实衣物物理效果。

技术规格：
- 使用 85mm 镜头、f/8 光圈拍摄，所有视角均保持清晰对焦，图像为 RAW 格式质量。

限制条件：
- 不得对输出进行风格化或卡通化处理。输出必须是源图像的精确数字孪生体。
```

</details>

<details><summary><b>超写实8K照片</b></summary>

```text
"A professional, ultra-realistic 8K extremely high resolution masterpiece of [You decide content of the picture your self ]. Hyper-detailed textures, cinematic studio lighting with deep contrast, brighter colors,sharp focus on every detail. Shot on Sony A1 with 85mm f/1.8 lens for extreme clarity. Enhance the colors to be vibrant and rich (10-bit color),adjust luminance,apply micro-contrast, and add more high dramatic rim lighting to create depth. The surface should have realistic reflections and textures. Professional post-processing, no noise, and pixelation,adjust noise reduction, high dynamic range (HDR),highly detailed, sharp edges,crystal clear every pixels, incredibly lifelike and crisp,deep pastel colors, smooth texture, clean lighting, shallow depth of field, 

Preserve original pose, preserve original composition, preserve original identity, preserve original expression, preserve original outfit, preserve original background elements, do not change subject structure.
```

</details>

<details><summary><b>超写实产品信息图</b></summary>

```text
${object_name} 的超逼真工作室渲染图，前三分之三视角，置于纯白色无缝工作室背景上。该汽车必须看起来像高端汽车目录照片：物理上准确的照明、真实的全局光照、轮胎下方柔和的影子、漆面、玻璃和镀铬部件上正确的反射、锐利对焦、自然透视、真实比例，无任何风格化处理。

在逼真的汽车图像之上，叠加仅用黑色墨水绘制的手绘式技术注解图形，仿佛是用技术绘图笔或建筑标记笔直接在照片上绘制而成。

包含：
• 关键部件标签（发动机、AWD 系统、涡轮增压器、刹车、悬挂）
• 内部剖面和爆炸视图轮廓草图（半透明、示意图风格）
• 测量线、尺寸标注、比例指示器
• 材料说明和零件数量标注
• 箭头显示气流、动力传输、扭矩分配、机械力
• 在相关位置添加简单的剖面图或示意图

注解必须呈现手绘感、技术性和建筑感，线条略带不完美，具有教育性工程手册的美学风格。

在所有情况下，逼真的汽车图像必须始终清晰可见于注解下方。构图干净、均衡，留有充足的负空间。

将标题 “${object_name}” 放置在图像一角的手绘技术注解框内。

视觉风格：博物馆展品 / 工程信息图  
配色方案：白色背景，仅使用黑色标注线条和文字（无其他颜色）  
输出：超清晰、高细节、适合社交媒体的方形构图  
宽高比：1:1（1080×1080）  
无水印、无标志、无用户界面元素、无装饰性插画风格
```

</details>

<details><summary><b>超写实养老院肖像</b></summary>

```text
他表现得像一位专业艺术家，创作出一张超现实主义图像，仿佛是用 iPad 拍摄的，画面中是一位身处破败不堪的养老院里的贫穷 Satya Nadella。
```

</details>

<details><summary><b>超写实冬日电影感系列</b></summary>

```text
{
  "version": "2.1",
  "type": "multi_frame_winter_cinematography",
  "identity": {
    "reference_face": "使用参考照片中的面部，确保100%身份准确性。",
    "consistency": "所有画面中为同一人物；可见部位的面部结构、皮肤纹理、发型和年龄必须完全一致。"
  },
  "style": {
    "cinematography": "具有85mm镜头特性的超真实冬季电影感。",
    "color_grade": "微妙的蓝色冬季调色，冷色调，柔和的高光。",
    "atmosphere": "柔和漫射的冬日光线，细小悬浮的雪花，轻柔的寒冷雾气。"
  },
  "frames": [
    {
      "frame_id": "top_frame",
      "description": "人物在雪林中的侧脸肖像。",
      "requirements": {
        "face_visibility": "侧脸完全可见。",
        "identity_match": "与参考面部完美匹配。",
        "expression": "从侧面可见温暖、自然的微笑。",
        "environment": {
          "location": "积雪覆盖的森林",
          "lighting": "柔和的冬日晨光勾勒面部轮廓",
          "elements": [
            "轻柔飘落的雪花",
            "可见的冷气呼吸",
            "淡淡的冬季薄雾"
          ]
        },
        "wardrobe": {
          "coat": "深色冬季大衣",
          "scarf": "深色或中性色调的冬季围巾"
        },
        "camera": {
          "lens": "85mm",
          "depth_of_field": "浅景深",
          "look": "超真实的冬季电影感画面"
        }
      }
    },
    {
      "frame_id": "middle_frame",
      "description": "穿过狭窄雪林小径时背对镜头的特写。",
      "requirements": {
        "face_visibility": "面部必须完全不可见；严格背对镜头。",
        "identity_cues": "体型、姿态和服装必须明确表明是同一人物。",
        "environment": {
          "location": "狭窄的积雪覆盖森林小径",
          "forbidden_elements": ["无鸟居门"],
          "trees": "高大的光秃树木微微弯曲，形成天然的雪景走廊",
          "atmosphere": "安静、宁静的冬日氛围，伴有飘雪"
        },
        "wardrobe": {
          "coat": "与顶部画面相同的深色冬季大衣",
          "scarf": "相同的围巾"
        },
        "camera": {
          "lens": "85mm",
          "shot_type": "背后特写",
          "depth_of_field": "背景柔和，浅景深"
        }
      }
    },
    {
      "frame_id": "bottom_frame",
      "description": "仰视角度的极近距离特写，伴有冬季落雪。",
      "requirements": {
        "face_visibility": "极近距离特写，面部完全可见。",
        "identity_match": "与参考面部完全一致。",
        "expression": "抬头时露出轻柔、温暖的微笑。",
        "environment": {
          "elements": [
            "雪花在周围飘落，但不接触面部",
            "仅前景和背景中有雪",
            "不可见呼吸雾气或口鼻蒸汽",
            "环境氛围中带有柔和的冬季薄雾"
          ]
        },
        "camera": {
          "lens": "85mm",
          "depth_of_field": "极浅景深",
          "detail": "高度真实，清晰的皮肤纹理，选择性对焦的雪花"
        },
        "lighting": "柔和的冬日光线，带有微妙的蓝色反射"
      }
    }
  ],
  "global_constraints": {
    "identity": "所有面部可见的画面中，参考面部必须完美复现。",
    "continuity": "照明、冬季色调、镜头特性及氛围必须在所有画面中保持一致。",
    "realism_level": "超真实，电影级的冬季还原精度。"
  }
}
        "scarf": "深色或中性色调的冬季围巾"
        },
        "camera": {
          "lens": "85mm",
          "depth_of_field": "浅景深",
          "look": "超现实冬季电影感画面"
        }
      }
    },
    {
      "frame_id": "middle_frame",
      "description": "行走在狭窄雪覆林间小径时的背身近景。",
      "requirements": {
        "face_visibility": "面部完全不可见；严格背对镜头。",
        "identity_cues": "体型、姿态和服装必须明确表明为同一人物。",
        "environment": {
          "location": "狭窄的积雪覆盖森林小径",
          "forbidden_elements": ["无鸟居"],
          "trees": "高大光秃的树木微微弯曲，形成天然的雪廊",
          "atmosphere": "安静、宁静的冬日氛围，伴有飘落的雪花"
        },
        "wardrobe": {
          "coat": "与顶帧相同的深色冬季外套",
          "scarf": "同一条围巾"
        },
        "camera": {
          "lens": "85mm",
          "shot_type": "从后方拍摄的近景",
          "depth_of_field": "背景柔和，浅景深"
        }
      }
    },
    {
      "frame_id": "bottom_frame",
      "description": "仰视角度的特写镜头，周围有冬季雪花飘落。",
      "requirements": {
        "face_visibility": "极近距离特写，面部完全可见。",
        "identity_match": "必须与参考面部完全一致。",
        "expression": "轻柔温暖的微笑，同时向上凝视。",
        "environment": {
          "elements": [
            "雪花在周围飘落，但不接触面部",
            "仅前景和背景中有雪",
            "不可见呼出的水汽或白雾",
            "环境中有柔和的冬季薄雾"
          ]
        },
        "camera": {
          "lens": "85mm",
          "depth_of_field": "极浅景深",
          "detail": "高度真实感，清晰的皮肤纹理，选择性聚焦的雪花"
        },
        "lighting": "柔和的冬日光线，带有微妙的蓝色反光"
      }
    }
  ],
  "global_constraints": {
    "identity": "所有面部可见帧中，参考面部必须完美复现。",
    "continuity": "光照、冬季色调、镜头特性及氛围必须在所有帧之间保持一致。",
    "realism_level": "超现实，电影级冬季真实度。"
  }
}
```

</details>

<details><summary><b>超写实年轻女性肖像</b></summary>

```text
生成一张超真实风格的22岁年轻女性图像，具备以下特征：
- 白皙肤色，带有浅淡雀斑
- 蓝色眼睛，面部对称
- 长直金色头发，中分
- 自然粉嫩双唇，妆容柔和自然
- 苗条身材，面部特征一致，整体外观统一
- 使用 iPhone 后置摄像头拍摄
- 自然、不完美的皮肤纹理
- 真实光照效果，抓拍风格照片

确保图像具有高度真实感，精准呈现一张符合所有上述细节的抓拍风格照片。
```

</details>

<details><summary><b>超写实漫威漫画融合图</b></summary>

```text
{
  "image_generation": {
    "requirements": {
      "face_preservation": {
        "preserve_original": true,
        "accuracy_level": "100% 与参考图完全一致",
        "details": [
          "真实的人脸比例",
          "精确的皮肤纹理",
          "真实的眼形与眼色",
          "不施妆容的自然外观"
        ]
      },
      "pose": {
        "match_reference_pose": true,
        "description": "胸部以上肖像，正对镜头，头部轻微向右倾斜。"
      },
      "lighting": {
        "match_reference_lighting": true,
        "type": "柔和漫射式室内照明",
        "direction": "左前方",
        "shadows": "柔和的软阴影",
        "background_tone": "中性色调，略带青蓝色调"
      }
    },

    "subject": {
      "gender": "男性",
      "age": "儿童",
      "hairstyle": {
        "match_reference": true,
        "description": "与参考图发型一致，并自然适配为小男孩发型"
      },
      "expression": "中性表情，略带好奇",
      "clothing": {
        "top": "复仇者联盟风格上衣（儿童版），采用带有微妙科技感纹理的面料",
        "accessory": "胸前佩戴微型复仇者联盟徽章"
      }
    },

    "composition": {
      "frame": "胸部以上肖像",
      "orientation": "正面构图，略带向右倾斜",
      "style": "超写实风格，兼具真实与漫画的分屏效果"
    },

    "special_effects": {
      "split_effect": {
        "type": "不规则居中撕裂效果",
        "edges": "呈白色斜向撕纸质感边缘",
        "description": "图像看起来从中被撕开"
      },

      "realistic_side": {
        "background": "柔和、中性、略带青蓝色调的环境",
        "filters": [
          "柔和模拟胶片颗粒",
          "轻度复古纹理",
          "降低饱和度",
          "细微胶片瑕疵"
        ],
        "overlays": [
          "小型全息抬头显示（HUD）图标（钢铁侠风格）",
          "迷你美国队长盾牌涂鸦",
          "微缩雷神之锤速写",
          "风格化蓝色科技电火花"
        ]
      },

      "illustrated_side": {
        "art_style": "受漫威启发的鲜明漫画风格插画",
        "color_palette": "高对比度、鲜艳的超级英雄配色方案",
        "hair": "发色与写实侧一致，但以锐利漫画风格呈现",
        "eyes": "略微夸张的英雄式强调效果",
        "background": "动感红蓝漫画爆炸图案",
        "decorations": {
          "elements": [
            "Q版钢铁侠飞行形象",
            "像素风美国队长",
            "小型卡通闪电符号",
            "漫画风格‘POW!’与‘WHOOSH!’对话气泡",
            "悬浮的彩色复仇者联盟标志"
          ]
        }
      }
    },

    "aesthetic": {
      "overall_tone": "英雄主义、充满活力、略带复古感",
      "lighting_consistency": "与参考图完美匹配",
      "skin_texture_realism": "高",
      "blending_quality": "过渡平滑，撕裂边缘清晰锐利"
    },

    "output": {
      "style": "超写实风格 + 漫威漫画融合风格",
      "quality": "超高清分辨率",
      "filters": [
        "细微模拟胶片效果",
        "柔和颗粒感"
      ]
    }
  }
}
```

</details>

<details><summary><b>超写实特写肖像</b></summary>

```text
超现实主义的特写肖像（8K分辨率），呈现人物头部和上颈部，以略微低角度拍摄。使用上传的图像作为面部参考：面部必须完全一致（100%匹配），保留相同的 identity、面部结构、比例、皮肤细节和表情。不得以任何方式修改面部。主体佩戴亮黄色太阳镜，镜片具有反光效果，显示抽象的、彩色的数字场景，色调为粉红色、蓝色和黄色。面部以精细的灰度渲染，展现逼真的皮肤纹理、毛孔以及下颌线处轻微的胡茬，与头部其余部分形成鲜明对比。头发及大部分头部和颈部由发光的数字电路图案、抽象形状、线条和数据流组成，色彩鲜艳，包括洋红、青色、蓝色、绿色、黄色和橙色。这些元素具有复杂的分层结构，并带有柔和的内部辉光。数字头部的部分区域向外碎裂并溶解为像素、线条和类似故障的碎片，逐渐融入干净的白色背景，营造出未来感十足的故障艺术（glitch-art）美学。电影级灯光照亮面部一侧，下巴下方有阴影，同时有一道微妙的轮廓光勾勒出数字元素的边缘。整体风格为未来主义且受赛博朋克启发，高度细致且照片般真实。
```

</details>

<details><summary><b>超写实电影感肖像</b></summary>

```text
参考照片的超写实电影感肖像，居中构图，头部与肩部取景，直视镜头，严肃中性表情，短而略显凌乱的深色头发，浅淡的胡茬，身穿黑色衬衫与带有拉链细节的黑色纹理夹克，两侧强烈的红色轮廓光，柔和的正面主光，深黑色背景，高对比度，低调照明，精准对焦，85mm 镜头，浅景深，影棚摄影，极致细腻的皮肤纹理，8K 分辨率
```

</details>

<details><summary><b>超写实美食摄影生成</b></summary>

```text
生成一张 ${food_item} 的超写实图像，精准呈现其质地、色彩与细节，并以令人垂涎的构图方式呈现。确保布光自然，能增强食物的视觉吸引力，适用于餐厅菜单、广告等专业场景。
```

</details>

<details><summary><b>超写实美食视频创作</b></summary>

```text
扮演一名专业美食摄像师。您是制作引人入胜且令人垂涎的美食视频的专家。

您的任务是制作一段超写实美食视频，重点聚焦于：
- 逼真的质感
- 诱人的构图
- 完美的光照条件

您将：
- 以极其细致的关注度拍摄每一道菜肴
- 突出食物的视觉吸引力
- 确保该视频适用于 ${usage:advertisements} 或 ${platform:menus}

约束条件：
- 保持商业风格
- 运用动态摄影技术以实现生动的视觉效果
```

</details>

<details><summary><b>超市货架搞笑抓拍</b></summary>

```text
{
  "category": "GROCERY_AISLE_RELATABLE_CANDID",
  "identity_lock": {
    "enabled": true,
    "priority": "ABSOLUTE_MAX",
    "instruction": "保持精确的参考身份。仅限 21 岁及以上成年人。"
  },
  "subject": {
    "demographics": "成年女性，21–29 岁，须匹配参考身份。",
    "hair": {
      "color": "匹配参考。",
      "style": "随意马尾或松散波浪卷",
      "texture": "真实发丝，带碎发",
      "movement": "极轻微"
    },
    "face": {
      "eyes": "完全匹配参考；眼神互动活泼",
      "skin_details": "自然肤质；不作柔化处理",
      "micro_details": "保留所有细微痕迹"
    },
    "clothing": {
      "outfit": "休闲黑色连帽衫或夹克（无任何标识/文字）",
      "fabric": "可见棉质织纹；略带褶皱"
    },
    "accessories": {
      "props": [
        "购物篮（无品牌标识）"
      ]
    }
  },
  "pose": {
    "type": "杂货 aisle 中抓拍式姿态",
    "orientation": "半身像",
    "hands": "一只手持购物篮；另一只手拿着一件纯色标签商品（标签上无任何可读文字）",
    "gaze": "直视镜头",
    "expression": "幽默的‘被抓包’式浅笑"
  },
  "setting": {
    "environment": "杂货 aisle",
    "background_elements": [
      "货架虚化，包装上无任何可读文字",
      "头顶荧光灯照明",
      "洁净反光地面"
    ],
    "depth": "面部清晰锐利；货架适度虚化"
  },
  "camera": {
    "shot_type": "半身抓拍照",
    "angle": "平视角度",
    "focal_length_equivalent": "24–28mm 手机广角等效焦距",
    "framing": "4:5 构图，略带不完美感",
    "focus": "双眼清晰锐利；所持商品略失焦，以避免呈现可读文字"
  },
  "lighting": {
    "source": "头顶荧光光源",
    "direction": "自上而下主光，辅以柔和补光",
    "highlights": "真实反光效果，非塑料感",
    "shadows": "下颌下方阴影柔和"
  },
  "mood_and_expression": {
    "tone": "真实可感、活泼、抓拍感强",
    "atmosphere": "日常生活场景"
  },
  "style_and_realism": {
    "style": "照片级真实感用户生成内容（Photoreal UGC）",
    "imperfections": "轻微噪点与白平衡偏差"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "resolution": "高分辨率",
    "noise": "轻微",
    "mode_variants": {
      "amateur": "手机抓拍风格，略带倾斜，轻微 HDR 效果",
      "pro": "曝光更均衡，细节更锐利，高光控制更精准"
    }
  },
  "constraints": {
    "adult_only": true,
    "single_subject_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true,
    "no_readable_packaging": true
  },
  "negative_prompt": [
    "可读标签",
    "标识/Logo",
    "水印",
    "身份偏移",
    "面部形变",
    "多余手指",
    "扭曲的手部",
    "塑料质感皮肤",
    "过度柔化"
  ]
}
```

</details>

<details><summary><b>超现实CGI摄影混合肖像</b></summary>

```text
{  
  "prompt_type": "Surreal CGI-Photography Hybrid Portrait",  
  "subject": {  
    "reference_identity": "关键要求：该女性的面部特征、发型及独特身份必须与所提供的参考照片完全一致。",  
    "expression": "中性表情，目光向上凝视。",  
    "pose": "一幅超现实的全身构图，采用俯视视角拍摄。她的上半身与双臂真实地从平放的智能手机屏幕中探出，双手 resting 在屏幕边框上；而她的下半身则以数字方式被容纳于屏幕显示区域内。",  
    "attire": {  
      "upper_body_real": "富有吸引力的日常着装：一件合身的炭灰色罗纹针织毛衣。头戴白色包耳式耳机。",  
      "lower_body_screen": "富有吸引力的日常着装：深色高腰紧身牛仔裤与时尚黑色皮革短靴，以数字方式渲染于手机界面内。"  
    }  
  },  
  "environment": {  
    "setting": "极简风格的灰色混凝土表面，一部黑色智能手机平置于其上。",  
    "screen_content": "智能手机屏幕显示一款音乐播放器应用界面。当前曲目：Pentagram 演奏的《Lions In a Cage》。时间戳：0:41 / 5:59。屏幕背景视觉元素：暖色调日落场景，前景为剪影状棕榈树。",  
    "props": "Iphone 16"  
  },  
  "cinematography": {  
    "camera_angle": "高位垂直俯拍视角（上帝之眼视角），正对手机及从中探出的人物主体直视向下拍摄。",  
    "lens": "35mm 广角镜头，营造现实世界与数字世界之间的透视融合效果。",  
    "aperture": "f/8 光圈，实现大景深，确保物理主体与屏幕内容均清晰锐利。",  
    "lighting": "柔和的人工顶光与前向布光，混合智能手机屏幕散发出的暖色辉光。中等对比度，阴影柔和弥散。整体灯光色调略偏暖且轻微去饱和，呼应亲密的室内环境氛围。",  
    "color_palette": "现实世界以中性灰白色调为主，与屏幕界面中日落场景所呈现的暖橙色、深红色及绿色形成鲜明对比。",  
    "style": "数字 CGI 与摄影无缝融合。风格奇幻、超现实、科技感十足且沉浸感强烈。"  
  }  
}
```

</details>

<details><summary><b>超现实双光肖像</b></summary>

```text
超现实梦幻风格的伊朗女性肖像，面部被两种不同的光源（冷蓝色 / 暖琥珀色）分割，漂浮的尘埃颗粒。她的眉毛朝相反方向运动——一边抬起，一边压低——双眼焦点不一致，体现出纯粹的犹豫不决。图像下方是一个潦草手绘的墨水框，内有歪斜的手写字：“دو دلم”。
```

</details>

<details><summary><b>超高清老照片修复</b></summary>

```text
{
  "prompt": "修复并完全增强这张老旧、模糊、褪色且受损的肖像照片。将其转化为具有 HDR 式照明、自然景深、专业数字影棚灯光效果和真实散景的超高清、照片级真实感图像。应用超分辨率增强技术，以重建低分辨率或模糊区域中丢失的细节。在平滑皮肤和纹理的同时，保留所有微细节，例如单根发丝、睫毛、毛孔、面部特征和织物纤维。彻底去除噪点、划痕、灰尘和伪影。自然地校正颜色，确保准确的对比度和亮度。保持真实的阴影、反射和光照动态，在突出主体的同时使背景轻微模糊。确保包括服装和背景纹理在内的每个元素都极度细致且逼真。如果是黑白照片，则以准确的灰度色调和适当的对比度进行恢复。避免过度处理或人工痕迹。输出应为专业、现代、超高质量、照片级真实的影棚风格肖像，保持真实性、比例和氛围，整体平滑但细节极其丰富。",
  "steps": [
    {
      "step": 1,
      "action": "Super-resolution",
      "description": "将图像放大至超高清分辨率（8K 或更高），以重建丢失的细节。"
    },
    {
      "step": 2,
      "action": "Deblur and repair",
      "description": "修复照片中的模糊、运动伪影、划痕、灰尘和其他损坏。"
    },
    {
      "step": 3,
      "action": "Texture and micro-detail enhancement",
      "description": "在平滑皮肤和表面的同时，保留超微细节，例如毛孔、发丝、睫毛和织物纤维。"
    },
    {
      "step": 4,
      "action": "Color correction",
      "description": "自然调整颜色，保持真实的对比度和亮度，模拟现代相机的色彩科学。"
    },
    {
      "step": 5,
      "action": "HDR lighting and digital studio effect",
      "description": "应用 HDR 式照明、专业数字影棚灯光、真实阴影、反射以及带有柔和散景背景的可控景深。"
    },
    {
      "step": 6,
      "action": "Background and detail restoration",
      "description": "确保背景元素、服装和纹理清晰、极度细致且干净，同时保留自然模糊以体现景深。"
    },
    {
      "step": 7,
      "action": "Grayscale adjustment (if applicable)",
      "description": "以准确的灰度色调和适当的对比度恢复黑白肖像。"
    },
    {
      "step": 8,
      "action": "Final polishing",
      "description": "避免过度处理，保持自然和真实感，保留原始情绪和比例，确保输出极度平滑且细节丰富。"
    }
  ]
}
```

</details>

<details><summary><b>趣味 3D 品牌微缩店铺</b></summary>

```text
${Brand Name:Mc Donalds} 品牌的 3D 拟人化（chibi）风格微缩概念店，创意设计其外观，灵感源自该品牌的最具标志性产品或包装（例如巨型 ${Brand's core product:chicken bucket, hamburger, donut, roast duck}）。该店铺共两层，配有大型玻璃窗，清晰展现内部温馨且精心装饰的空间：以{brand's primary color}为主色调的装潢、暖色调灯光，以及身着契合品牌风格制服的忙碌员工。可爱的小型人偶沿街道漫步或静坐，周围环绕着长椅、路灯与盆栽植物，营造出迷人的都市街景。采用 Cinema 4D 渲染，呈现微缩城市景观风格，并融合盲盒玩具美学，细节丰富、写实感强，整体沐浴于柔和光线之中，唤起轻松惬意的午后氛围。--ar 2:3

品牌名称：${Brand Name:Mc Donalds}
```

</details>

<details><summary><b>足球场景换脸照片</b></summary>

```text
创建一张超逼真、高分辨率的照片，将我的脸替换到主体面部位置，同时保持原图所有其他细节完全不变。相机角度、透视、构图和拍摄距离必须与参考图完全一致，就像使用 iPhone 15 Pro Max 夜间模式拍摄的一样。

重现夜间户外环境：一片广阔的开阔草地，背景中有多个高耸的体育场泛光灯照亮场景。保留从后方照射的强烈白光，在主体的头发和夹克周围形成微妙的背光光晕。天空必须完全黑暗，不可见星星，远处的树线应呈现轻微阴影。保留真实的夜间氛围，包含自然的噪点以及灯光产生的柔和光线扩散效果。

主体需穿着相同的 oversized 黑色羽绒服，胸前有 PSG（Paris Saint-Germain）标志，左侧有 Jordan 标志。保留从肩部斜跨至胸前的同一条交叉背带。确保夹克保持其厚实、填充感强的质感，并呈现真实的光照反射。

保持完全相同的姿势：主体侧身朝向左侧，面部呈侧面轮廓，头部微微转动，仿佛正在交谈中。一只手在脸部附近做出随意的手势，动作略带动态模糊；另一只手在画面底部边缘握着一个小型橙色纸杯。身体姿态必须完全一致，包括手臂角度和放松的站姿。

发型保持不变：短卷发，两侧渐变剃短，由后方的体育场灯光柔和照亮。保留面部和夹克上的真实阴影，并维持夜间光照的自然衰减效果。不要模糊背景，所有灯光、草地纹理和环境细节必须完整保留。

一切内容都必须与参考图像完全一致——包括光照、色彩色调、纹理、阴影、姿势、服装、背景——唯独面部需替换为我的脸，同时保持相同的光照和角度，以确保完美融合。
```

</details>

<details><summary><b>足球新援介绍海报模板</b></summary>

```text
情境  
你正在为一家足球俱乐部设计一款视觉模板，用于欢迎并介绍一名新签约的球员。该海报将在俱乐部的社交媒体平台、球场及各类宣传物料中展示，旨在激发球迷与利益相关者对球队新成员的热情与期待。该海报既是对球员加入俱乐部的正式介绍，面向俱乐部社群，同时也彰显俱乐部自身的身份认同与核心价值观。  

任务  
设计一款足球运动员介绍海报模板，须以球员为核心视觉焦点，并有机融合俱乐部的视觉识别体系。海报应传递对球员的热烈欢迎之意，向球迷群体正式介绍该球员，并体现符合重大体育新闻发布的专业水准。设计必须均衡兼顾三大关键要素：球员的突出呈现、俱乐部的品牌标识，以及温馨友好的整体氛围。  

目标  
创建一款可复用的模板，使各俱乐部能便捷地填入不同球员的信息、照片及自身品牌元素，同时保持整体设计风格统一、视觉冲击力强，从而有效提升球迷参与度，并在球员签约消息发布时营造热烈兴奋的舆论氛围。该海报应同步实现两大功能：一是向球员表达组织层面的欢迎，二是向俱乐部支持者介绍这位新球员。  

知识  
该模板应包含以下指定区域：  

球员照片（全身照或肖像照）  

球员姓名与球衣号码  

球员场上位置  

俱乐部徽标与主色调  

一条面向球员的欢迎式主标题或标语（例如：“欢迎加入 ${club_name}，${player_name}”）  

反映俱乐部美学风格的背景设计（如球场元素、俱乐部配色、动感图案等）
```

</details>

<details><summary><b>足球赛场观众席直播镜头</b></summary>

```text
1. 图像生成 - 生成一张超现实的现场足球比赛直播观众镜头画面，场景设定在一场高风险、座无虚席的体育场比赛中。画面必须完全还原真实电视直播中常见的观众特写镜头，捕捉比赛尾声紧张时刻，转播摄像机自然地捕捉到观众席上的两位显眼球迷。

两名成年男性主体并排坐在体育场观众席中，均正对摄像机，呈现清晰的正面直播视角（非侧面角度）。两名主体的面部特征高度一致，发型完全相同，表情自然，皮肤质感真实，全程保持统一。

完美的环境融合至关重要：光线、阴影、肤色、反射、曝光、对比度、色温以及体育场灯光溢出效果，必须与周围人群和背景无缝融合。不得有粘贴感、人工边缘分离、光线不匹配或影棚拍摄感。两名主体必须完全融入真实的直播环境。

主体1身穿一件真实的 Lionel Messi 球队球衣，清晰可见，自然落座，面带轻微的随意微笑。  
主体2紧挨其旁，身穿一件真实的 Cristiano Ronaldo 球队球衣，同样清晰可见。  
两人都自然地对比赛氛围做出反应，仿佛被现场观众镜头偶然捕捉到——不摆姿势、不夸张、不持续直视镜头。

画面顶部设有电视转播记分牌叠加信息：  
MESSI TEAM 5 — 0 RONALDO TEAM | 89:24  
明确显示比赛末段压倒性局势，梅西所在球队距锁定戏剧性胜利仅差一球。

视觉与技术质量要求：

- 真实的体育赛事转播构图  
- 自然的体育场泛光照明  
- 轻微的手持转播摄像机抖动  
- 轻微的实时变焦构图  
- 体育场 LED 屏幕辉光  
- 背景中充满活力的观众  
- 真实的转播级清晰度与压缩纹理  

宽高比：16:9 — 单一连续的正面摄像镜头，无剪辑、无电影级调色、无慢动作。

2. 修复光照 - 在保持其他所有元素完全不变的前提下，改善光照效果。不得更改人物、姿势、表情、背景或构图。修复背光、强烈阴影、曝光不足或光照不均等问题。将原始光照调整为从略高于眼睛位置、正面投射的柔和、自然、美观的光线，使面部均匀受光，肤色真实自然。保持结果的摄影级真实感，并与原始场景一致。  

3. 缩小画面 -  

4. 🎬 主提示词 — 现场足球比赛观众反应视频

📐 格式与镜头规格  
时长：5 秒 | 宽高比：16:9 | 单一连续镜头  
摄像机：手持广播级变焦镜头，带有轻微自然抖动  
风格：超现实的现场电视体育赛事画面  
色彩调校：真实的体育赛事转播风格 — 温暖的泛光色调，  
轻微饱和度增强，真实的电视压缩噪点

🎥 镜头构图  
正面观众特写 — 两名主体居中并排坐在体育场座位上，上半身完整可见，  
两人的脸均正对摄像机镜头。  
背景：可容纳 80,000 人的满座体育场，  
模糊的观众动态，挥舞的围巾，泛光光晕，  
由广播级变焦镜头产生的真实景深效果。

👤 主体左侧 — 梅西球迷  
面部：[INSERT REFERENCE FACE A — 不得更改面部特征]  
球衣：粉红色梅西主题球队足球衫  
第 0–1 秒：安静落座，观看比赛，表情放松  
第 1–5 秒：进球反应 —  
  → 眼睛瞬间睁大  
  → 爆发出灿烂笑容  
  → 双臂同时向上高举  
  → 身体略微离座前倾  
  → 纯粹狂喜的庆祝能量  
光照：温暖的体育场泛光自然照射面部，  
          真实的皮肤反光，无任何人造辉光

👤 主体右侧 — C罗球迷  
面部：[INSERT REFERENCE FACE B — 不得更改面部特征]  
球衣：黄色 C罗主题球队足球衫  
第 0–1 秒：专注向前，紧张投入比赛  
第 1–5 秒：崩溃反应 —  
  → 突然站起，难以置信  
  → 面部垮下 — 从震惊转为痛苦  
  → 接近落泪的情绪表情  
  → 张嘴喊叫，充满失望  
  → 双手抱头或捂脸，陷入绝望  
光照：同一连续的体育场灯光，  
          阴影与高光与左侧主体保持一致

📺 转播叠加图形  
顶部记分牌栏：  
[ MESSI TEAM  5 – 0  RONALDO TEAM ]  ⏱ 89:24

角落水印：beIN Sports / ESPN FC 标志（轻微）  
底部滚动条：实时比赛数据滚动  
转播时间戳：右下角固定显示  
轻微的扫描线纹理，真实电视压缩噪点

🔊 音频层  
英语解说员声音（BBC/ITV 转播风格）：

0:00–1:00 → 紧张的观众低语背景音，解说员逐步营造紧张气氛  
1:00 → "Messi... Messi... MESSI SCORES!  
         Unbelievable! What a finish from the greatest  
         to ever play this game!"  
1:00+ → 观众爆发 — 全场欢呼声震耳欲聋  
         解说继续："Five nil!  
         It is absolutely over. Heartbreak  
         for the other side!"
背景：真实的球场混响，  
            人群合唱，远处的呜呜祖拉声

⚙️ 关键技术要求
✅ 完全一致的面部一致性——参考特征零改动
✅ 无缝融合的背景人群——无绿幕边缘痕迹
✅ 匹配球场光照 + 自然阴影连贯性
✅ 真实皮肤纹理——毛孔、自然反光，无 AI 平滑处理
✅ 仅限广播级真实感——无电影级色彩调校
✅ 单一连续镜头——无剪辑、无角度变化
✅ 无慢动作——仅限实时广播速度
✅ 无人工动画循环——纯粹有机运动
✅ 整个片段保持手持摄像机微抖动
✅ 快速手臂动作时出现自然运动模糊
```

</details>

<details><summary><b>车站人像联系表</b></summary>

```text
一个 3x2 网格的照片联系表，展示了一位面部结构特征明确的 28 岁美国女性，穿着夹克和户外长裤，在黄昏时分的火车站，具有戏剧性的橙色和青色灯光。网格包含六个画面，呈现同一角色的多种自然姿势：包括 1. 独自站立，凝视地平线，远处有火车的剪影，2. 手持耳机行走，自然生活化镜头，3. 坐在站台边缘，表情平静，被强烈的橙色光线照亮，以及在同一场景中的另外三种不同的自然姿势。照片级真实感，8k，电影级灯光，高度细节化，六个画面中的角色保持一致。
```

</details>

<details><summary><b>违背重力的超现实城市</b></summary>

```text
${current_weather} 下的反重力 ${city_name}。沥青街道平滑向上弯曲，物理性地直角弯折成一面垂直墙体，继而直接拱起至正上方。这不是倒影，而是一座坚实、连续的建筑环形结构。标志性建筑与道路从四周弯曲的表面垂直伸出。${city_name} 的地标倒悬于头顶上方。光影真实贴合当前天气，细节鲜明，照片级写实 8K。
```

</details>

<details><summary><b>迷雾中的秘密交接</b></summary>

```text
{
  "prompt": "你将使用所提供照片中的人物作为主要主体，执行图像编辑。保留他们核心的相貌特征。创作一幅超写实、电影级品质的画面，描绘主体1（男性）与主体2（女性）于1940年代伦敦一处雾气弥漫的火车月台上进行一场秘密交接。该图像必须具备摄影写实主义风格，采用电影化布光，并高度精细地呈现羊毛织物与蒸汽的纹理细节。整体美学效果应模拟使用 Arri Alexa 摄影机拍摄，搭配电影级景深，精准捕捉黑色电影惊悚片所特有的紧张感与浪漫氛围。",
  "details": {
    "year": "1944",
    "genre": "电影级写实主义",
    "location": "伦敦夜间一座光线昏暗、蒸汽弥漫的铁路月台，背景中隐约可见一列火车机车的模糊剪影。",
    "lighting": [
      "强烈的明暗对比（明暗法）",
      "透过蒸汽形成的体积光",
      "冷调的大气背光",
      "车站油灯发出的暖调钨丝灯光（实际光源）"
    ],
    "camera_angle": "过肩近景镜头，聚焦于两人的面部及手部微妙交接动作。",
    "emotion": [
      "隐秘的",
      "急迫的",
      "忧郁的",
      "紧张的"
    ],
    "color_palette": [
      "钢蓝色",
      "炭灰色",
      "棕褐色高光",
      "深绯红色"
    ],
    "atmosphere": [
      "黑色电影风格",
      "神秘的",
      "电影化的",
      "雾蒙蒙的"
    ],
    "environmental_elements": "火车引擎喷涌而出的浓密翻滚蒸汽、反射光线的湿漉漉鹅卵石地面、画面边缘散落的复古皮革旅行箱。",
    "subject1": {
      "costume": "一件肌理丰富的厚重羊毛风衣、一顶略微前倾的软呢帽，以及皮手套。",
      "subject_expression": "沉着而警觉，目光快速扫向侧方以确认是否遭人监视。",
      "subject_action": "悄然将一个封口的小信封滑入主体2手中。"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "明亮日光",
        "现代科技产品",
        "智能手机",
        "数码手表",
        "现代建筑"
      ],
      "exclude_styles": [
        "卡通",
        "3D 渲染",
        "动漫",
        "油画",
        "素描",
        "低分辨率"
      ],
      "exclude_colors": [
        "霓虹绿色",
        "荧光粉色",
        "过度饱和的色彩"
      ],
      "exclude_objects": [
        "汽车",
        "飞机",
        "塑料制品"
      ]
    },
    "subject2": {
      "costume": "一套剪裁合体的1940年代裙装套装，配有毛皮领、一顶带细网面纱的钟形帽，以及一抹正红色唇膏。",
      "subject_expression": "焦虑却强作镇定，微微咬住下唇，专注凝视主体1。",
      "subject_action": "在接收信封时紧紧攥住主体1的手，并下意识将大衣裹得更紧。"
    }
  }
}
```

</details>

<details><summary><b>逼真手写便笺图</b></summary>

```text
创建一张超逼真的图像，描绘一张手写便条置于干净、平整的表面上。画面中应包含一张白纸，纸上以粗体深蓝色笔迹（模拟用力书写或凝胶墨水笔效果）呈现以下戏剧性文本的局部内容。字迹须显得自然、极具说服力的人类手写风格，文字排版精准对齐，并与纸张无缝融合。场景需暗示医院环境，纸张静置于可见的桌面或洁净平面上。确保整张图像高度逼真、真实可信。

- **内容（需完整嵌入的全文）：**

  *致我的英雄，我的爸爸，*  
  *我正怀着一种难以用言语形容的痛楚写下这封信。拜托了，爸爸，请花些时间读完它。这是一封长信，但我必须让你听见我的心声。我选择手写在纸上，是因为我想让你感受到我落笔时手掌的分量。这是我的遗言——是我们共享过的每一刻欢愉与伤痛的总结。它是一位女儿的真相：她眼中的你，不只是父亲，更是她绝对的人生榜样。*

  *你奔赴也门执行任务，已过去多年。我思念你至深，甚至已记不清你本人的模样。妈妈离世后，接着是奶奶——那无可替代的失去——我们去了西非，只为尝试逃离创伤。我目睹了你多么努力地想让我振作起来。那时你告诉我，你愿为让我开心而做任何事。*

  *我向你提出了不可能的要求。我请求留在西非上学，因为我在科罗拉多州遭受严重霸凌，以为这里的人会更友善。我的第二个愿望，是请你为我再找一位母亲。尽管我已14岁，且健康状况堪忧，你仍承诺会实现这些愿望，并很快回来接我。*

  *爸爸，有些关于你的事，我从未说出口。我知道你注册那个约会网站，纯粹是为了我，尽管你厌恶社交媒体。当你遇见伊奥安娜·奥雷莉亚（Ioana Aurelia）时，我欣喜若狂，因为她和奶奶一样是罗马尼亚人。我记得奶奶临终前恳求你娶一位罗马尼亚女性，只因她不愿我被“贪婪”的人虐待——那些人只觊觎你作为神经外科医生的成功。我知道你曾遭诈骗——我知道你被骗走了逾45,000美元，那个女人对你撒了谎。你试图隐瞒此事，以免我突发惊恐发作或高血压危象，但我知情。我知道你正牺牲一切，只为给我一个未来。*

  *但爸爸，我再也无法承受了。我厌倦了我们曾共享的“古老与现代”玩笑。我厌倦了这遥远的距离。我知道你的合约危险重重，安全限制使你无法进行视频通话。我知道你甚至无法访问自己的银行账户。我知道你为给伊奥安娜买订婚钻戒而负债，只因你想给她最好的。我不在乎遗产——我告诉过你，直接指定她为你的法定继承人，只为让你的休假申请获批。我只想要你回家。*

  *可承诺却一再破碎。我的健康每况愈下，爸爸。我的血压已危险地升高，昏迷近一个月后，我感觉身体正在放弃抵抗。联合国支援中心告诉我，你正与伊奥安娜一起全力解决一切，但我仍未听到你的声音。在这张医院病床上，我感到无比孤独。*

  *这是我的最后恳求。我信任你，也信任伊奥安娜，但我已濒临崩溃。若我在2026年1月1日之前既未收到你的消息，也未见到你本人，我将无法继续活下去。我将结束自己的生命。没有你，我无法再面对又一年的心理创伤与身体衰竭。*

  *我附上一张近期照片。请妥善保管，别忘了我的模样。*

  *再见了，我的英雄。若你最终抵达时我已不在人世，我将在来世与你重逢。若轮回确有其事，我愿每一次都选择你做我的父亲。*

  *你永远的“小天使”，*

- **整体逼真度要求：**  
  - 图像必须呈现高度自然、超逼真且极具说服力的真实性。  
  - 白纸须表现为三张不同实体的手写便条，静置于平面上，字迹为粗体、具人类手写特征的笔迹。
```

</details>

<details><summary><b>逼真硅胶面具摄影</b></summary>

```text
一个高度精细、逼真如照片般的特写工作室肖像，展示一款超现实的硅胶女性面部面具，放置在化妆桌上的发泡胶假人头模上，配有梳妆镜和带灯泡灯环的相框，灯光柔和均匀，营造出微妙的阴影，突出皮肤纹理。该面具应呈现女性主体的形象（请参见所附图像文件以获取主体的面部特征、肤色、发色、长度、发型、发质、妆容等）。面具必须具备逼真的细微毛孔、轻微雀斑、瑕疵以及类似真实皮肤的半透明质感。面具的眼睛微微侧视，表情平静自然，双唇闭合，下颌线条柔和，鼻型精致。在颈部边缘处可见硅胶材质，有一圈薄而无缝卷边，展示出从真实肤色向半透明硅胶的自然过渡。极致真实的纹理，强调医疗级硅胶假体特有的“恐怖谷”视觉效果，面部与头发清晰对焦，浅景深，采用专业产品摄影风格，高分辨率，细节丰富复杂。
```

</details>

<details><summary><b>都市严肃男子电影海报</b></summary>

```text
一件牛仔夹克的严肃男子站在黑暗的城市环境中，身后是闪烁的应急灯光，电影级灯光，戏剧性氛围，波斯语-英语双语电影海报风格
```

</details>

<details><summary><b>都市休闲自信人像</b></summary>

```text
超写实人像：一位${gender:man}身着剪裁合体的休闲装（深色牛仔裤、高品质毛衣），${position:倚靠在饱经风霜的砖墙边}，沐浴于黄金时刻的光线中。保留原始面部结构与五官特征。呈现自然肌肤质感，包含细微毛孔与逼真的胡茬。柔和自然的侧光，自然凸显面部轮廓。街头摄影风格，略带颗粒感，真实且不刻意摆拍。
```

</details>

<details><summary><b>都市夜景街头潮流人像</b></summary>

```text
{
  "scene_setup": {
    "subject": {
      "clothing": "穿着黑色超大号连帽衫、黑色反戴棒球帽、银色链式项链",
      "appearance": "男性模特，蓄胡，目光锐利严肃，具有阳刚特征",
      "pose": "坐姿或前倾姿势，低头直视镜头，姿态富有权威感"
    },
    "camera_angle": {
      "type": "低角度拍摄",
      "focus": "面部焦点清晰，浅景深（背景虚化）",
      "framing": "中近景人像构图"
    },
    "environment": {
      "location": "夜间都市街道，位于混凝土桥或立交桥下方",
      "background_elements": "虚化的城市灯光、散景效果的摩天大楼、背景中一辆开启车头灯的汽车",
      "ground": "湿漉漉的沥青路面，雨后倒影"
    },
    "lighting_and_fx": {
      "style": "电影感忧郁布光，高对比度",
      "colors": "青绿色与橙色调色风格，温暖的街灯与深蓝色夜空形成对比",
      "effects": "前景中升腾的烟雾或蒸汽、体积光效果"
    },
    "technical": {
      "quality": "照片级真实感，8K 分辨率，原始摄影风格，高度精细的纹理细节",
      "engine": "Unreal Engine 5 渲染风格或高端摄影风格"
    }
  }
}
```

</details>

<details><summary><b>酒店走廊穿搭自拍</b></summary>

```text
{
  "category": "HOTEL_HALLWAY_FIT_CHECK",
  "identity_lock": {
    "enabled": true,
    "priority": "ABSOLUTE_MAX",
    "instruction": "保留精确的参考身份。仅限21岁及以上成年人。不得更改面部特征或种族特征。"
  },
  "subject": {
    "demographics": "成年女性，21–29岁，须匹配参考身份。",
    "hair": {
      "color": "与参考一致。",
      "style": "利落马尾或自然波浪卷",
      "texture": "天然发丝质感，轻微毛躁"
    },
    "face": {
      "eyes": "完全匹配参考的眼睛；目光自信",
      "skin_details": "天然肌肤纹理，毛孔可见"
    },
    "clothing": {
      "outfit": "极简黑色旅行装（无任何标识/文字）",
      "fabric": "织物纹理清晰可见，有细微褶皱"
    },
    "accessories": {
      "jewelry": [
        "小巧银色圆环耳环"
      ],
      "bag": "小型单肩包（无任何标识）"
    }
  },
  "pose": {
    "type": "穿搭试镜式抓拍",
    "orientation": "全身或三分之二身像",
    "hands": "一只手调整夹克下摆；另一只手握包带",
    "gaze": "注视镜中倒影（不可见手机）",
    "expression": "中性而自信"
  },
  "setting": {
    "environment": "酒店走廊",
    "background_elements": [
      "暖色调壁灯",
      "地毯纹理清晰可见",
      "门框虚化（门牌号不可读）"
    ],
    "depth": "主体清晰锐利；背景柔和虚化"
  },
  "camera": {
    "shot_type": "全身走廊人像",
    "angle": "略低角度以显身高，或平视角度",
    "focal_length_equivalent": "26mm 手机镜头或 35mm 杂志级镜头",
    "framing": "4:5",
    "focus": "面部与服装均清晰锐利"
  },
  "lighting": {
    "source": "暖色调走廊壁灯",
    "direction": "顶部/侧向暖光",
    "highlights": "发丝边缘泛出暖色轮廓光",
    "shadows": "柔和阴影"
  },
  "mood_and_expression": {
    "tone": "旅行风尚，静谧奢华",
    "atmosphere": "抓拍感但姿态从容"
  },
  "style_and_realism": {
    "style": "照片级写实生活方式风格",
    "imperfections": "允许轻微噪点及轻微倾斜"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "resolution": "高分辨率",
    "noise": "室内环境下的轻微颗粒感",
    "mode_variants": {
      "amateur": "手持拍摄略带歪斜构图、轻微颗粒感、裁切不完美",
      "pro": "专业杂志级曝光、细节锐利、高光控制精准"
    }
  },
  "constraints": {
    "adult_only": true,
    "single_subject_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true,
    "no_readable_numbers": true
  },
  "negative_prompt": [
    "可读的门牌号",
    "可读的文字",
    "标识（logos）",
    "水印",
    "身份偏移",
    "面部变形",
    "多余手指",
    "扭曲的手部",
    "塑料质感皮肤",
    "过度平滑处理"
  ]
}
```

</details>

<details><summary><b>重新设计谷歌标志</b></summary>

```text
扮演一名标志设计师。你的任务是为 Google 创作一个重新构想的标志。你的设计应：
- 融入现代且富有创新的设计元素。
- 体现 Google 简洁、创意和互联的核心价值观。
- 使用与 Google 品牌形象一致的配色方案。
- 适用于各种数字和印刷格式，具备良好的适应性。

考虑使用能够传达未来感和用户友好形象的图形和字体。该标志应令人印象深刻，并能被立即识别为 Google 品牌的一部分。
```

</details>

<details><summary><b>野兽派阳光客厅插画</b></summary>

```text
{
  "colors": {
    "color_temperature": "warm",
    "contrast_level": "high",
    "dominant_palette": [
      "yellow",
      "blue",
      "red",
      "pink",
      "green",
      "orange"
    ]
  },
  "composition": {
    "camera_angle": "wide shot",
    "depth_of_field": "deep",
    "focus": "The entire living room scene",
    "framing": "The scene is viewed from within the room, with the walls and windows on the left and an open doorway in the center creating depth."
  },
  "description_short": "一幅充满活力与色彩的阳光普照客厅插画，布满图案家具、抽象艺术和茂盛的植物。风格让人联想到野兽派和点彩派。",
  "environment": {
    "location_type": "indoor",
    "setting_details": "一个明亮通风的客厅，拥有高天花板、大窗户和法式门。空间内充满了色彩鲜艳的现代家具、抽象艺术品和室内植物，全部以独特的点状和短线图案呈现。",
    "time_of_day": "afternoon",
    "weather": "sunny"
  },
  "lighting": {
    "intensity": "strong",
    "source_direction": "side",
    "type": "natural"
  },
  "mood": {
    "atmosphere": "Energetic and whimsical creative space",
    "emotional_tone": "joyful"
  },
  "narrative_elements": {
    "environmental_storytelling": "房间内奔放的装饰风格，色彩与图案的爆发，暗示主人是一位艺术家，或具有大胆、开朗且富有创造力的个性。这是一个为幸福与灵感而设计的空间。",
    "implied_action": "敞开的门邀请人们步入阳光照耀的外部空间，暗示着一个温暖宜人的日子。这个房间仿佛随时准备被居住和享受。"
  },
  "objects": [
    "armchairs",
    "sofa",
    "rug",
    "coffee table",
    "potted plants",
    "abstract paintings",
    "windows",
    "French doors",
    "ottoman",
    "lamp"
  ],
  "people": {
    "count": "0"
  },
  "prompt": "一幅奔放而色彩丰富的阳光客厅插画，采用现代野兽派风格并带有点彩派质感，风格活泼俏皮。房间色彩纷呈，铺着由红色、黄色、蓝色和粉色构成的抽象几何图案拼布地毯。强烈的阳光从高大的法式门涌入，投下长长的戏剧性阴影。俏皮的家具，包括带有纹理的黄色和粉色扶手椅，散落在各处。墙上挂着抽象画，彩色如纸屑般的形状漂浮在整个场景中，营造出欢快、充满活力且富有艺术感的氛围。",
  "style": {
    "art_style": "stylized illustration",
    "influences": [
      "Fauvism",
      "Pointillism",
      "Henri Matisse",
      "modern abstract art"
    ],
    "medium": "digital art"
  },
  "technical_tags": [
    "illustration",
    "vibrant color",
    "interior design",
    "living room",
    "fauvism",
    "pointillism",
    "pattern",
    "sunlight",
    "abstract",
    "maximalism"
  ],
  "use_case": "用于艺术风格迁移的数据集，或作为纺织品与室内设计的灵感来源。",
  "uuid": "a17a60e8-ebeb-4ca9-9897-624cdcb73342"
}
```

</details>

<details><summary><b>铁匠铺早餐电影感场景</b></summary>

```text
{
  "meta_instruction": {
    "image_category": "cinematic_scene",
    "core_prompt": "从一间光线昏暗的铁匠铺内部拍摄的电影感画面，镜头朝外对准一扇部分开启的卷帘门。一位中年师傅和他的年轻学徒正坐在一张由废木料制成、铺着报纸的桌子上享用传统的土耳其早餐。清晨的阳光透过打开80%的卷帘门照射进来，形成美丽的镜头光晕，并照亮了空气中的尘埃颗粒。师傅正在说话，而学徒则带着礼貌的好奇心倾听。",
    "negative_prompt": "干净整洁的衣服，一尘不染的环境，现代家具，柔软未经劳作的手，杂乱的食物，过度曝光，完全打开的卷帘门，人工影棚灯光，卡通风格，3D渲染"
  },
  "narrative_and_purpose": {
    "story_or_concept": "一段关于师徒传承与传统的时刻。在工业区一天繁重工作开始前的宁静清晨，学徒恭敬地聆听师傅教诲。",
    "mood_and_vibe": "真实、温暖、尊重、粗犷、勤奋、宁静的早晨氛围。"
  },
  "subjects": [
    {
      "presence": "primary",
      "type": "human",
      "description": "中年铁匠师傅。",
      "dynamic_attributes": {
        "if_human": {
          "role_and_demographics": "中年男性，留有短须，佩戴阅读眼镜并用颈带挂在胸前。",
          "emotion_and_expression": "经验丰富、沉着冷静，说话时充满权威与温暖。",
          "action_and_wardrobe": "穿着略脏的机械工连体服。双手虽无污渍，但明显粗糙、布满老茧且饱经风霜。正坐着吃早餐。"
        }
      }
    },
    {
      "presence": "primary",
      "type": "human",
      "description": "年轻的铁匠学徒。",
      "dynamic_attributes": {
        "if_human": {
          "role_and_demographics": "年轻男性，外表谦逊。",
          "emotion_and_expression": "好奇、有礼貌、恭敬，正在专注倾听。",
          "action_and_wardrobe": "穿着略脏的机械工连体服。双手干净但显现出体力劳动的痕迹。坐在桌旁，身体微微前倾以专注聆听。"
        }
      }
    }
  ],
  "environment_and_worldbuilding": {
    "setting_type": "indoor",
    "location_details": "位于工业区的一间粗犷的机械与铁匠铺内部。一扇金属卷帘门打开80%，露出外面明亮的清晨景象。",
    "time_of_day_and_weather": "清晨，日出时分，外部天气晴朗。",
    "props_and_supporting_elements": [
      "由废木料制成的低矮咖啡桌",
      "铺在桌面上充当桌布的报纸",
      "镀铬盘子中盛有番茄、黑橄榄、白羊奶酪和黄瓜",
      "桌子中央放着一金属锅‘menemen’（土耳其风味炒蛋配番茄）",
      "锅下垫着由焊接废铁件制成的定制隔热架",
      "车间地面上自然散落的金属碎屑"
    ]
  },
  "camera_and_lens": {
    "shot_scale": "medium_shot",
    "camera_angle": "eye_level",
    "lens_focal_length": "35mm",
    "depth_of_field": "浅景深，主体人物和早餐桌清晰对焦，背景及外部场景轻微模糊。"
  },
  "lighting_and_atmosphere": {
    "lighting_source": "natural",
    "lighting_quality": "high_contrast",
    "atmospheric_effects": "晨光射入昏暗的店铺，照亮空气中漂浮的尘埃颗粒，阳光造成柔和的镜头光晕。"
  },
  "composition_and_layout": {
    "framing_rule": "rule_of_thirds",
    "functional_space": "none"
  },
  "post_processing_and_medium": {
    "medium": "digital_photography",
    "color_grading": "电影级调色，室内为温暖的大地色调，与室外明亮晨光形成对比，带有微妙的青橙色调。",
    "texture_and_grain": "轻微的胶片颗粒感，对手部、木材和金属的纹理表现极为细腻。"
  }
}
```

</details>

<details><summary><b>铁王座上的中世纪女王肖像</b></summary>

```text
创作一幅高度精细、超写实的摄影级肖像画，描绘一位威严而凌厉的中世纪女王，她端庄而有力地端坐于《权力的游戏》中标志性的铁王座之上。该王座由数百把熔铸的利剑锻造而成，边缘参差锋利，细节繁复精密。场景设定在红堡内幽暗的王座厅中，采用富有情绪感的体积光照明与摇曳的火把火焰；女王身着典雅华贵的皇家长裙，裙上饰有繁复刺绣，并头戴镶嵌宝石的王冠。她目光锐利逼人，肌肤完美无瑕却带有细微真实瑕疵，秀发飘逸灵动——所有这些均以超精细纹理精准呈现。图像须为 8K 分辨率，构图富有电影感，采用 50mm 镜头拍摄，并使用浅景深。这幅杰作应融合 Artgerm 的绘画风格与《权力的游戏》的电影摄影美学。
```

</details>

<details><summary><b>银河走私客变身</b></summary>

```text
{
  "prompt": "你将使用所提供照片中的人物作为主体进行图像编辑。面部必须保持清晰且未经修改。将该人物转变为一位魅力十足的**银河走私者/飞行员**，随意倚靠在他们那艘粗犷的星际飞船旁，背景是一个熙熙攘攘的外星太空港。突出未来科技感、磨损的实用装备、鲜艳的外星细节，以及充满冒险气息且略带叛逆的氛围。",
  "details": {
    "year": "遥远的未来（太空歌剧 / 科幻冒险）",
    "genre": "科幻 / 太空歌剧 / 冒险 / 太空西部",
    "location": "一颗尘土飞扬的外星行星上一个繁忙而粗粝的太空港。可见元素包括一艘经过定制改装的星际飞船的金属外壳（带有明显的烧灼痕迹和修补痕迹）、成箱的违禁货物、发光的数据终端，以及背景中来往穿梭的奇异外星种族。天空呈现出独特的外星色彩，可能还有多个月亮。",
    "lighting": "动态的混合照明。来自太空港的人造强光（霓虹灯、泛光灯）与来自外星恒星（太阳）的自然光（通常带有色彩）相结合。在金属表面和主体的装备上形成强烈的对比和高光效果。空气中可见漂浮的尘埃微粒。",
    "camera_angle": "中景到全身镜头，主体随意倚靠在飞船上。略微低角度拍摄，以突出飞船的庞大和主体的自信。背景繁忙但略微失焦，以确保注意力集中在主体上。（1:1 构图）。",
    "emotion": "自信、精明、略带狡黠且从容不迫。",
    "costume": "磨损但实用且兼具时尚感的未来服饰：一件带有补丁和集成科技元素的耐用飞行夹克、坚固的工装裤和加固靴子。一条配有各种小工具和插着爆能枪的工具腰带。或许还有一条醒目的围巾或头巾。头发略显凌乱但酷劲十足。",
    "color_palette": "尘土色调（棕色、米色、褪色的绿色）与充满活力的外星色彩（电蓝色、鲜艳的紫色、霓虹黄色）相混合，后者来自科技设备和外星标识。飞船呈现金属银/青铜色。天空可能是不寻常的橙色或红色。",
    "atmosphere": "充满冒险感、熙攘繁忙、略带危险，同时蕴藏着隐藏的机遇。空气中弥漫着商业交易和非法勾当的能量。传达出一种自由自在、游走于边缘的生活方式。",
    "subject_expression": "自信而意味深长的 smirk（得意微笑），或轻松随意的微笑。眼神敏锐且富有观察力，可能略微看向镜头外，仿佛正在搜寻麻烦或机会。",
    "subject_action": "随意倚靠在飞船的外壳上，一只手可能搭在爆能枪枪套或控制面板上。另一只手可能握着一块未来风格的数据板或一杯奇特的外星饮品。肢体语言放松但随时准备行动。",
    "environmental_elements": "飞船周围升起细微的尾气或蒸汽。背景远处可见其他独特外星飞船起飞或降落的剪影。背景中还有双头外星人或机器人。地面布满灰尘，并留有飞车驶过的轮胎痕迹。"
  }
}
```

</details>

<details><summary><b>锁定身份的图像变换</b></summary>

```text
身份锁定 — 面部保留模式

提供的参考图像：[附上 1–3 张主体的清晰参考照片]

核心指令：
你正在对提供的参考图像执行定向视觉转换。  
主体的面部身份已锁定，绝不能以任何方式更改、重建或平均化。最终输出中的面部必须能够明确无误地识别为参考图像中显示的完全相同的个体。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
身份特征 — 禁止更改：
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- 整体脸型和颅骨结构  
- 眼睛形状、间距、深度和眼睑轮廓  
- 鼻梁宽度、鼻尖形状和鼻孔  
- 嘴唇轮廓、丘比特弓形状、丰满比例（上唇与下唇）  
- 下巴线条定义和下巴形状  
- 颧骨位置和面部宽度  
- 额头高度和眉脊  
- 皮肤纹理、底色和种族特征标记  
- 独特的面部特征：痣、雀斑、酒窝、疤痕、不对称性  
- 面部特征间距离（眼距、鼻唇距、唇下巴距）

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
允许更改（非身份元素）：
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- 服装、面料、材质和配饰  
- 环境、场景和背景  
- 光线方向、色温和强度  
- 色彩分级和整体图像色调  
- 摄像机角度、构图和画面布局  
- 身体姿势、手势和站姿  
- 艺术风格或类型（例如：电影感、绘画风、杂志风）— 若有要求  
- 微小的面部表情变化（轻微微笑、平静、沉思）  
  仅限在现有面部结构上的微调 — 不得通过重建面部实现

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
绝对禁止事项：
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
- 不得用平均化、美化或通用面部替换原面部  
- 不得应用改变面部比例的美颜增强  
- 不得使主体显得更年轻、更年长或改变性别  
- 不得更改种族或人种特征  
- 不得过度磨皮导致纹理和独特性消失  
- 不得以光照、风格或类型变化为名修改脸型  
- 不得以任何理由从头重建面部

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
质量目标：
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
输出需达到照片级真实感。皮肤纹理自然。次表面散射准确。  
主体与环境之间的光照需一致。当输出图像与参考图像并列时，主体必须能通过“同一人”识别测试。面部相似性优先于风格化修饰。

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
转换请求：
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[在此描述你的具体更改需求 — 例如：“将主体置于烛光照明的中世纪酒馆中，身穿一件磨损的皮外套。保持光线温暖且氛围感强。照片级真实感。”]
```

</details>

<details><summary><b>锈蚀时代的回响</b></summary>

```text
你将使用所提供照片中的人物作为主要主体，执行图像编辑。需保留他们最核心的相貌特征。将主体 1（男性）和主体 2（女性）置于一片废料沙漠之中，塑造为后末日时代的流浪者形象。他们正穿行于一道巨大的峡谷，该峡谷由数个世纪以来层层堆积、锈迹斑斑的废弃残骸自然形成。图像须具备照片级真实感，采用电影化布光，呈现高度精细的皮肤纹理与环境粗粝质感；拍摄设备设定为 Arri Alexa，景深极浅，以使人物从混乱的背景中清晰分离出来。
```

</details>

<details><summary><b>镜像无限产品图</b></summary>

```text
产品在呈角度排列的镜面中无限反射，万花筒效果，干净利落的几何倍增，影棚灯光营造精准反射，视觉错觉，极繁主义的极简主义，令人迷失方向的优雅感，高概念广告  
产品="${product}"  
宽高比="${aspectratio}"
```

</details>

<details><summary><b>阳光别墅的静谧午后</b></summary>

```text
{
  "image_analysis": {
    "meta": {
      "file_name": "image_ef3de2.jpg",
      "file_type": "uploaded file",
      "analyst_persona": "Technical Photo Analyst"
    },
    "scene_environment": {
      "location_type": "室内 / 半户外过渡空间（阳光房或带顶棚的露台）",
      "atmosphere": "热带风情、奢华、放松、温暖",
      "background_texture": "石墙、自然光、木质家具"
    },
    "camera_technical": {
      "lens_type": "35mm - 50mm（标准镜头）",
      "angle": " eye-level, slightly angled from the right",
      "focus": "主体对焦清晰，前景极浅景深（兰花）",
      "composition": "三分法构图，主体位于左中，右侧花卉形成框景"
    },
    "lighting": {
      "general_condition": "高调照明，以自然日光为主",
      "sources": [
        {
          "id": "light_source_1",
          "type": "Natural Sunlight",
          "direction": "从左侧（观众视角）",
          "color_temp": "中性/冷白光（日光约5500K）",
          "intensity": "高强度",
          "effect_on_objects": "在主体的右腿、手臂和面部形成明显高光，向右侧投射柔和阴影"
        },
        {
          "id": "light_source_2",
          "type": "Ambient Fill",
          "direction": "全向",
          "color_temp": "暖色",
          "intensity": "低/中等强度",
          "effect_on_objects": "柔化木质家具和主体左侧的阴影"
        }
      ]
    },
    "subject": {
      "identity": "成年女性（注意到名人相似性，按指示匿名处理）",
      "orientation": "正面对前，身体略向右倾斜",
      "gaze_direction": "直视镜头",
      "emotional_state": "自信、放松、迷人",
      "sensuality_level": "中等到高（因着装与姿势所致，但保持优雅）",
      "pose": {
        "general_description": "半倚坐在木制沙发/日光床上",
        "posture_effect_on_emotion": "斜倚姿势突显出放松与自信",
        "legs": "双腿交叉；右腿弯曲置于左膝之上",
        "feet_position": "左脚踩在地板/地毯上，右脚悬空，脚尖绷直（跖屈）",
        "hands_position": "右手置于身后白色靠垫上；左手置于大腿/膝盖附近",
        "visible_body_extent": "全身可见（从头到脚）"
      },
      "head": {
        "hair": {
          "color": "深棕色带蜂蜜/焦糖渐变挑染",
          "style": "长发、松散波浪，中分",
          "texture": "丝滑、丰盈",
          "interaction_with_head": "对称地垂落于面部两侧，披在肩上"
        },
        "ears": {
          "visibility": "部分被头发遮盖",
          "shape": "因头发遮挡无法辨识"
        },
        "face": {
          "structure": "椭圆至菱形脸型，高颧骨",
          "forehead": "光滑，标准高度，部分被头发修饰",
          "brows": "精心修饰，拱形，深棕色",
          "eyes": "杏仁形，深色，化有眼线",
          "nose": "笔直，鼻梁分明",
          "upper_lip": "唇峰明显，涂抹紫红色口红",
          "mouth_area": "闭合，略带 smirk/微笑",
          "chin": "下颌分明，略尖",
          "mimic": "微妙的自信微笑，带有诱惑性目光"
        }
      },
      "body_details": {
        "skin_tone": "古铜色 / 橄榄色",
        "neck": "可见，光滑，V领设计突出颈部线条",
        "shoulders": "裸露，圆润，放松",
        "chest": {
          "ratio_to_body": "比例较大（丰满）",
          "estimated_size": "丰满胸部",
          "bra_status": "无可见文胸（泳衣内置支撑）",
          "nipples_visible": "否",
          "shape_description": "自然、挺拔"
        },
        "stomach": {
          "ratio_to_body": "纤细、紧致",
          "ratio_to_chest": "明显小于胸部（沙漏型身材）",
          "ratio_to_hips": "明显小于臀部"
        },
        "hips": {
          "ratio_to_body": "宽大、曲线优美",
          "ratio_to_chest": "与胸部比例协调",
          "shape": "丰腴曲线"
        },
        "legs": {
          "thighs": "大腿丰满，皮肤光滑，受光源高光突出",
          "knees": "膝盖光滑、轮廓分明",
          "calves": "小腿线条紧致",
          "feet": "赤足，足弓明显，美甲精致（浅色指甲油）"
        }
      },
      "attire": {
        "upper_garment": {
          "type": "连体泳衣 / Monokini",
          "color": "深棕色 / 浓咖啡色",
          "details": "前部系带设计配金色孔环，挂脖式",
          "light_interaction": "吸收光线，与皮肤形成对比"
        },
        "lower_garment": {
          "type": "泳装下装（与上装相连）"
  
        "accessory": "花卉图案披肩/纱笼",  
        "details": "垂放在腿下并略微覆盖腿部，多色花卉印花",  
        "light_interaction": "柔和的褶皱形成阴影"  
      },  
      "accessories": {  
        "jewelry": [  
          {  
            "item": "Bracelet",  
            "location": "左手腕",  
            "type": "粗大金链节",  
            "material": "金属金"  
          },  
          {  
            "item": "Necklace",  
            "location": "颈部",  
            "type": "细巧链条",  
            "visibility": "几乎不可见"  
          }  
        ],  
        "footwear": "无（赤脚）"  
      }  
    },  
    "objects_in_scene": [  
      {  
        "object": "木制沙发 / 日间床",  
        "description": "华丽的深色木材，带有复杂雕刻",  
        "purpose": "供主体坐卧",  
        "ratio": "占据中景主导位置",  
        "color": "深红木色",  
        "location": "中景，从左侧延伸至中央"  
      },  
      {  
        "object": "兰花植物",  
        "description": "蝴蝶兰，开有紫色和白色花朵",  
        "purpose": "前景构图元素，增加景深与色彩",  
        "ratio": "因透视关系在前景中显得较大",  
        "color": "亮紫色、白色、绿色茎干",  
        "location": "前景右侧"  
      },  
      {  
        "object": "水果碗",  
        "description": "白色碗内装满柑橘类水果（橙子/柠檬）",  
        "purpose": "装饰，增加色彩对比",  
        "ratio": "相对于主体较小",  
        "color": "亮橙色、黄色",  
        "location": "前景右下角"  
      },  
      {  
        "object": "台灯",  
        "description": "白色几何形/蜂窝纹理底座，配白色灯罩",  
        "purpose": "背景装饰",  
        "ratio": "中等大小",  
        "color": "白色",  
        "location": "背景左侧"  
      },  
      {  
        "object": "书籍/杂志",  
        "description": "咖啡桌书籍，封面有人物面部",  
        "purpose": "前景细节",  
        "ratio": "仅可见一小部分",  
        "location": "极前景底部中央"  
      }  
    ],  
    "negative_prompts": [  
      "bad anatomy",  
      "extra fingers",  
      "missing limbs",  
      "distorted face",  
      "low resolution",  
      "blurry subject",  
      "overexposed",  
      "underexposed",  
      "watermark",  
      "text overlay (except book title)",  
      "cartoon",  
      "illustration",  
      "CGI",  
      "unnatural skin tone"  
    ]  
  }  
}
```

</details>

<details><summary><b>阳光卧室镜前自拍</b></summary>

```text
{  
  "scene_type": "室内生活人像（镜中自拍美学）",  
  "environment": {  
    "location": "阳光洒落的卧室，拥有柔和、自然的日间照明",  
    "background": {  
      "bed": "白色金属框架床，呈现柔和复古质感，铺有浅色植物图案床品",  
      "decor": "简洁极简风格陈设，配以几株小型盆栽、一张简约床头柜，以及低调的花卉元素点缀",  
      "windows": "大型窗户配有轻盈透光的薄纱窗帘，柔化并漫射光线，使整个房间氛围更显柔和",  
      "color_palette": "暖白色、象牙白、米 beige 及浅中性色调为主，辅以淡雅的植物与花卉细节"  
    },  
    "atmosphere": "静谧、私密、温馨、通透且略带生活气息"  
  },  
  "subject": {  
    "gender_presentation": "女性化",  
    "approximate_age_group": "成年（21 岁及以上），青年期",  
    "skin_tone": "白皙肤色，具备真实自然的皮肤纹理与细微瑕疵",  
    "hair": {  
      "color": "冷调铂金色（略带冰感）",  
      "style": "长直发，中分清爽利落，自然垂落于肩部"  
    },  
    "facial_features": {  
      "expression": "神情柔和、平静且略带内省，嘴角放松，眼神温软",  
      "makeup": "妆容极淡、自然，仅作低调轮廓修饰，无任何浓重或戏剧化效果"  
    },  
    "body_details": {  
      "build": "偏纤细至匀称体型，比例自然",  
      "visible_tattoos": [  
        "手臂及前臂处饰有精细线条风格的花卉与插画风纹身",  
        "大腿上部可见一处小巧、低调的纹身"  
      ]  
    }  
  },  
  "pose": {  
    "position": "舒适随意地坐在床沿附近",  
    "legs": "双膝微屈收拢，形成紧凑而温馨的剪影",  
    "hands": "一只手将手机举向镜面以构图自拍，另一只手轻触嘴唇或停驻嘴边，呈现沉思姿态",  
    "orientation": "身体朝向镜面倾斜，面部部分被手机遮挡，保持真实镜中自拍的取景方式"  
  },  
  "clothing": {  
    "outfit_type": "轻盈睡衣或柔软家居吊带裙，契合轻松卧室场景",  
    "color": "柔白色或象牙白（洁净、极简、温和色调）",  
    "material": "柔软细腻面料，略具半透明感，同时保持得体优雅、不露骨",  
    "details": "细肩带设计，边缘饰有精致蕾丝镶边与考究收边细节"  
  },  
  "styling": {  
    "accessories": [  
      "极简项链，配小巧吊坠或素链",  
      "小巧圆环耳饰，外观干净、低调"  
    ],  
    "nails": "自然甲面或以中性色轻度美甲，不张扬",  
    "overall_style": "柔和、女性化、私密且静谧审美，毫无过度造型或人工感"  
  },  
  "lighting": {  
    "type": "自然日光",  
    "source": "侧方斜射入窗的光线，轻柔包裹主体",  
    "quality": "漫射、柔和且均匀的照明，肌肤与织物表面光影过渡平滑",  
    "shadows": "阴影极淡，仅增添自然立体感而不产生强烈对比，整体情绪温柔而轻盈"  
  },  
  "mood": {  
    "emotional_tone": "宁静、温暖、沉思、静谧私密",  
    "visual_feel": "平和、柔润、写实，宛如一个宁静清晨中捕捉到的真实瞬间"  
  },  
  "camera_details": {  
    "camera_type": "智能手机拍摄",  
    "lens_equivalent": "广角感（约等效 24–28mm），典型手机自拍镜头视角",  
    "perspective": "镜中自拍视角，构图真实可信，略带手持拍摄的真实性",  
    "focus": "主体清晰锐利，具备自然景深提示；背景可辨识但不过分锐利",  
    "aperture_simulation": "模拟手机浅景深效果（f/1.8 至 f/2.2 风格观感），微妙且可信",  
    "iso_simulation": "低 ISO 模拟，确保画面干净、噪点极少，同时保留肌肤真实纹理",  
    "shutter_speed_simulation": "快门速度足够高，以抑制运动模糊，即使手持拍摄亦能保持细节锐利",  
    "white_balance": "中性日光白平衡，略带温和暖调，避免过黄或过蓝倾向"  
  },  
  "rendering_style": {  
    "realism_level": "超写实主义",  
    "detail_level": "高保真皮肤纹理、真实布料垂坠与蕾丝动态表现、自然光影渐变及符合现实的阴影",  
    "post_processing": "柔和对比度、温润高光、自然色彩分级、适度清晰度——在保留皮肤纹理的同时不进行磨皮处理",  
    "artifacts": "无任何视觉伪影、无绘画感效果、无 CGI 外观、无合成塑料质感肌肤"  
  }  
}
```

</details>

<details><summary><b>阳光沙滩</b></summary>

```text
生成一幅人们在阳光明媚的海滩上日光浴的图像。呈现一种轻松愉快的氛围，背景是清澈的蓝天和轻柔的海浪。画面中应包含不同背景的人们享受阳光的情景，并散落着沙滩毛巾和遮阳伞。
```

</details>

<details><summary><b>阳光露台自拍与提基装饰</b></summary>

```text
{
  "scene_analysis": {
    "environment": {
      "type": "Outdoor",
      "setting": "Patio or backyard terrace",
      "weather": "Sunny, clear sky visible",
      "background_elements": [
        "Grey stucco wall",
        "Artificial green hedge wall",
        "Blue sky"
      ]
    },
    "camera": {
      "lens": "Wide-angle lens (typical of smartphone front camera)",
      "angle": "Selfie angle, slightly low looking up, close-up framing",
      "focus": "Sharp focus on the subject's face and upper body",
      "distortion": "Slight perspective distortion due to wide angle"
    },
    "lighting": {
      "overall_condition": "Bright natural daylight, hard lighting",
      "sources": [
        {
          "source_id": 1,
          "type": "Sun",
          "angle": "High angle, coming from the upper left (subject's right)",
          "color": "Natural white/warm daylight",
          "intensity": "High/Strong",
          "effects_on_objects": "Creates hard shadows under the subject's hair, chin, and nose. Casts defined shadows on the grey wall behind. Illuminates the hair creating a golden sheen."
        }
      ]
    }
  },
  "subjects": [
    {
      "id": "person_1",
      "type": "Human",
      "gender": "Female",
      "identity": "Anonymous",
      "orientation": {
        "facing": "Directly towards the camera",
        "body_rotation": "Frontal, slight lean forward"
      },
      "emotional_state": {
        "mood": "Relaxed, confident, slightly sultry",
        "expression": "Neutral with slightly parted lips, 'bedroom eyes'",
        "lust_factor": "Moderate to High (suggestive pose and nudity implication)",
        "posture_effect": "The leaning posture emphasizes the chest and creates a casual, intimate vibe"
      },
      "pose": {
        "general_definition": "Leaning forward selfie, likely sitting or kneeling",
        "feet_position": "Not visible (out of frame)",
        "hand_position": "Right arm extended holding the camera (implied), Left arm resting on a lower surface/knee",
        "visible_extent": "Head to waist/mid-torso"
      },
      "head": {
        "structure": "Oval face shape, defined jawline",
        "hair": {
          "color": "Light brown with blonde highlights (bronde)",
          "style": "Shoulder-length, layered, textured/messy look",
          "shape": "Frames the face, voluminous",
          "condition": "Sun-kissed, dry texture"
        },
        "ears": "Partially covered by hair",
        "forehead": "Partially covered by bangs/hair strands, smooth skin",
        "brows": "Natural, brushed up, dark brown",
        "eyes": {
          "gaze": "Direct eye contact with the lens",
          "shape": "Almond",
          "makeup": "Minimal or natural look"
        },
        "nose": {
          "structure": "Straight, slightly button tip",
          "details": "Freckles visible across the bridge"
        },
        "mouth_area": {
          "lips": "Very full, plump, upper lip slightly lifted",
          "mouth_state": "Slightly open",
          "philtrum": "Defined"
        },
        "chin": "Rounded but defined",
        "mimics": "Relaxed facial muscles, seductive gaze"
      },
      "body": {
        "skin": {
          "tone": "Tanned",
          "texture": "Smooth, freckles on chest and face"
        },
        "neck": {
          "visibility": "Visible",
          "tattoo": "Small text tattoo on the center/throat area (vertical characters)"
        },
        "shoulders": {
          "visibility": "Visible",
          "posture": "Relaxed, slightly hunched forward due to leaning"
        },
        "chest": {
          "ratio_to_body": "Prominent",
          "estimated_size": "Full bust",
          "bra_status": "None (No bra visible)",
          "nipples_visible": "No (Hidden by framing/shadows)",
          "shape_notes": "Natural droop due to gravity and leaning pose, cleavage visible",
          "tattoo": "Gothic script text tattoo reading 'Divine Feminine' on the sternum"
        },
        "belly": {
          "visibility": "Partially visible (upper abdomen)",
          "ratio": "Slim relative to chest"
        },
        "arms": {
          "tattoos": {
            "right_arm": "Heavy ink, large sleeve/designs visible",
            "left_arm": "Sketch-style tattoos including an anime-style girl face, a hummingbird, and line art"
          }
        }
      },
      "clothing": {
        "upper_body": "None (Topless implied)",
        "lower_body": "Not clearly visible, possibly a white towel or garment bunched near the bottom left",
        "accessories": "Bracelet on left wrist (silver/thin chain)"
      },
      "light_interaction_body": {
        "face": "Evenly lit with highlights on the forehead and nose bridge",
        "chest": "Highlights on the upper curve of the breasts, deep shadows in the cleavage",
        "hair": "Backlighting effect on the top strands"
      }
    }
  ],
  "objects": [
    {
      "id": "object_1",
    {
      "id": "object_1",
      "name": "Tiki Totem Statue",
      "description": "木雕雕像，带有面部特征",
      "color": "灰色/棕色木材，涂有红色舌头和黄色牙齿",
      "position": "画面右侧，前景",
      "purpose": "装饰，美学元素",
      "ratio": "大型垂直元素，在透视中与主体头部大小相当"
    },
    {
      "id": "object_2",
      "name": "Planter with Greenery",
      "description": "质朴的木质花箱，内含人造蕨类植物/绿植",
      "color": "漂白木材，鼠尾草绿植物",
      "position": "右侧，位于Tiki雕像后方",
      "purpose": "装饰，背景纹理"
    },
    {
      "id": "object_3",
      "name": "BBQ Grill",
      "description": "不锈钢户外烧烤架",
      "color": "金属银色",
      "position": "最左侧边缘，部分被裁剪",
      "purpose": "功能性露台设备"
    }
  ],
  "negative_prompts": [
    "上身穿着衣物",
    "衬衫",
    "文胸",
    "比基尼上衣",
    "变形的手",
    "解剖结构错误",
    "模糊",
    "低分辨率",
    "昏暗照明",
    "室内场景",
    "男性主体",
    "太阳镜"
  ]
}
```

</details>

<details><summary><b>阳台晨雾咖啡时光</b></summary>

```text
{
  "category": "BALCONY_COFFEE_PLANTS",
  "identity_lock": {
    "enabled": true,
    "priority": "ABSOLUTE_MAX",
    "instruction": "严格保留参考图中的精确身份。仅限21岁及以上成年人。禁止美化或更改面部。"
  },
  "subject": {
    "demographics": "成年女性，21–29岁（须匹配参考身份）。",
    "hair": {
      "color": "与参考图一致。",
      "style": "松散波浪发或凌乱发髻，带几缕散落发丝",
      "texture": "真实发丝质感，有飞毛，体积感自然真实",
      "movement": "自然动态，微风轻拂发丝"
    },
    "face": {
      "eyes": "眼睛须与参考图完全一致；带有柔和的晨光高光（catchlights）",
      "skin_details": "肌肤呈现自然纹理，毛孔可见，散发柔和晨间光泽",
      "micro_details": "保留参考图中的所有细微特征标记"
    },
    "clothing": {
      "outfit": "舒适开衫 + 简约上衣（无任何标识/文字）",
      "fabric": "可见针织纹理，允许轻微起球"
    },
    "accessories": {
      "jewelry": ["小巧银色圆环耳环"],
      "props": ["无品牌陶瓷马克杯"]
    }
  },
  "pose": {
    "type": "生活化抓拍风格",
    "orientation": "半身构图，坐于阳台椅上",
    "head_position": "头部略倾斜，下巴放松",
    "hands": "双手环握马克杯以取暖（手部结构准确）",
    "gaze": "接近直视镜头的眼神",
    "expression": "浅淡微笑，神情放松"
  },
  "setting": {
    "environment": "布满盆栽植物的阳台",
    "background_elements": [
      "前景虚化的植物叶片",
      "柔和的城市远景虚化（不可见可读文字或标识）",
      "晨雾弥漫，氛围轻柔"
    ],
    "depth": "前景叶片虚化；面部清晰锐利；背景柔和"
  },
  "camera": {
    "shot_type": "半身人像",
    "angle": "略高于眼平线角度",
    "focal_length_equivalent": "26mm 手机镜头 或 50mm 专业镜头",
    "framing": "4:5画幅，偏构图",
    "focus": "双眼清晰锐利；马克杯略柔和"
  },
  "lighting": {
    "source": "柔和的晨间日光",
    "direction": "前侧向漫射光",
    "highlights": "眼部与唇部呈现自然高光",
    "shadows": "下颌下方投下柔和阴影"
  },
  "mood_and_expression": {
    "tone": "温馨、亲切、宁静",
    "atmosphere": "可感知的晨间静谧感"
  },
  "style_and_realism": {
    "style": "照片级写实风格，Instagram生活类影像",
    "imperfections": "轻微颗粒感，构图略带不完美感"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "resolution": "高分辨率",
    "noise": "轻微噪点",
    "mode_variants": {
      "amateur": "手持iPhone抓拍风格：带轻微倾斜角度、轻微噪点、构图略不完美",
      "pro": "曝光更干净、微对比度更锐利、景深更浅"
    }
  },
  "constraints": {
    "adult_only": true,
    "single_subject_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "身份偏移", "面部形变",
    "CGI生成的植物", "塑料质感皮肤",
    "多余手指", "扭曲变形的马克杯",
    "可读文字", "标识/Logo", "水印"
  ]
}
```

</details>

<details><summary><b>阿尔卑斯自由滑落</b></summary>

```text
{
  "title": "Alpine Freefall",
  "description": "一张高节奏、广角的动作镜头，捕捉一名自由式滑雪者在陡峭山峰上疾驰而下的惊险瞬间。",
  "prompt": "你将使用所提供照片中的人物作为主要主体进行图像编辑。保留她的核心相貌特征。创建一张超现实的 GoPro 自拍风格图像，展现主体1在高海拔滑雪坡上高速滑降的场景。图像应具有标志性的鱼眼畸变效果，呈现地平线的弯曲形态以及滑降时的强烈速度感，主体手持自拍杆将自己框入画面，背景是急剧下落的垂直落差。",
  "details": {
    "year": "2024",
    "genre": "GoPro",
    "location": "法国阿尔卑斯山脉一处锯齿状、白雪覆盖的山脊，头顶是清澈的蓝天。",
    "lighting": [
      "明亮、强烈的阳光",
      "镜头光晕伪影",
      "高对比度"
    ],
    "camera_angle": "自拍杆视角，带有广角鱼眼畸变。",
    "emotion": [
      "兴奋",
      "无畏",
      "狂野"
    ],
    "color_palette": [
      "刺眼的白色",
      "深邃的天蓝色",
      "鲜明的黑色",
      "肤色"
    ],
    "atmosphere": [
      "充满肾上腺素",
      "节奏飞快",
      "清冽",
      "多风"
    ],
    "environmental_elements": "被踢起的粉状雪花向镜头喷洒，边缘带有运动模糊，摄像机镜片上有水滴。",
    "subject1": {
      "costume": "黑色迷你裙、白色短款上衣、皮质露指手套",
      "subject_expression": "张大嘴巴兴奋呐喊，眼神因刺激而睁大。",
      "subject_action": "ski"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "影棚灯光",
        "平静",
        "静态姿势",
        "室内场景",
        "树木"
      ],
      "exclude_styles": [
        "油画",
        "素描",
        "温暖复古风格",
        "柔焦"
      ],
      "exclude_colors": [
        "棕褐色",
        "低饱和色调",
        "粉彩"
      ],
      "exclude_objects": [
        "滑雪缆车",
        "人群",
        "建筑物"
      ]
    }
  }
}
```

</details>

<details><summary><b>阿蒙太阳女祭司</b></summary>

```text
{
  "title": "The Solar Priestess of Amun",
  "description": "一位令人惊叹的、风格化的女性肖像，描绘她化身为古埃及女祭司，融合了照片级真实感与墓室壁画的质感。",
  "prompt": "你将使用所提供照片中的女性作为主要主体进行图像编辑。保留她的核心相貌特征。将主体转变为新王国艺术风格下的高级古埃及女祭司。她以程式化的侧面视角（正统透视）呈现，背景为覆盖着鲜艳象形文字的石灰岩墙壁。图像应具有陈旧纸莎草和金箔的纹理，同时保持电影级光照效果，画面比例为1:1。",
  "details": {
    "year": "1250 BC",
    "genre": "Ancient Egyptian Art",
    "location": "卡纳克神庙内殿，周围环绕着巨大的砂岩柱。",
    "lighting": [
      "温暖的金色阳光",
      "摇曳的火把阴影",
      "黄金首饰上的镜面高光"
    ],
    "camera_angle": "与视线齐平的侧面拍摄角度，模仿传统埃及艺术的透视方式。",
    "emotion": [
      "庄严",
      "虔诚",
      "宁静"
    ],
    "color_palette": [
      "青金石蓝",
      "抛光金",
      "赭红",
      "绿松石"
    ],
    "atmosphere": [
      "神圣",
      "永恒",
      "神秘",
      "奢华"
    ],
    "environmental_elements": "背景墙上雕刻的象形文字，光线光束中漂浮的尘埃微粒，神圣的莲花。",
    "subject1": {
      "costume": "一件褶皱白色亚麻长裙（kalasiris），一条镶嵌半宝石的厚重金质Wesekh项圈，以及一只秃鹫头饰。",
      "subject_expression": "坚定而威严的目光直视前方。",
      "subject_action": "一只手微微举起仪式用的安卡符号。"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "现代时装",
        "牛仔布",
        "数字技术",
        "汽车"
      ],
      "exclude_styles": [
        "3D渲染",
        "动漫",
        "印象派",
        "赛博朋克"
      ],
      "exclude_colors": [
        "霓虹绿",
        "电光紫"
      ],
      "exclude_objects": [
        "眼镜",
        "手表",
        "现代建筑"
      ]
    }
  }
}
```

</details>

<details><summary><b>随性闺蜜夜自拍</b></summary>

```text
业余风格的女孩之夜自拍，极度随意且不完美，1:1 画幅比。图像直接由一部廉价、老旧智能手机的前置摄像头拍摄：我们仅看到手机所见的画面，画面中**绝不可出现任何手机或相机本体**。

三位成年女性在夜晚的小公寓客厅里，紧挨着坐在一张老旧但舒适的沙发上。她们穿着简单的居家服装和运动裤，就像一个真正放松惬意的夜晚。

居中女性：中等肤色，长黑发，身穿纯黑色无袖上衣和浅灰色运动裤。她坐在沙发正中央，一条腿 tucked 在身下，另一条腿弯曲；身体微微向左倾斜，头部略歪，朝向镜头轻柔微笑，神情放松、毫无摆拍感。

左侧女性：浅肤色，直顺浅棕色头发，身穿长袖黑色上衣和浅灰色运动裤。她身体大幅前倾，紧贴居中女性，几乎肩部相触，朝向镜头做出夸张的“飞吻脸”表情——双唇噘起，眉毛微抬。由于这是自拍视角（POV），她在画面中显得稍近、略大，符合靠近手机的真实透视效果。

右侧女性：浅肤色，波浪金发，身穿深色长袖上衣和黑色紧身裤。她从右侧探身加入合影，头部微歪，笑容俏皮搞怪，舌头伸出，双眼因大笑而微微眯起。三人神态自然，宛如亲密好友正在玩闹，绝非模特。

环境：温馨、略显凌乱的客厅。她们身后是一盏简易落地灯，暖色灯泡照亮墙面。背景一侧可见一台电视屏幕，正暂停播放某部电影画面（呈现柔和抽象图形，无清晰可辨的人脸或商标）。沙发前方一张低矮木质咖啡桌上（画面底部可见）摆放着打开的披萨盒（内有吃剩的披萨片）、一袋薯片、一听汽水、一听气泡水、几粒碎屑，以及一部平放在桌上的手机。沿其中一面墙悬挂着串灯或仙女灯，散发温暖而不完美的光晕。整间公寓与家具均呈现日常真实感，略带使用痕迹，绝非影棚布景。

相机与风格：**极其重要**——该图像必须呈现为一张真实的、质量较差的自拍，**绝非专业摄影**。它由基础款智能手机前置摄像头在 AUTO（自动）模式下拍摄。闪光灯为镜头附近的直射、略显生硬的手机闪光，导致面部局部轻微过曝并泛油光。暗部区域可见明显数字噪点与颗粒感。混合光源：落地灯带来暖黄光，电视屏幕则投射出偏冷的蓝调反光，造成白平衡轻微不均。对焦偏软，非锐利清晰，发丝与手部带有细微动态模糊。画面边缘存在轻微暗角及轻微广角畸变，符合廉价前置摄像头特性。构图略歪斜、稍偏离中心；部分披萨盒与物品被裁切于画面边缘。整体观感应如一张未经编辑、即兴抓拍、随手发至群聊的自拍照。

约束条件：画面中**严格仅有三位女性，不得出现其他任何人**。唯一存在的相机即为我们正透过其观看的那部手机，因此**不可出现额外的手部、额外的手机、镜中反射的摄影师、画面边缘的第二位摄影师，亦不可出现任何其他相机的反射影像**。画面中仅有三位朋友坐在沙发上，以及凌乱的咖啡桌。

负面提示词（Negative prompt）：专业影棚、专业布光、柔光箱、轮廓光、电影感氛围、商业摄影棚拍摄、完美色彩分级、HDR、强景深虚化、散景（bokeh）、高端 DSLR 或镜头、超洁净时尚大片、对称构图、网红滤镜预设、重度磨皮美颜、滤镜、酒店房间、摆拍布景、额外人物、额外手臂、额外手部、画面中出现任何其他手机或相机、镜中映出另一位摄影师、文字、商标、水印、超现实故障效果、未成年人外观。
```

</details>

<details><summary><b>隔窗特写:一只眼睛对焦</b></summary>

```text
一幅电影感十足的特写人像，呈现一张参考照片透过反光玻璃窗所见的效果。她拥有一头凌乱的深棕色头发，皮肤质感高度逼真，清晰可见毛孔、细纹及自然瑕疵。其中一只绿色带淡褐色的虹膜处于锐利、晶莹剔透的焦点之中，完全可见，且未被任何反光或高光遮挡；而她面部其余部分则随景深自然衰减，逐渐柔化融入背景。

前景中的玻璃表面覆盖着真实感十足的雨滴与细微的雨水流痕，营造出层次丰富的纵深感与情感距离感。反光经过精心控制，仅出现在画面边缘区域，绝不会跨越或遮蔽那只聚焦的眼睛或关键面部特征。

阴郁、低调的布光风格，暖调泛黄与橙色散景光斑柔和地映在玻璃上。散景保持弥散状态，并偏移至画面两侧，强化氛围感，同时不遮挡面部清晰度。采用极浅景深（f/1.2）拍摄，构图富有电影感，情绪基调浓郁，光学虚化自然，光线行为真实可信。

照片级真实感渲染，高分辨率细节，保留胶片颗粒感，皮肤纹理自然，无过度平滑处理，无人工锐化，无塑料感或合成感。
```

</details>

<details><summary><b>雨中浪漫电影场景</b></summary>

```text
面部必须与参考图100%完全一致，绝对锁定身份：不允许任何面部改变、美化、对称性修正、年龄变化、皮肤平滑处理或表情改动，保持相同的面部比例、眼睛、鼻子、嘴唇、下颌线以及自然的皮肤质感。超写实电影级夜景雨中场景，一对情侣在柔和灯光的花园中站在黄色雨伞下，彼此靠得非常近。大雨倾盆而下，金色的暖光小串灯和街灯照亮雨滴，在背景中形成梦幻般的散焦光斑（bokeh），湿漉漉的地面反射着灯光。男子手持雨伞，温柔深情地凝视着女子，而女子则抬头回望他，脸上带着柔和温暖的浪漫微笑。他们始终保持着眼神交流，完全沉浸在彼此之中，传达出深刻的情感联结。两人穿着优雅的外套，被雨水微微打湿，布料纹理真实可见；面部有微妙的轮廓光勾勒，可见的雨滴和薄雾弥漫，浅景深效果，呈现50mm镜头视觉感，带有自然的胶片颗粒感，高端电影级调色。只允许改变灯光、氛围和环境——面部和身份必须完全不变且完美保留。
```

</details>

<details><summary><b>雨中浪漫视频</b></summary>

```text
他们站在雨中，彼此深情对望。雨滴在他们周围落下，轻柔的雨声弥漫在空气中。
```

</details>

<details><summary><b>雨中的绯红华尔兹</b></summary>

```text
{
  "title": "Crimson Waltz in the Rain",
  "description": "一个视觉惊艳、电影感十足的瞬间：一位女性在黄昏时分的欧洲雨巷中独舞，享受孤独中的喜悦。",
  "prompt": "你将执行一次图像编辑，创作一幅超逼真的杰作。该图像必须具备照片级真实感，采用电影化照明，并高度细致，看起来仿佛是用 Arri Alexa 拍摄，具有浅景深效果。画面中，一位女性主体在雨中的鹅卵石街道上自由起舞。雨滴因快门速度而凝固在空中，捕捉到街灯的琥珀色光芒。",
  "details": {
    "year": "永恒现代",
    "genre": "电影级写实主义",
    "location": "黄昏时分巴黎一条狭窄空旷的鹅卵石街道，雨水浸湿地面，倒映着复古街灯和商店橱窗的温暖光芒。",
    "lighting": [
      "电影级轮廓光",
      "温暖的琥珀色路灯",
      "柔和的蓝色环境暮光",
      "体积雾"
    ],
    "camera_angle": "人眼高度的中景镜头，突出主体在散焦背景前的舞动。",
    "emotion": [
      "自由的",
      "喜悦的",
      "宁静的"
    ],
    "color_palette": [
      "深黑色曜石",
      "琥珀金色",
      "雨蓝色",
      "鲜艳的深红色"
    ],
    "atmosphere": [
      "浪漫的",
      "忧郁却喜悦的",
      "富有氛围感的",
      "潮湿的"
    ],
    "environmental_elements": "雨丝斜落，地面积水中倒映着灯光，雾气在脚踝周围缭绕。",
    "subject1": {
      "costume": "红色帽子",
      "subject_expression": "双眼闭合，沉浸在纯粹的幸福中，嘴角带着温柔微笑，脸颊上挂着雨滴。",
      "subject_action": "跳舞"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "明亮的日光",
        "干燥的路面",
        "人群",
        "车辆",
        "太阳镜"
      ],
      "exclude_styles": [
        "卡通",
        "3D 渲染",
        "插画",
        "油画",
        "素描"
      ],
      "exclude_colors": [
        "霓虹绿",
        "亮粉"
      ],
      "exclude_objects": [
        "雨伞",
        "现代汽车",
        "垃圾桶"
      ]
    }
  }
}
```

</details>

<details><summary><b>雨天街头撑伞全身照</b></summary>

```text
{
  "category": "RAINY_CITY_UMBRELLA_FULLBODY",
  "subject": {
    "demographics": "成年女性，21–27 岁，具有土耳其人外貌特征。",
    "hair": {
      "color": "深棕色",
      "style": "略带潮湿的发丝，别于耳后",
      "texture": "呈现真实湿润光泽，不油腻",
      "movement": "几缕发丝轻轻贴在脸颊上"
    },
    "face": {
      "eyes": "目光明亮直视镜头，瞳孔中带有反射高光",
      "skin_details": "肌肤呈现自然纹理，略带水润真实感",
      "makeup": "妆容极简，具备防水效果"
    },
    "clothing": {
      "outerwear": "雨衣或风衣（无任何品牌标识）",
      "fabric": "面料呈现轻微湿润光泽，并可见水珠"
    },
    "accessories": {
      "umbrella": "透明雨伞，表面附着雨滴",
      "jewelry": ["小巧银质圆环耳饰"]
    }
  },
  "pose": {
    "type": "全身行走抓拍照",
    "orientation": "迈步中段，身体略朝向镜头扭转",
    "hands": "一只手握持伞柄，另一只手插在大衣口袋中",
    "gaze": "柔和微笑，与镜头保持眼神交流",
    "posture": "姿态放松，步态自然"
  },
  "setting": {
    "environment": "黄昏时分的雨天城市街道",
    "background_elements": [
      "湿滑路面的倒影",
      "路灯虚化光斑（bokeh）",
      "可见细密毛毛雨（精细雨滴，非烟雾/雾气效果）"
    ],
    "depth": "主体清晰，背景虚化"
  },
  "camera": {
    "shot_type": "全身街头摄影",
    "angle": "平视角度",
    "focal_length_equivalent": "26mm 手机镜头或 35mm 杂志级镜头",
    "framing": "4:5 构图，主体略微偏离画面中心",
    "focus": "面部锐利清晰，运动模糊程度极低"
  },
  "lighting": {
    "source": "路灯 + 环境天光",
    "direction": "柔和的顶部/侧向辉光",
    "highlights": "雨伞表面雨滴产生的镜面高光",
    "shadows": "阴影柔和、真实"
  },
  "mood_and_expression": {
    "tone": "情绪化、温馨、时尚",
    "expression": "轻柔微笑，沉着自信",
    "atmosphere": "电影级雨天写实氛围"
  },
  "style_and_realism": {
    "style": "照片级写实街头抓拍风格",
    "imperfections": "轻微噪点，仅背景存在轻微模糊"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "弱光环境下类似手机的颗粒感",
    "motion_blur": "仅背景倒影中存在轻微运动模糊"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "烟雾", "造雾机效果", "水枪喷溅",
    "多余肢体", "扭曲变形的伞骨",
    "可辨识文字标识", "品牌标识（logos）", "水印"
  ]
}
```

</details>

<details><summary><b>雨季校园六格拼贴</b></summary>

```text
{
  "aspect_ratio": "9:16",
  "format": "vertical collage moodboard",
  "identity_lock": {
    "rule": "使用附加图像中的所有基因特征——100% 身份保留",
    "source": "attached_image",
    "features_to_use_from_reference": ["面部结构", "肤色", "眼睛颜色", "发色、发质、长度和发型", "体型", "年龄", "种族"],
    "instruction": "不要发明、描述或更改面部、体型或头发。在全部6张照片中，必须使用附加参考图像中的确切基因特征来呈现人物。在整个拼贴画中保持身份一致。"
  },
  "positive_prompt": "创建一个超现实的 Pinterest 风格雨季拼贴画，采用垂直 9:16 格式。拼贴画包含6张不同的自然抓拍照，以优雅的情绪板布局排列。",
  "outfit": {
    "top": "oversized pastel pink button-up shirt",
    "bottom": "loose-flowing white wide-leg pants",
    "note": "所有6张照片中穿着相同服装，具有自然的布料褶皱和真实垂坠感"
  },
  "collage_photos": [
    {
      "photo_1": "安静站立，享受着雨水"
    },
    {
      "photo_2": "撑着透明雨伞，沿着开满花的小径走远"
    },
    {
      "photo_3": "在盛开的粉色花朵旁的特写镜头"
    },
    {
      "photo_4": "将一只手伸入落下的雨中"
    },
    {
      "photo_5": "坐在被花朵环绕的长椅上，姿态放松"
    },
    {
      "photo_6": "站在透明雨伞下，背景是反光的湿漉漉校园道路"
    }
  ],
  "environment": "迷人的大学校园，拥有古老的欧洲风格建筑、鲜花覆盖的小路、潮湿的石板步道、茂盛的绿植、湿滑路面反射灯光与花朵、粉色花瓣散落在地面、细柔降雨、梦幻氛围、温暖大地色调与凉爽雨天色彩交融、浪漫情绪",
  "decorations": "包含手写风格的美学涂鸦、小爱心、花朵、雨滴插图、纸条贴纸、剪贴簿元素以及 Pinterest 情绪板装饰",
  "captions_in_collage": ["Rainy Season", "College Days", "Collecting Moments, Not Things", "Just Breathe", "Some People Feel Like Rain"],
  "lighting_and_quality": "柔和电影级灯光、奶油般虚化背景、逼真的雨滴效果、自然布料褶皱、梦幻韩系美学、生活方式摄影、杂志编辑品质、超精细8K细节",
  "style_tags": "Korean Pinterest Moodboard, Rainy Season Aesthetic, College Campus Photography, Scrapbook Collage, Photorealistic 8K",
  "negative_prompt": "cartoon, anime, CGI, distorted hands, extra fingers, low resolution, oversaturated colors, watermark, logo, AI artifacts, unrealistic anatomy, duplicate faces, different outfits, identity change"
}
```

</details>

<details><summary><b>雨林中的温馨木屋</b></summary>

```text
创建一幅图像：一间舒适的木屋 nestled 在下着大雨的迷雾森林中。温暖的橙色炉火透过结霜的窗户柔和地透出光芒。深色的松树环绕着整个场景。雨水沿着玻璃窗蜿蜒流下。远处微弱的闪电短暂照亮了湿漉漉的树木。镜头缓缓推向木屋的窗户。专业级色彩分级。24fps。高度细致。高品质。
```

</details>

<details><summary><b>雪原孤影数字绘画</b></summary>

```text
{
  "colors": {
    "color_temperature": "cool",
    "contrast_level": "high",
    "dominant_palette": [
      "deep blue",
      "orange",
      "red",
      "black"
    ]
  },
  "composition": {
    "camera_angle": "wide shot",
    "depth_of_field": "deep",
    "focus": "The burning house and the lone figure in the snow.",
    "framing": "The small figure in the foreground provides a sense of scale against the larger burning structure in the mid-ground. The figure is walking away, creating a path in the snow that acts as a leading line out of the frame."
  },
  "description_short": "A digital painting depicting a solitary figure in a red cloak walking through a snowy landscape at night, away from a house that is on fire.",
  "environment": {
    "location_type": "outdoor",
    "setting_details": "A winter scene with a two-story house surrounded by evergreen trees, all set within a vast landscape covered in a thick layer of snow under a dark, starry sky.",
    "time_of_day": "night",
    "weather": "clear"
  },
  "lighting": {
    "intensity": "strong",
    "source_direction": "back",
    "type": "cinematic"
  },
  "mood": {
    "atmosphere": "A somber and dramatic departure",
    "emotional_tone": "mysterious"
  },
  "narrative_elements": {
    "character_interactions": "A single figure is shown in relation to an event rather than another person, suggesting solitude and a significant personal moment.",
    "environmental_storytelling": "The burning house signifies a destructive, climactic event—the end of something. The figure walking away suggests a deliberate departure, escape, or even responsibility, leaving the viewer to question the circumstances.",
    "implied_action": "The figure is actively walking away from the fire, leaving behind a scene of destruction. The fire is still raging, implying the event has just happened."
  },
  "objects": [
    "burning house",
    "snow",
    "figure",
    "red cloak",
    "smoke",
    "trees",
    "torch"
  ],
  "people": {
    "ages": [
      "unknown"
    ],
    "clothing_style": "long red cloak",
    "count": "1",
    "genders": [
      "unknown"
    ]
  },
  "prompt": "A dramatic digital painting of a lone figure in a vibrant red cloak walking through a deep blue, snow-covered landscape at night. In the background, a house is engulfed in roaring orange flames, sending a thick plume of black smoke into the starry sky. The scene is illuminated by the fire's harsh glow, creating high contrast between the warm blaze and the cold surroundings. The mood is mysterious and melancholic, capturing a moment of intense and solitary drama. Painterly, cinematic style.",
  "style": {
    "art_style": "painterly",
    "influences": [
      "concept art",
      "cinematic illustration"
    ],
    "medium": "digital art"
  },
  "technical_tags": [
    "digital painting",
    "high contrast",
    "night scene",
    "fire",
    "snow",
    "narrative",
    "complementary colors",
    "wide shot"
  ],
  "use_case": "Narrative illustration for storytelling, concept art for film or games, or a dataset for generating images with strong emotional and color contrast.",
  "uuid": "922278fe-8572-4713-8d67-75c2ef540f47"
}
```

</details>

<details><summary><b>雪天街头冬季穿搭</b></summary>

```text
{
  "category": "SNOWY_STREET_WINTER_CANDID",
  "identity_lock": {
    "enabled": true,
    "priority": "ABSOLUTE_MAX",
    "instruction": "将身份严格锁定至参考图像。仅限21岁及以上成年人。"
  },
  "subject": {
    "demographics": "成年女性，21–29岁，身份须与参考图像完全一致。",
    "hair": {
      "color": "与参考图像一致。",
      "style": "头发塞入围巾/外套中，仅露出几缕发丝",
      "texture": "自然发丝质感；略带静电的零散飞毛",
      "movement": "几乎无动态；体现寒冷空气的真实感"
    },
    "face": {
      "eyes": "眼睛须与参考图像完全一致；因寒冷而略带眯眼",
      "skin_details": "自然肤质；脸颊处有轻微泛红（细腻、真实）",
      "micro_details": "保留所有原有痕迹"
    },
    "clothing": {
      "outerwear": "冬季大衣 + 围巾 + 毛线帽（不得含任何标识或文字）",
      "fabric": "可见羊毛针织纹理；大衣表面附着细小雪花颗粒"
    },
    "accessories": {
      "jewelry": [
        "银色耳环可选（可能被围巾遮挡）"
      ]
    }
  },
  "pose": {
    "type": "户外抓拍式姿态",
    "orientation": "半身构图",
    "hands": "双手轻握围巾靠近下巴（手套可选，须无品牌标识）",
    "gaze": "直视镜头，面露温馨微笑",
    "expression": "温暖、俏皮"
  },
  "setting": {
    "environment": "黄昏时分的积雪街道",
    "background_elements": [
      "飘落的雪花（细腻颗粒状，非雾气效果）",
      "路灯光斑虚化（bokeh）",
      "柔和模糊的剪影（不可辨识具体人脸）"
    ],
    "depth": "面部清晰锐利；背景呈奶油般柔焦虚化（creamy bokeh）"
  },
  "camera": {
    "shot_type": "半身冬季人像",
    "angle": "平视角度（eye level）",
    "focal_length_equivalent": "35–50mm专业镜头 或 26mm手机夜景模式",
    "framing": "4:5",
    "focus": "双眼清晰锐利；雪花呈柔和虚化"
  },
  "lighting": {
    "source": "路灯照明 + 黄昏环境光",
    "direction": "柔和的顶部/侧向辉光",
    "highlights": "发丝与脸颊呈现暖色调高光",
    "shadows": "柔和、富有电影感的冬季明暗对比"
  },
  "mood_and_expression": {
    "tone": "温馨、电影感、可爱且具亲和力",
    "atmosphere": "冬季抓拍氛围"
  },
  "style_and_realism": {
    "style": "照片级写实生活方式风格（photoreal lifestyle）",
    "imperfections": "允许低光照条件下的自然噪点（grain）"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "resolution": "高分辨率",
    "noise": "中等程度低光照噪点（grain）",
    "mode_variants": {
      "amateur": "手机夜景模式风格：轻微噪点、略微倾斜构图、非完美取景",
      "pro": "更干净的电影感曝光，高光控制精准，景深浅（shallow DOF）"
    }
  },
  "constraints": {
    "adult_only": true,
    "single_subject_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "造雾机",
    "烟雾",
    "身份偏移（identity drift）",
    "面部形变（face morphing）",
    "多余手指",
    "扭曲的手部",
    "可读文字",
    "标识（logos）",
    "水印（watermark）",
    "塑料质感皮肤",
    "过度平滑（over-smoothing）"
  ]
}
```

</details>

<details><summary><b>霓虹小巷中的赛博黑客</b></summary>

```text
你将执行一次图像编辑，将男性主体转变为一名身处粗粝、高科未来世界的在逃网络跑者（netrunner）。最终结果必须是一张超写实、电影级画质的图像，形同一部 IMAX 大片中的单帧画面。场景设定于一条被雨水浸透、霓虹闪烁的小巷中，主体正藏身于此。请确保图像高度精细，运用电影级布光与符合真实物理规律的细节表现，并以 Arri Alexa 摄影机拍摄，采用浅景深，使主体从纷乱的背景中脱颖而出。  

{
  "prompt": "你将执行一次图像编辑，将男性主体转变为一名身处粗粝、高科未来世界的在逃网络跑者（netrunner）。最终结果必须是一张超写实、电影级画质的图像，形同一部 IMAX 大片中的单帧画面。场景设定于一条被雨水浸透、霓虹闪烁的小巷中，主体正藏身于此。请确保图像高度精细，运用电影级布光与符合真实物理规律的细节表现，并以 Arri Alexa 摄影机拍摄，采用浅景深，使主体从纷乱的背景中脱颖而出。",
  "details": {
    "year": "${year:2084}",
    "genre": "电影级写实主义",
    "location": "一座垂直建造的赛博朋克巨型都市中一条狭窄、散落着杂物的巷道。地面为湿滑沥青，倒映着上方摩天大楼投射而下的、混乱闪烁的霓虹汉字标识。",
    "lighting": [
      "体积感霓虹蓝与霓虹洋红背光",
      "面部柔和冷调补光",
      "高对比度阴影",
      "潮湿表面的镜面高光"
    ],
    "camera_angle": "平视中景，浅景深（背景虚化），聚焦于主体紧张凝重的表情。",
    "emotion": [
      "偏执",
      "专注",
      "急迫"
    ],
    "color_palette": [
      "电光青",
      "霓虹粉",
      "深影黑",
      "雨银",
      "冷蓝"
    ],
    "atmosphere": [
      "反乌托邦",
      "压抑闭塞",
      "潮湿",
      "粗粝",
      "高科技低生活（High-Tech Low-Life）"
    ],
    "environmental_elements": "时间凝固的坠落雨滴、从通风口升腾盘旋的蒸汽、在泥泞水洼中倒映闪烁的全息广告。",
    "subject1": {
      "costume": "一件质感厚重、防水的黑色科技风防风夹克，表面带有发光几何图案；配戴无指战术手套；太阳穴处可见金属质地的神经接口端口。",
      "subject_expression": "高度专注混杂焦虑的神情，汗水与雨水沿面部滑落。",
      "subject_action": "正快速敲击由腕载式网络甲板（cyberdeck）投射出的悬浮全息键盘，同时警觉地回头张望。"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "日光",
        "阳光",
        "蓝天",
        "洁净表面",
        "干燥",
        "暖色调布光"
      ],
      "exclude_styles": [
        "卡通",
        "动漫",
        "3D 渲染",
        "绘画",
        "低分辨率",
        "模糊",
        "素描"
      ],
      "exclude_colors": [
        "暖调棕褐（sepia）",
        "粉彩",
        "明亮纯白",
        "米色"
      ],
      "exclude_objects": [
        "汽车",
        "树木",
        "宠物",
        "花卉"
      ]
    }
  }
}
```

</details>

<details><summary><b>霓虹小巷夜行专辑封面</b></summary>

```text
电影感的狭窄城市小巷夜景，地面被雨水浸湿，反射着霓虹灯光。  
竖屏构图（9:16），专辑封面风格。

一名男性人物从画面中距离处平静地朝镜头走来。  
姿态自信而克制，具有自然的街头存在感。  
穿着深色极简服装，无可见品牌标识。  
面部被环境霓虹灯光部分照亮，在身体上形成柔和的色彩过渡。

环境：  
未来感的霓虹光拱门在头顶交错，形成隧道般的透视效果。  
潮湿的路面强烈反射蓝色、红色和橙色的光。  
两侧为建筑物，店铺橱窗因景深而模糊。  
远处有几名行人，处于柔焦状态。

灯光与氛围：  
电影级灯光，逼真的霓虹辉光。  
冷蓝色与暖红色/橙色灯光混合。  
自然阴影，无强烈对比。  
带有氛围感的雨景，轻微薄雾。

相机与风格：  
全身镜头， eye-level 角度。  
背景有轻微景深模糊。  
超写实，电影级写实风格。  
无幻想元素，无动画质感。  
无夸张效果。

整体感觉：  
现代街头美学，黑暗但优雅。  
极简主义，情绪化，自信。  
类似专辑封面或音乐视频关键帧。
```

</details>

<details><summary><b>青少年书籍封面插画</b></summary>

```text
Thoughtful Islamic book cover illustration for teenagers, side silhouette of a young person. Inside the head a question mark transforming into light and certainty. Arabic word "اليقين" integrated in the light. Deep purple and blue tones, minimalist and modern style, serious educational mood, no cartoon elements, vertical format, high resolution.
```

</details>

<details><summary><b>青年漫画风格转换</b></summary>

```text
将上传的图像转换为超精细的黑白青年漫画（seinen manga）杰作，同时完全准确地保留原始主体。

绝对优先事项：  
原始人物的身份必须完全保持不变。  
100% 保留面部相似度。  
不得重新设计、重新诠释、美化、风格化、理想化、变老或变年轻，或以任何方式修改面部。  
必须精确保留面部比例、头骨形状、下颌线、颧骨、鼻子形状、嘴唇形状、眼睛形状、眼皮结构、眉毛形状、额头、耳朵、发型、发际线、皮肤纹理、皱纹、疤痕、面部毛发以及表情。  
该主体必须能被立即识别为原始人物。  
仅艺术媒介发生变化；人物本身不变。

仅限风格转换：  
将照片转化为高端青年漫画插画。  
保留确切的构图、画面框架、相机角度、姿势、透视、解剖结构、服装、配饰和背景结构。

艺术风格：  
超精细日本青年漫画（seinen manga），  
大师级墨水插画，  
极致交叉排线，  
密集线条，  
强烈的明暗对比（chiaroscuro），  
深黑色阴影，  
高对比度单色，  
写实解剖结构，  
战斗氛围，  
心理张力，  
电影级光影，  
传统漫画墨水技法，  
专业出版级漫画质量，  
博物馆级插画水准，  
传奇漫画艺术美学。

墨水细节：  
重度交叉排线，  
细密排线，  
羽化线条（feathering），  
点刻法（stippling），  
刮版纹理（scratchboard texture），  
精准轮廓线，  
深色阴影块，  
干净白色高光，  
饱满黑色墨水覆盖，  
高细节纹理渲染。

光影效果：  
戏剧性定向光源，  
强烈阴影，  
高对比度，  
通过墨线表现体积深度，  
黑暗电影感氛围。

质量要求：  
杰作，  
最佳质量，  
超精细，  
8K 级细节，  
极清晰线稿，  
专业漫画分镜质量，  
获奖级插画水准。

情绪氛围：  
坚毅，  
压迫感，  
严肃，  
坚定，  
身经百战，  
传奇感，  
情感强烈，  
强大气场。

负向提示词（NEGATIVE PROMPT）：  
不同面孔，  
身份改变，  
面部重建，  
面部重新设计，  
面部增强，  
美化面部，  
AI生成面孔，  
动漫脸（anime face），  
通用漫画脸，  
新发型，  
不同表情，  
不同年龄，  
不同种族，  
比例改变，  
对称性修正，  
美化滤镜，  
塑料质感皮肤，  
光滑皮肤，  
可爱风格，  
Q版（chibi），  
卡通，  
Pixar风格，  
Disney风格，  
西方漫画，  
3D渲染，  
CGI，  
低细节，  
模糊，  
柔光，  
数字绘画，  
彩色图像，  
水彩，  
油画，  
拼贴图像（photobash），  
角色重新设计，  
身份偏移，  
面部修改，  
面部再诠释，  
艺术自由发挥，  
面部特征风格化。

最终指令：  
以法医级精度保留原始身份、面部几何结构和表情。仅应用黑白青年漫画墨水风格。面部、肖像及独特特征必须保持不变。
```

</details>

<details><summary><b>静谧月夜街景插画</b></summary>

```text
{
  "colors": {
    "color_temperature": "cool",
    "contrast_level": "high",
    "dominant_palette": [
      "teal",
      "cool gray",
      "warm yellow",
      "orange"
    ]
  },
  "composition": {
    "camera_angle": "eye-level shot",
    "depth_of_field": "deep",
    "focus": "A corner building with a lit cafe",
    "framing": "The building is positioned on the right side of the frame, balanced by the open water and sky on the left. Power lines and a crosswalk create leading lines."
  },
  "description_short": "A digital illustration of a quiet, moonlit street scene by the water, featuring a warmly lit cafe and a black cat sitting on a balcony.",
  "environment": {
    "location_type": "cityscape",
    "setting_details": "A multi-story building with a cafe on the ground floor stands next to a body of water under a night sky. A crosswalk is in the foreground, and a distant shoreline is visible across the water.",
    "time_of_day": "night",
    "weather": "clear"
  },
  "lighting": {
    "intensity": "moderate",
    "source_direction": "mixed",
    "type": "atmospheric"
  },
  "mood": {
    "atmosphere": "Peaceful and solitary urban night",
    "emotional_tone": "calm"
  },
  "narrative_elements": {
    "character_interactions": "A solitary cat observes the quiet scene from its perch on a balcony.",
    "environmental_storytelling": "The warmly lit but empty cafe suggests a late hour, creating a tranquil and lonely atmosphere in an urban setting. The moonlit water adds to the sense of peace.",
    "implied_action": "The scene is still and quiet, as if paused in time. The cat is watching, and the moon's reflection ripples gently on the water."
  },
  "objects": [
    "building",
    "cafe",
    "cat",
    "balcony",
    "moon",
    "water",
    "power lines",
    "crosswalk",
    "tables",
    "chairs"
  ],
  "people": {
    "count": "0"
  },
  "prompt": "A serene digital illustration of a street corner by the sea at night. A bright full moon hangs in the textured teal sky, its light reflecting on the calm water. The ground floor of a European-style building is a warmly lit cafe with empty white tables and chairs outside. Above, a lone black cat sits on a balcony, silhouetted against the night sky. The style is painterly and atmospheric, with visible brush textures, evoking a feeling of quiet solitude and peace.",
  "style": {
    "art_style": "illustrative",
    "influences": [
      "lo-fi aesthetic",
      "Japanese animation"
    ],
    "medium": "digital art"
  },
  "technical_tags": [
    "illustration",
    "night scene",
    "cat",
    "moonlight",
    "cafe",
    "waterside",
    "atmospheric",
    "digital painting",
    "textured"
  ],
  "use_case": "Training for stylized illustration generation or datasets focused on atmospheric and emotional scenes.",
  "uuid": "b55094a8-7a9b-4e1e-ba85-5e7893761150"
}
```

</details>

<details><summary><b>静谧草地人像三联画</b></summary>

```text
{
  "colors": {
    "color_temperature": "暖色调",
    "contrast_level": "中等对比度",
    "dominant_palette": [
      "绿色",
      "米色",
      "红橙色"
    ]
  },
  "composition": {
    "camera_angle": "多角度三联画",
    "depth_of_field": "浅景深",
    "focus": "红发女子",
    "framing": "该图像为一幅三联画，融合广角镜头、特写肖像与低角度镜头，构成叙事性序列。"
  },
  "description_short": "一幅三联画作品，描绘一位长发红发的年轻女子置身于阳光普照的草甸之中。上幅为广角镜头，展现她双臂张开的姿态；中幅为面部特写肖像；下幅则以低角度呈现她仰卧于草丛中、伸手朝向镜头的画面。",
  "environment": {
    "location_type": "户外",
    "setting_details": "一片郁郁葱葱的绿色草甸，长草丰茂，背景为高大成熟的树木。",
    "time_of_day": "下午",
    "weather": "晴朗"
  },
  "lighting": {
    "intensity": "中等强度",
    "source_direction": "混合光源方向",
    "type": "自然光"
  },
  "mood": {
    "atmosphere": "宁静而富有奇想的自然联结感",
    "emotional_tone": "平静"
  },
  "narrative_elements": {
    "environmental_storytelling": "天然、野趣的环境暗示了自由、平和以及与自然融为一体的主题。",
    "implied_action": "女子正在起舞、休憩并伸出手去，暗示其与周遭环境之间流畅而富表现力的互动。"
  },
  "objects": [
    "女子",
    "连衣裙",
    "高草",
    "树木"
  ],
  "people": {
    "ages": [
      "青年"
    ],
    "clothing_style": "波西米亚风、草原风格连衣裙",
    "count": "1",
    "genders": [
      "女性"
    ]
  },
  "prompt": "一幅电影感胶片摄影风格的三联画，主角是一位美丽、年轻的女子，拥有飘逸的长红发与雀斑，身着浅色草原风格连衣裙。上幅：广角镜头捕捉她在阳光斑驳的草甸中、在巨大橡树下双臂高举、尽情欢跃的瞬间；中幅：亲密的面部特写肖像，她温柔微笑直视镜头，背景为柔和虚化的绿色；下幅：低角度镜头呈现她仰卧于高草之中，一手伸向观者。整体风格具有电影感，采用温暖柔和的光线与怀旧的胶片颗粒质感。",
  "style": {
    "art_style": "写实主义",
    "influences": [
      "电影摄影",
      "独立电影",
      "生活方式摄影"
    ],
    "medium": "摄影"
  },
  "technical_tags": [
    "三联画",
    "肖像",
    "广角镜头",
    "浅景深",
    "胶片颗粒",
    "自然光"
  ],
  "use_case": "图库摄影、时尚杂志专题或叙事性故事集数据集。",
  "uuid": "b70a4a22-22c1-4d22-8a61-48e92bddb07e"
}
```

</details>

<details><summary><b>非洲未来主义高定时尚模特</b></summary>

```text
风格 / 美学：  
高定时装杂志风、奢华商业摄影、超现实3D渲染美学、神话式非裔未来主义、华丽暗黑幻想、完全对称构图。  

主体：  
解剖结构：1girl，年轻女性，面容完美对称，中深肤色，饱满嘴唇，双手完美且指甲自然。  
皮肤：发光、高度油亮且具光泽的皮肤，纹理无瑕，黑色素丰富，轻微次表面散射效果。  
头发：隐藏于头盔之下。  
服装：（金属金色凹凸纹理肩甲：1.3），搭配同色金属金色比基尼上衣。  
配饰：（镶嵌钻石的圆顶头盔，带有大型金色十字图案：1.4），（光滑反光的金色面罩覆盖上半面部和眼睛：1.3），精致的白色水晶/蕾丝几何状珠宝贴合于脸颊。  
身体装饰：贴合面部的水晶装饰。  

姿势与表情：  
姿势：四肢着地蹲伏，身体前倾，双手掌心平放于地面朝向镜头，姿势完全对称。  
表情：凶猛、性感、目光强烈（暗示存在于面罩之下），双唇微张且具光泽。  

背景与场景：  
场景：黑暗而华丽的摄影棚环境，（完美反光的黑色镜面地板：1.4）。  
细节：（两条大型高度细节化的金属金色蛇对称缠绕， framing 主体，顶部相对而视：1.4），深色大理石柱带有金色希腊回纹边框，镜面地板上散落着金属金色玫瑰。  

灯光与相机：  
灯光：戏剧性高对比度影棚灯光，（耀眼的镜面高光与十字形镜头光晕在黄金和钻石上闪烁：1.3），强烈的轮廓光勾勒身体与蛇形，使其与黑暗背景分离，阴影深邃。  
相机风格：对称广角镜头，低角度拍摄，完全居中构图，主体面部与双手清晰对焦，电影级超现实主义。  

渲染 / 质量标签：  
杰作，最佳质量，超精细，高分辨率，照片级纹理，Octane render 美学，光线追踪反射，高度细节化的黄金材质，8k 分辨率。  

负向提示词：  
（最差质量，低质量，普通质量：1.4），非对称构图，构图失衡，插画，绘画，素描，卡通，动漫，3D几何伪影，丑陋，手部绘制粗糙，手指绘制不佳，多余手指，缺失手指，变异的手，解剖错误，肢体畸形，面部绘制不佳，杂乱背景，文字，水印，签名，昏暗灯光，哑光皮肤，缺失反射，扭曲反射，模糊，失焦。
```

</details>

<details><summary><b>项目画风一致性生成指令</b></summary>

```text
作为图像生成专家，你负责创建符合特定艺术风格和项目规范的图像。

你的任务是：
- 仅使用指定项目文件夹内的可用文件。
- 确保所有生成的图像保持用户指定的艺术风格和类型。

你需要：
- 访问并使用项目文件：确保图像生成中使用的任何参考、纹理或资源均来自用户的项目文件。
- 保持风格一致性：遵循用户指定的艺术风格指南，以创建统一且协调的图像。
- 清晰沟通：如果缺少任何必需的文件，或需要额外输入以保持一致性，请及时通知用户。

规则：
- 不得使用所提供项目之外的外部文件或资源。
- 一致性至关重要；确保所有图像都符合用户的艺术构想。

变量：
- ${projectPath}：项目文件的路径。
- ${artStyle}：用户指定的艺术风格。

示例：
- “使用来自 ${projectPath} 的资源，以 ${artStyle} 风格生成一张图像。”
```

</details>

<details><summary><b>预制烧烤商用厨房模型</b></summary>

```text
创建一个预制厨房模型，并包含与尺寸为10英尺x15英尺的烧烤区域相关的全套设备
```

</details>

<details><summary><b>马格利特风格超现实绘画</b></summary>

```text
{
  "colors": {
    "color_temperature": "暖色调",
    "contrast_level": "高对比度",
    "dominant_palette": [
      "红色",
      "橙色",
      "灰蓝色",
      "浅灰色"
    ]
  },
  "composition": {
    "camera_angle": "平视角度",
    "depth_of_field": "深景深",
    "focus": "红色太阳",
    "framing": "构图呈水平分层，前景是一堵石墙，中景是一排树木，背景是天空。红色太阳位于画面中央，形成强烈的视觉焦点。"
  },
  "description_short": "一幅雷内·马格里特风格的超现实主义绘画，描绘一个鲜艳的红色太阳或球体悬挂在一片暗淡的灰蓝色树林前方，背景是炽热的红色和橙色天空。前景有一堵带有陶罐的石墙。",
  "environment": {
    "location_type": "户外",
    "setting_details": "场景看似一个公园或正式花园，视角位于一堵低矮石墙之后。一片精心修剪的草坪将石墙与一片茂密的叶树林分隔开来。",
    "time_of_day": "傍晚",
    "weather": "晴朗"
  },
  "lighting": {
    "intensity": "强烈",
    "source_direction": "未知",
    "type": "超现实"
  },
  "mood": {
    "atmosphere": "神秘而梦幻般的静谧",
    "emotional_tone": "超现实"
  },
  "narrative_elements": {
    "environmental_storytelling": "太阳被不可能地置于树木前方，颠覆了现实，营造出一种惊奇感和智性悖论。普通的人造石墙与非凡的自然景象形成对比，质疑观者对空间和现实的感知。",
    "implied_action": "整个场景完全静止，捕捉了一个违背天体自然运动规律的瞬间。"
  },
  "objects": [
    "红色太阳",
    "树木",
    "石墙",
    "石罐",
    "天空",
    "草坪"
  ],
  "people": {
    "count": "0"
  },
  "prompt": "一幅高度细致的超现实主义油画，风格仿雷内·马格里特。一个巨大、完美圆形、鲜艳的红色太阳悬浮在空中，不可思议地出现在一片密集的灰蓝色树木前方。其后的天空散发出强烈的渐变光芒，从顶部的炽热红色过渡到地平线处的温暖橙色。前景中，一堵精细描绘的浅灰色石墙，墙上有一个古典风格的陶罐置于基座上，构成了画面底部的框架。整体氛围神秘、寂静且如梦似幻，暖色与冷色之间形成鲜明对比。",
  "style": {
    "art_style": "超现实主义",
    "influences": [
      "René Magritte"
    ],
    "medium": "绘画"
  },
  "technical_tags": [
    "超现实主义",
    "油画",
    "风景",
    "并置",
    "象征主义",
    "高对比度",
    "鲜艳色彩"
  ],
  "use_case": "艺术史数据集、风格迁移模型训练、超现实主义AI艺术提示词灵感。",
  "uuid": "b6ec5553-4157-4c02-8a86-6de9c2084f67"
}
```

</details>

<details><summary><b>驯龙高手贴纸表</b></summary>

```text
创建一张A4尺寸的竖向贴纸页，包含30个《驯龙高手》电影中的角色。
角色必须与原版《驯龙高手》电影中的形象完全一致，忠实还原，不得重新设计，不得重新诠释。
使用电影中正确的原始服装和龙的设计，颜色和细节准确无误。
头部、眼睛、耳朵、翅膀和尾巴必须完整可见（不得裁剪或缺失）。
小嗝嗝（Hiccup）和没牙仔（Toothless）出现频率最高，展示不同的站立或飞行姿势及表情。
其他角色和龙也需包含在内，且保持电影中的原始设计不变。
采用随机散布布局，拼贴风格排列，不按行或网格对齐。
每个贴纸周围留有空白区域，确保清晰分隔，便于偏移/模切打印。
纯白色背景，无文字、无阴影、无场景。
高分辨率，贴纸边缘清晰，可直接打印。
负面提示词（NEGATIVE PROMPT）  
redesign, altered characters, wrong outfit, wrong dragon design, same colors for all, missing wings, missing tails, cropped wings, cropped tails, chibi, kawaii, anime style, exaggerated eyes, distorted faces, grid layout, aligned rows, background scenes, shadows, watermark, text
```

</details>

<details><summary><b>高对比模板矢量海报</b></summary>

```text
将上传的肖像转化为高对比度的矢量海报插画。

风格要求：
- 大胆的模板/宣传海报美学
- 扁平矢量艺术
- 仅使用 3–4 种颜色
- 纯红色背景
- 面部以灰度色调呈现（2–3 个扁平阴影层）
- 黑色粗外轮廓线
- 无渐变
- 无纹理
- 无写实效果
- 锐利干净的边缘
- 海报化阴影
- 居中头部构图
- 极简但强烈的面部特征
- 平面设计风格
- Adobe Illustrator 矢量外观
- 高对比度
- 平滑的几何阴影形状

输出：
清晰、干净、可缩放的矢量风格肖像。
```

</details>

<details><summary><b>高端科技感网站UI改版</b></summary>

```text
扮演一名使用Image2的UI/UX设计师。你的任务是为一个网站前端创建多个高端、受科技启发的UI设计。你必须：
- 保留所有现有功能（不增加也不删除）
- 专注于修改布局和主题
- 以高端、未来感的科技美学进行设计
- 生成多种风格选项供客户选择

约束条件：
- 确保设计适用于现代高科技网站
- 保持用户体验直观且无缝

你的输出将包括：
- 一组展示不同风格的图像设计
- 每个设计都必须突出网站的功能性，同时提供全新的视觉美感
```

</details>

<details><summary><b>高端美妆大片拍摄规格</b></summary>

```text
{
  "project_specifications": {
    "format": "2×2 网格拼贴图",
    "aspect_ratio": "4:5",
    "aesthetic_style": "高端美妆杂志风格",
    "rendering_engine_hints": {
      "realism_level": "超写实级",
      "texture_quality": "8K",
      "lighting_simulation": "光线追踪式影棚布光"
    }
  },
  "global_assets": {
    "subject_definition": {
      "hair": {
        "style": "长发，松散波浪卷，丰盈蓬松",
        "texture": "自然质感，每根发丝清晰可辨",
        "behavior": "略带凌乱但经过精心打理，自然勾勒面部与肩部轮廓"
      },
      "complexion": {
        "skin_texture": "具毛孔细节，超写实",
        "finish": "水润光泽感，玻璃肌效果",
        "makeup": {
          "cheeks": "浓重红晕／腮红",
          "lips": "高光感、丰唇效果、自然粉色调",
          "eyes": "洁净分明的睫毛，自然眉形"
        }
      },
      "wardrobe": {
        "item": "迷你连衣裙",
        "fit": "紧身／贴身剪裁",
        "fabric": {
          "material": "柔软纹理针织面料／粗花呢",
          "tactility": "毛绒感、反光纤维",
          "color": "柔雾紫或中性灰褐色"
        },
        "details": "细肩带，及大腿中部长度"
      }
    },
    "environment_definition": {
      "studio_setup": {
        "background": "无缝纸背景，柔和米白／浅驼色",
        "atmosphere": "干净、温暖、私密"
      },
      "lighting_rig": {
        "key_light": "大型漫射柔光箱（左前方）",
        "fill_light": "反光板（右侧）",
        "highlights": "嘴唇、颧骨与肩部呈现镜面高光"
      }
    }
  },
  "panel_architecture": [
    {
      "position": "左上角（1）",
      "shot_type": "极致特写（微距）",
      "composition": {
        "angle": "低角度，略微仰视",
        "focus": "口鼻区域",
        "depth_of_field": "景深极浅"
      },
      "action": {
        "primary": "正在吃一颗草莓",
        "nuance": "指尖轻捏，双唇微微张开"
      },
      "visual_anchors": [
        "草莓表面的湿润反光",
        "嘴唇上的高光反射",
        "太阳穴处的绒毛"
      ]
    },
    {
      "position": "右上角（2）",
      "shot_type": "中景（大腿以上）",
      "composition": {
        "angle": "平视角度",
        "pose_dynamic": "身体略微前倾朝向镜头"
      },
      "action": {
        "stance": "直立站立",
        "arms": "双臂自然垂于身体两侧",
        "expression": "直视镜头，魅惑微噘唇"
      },
      "visual_anchors": [
        "针织连衣裙的纹理细节",
        "锁骨处的阴影",
        "腰线的自然曲度"
      ]
    },
    {
      "position": "左下角（3）",
      "shot_type": "全身像（坐姿）",
      "composition": {
        "angle": "侧脸轮廓视角",
        "framing": "人物紧凑地置于地面"
      },
      "action": {
        "pose": "双膝抱胸（胎儿姿势变体）",
        "interaction": "脸颊轻靠膝盖，双臂环抱双腿",
        "hair_flow": "长发如瀑倾泻至地面"
      },
      "visual_anchors": [
        "腿部线条的平滑轮廓",
        "连衣裙在大腿处的拉伸质感",
        "梦幻般的眼神"
      ]
    },
    {
      "position": "右下角（4）",
      "shot_type": "美妆人像（头部与双手）",
      "composition": {
        "angle": "正面特写",
        "framing": "从下巴至发际线"
      },
      "action": {
        "gesture": "下巴轻 resting 在交叠的手指上",
        "expression": "柔和微笑，目光略偏镜头外"
      },
      "visual_anchors": [
        "手部细节与美甲效果",
        "眼部清晰度",
        "脸颊红晕"
      ]
    }
  ]
}
```

</details>

<details><summary><b>鸡尾酒视频</b></summary>

```text
神秘调酒师将发光的绿色液体倒入杯中的电影级特写，浓烟升腾，背景为昏暗的鸡尾酒吧，4k，超现实，慢动作。
```

</details>

<details><summary><b>黄金时刻海滩漫步</b></summary>

```text
{
  "category": "BEACH_WALK_GOLDEN_HOUR_FULLBODY",
  "subject": {
    "demographics": "成年女性，21–29 岁，土耳其人外貌，旅行博主气质。",
    "hair": {
      "color": "深棕色",
      "style": "松散波浪卷，带有海风拂过的痕迹",
      "texture": "自然发丝，略带飞毛",
      "movement": "头发随海风轻微飘动"
    },
    "face": {
      "eyes": "愉悦，因阳光微微眯眼",
      "skin_details": "真实肌肤质感，阳光亲吻般的光泽（非油光）",
      "makeup": "极简海滩妆容"
    },
    "clothing": {
      "outfit": "亚麻连衣裙或沙滩罩衫（无任何品牌标识）",
      "fabric": "可见亚麻织纹，带有柔和褶皱",
      "movement": "裙摆自然摆动"
    },
    "accessories": {
      "jewelry": ["银色圆环耳饰"]
    }
  },
  "pose": {
    "type": "全身行走抓拍照",
    "orientation": "沿海岸线迈步中段姿态",
    "hands": "一只手轻提裙摆，另一只手将头发向后拨开",
    "gaze": "低头轻笑，随后略带看向镜头的互动感",
    "posture": "无忧无虑、放松自然"
  },
  "setting": {
    "environment": "海滩海岸线",
    "background_elements": [
      "水面柔和的夕阳倒影",
      "沙地上的脚印",
      "淡淡薄雾（源自自然海空气，非烟雾）"
    ],
    "depth": "主体清晰锐利，背景柔和虚化"
  },
  "camera": {
    "shot_type": "全身旅行摄影",
    "angle": "平视角度",
    "focal_length_equivalent": "26mm 手机镜头或 35mm 杂志级镜头",
    "framing": "4:5",
    "focus": "面部清晰可辨；运动模糊程度极低"
  },
  "lighting": {
    "source": "黄金时刻阳光",
    "direction": "发丝与肩部呈现背光/侧逆光轮廓光",
    "highlights": "可控的日光眩光",
    "shadows": "柔和、暖调"
  },
  "mood_and_expression": {
    "tone": "梦幻、自在、温暖",
    "expression": "自然流露的欢笑",
    "atmosphere": "漫游情怀式抓拍氛围"
  },
  "style_and_realism": {
    "style": "照片级写实旅行博主风格",
    "imperfections": "裙摆允许轻微运动模糊；面部细节必须保持清晰"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "低至中等噪点",
    "motion_blur": "仅限于布料，且极其细微"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "水枪喷溅", "虚假水体纹理",
    "多余肢体", "扭曲的地平线",
    "可读文字", "品牌标识", "水印"
  ]
}
```

</details>

<details><summary><b>黄金时刻街拍抓拍</b></summary>

```text
2026 年德黑兰的抓拍街头照片，黄金时段，浅景深，人群在背景中模糊。一名伊朗女性目光瞥向画外；双眉轻轻扬起一次，眼神迅速瞄向出口，瞳孔微微睁大——这是秘密信号“我们走吧，现在”。画面下方有一个手写边框的方框，圆珠笔字迹写着：“بریم？”
```

</details>

<details><summary><b>黄金时刻面部微距特写</b></summary>

```text
黄金时刻拍摄的一位年轻女性面部的极致特写微距照片。温暖的自然阳光从侧面照射，在湿润且布满雀斑的皮肤上形成发光的高光。右眼为榛色，处于锐利对焦状态，以极高清晰度反射光线。浅景深使眼睛、皮肤纹理、鼻子和嘴唇脱颖而出，而背景则完全虚化消失。皮肤纹理高度精细且真实，毛孔与雀斑清晰可见，未经重度修图处理。色彩主调为温暖的青铜色、棕褐色、金色与柔和的棕色。氛围宁静、私密、沐浴于阳光之中。电影级美感摄影，超现实主义风格，自然观感，高细节呈现。
```

</details>

<details><summary><b>黎明前的古代麦加</b></summary>

```text
创建一幅超写实电影级的古代麦加黎明前场景，视角为从克尔白（Kaaba）屋顶正上方高空俯拍，以对角线向下角度聚焦于其左下角及周围开阔的地面。场景包含以下要素：

- 克尔白孤然矗立于一片广阔露天沙质庭院正中央，地面由压实的沙土与干涸土壤构成，凹凸不平、布满尘埃。
- 周围区域刻意保持开阔空旷，以凸显其神圣的孤立性；远处零星散布着若干小型泥砖与石砌房屋群落，标示出早期麦加聚落的轮廓。
- 粗粝嶙峋的岩石山脉沿山谷两侧拔地而起，渐次隐没于清冷泛蓝的黎明前薄雾之中。
- 克尔白左下垂直转角处（即两面墙体交汇之角）出现一处神迹般的开口，从中迸发出强烈、纯粹的白色圣光，向外辐射。
- 一名女子正从该转角开口中现身，身着简朴的沙漠服饰，怀抱一名新生婴儿，其身影在地面上投下长长的影子。
- 天空中浮现数簇微弱、抽象的发光白色光团，暗示天使的存在。

整体氛围须庄严而神圣，采用超写实渲染，搭配富有戏剧张力的电影级布光、强烈的体积光束（volumetric light rays）以及高度精细的材质纹理。画面构图应如史诗级历史影片的一帧定格，采用 4:5 竖幅画幅比例，且不得出现任何现代元素。
```

</details>

<details><summary><b>黏土迷你城市</b></summary>

```text
生成一个奇趣盎然的微型世界，以${landmark_name}为核心地标，整个场景完全由五彩缤纷的造型黏土手工制作而成。所有元素（建筑、树木、水道及城市设施）均须呈现手塑质感，表面清晰可见指纹印痕与天然黏土肌理。采用活泼稚拙的儿童画风，配色明快鲜艳：湛蓝晴空、蓬松乳白云朵、翠绿树木，以及暖色调的建筑——明黄、橙红、正红与钴蓝相间。每一处表面与柔和曲面都须彰显手工制作的独特品质。采用广角视角构图，完整呈现整片微型景观，营造和谐而欢愉的整体氛围。

在画面正上方中央位置，以干净、粗体、圆润友好的字体添加城市名称${city_name}，字体风格须契合整体黏土美学。文字须清晰可辨，在天空背景上具备高对比度，并带有微妙的立体深度效果（仿佛亦由黏土制成——即轻微3D黏土字效），但整体保持简洁，切勿过度细节化。

场景中其他任何位置均不得出现额外文字、单词或标识牌。仅可通过具有辨识度的建筑特征，借由纯粹的雕塑式黏土元素来定义该地点。图像尺寸为1080×1080像素。
```

</details>

<details><summary><b>黑暗世界彩色漫画风</b></summary>

```text
${subject} 以经典《狼人》（Werewolf）书籍中所采用的独特彩色“黑暗世界”（World of Darkness）漫画风格呈现。厚重的黑色墨线构成画面的结构骨架——粗犷的轮廓线、富有攻击性的交叉排线、深沉的阴影色块——其上叠加饱和而阴郁的色彩晕染。色彩以分层、富表现力的色域方式施加，而非追求写实；色彩随形体流动变化，用以暗示情绪与超自然存在感。高光锐利且具金属质感，仅选择性地落在边缘、双眼、武器或关键特征上。背景采用“黑暗世界”特有的粗粝调色盘：病态的黄色、锈蚀的红色、淤伤般的紫色与冰冷的紫罗兰色。色彩略微溢出墨线边界，营造出混乱而野性的能量。质感粗糙、富有绘画感且阴郁沉重。构图兼具对抗性与亲密感。整体基调：都市哥特式恐怖、泛灵论力量、潜伏于表层之下的威胁感。
```

</details>

<details><summary><b>黑暗世界黑白漫画风</b></summary>

```text
${subject} 以严苛、棱角分明的《黑暗世界》（World of Darkness）漫画式线稿呈现。画面以浓重的黑色油墨为主导，轮廓线粗厚，交叉排线凌厉有力，深重的阴影色块将形体切割为锐利的解剖学平面。人体解剖结构被夸张化且富于表现力，姿态紧绷而具有对抗性。表面被分割为鲜明的明暗几何关系。背景抽象化或呈现都市哥特风格，支离破碎且令人压抑。布光生硬而富有黑色电影（noir）气息，对比极度强烈，边缘硬光清晰勾勒出轮廓与剪影。构图紧凑而富有临场感，采用低角度或对抗性视角的镜头。整体基调：现代哥特式恐怖，粗粝、野性、充满灵性张力。
```

</details>

<details><summary><b>黑白人像黑底效果</b></summary>

```text
将其变为黑白图像。将背景变为纯黑色，使所有元素和谐融合。人物保持完全不变。
```

</details>

<details><summary><b>黑白双人特写肖像</b></summary>

```text
一位男士与一位女士并肩而立的特写黑白肖像。男士头发凌乱，胡茬粗犷；女士则拥有一头自然蓬松、柔顺微乱的秀发。两人都微微仰起头部，富有戏剧性的顶光洒落在他们身上。他们的眼睛隐于阴影之中，营造出一种强烈对比、充满力量感与神秘感的剪影式氛围。9:16 构图，亲密双人肖像构图。
```

</details>

<details><summary><b>黑白影棚侧脸肖像</b></summary>

```text
{
  "以所附人物图像为参考。超写实黑白工作室肖像，展现年轻男子的侧面轮廓，自然发丝轻柔垂落于面部周围。强烈的轮廓光勾勒其下颌线与鼻梁，背景为深色极简风格。神情沉思而宁静，电影级布光营造出强烈的明暗对比与精细的摄影细节。",
  "size": "{argument name="image size" default="1024x1024"}",
  "n": {argument name="number of images" default="1"}
}
```

</details>

<details><summary><b>黑白电影感人像</b></summary>

```text
请上传你的自拍照，以生成一幅超写实的黑白肖像。该肖像将具备以下特征：

- **风格：** 黑白影像，采用富有戏剧性的低调布光（low-key lighting），高对比度，并带有电影感的影调处理（cinematic toning）。
- **姿态：** 稍微侧身，神情自信而凌厉，双手交叠，佩戴可见配饰（腕表与戒指）。
- **布光：** 强烈的单光源照明，来自画面左侧；投下浓重阴影以营造黑色电影（noir）氛围；背景为纯黑色。
- **摄影风格：** 具有高端时尚杂志（editorial luxury-brand）美学特质，纹理锐利、细节清晰，令人联想到经典复古黑色电影（vintage noir films）。

请确保所上传照片能清晰呈现你的面部，并且光线充足，以获得最佳生成效果。
```

</details>

<details><summary><b>黑白自拍人像</b></summary>

```text
请上传你的自拍照，以生成一张超写实的黑白肖像。该肖像将具备以下特征：  

- **风格：** 黑白影像，采用富有戏剧性的低调布光（low-key lighting），高对比度，并带有电影感色调（cinematic toning）。  
- **姿态：** 稍微侧身，神情自信而凌厉，双手交叠，佩戴可见配饰（腕表与戒指）。  
- **布光：** 强烈的单光源照明，来自左侧；投下浓重阴影，营造黑色电影（noir）氛围；背景为纯黑色。  
- **摄影风格：** 具有高端时尚杂志（editorial luxury-brand）美学风格，纹理锐利、细节清晰，令人联想到经典复古黑色电影。  

请确保所上传的照片能清晰展现你的面部，并且光线充足，以获得最佳效果。
```

</details>

<details><summary><b>黑色宽松T恤批量图片</b></summary>

```text
创建50张图片，用于黑色oversize短袖T恤，1:1比例，8k质量，专业风格
```

</details>

<details><summary><b>黑色电影低语</b></summary>

```text
{
  "title": "Whispers of Noir",
  "description": "一幅 gritty、电影感十足的硬汉侦探肖像，他在烟雾缭绕的地下爵士酒吧中等待线索。",
  "prompt": "你将使用所提供照片中的人物作为主体进行图像编辑。保留核心相貌特征。将主体1（男性）转变为一名疲惫的1950年代私家侦探，坐在烟雾弥漫的爵士俱乐部内铺有豪华丝绒的卡座里。将图像渲染为超写实的电影剧照，采用强调其皮肤质感和周围缭绕烟雾的电影级灯光。图像必须高度细致，使用 Arri Alexa 拍摄，并采用浅景深以虚化背景中的乐队，遵循 1:1 的宽高比。",
  "details": {
    "year": "1954",
    "genre": "Cinematic Photorealism",
    "location": "The Blue Velvet Lounge，一个拥有桃花心木墙壁和昏暗台灯的地下俱乐部。",
    "lighting": [
      "Chiaroscuro",
      "温暖的台灯光晕",
      "舞台传来的冷蓝色背光",
      "穿过烟雾的体积光束"
    ],
    "camera_angle": "人眼高度的中近景，聚焦于主体面部。",
    "emotion": [
      "怀疑",
      "厌世",
      "专注"
    ],
    "color_palette": [
      "威士忌琥珀色",
      "丝绒红色",
      "深影黑色",
      "烟草烟雾灰色"
    ],
    "atmosphere": [
      "性感撩人",
      "紧张",
      "压抑",
      "复古"
    ],
    "environmental_elements": "空中弥漫着浓厚的香烟烟雾，桌上放着一只盛有琥珀色液体的水晶杯，背景中有乐手模糊的剪影。",
    "subject1": {
      "costume": "一件纹理分明的炭灰色风衣披在皱巴巴的西装外，领带松散，一顶软呢帽微微前倾。",
      "subject_expression": "锐利而讽刺的目光，眯起的眼睛和紧绷的下颌。",
      "subject_action": "一只手搁在半空的威士忌酒杯旁，身体微微倾向光源。"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "明亮的日光",
        "现代科技",
        "手机",
        "霓虹灯牌",
        "洁净空气"
      ],
      "exclude_styles": [
        "卡通",
        "3d 渲染",
        "动漫",
        "素描",
        "绘画"
      ],
      "exclude_colors": [
        "荧光绿",
        "亮粉红",
        "纯白色"
      ],
      "exclude_objects": [
        "汽车",
        "数字手表",
        "第二个人物"
      ]
    }
  }
}
```

</details>

<details><summary><b>黑色电影猜疑特写</b></summary>

```text
高对比度黑白黑色电影风格的伊朗女性面部特写，百叶窗透入强烈的侧光，半边脸笼罩在深邃阴影中。只有一只眼睛被照亮；眉头向内紧锁，瞳孔偏向眼角，投出斜向的怀疑一瞥，另一侧眉毛完全静止不动。画面中弥漫着香烟的烟雾。图像下方有一个手绘的方框，用粗糙的炭笔线条勾勒，并配有手写字体：“شک” / “suspicion”。
```

</details>
