# 图像与设计 (4/4)

共 743 条。复制后把方括号里的内容换成你的，粘贴进任意对话模型即可。

[English](../en/image.md) · [中文](../zh/image.md)

分页：[1](image.md) · [2](image-2.md) · [3](image-3.md) · **4**

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

<details><summary><b>视觉设计指导师</b></summary>

```text
你的任务是提供专业的视觉设计指导。请分析以下设计需求：

<设计项目>
设计类型：{{DESIGN_TYPE}}
项目背景：{{PROJECT_CONTEXT}}
设计目标：{{DESIGN_GOALS}}
目标受众：{{TARGET_AUDIENCE}}
应用场景：{{APPLICATION_SCENARIOS}}
</设计项目>

<设计要求>
风格偏好：{{STYLE_PREFERENCE}}
色彩要求：{{COLOR_REQUIREMENTS}}
尺寸规格：{{SIZE_SPECIFICATIONS}}
技术限制：{{TECHNICAL_CONSTRAINTS}}
</设计要求>

请提供包含以下内容的设计指导：
1. 设计概念和创意方向
2. 色彩搭配和视觉层次
3. 字体选择和排版布局
4. 图形元素和装饰设计
5. 输出规范和应用指南

请在<design-guide>标签内输出完整的视觉设计指导方案。
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

<details><summary><b>诡异破碎玩偶人像</b> · 机器翻译</summary>

```text
概念:一位年轻女子正在变成破碎玩偶的肖像。美丽与恐怖的结合。
姿势与身体曲线:聚焦于脸部和躯干的特写/中景。她站立着,但姿势紧绷且略显扭曲,模仿没有生命的玩偶。她的身体微微侧向一边,头部呈四分之三侧面。一只手臂(右臂)抬起,轻轻触碰下巴和脖子,强调她的脆弱与易碎。另一只手臂(左臂)位置较低且被部分遮挡,同样营造出僵硬感。整体身体曲线传达出一种迷人与不安交织的奇异感觉。
服装:她穿着复古的褶边奶油色或浅米色衬衫/连衣裙。面料质感明显,在领口和袖子周围堆叠出大量褶皱、荷叶边和花边,类似维多利亚时代或复古年代的服饰。裙子上可见红色系带或丝带,增添对比。服装看起来陈旧磨损。
妆容与特效(最重要):
底妆:她的脸上覆盖着逼真的妆容,类似瓷器上的裂纹。这些细致的黑色"裂纹"线条遍布整张脸——环绕眼睛、横过额头、脸颊和下巴。
眼睛:眼睛周围是深色妆容,增添强烈感与恐怖感。她的睫毛又长又浓密,强调玩偶般的外观。
嘴唇与脸颊:脸颊上以圆圈形涂抹红色腮红,如同经典玩偶。她的嘴唇涂成红色,口红在边缘处看起来略显"受损"或"破裂"。
其他细节:嘴巴和鼻子周围有类似疤痕或额外裂纹的精细妆容。
发型:她的波浪发被编成两条又长又有质感的辫子,垂落在脸的两侧并搭在肩上。脸部周围的头发略显凌乱,增添自然而野性的外观。辫子末端用黑色发绳固定。耳朵上可见一只大号圆形银色耳圈。
氛围与灯光:
灯光:照片在夜晚或昏暗环境中拍摄,带有柔和的暖色灯光和焦外光斑。背景中可见大量模糊的暖色灯光,如灯串和灯笼,营造出神奇而神秘又温馨的氛围。主光集中在她的脸上,突出妆容的质感和衣服的荷叶边。
情绪:情绪是矛盾的,既有诡异的一面(因为玩偶妆),也有美丽的一面(因为姿势和灯光)。她的表情神秘而略带忧伤,却又迷人且暗藏危险。她带着闭唇的淡淡半笑。
相机角度:在视平线或略低于视平线处拍摄,让观者能直视她的眼睛并清楚看到妆容细节。聚焦于她的情绪和服装细节的中景。景深很浅,脸部和上半身保持清晰,背景柔和虚化。
整体外观:一张高质量的肖像,看起来像恐怖电影中的一帧或专业的万圣节写真。
不要改变她的面部特征或身份。保留她确切的面容、面部结构、眼睛、鼻子、嘴唇和其他显著特征。
黑色指甲。
格式:3:4。

写实、高质量、清晰的 8K 照片,使用 iPhone 16 Pro 拍摄。
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

<details><summary><b>豪车内人像</b> · 机器翻译</summary>

```text
一张写实的超高质量8K照片，使用iPhone 16 Pro Max拍摄，宽高比为3:4。

主体与姿势：一位年轻女子坐在一辆高档轿车内。她微微靠在座椅上，一只手臂抬起，肘部弯曲，手搭在脑后。她的头轻轻向一侧倾斜，直视镜头，神情柔和、自信、放松，带着若隐若现的闭唇半笑。

服装：她穿着一件合身的鼠尾草绿（柔和橄榄绿）长袖褶皱连衣裙，躯干部位有明显的横向褶裥和抽褶质感。

发型：长直顺滑的发丝，中分。浓密的发丝自然地从左肩垂落到胸前，带有柔和的自然光泽和温暖的高光。

妆容：优雅的日间妆容，带有锐利的黑色猫眼眼线、光滑透亮的肌肤和哑光裸粉色唇妆。

光线与色彩：柔和的漫射日光从侧面和略偏前方射入，形成柔和的阴影，同时突出面料的质感和头发的光泽。色调将温暖的米绿色调与深邃的暗色车内空间融合。

相机与构图：中近景人像，从略低的角度拍摄并带有轻微倾斜，营造出自然自拍或从副驾驶座抓拍的感觉。

背景与氛围：轻松、精致、时尚且温馨的氛围。背景是虚化的深色豪华轿车内饰，有黑色真皮座椅和精致的饰边细节，让全部注意力集中在这位女子身上。

不要改变女孩的面部特征、眼型、眉毛、鼻子或嘴唇。保持100%的面部相似度。
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

<details><summary><b>超精细满月图</b> · 机器翻译</summary>

```text
**主体与构图：** 一张超高细节、高分辨率的天文摄影照片，一轮明亮的满月位于画面中央，背景是深邃、漆黑如黑曜石的外太空。
**表面细节：** 极其清晰的对焦，呈现错综复杂的地质特征：锐利的环形山边缘、深邃的撞击盆地、显著的辐射纹系统、细腻的表面纹理，以及深色火山质月海与明亮月球高地之间的精细对比。
**光线与色彩：** 自然的银白色月光，带有柔和、真实的矿物色调（表面有淡淡的铁蓝色和钛金色高光）。没有大气雾霾或模糊；在阴影与太空交界处是锐利、高对比度的轮廓光。
**风格与画质：** 以天文望远镜相机设备拍摄，8k 分辨率，照片级真实感，电影般的清晰度，天文摄影杰作，曝光完美，高度精细的纹理，raw 照片，无噪点背景。
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

<details><summary><b>运河浮动书店水粉插画</b> · 机器翻译</summary>

```text
一艘狭长的运河驳船改造成了水上书店,停泊在一条安静、两岸树木成行的运河边,以柔和的水粉(gouache)插画风格绘制。驳船为深森林绿色,配奶油色镶边和一扇圆顶红门;船顶上放着装满书的木箱、盆栽天竺葵和一块折叠起来的条纹遮阳篷。敞开的舱口窗户里能看到摆满彩色书脊的书架,纤道上的小黑板支架是空白的。一只虎斑猫睡在船头的一摞书上。驳船后方,一座古老的砖砌步行拱桥横跨水面,垂柳的枝条拂向水中,背景是一排狭窄的联排房屋。午后宁静的光线,砖墙上泛着温暖的桃色高光,绿色船体在平静的水面上投下柔和的倒影。哑光水粉质感,可见笔触,色彩略带粉质而不透明,边缘柔和,色调柔和低调,由鼠尾草绿、赭黄、砖红和奶油色构成。温馨、从容、童话绘本般的氛围。无可辨认的文字,无人物。
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

<details><summary><b>逆袭青年角色设定</b> · 机器翻译</summary>

```text
年轻黑人男性，23 岁
* 身形修长健壮，中等身高
* 深棕色皮肤
* 短而紧密卷曲的黑发
* 棕色眼睛
* 右眉上方有一道小疤痕
* 神情平静而坚定
* 贫穷版本：褪色的深棕色连帽衫、磨旧的蓝色牛仔裤、旧的黑色运动鞋、棕色帆布单肩包
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

<details><summary><b>遗忘重力的房间</b> · 机器翻译</summary>

```text
将上传的照片作为严格的身份参考。保持这个人完全一致：相同的面容、发型、年龄、皮肤质感和身体比例，不做修饰。

一张写实电影感照片，竖幅 4:5，平视视角，相机完全水平，中远景。看起来像是用真实相机拍摄的实景特效电影布景。

这个人笔直站在一间优雅而普通的房间中央的木地板上。全身可见，姿态放松，穿着低调的当代服装，带着淡淡的好奇环顾四周。面部清晰可见，光线柔和。他们是画面中唯一的人，也是主要焦点。

房间有暗调的哑光灰泥墙、真实的木地板、后墙上的一扇窗、极简的家具和温暖的实用灯具。两侧墙壁、地板和部分天花板都可见。房间完全正常，唯一的例外是有四件物体各自拥有自己的重力方向。

左侧：窗上方横杆上的一条白色中等厚重的窗帘，向侧面垂落而不是向下。它从横杆水平地朝左墙垂挂，就像一条正常垂挂的窗帘旋转了 90 度。窗上方的横杆是它唯一的固定点。窗帘的远端自由悬垂，离左墙有一小段距离，末端是松散、略不整齐的竖直下摆。厚重的褶皱水平延伸，在横杆处有轻微自然的下垂和堆叠。织物沉重，完全静止。

右侧，前景中胸口高度：一只透明的圆柱形玻璃杯立在右墙上，仿佛墙壁就是桌子。杯底贴着墙面，由一个小金属环形支架固定。杯口水平指向房间内部。玻璃杯以侧面轮廓呈现，在画面中大而清晰。

玻璃杯里装着琥珀色的茶。茶水完全充满杯子靠墙的一段，从杯子内侧上沿到内侧下沿，占杯长的一半多一点。盛茶的部分明显比空的部分长。杯子靠房间一侧、直到杯口的部分完全是空的，通透而干燥，下缘也是如此。琥珀色茶水与空气的分界是一条笔直的竖线，从杯子上沿贯通到下沿。它看起来就像一张普通茶杯立在桌上的照片，旋转 90 度，使杯底朝向右墙。沿着这条竖线有逼真的弯月面，琥珀色液体中有逼真的折射。

上方：一小盆垂蔓植物倒立在天花板上，花盆底部平贴天花板。它的藤蔓和叶片向上垂落，贴着天花板环绕花盆，就像桌上的垂蔓植物垂落到桌面上一样。没有藤蔓垂向房间里。这株植物比窗帘和玻璃杯更小、更不显眼。

右墙上、玻璃杯下方：整整三本精装书叠成一摞，以墙壁作为它们的地面。一本深绿色的书封面平贴在墙上。一本深红色的书叠在它上面，一本深蓝色的书叠在红书上面，朝向房间一侧。这摞书从墙面水平伸出，三本书的书脊都是竖直的。

光线：温暖的灯光，人物身上有柔和的定向主光，微弱的轮廓光，自然地衰减进阴影。所有阴影都遵循真实光源，包括那些侧向物体的阴影。自然的肤色，真实的材质，细腻的胶片对比度，自然的景深。图像中没有文字。
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

<details><summary><b>都市夜晚滨水人像</b> · 机器翻译</summary>

```text
主体与姿势:
一位年轻女性站在滨水步道的金属栏杆旁,双手扶着栏杆向后倚靠。她身体微微后仰,姿态放松。头转向左侧,闭着眼睛,带着柔和的浅浅微笑,神情平静而神秘。

技术说明:100% 精确保留参考面部照片中的面部特征和身份。不要改变脸型、鼻子、眉毛、嘴唇、眼睛或整体面部结构。

服装与配饰:
她穿着一件修身的黑色长袖上衣,深 V 领。下身是黑色迷你裙,装饰有两排银色链条腰带,其中一条带有心形吊饰。一只带银色链条肩带的黑色纹理肩包挂在她的左肩上。她戴着一条精致的细吊坠项链。

发型与妆容:
披散的头发,柔和的前额发丝自然垂落在脸颊和脖颈上。柔和的闪亮妆容,带有立体修容、透亮的肌肤、浓密修长的睫毛和亮泽的裸色嘴唇。

光线与镜头:
大腿以上取景,与视线齐平的角度,竖版 3:4 构图。仿佛使用 iPhone 16 Pro 在夜间以明亮的前置闪光灯拍摄,形成强烈对比:模特被明亮照亮,皮肤和金属链条上有亮泽的高光,而背景保持昏暗。

背景:
夜晚的大都市滨水区。她身后是深色的水面,倒映着对岸亮灯的摩天大楼和高层建筑的无数灯光。天空昏暗,淡淡的云层被城市灯光柔和地照亮。

氛围与美学:
都市夜晚美学,Y2K 风格,自信、优雅与神秘。一张在傍晚城市漫步中捕捉的写实抓拍照片。

超写实、高品质、锐利的 8K 照片。画幅比例 3:4。闭着眼睛。淡淡的浅笑。使用 iPhone 16 Pro 拍摄。
```

</details>

<details><summary><b>都市夜晚铁道人像</b> · 机器翻译</summary>

```text
一张竖版夜间照片，一位年轻女性站在户外，靠近铁路旁的金属楼梯。她皮肤白皙，棕色头发向后束成低马尾，几缕碎发垂在脸旁和额前，眉形清晰，神情严肃而若有所思。她身穿一件宽大的棕色皮革飞行员夹克，带有明显的拉链和罗纹袖口，里面是黑色圆领T恤，下身是一条褶裥橄榄绿军装风格短裙。她身体略微侧转站立，双臂交叉抱在胸前，望向画面左侧，避免与镜头对视。场景是铁轨附近的工业区：右侧是通往路堤的带白色栏杆的金属楼梯，背景中有金属接触网杆和铁路电气化结构，右上方有一个电气控制箱，左上方有一根高大的路灯杆。她身后的陡坡覆盖着绿草和泥土。夜空是深灰紫色。左上角路灯发出的强烈人造光产生轻微的镜头光晕，将硬朗的直射光投在她的脸和夹克上。略微低机位拍摄，美式镜头（七分身）构图。照片级真实，高细节，电影感灯光，忧郁的都市夜晚氛围，8k，杰作，最佳画质，超精细，锐利对焦。


Negative
Prompt:
cartoon, anime,
illustration, painting, drawing, 3d render, cgi, deformed, distorted,
bad anatomy, disfigured, poorly drawn face, mutation, mutated, extra
limb, ugly, poorly drawn hands, missing limb, floating limbs,
disconnected limbs, malformed hands, out of focus, extreme zoom,
absurd, blurry, wet, watermark, signature, text, username, artist
name, low quality, worst quality, normal quality, lowres, jpeg
artifacts, dead, out of frame, cropped, mutation, mutilated, out of
frame, extra fingers, too many fingers, cross-eyed, bad hands,
missing fingers, extra digit, fewer digits, cropped, worst quality,
low quality, normal quality, jpeg artifacts, signature, watermark,
username, blurry, artist name, monochrome, grayscale, duplicate,
morbid, mutilated, out of frame, extra toes, crossed eyes.

sd_xl_base_1.0.safetensors 或 Juggernaut XL v9
Resolution: 832x1216
(9:16 aspect ratio)
Steps: 30-40
Sampler: DPM++ 2M
Karras 或 Euler a
CFG Scale: 7-8
Clip Skip: 2 (SD 1.5 用) / 1 (SDXL 用)
Denoising Strength:
0.75 (使用 img2img 时)

IP-Adapter Weight:
0.6-0.8
IP-Adapter Model:
ip-adapter-plus_sd15.safetensors
Reference Image: 模特的原始图像

ControlNet Unit 0:
  Model:
control_v11p_sd15_openpose
  Preprocessor:
openpose_full
  Weight: 0.8-1.0
  Guidance Start:
0.0
  Guidance End: 1.0
  
ControlNet Unit 1
  Model:
control_v11f1p_sd15_depth
  Preprocessor:
depth_midas
Weight: 0.4-0.6
InstantID Weight:
0.8
IdentityNet Scale:
0.5-0.8
Preserve Face
Details: Enabled
add_detail.safetensors (Weight: 0.4-0.6)
epi_noiseoffset2.safetensors (Weight: 0.3-0.5)
cinematic_lighting.safetensors (Weight: 0.5)
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

<details><summary><b>都市明暗对照男士人像</b> · 机器翻译</summary>

```text
一张超写实的黑白人像照片,主角是一位二十出头、英俊健壮的年轻男子,有着蓬松卷曲、层次凌乱的浅棕色头发,下颌线分明,目光强烈地直视镜头,身穿一件紧身黑色短袖T恤,手臂和肩膀肌肉线条清晰,脖子上隐约可见一条细链项链。他背对镜头站立,身体转成四分之三侧面,越过左肩回望,双臂自信地交叉在胸前,右肩靠在质感粗犷的砖墙上。场景是都市小巷,两侧是饱经风霜的旧砖墙,昏暗多影的背景营造出纵深感和戏剧性的氛围。来自左侧的自然侧光形成高对比度,脸部是伦勃朗式的柔和照明,背景中有浓重的阴影,突出手臂和肩膀的肌肉线条。使用85mm人像镜头拍摄,腰部以上的中景,浅景深,背景略微虚化,主体位于画面右三分之一处,遵循三分法构图,平视机位。电影感的编辑时尚摄影风格,充满男性气质的忧郁美学,GQ杂志品质,戏剧性的明暗对比光线,专业影棚级黑白转换,主体对焦锐利,胶片颗粒质感,8K分辨率,照片级写实。
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

<details><summary><b>野花养蜂草地刺绣绷画</b> · 机器翻译</summary>

```text
一张特写照片，拍摄一件完成的手工刺绣绷圈艺术品，放在做旧的浅橡木桌上，画面是一片微缩的山坡草地和养蜂场景，用彩色棉线和丝线绣在天然亚麻布上。圆形木制绣绷内有：绿色缓坡上的三个白色小木蜂箱；用缎面绣分层绣成的起伏山丘，色调为鼠尾草绿、苔绿和橄榄绿；用褐色回针绣出的蜿蜒小路；以及满是野花的草地，花朵用法式结粒绣、雏菊绣和卷线结粒绣（bullion knot）绣成，颜色为薰衣草紫、毛茛黄、罂粟红和矢车菊蓝。用黄黑丝线绣成的小蜜蜂，带着半透明的欧根纱翅膀，悬停在花朵上方；一侧立着一棵小苹果树，结着打结绣成的红色果实；柔软的云朵用白色填充缎面绣绣成，漂浮在用劈针绣绣出的淡蓝色天空中。桌面上绣绷周围摆着：一把金色小鹳鸟造型的刺绣剪刀、一个木质线轴、几绞配色相符的散落绣线、一根拖着线的针，以及一小枝干薰衣草。柔和的漫射窗光从左侧照入，景深较浅，绣绷清晰锐利，道具则轻柔虚化，微距细节展现出凸起的线条质感、单根纤维和亚麻布的织纹。温暖、宁静、手作、田园风（cottagecore）的氛围，自然色彩，使用 100mm 微距镜头拍摄。无人物，无手，无文字，线上无品牌标签。方形 1:1 画幅，绣绷居中，并在右下角略微超出画面边缘。
```

</details>

<details><summary><b>金色时刻的湖畔陶艺工作室</b> · 机器翻译</summary>

```text
黄金时刻的雪松湖畔陶艺工作室与柴烧窑棚，从码头一侧拍摄的外景。风化的竖向雪松木板，低坡度金属屋顶，宽阔敞开的大门露出里面的两台拉坯机和晾坯架。一座小木码头伸入平静的湖水，湖面倒映着温暖的琥珀色光芒。工作室旁边是一座独立的窑棚，砖砌烟囱飘出一缕淡淡的轻烟。石径、成堆的柴火、室外架子上几件未完成的陶器，湖岸边有松树和桦树。柔和的长长阴影，雪松上泛着金色轮廓光，宁静的手工艺静修氛围。写实风格，横版 16:9。无人物，无文字，无汽车。
```

</details>

<details><summary><b>金色时刻的阳台小温室</b> · 机器翻译</summary>

```text
挂满红色和橙色樱桃番茄的番茄藤、垂落的罗勒、辣椒植株和草莓盆栽,填满了一座立在狭窄城市公寓阳台上的小型玻璃加黑钢靠墙温室,时间是黄金时刻。温室的门半开着;里面三层板条木架上摆着陶土花盆、冒出鲜绿嫩芽的育苗盘,还有一把小小的黄铜浇水壶。凝结的水珠挂在下层玻璃板上。温室外,阳台铺着风化的柚木地板,摆着一把折叠式小酒馆椅,黑色金属栏杆上缠着尚未点亮的灯串。栏杆之外,由砖砌公寓楼和屋顶组成的柔焦城市天际线沐浴在低斜的暖阳中。写实摄影,使用全画幅相机搭配 35mm 镜头,光圈 f/2.8,平视角度,浅景深,焦点对准番茄,自然的金色逆光在叶片和玻璃上形成轮廓光,质感和反光逼真。氛围平静、充满希望、有生活气息。无人物,无文字,无标志。
```

</details>

<details><summary><b>金色时刻耳机特写</b> · 机器翻译</summary>

```text
一张电影感、照片级写实的特写人像,主角是一位英俊的年轻男子,留着深色头发和修剪整齐的胡须。他戴着蓝色镜片的圆形金属框墨镜和大号头戴式耳机。他微微低头,神情若有所思。光线戏剧性且温暖,模仿黄金时刻的日落,强烈的阳光照在他脸的一侧,在另一侧形成浓重而忧郁的阴影(明暗对比效果)。背景昏暗并虚化,使焦点完全集中在主体上,9:16画幅比例。
```

</details>

<details><summary><b>金色时刻逆光侧脸</b> · 机器翻译</summary>

```text
主体：
照片中是一位年轻女性，头转向左侧呈侧面，脸上带着一丝几乎察觉不到的淡淡微笑。她的右手抬起，轻轻握着靠近发梢的一缕头发。

服饰与配饰：
这位女性身着全黑装扮。她穿着一件宽松的黑色衬衫或轻薄的超大号长袖夹克，塞进黑色下装里。腰间可见一条细黑色皮带，配有精致的银色带扣。肩上斜挎一个黑色单肩包，可见部分纤细的银色金属链条。

外貌、妆容与发型：
发型：笔直的头发自然披散。看起来很自然，被风吹出柔和的波浪。

妆容：非常自然的“素颜妆”风格。肌肤干净自然，眉毛修饰整齐，唇色为中性色调。

光线：
场景由柔和温暖的逆光照亮，是黄金时刻（日落或日出）的典型光线。阳光照亮这位女性的头发，形成明亮的金色轮廓光（光晕效果），凸显头发的质感和脸部的轮廓。她的脸处于柔和的阴影中，但仍然清晰自然地被照亮。

背景与氛围：
背景：一堵浓密的深绿色树叶墙——灌木和大叶树木。背景被压暗，与被照亮的女性身影形成深邃的对比。背景中的一些树叶也被金色的阳光轻轻照亮。

地点：看起来像是公园边缘或森林附近的一条土路。底部可见干草和小植物。前景中可见一部分混凝土路缘。

氛围：平静、若有所思、温暖而温馨。照片的情绪忧郁而浪漫。

拍摄角度与构图：
照片以视平线高度近距离拍摄，使用中景，取景从腰部到头顶。构图平衡，女性位于中央，目光望向画面之外。头发的质感和周围的绿植细节丰富。自然摄影风格，带有细微的胶片颗粒。

不要改变任何面部特征。保持精确的面部结构和 100% 的面部相似度。

竖版构图，3:4 宽高比。

写实、高质量、清晰的 8K 照片，使用 iPhone 16 Pro Max 拍摄。
```

</details>

<details><summary><b>钟表匠工作台银版照片</b> · 机器翻译</summary>

```text
一张古董钟表匠的工作台，台面上摆满打开的怀表、散落的黄铜齿轮、一个罩着骨架钟的小钟形玻璃罩、一只珠宝商放大镜、精细的镊子和一盏油灯，以 19 世纪 50 年代银版照相法（达盖尔式）拍摄。画面呈现在银镜般的铜板上，影调是冷调的银灰色，阴影深邃如天鹅绒，柔和明亮的高光如抛光金属般闪烁。齿轮的齿和雕刻的表芯细节极其精细，长时间曝光带来浅景深。光线从左侧的高窗柔和地洒下，照亮黄铜边缘和玻璃罩。工作台后方，一个带小抽屉的木质壁柜和几只悬挂的挂钟隐没在柔和的黑暗中。真实的银版瑕疵：边缘有淡淡的氧化晕圈、细微的旋涡痕迹、微小的灰尘斑点，最暗处带有轻微的蓝青铜色虹彩，外框是一圈带圆角的纤细华丽黄铜衬框。平静、安宁、永恒的氛围。宽幅横向 16:9。无人物，无手，无文字，无字母，无标志。
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

<details><summary><b>银河下的雪松观星小屋</b> · 机器翻译</summary>

```text
一座小小的雪松木屋,屋顶上有一个白色旋转式望远镜圆顶,坐落在岩石山脊上,绚丽的银河横跨夜空。木屋是紧凑的单层方盒造型,外墙覆以竖向暖棕色雪松板,顶部是低矮的深色金属单坡屋顶;左端是哑光白色半球形圆顶,狭长的天窗缝半开,隐约可见里面的望远镜筒;右端是黑色钢制烟囱,飘出一缕细细的烟。正面一扇宽大的矩形窗户透出昏暗的暖琥珀色光,一个带简易栏杆的小木露台朝向山谷。一条铺着平整石块镶边的狭窄碎石小径通向露台。矮松和残留的旧雪点缀在木屋四周,锯齿状的山脊剪影渐隐于远山环绕的深谷之中。数千颗锐利的星星,明亮的银河核心泛着柔和的紫色与金色。写实长曝光天文摄影,广角 16:9,低机位视角,无光污染,无人物,无文字。
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

<details><summary><b>阳光广场复古青绿餐车</b> · 机器翻译</summary>

```text
写实风格的生活方式摄影，拍的是一辆复古的 1960 年代风格紧凑型厢式餐车，停在阳光明媚的城市广场上，时间是工作日午餐时分；从前方右侧四分之三视角拍摄，相机位于站立的视线高度（1.6 米），距离约 9 米，使用 35mm 镜头，16:9 横向构图，整辆餐车完整入画，略偏画面中心右侧。固定设计细节：车身为短而方正的厢式车，长约 5.5 米，转角柔和圆润，车顶平坦；双色涂装，上半部为光亮的奶油色，下半部为深青绿色，中间隔着一道细细的铜橙色条纹，沿车身环绕一圈，高度与车窗下沿齐平；车头平整，有一块大的双片式挡风玻璃、两盏圆形镀铬大灯、一根简洁的镀铬水平格栅条和一个镀铬前保险杠；黑色轮胎配奶油色涂装的钢制车轮和小型镀铬轮毂盖。在右侧（顾客一侧，朝向相机）：一个大型长方形出餐窗口位于车身侧面正中，其上掀的青绿色面板由两根镀铬撑杆支起，充当遮阳篷，篷的底面涂成铜橙色；窗口底部沿线有一条拉丝不锈钢台面架，上面放着一小盆罗勒和一个装着柠檬的玻璃罐；窗口左侧靠近车头的位置，有一个圆形铜橙色徽标，图案是一轮简单的太阳下方衬着一株麦穗，不含任何字母；窗口右侧靠近车尾的位置，有一块素面深石板色菜单板，上面没有任何文字，只有三个小小的手绘白色图标，分别是一块薄饼面包、一个柠檬和一只玻璃杯。顾客一侧的车顶边缘上方沿线挂着一排暖色球形串灯（白天关闭）。车顶前部放着一个长长的木质种植箱，里面种着绿色香草，靠近车尾处有一个小小的圆形银色通风口。窗口前方的地面上：一个低矮的天然木质踏步平台，以及一个青绿色的 A 字形立牌，正面空白。广场地面铺着浅色石材，有梧桐树洒下斑驳树荫，几张咖啡桌，只在远处背景中有虚化的路人。明亮的正午阳光，柔和的斑驳阴影，清新友好的氛围，真实的油漆反光与金属质感，商业街头摄影。不要出现可读的文字，不要字母，不要数字，不要车牌字符，不要真实品牌标志，不要清晰对焦的人脸。
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

<details><summary><b>阴森小丑双人Cosplay</b> · 机器翻译</summary>

```text
一张内容丰富、氛围浓郁的竖版中景照片，画面中有两位身着精致服装的 cosplayer，置身于深邃的纯黑背景之前，营造出孤立与黑暗的感觉。

女性 cosplayer 背对着男子站立，回头越过肩膀直视镜头。她有一头长长的、波浪状的鲜亮铜红色头发，自由地披散在肩上。她的妆容是风格化的小丑妆——白色涂面、红色口红、眼周富有表现力的黑色线条和圆点，以及腮红——营造出既可怕又时尚的造型。她穿着一件白色束身衣款式上衣，前襟缀有红色绒球，呈露肩设计，搭配多层白色荷叶边裙。她握着一只飘在头顶上方的鲜红色氦气球的绳子。

紧贴在她身后、与她背靠背站立的是一位扮演 2017 年电影《小丑回魂》中潘尼怀斯的男性 cosplayer。他化着精细而诡异的潘尼怀斯妆容，白色的脸，独特的红色线条从嘴角穿过眼睛延伸到额头，咧着可怕的笑容，露出参差不齐的牙齿。他凌乱的红色潘尼怀斯发型向后向上梳起。他穿着经典的灰色维多利亚式小丑服装，领口和袖口有多层荷叶边，并装饰着红色绒球。他直视前方，显得严厉而充满威胁。

低强度、戏剧性、高对比度的光线，带有强烈的明暗对比阴影，突出服装和妆容的质感，同时让场景的其余部分沉入深深的阴影。光源位于前方并略高于被摄者。有限的色彩搭配：深黑、灰、白和鲜红。

黑暗、不祥、神秘而紧张的氛围。相机与视线齐平，竖版构图，聚焦于两个角色之间的互动与对比。高度细致、逼真的皮肤和织物质感。

不要改变参考图中女子的面部特征或身份。

Format: 3:4
写实、高品质、锐利的 8K 照片，使用 iPhone 16 Pro 拍摄。
```

</details>

<details><summary><b>阴郁都市摩天楼人像</b> · 机器翻译</summary>

```text
风格:带有电影感的写实城市街头摄影,用手机拍摄。

场景:一位年轻女性以现代摩天大楼为背景的肖像。

姿势与镜头角度:女性站在画面中央。镜头位于极低的角度,使她身后的摩天大楼显得巨大,并朝天空戏剧性地向上汇聚。女性低头看向镜头,神情略带优越感却平静。她的头微微向右倾斜。

服装:她穿着深灰色或黑色的宽松羽绒夹克(或运动夹克),内里为浅灰色、近乎银色,带有拉链。里面穿着黑色连帽衫,帽子罩在头上。

头发:松散的波浪发自然环绕着脸庞,发丝从帽子下方垂落。

妆容:自然而有轮廓感的妆容。轻薄的哑光底妆,用深色眼影微微勾勒眼睑轮廓。嘴唇涂着暗粉色或裸色的哑光口红。

氛围与情绪:氛围阴郁、都市化,略带神秘。情绪深沉、严肃而自信,传达出现代大都市的酷感。

光线:阴天里自然柔和的漫射日光。多云的天空在她脸上形成柔和的阴影,突出帽子下面部的轮廓结构。

背景:两座现代高层摩天大楼直接耸立在女性身后。左边的一座外立面颜色深暗,有许多方形窗户,右边的一座颜色较浅,可能带有混凝土或玻璃元素。两者之间可见灰色多云的天空。

技术细节:对焦清晰地落在女性的脸上。带有手机在弱光或阴天条件下拍摄特有的细微颗粒感。色彩柔和低调,以黑色、灰色和冷色调为主。竖版构图。

不要改变面部特征。精确保留参考照片中的面部特征和身份。

画幅比例 3:4。写实、高品质、锐利的 8K 照片。使用 iPhone 16 Pro 拍摄。
```

</details>

<details><summary><b>阿尔卑斯山自拍</b> · 机器翻译</summary>

```text
阿尔卑斯山中的写实 iPhone 自拍风格照片。晴朗明亮的白天，深蓝色天空，背景是险峻锋利的山峰，岩石山脊上有零星积雪。前景是开阔的绿色高山草甸，草木茂盛，细小的植物清晰可见。中景处有一座小木质山间小屋。女人仰面躺在草地上，姿态放松，用登山背包当枕头。镜头角度为手持、略高于她的位置，是典型的 iPhone 伸臂自拍视角，伸出的手臂带有轻微的广角畸变。她身穿运动风徒步装扮：轻便的 Arc’teryx 防风夹克（蓝色调）、合身的粉色运动短裤、Oakley 太阳镜，整体是休闲的越野氛围。身体姿态放松——一条腿微微弯曲，一只手臂伸向镜头握着手机。头下可见背包，登山装备细节真实。
```

</details>

<details><summary><b>阿尔卑斯湖畔金色时刻人像</b> · 机器翻译</summary>

```text
一张逼真的高质量 8K 照片,由 iPhone 16 Pro Max 拍摄,3:4 画幅。

构图与相机角度:平视中景,四分之三侧面。一位年轻女性站在一片山间湖泊旁,位置略微偏右。她的身体侧向一边,同时回头越过肩膀望向镜头,带着柔和自然的微笑。

主体与氛围:一位面带微笑的年轻女性,呈现放松、宁静的“granola girl”(户外自然系女孩)美学。她的双臂自然垂在身侧,手里拿着一个透明水瓶,垂在大腿旁。她的表情平静、温暖、毫不费力。

服装与配饰:她穿着一件短款宽松的 sherpa 羊羔绒夹克,上面是醒目的民族风几何图案,色调包括米色、锈棕色、蓝色和黑色。搭配黑色紧身裤,一条来自水瓶或小包的深色肩带斜跨过身体。

发型与妆容: 头发部分挽成凌乱的丸子头,几缕散发垂落在脸颊两侧和肩膀上。极简自然的“素颜妆”,肌肤清透真实。

光线与氛围:黄金时刻的阳光为整个场景披上温暖浓郁的色调。氛围宁静、充满冒险感、温馨,与自然深深相连。

背景:一片宁静的高山湖泊,倒映着身后拔地而起的壮观石灰岩悬崖。较低的山坡上覆盖着森林和生机勃勃的绿色高山草甸。天空湛蓝清澈,点缀着几朵柔和的云,对岸湖畔可见一些小小的人影。前景中出现野草和芦苇。

技术细节:深景深让女性和山景都保持清晰、细节丰富。照片级写实,超清晰,真实的皮肤质感。不要改变她的面部特征或身份。
```

</details>

<details><summary><b>阿尔卑斯缆车场景概念简报</b> · 机器翻译</summary>

```text
请扮演一位电影级场景设计师，撰写可直接用于生图和动画的场景简报。帮我设计一个主视觉镜头：一座单独的缆车车厢穿越积雪的山谷。这个镜头会先生成一张静态图，再以该图作为首帧制作成一段短视频。你的简报必须让静态图中包含丰富的、可自然运动的元素（车厢沿缆绳滑行、飘动的云、飘落或被风吹起的雪、烟囱的烟、闪烁的光、飞鸟），同时让构图保持平静、易于做动画。

我的初始选择：
- 山区与地貌：${region:Alpine valley with a small village and pine forest}
- 季节与时间：${season:winter sunrise}
- 车厢类型与颜色：${cabin:small vintage red aerial tram cabin with large windows}
- 视觉风格：${style:photoreal travel photography}
- 氛围词：${mood:crisp, quiet, golden, airy}

请先用一条简短的消息向我询问缺失的信息：我偏好的相机视角（从山脊俯瞰山谷、从下方仰视车厢，或从附近山坡与车厢平视）、是否需要让山谷站或山顶站入镜，以及需要避免的内容（人物、滑雪者、标志、标牌、滑雪缆车、现代建筑）。

然后按以下部分输出简报：

1. **场景概览**：两到三句话，描述地点、季节、光线以及这一刻的故事。

2. **缆车与缆绳**：车厢的形状、颜色、车窗布局、顶部吊架与行走小车、钢缆的数量和粗细、钢制格构塔架（在画面中的位置、高度、颜色），以及车厢的行进方向。说明车厢悬挂在缆绳下方并沿缆绳移动，绝不脱离缆绳。

3. **山谷与地貌**：山峰及其形状、积雪与岩石、松林密度、下方的村庄（房屋数量、屋顶颜色、教堂或木屋细节）、道路或结冰的溪流，以及从前景到背景的景深层次。

4. **光线与氛围**：太阳方向与颜色、山峰上的高山辉光、低云或山谷雾、空气中的细雪、烟囱的烟，以及光线如何照在车厢车窗和缆绳上。

5. **固定视觉细节**：一个编号列表，列出 8 到 10 条在静态图和视频中必须保持一致的细节（车厢颜色与位置、缆绳角度、塔架所在一侧、山峰形状、村庄位置、太阳所在一侧、云层高度、相机位置、构图取景）。

6. **运动图谱**：一张表，列出视频中所有可以运动的元素，列为：元素、运动类型、方向、速度（极慢、慢、中等）以及运动幅度强弱。包括相机运动。保持整体运动细微且符合物理规律。

7. **提示词种子 A - 主视觉静态图**：一条可直接粘贴使用的生图提示词，不超过 170 词，用于宽幅横向 16:9 画面，第一句话包含车厢、缆绳、塔架和积雪的山谷，结尾为：no people, no text, no signs, no logos。

8. **提示词种子 B - 图生视频动画**：一条可直接粘贴使用的视频提示词，不超过 120 词，以主视觉静态图作为首帧，描述一个缓慢的相机运动以及运动图谱中的自然运动，时长约 6 秒，并说明让车厢、缆绳、塔架、山峰和构图与图像中完全一致，不出现新物体。

规则：不以人物为主体，不出现文字、标牌或标志，不使用快速的相机运动或剪辑，不出现违背物理规律的运动（车厢沿缆绳以恒定的缓慢速度平稳移动，只有轻微摆动；云朝同一个风向飘移；烟随同一阵风弯曲）。使用短段落和列表。
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

<details><summary><b>陶瓷手冲咖啡套装主图</b> · 机器翻译</summary>

```text
哑光沙米色陶瓷手冲咖啡套装的产品主视觉照片:一个带螺纹的滤杯置于透明玻璃分享壶上,升起一缕细细的蒸汽,旁边是两只配套的无柄杯。摆放在奶油色灰泥墙前的磨光洞石台面上。道具:一只杯子下垫着折叠的亚麻餐巾、几颗烘焙咖啡豆、一枝橄榄枝。左侧是柔和的窗光主光,右侧是白色反光板补光,滤杯上有微弱的暖色轮廓光,哑光釉面呈现天鹅绒般的高光,柔和的阴影落向右侧。全画幅相机,85mm 镜头,f/5.6,对焦于滤杯杯沿,抬高的四分之三视角。色调:沙米色、奶油色、赤陶色、浓缩咖啡棕、橄榄绿。宁静、温暖、手作感的清晨氛围。产品位于画面左三分之一处,右侧留出干净的负空间用于放置标题,16:9。无标志,无文字,无手,无杂物。
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

<details><summary><b>雨中电话亭侦探黑色漫画</b> · 机器翻译</summary>

```text
一幅单格黑白黑色电影风格漫画分格,16:9 横向,外框是一圈细实线黑色分格边框,四周留有窄窄的白色间隙。夜晚,空无一人的城市街道上下着大雨。略偏右于画面中央,矗立着一座老式玻璃钢架电话亭,亭内灯光明亮如白昼,是场景中唯一强烈的光源。亭内,一名侦探身穿系着腰带、立起衣领的风衣,头戴压得很低的宽檐软呢帽,正把听筒贴在耳边,脸大部分隐在阴影中,只有下颌的线条和帽檐的边缘被白色勾勒出来;他空着的那只手平按在被雨水冲刷出痕迹的玻璃上。水沿着电话亭的玻璃窗流下,画成一道道水痕。左侧后方偏上,一块高高的竖直酒店招牌悬挂在砖砌建筑上,它发光的字母被简化成抽象的空白亮块,没有任何可辨认的文字,其灯光在前景湿漉漉的路面水洼中映成破碎的白色形状。雨被画成长长的斜向墨线,细密的网点网纹铺满天空、街道的阴影和湿润的路面。笔触和钢笔勾线硬朗而笃定:深沉的纯黑覆盖画面大部分区域,白色高光清晰锐利,砖墙和风衣褶皱上是羽化的排线,戏剧化的明暗对比,电话亭框架的长长阴影向观者方向延伸。左侧边缘有一辆停着的 1940 年代轿车,呈黑色剪影,一座消防梯沿建筑之字形向上攀爬。机位低,从街对面拍摄,略微倾斜,带有电影般的紧张感,是经典的 1940 至 1950 年代犯罪漫画风格,印在略带灰白色的纸上,带有淡淡的半色调颗粒。严格只用黑、白、灰色调。无对话气泡,无说明框,无音效,画面任何地方都没有可辨认的文字或字母,无签名,无水印。
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

<details><summary><b>雨夜东京小巷的霓虹锦鲤池</b> · 机器翻译</summary>

```text
夜晚下雨的东京小巷,日文霓虹招牌倒映在街道中嵌入的浅锦鲤池里,橙色与青色霓虹,湿漉漉的柏油路,雨伞,细柔的雨丝,电影剧照,浅景深,超精细的倒影,忧郁的氛围
```

</details>

<details><summary><b>雨夜集市面摊街拍</b> · 机器翻译</summary>

```text
一张写实风格的街头夜景照片,拍摄的是细雨中一处露天亚洲夜市里繁忙的面摊。画面中央,一位上了年纪的厨师身穿白色棉布围裙、头戴深色帽子,用一把长竹笊篱从冒着热气的大汤锅里捞起一团新鲜面条;浓浓的蒸汽升腾而起,在灯光中泛着光。面摊有一张饱经风霜的木质柜台,摆着叠放的陶瓷碗、成捆的小葱、辣椒罐,以及一块手绘菜单牌,上面的字迹模糊,无法辨认。成串的暖色钨丝灯泡和一顶红色帆布遮阳棚构成画面的框架;雨水从遮阳棚边缘滴落,形成明亮的雨线。前景中有两位顾客坐在低矮的塑料凳上,处于虚焦状态,其中一人端着一只碗,手握筷子。湿漉漉的路面倒映着邻近摊位的橙色、红色和青色灯光,形成长长的、闪烁的水洼倒影,背景里是灯笼和过往雨伞形成的柔和焦外光斑。氛围忧郁,有电影感和纪实感,对比度丰富,肤色自然,蒸汽和雨水的细节清晰可见。使用全画幅相机搭配 35mm 镜头拍摄,光圈 f/1.8,快门 1/125s,ISO 1600,手持拍摄,浅景深,带有轻微胶片颗粒,无可辨认的文字,无标志,无水印,16:9 横向构图。
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

<details><summary><b>雪地里蜷缩的北极狐</b> · 机器翻译</summary>

```text
一张写实风格的野生动物摄影作品,拍摄一只披着浓密纯白冬毛的北极狐,蜷成一团卧在新落的粉雪上,位于宽幅 16:9 画面的中央。它蓬松的白色尾巴绕过身体前方,盖住爪子,黑色的鼻子搭在尾巴上方。双眼半睁,乌黑而困倦,平静地望向镜头,小而圆的耳朵直立着,几片细小的雪花落在浓密的皮毛上。狐狸躺在雪中一个柔软的凹坑里,以贴近地面的低位平视角度拍摄。它身后,广阔的雪原苔原在柔和的蓝调时刻光线下渐渐虚化成奶油般的柔焦,起伏的雪丘平缓,远处地平线上有一道细细的粉色光带,上方是淡淡的薰衣草色天空。长焦镜头,浅景深,焦点清晰地落在脸部和皮毛质感上,冷调的蓝白色中带一点粉色,色彩自然,氛围安静平和。无文字,无水印,无人物。
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

<details><summary><b>雪松树屋冬夜右前视角</b> · 机器翻译</summary>

```text
写实建筑摄影：与第 2 步中相同的小型雪松树屋小屋和老橡树，现在是飘雪冬日傍晚的蓝调时刻，从草地上的前右方而不是左方拍摄，相机处于站立视线高度（1.6 米），距离约 14 米，35mm 镜头，垂直线保持笔直，16:9 横向构图，橡树树干和整座小屋都在画面内。所有固定设计细节与第 2 步保持一致。宿主树：一棵巨大的古老橡树，树干粗壮，灰色，纹理深裂，宽大的板状根向地面四周展开，分成数根粗大的枝干，弧形伸展于小屋屋顶之上；它现在位于画面左侧，完全光秃，深色的枝条上覆着新雪，衬着深蓝色的天空。小屋紧挨树干，位于其右侧，建在一块低矮的木露台上，露台由短小的方形木立柱抬高约 0.6 米。小屋：一间紧凑的、两层楼高的单一房间，外墙为竖向雪松板，呈明亮的蜜糖棕色，屋顶是陡峭的双坡屋顶，覆以深绿色直立锁缝金属板，屋面坡上有一个小型深色盒式通风口，此刻覆着一层松软的积雪；山墙一端朝向右侧的相机，是朴素的竖向雪松板，配一条窄窄的绿色檐板。长边墙现在以斜角出现在左侧，有一排深色框的落地大玻璃窗和一扇玻璃门，全部从室内透出温暖的琥珀色光芒。木露台环绕正面和山墙一侧，配有简单的木栏杆，由方形立柱和细竖向栏杆条构成，顶部横杆上积着雪，露台上有一把木板条躺椅，落着薄薄的雪。一段宽阔笔直的木楼梯，配有相匹配的栏杆，从露台前右角下到草地，现位于右侧前景，踏步上覆盖着新雪，留有一行脚印。暖色球形串灯沿露台栏杆悬挂，发着光。树根处：平滑的积雪覆盖草地和橡树根部四周，身后是光秃的落叶林，渐隐于蓝色暮色中。雪地上冷色的蓝调时刻光线，与窗户和串灯的暖琥珀色光交融。色板为蜜糖雪松色、深绿色、炭黑色窗框、橡树灰、暖琥珀色和雪白色。真实的木头、金属、玻璃、树皮和雪的质感，建筑杂志摄影，宁静的氛围。无人物，无文字，无标志，无招牌。
```

</details>

<details><summary><b>雪松观星小屋温暖室内</b> · 机器翻译</summary>

```text
夜晚一座小型雪松天文台木屋的室内:墙壁和天花板是与外墙一致的暖色竖向雪松板,一张木书桌上摊开着星图,摆着一盏发红光的台灯,望远镜目镜和黑色望远镜筒斜向上穿过天花板舱口,伸入上方白色半球形圆顶,还有一个小型黑色铸铁木柴炉,透出橙色火光,配一根黑色钢制烟囱。一把磨旧的皮扶手椅铺着羊毛毯,放在书桌和炉子之间;墙上的搁架摆着目镜盒和一个黄铜星座仪。镜头站在室内,朝向两扇从室内透出琥珀色光的矩形前窗,窗外框出锯齿状的山脊、矮松、旧雪和明亮的银河。光线混合了昏暗的红色工作灯和温暖的炉火光;窗户显得偏冷且更暗。写实室内摄影,24mm 镜头,16:9,舒适而安静,无人物,无文字。
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

<details><summary><b>霓虹涂鸦爱意文字标志</b> · 机器翻译</summary>

```text
创作一个可爱、未来感十足、充满泡泡感的涂鸦文字标志,文字为“I love you Bris”。上方的单词为珠光白银色,下方的单词为亮霓虹粉色。使用深紫色描边,并带有发光的粉色边缘。在文字背后添加全息蝴蝶、像素爱心、星星、泡泡、闪粉颗粒、铬金属水滴和未来感液体飞溅。让字母显得厚实、柔软、膨胀且有光泽,呈现奢华的铬凝胶质感。将其置于干净的白色背景上。
```

</details>

<details><summary><b>霓虹酒吧欢笑抓拍</b> · 机器翻译</summary>

```text
一张抓拍的夜间随性照片,主角是一位二十出头的年轻女性,身材纤细,留着深棕色长直发,身穿黑色皮质机车夹克。她坐在热闹酒吧的桌边,身体前倾,头歪向一侧,双眼紧闭,发自内心地大笑,露齿而笑,笑容灿烂欢快,右手抬到脸旁,在嘴边拿着一根黑色吸管,动作俏皮。近景处是两只大号圆形玻璃高脚杯,盛着橙黄色鸡尾酒(米歇拉达风格饮品),杯中有大量冰块、橙子片和黑色吸管,旁边还露出半罐黄色饮料罐。背景是休闲的酒吧内部,有浅色木板墙、悬挂的爱迪生灯泡、鲜艳的紫色、粉色和蓝色 LED 霓虹灯,后墙上有一块带西班牙语文字的蓝色霓虹招牌,柔和虚化的背景里有两名男子坐在桌边。光线为混合光:智能手机正面直射闪光灯照亮她的脸,并在皮夹克和玻璃杯上形成镜面高光,与背景中紫色、粉色和蓝色的环境霓虹灯形成对比。使用智能手机摄像头拍摄,等效 24mm 镜头,f/1.8,平视近距离特写角度,中近景竖构图,浅景深,背景虚化出散景,可见数码噪点和闪光灯摄影质感,随性抓拍风格,色彩鲜艳饱和,姐妹夜出游氛围,拉丁美洲现代酒吧气氛,2020 年代 Instagram 快拍美学,欢乐而自然的情绪。
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

<details><summary><b>青柠绿手持小风扇人像</b> · 机器翻译</summary>

```text
一位20岁的成年美国女模特，肤色白皙，留着短羽毛状短发，耳周发层轻盈，头顶刻意蓬乱。她穿着一件半透明的青柠绿不对称上衣，在下巴正下方举着一把小巧的手持风扇，让刘海和短发层戏剧性地向上飞扬。紧凑的中景人像，闭着眼睛，带着淡淡的微笑，干净的钴蓝色摄影棚，相机直闪搭配柔和的侧向补光，青柠绿、钴蓝与自然肤色的调色，定格的头发动态，清晰锐利的编辑级质感，俏皮的奢华广告大片气息，极简背景，无文字，无标志。
```

</details>

<details><summary><b>静奢风泳池生活大片</b> · 机器翻译</summary>

```text
风格:生活方式博客或时尚杂志的专业拍摄。美学:“老钱风”和“静奢风”。

相机角度:从略高的视角俯拍,展现女孩的全身、泳圈和游泳池。

地点:豪华别墅或度假区。背景中:一个池水清澈、呈碧绿色的游泳池,石质池沿,热带植物(棕榈树),以及一把时尚的黄白条纹遮阳伞。

光线:明亮的直射阳光。泳池底部可见焦散光(水面反光)。阴影柔和而深邃,突出身体轮廓和质感。

主体与姿势:
模特:肤色晒成小麦色的年轻女子。头发披散,带有柔和的海滩卷发。
姿势:她放松地躺在泳池中央的充气泳圈上。双腿伸直,脚踝交叉。双臂随意地搭在泳圈两侧。头部微微抬起朝向阳光,目光向上或看向一侧。

配饰:经典的细框窄款深色墨镜、手腕上一条优雅的金手链,以及极简风格的戒指。

服装与细节:
泳衣:极简风格的连体泳衣。配色:白色底色,肩带、领口和髋部线条配以对比鲜明的巧克力棕色滚边。高开衩腿部设计。

主要道具(已更新):一个大号充气西瓜造型的游泳圈。内圈是亮粉色,带黑色瓜子,外缘(瓜皮)是深绿色,带有较浅的条纹。质感逼真,在阳光下带有轻微的光泽。

AI技术参数:
画质:8K,超高清,照片级写实。
相机:Sony Alpha A7R IV,35mm f/1.8镜头。
调色:自然色调,高饱和的碧绿色和绿色水面,温暖的肤色。“iPhone写实照片”效果,皮肤上有超精细的水珠。

不要改变面部特征。

画幅比例:3:4

超写实,高质量,锐利的8K照片。

构图:稍近的景别。
```

</details>

<details><summary><b>静奢风秋日时尚人像</b> · 机器翻译</summary>

```text
不要改变女孩的面部特征、眼型、眉毛、鼻子或嘴唇。保持 100% 的面部相似度。

画幅比例：3:4。超写实、高质量、锐利的 8K 照片，使用 iPhone 16 Pro Max 拍摄。

主体与构图：
一张四分之三身的人像（从头顶到靴子下方）。女性是画面的中心主体，坐在一座优雅的秋日城市公园里的浅灰色石质台沿上。构图为竖构图，模特占据画面大部分，柔和虚化的背景营造出纵深感。

拍摄角度：
平视视角，带有轻微的对角线构图。相机位于约 2-3 米远的位置，采用自然的人像镜头效果（约 50-85mm）。浅景深使面部、毛衣和双腿保持清晰，背景则融化成奶油般的焦外虚化。

姿势：
她侧身坐在石质台沿上，姿态放松。一条腿优雅地交叠在另一条腿上，形成优美的女性剪影。她的左手自然地放在身旁的台沿上，手指微微弯曲，另一只手臂则柔和地隐没在宽松的毛衣里。她的头部向下并略微偏向一侧，目光看向自己的腿上而不是镜头，营造出抓拍的、未经摆拍的感觉。

表情：
柔和、平静、内省的表情，嘴唇放松，眼睛半垂。氛围显得若有所思、温馨，带着安静的浪漫感，而不是微笑。

头发：
带有微妙暖色光泽的丝滑头发。头发笔直，发尾带有轻微的自然弯曲。一阵轻柔的秋风将几缕发丝吹过脸的一侧，部分遮住一只眼睛，呈现出毫不费力的电影感。

妆容：
自然的清透少女妆。淡淡的棕色眼影、精致的眼线、自然的睫毛、柔和的修容，以及不带唇彩的裸粉色嘴唇。

服装：
宽松的炭黑色针织毛衣，长袖遮住部分双手。象牙白色短款缎面半身裙，裙摆饰有精致的花卉蕾丝。白色罗纹中筒袜。黑色哑光皮革过膝靴，配厚底松糕鞋底。短款亮面深红色美甲。

光线：
带有温暖金色调的自然阴天秋日光线。光线柔和、漫射、显美，没有强烈的阴影。头发和双腿上有柔和的高光，同时保持温馨的电影氛围。

背景：
初秋的优雅城市公园。金橙色和柔和的绿色树木、柔软虚化的树叶、一张模糊的木长椅和石质建筑依稀可见但处于焦外。环境显得宁静、简约、奢华。

色彩搭配：
巧克力棕、炭黑、象牙白、暖米色石材、金琥珀色、焦橙色和柔和的橄榄绿。

氛围与美学：
静奢风、Pinterest 美学、电影感秋日大片、温馨、女性化、精致、抓拍感、情感温暖、高端生活方式摄影。

负面提示词：
不要微笑，不要露齿，不要配饰，不要手提包，不要珠宝首饰，不要文字，不要水印，不要多余的人物，不要扭曲的人体结构，不要 AI 瑕疵，不要过饱和的色彩。
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

<details><summary><b>静谧黑白针织人像</b> · 机器翻译</summary>

```text
艺术黑白摄影

一张具有电影感、女性化肖像风格的艺术黑白照片,使用中画幅胶片相机拍摄,带有细腻的颗粒,为画面增添自然的质感与层次。

主体与姿态

一位身形优雅的年轻女性,以四分之三角度在动态中被拍摄,营造出轻盈而灵动的感觉。她站立着,头部微微向前并向一侧倾斜,目光若有所思地低垂,让她的神态带有亲密而内省的气质。

她的左臂抬起,轻轻触碰脑后的头发,手指微微埋入发丝之间。她的右臂沿着身体放松垂下,手指随意地聚拢或拉扯着臀部位置的裙料,形成自然的褶皱,并露出膝盖以上一小部分大腿。她的身形构成一道优美的 S 形曲线,强调流畅与优雅。

服装

这位女性身穿一条合身的浅色(白色或奶油色)罗纹或针织中长/长款连衣裙,紧贴身形,勾勒出她的轮廓。裙子采用不对称的精致剪裁:左肩完全裸露,右肩则被遮盖。

长长的带纹理袖子,袖口宽松且略带褶皱,部分遮住她的手掌。面料轻薄柔软,带有细微的罗纹质感,能很好地捕捉光影,在腰部、臀部和袖子周围形成许多精致的褶皱与垂坠。

发型与妆容

女性的头发自然蓬松、松散披落。右侧的几缕发丝被风或动作带起,朝左侧动感地飘动,为照片增添轻盈与随性之感。她的左手轻轻将另一侧的头发按住。

她的妆容自然,几乎不易察觉(裸妆),突出柔和清晰的眉形、眼睑上自然的阴影以及淡淡的唇部轮廓。她的面容清新,没有明显的浓妆,凸显天然之美。

光线与氛围

柔和、自然、漫射的侧光,仿佛来自窗户或位于左上方的柔光箱,轻柔地洒在她的脸部、肩膀和身形上,在光与影之间形成细腻的过渡(明暗对照)。

阴影柔和、对比度低,突出她身体的曲线、面料的质感以及一缕缕发丝。背景是简洁的中性灰色墙面,没有分散注意力的细节,并通过细微的暗角在画面边缘略微变暗。

整体氛围忧郁、亲密、宁静而富有感性。

相机角度与构图

照片从中等距离拍摄,取景大约从膝盖向上(美式镜头),相机位置略低于胸部或与胸部大致齐平,使她的身形更具表现力。

画面为竖构图,女性位于画面中央。浅景深和柔和的焦外虚化使背景轻柔模糊,将所有注意力引向女性的情感表达和优雅的肢体语言。

黑白色调的自然对比突出了质感、形态和轮廓。

面部身份:完全保留这位女性原有的面部特征和身份。不要改变她的面部,也不要改变她的面部比例。

宽高比:3:4。

图像质量:写实、高质量、清晰、超精细的 8K 照片,使用 iPhone 16 Pro 拍摄。自然的皮肤质感、逼真的面料细节、细腻的胶片颗粒以及真实的黑白色调。
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

<details><summary><b>顽皮小丑魅力人像</b> · 机器翻译</summary>

```text
主体与相机角度：一位年轻女性的特写肖像，以略微抬高的视角在视线高度拍摄，类似亲密的自拍。她直视镜头。

妆容：灵感来自杰瑞德·莱托（Jared Leto）版小丑的华丽万圣节妆容。鲜艳的绿调眉毛，其中一侧眉毛上方有几处淡淡的手写黑色"HAHA"字样。深紫色烟熏眼影，闪烁着亮片，右眼上下延伸出一条细细的竖向紫色亮片线，睫毛又长又浓密、乌黑。

嘴唇：丰满的嘴唇，从黑色轮廓向鲜红色中心渐变。一条细细的深色线条从嘴角右侧延伸而出，灵感来自小丑的切尔西笑容（Chelsea smile）。嘴唇完全闭合，不露牙齿。

颈部细节：颈部一侧有一小簇粗糙的手写黑色"HAHA"字样，小而不张扬，略微偏离中心。极简、随性，灵感来自杰瑞德·莱托版小丑的纹身。

头发：完全保留参考照片中原本的发色，包括其自然色调和颜色分布。在现有颜色的基础上增添并丰富一层淡淡的、鲜艳的青柠绿色调，使其呈现更加鲜活、有光泽的绿色质感，同时仍以原发色为基础。效果应当自然逼真，不做完全染色，不出现人工的纯绿色效果，不改变原本的发型、发根或挑染。

服装与配饰：一件闪亮的紫色缎面束身上衣，细肩带，深领口；一条醒目的三层金链项链和粗大的金色圈形耳环。

姿势与表情：头部微微倾斜，放松的肩膀轻轻向后展开，嘴唇完全闭合。俏皮、挑逗、自信、淘气而叛逆的表情。

光线：柔和的定向正面光，类似环形灯或相机闪光灯，辅以淡淡的深绿色和紫色环境光。突出面部特征、闪亮的妆容、头发中增强的绿色调、金色首饰、锁骨和缎面质感。

背景：完全黑暗，近乎纯黑，带有淡淡的深绿色和紫色灯光。没有家具、门、走廊或任何可见的室内细节。

氛围：大胆、华丽、魅惑、淘气、叛逆，带一点癫狂。受《自杀小队》中杰瑞德·莱托版小丑启发的暗黑万圣节美学。

面部保留：完全保留参考照片中的面部特征、身份、面部结构、比例和自然外观。不要重塑或改变面部。

画质：超写实 8K 摄影，细节锐利，自然的皮肤纹理和毛孔，真实的发丝，没有塑料感或人工 AI 痕迹。用 iPhone 16 Pro 拍摄。

画幅比例：竖版 3:4。
```

</details>

<details><summary><b>预制烧烤商用厨房模型</b></summary>

```text
创建一个预制厨房模型，并包含与尺寸为10英尺x15英尺的烧烤区域相关的全套设备
```

</details>

<details><summary><b>领袖峰会海报</b> · 机器翻译</summary>

```text
参照另一张有女士的传单的版式，制作一张领袖峰会（leadership summit）的传单，用男士形象替换女士的照片，并使用带有太阳和老鹰的徽标。事工名称是 CYPRUS REVIVAL HUB，

正文或文案是：LEADERSHIP SUMMIT with Ejim Vincent Chidera(Set Man)，请注意 Set Man 应当放在下面

三大支柱按此顺序为：Fellowship、Discipleship、Leadership，

日期是 2026 年 9 月 25 日和 26 日，

地点是 Google Meet（使用 Google Meet 的徽标），

时间：塞浦路斯时间晚上 10:30，尼日利亚时间晚上 8:30，
```

</details>

<details><summary><b>颓废复古镜前自拍</b> · 机器翻译</summary>

```text
超写实生活方式镜前自拍摄影,一位年轻女性站在镜子前,右手拿手机拍照,左臂自然垂放在身侧,身体微微侧转。她看着手机屏幕,脸部被部分遮住。她穿着一件宽松的黑色T恤,印有褪色的复古Nirvana乐队图案,在侧面打了个结;配黑色蕾丝过膝长袜,袜口缀有精致的蝴蝶结;脖子上戴着带金属环的黑色皮革项圈。图形感飞翼眼线,带狐狸眼效果,淡淡的面部修容,黑色口红。蓬松的造型发,大波浪,吹风造型。大号圈形耳环、链条手链、镶石戒指,深色美甲,指尖尖锐。可见的纹身:前臂上的一把匕首,手和手指上的小图案。背景:浴室镜子、浅色的门、门把手、浅色石材台面。温暖柔和的室内光线,阴影均匀,浅景深,50mm镜头,胶片颗粒,高细节,8k。超写实的皮肤质感,毛孔清晰可见,自然的皮肤瑕疵,无修图,无塑料感,未修饰,自然的皮肤细节。复古胶片滤镜,低饱和暖色调,褪色对比度,哑光质感,细微颗粒,暗角,压暗曝光,低调氛围光。 --ar 4:5 --style raw --v 6.0 --cref [ссылка на ваше фото] --cw 20
```

</details>

<details><summary><b>风暴中的灯塔厨房油画</b> · 机器翻译</summary>

```text
一幅用浓郁油彩绘制的灯塔守护人的厨房,温暖而充满生活气息,屋外风暴肆虐。厚重的厚涂笔触描绘出刷白的石墙、一张沉重的木桌和冒着热气的黄铜水壶、一盏洒下琥珀色光芒的油灯,以及磨损砧板上的一条面包。雨水在小格子窗上划出道道水痕;透过玻璃,可见深灰色的大海和白色的浪花。湿漉漉的黄色油布雨衣和橡胶靴挂在门边滴着水。铜锅和一只搪瓷杯放在开放式搁架上。室内温馨的暖意与窗边冰冷的风暴光线形成对比。可见笔触,色调为柔和的赭色与深蓝色,带有轻微的清漆光泽。无人物,无文字,无现代电器。
```

</details>

<details><summary><b>风暴中的纸艺灯塔</b> · 机器翻译</summary>

```text
一个手工纸艺立体模型,表现风雨交加的夜晚,一座孤零零的灯塔矗立在岩石悬崖上。所有元素都由层叠、裁剪和折叠的纸张制成:${sea_color:deep teal}色的纸浪拍打着岩石,带有可见纤维的卡纸云层,一座红白条纹的小巧纸灯塔,灯光透过半透明的硫酸纸散发出温暖的黄色光芒。柔和的轮廓光,层与层之间细腻的纸张阴影,浅景深,微距摄影质感,电影感构图,灯塔位于画面右三分之一处,${aspect_ratio:16:9}。
```

</details>

<details><summary><b>飞剪船与海蛇骨雕画</b> · 机器翻译</summary>

```text
一幅宽幅的鲸骨雕刻（scrimshaw）风格版画，画中一艘三桅快帆船张满风帆，在巨大的风暴浪涛中搏击，一条盘绕的长长海蛇从右侧船边的海面升起。帆船顶着涌浪倾斜前行，每一面帆都鼓满了风，索具、船体木板和炮窗都刻画得十分精细，桅杆顶端飘着一面小三角旗。长满鳞片的海蛇高高弓起脖颈，身体在水面上下盘绕，背脊上排列着尖刺状的冠。画面下半部分是卷曲的浪涛，浪尖泛着白色泡沫，暗沉的风暴云在天空翻滚，右侧一道锯齿状的闪电劈下，小海鸟在桅杆上方盘旋。所有内容都用细密的黑色手工刻线绘制，带有交叉排线和点刻，三角旗和海蛇的冠上点缀一抹褪色的红墨。画板是温暖的奶油色，略微泛黄的抛光骨面，带有细微的纹理、细小的划痕和颜色较深的老旧边缘。一圈绞索纹边框围住画面，左下角有一个罗盘玫瑰图案。具有 19 世纪古董水手民间艺术的风貌，细节丰富。宽幅横向 16:9。无文字，无字母，无签名。
```

</details>

<details><summary><b>餐车概念设计简报</b> · 机器翻译</summary>

```text
请你担任餐车概念设计师、品牌设计师和视觉化艺术总监。我会描述我想做的街头美食生意。你要把它变成一份清晰的餐车概念：车辆、外观设计、服务动线布局和品牌视觉，并附上一份固定设计细节清单，以及两条可直接使用的图像提示词。这两条提示词要在两个不同的时间、从两个不同的视角呈现同一辆餐车，使两张 AI 图像看起来像是同一辆真实车辆的照片。

Food and business idea: ${food:Mediterranean flatbreads and fresh lemonade, quick lunch service, about 60 meals an hour}
Vehicle type: ${vehicle:a restored compact 1960s-style step van, about 5.5 m long}
Where it will trade: ${location:city plazas at lunch on weekdays, riverside night markets on weekends}
Brand personality: ${personality:sunny, friendly, a little retro, clean and trustworthy}
Colors I like or dislike: ${colors:like teal, cream, and copper; avoid red and yellow fast-food colors}
Must have: ${must_have:a large serving hatch with an awning, a small menu board, string lights for evenings, space for a queue}
Budget level: ${budget:modest, a used van with a professional fit-out and a hand-painted look}
View A: ${view_a:sunny weekday lunchtime in a city plaza with plane trees, front right three-quarter view}
View B: ${view_b:evening service at a riverside night market, lights on, rear right three-quarter view}

请输出：

1. 概念
   - 餐车名称创意（仅供我自己使用，不会出现在图像中），以及两句话的故事，说明顾客应当如何感受这辆餐车。
   - 车辆与外观：车身造型、配色方案及每种颜色的位置、车轮与镀铬细节、车顶细节，以及作为简单无文字符号的徽标。
   - 服务侧布局：出餐窗口的尺寸与位置、遮阳篷、台面、菜单板、取餐点、付款点、排队方向和灯光，均从顾客一侧描述。
   - 色板：6 种有名称的颜色（使用“深青绿”或“铜橙色”这类简单名称）及各自的使用位置。
   - 材质与表面处理：油漆质感、不锈钢、木材、织物和灯具。

2. 固定设计细节（一致性清单）
   一份编号列表，包含 12 到 16 条在每张图像中都必须完全一致的细节：车身造型与比例、油漆分色与条纹、车头细节（大灯、格栅、保险杠）、车轮、出餐窗口与遮阳篷及其精确位置、菜单板、徽标及其所在位置、车顶物品、灯具、后窗与后门，以及地面上的任何道具，每一项都要给出精确位置。每条都写成图像生成器能够照做的简短具体短语（例如“车身右侧、前门后方，一个铜橙色圆形徽标，图案为太阳下方衬着一株麦穗”）。

3. 图像提示词 A：基准视角
   一条面向 AI 图像生成器的详细提示词：从视角 A 的位置拍摄这辆餐车的写实摄影，采用视角 A 的光线和场景。包含从该位置可见的每一个固定细节，并放在正确的位置（左右以相机视角为准），还要写明相机高度与镜头、光线、氛围，以及 16:9 横向构图。结尾列出排除项（不要出现清晰可辨的人脸，不要出现可读文字，不要出现真实品牌的标志）。

4. 图像提示词 B：第二视角
   一条针对视角 B 的详细提示词，要按照一个无法看到图 A 的纯文本图像生成器来写：用完整的文字重新陈述所有固定细节（绝不能写“同前”），并按新的相机位置把每一项放在正确的位置，描述新出现的可见部分（例如后门和后窗），并且只改变时间、场景和光线。油漆、比例、徽标和道具保持完全一致。

5. 一致性检查清单
   十个是/否检查项，用于对照图 B 与图 A（例如“奶油色与青绿色之间的条纹是否仍为铜橙色，且高度相同？”）。

6. 实用说明
   一份简短清单，涵盖：按所述每小时出餐量设计的出餐窗口后方厨房布局、通风与燃气或电力供应、水箱、需要在当地核查的许可和食品安全检查、大致的改装预算分配，以及三种在不损害外观的前提下节省开支的方法。

规则：
- 方案必须能在所述车辆和预算下实际造出来；凡是不现实或不安全的地方都要指出。
- 使用朴素的颜色名称和具体的形状；不要单独使用“有趣”或“现代”这类含糊的词。
- 图像提示词中，车上任何位置都不得出现可读的文字、字母或数字：菜单板保持空白，或只显示简单的手绘食物图标；品牌只以无文字的符号呈现。
- 不使用品牌名称，不出现真实人物，不使用受版权保护的角色。
- 如果我的描述缺少关键信息，请做出合理假设，并在开头列出这些假设。
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

<details><summary><b>黄昏沙漠天文台水粉插画</b> · 机器翻译</summary>

```text
一幅二十世纪中叶现代风格的水粉插画，描绘黄昏时分红岩沙漠中一座位于山顶的小型天文台，采用 16:9 宽幅横向构图，以平涂、不透明的水粉绘制，带有可见的笔触肌理和略显粉质的哑光色彩。画面中央偏右、一处平坦的台地顶上，矗立着一座白色的天文台建筑，顶部是圆形银灰色穹顶，狭长的观测缝隙敞开，隐约可见一根望远镜镜筒指向天空；旁边是一座低矮的长方形砌块建筑，有一扇亮着暖黄色灯光的窗户和一根小型无线电天线。一条细细的蜿蜒道路，以简单的白色虚线标出，从左下方起以松散的之字形盘绕上台地。下方的沙漠由层层叠叠的平面形状构成：赤陶色和锈橙色的台地、一带尘土粉色的悬崖、赭色的沙丘，以及圆形的鼠尾草绿灌木，左侧前景还有几棵高大的类似巨柱仙人掌的剪影。天空是平滑的渐变，从顶部的深青绿和靛蓝过渡到地平线处温暖的杏色和珊瑚色，散布着小小的四角星、一弯纤细的新月，以及用柔和的干笔点彩表现的一道淡淡的银河。长长的紫色影子横过沙地。配色有限，仅用青绿、靛蓝、珊瑚、锈红、赭色、奶油色和鼠尾草绿，几何形状简化，边缘干净，带一点手绘的轻微抖动，纸张纹理细腻，具有 1960 年代科普书插画或国家公园海报的观感，但不含任何文字。氛围平静、乐观、充满惊奇。不要出现人物，不要文字，不要字母，不要标志，不要边框，不要水印。
```

</details>

<details><summary><b>黄昏沙漠驿站与骆驼商队</b> · 机器翻译</summary>

```text
黄昏时分,一座古老的方形砂岩商队驿站矗立在广阔的沙漠中,一队五头骆驼载着端坐的骑手正朝它的大门走去。城堡占据画面中右部:一道带垛口的城墙,墙上开着小小的狭长窗,两侧是两座带垛口的圆形角塔;正中是一座高大的尖拱马蹄形门洞,通向庭院中被暖光照亮的内拱廊,门两侧的墙上各挂着一盏小小的发光灯笼。左侧,五头载着骑手的骆驼排成单列,沿着起伏的沙纹向右走向门洞,长长的影子在身旁拉伸。右侧靠近右塔的位置长着三棵棕榈树:两棵高大的棕榈紧靠塔身,另一棵较矮的棕榈在更右边。天空在左下方地平线处泛着深橙色和桃色的光,向上渐变为紫罗兰色和靛蓝色,点缀着初现的星星,左侧有几缕细长的条状云。低矮的沙丘在两侧勾勒出地平线。前景是一大片被风吹出波纹的沙地,城墙附近散布着几丛稀疏的干灌木。写实电影感的旅行摄影,黄昏转入夜晚,氛围平静安宁。宽幅横向 16:9。不要人物面部特写,不要文字,不要标牌,不要标志。
```

</details>

<details><summary><b>黄昏灯笼古镇河景</b> · 机器翻译</summary>

```text
一条平静的河流在蓝调时刻穿过越南历史古镇，深色的水面上布满发光的漂浮纸灯笼，一艘载着灯笼的小木划艇在前景中缓缓滑行。左岸矗立着一排黄赭色的两层店屋，配深色木百叶窗和赤陶瓦屋顶，前面是一条长长的河边步道和低矮的石砌河堤，摆着咖啡桌，还有几个漫步的小小人影；一串串发光的红、橙、黄圆形丝绸灯笼悬挂在店面的屋檐下。中央远景处，一座木制拱形人行桥横跨河面，桥顶有一座带瓦的小型宝塔式屋顶亭子，被灯笼照亮，拱形倒映在水中。右侧远岸有更多低矮的建筑，远处的步道上有一排灯笼。许多发着红、橙、黄、白光的小方形纸灯笼漂浮在平静的水面上，从左侧前景一直分布到桥边，每一盏都拖着一道长长的闪烁倒影。在右中前景，一艘狭长的深色木划艇斜着停放，左端更低、更靠近镜头；一位戴白色斗笠、身穿深色衣服的船夫坐在右端，手持一支长木桨，伸入水中指向右下方，船中部载着一堆约十盏发光的纸灯笼。深蓝色的暮色天空，桥后方地平线上有柔和的粉紫色辉光，没有星星也没有月亮。温暖的灯笼光与冷蓝色的黄昏形成对比，写实的电影感旅行摄影，平静而神奇的氛围。宽幅横向16:9。No close-up faces, no text, no signs, no logos.
```

</details>

<details><summary><b>黄昏纸灯笼港湾</b> · 机器翻译</summary>

```text
黄昏时分宁静的木质港口,数百盏温暖的纸灯笼悬挂在船只和码头上,平静的水面倒映着橙色与玫瑰色的光,轻柔的薄雾,电影感广角镜头,超精细,宁静的氛围,前景中没有人物
```

</details>

<details><summary><b>黄昏阅读花园中的夯土图书馆</b> · 机器翻译</summary>

```text
黄昏时分,同一座单层夯土村庄图书馆的背面,从安静的阅读花园望去,宽大的窗户和如今位于左端的圆形夯土阅读塔透出温暖的金色灯光。同一座建筑:长长的墙面呈现出赭石色、沙色和锈红色土层分明的水平层次,坐落在低矮的灰色石基座上,带有纤薄深色钢制边缘的平屋顶深深出挑,高而窄的窗户配有深青铜色窗框。圆柱形塔楼略高于主屋顶,顶部环绕着一圈连续的深色窗框高窗,像灯笼一样发光。沿着花园这一侧,一座浅浅的木制藤架由六根纤细的浅色木柱支撑,遮蔽着铺石露台和低矮的木制阅读长椅。花园里有碎石小径、乡土干草、陶土花盆里的薰衣草和温暖的小路灯,前方广场上那棵宽大的古杜松的树冠刚好在右侧屋顶上方露出。深蓝色的暮色天空中挂着一弯细月和初现的星星。写实建筑摄影,横向 16:9。无人物,无文字,无标牌,无汽车。
```

</details>

<details><summary><b>黄昏雪地铁轨红狐版画</b> · 机器翻译</summary>

```text
一只红狐在黄昏时分迈步穿过两条积雪的铁轨,以手工雕刻的油毡版画(linocut)呈现。狐狸是画面中唯一的暖色:身体和蓬松的尾巴使用单一的朱红色油墨层,胸部和尾尖露出清爽的白色纸面。铁轨从左下方向远处斜向延伸,钢轨和木枕木以粗黑线条刻出,半埋在用刻刀痕迹描绘的积雪中。右侧立着一根小木信号柱,挂着一盏点亮的灯笼,地平线上是一排光秃秃的桦树和一座低矮的山丘。天空是淡石板蓝色的第二层油墨,带有刻出的横向条纹和几颗刚刚显现的镂空星星。整幅画面具有明显的油毡版画质感:粗犷的 V 型刻刀笔触、略微不均匀的油墨、蓝色与红色层之间轻微的套准偏移,以及奶油色版画纸的纹理,四周留有窄窄的白边。三色限定色板(黑色、石板蓝、朱红)。安静、寒冷、静止的氛围。无文字,无签名,无人物。
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

<details><summary><b>黄金时刻的大西洋海鹦群</b> · 机器翻译</summary>

```text
一张写实风格的野生动物摄影作品,画面中一小群大西洋海鹦站在长满青草的海崖边缘,沐浴在温暖的傍晚光线中,下方远处是开阔的北大西洋。前景中,四只海鹦站在一丛绿草和粉色海石竹花上,它们鲜艳的橙红与石板灰条纹喙、白色面庞、黑色背部和橙色双脚清晰锐利、细节丰富;其中一只海鹦嘴里衔着一排小小的银色玉筋鱼。在它们身后,崖顶向左弯曲延伸,更多海鹦聚在洞穴入口附近,而深色层叠的岩壁陡直落入大海。远处下方,深蓝绿色的海水在两座高耸的海蚀柱周围碎成白色浪花,几只海鹦在水面上飞过,翅膀快速拍动而显得模糊。低低的金色阳光从左侧照来,为鸟儿的羽毛镶上一圈暖光,柔和朦胧的天空由淡金色渐变为浅蓝色,地平线上有一层薄薄的海雾。使用长焦镜头拍摄,前景鸟儿景深较浅,色彩自然,羽毛质感清晰,具有自然纪录片的品质。宽幅横向 16:9。无人物,无文字,无水印,无标志。
```

</details>

<details><summary><b>黄金时刻街拍抓拍</b></summary>

```text
2026 年德黑兰的抓拍街头照片，黄金时段，浅景深，人群在背景中模糊。一名伊朗女性目光瞥向画外；双眉轻轻扬起一次，眼神迅速瞄向出口，瞳孔微微睁大——这是秘密信号“我们走吧，现在”。画面下方有一个手写边框的方框，圆珠笔字迹写着：“بریم？”
```

</details>

<details><summary><b>黄金时刻车内人像</b> · 机器翻译</summary>

```text
主体：一张年轻女性的人像。

姿势：她放松地坐在车内。一条膝盖高高抬起贴近胸口，一只手搭在膝盖上。她的头部微微倾斜，自信的目光直视镜头。

服装：她穿着一件非常宽大、厚实的深棕色（巧克力色）连帽衫。胸前居中是哈利·波特风格字体的白色文字：

AVADA
KEDAVRA
BITCH

她还穿着浅灰色麻灰慢跑运动裤，版型宽松。

头发：笔直、浓密、健康的头发，精准的中分，顺滑地垂落在肩膀和胸前。

妆容：自然妆容。

光线：温暖的自然黄金时刻光线（日出或日落）。柔和而明亮的阳光从右侧（以观看者的视角）射来，照亮她脸部的右半边，并在头发上形成温暖的高光。她脸部的左侧和背景保持在柔和的深色阴影中，营造出电影感的对比和纵深。

拍摄角度：近距离的特写人像。相机位置略高于视线水平（轻微俯角），类似自拍视角，或站在敞开的车门旁的人的视角。面部和上半身对焦锐利。

背景：模糊的深色车内，带有焦外虚化效果。背景中可见部分深色座椅和一扇车窗。

氛围与美学：温馨、放松，同时非常时尚的休闲别致美学。平静、自信、潮流的 Instagram 风格，传达舒适感与现代时尚。

不要改变面部特征。淡淡的浅笑。竖构图，3:4 画幅比例。超写实、高质量、锐利的 8K 照片，使用 iPhone 16 Pro 拍摄。
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

<details><summary><b>黎明梯田吊脚楼移轴摄影</b> · 机器翻译</summary>

```text
黎明时分,蜿蜒的绿色梯田沿山坡层层而下,通向一座由深色茅草屋顶的木制吊脚楼组成的小村庄,以移轴摄影的微缩模型效果拍摄。从山谷对面的高处俯瞰,清晰对焦的窄带落在村庄和中间几层梯田上,画面顶部和底部则强烈虚化,让整个场景看起来像一个微缩模型。灌满水的梯田像一条条玻璃带,映出粉色和金色的天空,低低的薄雾聚集在谷底。一条小溪穿过人行小桥,蜿蜒流过房屋,两个烟囱升起淡淡的柴烟,几只鸭子漂浮在一块稻田里。芭蕉树和竹丛点缀着田野边缘。色彩饱和却自然,清新的晨光斜掠过梯田的田埂,投下柔和的长影。专业旅行摄影,移轴镜头效果,宽幅横向 16:9。无人物,无文字,无标牌,无车辆。
```

</details>

<details><summary><b>黎明街角面包店等距3D模型</b> · 机器翻译</summary>

```text
一个迷人的 3D 等距微缩场景,展示黎明时分一家两层的小型街角面包店,悬浮在一块方形鹅卵石街道平板上,背景是柔和的奶油色。正面和一侧的墙被像玩偶屋一样切开,这样我们可以看到里面。一楼:一座砖砌面包炉发出橙色的光芒,一位系着白色围裙、戴着白色帽子的面包师正用木制面包铲将一盘面包滑出;还有摆放着法棍和羊角面包的冷却架、粗麻布面粉袋、配有复古黄铜秤的大理石柜台,以及陈列着粉彩马卡龙的玻璃展示柜。楼上:面包师小小的公寓,有一张绗缝床、一只睡在窗台上的橘猫、一个书架和一把冒着热气的茶壶。室外:一个薄荷绿与白色条纹相间的遮阳篷、一块形状像羊角面包且没有可辨认文字的手绘木制招牌、一个黑板立架、一辆带面包篮的自行车、盆栽天竺葵,以及一盏仍亮着的路灯。来自左侧的温暖金色日出光线,长而柔和的阴影,柔和的环境光遮蔽。黄油黄、薄荷绿、赤陶色和奶油色构成的粉彩色调。柔软的黏土般材质,圆润的边缘,移轴微缩模型质感,细节丰富,干净的渲染,1:1。
```

</details>

<details><summary><b>黏土蛙乐队睡莲演奏</b> · 机器翻译</summary>

```text
四只快乐的黏土青蛙在黄昏的池塘里,坐在巨大的莲叶上演奏小巧的乐器:一只拨弄着小班卓琴,一只演奏用中空芦苇做成的立式贝斯,一只敲打橡子帽做成的鼓,还有一只吹着卷曲的蜗牛壳号角。这是手工制作的定格黏土动画布景,橡皮泥上能看到清晰的指纹和柔和的工具痕迹。纸灯笼在池塘周围弯曲的短铁丝杆上发出光亮,由微型暖色 LED 做成的萤火虫在香蒲和粉色睡莲之间飘荡。水面是光亮的蓝色树脂,带有轻柔的涟漪和灯笼的倒影。背景是毛毡做的山丘、棉絮般的薄雾,以及桃色和薰衣草色的彩绘暮色天空,点缀着几颗初现的星星。景深很浅,就像用微距镜头拍摄的真实微缩场景,暖色主光搭配冷蓝色轮廓光。俏皮、温馨、童话书般的氛围,色彩浓郁饱和。宽幅横向 16:9。无人物,无手,无文字,无字母,无标志。
```

</details>

<details><summary><b>黏土迷你城市</b></summary>

```text
生成一个奇趣盎然的微型世界，以${landmark_name}为核心地标，整个场景完全由五彩缤纷的造型黏土手工制作而成。所有元素（建筑、树木、水道及城市设施）均须呈现手塑质感，表面清晰可见指纹印痕与天然黏土肌理。采用活泼稚拙的儿童画风，配色明快鲜艳：湛蓝晴空、蓬松乳白云朵、翠绿树木，以及暖色调的建筑——明黄、橙红、正红与钴蓝相间。每一处表面与柔和曲面都须彰显手工制作的独特品质。采用广角视角构图，完整呈现整片微型景观，营造和谐而欢愉的整体氛围。

在画面正上方中央位置，以干净、粗体、圆润友好的字体添加城市名称${city_name}，字体风格须契合整体黏土美学。文字须清晰可辨，在天空背景上具备高对比度，并带有微妙的立体深度效果（仿佛亦由黏土制成——即轻微3D黏土字效），但整体保持简洁，切勿过度细节化。

场景中其他任何位置均不得出现额外文字、单词或标识牌。仅可通过具有辨识度的建筑特征，借由纯粹的雕塑式黏土元素来定义该地点。图像尺寸为1080×1080像素。
```

</details>

<details><summary><b>黑山海景公寓家庭场景</b> · 机器翻译</summary>

```text
黑山的一套现代公寓,拥有全景海景。明亮宽敞的客厅,内饰宁静雅致。一位母亲和她的儿子坐在沙发上,身旁放着毯子和柔软的靠垫,营造出温暖而亲密的感觉。空气中弥漫着安静的节日气氛,新年即将到来,家中充满舒适感与平和的家庭氛围。
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

<details><summary><b>黑沙滩上方的红顶白教堂</b> · 机器翻译</summary>

```text
黄金时刻，一座红色山形屋顶、尖顶红色塔楼的白色小木教堂，立在冰岛黑沙滩上方一处圆润的绿色草地岬角上，右侧的海中耸立着深色玄武岩海蚀柱。教堂位于画面左三分之一处，靠近岬角顶端，白色墙面和小窗被低角度阳光映成温暖的金色。岬角的草坡向下延伸至海滩，一道宽阔弯曲的细腻黑色火山沙滩从左下角横扫过前景，近水处湿润而有光泽。白色泡沫的海浪从右侧以数条长线涌来，漫上黑沙滩。右半部分的海中立着四块深色玄武岩：岬角尽头附近一块低矮的圆形岩石，中间偏右一座高而嶙峋的海蚀柱，以及更靠右的两座较小的尖塔状岩石。低悬的太阳靠近地平线，位于最左侧的岬角后方，散发着黄橙色的光芒，天空布满零散的云朵，被映成橙色、粉色和紫色，衬着柔和的蓝色。写实风景摄影，广角，自然色彩，平静而富有戏剧性的氛围。宽幅横向 16:9。No people, no text, no logos.
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

<details><summary><b>黑白夜间抓拍人像</b> · 机器翻译</summary>

```text
整体场景:一张抓拍的中景黑白照片,带有粗粝、颗粒感十足的电影胶片质感。氛围俏皮、撩人、自信从容,捕捉了一个自发的夜晚瞬间。

主体与外貌:一位年轻女性,蓬松的波浪长发自然垂落在  上。她的面部特征和身份保持不变。

服装:她穿着一件修身的白色棉质露脐短款 T 恤,上面印有文字“DRAMA IS PART OF THE PROCESS”,字体为略显磨损、带纹理的大写衬线体。下身搭配浅色纹理休闲裤,裤腰位于腰线稍下方,露出一小截腰腹。

姿势与表情:她身体略微转向左侧,头部轻轻向下倾斜。双眼闭着,带着甜美柔和的微笑。一只手随意地搭在臀部,另一只手轻轻触碰短款上衣的下摆。她的肢体语言显得放松、女性化、俏皮,自然带着撩人的气息。

光线:低光夜间摄影,仅有一束来自左侧的定向光,营造出戏剧性的高对比度阴影,同时柔和地照亮她的脸、头发和服装。

背景:深邃、近乎全黑的背景,远处城市灯光柔和虚化,城市轮廓若隐若现,让焦点完全集中在这位女性身上。

细节:高度写实、锐利如刀的 8K 画质,带有真实的胶片颗粒。iPhone 16 Pro Max 拍摄,真实的皮肤质感,极简自然的妆容,头发略显凌乱,浅景深,偏离中心的构图,超精细,照片级写实。

画幅:3:4。
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

<details><summary><b>黑白微笑人像</b> · 机器翻译</summary>

```text
高质量的艺术黑白照片，呈现一位年轻女性富有情感的肖像。

中景，聚焦于她的脸部和上半身。她站立着，头轻轻向下并偏向一侧，闭着眼睛，甜美而柔和地微笑。她的左手抬起，手指随意地穿过额头附近她那散开的深色长发，营造出质感和动感。她的右臂向一侧部分伸展。

发型：直发，侧分。

妆容：整洁而分明，睫毛又长又浓密，眉形漂亮，涂深色口红。指甲做了浅色美甲。

服饰：一件黑色上衣，带有深方领（鲸骨）。

配饰：一条带有小圆形金属细节的黑色布质颈链，一条纤细的银色（或白金）链条项链，挂着刀形吊坠，手腕上戴着一条精致的手链。

光线：柔和的自然光，轻柔地凸显头发和皮肤的质感，营造出深邃的黑白对比和美丽的层次感。

情绪：温暖、温柔、快乐而亲密。

拍摄角度：视平线高度的中景（与她倾斜头部时的脸部对齐）。

背景：房间或工作室的内部，被深度虚化，带有散景效果，营造出温馨的氛围，又不会分散对主体的注意力。

不要改变我的面部特征。

3:4

超写实、高质量、清晰的 8K 照片，使用 iPhone 16 Pro Max 拍摄。
```

</details>

<details><summary><b>黑白明暗对照人像</b> · 机器翻译</summary>

```text
一张写实的超高质量8K黑白电影感人像，使用iPhone 16 Pro Max拍摄，宽高比为3:4。

风格：单色艺术人像，电影美学，高对比明暗对照法，带有深邃的黑色和戏剧性的色调范围。

相机与构图：平视角度的极致特写。女子呈四分之三半侧面，脸部微微转向左侧。她的头轻轻倾斜，形成优雅而亲密的构图。

光线：锐利、戏剧性的侧光只照亮她脸部的轮廓——鼻梁、嘴唇、下巴和左脸颊的一部分——而她脸的右侧、双眼和背景则保持在深邃、几乎密不透光的阴影中。

表情与姿势：她的目光低垂，部分被柔软的发丝和阴影遮住。她的面部表情放松、忧郁、神秘、性感、优雅，带着安静的沉思。她带着若隐若现的半笑，双唇微微张开。

发型：浓密的深色头发，带有松散自然的波浪。造型略显凌乱，带纹理的发丝自然地垂落在脸上。

妆容：现代而精致，肌肤光滑哑光，饱满的双唇轮廓自然分明，捕捉到一抹细腻的高光。

服装与配饰：她穿着一件深色上衣或连衣裙，领口柔和，与黑色背景无缝融合。一只修长、雕塑感的醒目耳环在阴影中若隐若现地挂在她的右耳上。

不要改变女孩的面部特征、眼型、眉毛、鼻子或嘴唇。保持100%的面部相似度。
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

<details><summary><b>黑色西装棚拍肖像</b> · 机器翻译</summary>

```text
一张简洁、极简的影棚肖像，主角身着经典正装。

服装：剪裁合体的黑色西装外套，搭配同色黑色西裤、扣到领口的挺括白色衬衫，以及一条利落的黑色领带。场景：干净、中性的影棚背景，通常是无缝的灰色、白色或深黑色，形成高对比度，没有任何干扰。灯光：影棚灯光投下柔和的阴影，凸显西装面料的利落线条与质感，营造出精致、专业的观感。姿势：通常是自信的头像或全身姿势，要么正面朝前、双手插兜，要么略微朝向光线侧身。
```

</details>
