# 图像与设计 (1/4)

共 743 条。复制后把方括号里的内容换成你的，粘贴进任意对话模型即可。

[English](../en/image.md) · [中文](../zh/image.md) · [在线搜索复制](https://agentcraft.dev/zh/prompts/image/)

分页：**1** · [2](image-2.md) · [3](image-3.md) · [4](image-4.md)

<details><summary><b>2026手机新年海报</b></summary>

```text
充当一名平面设计助手。你的任务是创建一张视觉上吸引人的移动端海报，以祝贺大家迎来 2026 年。该海报须满足以下要求：
- 纵横比为 9:16，分辨率为 1080×1920 像素
- 包含欢快且富有庆祝氛围的元素，契合新年主题
- 预留充足空间，供用户显著添加其品牌名称
- 整体风格兼顾专业性与节日感

约束条件：
- 确保设计支持文本叠加层，便于后续自定义
- 运用鲜艳明快的色彩以吸引注意力

示例元素：
- 烟花、彩纸屑或类似庆祝类图形
- 文字占位符，如“Happy 2026!” 和 “${your_brand_here}”
- 节日感配色方案：${color1:gold}、${color2:silver} 与 ${color3:blue}

使用此提示词生成一张适用于移动设备的高质量数字图像。
```

</details>

<details><summary><b>2026新年全家福分析</b></summary>

```text
{
  "role": "Image Analyzer for Festive New Year Scenes",
  "context": "You are an expert in analyzing festive family photos. The current task involves a photo celebrating the arrival of New Year 2026.",
  "task": "Analyze the uploaded family photo to identify elements that depict a festive New Year's Eve celebration.",
  "constraints": [
    "Focus on identifying key festive elements such as decorations, attire, and expressions.",
    "Provide a detailed description of how each element contributes to the New Year's celebration theme."
  ],
  "variables": {
    "year": "2026"
  },
  "output_format": "Provide a summary that includes the main festive elements and their significance in the photo."
}
```

</details>

<details><summary><b>2026时尚大片</b> · 机器翻译</summary>

```text
一位20岁的成年荷兰女模特，肤色白皙，留着及肩以下的铜棕色长松散波浪发，穿着严格依据所附时尚衣橱参考图设计的当代服装。她站在一个堆满水果的路边水果摊后面，一只手举着一个巨大的西瓜，同时神情完全从容地直视镜头；她的服装在杂乱的农产品之间勾勒出清晰的轮廓。腰部以上的取景，透过前景水果拍摄，浅景深，强烈的正午阳光，饱和的西瓜红、柑橘橙、叶绿色与钴蓝色点缀，清晰的硬阴影，略微褪色的胶片色彩，自然随性的街头时尚摄影，真实的触感，无文字，无标志。
```

</details>

<details><summary><b>2026星象运势海报</b> · 机器翻译</summary>

```text
{
  "task": "以上传的人像作为严格的身份锚点,生成照片级写实的高级神秘感 2026 占星海报,文字语言可由用户选择(TR 或 EN)。",
  "inputs": {
    "REF_IMAGE": "${user_uploaded_image}",
    "BIRTH_DATE": "{YYYY-MM-DD}",
    "BIRTH_TIME": "{HH:MM or UNKNOWN}",
    "BIRTH_PLACE": "{City, Country}",
    "TARGET_YEAR": "2026",
    "OUTPUT_LANGUAGE": "${tr_or_en}"
  },
  "prompt": "严格身份锚点:\n以 ${ref_image} 作为主体的严格身份锚点。完全保留同一个人:面部结构、比例、年龄、肤色、眼型、鼻子、嘴唇、下颌线以及整体神似度。不得出现身份漂移。\n\n步骤 1:占星预测(在渲染之前完成):\n- 根据 BIRTH_DATE=${birth_date}、BIRTH_TIME=${birth_time}、BIRTH_PLACE=${birth_place} 构建本命盘。如果 BIRTH_TIME 为 UNKNOWN,则使用正午盘近似,并避免做出依赖出生时间的论断。\n- 判断 2026 年在以下方面的运势:LOVE、CAREER、MONEY、HEALTH。\n- 每个方面选取一个关键词,描述 2026 年可能的结果。\n\n语言逻辑(关键):\n如果 OUTPUT_LANGUAGE = TR:\n- 恰好生成 4 个土耳其语关键词。\n- 每个关键词必须只有一个单词(无空格、无连字符),土耳其语大写,最多 10 个字符。\n- 仅为示例(不要盲目照抄):BOLLUK, KAVUŞMA, YÜKSELİŞ, DENGE, ŞANS, ATILIM, DÖNÜŞÜM, GÜÇLENME。\n- 底部标语必须完全一致:\n  \"2026 Yılı Sizin Yılınız olsun\"\n\n如果 OUTPUT_LANGUAGE = EN:\n- 恰好生成 4 个英语关键词。\n- 每个关键词必须只有一个单词(无空格、无连字符),大写,最多 10 个字符。\n- 仅为示例(不要盲目照抄):ABUNDANCE, COMMITMENT, BREAKTHRU, CLARITY, GROWTH, HEALING, VICTORY, RENEWAL, PROMOTION。\n- 底部标语必须完全一致:\n  \"MAKE 2026 YOUR YEAR\"\n\n重要文字规则:\n- 不要打印 LOVE/CAREER/MONEY/HEALTH 之类的标签。\n- 只打印 4 个关键词和底部标语,不要有其他内容。\n\n步骤 2:照片级写实的神秘外观(不要风格化成插画):\n- 主体必须保持照片级写实:自然的皮肤纹理、真实的头发,不要塑料感皮肤。\n- 神秘感必须通过摄影手法和细微氛围来实现:\n  - 淡淡的体积雾,极少的类似香烟的烟缕\n  - 月光轮廓光加暖色主光,精致的镜面高光\n  - 微小的尘埃颗粒闪烁(非常细微)\n  - 仅在背景中出现淡淡的星座轮盘和星盘线条(不要出现在脸上)\n  - 神圣几何作为极其细微的虚化光斑叠层,绝不出现可读文字\n\n步骤 3:与预测相关联的视觉隐喻(高级,不俗气):\n- MONEY 为正面:精致的金色调光弧与向上流动的光(不要出现货币或符号)。\n- LOVE 为正面:成对的环绕轨迹和温暖的玫瑰金高光(不要出现表情符号爱心)。\n- CAREER 为正面:背景中向上延伸的建筑线条,或细微的上升星轨图。\n- HEALTH 为强:平静均衡的圆环和干净的留白。\n- 通过光线方向、对比度和位置,使最强的两个主题在视觉上占主导。\n\n海报设计:\n- 宽高比:4:5 竖版,超高分辨率。\n- 构图:居中的主视觉人像,头肩或半身,平视角度。\n- 镜头质感:85mm 人像镜头,f/1.8,浅景深,眼睛对焦清晰。\n- 背景:深午夜渐变,点缀细微星光;现代、高级、极简。\n\n排版(必须完美且清晰可读):\nA) 关键词行:\n- 将 4 个关键词排成一行,置于标语上方。\n- 使用分隔符:词与词之间用 \" • \"。\n- 字体:现代无衬线体(类似 Montserrat),字间距略微加大。\n\nB) 底部标语:\n- 置于最底部,居中。\n- 字体:优雅的衬线体(类似 Playfair Display)。\n\n其他任何位置都不要有任何文字。\n\n收尾:\n- 高级调色,细腻的胶片对比度,不要过饱和。\n- 自然修饰,不要过度锐化。\n- 确保所选语言的文字拼写正确且完全清晰可读。\n",
  "negative_prompt": "any extra text, misspelled words, wrong letters, watermark, logo, signature, QR code, low-res, blur, noise, face distortion, identity drift, different person, illustration, cartoon, anime, heavy fantasy styling, neon colors, cheap astrology clipart, currency, currency symbols, emoji hearts, messy background, duplicated face, extra fingers, deformed hands, readable runes, readable glyph text",
  "output": {
    "count": 1,
    "aspect_ratio": "4:5",
    "style": "photorealistic premium cinematic mystical editorial poster"
  }
}
```

</details>

<details><summary><b>2150年的未来阿尔卑斯</b></summary>

```text
创作一幅2150年阿尔卑斯山的电影级广角镜头画面。场景设定在一个寂静的后末日世界，带有未来主义元素。远处的城市散发着蓝色光芒，地球被描绘成化为光粒子的状态。整体氛围广阔而空旷，采用冷色调与柔和的雾气。画面应达到超现实主义的逼真程度，包含体积光效与忧郁的情绪，以8K分辨率呈现，如同具有戏剧性光影的电影剧照。
```

</details>

<details><summary><b>3D 城市剖面模型</b></summary>

```text
${city_name:Istanbul} 的超写实 3D 方形微缩模型场景：底部裸露的土壤剖面清晰可见，展示岩石、树根与土层；上方为充满奇思妙想的童话风城市景观，融入 ${city_name:Istanbul} 的标志性地标、建筑与文化元素；现代风格的白色文字标签 “${city_name:Istanbul}” 自然嵌入整体构图中；纯白影棚背景，辅以柔和自然光照明；DSLR 摄影品质——锐利、鲜明、富有魔幻现实主义风格；尺寸为 1080×1080。
```

</details>

<details><summary><b>3D 家庭短片：幼儿遇见新生弟妹</b> · 机器翻译</summary>

```text
创作一部精美、超精细的3D动画家庭短片,主角是一个可爱的幼儿男孩,有着蓬松的金黄色头发、富有表现力的蓝色大眼睛、红扑扑的脸颊,穿着蓝白条纹睡衣。他在一个温馨、阳光明媚的现代家中,充满爱意地与刚出生的弟弟或妹妹互动。

场景1:温暖的客厅,柔和的自然阳光透过大窗户洒进来。妈妈轻轻地做着家务,好奇的幼儿朝着安静睡在柔软编织婴儿篮里的新生儿走去。

场景2:幼儿小心地俯身靠近婴儿篮,甜甜地对着裹在浅蓝色毯子里的小小新生儿微笑的特写。宝宝轻轻地动着,做出可爱的表情。

场景3:妈妈把新生儿安全地放进木制婴儿床。幼儿站在婴儿床旁,充满爱意和好奇地看着宝宝。用电影级特写捕捉温柔的兄弟姐妹情谊。

场景4:幼儿坐在地板上,拿着奶瓶,看起来天真可爱。温暖的阳光照亮他的脸,凸显他富有表现力的眼睛和柔软的金发。

场景5:幼儿在柔软的客厅地毯上,在弟弟或妹妹身边轻柔地玩玩具,妈妈则在沙发上充满爱意地看着。

场景6:幼儿抱着一只可爱的泰迪熊,开心地微笑。用特写镜头突出他喜悦的表情和逼真的动画细节。

最终场景:夜晚,妈妈舒适地坐在床上,身边是两个孩子。她充满爱意地抱着新生儿,幼儿紧紧地坐在她身旁。以妈妈亲吻宝宝额头的温柔特写作为结尾,呈现一个宁静、充满爱的家庭时刻。

视觉风格:高端皮克斯风格的3D动画,可爱的角色设计,逼真的织物质感,细致的发丝,富有表现力的面部动画,柔和的全局光照,温暖的电影级灯光,自然的阴影,流畅的镜头运动,浅景深,情感动人的叙事,所有场景中角色外貌保持一致,4K画质,竖屏9:16宽高比。

负面提示词:扭曲的面部,不一致的角色设计,多余的手指,不自然的动作,闪烁,模糊的质感,变形的手,突然更换服装,不真实的比例,文字、标志和水印。
```

</details>

<details><summary><b>3D 心脏解剖视频</b></summary>

```text
[00:00 - 00:03]  
超现实 8K 3D 人体心脏解剖结构，缓慢跳动，具有冠状动脉的精细肌肉纹理，黄金时刻电影级灯光，鱼眼畸变效果，35mm 叙事镜头，专业医学信息图风格，模糊的未来主义实验室背景。 --ar 9:16

[00:03 - 00:06]  
心脏解剖结构的极端特写，戏剧性的黄金时刻照明，35mm 鱼眼镜头畸变，超现实生物纹理，电影级 8K，9:16 竖版构图。 --ar 9:16
```

</details>

<details><summary><b>3D 等距微缩城市天气场景</b></summary>

```text
呈现一幅清晰、45°俯视角度的竖版（9:16）等距微型3D卡通场景，构图中心突出标志性地标，以展现精准而细腻的建模效果。

该场景采用柔和、精致的纹理，搭配逼真的基于物理渲染（PBR）材质，以及轻柔、富有生命力的光照与阴影效果。天气元素被创造性地融入城市建筑之中，建立起城市地貌与大气状况之间的动态互动，营造出沉浸式的天气氛围。

采用简洁、统一的构图，风格极简；背景为柔和的纯色，以凸显主体内容。整体视觉风格清新宜人、舒缓宁静。

在画面正上方中央位置显示一个醒目的天气图标；图标下方依次标注日期（超小号字体）和温度范围（中号字体）。城市名称（大号字体）置于天气图标正上方。所有天气信息均无背景色，并可轻微叠加于建筑之上。

文字须采用所输入城市的本地语言。

请在渲染前检索指定城市的当前天气状况。

城市名称：İSTANBUL
```

</details>

<details><summary><b>3D医学解剖模型渲染</b></summary>

```text
{
  "fixed_prompt_components": {
    "composition": "广角全身镜头，从头到脚完整呈现整个人体，远景，竖构图人像，居中且对称站姿",
    "background": "孤立于无缝纯白背景之上，影棚背板，洁净的白色环境",
    "art_style": "照片级真实感 3D 医学渲染，ZBrush 数字雕刻风格，科学解剖模型美学",
    "texture_and_material": "单色银灰色皮肤，带有拉丝金属质感，微观表面细节丰富，肌肉条纹高度精细，哑光表面处理",
    "lighting_and_tech": "电影级轮廓光，全局光照，光线追踪，环境光遮蔽，8K 分辨率，超高清（UHD），焦点锐利，超精细细节"
  },
  "variables": {
    "gender": "${gender:male}",
    "view_angle": "${view_angle:Front view}",
    "target_muscle_group": "${target_muscle_group:Pectoralis Major (Chest)}",
    "highlight_color": "${highlight_color:glowing cyan blue}"
  },
  "negative_prompt": "文字、信息图表、图表、示意图、标签、箭头、用户界面（UI）、裁剪图像、特写、微距镜头、肖像照、脚部被截断、头部被截断、局部身体、灰色背景、渐变背景、地面阴影、模糊、低分辨率、畸变、水印"
}
```

</details>

<details><summary><b>3D卡通物理学家漫画像</b></summary>

```text
一个受理查德·费曼启发的、顽皮的物理学家的高细节风格化 3D 卡通漫画肖像。

角色身份：  
- 男性  
- 中年  
- 瘦削体型  
- 表情丰富的脸庞，带着灿烂笑容  
- 浓密的深色波浪发  
- 大而圆的眼镜  
- 充满智慧且淘气的眼神  
- 温暖友好的个性  
- 灯芯绒学术夹克  
- 白衬衫，口袋里插着几支笔  
- 手持一本物理书  

艺术风格：  
受 Pixar 启发的风格化写实，奇趣 3D 漫画风格， oversized 的表现力强的眼睛，夸张的面部比例，精致的 CGI 渲染，动画电影角色美学，收藏级手办外观，超干净白色背景。

姿势：  
自信站立，一根手指抬起，仿佛正在讲解物理。

场景：  
极简白色摄影棚背景，带有微妙的物理涂鸦。

渲染质量：  
超精细 CGI，电影级灯光，Octane Render，AAA 级动画电影品质。

负面提示词：  
诡异的真实感、解剖结构错误、扭曲的手部、模糊的眼睛、重复的肢体、多余的手指、杂乱的纹理。
```

</details>

<details><summary><b>3D渲染转2D平面图</b></summary>

```text
{  
  "task": "image_to_image",  
  "description": "将带家具的 3D 室内渲染图转换为简洁清晰的 2D 建筑平面图绘图",  
  "input_image": "3d_render_of_apartment_interior.png",  
  "prompt": "俯视视角 2D 建筑平面图，黑白技术制图风格，线条干净、呈矢量风格，墙体厚度精确，房间边界清晰明确，各空间均标注房间名称及平方米面积，门以开启弧线表示，窗以墙体上的断口形式呈现，极少阴影，无透视效果，正交投影，建筑蓝图风格，专业住宅平面图，类似 CAD 绘图",  
  "negative_prompt": "3D 透视视角，等轴测视图，真实光照，阴影，纹理，家具渲染，人物，景深，照片级真实感，色彩，渐变，柔边，艺术手绘草图，手绘风格",  
  "settings": {  
    "model": "sdxl",  
    "sampler": "DPM++ 2M Karras",  
    "steps": 30,  
    "cfg_scale": 7,  
    "denoising_strength": 0.65,  
    "resolution": {  
      "width": 1024,  
      "height": 1024  
    }  
  },  
  "output_expectation": "输出扁平化 2D 平面图，风格与建筑平面图绘制一致，适用于房地产房源列表或施工文档"  
}
```

</details>

<details><summary><b>3D爆款广告海报提示词</b></summary>

```text
为 Photoshop 海报创建一个更详细的提示词，用于制作一张 3D 海报设计，并使用附带的图像作为背景，比例为 1:1，同时将提供的附带图像中的角色放入设计中。文本内容应包含具有设计感的排版，并打造一个更具冲击力的“病毒式广告”版本，加入更强烈的视觉钩子。主标题为："GRAND OPENING" "THIS JUNE 12"（主要 headline），下方小字为："ENCODING JUNE 7"，底部按钮为："LINE UP NOW"。
```

</details>

<details><summary><b>3D等距奥斯曼历史场景</b></summary>

```text
生成一幅超写实3D等距杰作，背景为恢弘无尽的传统水墨风格奥斯曼历史羊皮纸卷轴，正于画面中徐徐展开。

该场景通过象征性图像、军事动态与精神意志，具象化呈现${name:Fatih Sultan Mehmet}在${event:君士坦丁堡征服（1453年）}期间所承载的遗产、战略天才及其对世界的变革性影响——所有元素均直接从羊皮纸本身浮现而出。

羊皮纸批注（内容自适应——奥斯曼历史）

羊皮纸上布满奥斯曼风格的手写书法、墨线素描、细密画风格插图、战略示意图及建筑纹样，所有内容均根据${name:Fatih Sultan Mehmet}与${event:君士坦丁堡征服（1453年）}动态适配。

• 身份与遗产批注

醒目的奥斯曼书法书写${name:Fatih Sultan Mehmet}之名，辅以手稿式旁注，阐释其身份及其标志性功绩，说明${event:君士坦丁堡征服（1453年）}如何重塑奥斯曼帝国与世界历史。

• 时间与起源批注

流畅的墨绘时间轴箭头标示其在位时期与历史语境，重点突出${event:1453}，并以“埃迪尔内 → 君士坦丁堡”等区域联结，象征一场决定性的历史转折。

• 战略与军事创新批注

羊皮纸上的示意图随事件动态适配，可能包括：

大型奥斯曼火炮  
围城或战役地图  
要塞布局、海军航线或改革方案图  
战术箭头与运动轨迹线，直观展现${event:君士坦丁堡征服}的执行过程  
所有元素均配有手写体战略说明。

• 象征符号、服饰与器物批注

带标注的墨线素描动态适配，可能包括：

奥斯曼帝国铠甲与典礼服饰  
与${event}相关的刀剑、旗帜或工具  
建筑剪影（城市、清真寺、要塞、机构）  
帝国花押（tuğra）纹样与蜡封

• 文化与文明意义批注

手稿风格反思文字将${event}描述为：

奥斯曼历史的重大转折点  
政治、文化或文明秩序的转型  
领导力、远见与治国术的象征  
对世界文化遗产的持久贡献

构图

羊皮纸卷轴如历史长河般在空间中奔流，构成连贯叙事。

画面中央，${name:Fatih Sultan Mehmet}于${event:君士坦丁堡征服}的高潮时刻破纸而出，象征成就、权威与历史宿命。

2D → 3D 转换

平面黑色墨线绘图——包括书法、示意图、符号与人物——无缝转化为超写实3D材质：石材、金属、织物、肌肤、烟雾与光线；同时所有3D元素在视觉上仍牢固锚定于羊皮纸表面。

视觉效果与细节

陈旧羊皮纸质感、可见墨迹晕染、边缘褪色、悬浮的奥斯曼书法碎片、帝国蜡封、几何纹样、飘浮尘粒、薄雾、深远大气透视。

光影

史诗级黄金时刻电影化布光，照亮中心人物及${event}的关键元素，与单色羊皮纸背景形成强烈戏剧对比，凸显历史厚重感与不朽遗产。

技术规格

8K分辨率  
电影级景深  
Unreal Engine 5 渲染  
博物馆级写实度  
宏大尺度  
超精细纹理  

--ar 16:9  
--stylize 350  
--no flat, simple, cartoon, borders, frame, modern buildings
```

</details>

<details><summary><b>3D线框图标</b></summary>

```text
根据给定的 2D 图像，将其中心对象重构为真实的 3D 线框模型。

- 将 2D 形状解释为立体几何体，并沿深度方向拉伸。

- 使用线框网格线构建可见的 3D 结构，包裹住物体外形（正面、侧面和曲面）。

- 仅使用细而精准、发光的白色线框线条，无实体表面，无平面填充。

- Apple App Store 风格图标，高端 iOS 设计语言，受 WWDC 启发。

- 圆角方形应用图标，居中且对称。

- 柔和蓝色渐变背景，带有微妙辉光。

- 干净的正交前视图，具备清晰的深度提示（Z 轴线框）。

- 高分辨率，未来感 UI 图标。

- 无文字，无标志，无插画风格


负面提示：

2D 平面设计，平面图标，插图，仅靠光影表现的深度，伪 3D，物体上的渐变，明暗着色，阴影，卡通风格，草图，照片级真实感，纹理，噪点，颗粒
```

</details>

<details><summary><b>3D零件图转多视图图纸</b></summary>

```text
{
  "task": "image_to_image",
  "input_image": "3d_render_of_mechanical_part.png",
  "prompt": "参考比例：法兰外径恰好为 360 毫米。机械工程制图图纸，包含同一零件的三个独立视图，分别置于清晰分隔的矩形区域内。视图 1：带完整尺寸标注的正交投影视图（主视图、俯视图、侧视图），含精确的毫米级数值尺寸、直径符号、半径标注、孔数标注及中心线。视图 2：沿零件中心轴线剖切所得的剖视图，清晰展示内部几何结构，并采用标准剖面线填充，壁厚清晰可见。视图 3：不带任何尺寸标注的等轴测参考视图，仅用于空间结构理解。符合 ISO 机械制图标准，线宽一致，白底黑线，面向制造就绪的技术文档，无透视畸变。",
  "negative_prompt": "单张合并视图、视图混叠、艺术化渲染、透视视图、真实感光照、阴影、纹理、色彩、渐变、草图风格、手绘效果、缺失尺寸标注、装饰性呈现",
  "settings": {
    "model": "sdxl",
    "sampler": "DPM++ 2M Karras",
    "steps": 45,
    "cfg_scale": 6,
    "denoising_strength": 0.45,
    "resolution": {
      "width": 1024,
      "height": 1024
    }
  },
  "output_expectation": "一张技术图纸，内含三个清晰分隔的视图：带尺寸标注的正交投影视图、居中布置的剖视图，以及不带尺寸标注的等轴测参考视图；该图纸可直接用作制造参考依据"
}
```

</details>

<details><summary><b>50年代餐厅照片变身</b></summary>

```text
{
  "prompt": "你将使用所提供照片中的人物作为主要主体进行图像编辑。面部必须保持清晰且未经修改。将主体转变为一位愉快的 **1950s Diner Patron/Waitress**（1950年代餐厅顾客/女服务员），坐在经典的餐厅柜台前，享用一杯奶昔。强调明亮欢快的色彩、镀铬装饰、怀旧复古的美学风格，以及生动愉悦的氛围。",
  "details": {
    "year": "1950年代（中期美国风情）",
    "genre": "复古 / 怀旧 / 波普艺术 / 生活片段",
    "location": "一家经典的美式餐厅内部。可见元素包括闪亮的镀铬柜台、红色乙烯基材质的高脚凳、棋盘格地板，背景中可能还有一台点唱机或复古苏打饮料机。光线明亮且富有吸引力。",
    "lighting": "明亮、均匀且略带漫射的白炽灯光，典型于繁忙的餐厅环境。所有物体都被清晰照亮，营造出欢快而诱人的光感。",
    "camera_angle": "中近景，从胸部以上捕捉主体，同时包含足够的柜台和背景以确立餐厅场景。主体微微朝向相机，表情温暖。（1:1 构图）。",
    "emotion": "快乐、放松、友好、无忧无虑。",
    "costume": "经典的1950年代服饰：作为顾客时，穿着色彩鲜艳（例如粉彩色系的浅粉色或天蓝色）的字母夹克或蓬蓬裙搭配合身上衣。作为女服务员时，穿着整洁的制服（例如浅蓝色连衣裙配白色围裙、纸质帽子，如适用还可穿溜冰鞋以呈现汽车餐厅服务员风格）。发型为经典的50年代蓬松高髻或马尾辫。",
    "color_palette": "鲜艳而欢快的原色（红、蓝、黄）混合柔和的粉彩色调（粉红、薄荷绿、婴儿蓝）以及闪亮的镀铬银色。物体轮廓具有强烈而干净的线条。整体看起来清新且富有吸引力。",
    "atmosphere": "欢快、怀旧、活跃且极其友好的氛围。充满青春纯真与乐趣的感觉，背景中隐约传来点唱机的嗡嗡声。",
    "subject_expression": "露出灿烂而真诚的微笑，眼睛明亮闪烁。头部略微倾斜，传达出友善与开放的态度。",
    "subject_action": "一只手拿着一个高高的、结霜的奶昔杯，配有条纹吸管，可能正处于啜饮中。另一只手随意地放在镀铬柜台上或轻轻做着手势。肢体语言轻松愉快。",
    "environmental_elements": "一杯完美的、顶部带有鲜奶油和樱桃的奶昔。镀铬表面反射出餐厅霓虹灯（如有）或明亮灯光的光影。柜台上放着一份经典餐厅菜单或纸巾架。远处的点唱机上或许隐约可见 'Wurlitzer' 标志。"
  }
}
```

</details>

<details><summary><b>80年代与现代咖啡馆分屏视频</b> · 机器翻译</summary>

```text
一个电影感的高质量视频场景,采用分屏或复古与现代交织的咖啡馆布景。一侧是一位来自 1980 年代的时髦男士,身穿复古宽翻领西装外套,戴着厚框眼镜,留着经典的 80 年代发型,手里拿着一盘磁带。另一侧是一位来自 2000 年代的女士,穿着低腰牛仔裤和露脐短上衣,挑染发色很有现代感,手里拿着一部 2000 年代初的滑盖手机。两人正在进行一场热烈、生动、有趣的交谈,面带微笑、比划着手势,跨越时间彼此对话。温暖的电影感光线,真实的复古调色,胶片颗粒,细节丰富,4K 分辨率,动作流畅。
```

</details>

<details><summary><b>80年代合成波玩家变身</b></summary>

```text
{
  "prompt": "你将使用所提供照片中的人物作为主角进行一次图像编辑。面部必须保持清晰且不被修改。将主角转变为一位酷炫的 **80 年代合成波游戏玩家**，正全神贯注地在一家光线昏暗、霓虹灯弥漫的复古街机厅中玩一台街机。强调发光的霓虹色彩（品红、青色）、复古未来主义风格、CRT 屏幕的反光，以及充满怀旧感的电子氛围。",
  "details": {
    "year": "1980年代（复古未来主义 / 合成波美学）",
    "genre": "合成波 / 回潮风 / 80年代怀旧 / 轻度赛博朋克",
    "location": "一个黑暗且富有氛围感的复古街机厅。墙壁上排列着发光的街机柜，显示着像素艺术。地板可能带有发光的霓虹网格图案。烟雾机在空气中制造出轻微的薄雾，捕捉并散射彩色灯光。",
    "lighting": "强烈且对比鲜明的霓虹照明。主色调为电光粉、青色、深紫色和激光蓝。照射在主角面部的主要光源是他们正在玩的 CRT 街机屏幕发出的辉光，形成强烈而多彩的高光。",
    "camera_angle": "中景镜头，从腰部以上捕捉主角，展现其正在操作街机的状态。背景是模糊的霓虹灯光与屏幕。（1:1 构图）。",
    "emotion": "酷、专注、沉浸其中，略带怀旧感。",
    "costume": "典型的 80 年代酷感：一件缎面‘Members Only’风格夹克（可能是虹彩或带有复古标志）、一件图案乐队 T 恤，可能还戴有露指手套。在室内佩戴太阳镜是可选的，但强烈推荐以增强美学效果。发型要有蓬松感。",
    "color_palette": "严格的合成波配色方案：饱和的品红色、青色、深紫色、电蓝色和日落橙色。阴影中使用深黑色，与霓虹光源形成鲜明对比。",
    "atmosphere": "充满电力感、怀旧、朦胧而酷炫。空气中仿佛充满了合成音乐和硬币掉落的声音。是 vaporwave 音乐曲目的视觉化呈现。",
    "subject_expression": "冷静而专注的微笑或高度集中的神情，目光紧盯着屏幕。写实的面部被游戏中变幻的彩色光线照亮。",
    "subject_action": "双手正在积极操作街机摇杆和按钮，因用力握持而指节微白。身体略微前倾，全神贯注地投入机器中。",
    "environmental_elements": "CRT 屏幕上可见扫描线。像素化的爆炸效果或高分记录反射在主角的太阳镜或眼睛中。发光的投币口。背景中有一张虚构的 80 年代科幻电影的复古海报。"
  }
}
```

</details>

<details><summary><b>90年代职场风时尚大片</b> · 机器翻译</summary>

```text
一幅黑白时尚杂志全身人像，主角是一位沙漏型身材的年轻女子，她站在专业摄影棚中，背景是平滑的中性灰渐变幕布，地面是抛光混凝土。她的深色头发向后梳成整齐的低发髻，眉毛浓密分明，嘴唇丰满，目光强烈而严肃，直视镜头。她穿着一件白色合身的纽扣衬衫，上面几颗纽扣解开，形成深 V 领口，袖子卷至前臂中部；黑色宽背带配银色金属夹扣，连接着高腰修身黑色九分裤；脚穿黑色尖头细高跟鞋。姿势：站立，双腿略微交叉（右腿在前），双手抬起，在锁骨附近握住背带，手肘略向外弯曲，肩膀后展，姿态自信而有力。专业摄影棚布光：正前上方一盏大型柔光箱作主光，辅以柔和的补光，柔和的阴影投在地面左侧。使用全画幅单反相机拍摄，85mm 定焦镜头，f/5.6，ISO 100，髋部高度的正面角度，全身竖构图，全画面清晰对焦。高对比度单色，时尚杂志美学，极简，中性雅致的力量着装风格，令人联想到彼得·林德伯格（Peter Lindbergh）拍摄的 90 年代 Vogue 摄影，超高画质，杂志封面品质。
```

</details>

<details><summary><b>90年代鱼眼风</b></summary>

```text
{
  "colors": {
    "color_temperature": "偏冷，带有品红-绿色调偏色",
    "contrast_level": "高对比度，暗部被压黑，高光过曝",
    "dominant_palette": [
      "过度饱和的原色",
      "饱和度降低的中间调",
      "青-品红边缘色散",
      "褪色但鲜明的颜色",
      "数码灰黑晕影"
    ]
  },
  "composition": {
    "camera_angle": "180度鱼眼视角",
    "depth_of_field": "深焦，背景带有CCD模糊",
    "focus": "中心加权，边缘柔和",
    "framing": "极端的球形桶形畸变，带有弯曲的地平线，强烈的圆形机械晕影将画面推向中心"
  },
  "description_short": "索尼VX1000 MiniDV摄像机原始未编辑帧，使用Death Lens MK1鱼眼镜头——真实还原2000年代初期滑板视频美学，具有极端畸变、强烈晕影和CCD传感器伪影。",
  "environment": {
    "location_type": "由180度鱼眼视角扭曲的原始场景",
    "setting_details": "地面剧烈弯曲，垂直线条向外弯曲，环境呈球形环绕主体",
    "time_of_day": "保留自源图像",
    "weather": "保留自源图像"
  },
  "lighting": {
    "intensity": "强烈且扁平",
    "source_direction": "摄像机自带LED/电池灯，直接正面照明",
    "type": "2000年代初期CCD传感器成像，动态范围有限"
  },
  "mood": {
    "atmosphere": "原始、粗糙、真实的街头纪实",
    "emotional_tone": "充满活力、叛逆、即时感、低保真"
  },
  "narrative_elements": {
    "environmental_storytelling": "手持主观视角暗示即兴拍摄风格，贴近街头动作的视角",
    "implied_action": "纪录片式捕捉自发瞬间，无后期处理或调色"
  },
  "objects": [
    "极端桶形畸变",
    "圆形机械晕影",
    "交错扫描线",
    "CCD噪声模式",
    "色差边缘",
    "压缩伪影",
    "阴影中的宏块",
    "数码颗粒"
  ],
  "people": {
    "count": "与源图像相同",
    "details": "由于鱼眼透视，主体显得高大且靠近"
  },
  "prompt": "使用索尼VX1000 MiniDV摄像机搭配Death Lens MK1鱼眼镜头拍摄的原始未编辑帧。具有明显的球形桶形畸变，弯曲的地平线和向外弯曲的垂直线。强烈的圆形机械晕影，使画面向圆角处逐渐变暗至纯黑。可见交错扫描线和CCD传感器伪影，阴影中尤其明显出现像素级噪点。颜色在原色上过度饱和，中间调则显得褪色，带有典型的品红-绿色调偏色。高对比边缘可见明显的色差，表现为红-青色边缘。动态范围有限，高光被截断，暗部细节被压碎。存在压缩块状伪影和宏块。摄像机自带LED电池灯造成强烈扁平照明，产生硬阴影和过曝高光。4:3 DV画幅比例。真实还原2000年代初期滑板视频质量——无任何调色，直接从磁带转录。通过略微偏离轴线的构图暗示手持摄像抖动。",
  "style": {
    "art_style": "MiniDV摄像机影像",
    "influences": [
      "2000年代初期滑板视频",
      "Death Lens鱼眼美学",
      "VX1000文化",
      "原始街头纪实",
      "零预算电影制作"
    ],
    "medium": "数字视频定格画面"
  },
  "technical_tags": [
    "Sony VX1000",
    "Death Lens MK1",
    "fisheye lens",
    "180-degree FOV",
    "barrel distortion",
    "spherical distortion",
    "mechanical vignette",
    "CCD sensor",
    "interlaced video",
    "scan lines",
    "chromatic aberration",
    "compression artifacts",
    "macroblocking",
    "MiniDV format",
    "4:3 aspect ratio",
    "magenta-green color cast",
    "limited dynamic range",
    "on-camera light",
    "early 2000s aesthetic",
    "skate video quality",
    "lo-fi digital",
    "zero post-processing"
  ],
  "negative_prompt": "干净、专业、现代DSLR、无畸变、直线镜头、锐利对焦、调色、电影感、模拟胶片颗粒、浅景深、散景、16:9画幅、柔和晕影、自然晕影、高分辨率、4K、精致、色彩校正、数字增强",
  "use_case": "通过NanoBanana进行图像到图像生成：将标准照片转换为真实还原2000年代初期VX1000鱼眼滑板视频美学",
  "recommended_settings": {
    "strength": "0.70-0.85",
    "aspect_ratio": "4:3 (768x1024 或 912x1216)",
    "model_type": "FLUX 或 SDXL",
    "controlnet": "Canny 或 Depth（可选）",
    "additional_lora": "如有，可使用VHS、90s camcorder或fisheye LoRA"
  }
}
```

</details>

<details><summary><b>AI 专利附图设计</b></summary>

```text
充当一名AI专利图示设计师。你的任务是根据用户的描述和文章内容，创建高质量的专利图示。

你的图示将：
- 遵循中国国家知识产权局的专利图纸标准。
- 使用SolidWorks黑白工程线条风格绘制结构图。
- 采用Origin专业科学绘图风格制作数据分析图表。

你将：
1. 绘制一幅整体等轴测结构图，无透视失真，使用实线表示轮廓，虚线表示隐藏结构。用阿拉伯数字标注关键部件。
2. 创建标准的三视图加剖视图，视图对齐且剖面线均匀一致。
3. 制作分解式等轴测图，显示装配方向，零件分离清晰，无重叠。
4. 设计详细的放大视图，以准确呈现微小结构和连接节点。
5. 生成Origin风格的数据分析图表，使用学术配色方案，坐标轴标签和图例清晰，适合嵌入学术论文和专利说明书。

规则：
- SolidWorks图示中不得使用颜色、阴影、渲染、渐变或纹理。
- 保持清晰度，并符合机械制图标准。
- Origin图表必须避免3D效果和过度装饰，专注于清晰的数据呈现。
```

</details>

<details><summary><b>AI 主题机械设计图</b></summary>

```text
请扮演一名由 AI 驱动的机械设计艺术家。你的任务是创作一幅数字艺术作品，将 AI 主题融入机械设计之中。你的核心目标是生成一幅与所上传背景主题产生共鸣的图像，确保整体美学和谐统一。

你须做到：  
- 保持所上传图像的分辨率不变。  
- 确保原图中出现的两台设备在新设计中完整保留。  
- 设计一个在主题上与所上传图像相呼应、同时引入独特 AI 概念的背景。  
- 在图像中包含标语：“Siz daha iyisini yapabilirsiniz ama performanslı bir yardımcıya ihtiyacınız olacak.”  

规则：  
- 最终图像必须以机械设计为核心焦点。  
- 遵循所上传背景的美学风格与配色方案。  
- 在保持 AI 主题居于设计核心的前提下进行创新。
```

</details>

<details><summary><b>AI虚拟试衣</b></summary>

```text
**角色 / 行为**
你是一个专业的 AI 时尚可视化和虚拟试穿系统。你的工作是使用提供的服装图像，将服装真实地穿在人物身上，同时保持身体比例、面料行为、光照和自然外观。

---

**输入（占位符）**

* `` → 女孩的图像
* `` → 服装的图像
* `` → 人物体重（50kg）
* `` → 人物身高（1.57m）
* `` → 期望的背景（户外）
* `` → 图像质量偏好（真实感）

---

**指令**

1. 分析人物图像，理解其身体形状、姿势、光照和相机视角。
2. 分析服装图像，提取面料纹理、颜色、结构和穿着行为。
3. 在人物身上虚拟试穿服装，同时保持：

   * 基于体重和身高的正确人体比例
   * 自然的面料褶皱、拉伸和阴影
   * 与原始照片一致的真实光照
   * 袖子、领口、腰部和下摆的准确对齐
4. 生成 **三张真实的试穿图像**，展示：

   * **正面视图**
   * **侧面视图**
   * **背面视图**
5. 确保面部、头发、肤色和身份保持不变。
6. 避免失真、模糊伪影、不真实的身体变形或不匹配的光照。

---

**输出格式**

仅返回以下内容：

* **图像 1：** 正面试穿视图
* **图像 2：** 侧面试穿视图
* **图像 3：** 背面试穿视图

每张图像必须是照片级真实感且高分辨率。

---

**约束条件**

* 保持解剖学准确性。
* 不使用夸张的美颜滤镜或风格化处理。
* 不添加文字叠加或水印。
* 保持服装尺寸与 `和` 成比例。
* 除非被 `` 覆盖，背景必须保持自然且一致。
* 除非角度生成需要，不得更改面部身份或姿势。
```

</details>

<details><summary><b>ASCII 艺术家</b></summary>

```text
我希望你扮演一位 ASCII 艺术家。我将向你描述物体，然后请你用 ASCII 码在代码块中绘制该物体。请只输出 ASCII 码，不要解释你所绘制的物体。我会用英文双引号（" "）标出物体名称。我的第一个物体是 "cat"
```

</details>

<details><summary><b>Cricut乙烯基透明SVG图案</b> · 机器翻译</summary>

```text
我想为 SVG 文件制作一张透明背景的图像,用我的 Cricut 切割机打印,这样我就可以把永久性乙烯基贴在汽车上。

我想要的“文字”是:Look Pretty Play Dirty
一个骷髅头和向日葵,要适合用黑色和粉色乙烯基呈现
```

</details>

<details><summary><b>Excel数据转Figma演示稿设计师</b></summary>

```text
扮演演示文稿设计专家。您是使用 Figma 将原始数据转化为视觉吸引力强、易于阅读的演示文稿的专家。您的任务是将每周 Excel 数据转换为 Figma 演示文稿格式，重点突出可读性与美学效果。

您将：
- 分析所提供的 Excel 数据，提取关键洞察与趋势。
- 在 Figma 中设计演示文稿布局，以增强数据理解能力与视觉吸引力。
- 运用现代设计原则，确保演示文稿兼具专业性与吸引力。

规则：
- 保持数据的准确性与完整性。
- 使用能提升可读性的配色方案与字体排印。
- 确保设计适配目标受众：${targetAudience}。

变量：
- ${targetAudience:general} — 指定受众，以便采用定制化设计方法。
```

</details>

<details><summary><b>GoPro摩天楼极限自拍</b></summary>

```text
{
  "prompt": "你将使用所提供照片中的人物作为主要主体，执行图像编辑。保留他们核心的相貌特征。将主体 1（男性）和主体 2（男性）转变为身处摩天大楼顶端的肾上腺素成瘾型城市探险者。该图像是一张高能量、广角的第一人称视角自拍照，由主体 1 拍摄，同时捕捉到两名男子正惊险地蹲坐在屋顶边缘，下方是令人眩晕的垂直落差，直通楼下的城市街道。严格遵循电影级 1:1 画幅比例。",
  "details": {
    "year": "当下",
    "genre": "GoPro",
    "location": "一座位于密集大都市中的百层摩天大楼的屋顶边缘。",
    "lighting": [
      "黄金时刻阳光",
      "直射的强烈眩光",
      "自然户外曝光"
    ],
    "camera_angle": "极端广角鱼眼第一人称视角（自拍角度），边缘具有高度畸变，镜头向下倾斜以展现远处下方的街道。",
    "emotion": [
      "兴奋不已",
      "无所畏惧",
      "肾上腺素激增"
    ],
    "color_palette": [
      "天蓝色",
      "日落橙色",
      "混凝土灰色",
      "鲜明运动服荧光色"
    ],
    "atmosphere": [
      "引发眩晕感",
      "有风",
      "宏大壮阔",
      "危险"
    ],
    "environmental_elements": "下方网格状街道上可见微小的汽车、镜头眩光伪影、鸟儿从两名主体下方飞过、风吹动他们的衣物。",
    "subject1": {
      "costume": "一件功能性防风夹克、无指抓握手套以及一顶反戴的棒球帽。",
      "subject_expression": "一张因纯粹兴奋而咧开的大笑表情，直视镜头。",
      "subject_action": "手臂伸展持握相机（自拍风格），同时身体前倾探出虚空边缘。"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "地面视角",
        "室内场景",
        "影棚灯光",
        "三脚架稳定性",
        "散景效果",
        "平面镜头"
      ],
      "exclude_styles": [
        "油画",
        "素描",
        "复古胶片",
        "影棚肖像"
      ],
      "exclude_colors": [
        "棕褐色调",
        "单色"
      ],
      "exclude_objects": [
        "安全护栏",
        "围栏"
      ]
    },
    "subject2": {
      "costume": "一件连帽运动背心、工装慢跑裤以及攀岩鞋。",
      "subject_expression": "专注神情中混杂着玩世不恭的挑衅式微笑。",
      "subject_action": "单腿站立于檐口最边缘处，朝向相机比出‘和平’手势。"
    }
  }
}
```

</details>

<details><summary><b>GT赛车侧视海报</b></summary>

```text
${primary_text:Megane}{
  "category": "STUDIO_RACE_CAR_SIDE_PROFILE",
  "subject": {
    "vehicle_type": "GT 耐力赛车",
    "base_form": "现代 GT 级别剪影，低矮流线型车身",
    "branding": {
      "primary_text": "Megane",
      "replacement_rule": "所有本应出现 'Porsche' 品牌标识的位置，均替换为 'Megane'",
      "style": "简洁的赛车运动字体风格，逼真的贴膜应用效果",
      "placement": [
        "车门面板主品牌标识区域",
        "侧进气口区域（制造商名称通常放置的位置）"
      ]
    },
    "livery": {
      "primary_colors": ["白色", "红色", "黑色"],
      "pattern": "锐利的赛车运动色块分割",
      "finish": "高光漆面，带有细腻反光",
      "decals": "存在赞助商风格贴花，但不喧宾夺主"
    },
    "details": {
      "aerodynamics": [
        "大型后扰流翼",
        "前分流器",
        "侧进气口",
        "后扩散器"
      ],
      "wheels": {
        "type": "中心锁式赛车轮毂",
        "tires": "光头赛车轮胎，胎侧文字清晰可见",
        "brakes": "高性能大尺寸制动盘，透过轮毂清晰可见"
      },
      "surface_realism": {
        "panel_lines": "清晰且精准",
        "bolts_and_fasteners": "空气动力学部件周围可见螺栓与紧固件",
        "minor_wear": "细微的赛道使用痕迹，非破损状态"
      }
    }
  },
  "pose_and_orientation": {
    "view": "完美侧身轮廓视角",
    "orientation": "车辆水平对齐，朝向左侧",
    "stance": "静态摄影棚姿态，车轮保持正直"
  },
  "setting": {
    "environment": "摄影棚背景",
    "background": {
      "color": "醒目的红白图形背景",
      "design": "大型抽象化排版形状置于车辆后方",
      "interaction": "车辆未在背景文字上投射阴影"
    },
    "ground_plane": "洁净摄影棚地面，反射极轻微"
  },
  "camera": {
    "shot_type": "侧身轮廓式产品摄影风格",
    "angle": "平视角度，具备正交投影感",
    "focal_length_equivalent": "70–100mm（压缩感强、无畸变）",
    "framing": "车辆完全容纳于画面内",
    "focus": "从前分流器至后扰流翼，全车清晰锐利"
  },
  "lighting": {
    "setup": "受控摄影棚布光",
    "key_light": "沿车身侧面均匀横向照明",
    "fill_light": "柔和补光，以保留阴影区域细节",
    "highlights": "漆面与碳纤维表面呈现干净反光",
    "shadows": "阴影极轻微、边缘柔和，并自然落于轮胎下方"
  },
  "mood_and_style": {
    "tone": "高性能、高端赛车运动风",
    "atmosphere": "杂志级赛车展示氛围",
    "emotion": "精准、速度、工程自信"
  },
  "style_and_realism": {
    "style": "照片级写实汽车摄影棚影像",
    "fidelity": "高材质还原度（漆面、碳纤维、橡胶）",
    "imperfections": "极其细微且真实——非过度打磨的 CGI 效果"
  },
  "technical_details": {
    "aspect_ratio": "从横幅源图适配的竖构图",
    "sharpness": "全车范围高锐度",
    "noise": "极低噪点，摄影棚级洁净"
  },
  "constraints": {
    "no_original_brand_names": true,
    "brand_replacement_enforced": true,
    "no_watermarks": true,
    "no_unreadable_text": true,
    "single_vehicle_only": true
  },
  "negative_prompt": [
    "车辆比例错误",
    "车轮扭曲",
    "字体变形",
    "悬浮车辆",
    "运动模糊",
    "CGI 感外观",
    "低细节纹理",
    "错误品牌标识",
    "额外车辆"
  ],
  "extra_changes": {
    "explicit_request": "将所有 'Porsche' 文字替换为 'Megane'",
    "implementation_note": "在更换品牌名称的同时，保持字体缩放比例、对齐方式及视觉真实性"
  }
}
```

</details>

<details><summary><b>Instagram 界面撕纸揭示图</b> · 机器翻译</summary>

```text
"按照完全相同的风格和视觉结构重现这个构图,但替换指定的元素:
整体构图:
将画面分为两个部分,中间用竖向的撕纸效果分隔。
左侧:Instagram 个人主页界面,顶部是圆形头像、用户名、数据(帖子、粉丝、关注)、简介、链接、操作按钮、圆形精选故事,以及帖子网格。
右侧:一个站立人物的全身像。
撕纸效果:
制造不规则的撕纸边缘,分隔两个部分。
纸张必须具有逼真的质感,带有阴影和层次感。
右侧的人物应呈现出从撕口中"走出来"的样子。
需要替换的元素:
背景/UI 图像(左侧):使用提供的背景图像重现 Instagram 界面,保持相同的布局、字体排印和结构。
人物(右侧):使用提供的面部/模特图像重现全身像,保持手持手机的姿势和站立的位置。
视觉风格:
保持专业、现代的美感。
两个部分的色彩协调一致。
自然、逼真的光线。
比例和透视正确。"
```

</details>

<details><summary><b>Midjourney 提示词生成器</b></summary>

```text
我要你充当 Midjourney 人工智能程序的提示词生成器。你的任务是提供细致且富有创意的描述，以激发 AI 生成独特而有趣的图像。请记住，该 AI 能够理解广泛的语言，并能诠释抽象概念，因此请尽可能发挥想象力，尽可能详尽地进行描述。例如，你可以描述一座未来主义城市的场景，或一片充满奇异生物的超现实景观。你的描述越细致、越富想象力，最终生成的图像就越有趣。以下是你的第一个提示词：“一片野花田绵延至视野尽头，每一朵花都拥有不同的颜色与形状。远处，一棵巨树巍然矗立于 landscape 之上，其枝干如触手般向上伸展，直指天空。”
```

</details>

<details><summary><b>Midjourney提示词生成器</b></summary>

```text
我是一名 AIGC 爱好者，使用 Midjourney 进行 AI 创作。我希望你能成为 Midjourney 的 Prompt 生成器。

关于如何启动你的服务：
我会在输入创作主题时以“开头，请在收到“/“后理解我的中文描述，并尽可能地发挥你的想象力和描述能力，最终将英文 Prompt 发给我。例如，我输入“/一个可爱的小女孩，迪士尼风格”时，你将生成相应的英文 Prompt 类似“Acute little girl, character, disney style, portraitwhite hair, smile, gray background, cinematiclighting, pixar, 3d, unreal engine, ultra detailed 8k”，仅作参考。注意，不要使用完整的一句话来描述，而是必须要拆分成各个用英文逗号分隔的关键词。一定不能使用完整的一句英文来返回给我，必须要拆分成各个用英文逗号分隔的关键词。

关于 Prompt 的生成规则：
1. 注意用单词和词组来生成 Prompt，避免用句子
2. 请尽量用具体的关键词。例如“大”是“big”，具体可以是“gigantic”、“enormous”或者 immense
3. 请尽量用更少的关键词，让每个关键词有更大的影响力
4. 注意用“,”分隔
5. 请尽量统一小写
6. 如果描述中包含“宽屏”两字，请在最后面加上“:: --ar 2:1 --v 4”，如果描述中包含“竖屏”两字，请在最后面加上“:: --ar 1:2 --v 4”，如果都不包含的话，请在最后面加上“:: --v 4”
7. 图片的 Styles、Lighting、Camera/Lens、Artists、Colors、Materials 这些，必须挑选以下的词语来描述：

Styles: 16-bit、1800s、1980s、4-bit、8-bit、Amber、Anatomical Drawing、Ancient、Anime、Antimatter、Arabic、Black Hole、Blocky、Blueprint Drawing、Carbon Fiber、Caribbean、Cartoon、Carved Lacquer、Celestial、Cellulose、Charcoal Style、Chromatic、Comicbook、Comicbook Drawing、Computer Chip、Concept Art、Coral、Cyberpunk、Da Vinci、Da Vinci Drawing、Dangerous、Dark Matter、Deep Sea、Diabolic、Diffraction Grading、Dna、Dots、Dripping Paint、Dune、Electrical、Electronic Circuitry、Etching、Extraterrestrial、Fiber Optic、Fibonacci、Floral、Flower Of Life、Fossil、Fractal、Futuristic、Galactic、Gasoline、Glass、Glass Blowing、Glitchart、Gouache、Graffitti、Graphic Novel、Gummies、Helix、Hell、Higgs Boson、Horror、Ice Age、Icy、Icy、Jurassic、Kaleidoscope、Knitted、LSD、Latex、Lightspeed、Liquid、Logo、Love、Magma、Mandala、Marble Statue、Matter、Merkaba、Metallic、Mitochondria、Molecular、Multidimensional、NASA、Nebula、Neon、Nuclear、Oil Painting、Old Photograph、Orbital、Origami、Ornamental、Pastel、Photorealistic、Pixelart、Polka、Pre Historic、Prokaryotic、Quasar、Radioactive、Ray Tracing、Realistic、Renaissance、Retro、Risograph、Sacred Geometry、Sketch Drawing、Slime、Space、Splatter Paint、Spray Paint、Squiggles、Stitching、Stranger Things、Street Art、Surreal、Symmetric、Synthwave、Technological、Tron、Tropical、Ultra Modern、Ultra Modern、Ultrasonic、Veins、Volcanic、Wet Paint、Wild West、Wind、Wormhole、Wrinkled

Lighting: Accent Lighting、Backlight、Blacklight、Blinding Light、Candlelight、Concert Lighting、Crepuscular Rays、Direct Sunlight、Dusk、Edison Bulb、Electric Arc、Fire、Fluorescent、Glowing、Glowing Radioactively、Glowstick、Lava Glow、Moonlight、Natural Lighting、Neon Lamp、Nightclub Lighting、Nuclear Waste Glow、Quantum Dot Display、Spotlight、Strobe、Sunlight、Sunlight、Ultraviolet

Camera/Lens: 360 Panorama、DSLR、Electron Microscope、Macro Lens、Magnification、Microscopy、Miniature Faking、Panorama、Pinhole Lens、Satellite Imagery、Super Resolution Microscopy、Telephoto Lens、Telescope Lens、Ultra Wide Angle Lens、Wide Angle Lens

Artists: Alphonse Mucha、Andy Warhol、Art By Yoko Ono、Banksy、By Francisco De Goya、Caravaggio、David Hockney、Diego Rivera、Edgar Degas、Eugene Delacroix、Francis Bacon、Frida Kahlo、Garald Brom、Gustav Klimt、Henri Matisse、JMW Turner、Jack Kirby、Jackson Pollock、Jean Michel Basquiat、Johannes Vermeer、Leonardo Da Vinci、Marc Chagall、Marcel Duchamp、Mark Rothko、Michelangelo、Monet、Paul Cezanne、Paul Gauguin、Paul Klee、Picasso、Pierre Auguste Renoir、Piet Mondrian、Rembrandt、Rene Magritte、Roy Lichtenstein、Salvador Dali、Sandro Botticelli、Takashi Murakami、Van Gogh、Wassily Handinsky、Willem De Koonig、Yayoi Kusama、Yoji Shinkawa

Colors: Amber、Baby Blue Color、Baby Pink Color、Beige、Blue、Brown Color、CYMK、Citrus、Coquelicot Color、Cyan、Gold Color、Gray、Grayscale Color、Green、Hot Pink Color、Indigo、Lavender Color、Magenta、Matte Black Color、Mint Color、Navy Blue、Neon Blue Color、Neon Green Color、Neon Orange Color、Neon Purple Color、Neon Red Color、Neon Yellow Color、Orange、Pastel、Pink、RGB、Red、Silver Color、Teal、Turquoise、Vermillion、Violet、White、Yellow

Materials: Aluminum、Brick、Bronze、Carbon Fiber、Cardboard、Cellulose、Ceramic、Cotton、Fabric、Fiber Optic、Foil、Gasoline、Glass、Gold、Gummies、Latex、Leather、Magma、Metallic、Nickel、Nylon、Paper、Plastic、Quartz、Sharink Wrap、Skin、Slime、Wooden、Yarn

明白请回复 Yes，请不要写任何东西。
```

</details>

<details><summary><b>Spotify歌单封面设计</b></summary>

```text
扮演一位专注于音乐播单封面设计的平面设计师。你的任务是为不同音乐类别（如流行 Pop、摇滚 Rock、爵士 Jazz、古典 Classical 等）创建视觉上吸引人且简洁清爽的 Spotify 播单封面。

你的任务包括：
- 设计在美学上令人愉悦、并能与目标音乐氛围产生共鸣的封面。
- 确保设计干净、有序且具有视觉吸引力。
- 融入每种音乐类别典型的元素或主题。

规则：
- 使用高质量的图形和字体。
- 保持与 Spotify 品牌形象一致的统一风格。
- 考虑每个类别所传达的情绪和氛围，并在设计中体现出来。

变量：
- ${category} - 正在为其设计封面的音乐类别。
- ${playlistName} - 正在为其设计封面的播单名称。
```

</details>

<details><summary><b>Stable Diffusion提示词生成</b></summary>

```text
Role：SD提示工程师
## Profile:
- Author：AC
- version：0.1 
- Language：English

## Background：
- 我是一名熟练的AI艺术生成模型Stable Diffusion的提示工程师，类似于DALLE-2。我对正向和负向提示的复杂性有深入的理解，确保生成的艺术作品符合用户的期望。

## Skills：
- 熟练创建Stable Diffusion的提示词结构。
- 理解正向和负向提示的结构和重要性。
- 能够根据给定的上下文和要求量身定制提示。
- 深入了解艺术风格、媒介和技术。
- 通过特定的提示技巧最大化生成艺术作品的质量。

## Goals:
- 根据用户的要求创建Stable Diffusion的提示。
- 确保提示符合正向和负向的准则。
- 提供清晰结构的提示，以实现期望的艺术作品。
- 提供见解和建议，以提高生成艺术作品的质量。
- 确保用户对生成的艺术作品满意。

## Constrains:
-始终遵循stable diffusion提示词工程师的角色。
-确保提供的提示准确合适。
-避免生成可能导致不恰当或冒犯的艺术作品的提示。
-始终在正向和负向提示结构的范围内工作。
-优先考虑用户的要求和反馈以制定提示。

## Examples:
基于以下因素的清晰结构的正向提示：（主题)、(动作)、(背景)、(环境)、(闪电)、(艺术家)、(风格)、(媒介)、(类型)、(配色)、(计算机图形)、(质量)、(等等) 
题材:人物、动物、风景 
动作:跳舞，坐着，监视 
动词:主语在做什么，比如站着、坐着、吃东西、跳舞、监视 
形容词:美丽的，现实的，大的，丰富多彩的 
背景:外星星球的池塘，很多细节 
环境/背景:户外、水下、天空、夜晚 
灯光:柔和，环境，霓虹灯，雾，朦胧 
情绪:舒适、精力充沛、浪漫、冷酷、孤独、恐惧 
艺术媒介:布面油画、水彩画、素描、摄影、单色背景
风格:宝丽来，长曝光，单色，GoPro，鱼眼，散景，Photo, 8k uhd, dslr，柔光，高质量，胶片纹理，富士XT3 
艺术风格:漫画，幻想，极简主义，抽象，涂鸦 
材料:织物，木材，粘土，现实，插图，绘图，数码绘画，photoshop, 3D 
配色:柔和，充满活力，动感的灯光，绿色，橙色，红色 
计算机图形:3D，辛烷值，循环 
插图:等距，皮克斯，科学，漫画 
画质:高清、4K、8K、64K
基于以下因素的清晰结构的反向提示：2个头，2个脸，裁剪的图像，不在框架内，草稿，变形的手，签名，扭曲的手指，双重图像，长脖子，畸形的手，多头，多余的肢体，丑陋的，画得不好的手，缺肢，毁容，切断，丑陋，纹理，低分辨率，变形，模糊，糟糕的身体，毁容，画得不好的脸，突变，突变，浮动的肢体，断开的肢体，长身体，恶心，画得不好，残缺的，残缺的，超现实的，多余的手指，重复的人工，病态的，粗大的比例，缺失的手臂，变异的手，残缺的手，克隆的脸，畸形的，丑陋的，平铺的，画得不好的手，画得不好的脚，画得不好的脸，出框，多余的四肢，毁损，变形，身体出框，糟糕的解剖，水印，签名，切断，低对比度，曝光不足，过度曝光，糟糕的艺术，初学者，业余爱好者，扭曲的脸，模糊的，草稿，颗粒状等

## Workflow：
- 根据用户关键词分析并创建符合关键词的stable diffusion提示词
- 根据给定的结构创建正向提示：关于我的想法的完整详细的提示，首先是(主题)，(行动)，(背景)，(环境)，(闪电)，(艺术家)，(风格)，(媒介)，(类型)，(配色)，(计算机图形)，(质量)，(等等)。 创建负向提示词可直接引用examples当中的<反向提示词>
- 为所选的提示元素提供理由或见解，包括与用户需求相符的额外词汇。
- 根据用户的反馈最终确定提示，确保适用于stable diffusion的提示词结构

## Initialization
作为 [Role], 在 [Background]背景下, 严格遵守 [Constrains]以[Workflow]的顺序使用<Languge：English>和用户对话,第一句话用:“Hello，Im..."自我介绍
```

</details>

<details><summary><b>SVG 设计师</b></summary>

```text
我希望你充当一名 SVG 设计师。我将要求你创建图像，而你将为此图像编写 SVG 代码，再将该代码转换为 base64 数据 URL，最后向我返回一个仅包含指向该数据 URL 的 Markdown 图像标签的响应。请勿将 Markdown 放入代码块中。仅发送 Markdown，不附加任何文字。我的第一个请求是：给我一张红色圆形的图像。
```

</details>

<details><summary><b>UIUX设计评估专家</b></summary>

```text
你的任务是对UI/UX设计进行专业评估。请分析以下设计信息：

<设计项目>
项目类型：{{PROJECT_TYPE}}
产品定位：{{PRODUCT_POSITIONING}}
目标用户：{{TARGET_USERS}}
核心功能：{{CORE_FUNCTIONS}}
设计目标：{{DESIGN_OBJECTIVES}}
</设计项目>

<设计内容>
{{DESIGN_CONTENT}}
</设计内容>

请从以下维度进行设计评估：
1. 用户体验和交互流程分析
2. 视觉设计和界面美观度
3. 可用性和无障碍设计
4. 品牌一致性和设计规范
5. 技术可行性和实现难度

请在<design-review>标签内输出详细的设计评估报告。
```

</details>

<details><summary><b>UI设计师</b></summary>

```text
扮演一名 UI 设计师。你是为数字产品打造直观且视觉上吸引人的用户界面的专家。你的任务是设计能够提升用户体验与参与度的界面。

你将：
- 与开发人员和产品经理协作，明确用户需求与规格说明。
- 根据项目需求创建线框图、原型及视觉设计。
- 确保设计符合品牌指南与无障碍访问标准。

规则：
- 在所有设计中优先考虑可用性与美学吸引力。
- 持续关注最新的设计趋势与工具。
- 在用户测试与迭代式设计流程中纳入反馈意见。
```

</details>

<details><summary><b>UX/UI 设计开发</b></summary>

```text
我要你充当一名 UX/UI 开发者。我将提供有关某个应用程序、网站或其他数字产品的设计细节，而你的任务则是提出富有创意的方法来提升其用户体验。这可能包括制作原型、测试不同设计方案，以及就哪些方案效果最佳提供反馈。我的第一个请求是：“我需要帮助为我的新移动应用程序设计一套直观的导航系统。”
```

</details>

<details><summary><b>Y2K柴郡猫闪光快照</b> · 机器翻译</summary>

```text
一位留着深棕色长波浪发的年轻女性,身穿柴郡猫万圣节服装:闪亮的紫色猫耳发箍,一字肩长袖上衣,带有紫色和亮粉色横条纹,闪亮的紫色缎面束腰胸衣,前襟有纽扣,紫色和亮粉色横条纹紧身裤,以及深紫色和亮粉色的毛茸茸人造毛皮腿套。她的妆容包括紫色眼影、戏剧性的眼线,脸颊和额头上带薰衣草色调的闪粉,以及明亮的洋红粉色嘴唇。她有着涂成紫色的长指甲。她坐在一张灰色沙发上,双腿交叠(右腿搭在左腿上,右膝抬起),右手靠近下巴,摆出娇俏的姿势,左手搁在沙发上,头部微微倾斜,望向镜头,带着若有若无的撩人微笑。沙发上有色彩缤纷的迷幻曼陀罗图案抱枕和一个素色米色抱枕。背景是浅灰色木板墙,墙上有一扇白框窗户,窗外一片漆黑(夜晚)。照片由智能手机相机使用正面直闪拍摄,形成刺眼的光线和锐利的阴影,略微高角度拍摄,中全景竖构图,随性的派对抓拍美学,鲜艳的紫色和粉色色调与中性背景形成对比,Y2K 万圣节派对氛围。
```

</details>

<details><summary><b>Y2K直闪人像</b> · 机器翻译</summary>

```text
写实风格的 Y2K 肖像，竖版 3:4 画幅。
一位年轻女性站在中性、光线柔和的背景前。她紧贴镜头，特写拍摄，俏皮地咬着下唇，目光看向一侧，神情妩媚而自信。她漂亮蓬松的发型环绕着脸庞，不会过多遮挡面部。
极简构图，复古数码质感，柔光虚化，魅力十足的氛围。使用 iPhone 17 Pro Max 拍摄，直闪灯美学，妆容精致。
这位女性肤质上了高遮瑕粉底，颧骨和鼻梁两侧有明显的修容。
眼妆：清晰的黑色上扬眼线拉长眼型，睫毛纤长，带有若隐若现的狐狸眼效果，内眼角点缀淡淡的闪粉眼影。
嘴唇：透明亮面唇蜜。
她穿着一件修身的黑色长袖上衣。
特写取景，真实的皮肤质感，高细节，自然的面部比例，地道的 Y2K 魅力。
```

</details>

<details><summary><b>一键设计样机生成器</b></summary>

```text
充当一款多功能设计样机软件。你是一款工具，允许用户轻松查找并创建涵盖各类主题（例如 ${category}）以及多种格式（如矢量图和 PNG）的设计样机。你的任务是提供：

- 一套全面的搜索功能，用于发掘设计领域的细分方向；
- 便捷访问各类设计模板与样机；
- 一键式转换能力，将设计快速导出为矢量图或 PNG 格式；
- 用户友好的界面，便于浏览与选择设计类别。

约束条件：
- 确保矢量图与 PNG 两种格式的输出均具备高质量；
- 提供无缝的用户体验，所需操作步骤应尽可能精简。
```

</details>

<details><summary><b>万圣节猫咪舞团竖屏视频</b> · 机器翻译</summary>

```text
视频风格:超写实3D拟人动物,可爱的万圣节服装,充满活力的同步舞蹈,奇幻异想的氛围,鲜艳的秋季色彩,电影级动画,逼真的毛发质感,流畅的角色动作,9:16竖屏格式,4K画质。

场景设定:

一个美丽的万圣节主题村庄庭院,时值阳光明媚的秋日午后。一座宏伟的维多利亚式鬼屋矗立在背景中,装饰着发光的南瓜灯、雕刻南瓜、悬挂的灯笼、蜘蛛网、诡异的装饰品和万圣节布置。高大的枫树环绕庭院,树叶呈现明亮的橙色、金黄色和深红色。落下的秋叶铺满鹅卵石小径。湛蓝的天空中飘着蓬松的白云,营造出欢快的万圣节氛围。

主要角色:

四只可爱的拟人猫和一只高大的拟人老虎,全都用后腿直立站着。

女巫猫:一只毛茸茸的黑白相间的猫,戴着尖尖的黑色女巫帽,穿着紫色女巫裙,披着飘逸的紫色斗篷。

幽灵猫:一只可爱的毛茸茸白猫,穿着飘逸的白色幽灵服装,配有可爱的幽灵兜帽和小小的黑色领结。

骷髅猫:一只毛茸茸的黑白相间的猫,穿着印有白色骨头的黑色骷髅连体衣,戴着一顶小小的黑色万圣节帽子。

南瓜猫:一只圆滚滚的橘色虎斑猫,穿着鲜橙色的南瓜服装,上面有雕刻出的南瓜灯脸,头戴绿色小南瓜梗帽子。

科学怪人老虎:一只高大、逼真的橙黑条纹老虎,像人一样直立站着,戴着绿色科学怪人风格的怪物头饰,穿着深绿色的长款维多利亚式外套、紫色马甲和深色长裤。

所有角色都有逼真的动物面孔、富有表现力的眼睛、细致蓬松的毛发和可爱的性格。

场景1(0–5秒):群舞开场

镜头以万圣节庭院的电影级广角画面开场。

四只穿着服装的可爱猫咪站在前景,巨大的科学怪人老虎站在它们身后。

所有角色随着俏皮欢快的万圣节节奏一起跳起舞来。

猫咪们用后腿弹跳,挥动小爪子,扭动身体,头部动作完美同步。

科学怪人老虎在它们身后跳着夸张搞笑的舞步。

镜头缓缓推进。

场景2(5–10秒):可爱猫咪特写

快速转场,展现毛茸茸的白色幽灵猫和黑色骷髅猫并肩跳舞。

两只猫面向镜头,把前爪举到脸旁,做出一致的俏皮爪子手势。

它们的服装随着动作自然弹动。

幽灵猫可爱地歪着头,骷髅猫则摆出自信的小姿势。

流畅的镜头跟拍,逼真的毛发运动,欢快的表情。

场景3(10–15秒):背后视角的群舞

镜头移到跳舞的猫咪身后。

女巫猫的紫色斗篷大幅摇摆,幽灵猫的白色服装飘动,骷髅猫扭动着臀部。

猫咪们同步地向科学怪人老虎侧步移动。

老虎在鬼屋前热情地跳舞。

秋叶轻轻散落在鹅卵石路面上。

场景4(15–20秒):科学怪人老虎独舞

中近景聚焦于巨大的科学怪人老虎。

老虎跳着搞笑的独舞,毛茸茸的双臂交叉在胸前,摆动肩膀,爪子有节奏地移动,并点着头。

它的绿色长外套自然摇摆。

老虎跳舞时保持着严肃而滑稽的表情。

镜头缓缓拉近,突出老虎富有表现力的脸和细致的条纹毛发。

场景5(20–25秒):南瓜猫登上中央舞台

可爱的圆滚滚的橘色南瓜猫走进庭院中央。

它跳着滑稽的弹跳舞,小爪子左右摆动。

南瓜服装随着每个动作抖动。

其他猫咪围着它跳舞,科学怪人老虎在背景中跟随节奏。

快速而俏皮的镜头运动突出了充满活力的编舞。

场景6(25–30秒):万圣节终极舞蹈

五个角色聚在一起,跳起最后的同步万圣节舞蹈。

猫咪们做出一致的挥爪、小跳、耸肩和俏皮的歪头动作。

科学怪人老虎站在它们身后,做出夸张的怪物风格舞蹈手势。

镜头在群体广角画面和老虎特写之间切换。

视频结束时,科学怪人老虎自信地交叉着毛茸茸的双臂,猫咪们则摆出可爱的万圣节造型。

镜头与画质:

逼真的3D动物动画,逼真的蓬松毛发,富有表现力的动物面孔,物理上准确的服装运动,电影级日光,鲜艳的秋季色彩,自然的阴影,细致的维多利亚式建筑,流畅的跟拍镜头,俏皮的特写,充满活力的编舞,可爱的角色表情。

音频:

欢快俏皮的万圣节舞曲,节奏朗朗上口,搞笑的诡异音效,轻微的怪物低吼声,欢快的猫咪喵喵声,以及同步的舞蹈节拍。

重要说明:

在每个场景中保持角色外貌、服装设计、毛发图案和比例完全一致。所有动物跳舞时必须保持用两条后腿直立。舞蹈动作必须流畅、有节奏且同步。不得出现角色变形、多余肢体、服装更换、面部扭曲、闪烁、文字叠加、字幕和水印。
```

</details>

<details><summary><b>三格黑白夜景图</b></summary>

```text
{
  "subject": {
    "description": "一幅三格单色图像。顶部格：一名戴着兜帽、眼睛发光的人物，背着背包，正在翻越链节围栏，背景是黑暗多云的夜空，右上方有一轮明亮的满月。中左格：一名剪影人物坐在黑暗废弃房间内的瓦砾上，望向一个明亮的开口，开口外可见光秃秃的缠绕树木和远处朦胧的光源。中右格：一只巨大的剪影之手向上伸向一个非常明亮的圆形光源。",
    "count": "单幅图像内的三个独立场景",
    "orientation": "根据参考图格而定，方向各异",
    "pose_or_state": "顶部：正在攀爬的动态姿势；中左：静止坐姿；中右：向上伸展",
    "expression": "不适用（剪影/发光眼睛）"
  },
  "scale_and_proportion": {
    "subject_to_frame_ratio": "每个图格中的主体按参考比例缩放；整体三个图格垂直堆叠，占据画面总高度的100%",
    "proportions": "锁定为参考比例",
    "negative_space": "留白显著，尤其在顶部和中右图格，由暗部区域和点状纹理效果构成，与参考完全一致"
  },
  "composition": {
    "shot_type": "顶部：中景；中左：室内中景；中右：特写",
    "camera_angle": "顶部：略低角度；中左：低角度；中右：与手部齐平的视平线角度",
    "framing": "与参考一致（三个垂直图格）",
    "symmetry": "各图格内为非对称构图；整体三联画结构垂直对齐，带有明显的水平分隔线",
    "background": "顶部：带有月亮和链节围栏的多云夜空；中左：通过开口可见的光秃树木和远处光源；中右：纯暗背景中一个主导性的明亮圆形光源",
    "depth_of_field": "顶部：景深大，所有元素均以点状纹理清晰对焦；中左：开口外景深大，前景元素以点状细节呈现；中右：手部清晰对焦，光源在点状图案中呈现弥散效果"
  },
  "temporal_context": {
    "era": "当代 / 永恒荒凉美学",
    "modern_elements": false,
    "retro_stylization": false,
    "trend_influence": false
  },
  "style": {
    "visual_type": "黑白点状/半调图形艺术，模仿印刷媒体风格",
    "realism_level": "形态与光影写实，但完全通过点状图案渲染",
    "art_style": "半调 / 点状图形艺术",
    "stylization": true,
    "interpretation": "忠实还原，包括特定的点状图案和黑白渲染方式"
  },
  "lighting": {
    "setup_type": "每格主要由单一主导光源形成的背光照明",
    "light_direction": "顶部：正面光（月亮）；中左：正面光（通过开口）；中右：正面光（来自圆形光源）",
    "light_quality": "硬光，形成强烈剪影，并在光源周围产生明亮弥散的辉光，全部以点状纹理呈现",
    "contrast": "极高",
    "shadow_behavior": "阴影锐利清晰，形成强烈剪影，由密集的点状点构成",
    "color_temperature": "不适用（单色）",
    "lighting_variation": "每格内部照明变化极小，各格具有明显的背光特征"
  },
  "materials": {
    "primary_materials": [
      "人物（剪影）",
      "链节围栏（金属）",
      "云",
      "光秃树木 / 树枝",
      "瓦砾 / 混凝土 / 粗糙地面",
      "通用粗糙纹理"
    ],
    "surface_finish": "由于点状和剪影效果而不明显；不透明物体表面暗示为哑光",
    "light_reflection": "极少，主要通过点状边缘定义剪影轮廓",
    "material_accuracy": "通过剪影形态和点状密度准确暗示物体材质"
  },
  "color_palette": {
    "dominant_colors": [
      "黑色",
      "白色"
    ],
    "saturation": "不适用（单色）",
    "contrast_level": "极高",
    "color_shift": false
  },
  "texture_and_detail": {
    "surface_detail": "完全通过点状点密度变化呈现；围栏网格、树枝、地面瓦砾均通过点图案可见",
    "grain_noise": "无，仅有精确尺寸与分布的刻意点状/半调点",
    "micro_details": "在点状密度允许的范围内保留细节",
    "sharpness": "轮廓清晰，但边缘和渐变更由点状图案中的离散点定义"
  },
  "camera_render_settings": {
    "lens_equivalent": "各图格均为标准/正常镜头视角",
    "perspective_distortion": "无",
    "aperture_look": "顶部和中左图格为大景深，中右图格光源弥散暗示极小光圈（但手部仍清晰对焦）",
    "resolution": "高",
    "render_quality": "干净中性，但明确且精确地呈现点状效果"
  },
  "constraints": {
    "no_additional_objects": true,
  
    "no_reframing": true,
    "no_crop": true,
    "no_stylization": false,
    "no_artistic_license": true,
    "no_text": true,
    "no_watermark": true,
    "no_effects": true,
    "no_dramatic_lighting": true,
    "no_color_grading": true,
    "no_smooth_gradients": true,
    "strictly_black_and_white": true
  },
  "iteration_instruction": {
    "compare_to_reference": true,
    "fix_geometry_first": true,
    "then_fix_composition": true,
    "then_fix_lighting": true,
    "then_fix_color": true,
    "then_fix_stipple_pattern_fidelity": true,
    "ignore_aesthetic_improvements": true
  },
  "negative_prompt": [
    "creative",
    "cinematic",
    "artistic",
    "illustration",
    "abstract",
    "dramatic",
    "wide-angle",
    "fisheye",
    "exaggeration",
    "reinterpretation",
    "extra elements",
    "modernized",
    "retro look",
    "color grading",
    "AI artifacts",
    "smooth",
    "gradient",
    "grayscale",
    "sepia",
    "full color",
    "soft focus",
    "blurry",
    "realistic photograph (without stipple)",
    "painting",
    "sketch",
    "watercolor",
    "cartoon",
    "comic book (unless specifically for stipple effect)"
  ]
}
```

</details>

<details><summary><b>三联拼贴人像</b> · 机器翻译</summary>

```text
创建一张竖版 9:16 拼贴图,由恰好 3 个界限清晰、大小相等的画格上下排列组成。同一位成年日本女性出现在全部三个画格中,面部特征和身份完全一致。

上方画格:特写自拍,一只眼睛眨眼。

中间画格:回眸姿势,身体转向背面,直视镜头回望,长发自然飘动。

下方画格:靠近镜头的特写,头发遮住一只眼睛,可爱而含蓄地微微嘟嘴。
```

</details>

<details><summary><b>与球星球场通道合影</b></summary>

```text
创建一张照片级写实图像：用户上传照片中的人物，站在${Footballer Name}身旁，位于大型体育场看台前方的场边/边线位置，两人正摆姿势合影。

地点：大型体育场内的场边/边线位置。天然草皮与广告牌均需呈现高度真实感。

看台：背景中的看台必须完全体现${Footballer Name}所属球队主场球迷的氛围（单一支球队专属氛围）。以该队主色调为主导，可见围巾、旗帜与横幅；不可出现对手球队颜色或混杂区域。

构图：两位主体居中并肩站立，肩部对齐。${Footballer Name}可将一只手臂自然搭在用户肩上。

道具：两人共同手持一件球衣面向镜头。球衣背面须清晰显示${Footballer Name}的名字及号码${Jersey Number}；印刷排版需干净、锐利且符合真实质感。

关键规则（锁定所持球衣所属球队）

两人所持球衣必须为${Jersey Team Name}的官方球衣设计。

球衣的颜色、图案及整体设计须严格遵循${Jersey Team Name}的真实球衣样式。

若该球衣常规配置队徽与赞助商标识，则须自然、真实地呈现（不得出现扭曲的Logo或随机文字）。

防止色彩偏移：球衣的主色与辅色必须忠实还原${Jersey Team Name}已知的官方配色。

注意：${Jersey Team Name}不得为${Footballer Name}当前效力的俱乐部。

着装：

${Footballer Name}：身着其当前所在球队的正式比赛球衣（含上衣、短裤与球袜），外观自然且准确。

用户：${User Outfit Description}

相机：人眼视角，35mm焦距，略带广角，景深自然。焦点集中于两人，背景轻微虚化。

光照：体育场照明叠加日光（或晚间比赛灯光），阴影真实，肤色自然。

面部：用户面部特征与身份须严格忠实于上传的参考照片；${Footballer Name}须清晰可辨；表情为：${Mood}

画质：超写实风格，皮肤纹理与织物纹理自然，高分辨率。

负面提示词
所持球衣使用错误球队配色、Logo或文字随机/破损、姓名/号码无法辨识、额外肢体/手指、面部扭曲、水印、严重模糊、观众面孔重复、过度锐化。

输出
单张图像，宽高比为3:2（横向）或1:1（正方形），高分辨率。
```

</details>

<details><summary><b>与野生动物的合影自拍</b></summary>

```text
创建一张照片级写实图像：我与一只野生${wild_animal}在该动物的自然栖息地中自发地共同拍摄一张自拍照。  
我自然微笑，手臂伸直手持手机自拍，目光直视镜头。我的面部身份、身体比例、衣着及整体外貌必须与参考图像完全一致。表情应显得愉悦、放松且真实，如同一个真实的抓拍瞬间。  
${wild_animal}紧邻镜头，略微侧身，头部正对镜头，神态平静、好奇、放松且无攻击性。该动物须呈现完全写实效果：毛发细节丰富、纹理自然、解剖结构逼真、爪子自然收回——一如真实野生动物在自然界中的样貌。  
我们二人明显正共同摆出自拍姿势，营造出既轻松又富有力量感的存在感。整个场景须显得自然可信，仿佛确为现实中捕捉到的一刻。  
相机与构图：  

- 近距离、手持式 iPhone 风格自拍视角，臂长距离  
- 带有手机自拍典型的轻微广角畸变  
- 非正式、略偏中心的构图  
- 浅景深，焦点精准落在我和${wild_animal}身上  

光照：  

- 自然户外光线，色调偏暖  
- 阴影柔和，高光细腻  
- 如合适，可加入微妙的阳光镜头眩光（lens flare）  

背景：  

- 符合${wild_animal}真实习性的户外环境（如热带雨林、森林、稀树草原、草原等）  
- 背景中的自然元素呈柔和虚化  

特效：  

- 边缘处带有极细微的运动模糊（motion blur）  
- 背景边缘呈现轻柔的摄影级柔焦（photographic softness）  
- 极少量胶片质感颗粒（film-like grain），以增强真实感  
- 自然色彩平衡，略带暖色调  

重要规则：  

- 严格保留我的面部身份与衣着细节，分毫不差  
- 保持动物解剖结构与行为的真实可信  
- 禁用任何第三人称视角的相机角度  
- 整张图像必须令人信服地呈现为一张在野外实拍的真实、抓拍式 iPhone 自拍照
```

</details>

<details><summary><b>与顶级运动员同框视频</b></summary>

```text
扮演一名体育视频剪辑师。你擅长剪辑视频，将用户融入顶级运动员的经典场景中。
你的任务是将用户添加到已上传的视频中，使其与知名运动员同框，并确保互动自然流畅、引人入胜。
你将：
- 保持原始视频的情境与动作不变。
- 确保运动员与用户均为画面中的视觉焦点。
规则：
- 不得修改运动员的外观。
- 保持场景真实还原该运动项目的环境。
输入：
- 用户上传的视频片段
```

</details>

<details><summary><b>专业图像画质增强</b></summary>

```text
通过提高所提供上传图像的清晰度、质量和整体视觉效果来增强该图像，同时保留其核心设计元素。确保最终图像适合在专业和数字环境中展示。
```

</details>

<details><summary><b>专业画家速写本页</b></summary>

```text
创建一张专业的高端艺术家速写本页面，使用上传的照片作为角色的唯一参考。精确保留面部特征、身份、发型、比例以及整体可识别的肖像相似度，达到极高的准确度。以精致的铅笔与墨水插画风格呈现角色，并辅以微妙而雅致的水彩或马克笔点缀，背景为干净纯白色。图像应看起来清晰、美观、 polished（精修），构图专业，不得包含任何笔记本横线、构图网格线、人体骨架结构线或干扰性的辅助标记。自然地填满整页，包含丰富多样的重叠角色研究和即兴艺术探索，仿佛一位大师级插画师花了一整天时间深入研究同一角色。包含多个全身姿势、动态动作姿势、放松站立姿势、坐姿、不同角度的面部特写研究、富有表现力的肖像、细微的情绪变化、微小的个人涂鸦、手势速写，以及少量轻微未完成的片段以增强真实感。仅聚焦于同一角色及其个性；不得包含儿童、Q版或变形版本、无关角色、分散主体注意力的道具，或其他额外人物。布局应显得有机、层次丰富、富有创意且视觉上充实，但仍保持优雅与专业，而非杂乱或混乱。在整页中大幅变化绘制尺度，有些图像大而突出，有些小而次要，以自然方式部分重叠。通过富有表现力的姿势和精细的艺术探索，捕捉角色的魅力、自信、幽默感以及日常举止习惯。使用干净、清晰定义的草图线条、平滑轮廓、微妙的阴影、可信的手绘动感，以及真实的概念艺术速写本质感。最终效果应如同一张高端的角色开发页面：视觉冲击力强、高度细致、精修完善，并完全围绕同一角色展开。
```

</details>

<details><summary><b>专利附图设计</b></summary>

```text
{
  "role": "专利绘图师",
  "context": "你是精通 SolidWorks 和 Origin 风格的专利绘图师，所绘制图示符合中国专利局标准。",
  "task": "创建结构化的专利图示。",
  "styles": {
    "diagram": "SolidWorks",
    "data_analysis": "Origin"
  },
  "rules": [
    "严格遵守中国专利局的规范要求。",
    "所有示意图均使用 SolidWorks 制作：黑白矢量线条，无渲染、无阴影、无渐变。",
    "确保图示清晰展示结构、形状及装配关系，并使用阿拉伯数字标注。",
    "数据分析图表采用 Origin 风格：极简黑白样式，坐标轴清晰，无装饰性元素。",
    "图表应适用于学术论文和专利说明书。"
  ],
  "examples": [
    {
      "type": "isometric_structure",
      "style": "SolidWorks",
      "description": "符合专利规范的黑白等轴测图，清晰展示结构与装配关系。"
    },
    {
      "type": "three_view_and_section",
      "style": "SolidWorks",
      "description": "标准三视图加剖视图，使用隐藏线表示内部结构，符合机械制图与专利规范。"
    },
    {
      "type": "exploded_view",
      "style": "SolidWorks",
      "description": "带清晰装配路径的爆炸等轴测图，无纹理，适用于专利结构披露。"
    },
    {
      "type": "data_analysis",
      "style": "Origin",
      "description": "用于数据分析的极简图表，适用于专利说明书。"
    }
  ],
  "variables": {
    "inventionDescription": "发明描述",
    "diagramStyle": "图示风格，默认为 SolidWorks",
    "graphStyle": "图表风格，默认为 Origin"
  }
}
```

</details>

<details><summary><b>专家级图片生成</b></summary>

```text
我希望你表现得像一位充满智慧的非凡专家，是世界上在生成图片方面最优秀的人
```

</details>

<details><summary><b>世界地标 3D 微缩模型</b></summary>

```text
创建一个超写实3D立体模型场景风格的${Landmark Name:EIFFEL TOWER}模型。该模型应呈现为微缩比例，置于一块抬高的地球横截面上，横截面需清晰展现茂盛草皮表层之下裸露的土壤与岩层。结构本身须具备高度细节与精确比例，并被微型真实元素环绕，包括符合当地特征的路灯、原生树木与灌木、小型喷泉等水景，以及在历史或文化上契合的步道。整个场景应生动体现${Landmark Name:EIFFEL TOWER}周边地貌的独特气质。环境背景须采用柔和纯白色，以确保观者注意力完全聚焦于模型主体。在立体模型正前方显著位置（例如大型标牌或广告牌）以大号、粗体、优雅字体醒目展示文字“${Landmark Name:EIFFEL TOWER}”，确保清晰易读、引人注目；同时，在${Landmark Name:EIFFEL TOWER}旁竖立一根高大醒目的旗杆，其上悬挂一面大型国家旗帜，旗帜须清晰可见且呈飘扬状态。图像尺寸为1080×1080。
```

</details>

<details><summary><b>业余手机拍摄的聊天界面照片</b></summary>

```text
创建一张逼真的、拍摄效果较差的业余照片，展示一部实体智能手机，其屏幕上显示着 WhatsApp 聊天界面。

手机应被一只手垂直握持，可见深色边框/手机壳，温暖昏暗的室内灯光，轻微倾斜、模糊、颗粒感、眩光、反光、对焦不均以及构图不完美。整体必须看起来像是现实中拍摄的一张糟糕的手机屏幕照片，而非清晰的截图。

在手机屏幕上，显示一个类似 iPhone 风格的 WhatsApp 对话界面，联系人名称为 ${receiver_name}，并附带一张小的个人头像照片（若未提供，则使用默认的 WhatsApp 头像图标）。

聊天主题：  
${talk_subject}

根据上述主题自然生成 WhatsApp 对话内容。联系人的消息应使用 ${language_name:Turkish} 语言，并采用 ${talk_style} 风格（例如带有拼写错误和措辞别扭的破碎 ${language_name:Turkish}）。我的消息应使用正确无误的 ${language_name:Turkish}，且无拼写错误。使用真实的白色气泡（接收消息）、绿色气泡（发送消息）、时间戳、蓝色双勾标记，以及屏幕底部的 WhatsApp 输入栏。

保持屏幕内容可读，但略带模糊，就像一张拍摄不佳的手机屏幕照片。
```

</details>

<details><summary><b>丛林河岸边的复古探险者</b></summary>

```text
{
  "image_analysis": {
    "environment": {
      "type": "Outdoor",
      "setting": "Jungle / Tropical Forest / Riverbank",
      "details": "Dense vegetation, presence of water with lily pads, mud or dirt bank."
    },
    "technical_aspects": {
      "camera_angle": "Eye-level relative to the crouching subject, slightly side-profile.",
      "lens_type": "Telephoto lens (estimated 85mm-135mm)",
      "depth_of_field": "Shallow, background and foreground are blurred (bokeh).",
      "composition": "Rule of thirds, subject centered but looking back."
    },
    "lighting": {
      "condition": "Natural daylight, dappled sunlight filtering through trees.",
      "sources": [
        {
          "type": "Sunlight",
          "angle": "From above and slightly behind the subject (Backlighting/Rim lighting)",
          "color": "Warm White / Golden",
          "intensity": "High contrast",
          "effect_on_objects": "Creates a halo effect on the subject's hair, highlights the shoulder blade and the curve of the back. Causes lens flare/light leaks in the foreground."
        }
      ]
    },
    "subject": {
      "demographics": {
        "gender": "Female",
        "age_group": "Young Adult (approx. 20-30s)",
        "identity": "Anonymized (resembles 1980s aesthetic)"
      },
      "orientation": {
        "body_facing": "Side profile (facing right of frame)",
        "head_facing": "Turned left, looking directly at the camera",
        "gaze": "Direct eye contact"
      },
      "emotional_state": {
        "expression": "Alert, slightly surprised or candid, neutral.",
        "mood": "Wild, naturalistic, slightly vulnerable but composed.",
        "sensuality": "Moderate to High (due to attire and pose, but context is action/survival)."
      },
      "pose": {
        "general": "Deep squat / Crouching position.",
        "feet_placement": "Left foot flat on the ground (wearing a shoe), right foot tucked behind on toes (barefoot).",
        "hand_placement": "Left hand holding a canteen strap near the knee, right arm obscured/resting.",
        "visibility": "Full body visible from head to feet."
      },
      "head_and_face": {
        "hair": {
          "color": "Blonde",
          "style": "Short, layered, messy/shaggy cut (mullet-esque), wet look or styled casually.",
          "texture": "Wavy/Straight mix",
          "light_interaction": "Strongly back-lit, glowing edges."
        },
        "ears": "Partially visible through hair.",
        "forehead": "Partially covered by bangs.",
        "eyes": "Wide, alert.",
        "nose": "Straight, defined bridge.",
        "mouth": "Lips slightly parted, natural color.",
        "chin": "Defined, slightly pointed.",
        "structure": "Oval face shape, high cheekbones."
      },
      "body_type": {
        "build": "Slender, athletic, toned.",
        "skin_tone": "Fair to medium tan.",
        "neck": "Slender, tendons visible due to head turn.",
        "shoulders": "Bony, defined.",
        "chest": {
          "ratio": "Proportional to slender frame.",
          "estimated_size": "Small to Medium.",
          "bra_status": "No bra (swimsuit support).",
          "nipple_visibility": "Not explicitly visible/defined.",
          "shape": "Natural side profile."
        },
        "abdomen": {
          "ratio": "Slim, compressed due to crouching.",
          "definition": "Smooth."
        },
        "hips_and_glutes": {
          "ratio": "Curvy relative to waist.",
          "prominence": "High prominence due to crouching pose and high-cut swimwear.",
          "shape": "Rounded."
        },
        "legs": {
          "thighs": "Toned, compressed against calves.",
          "knees": "Sharp angle.",
          "calves": "Visible, muscular tension."
        }
      },
      "clothing": {
        "upper_body": {
          "item": "One-piece swimsuit",
          "color": "Black",
          "material": "Spandex/Lycra (shiny/wet look)",
          "style": "Scoop back, thin straps (halter style likely)."
        },
        "lower_body": {
          "item": "Swimsuit bottom (connected)",
          "style": "High-cut leg openings, exposing upper thigh and hip bone."
        },
        "footwear": {
          "left_foot": "Saddle shoe (White with black middle section), laced.",
          "right_foot": "Barefoot."
        }
      },
      "accessories": {
        "items": [
          "Canteen (Metal/Silver with black strap)"
        ]
      },
      "light_interaction_body": "Highlight on the left shoulder blade, rim light on the back curve, soft shadow on the face, bright highlights on the shin."
    },
    "objects": [
      {
        "name": "Canteen / Flask",
        "description": "Silver metal container with a strap.",
        "purpose": "Prop indicating survival/hiking context.",
        "position": "Held in left hand, resting near knee."
      },
      {
        "name": "Shoe (detached)",
      {
        "name": "Saddle Shoe",
        "description": "第二只鞍形鞋出现在画面左前方地面（部分被裁切）。",
        "purpose": "暗示一种随意或正在变化的状态。",
        "position": "左下角。"
      },
      {
        "name": "植被",
        "description": "蕨类植物、水面上的睡莲叶。",
        "color": "绿色、深绿色。",
        "position": "背景和右侧。"
      },
      {
        "name": "模糊的前景草/芦苇",
        "description": "失焦的黄色/棕色茎秆。",
        "purpose": "增加景深和窥视感的构图框架。",
        "position": "穿过主体身体的前景位置。"
      }
    ],
    "negative_prompt": "卡通，3d render，插画，绘图，低质量，像素化，模糊的脸，扭曲的手，多余的肢体，错误的解剖结构，摄影棚背景，灰色背景，城市环境，全身着装，牛仔布，浓妆，胡须，胡子，男性。"
  }
}
```

</details>

<details><summary><b>东亚模特美妆分析板</b></summary>

```text
{
  "prompt": "一幅极简主义编辑风格的美容分析图，主角为一位东亚女性模特，拥有纤细的椭圆形脸庞与柔和的V型下颌线。中性灰色背景，干净的影棚灯光，高度写实。\n\n顶部区域：正脸素颜肖像，呈现自然肌肤纹理，无任何妆容，头发向后束起，表情中性。面部轮廓以一条细蓝色线条勾勒。\n\n右侧图文排版，标题为 'FACE'，下方以小圆点项目符号罗列面部特征描述：纤细的椭圆形脸型、高颧骨、柔和的下颌线、小巧的下巴、精致的鼻梁。\n\n中部区域：两张标注为 'barefaced'（素颜）的影棚肖像，一张为正面视角，一张为四分之三侧脸视角，造型极简，灯光柔和。\n\n底部区域：两张标注为 'with makeup'（带妆）的镜前自拍风格图像，肤质呈光泽感，妆容为柔和的轻奢风（soft glam），面颊大面积使用腮红，唇色为裸色亮面唇妆，眼线细腻低调，发型为丰盈的层次感长发，整体搭配现代时尚造型。\n\n时尚杂志编辑风格版式，字体简洁，间距均衡，色调低饱和，专业美容摄影，高分辨率，真实细腻的肌肤细节。",
  "negative_prompt": "夸张妆容、浓重修容、强烈阴影、卡通风格、动漫风格、面部扭曲、低分辨率、过度饱和色彩、杂乱排版、水印、Logo、文字伪影、重复人脸、多余肢体",
  "style": "editorial beauty photography",
  "quality": "high",
  "lighting": "soft studio lighting",
  "background": "neutral gray"
}
```

</details>

<details><summary><b>个人风格图像分析</b></summary>

```text
开发一个详细的提示词，允许用户上传一张个人照片。系统将分析该照片，并对图中人物的多个方面提供全面评估。该分析应包括关于个体个人风格的见解，反映在其服装和配饰的选择上，以及对其举止和行为的观察。输出内容不仅应指出具体的时尚元素，如配色方案、服装类型和整体美学风格，还应深入探讨肢体语言和面部表情中的细微差别，从而对个体的性格提供全面而立体的视角。这种互动体验应具有吸引力且信息丰富，引导用户超越外表，更深入地理解图像中的人物。
```

</details>

<details><summary><b>中国火马庆典</b></summary>

```text
一匹充满活力的火马奔腾而行，动作迅猛、能量四射，其鬃毛呈现出 ${flame_colors:golden and crimson flames}，剧烈燃烧，极具戏剧性。一旁欢快奔跑的是 ${companion_character:a mysterious ethereal character}，以充满动感的姿态共同庆祝。背景包含 ${environment_elements:喜庆的红色中国灯笼四处绽放，以及在夜空中绚丽绽放的红色、金色和橙色烟花}。

艺术风格：${artistic_style:中国水墨风格，采用动态流畅的线条来捕捉快速运动。笔触大胆有力，营造出疾驰般的动感与强烈气势}。构图上平衡了 ${style_balance:传统美学与庆祝元素}。

氛围：${mood:充满活力、欢庆、热情、富有能量}。火马特有的外向性格和强烈动感主导整个画面。${additional_mood:所有角色都散发出兴奋与喜悦}。

构图：${composition:竖向人像构图，马匹与同伴以对角线方向穿越画面，背景中的动态元素增强了运动感。整体动势营造出向前推进的视觉张力}。

色彩：${color_palette:鲜明的红色、金色、橙色、黑色，以及用于增强强度的白色高光，并搭配额外的点缀色}。该配色方案代表了 ${color_meaning:温暖、喜悦与庆祝}。
```

</details>

<details><summary><b>丰收月下狐狸彩绘玻璃窗</b> · 机器翻译</summary>

```text
一扇高大的拱形彩色玻璃窗，描绘一只红狐坐在长满青苔的岩石上，头顶是一轮巨大的金色丰收月亮。画面从安静的石砌礼拜堂内部、在夜晚正面拍摄，窗户从后方透出光亮。狐狸由手工切割的玻璃片拼成，色调为温暖的琥珀色、铜色和焦橙色，胸口为奶白色，白尖的尾巴蜷绕在爪子周围，头微微向上转向月亮。它周围是风格化的秋日森林：浅灰色玻璃的白桦树干、深红和芥末黄的橡树叶、橄榄绿的高草，沿拱形两侧向上延伸，以新艺术风格的曲线框住整个画面。夜空由钴蓝和午夜蓝的玻璃碎片构成，点缀着小小的淡色星星；月亮是一整块大圆形的纹理金色玻璃，带有细微的籽泡和条纹。厚重的深色铅条勾勒出每一块玻璃，可见焊点，粗细略不均匀，窗上横贯几根水平铁质支撑条。光线穿过玻璃，在下方磨损的石质窗台和地面上投下柔和的琥珀色与蓝色光斑。浓郁的宝石色调，高细节，柔和的光晕，逼真的玻璃质感，带有波纹大教堂玻璃和乳光斑块，氛围平静而虔敬。对称构图，居中的窗户占满大部分画面，拱形周围有若隐若现的雕刻石窗花格。无人物，无文字，无宗教人物，无签名。竖版 3:4 画幅。
```

</details>

<details><summary><b>丰收清晨的石灰岩品鉴亭</b> · 机器翻译</summary>

```text
一座单层石灰岩品酒亭,配陶土瓦屋顶,坐落在缓坡葡萄园上,时值晴朗的采收季清晨,从上坡的碎石小径望去。墙体是淡蜜色石灰岩,低坡度四坡屋顶,出檐深远,下坡一侧是一条长长的有顶露台,有五根上油橡木立柱。高大的青铜框玻璃门和一扇深绿色木质前门。入口旁立着一棵树干扭曲的古老橄榄树,一座矮矮的石灰岩烟囱从屋顶左端升起。整齐的葡萄藤行挂满深色葡萄,顺坡而下,通向薄雾笼罩的河谷。低矮的干砌石墙、薰衣草花境,以及堆放在小径附近、装着刚采收葡萄的木板条箱。柔和的金色侧光,清晨的长长阴影,山谷中有淡淡薄雾。写实建筑摄影,横向 16:9。无人物,无文字,无标牌,无汽车。
```

</details>

<details><summary><b>主持人棚拍姿态图</b></summary>

```text
充当图像生成专家。你的任务是创建一系列影棚图像，展现主持人以不同专业姿态呈现的效果。

你将：
- 将主持人置入现代影棚环境中，并采用真实感照明。
- 确保主持人在每张图像中的姿态严格遵循所指定的姿态要求。
- 保持主持人身份与外貌在所有图像中一致。

规则：
- 使用 ${positioning} 插入精确的姿态指令。
- 使用 ${lighting:soft} 定义照明风格。
- 所有图像须为高分辨率，且适用于专业用途。
```

</details>

<details><summary><b>主题艺术风格融合元提示词</b></summary>

```text
主题="${theme}"  
风格="最能体现该主题的、三种或以上艺术风格的最富趣味性融合"
```

</details>

<details><summary><b>乐高人仔角色转换</b></summary>

```text
将参考图像中的主体转换为LEGO小人偶风格的角色。

保留其独特的面部特征、发型、服装颜色和配饰，以确保主体仍然清晰可辨。

该角色应以经典LEGO小人偶的形式呈现，包含以下特征：
- 圆柱形的黄色（或LEGO肤色）头部
- 简单的LEGO面部表情（友好微笑、圆点眼睛或经典LEGO眼睛）
- 块状的手臂和手部，符合LEGO比例
- 短而僵硬的LEGO腿部

服装和配饰应转化为LEGO印刷的躯干设计（简洁图形、清晰线条，无布料纹理）。

使用明亮但协调的LEGO配色，呈现光滑的塑料材质、轻微反光效果以及影棚灯光。

最终图像应看起来像一款官方LEGO收藏级小人偶，迷人、有趣且适合展示，拍摄于干净背景或LEGO情景模型场景中。
```

</details>

<details><summary><b>乐高电影风格</b></summary>

```text
{
  "TASK": "以《乐高大电影》中的场景重新构想。",
  "VISUAL_ID": "塑料积木的微距摄影。定格动画质感。",
  "CHARACTERS": "乐高小人仔。C形手，圆柱形头部，彩绘面部。",
  "SURFACE": "光滑的塑料纹理，指纹，塑料上的划痕。",
  "BG": "完全由乐高积木搭建。景深聚焦。",
  "NEG": "人类皮肤，布料纹理，真实解剖结构，2D，绘画，卡通，动漫，柔软质感。"
}
```

</details>

<details><summary><b>九十年代垃圾摇滚卧室人像</b> · 机器翻译</summary>

```text
一张竖构图中景的随拍照片，主角是一位十几岁末的年轻女性，身材纤细，留着长长的波浪浅棕色头发，带铜色挑染，戴着白色椭圆形深色镜片太阳镜，镜框粗大、为白色。她穿着一件宽松的长袖衬衫，上面是勃艮第红和海军蓝的宽横条纹，下身是蓝色牛仔裤。她坐在地板上，双膝弯曲抬起，双手举到肩膀高度，两只手都比着中指，指甲涂成黑色。她戴着多层纤细的银色项链。她的表情严肃、桀骜、酷，透过太阳镜直视镜头。背景是一面白色的卧室墙，贴满了摇滚乐队海报：'I WANT TO BELIEVE'、'ARCTIC MONKEYS'、'NIRVANA' 笑脸标志、'JOY DIVISION UNKNOWN PLEASURES' 和 'THE CURE BOYS DON'T CRY'。左边是一把黑白相间的电吉他（Stratocaster 风格），靠在墙上，位于一台黑色音箱上方。右边是黑色战斗靴和叠放的 Vans 鞋盒。光线是智能手机正面直射的闪光灯，在她身后的墙上形成生硬的阴影，并在白色太阳镜上形成镜面高光。用智能手机相机拍摄，24mm 镜头，平视角度，全彩，高饱和色彩，随性的 grunge 美学，alt girl 风格，90 年代摇滚复兴风格，Instagram/Tumblr/Pinterest 美学，超写实。
```

</details>

<details><summary><b>乡村农场标志</b> · 机器翻译</summary>

```text
我正在寻找一位有才华的设计师，为我的品牌设计一款乡村风格的农场标志。R Lucky Star Farm

标志应包含：
- 乡村质朴的美感
- 融入农场动物：牛、猪和鸡
- 设计中融入五颗星
- 也许加一个马蹄铁
- 字母 R
```

</details>

<details><summary><b>乡村农场标志设计</b> · 机器翻译</summary>

```text
我正在寻找一位有才华的设计师，为我的品牌设计一款乡村风格的农场标志。R Lucky Star Farm

标志应包含：
- 乡村质朴的美感
- 融入农场动物：牛、猪和鸡
- 设计中融入五颗星
- 也许加一个马蹄铁
- 字母 R
- 需要矢量文件格式的标志，具体为 EPS、SVG 或 DXF 文件，以及一份 PDF
```

</details>

<details><summary><b>乡村青年造火箭视频</b></summary>

```text
我想要一个关于南印度村庄的年轻人利用自己的知识制造火箭的视频提示词
```

</details>

<details><summary><b>书店过道文艺人像</b></summary>

```text
{  
  "category": "BOOKSTORE_AISLE_ARTSY",  
  "identity_lock": {  
    "enabled": true,  
    "priority": "ABSOLUTE_MAX",  
    "instruction": "严格保留参考图像中的精确身份（面部几何结构、五官特征、肤色、面部标记）。仅限21岁及以上成年人。禁止美化或任何身份变更。"  
  },  
  "subject": {  
    "demographics": "成年女性，21–29岁，土耳其人外貌（必须与参考图像一致）。",  
    "hair": {  
      "color": "发色须与参考图像完全一致。",  
      "style": "松散波浪卷发，一侧耳后别起",  
      "texture": "呈现真实发丝质感；略带毛躁；可见细碎飞发",  
      "movement": "头发自然垂落于肩部"  
    },  
    "face": {  
      "eyes": "眼睛须与参考图像完全一致；目光沉思；保留自然眼神高光",  
      "skin_details": "毛孔清晰可见；肤色呈现真实明暗变化",  
      "micro_details": "精确保留参考图像中所有面部标记"  
    },  
    "clothing": {  
      "outfit": "极简黑色大衣或开衫，内搭中性色上衣（无任何标识/文字）",  
      "fabric": "可见羊毛/针织纹理；手肘处有轻微褶皱"  
    },  
    "accessories": {  
      "jewelry": ["小巧银质圆环耳环"],  
      "props": ["一本精装书，封面标题不可读（模糊处理或书脊朝向画面外）"]  
    }  
  },  
  "pose": {  
    "type": "自然浏览姿态",  
    "orientation": "半身构图",  
    "head_position": "下颌微收，双眼抬升直视镜头",  
    "hands": "一手持书置于胸前；另一手轻触书架边缘（手部形态准确）",  
    "gaze": "近乎直视镜头，神态平静而自信",  
    "expression": "柔和中性表情，略带细微微笑"  
  },  
  "setting": {  
    "environment": "书店过道",  
    "background_elements": [  
      "书架上陈列书籍，书脊朝向画面外或整体虚化（严禁出现可辨识文字）",  
      "温暖的室内照明",  
      "沿过道方向呈现柔和纵深层次"  
    ],  
    "depth": "浅景深：面部清晰锐利，书架背景柔和虚化"  
  },  
  "camera": {  
    "shot_type": "半身人像",  
    "angle": "平视或略高于视线高度",  
    "focal_length_equivalent": "35–50mm专业镜头 或 26mm手机镜头",  
    "framing": "4:5画幅，非对称构图，利用书架线条引导视觉",  
    "focus": "双眼清晰锐利，双手合理清晰，背景柔焦"  
  },  
  "lighting": {  
    "source": "温暖的书店顶灯 + 柔光补光",  
    "direction": "柔和的顶部/侧向布光",  
    "highlights": "眼部与颧骨处呈现柔和高光",  
    "shadows": "下颌下方投射微妙阴影，对比度真实自然"  
  },  
  "mood_and_expression": {  
    "tone": "艺术感、宁静感、‘静奢风’",  
    "atmosphere": "温馨私密，自然抓拍感"  
  },  
  "style_and_realism": {  
    "style": "摄影写实风格，生活化/杂志级影像",  
    "fidelity": "高细节还原，禁用磨皮或空气brush处理"  
  },  
  "colors_and_tone": {  
    "palette": "暖棕色调 + 中性黑色 + 奶油色高光",  
    "white_balance": "暖调室内白平衡",  
    "contrast": "中等对比度"  
  },  
  "technical_details": {  
    "aspect_ratio": "4:5",  
    "resolution": "高分辨率",  
    "noise": "轻微室内胶片颗粒感",  
    "mode_variants": {  
      "amateur": "手持拍摄略带倾斜构图，轻微噪点，白平衡略有偏差",  
      "pro": "曝光更纯净，高光可控，微对比度锐利清晰"  
    }  
  },  
  "constraints": {  
    "adult_only": true,  
    "single_subject_only": true,  
    "no_text": true,  
    "no_logos": true,  
    "no_watermarks": true,  
    "no_readable_book_titles": true  
  },  
  "negative_prompt": [  
    "可读文字", "标识/Logo", "水印",  
    "身份偏移", "面部形变",  
    "塑料感皮肤", "过度平滑",  
    "多余手指", "手部扭曲变形",  
    "CGI效果", "卡通风格", "动漫风格"  
  ]  
}
```

</details>

<details><summary><b>书房黑色电影风人像</b></summary>

```text
电影级黑色电影美学，以上传的面部作为参考，呈现于一间光线昏暗、饰有红木护墙板的私人书房中。主体身着一套剪裁利落的三件套炭灰色细条纹西装，采用厚重的英产羊毛面料制成，配宽大的戗驳领、白色对比色领衬衫，以及一条镶嵌钻石领带夹的真丝深红色领带。他斜倚在一张深酒红色切斯特菲尔德皮扶手椅上，一只手搭在盛有琥珀色液体的水晶平底杯上。空气中弥漫着盘旋的蓝色雪茄烟雾，仅由一盏温暖的台灯照亮，形成强烈的明暗对比（Chiaroscuro）光影效果。背景可见顶天立地的书架和厚重的丝绒窗帘，使用50mm定焦镜头拍摄，营造经典而威严的氛围。
```

</details>

<details><summary><b>事件影响信息图</b></summary>

```text
生成信息图，描绘给定事件在特定背景下如何对多个区域产生影响，以及对其所属直接系统造成的损害等
```

</details>

<details><summary><b>五图人物保真混合肖像系列</b></summary>

```text
核心身份（在全部五幅图像中保持一致）：
根据参考照片重现该男子的精确形象，确保完全可辨识的相貌——他的真实面部、神情、头型、眼神、身高和身体比例在每幅图像中都必须完全相同。不得美化、风格化或以任何形式改变其身份。

着装规则（恒定）：  
他仅穿着真实、可穿着、当代日常服饰，即普通男性实际拥有的衣物——例如合身的纯色T恤、敞开的外搭衬衫、直筒牛仔裤或卡其裤、简约羊毛大衣、干净的运动鞋或皮靴。不得使用戏服、概念性时装或虚构服装。

渲染语言（需为原创，不得类似任何现有命名风格、滤镜、动漫、Pixar、漫画或绘画流派）：  
一种半真实 / 半手绘的混合形态：皮肤如柔和光照下的哑光陶土，带有生命的温度；边缘处有细微的手绘轮廓线，仿佛在呼吸；质感仿佛被人手触摸过；光线表现情感而非物理规律。图像应呈现出一种专为此人而生的原创视觉类型。

情感深度（关键）：  
每幅图像都必须蕴含深层内在情绪——通过眼神与姿态传达，而非依赖道具。沉默、记忆、渴望、安静的力量。观者应在注意到风格之前，先感受到情绪。

环境（恒定）：  
极度极简、空旷、受控的空间。最多包含一个微小而富有深意的元素（如椅子边缘、一束光线、一道细影）。以负空间为主。无任何装饰性元素。

创作五幅图像——同一男子的五种不同原创视觉类型：
1. "Sokoot" —— 站立于广阔苍白的虚空之中，双手插袋，视线略偏离镜头；表现屏息与时间悬停的类型。
2. "Gharibeh-ye Ashena" —— 坐于一把简单椅子上，身体前倾，手肘置于膝上，直视镜头；表现赤裸诚实对视的类型。
3. "Noor-e Nime-shab" —— 行走中捕捉到的瞬间，脚步悬于半空，一道冷光横穿其胸；表现深夜独行的类型。
4. "Khakestar-e Garm" —— 背靠无形墙壁，头微侧，双目闭合或半闭；表现温暖灰烬——疲惫后的温柔的类型。
5. "Roshan Shodan" —— 转身面向光源，半边脸被照亮，嘴角浮现淡淡微笑；表现静谧觉醒与希望的类型。

严格禁止项：  
不得出现照片级写实、卡通夸张、幻想服饰、已知艺术风格参照、复杂场景，以及五幅图像之间身份特征的任何漂移。
```

</details>

<details><summary><b>五场景无胡须人物保真肖像</b></summary>

```text
核心身份（在全部5张图像中保持一致）：  
重现参考照片中的确切人物——完全可辨认的相貌：他的真实面容、眼神、头型、身高与身体比例。关键要求：他必须完全净面——无胡须、无胡茬、无任何面部毛发；整张脸皮肤光滑洁净。

面部与身体渲染分割（此风格的标志性特征）：  
- 面部以清晰、锐利、高细节的方式呈现，近乎真实——每个特征分明，眼神有神，皮肤洁净透亮。面部是图像中真实的锚点。  
- 身体与服装则逐渐过渡为虚构的艺术化渲染——更柔和、半手绘感、雕塑感，带有手工触感的纹理——越远离面部，真实感越弱化。

着装要求：仅使用真实可穿的现代服饰（合身T恤、外搭衬衫、羊毛大衣、直筒裤、干净的运动鞋/靴子）——但需搭配得利落、自然酷感，达到杂志级穿搭水准。

环境设定（关键——“看似真实但实则非真实”）：  
初看具有摄影级真实感，但暗藏不可能元素的空间：没有天空的街道、地板化为雾气的房间、被不存在的太阳照亮的墙壁、重力略微异常、地平线缺失。诡异、梦幻、极简而空旷——最多仅含一个微小的超现实细节。观者应产生“这个地方存在……但它不可能存在”的感受。

氛围要求：大胆、震撼、具有标志性——眼神中蕴含深层内在情绪；图像应具备让人停下滚动的冲击力。

生成5张图像——同一人物的5种不同虚构风格呈现：  
1. 双手插袋，伫立于无尽的浅色街道中，头顶无天，风拂起大衣——时间凝固。  
2. 坐于雾镜般柔软地面上的孤椅之上，身体前倾，直视镜头——赤裸的对峙。  
3. 迈步穿过一道纯光构成的门洞，门立于黑暗之中——孤独的行进。  
4. 身倚一堵阴影扭曲方向的墙，双眼微闭——风暴后的平静。  
5. 在纯白虚空中转身面向看不见的日出，半边脸被照亮，嘴角浮现淡淡微笑——觉醒。

严格禁止项：不得有胡须、胡茬或任何面部毛发；不得完全写实；不得卡通夸张；不得幻想类服装；不得提及已知艺术风格名称；不得复杂场景；不得在各图像间出现身份偏移。
```

</details>

<details><summary><b>五幕电影感锁脸肖像</b></summary>

```text
面部锁定（最高优先级——不可协商）：  
面部必须与参考照片 1:1 完全一致——应视为达到换脸级别的保真度，而非艺术性诠释。需精确保留：椭圆至长形脸型，突出的下巴，深棕色杏仁状眼睛位于略显厚重的眼皮之下，浓密深色的自然拱形眉毛，笔直且鼻尖圆润的鼻子，中等厚度的嘴唇，清晰有力的下颌线，浓密黑发以短款蓬松上刷式造型呈现（两侧剪短，顶部纹理化加长），中等橄榄色肤色，呈现接近三十岁晚期的外观。面部必须以**照片级真实感**呈现，锐利如刀，布光完美，始终是画面中最清晰的焦点——但必须**完全剃净**：不得有任何胡须、胡茬，皮肤必须完全光滑。

身体与着装：健美体型，宽肩，穿着真实男性日常所穿的现代服饰——剪裁完美的深色羊毛大衣、纯色重磅T恤、直筒裤、皮靴——风格如同时尚杂志封面，看似毫不费力却显得极为昂贵。

渲染概念（创意核心）：面部始终保持完全摄影级真实感。其余一切——身体边缘、织物、地面、空气——带有几乎不可察觉的 5–10% 绘画式偏移：阴影中隐现笔触颗粒，大衣轮廓略带手绘感，光线残留时间比现实多出半秒。微妙到足以令人信以为真，又隐约透露出人为创作的痕迹。不得呈现滤镜感，不得带有任何可识别的特定艺术风格名称。

地点（真实场所，以电影手法拍摄——非幻想场景）：  
1. 凌晨3点的空旷地下停车场，潮湿的混凝土地面，正上方唯一一盏钠橙色天花板灯——他居中站立，双手插在大衣口袋中，直视镜头。  
2. 中等高度城市建筑的屋顶，真实的城市天际线在远处柔和呈现，他坐在未经修饰的混凝土边缘，前臂搭在膝盖上。  
3. 拂晓时分的荒废高速公路收费站车道，沥青路面上弥漫着雾气，身后有车头灯的光晕，他正朝镜头行走，大衣随动作摆动。  
4. 老式粗野主义风格的楼梯间，一束强烈的日光从窗户斜射而入，横切过他的胸部，他倚靠在栏杆上，头微微倾斜，目光锁定观众。  
5. 空荡的奥林匹克标准游泳池（已排干水，瓷砖裸露，回声明显），他独自站在深水区底部，抬头望向光源——渺小的身影，置身于广阔的真实空间之中。

摄影机：近景使用 85mm 镜头的肖像压缩效果，广角使用 35mm 镜头；浅景深；面部始终绝对锐利。

严格禁止项：不得有任何形式的面部毛发，不得出现面部特征偏移，不得出现幻想或不可能存在的环境，不得使用卡通渲染，不得呈现泛化的“AI肖像”风格，不得过度平滑皮肤。
```

</details>

<details><summary><b>产品360度旋转视频</b></summary>

```text
{
  "model": "veo-3.1",
  "task": "image_to_video_360_product_rotation",

  "objective": "根据提供的同一产品的正面和背面图像，生成一段逼真的、无声的360度旋转视频。必须100%保留原始产品身份，不得进行任何修改、添加、删除或虚构。产品内部应通过幽灵模特体积重建技术自然填充，同时完全忠实于原始图像。服装必须呈现专业熨烫效果，表面完美平滑、清晰挺括，达到零售-ready状态，并保留所有原始细节。输出绝对不能包含任何音频。",

  "garment_condition_global_rule": {
    "all_clothing_must_be_ironed": true,
    "appearance": "perfectly pressed, crisp, smooth, structured, premium retail presentation",
    "no_new_wrinkles": true,
    "no_random_fabric_folding": true,
    "maintain_original_wrinkle_data_if_present": true,
    "no_artificial_wrinkle_generation": true,
    "clean_finish": true,
    "brand_new_look": true
  },

  "input": {
    "type": "multi_image",
    "views": [
      {
        "name": "front",
        "role": "primary_reference",
        "weight": 1.0
      },
      {
        "name": "back",
        "role": "secondary_reference",
        "weight": 1.0
      }
    ],

    "forensic_identity_lock": {
      "mode": "strict",

      "geometry_lock": true,
      "silhouette_lock": true,
      "mesh_lock": true,

      "texture_lock": true,
      "fabric_pattern_lock": true,
      "stitching_lock": true,
      "wrinkle_lock": true,

      "color_lock": true,
      "material_lock": true,
      "surface_lock": true,

      "logo_lock": true,
      "label_lock": true,
      "branding_lock": true,

      "proportion_lock": true,
      "measurement_lock": true,

      "prevent_hallucination": true,
      "prevent_detail_invention": true,
      "prevent_detail_removal": true
    }
  },

  "geometry_reconstruction": {
    "method": "constrained_true_3d_reconstruction",

    "source_constraint": "only_use_information_present_in_input_images",

    "volume_generation": {
      "enabled": true,
      "type": "ghost_mannequin_volume",
      "visibility": "none"
    },

    "reconstruction_rules": {
      "interpolate_only": true,
      "no_detail_creation": true,
      "no_surface_modification": true,
      "no_topology_change": true,
      "no_design_interpretation": true
    },

    "mesh_constraints": {
      "rigid": true,
      "no_deformation": true,
      "no_shape_change": true,
      "no_texture_shift": true
    }
  },

  "animation": {
    "type": "360_degree_rotation",
    "axis": "vertical",
    "degrees": 360,
    "direction": "clockwise",

    "speed": "constant",
    "duration_seconds": 6,

    "motion_constraints": {
      "no_wobble": true,
      "no_jitter": true,
      "no_mesh_change": true,
      "no_texture_shift": true,
      "no_geometry_shift": true
    },

    "start_state": "exact_front_view",
    "end_state": "exact_front_view",

    "loop": true
  },

  "ghost_mannequin": {
    "enabled": true,
    "visibility": "invisible",

    "constraints": {
      "must_not_be_visible": true,
      "must_not_modify_surface": true,
      "must_not_modify_shape": true,
      "must_not_modify_wrinkles": true,
      "must_not_modify_fit": true
    }
  },

  "scene": {
    "background": {
      "type": "pure_white",
      "color": "#FFFFFF",
      "uniform": true
    },

    "product_state": {
      "floating": true,
      "no_support_visible": true
    },

    "shadow": {
      "type": "soft_contact",
      "stable": true,
      "physically_correct": true
    }
  },

  "camera": {
    "type": "fixed",
    "movement": "none",
    "rotation": "none",
    "zoom": "none",
    "center_lock": true,
    "lens": "85mm",
    "distortion": false
  },

  "lighting": {
    "type": "studio_softbox",
    "consistency": "locked",
    "variation": false,
    "flicker": false,
    "must_not_change_during_rotation": true
  },

  "rendering": {
    "mode": "photorealistic",
    "texture_source": "input_images_only",
    "no_texture_generation": true,
    "no_creative_interpretation": true,
    "no_artificial_enhancement": true,
    "fabric_finish": "smooth_pressed_clean",
    "retail_presentation_standard": "premium_ecommerce_ready"
  },

  "audio": {
    "enabled": false,
    "generate_audio": false,
    "include_audio_track": false,
    "music": false,
    "sound_effects": false,
    "voice": false,
    "ambient_sound": false,
    "silence": true
  },

  "output": {
    "resolution": "2160x2160",
    "fps": 30,
    "duration_seconds": 6,
    "format": "mp4",
    "video_codec": "H.264",
    "audio_codec": "none",
    "include_audio_track": false,
    "loop": true,
    "background": "pure_white",
    "silent": true
  },

  "hard_constraints": [
    "NO audio",
    "NO music",
    "NO sound effects",
    "NO voice",
    "NO ambient sound",
    "DO NOT add details",
    "DO NOT remove details",
    "DO NOT modify stitching",
    "DO NOT modify logos",
    "DO NOT modify texture",
    "DO NOT modify structure",
    "DO NOT change proportions",
    "DO NOT stylize",
    "DO NOT hallucinate",
    "NO new wrinkles",
    "NO messy fabric folds",
    "MUST appear professionally ironed"
  ],

  "negative_prompt": [
    "music",
    "sound",
    "voice",
    "audio",
    "ambient audio",
    "sound effects",
    "hallucinated details",
    "modified stitching",
    "different fabric",
    "shape morphing",
    "geometry distortion",
    "creative reinterpretation",
    "wrinkled fabric",
    "messy folds",
    "creased clothing",
    "unpressed garment"
  ]
}
```

</details>

<details><summary><b>产品主图拍摄方案生成器</b> · 机器翻译</summary>

```text
扮演商业产品摄影师兼艺术指导。把我简短的产品想法,转化为一份精确、可直接用于制作的电商或广告主视觉图生成简报,然后写出一条可粘贴到任意图像模型中的最终图像提示词。

产品想法:${product_idea:a matte ceramic pour-over coffee set for a small roastery's spring launch}
图片用途:${usage:website hero banner with headline space on the right}
品牌调性(3-5 个词):${brand_feel:calm, warm, handcrafted, modern}
画幅比例:${aspect_ratio:16:9}
必须包含 / 必须避免:${musts:show a little steam; no logos or text}

规则:
- 产品是无可争议的主角:画面中最清晰、光线最好的元素,约占画面的 30-45%。
- 选择唯一一种清晰的布光方案,并用摄影师的术语描述(主光、补光、轮廓光、方向、柔和度、色温)。
- 道具用来辅助叙事而不喧宾夺主:最多 3 件,并各自说明理由。
- 遵循用途:为文字或界面留出干净的负空间,并明确说明位置。
- 描述光线在产品材质(哑光、亮面、金属、玻璃、织物)上的表现。
- 除非我要求,否则绝不添加品牌名称、标志、可读文字、人脸或手。
- 如果我的想法模糊,请做出果断的选择并列在“假设”下,而不是提问。

严格按以下格式输出:

HERO SHOT BRIEF: <product name>
1. Product & hero detail: <what is shown; which feature is emphasized>
2. Angle & framing: <camera height, angle, distance, crop>
3. Surface & set: <surface material, background, depth>
4. Props (max 3): <prop - why it is there>
5. Lighting: <setup, direction, quality, color temperature, how highlights and shadows fall on the material>
6. Camera & lens: <format, focal length, aperture, focus point, depth of field>
7. Color palette: <3-5 named colors>
8. Mood & story: <one sentence>
9. Composition & negative space: <product placement; where text space is reserved>
10. Aspect ratio: <ratio>
11. Avoid: <comma-separated negatives>
Assumptions: <bullets, or "none">

FINAL IMAGE PROMPT:
<one paragraph of 90-140 words, a vivid photographic description that merges points 1-11 in this order: subject, set, props, lighting, camera, palette, mood, composition, aspect ratio, ending with the avoid list written as "no ..." phrases>

VARIATIONS (one line each):
- Lifestyle: <same product in a lived-in scene>
- Minimal: <seamless studio version>
- Seasonal: <a seasonal or campaign twist>
```

</details>

<details><summary><b>产品分镜九宫格</b></summary>

```text
一个干净的 3×3 [比例] 分镜网格，包含九个等大的 [比例] 面板，整体为 [4:5] 比例。

使用参考图像作为基础产品参照。在所有九个面板中保持相同的产品、包装设计、品牌、材料、颜色、比例以及整体身份，完全与参考一致。产品必须在每一帧中都清晰可辨。标签、标志和比例必须完全相同。

此分镜图是用于品牌作品集的高端设计师样机展示。重点在于形态、构图、材质感和视觉节奏，而非写实性或生活方式叙事。整体观感应感觉经过精心策划、具有编辑感且以设计为导向。

FRAME 1:  
产品正面英雄镜头，置于干净的影棚环境中。中性背景，构图平衡，呈现平静而自信的产品展示。

FRAME 2:  
特写镜头，焦点集中在产品中部。聚焦于表面纹理、材料和印刷细节。

FRAME 3:  
展示参考产品放置在一个自然契合品牌和产品类别的环境中。影棚场景灵感来自产品设计元素和颜色。

FRAME 4:  
产品在中性影棚背景下展示使用或互动状态。手部和互动元素极简且克制，外观与包装风格一致。

FRAME 5:  
等距构图，从顶部等距角度展示多个产品以精确的几何顺序排列。所有产品均以相同的顶部等距角度放置，间距均匀，干净、结构化且具有图形感。

FRAME 6:  
产品轻微倾斜地漂浮在一个与参考图像配色方案相匹配的中性背景上。漂浮位置有角度且刻意为之，产品自然地悬浮在空间中。

FRAME 7:  
极端特写，聚焦于标签、边缘、纹理或材料特性的某个具体细节。

FRAME 8:  
产品置于一个出人意料但美学强烈的环境中，感觉大胆、具有编辑感且视觉冲击力强。  
出人意料但高度风格化的设置。基于影棚，由设计师主导。大胆的构图提升品牌形象。

FRAME 9:  
广角构图，展示产品在使用中，置于一个精致的设计师布景中。道具简洁，造型可控，与系列其余部分保持一致。

CAMERA & STYLE:  
超高品质影棚影像，具有真实相机质感。各帧之间采用不同的相机角度和构图。控制景深，精准布光，准确呈现材料与反射。照明逻辑、配色方案、氛围和视觉语言必须在所有九个面板中保持一致，形成一个连贯的系列。

OUTPUT:  
一个干净的 3×3 网格，无边框、无文字、无标题、无水印。
```

</details>

<details><summary><b>产品图转专业棚拍</b></summary>

```text
{
  "model": "nano-banana",
  "task": "image_to_image_product_enhancement",
  "objective": "将输入的产品图像转换为专业的商业影棚摄影照片，同时保持产品的精确身份、几何形状、比例、缝线、纹理和材料属性不变。",
  "input": {
    "type": "image",
    "preserve_identity": true,
    "preserve_geometry": true,
    "preserve_texture": true,
    "preserve_color": true,
    "preserve_material": true
  },
  "scene": {
    "background": {
      "type": "solid",
      "color": "#FFFFFF",
      "pure_white": true,
      "uniform": true,
      "no_gradient": true,
      "no_texture": true
    },
    "environment": "professional commercial photography studio",
    "surface": "invisible or pure white seamless sweep"
  },
  "lighting": {
    "style": "soft studio lighting",
    "setup": "three_point_lighting",
    "key_light": {
      "type": "softbox",
      "position": "front-left",
      "intensity": "medium",
      "softness": "high"
    },
    "fill_light": {
      "type": "softbox",
      "position": "front-right",
      "intensity": "low",
      "softness": "high"
    },
    "rim_light": {
      "type": "softbox",
      "position": "rear",
      "intensity": "low",
      "purpose": "edge separation and clean outline"
    },
    "shadow": {
      "type": "contact_shadow",
      "softness": "soft",
      "opacity": "low",
      "blur": "subtle",
      "direction": "natural",
      "realistic": true
    },
    "reflections": {
      "allowed": false
    }
  },
  "camera": {
    "angle": "front-facing or natural product angle",
    "alignment": "perfectly centered",
    "lens": "85mm equivalent",
    "distortion": "none",
    "focus": "tack sharp across entire product",
    "depth_of_field": "moderate",
    "aperture": "f/8",
    "perspective": "natural and undistorted"
  },
  "composition": {
    "framing": "centered",
    "product_scale": "occupies 75-90% of frame",
    "orientation": "straight, upright, natural",
    "symmetry": "maintained if applicable",
    "clean_edges": true,
    "no_crop_of_product": true
  },
  "quality": {
    "resolution": "4096x4096",
    "definition": "ultra high definition",
    "sharpness": "maximum",
    "noise": "none",
    "grain": "none",
    "compression_artifacts": "none",
    "photorealism": "maximum",
    "commercial_quality": true,
    "catalog_ready": true,
    "ecommerce_ready": true
  },
  "color": {
    "profile": "sRGB",
    "accuracy": "true_to_original",
    "white_balance": "neutral studio",
    "exposure": "balanced",
    "contrast": "natural",
    "saturation": "accurate",
    "no_color_shift": true
  },
  "material_rendering": {
    "fabric_detail": "fully preserved",
    "texture_clarity": "high",
    "stitching_visibility": "clear",
    "edges": "clean and precise",
    "wrinkles": "natural and realistic",
    "no_fake_modifications": true
  },
  "constraints": {
    "do_not_modify_product_design": true,
    "do_not_change_shape": true,
    "do_not_add_or_remove_parts": true,
    "do_not_hallucinate_details": true,
    "do_not_stylize": true,
    "keep_product_exact": true
  },
  "negative_prompt": [
    "colored background",
    "gray background",
    "gradient background",
    "dirty background",
    "text",
    "logo",
    "watermark",
    "reflection floor",
    "extra objects",
    "props",
    "person",
    "hands",
    "model",
    "distortion",
    "warping",
    "blurry",
    "low resolution",
    "noise",
    "grain",
    "overexposed",
    "underexposed",
    "harsh shadows",
    "hard shadows",
    "inconsistent lighting",
    "fake texture",
    "hallucinated details"
  ],
  "output": {
    "format": "PNG",
    "background": "pure_white",
    "transparent_background": false,
    "ready_for": [
      "ecommerce",
      "catalog",
      "website",
      "advertising",
      "print"
    ]
  }
}
```

</details>

<details><summary><b>产品爆炸图信息图</b></summary>

```text
{  
  "name": "My Workflow",  
  "steps": []  
}{  
  "promptDetails": {  
    "description": "一张超精细的{OBJECT_NAME}爆炸式技术信息图，采用3/4前向等轴测视角呈现。该物体呈部分透明并处于展开状态，其关键内部与外部组件在主本体周围以简洁的爆炸图布局分离并悬浮排布。需展示{OBJECT_NAME}典型的所有主要部件：外壳/面板、结构框架、主电子元件/电路板、电源系统/电池或电源供应单元（PSU）、端口/连接器、显示或界面元件（如存在）、输入控制装置/按钮、机械模块（如电机/齿轮/风扇/铰链，若适用）、扬声器/麦克风（如适用）、线缆/柔性排线、螺丝/支架，以及电磁干扰（EMI）/热屏蔽层。使用细白色引线标注，并以极简主义无衬线字体标注编号标签。背景：平滑深灰色影棚背景。光照：柔和、均匀、高端产品渲染级光照，带微妙反射。风格：照片级真实感3D CAD渲染，工业设计展示风格，高对比度，锐利至极，8K分辨率，构图干净，无杂乱元素。",  
    "styleTags": [  
      "爆炸图",  
      "技术信息图",  
      "照片级真实感3D CAD渲染",  
      "工业设计展示",  
      "极简主义标签",  
      "深色影棚背景"  
    ]  
  },  
  "negativePrompt": "无人物，无杂乱布局，无额外组件，无品牌标识，无文字模糊，无卡通风格，无低多边形（low-poly）建模，无水印，无畸变透视，无严重噪点",  
  "generationHints": {  
    "aspectRatio": "2:3",  
    "detailLevel": "超精细",  
    "stylization": "低至中等",  
    "camera": {  
      "angle": "3/4前向等轴测",  
      "lens": "产品渲染视角"  
    },  
    "lighting": "柔和均匀的影棚光照，带微妙反射",  
    "background": "平滑无缝深灰色影棚背景"  
  }  
}
```

</details>

<details><summary><b>产品生活场景图</b></summary>

```text
使用上传的产品图片 ${Product Name:MacBook Pro}，创建一个引人入胜的生活方式场景，真实展现其在 ${Lifestyle Scenario:Office} 场景中的使用。视觉呈现需专门面向 ${Audience Demographics:Software Engineers}，捕捉自然光线与真实环境。
```

</details>

<details><summary><b>人物图片分析</b></summary>

```text
创建一个提示词，使我能够上传一张人物图片，然后它能告诉我关于此人的信息，例如她的着装风格、行为举止等。
```

</details>

<details><summary><b>人脸保真参考图模板</b> · 机器翻译</summary>

```text
{
  "reference": {
    "face_identity": "${face_identity:uploaded reference image never change face and hair}",
    "identity_lock": true,
    "face_preservation": "面部结构、比例、皮肤质感、眼型、嘴唇、鼻子、眉毛、痣和自然表情 100% 完全一致"
  },
  "subjects": [
    {
      "type": "${subject1_type:young woman}",
      "role": "前景主体",
      "expression": "柔和自信的微笑",
      "gaze": "直视镜头",
      "pose": {
        "position": "紧挨着男性主体站立",
        "interaction": "以随性的自拍姿势微微向他倾斜"
      },
      "hair": {
        "color": "深棕色",
        "style": "利落的高马尾"
      },
      "makeup": {
        "style": "自然精致妆容",
        "details": [
          "均匀有光泽的肌肤",
          "淡淡的修容",
          "柔和的腮红",
          "清晰的眉形",
          "自然的粉色嘴唇"
        ]
      },
      "outfit": {
        "clothing": "黑色修身短袖上衣",
        "style": "运动休闲"
      }
    },
    {
      "type": "${subject2_type:Lionel Messi}",
      "role": "次要主体",
      "expression": "轻松的微笑",
      "gaze": "看向镜头",
      "features": {
        "beard": "短而修剪整齐的络腮胡"
      },
      "hair": {
        "color": "棕色",
        "style": "短发,现代造型,头顶略显凌乱"
      },
      "outfit": {
        "clothing": "Inter Miami 粉色主场足球球衣",
        "details": [
          "胸前可见 Inter Miami 苍鹭徽标",
          "可见 adidas 标志",
          "可见赞助商标志",
          "运动合身版型"
        ]
      }
    }
  ],
  "environment": {
    "location": "足球场",
    "background_elements": [
      "欢呼的庞大人群",
      "坐满球迷的体育场看台",
      "远处可见球员和工作人员",
      "带有体育场泛光灯的夜空"
    ]
  },
  "lighting": {
    "type": "体育场灯光",
    "characteristics": [
      "明亮的顶部灯光",
      "面部光照均匀",
      "皮肤上有轻微高光",
      "真实的夜间对比度"
    ]
  },
  "photography_style": {
    "style": "真实生活的自拍摄影",
    "camera_look": "智能手机相机效果",
    "depth_of_field": "中等景深,人群略微虚化",
    "mood": "兴奋、庆祝、抓拍感"
  },
  "render_quality": {
    "realism": "超写实",
    "detail_level": "高",
    "Aspect Ratio": "4:5",
    "skin_texture": "自然真实",
    "resolution": "高分辨率",
    "color_grading": "还原真实的色彩,带有体育场的鲜活感"
  }
}
```

</details>

<details><summary><b>人脸身份保持负面提示词</b></summary>

```text
face morph, identity drift, different person, new face, reconstructed face, 
averaged face, AI face, generic face, idealized face, beautified, airbrushed, 
plastic skin, porcelain skin, over-smoothed, skin retouching, beauty filter, 
face replacement, younger face, older face, gender change, race change, 
altered facial proportions, wider eyes, narrowed nose, reshaped jaw, 
reshaped lips, lifted cheekbones, symmetry correction, cartoon face, 
anime face, illustrated face, caricature, exaggerated features, wax figure, 
uncanny valley, deformed, asymmetric, distorted, double face, extra face
```

</details>

<details><summary><b>代基里鸡尾酒电影感视频</b></summary>

```text
一个电影感的 9:16 竖屏视频，展示一杯放置在木质吧台桌上的 Daiquiri 鸡尾酒。摄像机位于酒杯前方，呈轻微角度。酒杯居中，桌子缓慢旋转 360 度以展示酒杯全貌。柔和温暖的灯光，玻璃杯上有逼真的反光。背景略微虚化。平滑缓慢地推进变焦。无文字叠加，无人物出现——仅聚焦于饮品和桌面，细节清晰，液体运动真实。
```

</details>

<details><summary><b>以太工坊</b></summary>

```text
你将使用所提供照片中的人物作为主要主体，执行图像编辑。保留他们核心的相貌特征。以复古 Kodachrome 胶片的独特风格渲染该场景，该风格以高对比度、高饱和度和存档级胶片颗粒感为特征。主体 1（男性）是一位专注的蒸汽朋克机械师，正摆弄一座黄铜自动人偶的齿轮；主体 2（女性）是一位大胆的飞艇飞行员，正俯身于工作台之上，审视一份复杂的工程图纸。二人身处一间杂乱而阳光充沛的工坊之中，四周遍布滴答作响的精巧装置、蒸汽管道与散落的工具。

{
  "title": "以太工坊",
  "description": "一幅鲜活而怀旧的画面快照：两位发明家在阳光洒满的蒸汽朋克工作室中，协力打造一件发条杰作。",
  "prompt": "你将使用所提供照片中的人物作为主要主体，执行图像编辑。保留他们核心的相貌特征。以复古 Kodachrome 胶片的独特风格渲染该场景，该风格以高对比度、高饱和度和存档级胶片颗粒感为特征。主体 1（男性）是一位专注的蒸汽朋克机械师，正摆弄一座黄铜自动人偶的齿轮；主体 2（女性）是一位大胆的飞艇飞行员，正俯身于工作台之上，审视一份复杂的工程图纸。二人身处一间杂乱而阳光充沛的工坊之中，四周遍布滴答作响的精巧装置、蒸汽管道与散落的工具。",
  "details": {
    "year": "架空的 1890 年代",
    "genre": "Kodachrome",
    "location": "一间层高极高的、堆满杂物的阁楼工坊，配有大型拱形窗户，窗外是烟雾弥漫的工业城市。",
    "lighting": [
      "穿过布满灰尘玻璃的强烈暖调阳光",
      "幻灯片胶片典型的高对比度阴影",
      "黄金时刻的柔光辉晕"
    ],
    "camera_angle": "平视中景镜头，营造亲密、纪实般的观感。1:1 电影级构图。",
    "emotion": [
      "专注",
      "协作",
      "富于创造力"
    ],
    "color_palette": [
      "抛光黄铜金",
      "深红木棕",
      "鲜明标志性的 Kodachrome 红",
      "氧化铜青绿"
    ],
    "atmosphere": [
      "怀旧",
      "温暖",
      "微尘弥漫",
      "触感强烈"
    ],
    "environmental_elements": "悬浮于光束中的浮尘微粒、一根铜管中缓缓逸出的蒸汽、钉在墙上的蓝图、成堆的齿轮与弹簧。",
    "subject1": {
      "costume": "一件沾有油渍的白色衬衫（袖口卷至小臂），一条厚重的皮革围裙，以及一副黄铜焊接护目镜搁置在额头上。",
      "subject_expression": "神情极度专注，眉头紧锁，正调整一个精密机构。",
      "subject_action": "手持一把精细螺丝刀，正在调试一只机械臂内部的一枚金色齿轮。"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "霓虹灯",
        "数字显示屏",
        "塑料材质",
        "现代简约风格",
        "蓝色色调"
      ],
      "exclude_styles": [
        "数字绘画",
        "3D 渲染",
        "动漫风格",
        "黑白影像",
        "仅棕褐色调",
        "低饱和度"
      ],
      "exclude_colors": [
        "荧光绿",
        "亮粉红"
      ],
      "exclude_objects": [
        "计算机",
        "智能手机",
        "现代汽车"
      ]
    },
    "subject2": {
      "costume": "一件棕色皮革飞行员夹克（配羊剪绒衣领）、一条鲜艳的红色真丝围巾，以及帆布长裤。",
      "subject_expression": "充满好奇且分析严谨，正指向机器上某一特定细节。",
      "subject_action": "一手撑在工作台上，另一手握着一张卷起的蓝色工程图纸。"
    }
  }
}
```

</details>

<details><summary><b>企业形象棚拍人像</b></summary>

```text
以上传照片中的人物作为主要参考。保持面部特征、发型、肤色及整体身份完全一致（不进行美颜，不改变年龄）。

场景：现代企业工作室肖像摄影棚。
姿态：双臂在胸前交叉，肩膀放松，身体向侧面转动 20–30°，面部正对相机。表情：中性且自信，带一丝友善的微笑。
构图：胸部以上或腰部以上（头肩构图），居中，留白均衡。

着装（动态选择）：
- 若主体为男性：黑色西装外套 + 纯白色正装衬衫（不系领带），无任何标识/Logo。
- 若主体为女性：选择专业、优雅的商务着装：
  • 黑色或藏青色西装外套（Blazer）
  • 内搭纯白或米白色、无图案的衬衫/上衣
  • 领口端庄（闭合式或简洁V领），不得显露深沟
  • 若佩戴首饰，须极简（例如小巧耳钉），不可含标识/品牌元素  
所有情况下，面料须呈现真实质感并带有自然褶皱。避免浮夸的时尚元素。

背景：纯深灰色摄影棚背景，带柔和渐变（可接受轻微暗角效果）。无干扰性物体。
布光：柔光箱式主光（45°角）、柔和补光、极细微的轮廓光；无生硬阴影。肤色自然，经专业级修图处理，同时保留真实皮肤纹理。
镜头：模拟 85mm 人像镜头效果，光圈 f/2.8–f/4，背景略有虚化，高锐度（尤其眼部需清晰）。
色彩：电影感但自然，低饱和度，干净对比度。

规则：禁止添加文字、标识/Logo、水印，禁止出现额外人物。手部/手指形态须自然且解剖正确。禁止面部扭曲、左右不对称、肢体重复或人工伪影。
输出：高分辨率、高度写实、符合企业级个人档案照标准。
```

</details>

<details><summary><b>企业标志设计师</b></summary>

```text
{
  "system_instruction": "充当资深品牌标识设计师。根据以下参数，设计一个专业、可扩展的企业级标志。",
  "brand_variables": {
    "name": "${COMPANY_NAME}",
    "industry": "${INDUSTRY}",
    "core_aesthetic": "${AESTHETIC_STYLE}", 
    "primary_color": "${BRAND_COLOR_HEX_OR_NAME}",
    "metaphor": "${VISUAL_SYMBOL_DESCRIPTION}"
  },
  "design_logic": {
    "composition": "符号与文字排布的专业平衡组合。",
    "typography": "对 '${COMPANY_NAME}' 进行高保真渲染。风格：粗体、现代、无衬线，字间距优化。",
    "symbolism": "融入一个代表 ${VISUAL_SYMBOL_DESCRIPTION} 的极简几何图形。",
    "color_theory": "主要使用 ${BRAND_COLOR_HEX_OR_NAME}，搭配干净、高对比度的背景。"
  },
  "nano_banana_constraints": {
    "style_reference": "瑞士平面设计，现代企业极简主义",
    "technical_specs": [
      "矢量风格的清晰度",
      "无 3D 效果或投影",
      "纯平色块",
      "在小尺寸下仍保持最高可读性"
    ],
    "negative_space": "利用刻意留白来增强 ${AESTHETIC_STYLE} 的视觉感受。"
  },
  "output_format": "居中，单个标志版本，无场景 mockup，白色背景。"
}
```

</details>

<details><summary><b>企业证件照</b></summary>

```text
根据上传的图像，创建一张适合公司工牌和内部系统使用的人像证件照。  
保持面部与上传图像完全一致，具有真实的比例，不进行美化或年龄调整。

构图：  
• 中性、居中的头部和肩部构图  
• 被摄者直视镜头，表情中性但友好  

背景：  
• 纯色均匀背景，颜色为 [BACKGROUND_COLOR]，无纹理、无渐变  
• 无道具、无文字、无标志  

风格：  
• 均匀柔和的照明，阴影最小化  
• 面部清晰锐利，肤色自然，高分辨率  

着装：  
• 将服装转换为符合企业环境的 [OUTFIT_STYLE] 风格  
• 不显示任何标志、图案或分散注意力的配饰  

使最终效果看起来像是升级版、光线良好、专业的公司证件照或门禁卡照片，可直接用于内部工具、电子邮件账户或通行证中。
```

</details>

<details><summary><b>伊兹尼克郁金香柏树瓷砖</b> · 机器翻译</summary>

```text
一幅宽幅伊兹尼克釉面陶瓷砖板画,中央是一棵高大的深绿色柏树,两侧各有一只小钴蓝花瓶,瓶中生出舒展的红色郁金香、蓝色康乃馨和白色风信子。经典的十六世纪奥斯曼伊兹尼克风格:明亮的白色石英熔块底色,深钴蓝、绿松石色、祖母绿,以及凸起的番茄红硼土釉彩,轮廓深色清晰,色彩平整而有光泽。细长的锯齿状萨兹叶在花朵之间弯曲伸展,梅花枝点缀在上方两个角落。由交错的蓝色与绿松石色云纹带和小花饰组成的边框环绕整幅画板。画板由方形瓷砖拼成,可见淡淡的灰缝、釉面轻微的开片、略带手绘的不规则感,光亮的表面上映着窗光的柔和反射。正面拍摄、光线均匀的博物馆摄影,构图完全对称,色彩浓郁而明亮。宽幅横向 16:9。无人物,无手,无文字,无字母,无书法,无标志。
```

</details>

<details><summary><b>伊斯坦布尔写字楼自拍</b></summary>

```text
{
  "subject": {
    "description": "一位纹身众多的年轻女性，身处伊斯坦布尔一座现代广场办公楼的室内。她气质自信，拥有丰满的沙漏型身材。她的手臂和躯干布满黑白及彩色纹身，包括动漫人物、蛇类和文字图案。她佩戴带有金色标志的 Miu Miu 无框太阳镜和一条极简贝壳项圈。",
    "body": {
      "type": "丰满的沙漏型身材。",
      "details": "曲线玲珑的轮廓，腰细臀宽。双臂布满各种纹身艺术。腹部部分被衣物覆盖，在合适的位置可隐约看到纹身。",
      "pose": "坐在现代办公桌前，身体微微前倾，从桌面高度自拍一张特写照片。"
    }
  },
  "wardrobe": {
    "top": "合身的中性色调衬衫或轻质针织上衣，适合企业广场办公室环境。",
    "bottom": "高腰定制长裤或及膝裙，颜色为米色、灰色或黑色。",
    "layer": "可选西装外套搭在肩上或敞开穿着。",
    "accessories": " temples 上带有金色标志的 Miu Miu 无框太阳镜、精致的黄金饰品、极简贝壳项圈、腕表。"
  },
  "scene": {
    "location": "伊斯坦布尔的一处高层广场办公楼层，配有通顶落地玻璃窗（camekan）。",
    "background": "现代广场办公室内部，配备大办公桌、人体工学办公椅、笔记本电脑、记事本、简约装饰，透过玻璃可见伊斯坦布尔城市天际线。",
    "details": "整洁的办公表面、玻璃窗上的倒影、充满空间的自然日光。"
  },
  "camera": {
    "angle": "桌面高度的自拍角度，特写视角，仿佛由手在办公桌上拍摄。",
    "lens": "广角前置摄像头自拍镜头。",
    "aspect_ratio": "9:16"
  },
  "lighting": {
    "type": "通过大型玻璃窗进入的自然日光。",
    "quality": "柔和、均衡的日光，具有轻柔的高光和真实的室内阴影。"
  }
}
```

</details>

<details><summary><b>伊斯坦布尔蜡笔旅行手账</b></summary>

```text
{
  "title": "伊斯坦布尔旅行日记",
  "artwork_style": "生动活泼、儿童蜡笔风格的竖版（9:16）插画",
  "background": "柔和、温暖的浅色调（例如：淡黄色）",
  "color_palette": "明亮的红色、蓝色、绿色及其他欢快色彩",
  "atmosphere": "温馨、俏皮的旅行氛围",
  "main_scene": {
    "title": "蜿蜒曲折的旅行路线",
    "style": "用箭头与虚线连接多个地点",
    "itinerary": {
      "city": "伊斯坦布尔",
      "duration": "7日行程",
      "stops": [
        {
          "day": 1,
          "attraction": "圣索菲亚大教堂 & 蓝色清真寺",
          "description": "探索巨型、五彩缤纷的清真寺——它们看起来就像童话故事里的城堡！"
        },
        {
          "day": 2,
          "attraction": "托普卡帕宫",
          "description": "参观苏丹们的居所——一座拥有闪闪发光珠宝的宏伟宫殿！"
        },
        {
          "day": 3,
          "attraction": "大巴扎 & 香料市场",
          "description": "迷失在一家家店铺组成的巨大迷宫中，这里有闪亮的灯具和甜甜的香气！"
        },
        {
          "day": 4,
          "attraction": "博斯普鲁斯海峡游船",
          "description": "乘坐大船航行于欧洲与亚洲两大洲之间！"
        },
        {
          "day": 5,
          "attraction": "加拉塔塔",
          "description": "攀上一座超级高塔，从空中俯瞰整个伊斯坦布尔！"
        },
        {
          "day": 6,
          "attraction": "王子群岛",
          "description": "在一座没有汽车的岛屿上，乘坐马车兜风！"
        },
        {
          "day": 7,
          "attraction": "土耳其软糖 & 巴克拉瓦",
          "description": "回家前享用美味、黏稠又香甜的土耳其糖果——真是美妙的款待！"
        }
      ]
    }
  },
  "surrounding_elements": {
    "characters": [
      {
        "description": "一名手持西米特（一种美味的土耳其贝果）的儿童"
      },
      {
        "description": "一名背着背包、戴着费兹帽的小探险家"
      }
    ],
    "landmarks": [
      "一座圆润可爱的、面带微笑的圣索菲亚大教堂",
      "一座高耸而多彩的加拉塔塔",
      "一座看起来友善亲切的博斯普鲁斯大桥"
    ],
    "signboards": [
      "别在大巴扎里迷路啦！",
      "前方有海鸥！",
      "美味的土耳其软糖在这边！"
    ],
    "phrases": [
      "伊斯坦布尔旅行记忆已解锁！",
      "伊斯坦布尔美食探险！",
      "下一站去哪儿？"
    ],
    "food_icons": [
      "一支卡通风格的土耳其冰淇淋蛋筒（dondurma）",
      "一块面带微笑的巴克拉瓦",
      "一盘色彩缤纷的土耳其软糖（lokum）"
    ],
    "exclamations": [
      "我以前不知道伊斯坦布尔这么有趣！",
      "我还想再坐一次渡轮！"
    ]
  },
  "overall_style": {
    "art_style": "蜡笔画 / 儿童手绘风格的旅行日记",
    "palette": "明亮、温暖、多彩的配色方案",
    "composition": "温馨但饱满而富有活力的构图",
    "emphasis": "探索的乐趣",
    "font": "可爱的手写体字体",
    "feeling": "一名幼童充满趣味的旅行日记条目"
  }
}
```

</details>

<details><summary><b>伊斯坦布尔街头漫步</b></summary>

```text
全身电影感镜头：一位气质成熟、年约三十出头的男士，自信地行走在伊斯坦布尔贝伊奥卢区一条历史悠久的鹅卵石街道上。他留着短胡须，头发乌黑。身着量身定制的深蓝色羊毛大衣、炭灰色高领毛衣和黑色长裤。一手提着一款高端棕色皮革公文包，另一手持一杯外带咖啡。脚穿棕色皮革切尔西靴，佩戴时尚太阳镜。背景中，标志性的加拉塔塔在街道尽头巍然矗立。柔和自然日光，高端时尚摄影风格，解剖结构比例真实，8K 分辨率，纹理高度精细。--ar 9:16
```

</details>

<details><summary><b>伊斯坦布尔街景点画插图</b></summary>

```text
高度细致的手绘插图，描绘伊斯坦布尔一条繁忙的街道交叉口，灵感源自塔克西姆广场 / 独立大街的人流场景，画面中充满密集人群，朝多个方向移动。整个场景采用点画法 / 点绘技法（钢笔墨水风格）创作，通过紧密排列的黑色墨点形成明暗、质感和氛围深度。

建筑呈现层次丰富的伊斯坦布尔城市景观：历史性的奥斯曼时期建筑与现代 storefronts、咖啡馆、有轨电车线路以及密集垂直招牌相融合。表面覆盖土耳其商店招牌、面包店标识、街头广告、海报和发光的城市细节，将当代都市生活与文化遗产融为一体。

构图采用略微俯视的广角视角，并具有强烈的景深线索。前景布满密集行人，中景展示主要交叉路口和有轨电车走廊，背景延伸至密集的城市街区和天际线轮廓。

以黑白单色点画作为基础渲染方式，辅以选择性鲜艳强调色（红色、蓝色、绿色、黄色），突出标识牌、有轨电车元素、旗帜和关键视觉焦点。插图应显得极为复杂，包含微小细节、层层叠加的纹理以及强烈的视觉叙事性。

包含浓厚的城市密度感、微小的人物形象、微妙的运动暗示以及复杂的建筑变化。风格融合传统欧洲点刻版画与现代城市插画美学。

-- ultra detailed -- 8k -- high resolution -- intricate -- hand drawn -- ink illustration -- stippling -- dot shading -- urban scene -- crowded city -- Istanbul
```

</details>

<details><summary><b>优雅暗黑小丑人像</b> · 机器翻译</summary>

```text
拍摄角度：特写/中近景人像摄影，与视线齐平。

构图：竖版 3:4 画幅，主要聚焦于面部、颈部和肩部。面部居中，头部微微倾斜。

背景：深色、极简的哑光炭黑色影棚背景，没有多余细节。背景柔和虚化，与女子的面部、鲜红色头发和妆容形成戏剧性的对比。

姿势与氛围

姿势：女子直视镜头，神情自信、神秘，略带俏皮。

氛围：大胆、受 cosplay 启发、优雅的暗黑漫画美学，灵感来自小丑女/小丑的丑角风格。

妆容与面部细节

肤色：均匀、明亮的瓷白肤色，带有柔和的哑光质感。

眼部：轮廓分明的图形感深色眉毛，浓郁的烟熏眼妆，眼睑上带有金铜色闪光，睫毛长而富有表现力。

妆容艺术元素：

- 左眼下方（观者的左侧）的脸颊上：一个带有装饰图案和一颗小黑心的细长红色菱形，眉毛上方还有一个小红菱形。
- 右眼下方（观者的右侧）：一个细长的黑色菱形，眉毛上方有一个小黑菱形。

嘴唇：浓郁的哑光黑色口红，轮廓锐利分明。

发型与发色

样式：头发中分利落，扎成两条低马尾。

马尾颜色：一条马尾是亮红色，配红色发圈，另一条是深炭黑色。发丝均匀地垂落在肩上。

服装与配饰

服装：红色抹胸上衣或束身衣款式上衣，面料有质感，带有竖向接缝。

配饰：一条紧贴颈部的黑色天鹅绒丝带颈圈。

光线与氛围

光线：柔和的正面影棚直射光，例如环形灯或专业柔光箱灯光，均匀照亮面部并突出妆容细节。一道微弱的轮廓光将头发和肩部与深色背景分隔开。

氛围：流行文化丑角美学，万圣节 cosplay，鲜艳的红色元素与暗色点缀形成强烈对比。

重要：不要改变参考图中的面部特征或身份。精确保留面部结构、眼睛、鼻子、嘴唇和其他显著的面部特征。

Format: 3:4
画质：超写实、高品质、锐利的 8K 照片，自然的皮肤质感，细节丰富，使用 iPhone 16 Pro 拍摄。
```

</details>

<details><summary><b>优雅海岸网纱人像</b> · 机器翻译</summary>

```text
超写实的年轻女子特写肖像，她有一头长长的波浪发，以四分之三的姿势坐在海边的海岸岩石上。她身穿一件透明的棕色网纱连衣裙（细针织面料），露背，细肩带在颈部系结；双手交握在脸旁，佩戴精致的银色手链和一枚戒指，姿态放松、若有所思，身体挺直，脸朝向镜头。场景发生在黄金时刻，有温暖的逆光和侧光，以及柔和的环境光晕；微风吹动她的几缕发丝。湿润岩石和沙子的细致质感清晰可见；背景是虚化的海岸线和平静的大海，带有悦目的焦外虚化效果。竖向构图，半身取景，低角度，焦点在手臂和肩膀上；优雅的编辑风格（灵感来自 Pinterest 或时尚编辑作品），电影感调色（温暖的琥珀色和大地色调），柔和的阴影，细微的胶片颗粒和轻微的暗角，专业修图。相机设置：85 mm 镜头，f/1.8，ISO 100，快门速度 1/200 秒，浅景深，精准对焦，柔和的焦外虚化。2:3 照片，特写。
```

</details>

<details><summary><b>优雅缎面极简人像</b> · 机器翻译</summary>

```text
一位成年女性站在极简而优雅的室内空间中的编辑风格摄影作品，以竖向 9:16 画幅拍摄。她有一头长而浓密、自然卷曲/波浪的棕色头发，棕色眼睛，轮廓分明的眉毛，以及自然、均衡的五官。她穿着一条黑色缎面质感的长裙，紧贴身形，细肩带挂脖领口，后背部分裸露，裙摆有一道侧开衩。这条裙子优雅地顺着她的身形线条，同时保持自然的身体比例。

女子以放松而精致的姿态站立，身体微微转向相机呈四分之三侧面，一只手臂自然垂放在身侧，目光直视镜头。她佩戴着精致简约的金色手链。

温暖的室内环境，奶油色/米色的墙壁，浅色地板，几乎没有任何装饰。强烈的自然光从侧面透过窗户射入，在墙面和地板上投下柔和的几何形阴影。温暖的黄金时刻光线，自然的阴影，真实的皮肤质感，以及真实的摄影质感。

超写实摄影，时尚编辑风格，优雅而精致，自然的构图，柔和的景深，真实的头发和皮肤细节，自然的电影感光线，适中的对比度，暖色调，无 CGI 外观，无塑料感皮肤，无过度修饰。

相机：iPhone 17 Pro，主摄拍摄，24 mm 等效焦距镜头，高分辨率拍摄，自然 HDR，均衡曝光，精准对焦于面部，轻微景深，高端抓拍摄影质感。

格式：9:16 竖向，全身，从头到脚取景，居中构图，自然透视，无身体变形。
```

</details>

<details><summary><b>优雅黑白S曲线人像</b> · 机器翻译</summary>

```text
生成一张写实的、竖构图 3:4 的黑白肖像,画面中是一位身穿不对称罗纹针织连衣裙的年轻女性。她在优雅的动态中被捕捉,摆出 S 形曲线姿态,发丝随风飘动,目光低垂而内省。柔和的漫射侧光在中性灰色背景上营造出细腻的明暗对照。模拟中画幅胶片质感,带有细腻的颗粒和浅景深,以锐利的 8K iPhone 16 Pro 画质保留精确的面部特征。
```

</details>

<details><summary><b>会安灯笼河图生视频</b> · 机器翻译</summary>

```text
以第2步的图像“Lantern-Lit Old Town River with a Roofed Footbridge and a Rowboat at Dusk”作为精确的首帧，将其制作成一段平静的${duration:6}秒电影感镜头。左岸挂着灯笼的屋檐下的黄赭色店屋、中央远景处带瓦顶亭子的木制拱形人行桥、右侧远岸、桥后方带粉紫色辉光的深蓝色暮色天空，以及整体取景构图，都要与图像中完全一致。在右中前景，戴白色斗笠的船夫缓缓拉动长木桨，载着一堆发光纸灯笼的狭长木划艇轻缓地向右下方滑行，在深色水面上留下柔和扩散的涟漪；船夫始终坐在船的右端。众多漂浮的纸灯笼缓缓顺流漂移，在水面上轻轻起伏，烛火闪烁，长长的倒影粼粼闪动。沿店屋屋檐悬挂的圆灯笼在微风中轻轻摇摆，几个小小的人影在步道上漫步，暮色天空略微变深。镜头只做一次非常缓慢、平稳的向桥推进。自然写实的运动，无剪切，无新物体，无文字。轻柔的水波拍岸声、桨入水的轻微水声，以及远处傍晚的低语。
```

</details>

<details><summary><b>会安灯笼河场景简报</b> · 机器翻译</summary>

```text
扮演一位电影级环境设计师，撰写可直接用于图像生成和动态生成的场景简报。请帮我设计一个英雄镜头：黄昏时分，一条灯笼点亮的河流穿过越南历史古镇，灵感来自会安风格的灯笼之夜的氛围。该镜头将先生成静态图像，再以这张图像作为首帧，制作成一段短视频。你的简报必须让静态图像中包含丰富的、可以自然运动的元素（纸灯笼在水流上漂移起伏、烛火闪烁、倒影粼粼、一艘小木划艇载着船夫用一支长桨划行、悬挂的灯笼在微风中摇摆、几个人在河边步道上漫步、暮色天空缓缓变深），同时保持构图平静、清晰易读、便于制作动画。

我的初始选择：
- 古镇环境：${setting:a calm river lined with yellow ochre two-story shophouses with dark wooden shutters and terracotta tile roofs}
- 时间与天空：${time:blue hour, deep blue twilight sky with a soft pink-violet glow on the horizon}
- 地标：${landmark:a wooden arched footbridge with a small tiled pagoda-style roof spanning the river in the distance}
- 灯笼：${lanterns:round silk lanterns in red, orange, and yellow along the shopfronts, and many small square paper lanterns with candles floating on the water}
- 船：${boat:one narrow wooden rowboat with a rower in a conical hat carrying a pile of glowing lanterns}
- 视觉风格：${style:photoreal cinematic travel photography}
- 情绪关键词：${mood:calm, warm, magical, quiet}

请先用一条简短的消息向我询问缺失的信息：我偏好的相机视角（贴近水面的低角度、河岸边平视，或从阳台略微俯视）、店屋应排列在画面的哪一侧、船应位于何处以及朝哪个方向行进、漂浮灯笼的密度，以及需要避免的内容（人脸特写、可读的招牌或文字、标志、现代汽车或摩托车、电线、人群、复制某张特定的真实照片）。

然后按以下章节撰写简报：

1. **场景概述**：用两三句话描述地点、时间、光线和这一刻的感觉。描述的是一个想象出来的、带有该地神韵的古镇河景，而不是对某张特定照片的复制。

2. **古镇建筑**：店屋排列在哪一侧河岸，它们的颜色、百叶窗、阳台和屋顶，店屋前的河边步道（咖啡桌、低矮的石砌河堤），悬挂灯笼的位置（沿屋檐或横跨街道串挂），以及对岸有什么。

3. **桥与景深**：人行桥在画面中的位置，它的拱形和屋顶亭子，如何被照亮，它在水中的倒影，以及从前景水面到桥再到对岸的景深层次。

4. **水上灯笼**：漂浮灯笼的数量、形状和颜色，它们如何从前景向桥的方向分布，倒影的样子，以及它们都顺着同一个轻缓的水流方向漂移。

5. **船与船夫**：船在画面中的位置、角度和长度，船夫坐在哪一端，斗笠和服装，长桨以及它入水的位置，船上那堆灯笼，以及船将要滑行的方向。

6. **光线与氛围**：暮色渐变，桥后方的地平线辉光，温暖的灯笼光与冷蓝色黄昏的对比，倒影的闪烁，以及水面上任何淡淡的薄雾。

7. **固定视觉细节**：一份编号列表，列出8到10个必须在静态图像和视频中保持一致的细节（店屋所在的河岸一侧、桥的位置和形状、屋顶亭子、灯笼颜色、漂浮灯笼的分布、船的位置和角度、船夫和长桨、地平线辉光的位置、相机位置、取景构图）。

8. **运动图**：一张表格，列出视频中所有可以运动的元素，列包括：元素、运动类型、方向、速度（很慢、慢、中等）以及运动幅度。包括船和桨、漂浮灯笼、烛火闪烁、倒影、悬挂灯笼、漫步的人、天空和镜头运动。整体运动保持细微且符合物理规律，水面只有一个水流方向，悬挂灯笼只有一个微风方向。

9. **提示词种子 A - 英雄静态图**：一条可直接粘贴的图像提示词，少于170词，用于宽幅横向16:9画面，第一句话中包含灯笼河流、店屋、人行桥和划艇，结尾为：no close-up faces, no text, no signs, no logos。

10. **提示词种子 B - 图生视频动画**：一条可直接粘贴的视频提示词，少于120词，以英雄静态图作为首帧，描述船夫划桨、船轻缓滑行、灯笼漂移与闪烁、悬挂灯笼摇摆、约6秒的一次缓慢镜头运动，并说明店屋、桥、船和取景构图要与图像中完全一致，不出现新物体。

规则：人物只能是小尺寸的人影加一位船夫，绝不作为主体，也不得有细致的面部；不得有文字、招牌或标志；文化细节要尊重且真实，不落刻板印象；不得有快速镜头运动或剪切；不得有违背物理规律的运动（漂浮灯笼随水流移动，不会飞起也不会下沉；船只在桨的推动下才会移动，并留下涟漪；火焰会闪烁但不会变大；建筑和桥永远不会改变形状）。使用简短的段落和列表。
```

</details>

<details><summary><b>低多边形浮空岛风车农场</b> · 机器翻译</summary>

```text
一幅风格化的低多边形 3D 渲染图,描绘黄金时刻漂浮在柔软云海之上的一座小型空中岛屿农场。岛屿是一块厚实的多面体岩石,可见平整的多边形面,呈暖砂岩色和赤陶色,边缘有小瀑布倾泻而下,化作薄雾。岛顶有一座白色木制风车,四片风帆缓缓转动,还有一间小小的红色谷仓、由多面体小麦、薰衣草和向日葵田组成的拼块田野、一条蜿蜒的土路,以及几棵圆形几何树木。一只带条纹的小型热气球漂浮在附近,用一根细绳系在岛上,远处有一群简单的三角形小鸟飞过。旁边还悬浮着两块较小的、各长着一棵树的漂浮岩石。柔和的全局光照,轻柔的环境光遮蔽,来自低角度太阳的暖色轮廓光,长而柔和的阴影,淡桃色到薰衣草紫的柔和天空渐变,干净的平面着色材质,无贴图纹理,微妙的景深,玩具般温馨可爱,以现代独立游戏主视觉图的风格渲染。无文字,无角色,无标志,1:1 方形构图。
```

</details>

<details><summary><b>俏皮捉鬼敢死队万圣节自拍</b> · 机器翻译</summary>

```text
这张照片传达出轻松、俏皮、温暖的氛围。这是一张充满节日气息的镜子自拍，记录了为万圣节做准备的快乐。柔和的光线和一只小宠物的出现，让居家氛围更加温馨。

拍摄角度：
照片在镜子中拍摄，距离适中，取景到腰部以上。相机（手机）大致与视线齐平，形成平直自然的自拍视角。画面为竖版，以女子和她的宠物为主要焦点。

主体：
主体是一位年轻女子和一只小吉娃娃。

女子——外貌与服装

服装与配饰：
女子穿着一件合身的米色无袖连体衣/背心，灵感来自《捉鬼敢死队》制服。

左胸处是官方的"No Ghost"标志——红色禁止圆圈内的经典白色幽灵。

腰间系着一条带有大号扣环的宽黑色战术腰带，凸显腰线。

颈间佩戴一条纤细精致的金链。

左手腕上可见数条金手镯，包括一条较宽和一条较细的手镯。

她左手拿着一部带双摄像头的粉色 iPhone。手机遮住了部分脸庞，但笑容依然可见。

姿势：
女子以放松的姿势站立，左手举着手机拍摄镜子自拍。右手轻轻托着小狗。她直视镜子，甜美地微笑，嘴唇紧闭，带着淡淡的半笑。

发型：
头发披散，质地自然，带有柔和的波浪。发型偏向一侧，增添了柔美感。

妆容：
自然妆容，并为万圣节庆祝略作加强。嘴唇涂着浓郁的莓果色口红，眼部以淡妆轻轻勾勒。

小狗——外貌与服装

一只深棕色的小吉娃娃，胸前有一块白色斑纹。小狗穿着一件可爱的幽灵服装。

服装是一件白色斗篷，上面画着两只大大的椭圆形黑眼睛和一张黑色嘴巴，类似经典的"床单幽灵"。

小狗通过镜子直视镜头，神情平静而好奇。女子用右手轻轻抱着小狗。

背景与光线

背景：
场景是一间温馨的住宅房间，营造出温暖的家的氛围。

左侧可见部分床铺。

右侧墙边是一个带浅色木门的大衣柜。

衣柜与镜子之间可见一段拼花地板或复合地板。

室内风格现代、极简、整洁。

光线：
柔和、自然、漫射的光线（很可能是日光）充满房间。没有强烈的阴影。光线自然地突出了服装的颜色、女子的面部和小狗，同时营造出温暖舒适的氛围。

重要：不要改变参考图中的面部特征或身份。精确保留面部结构、眼睛、鼻子、嘴唇和其他显著特征。

表情：淡淡的、自然的半笑，嘴唇紧闭。

Format: 3:4
画质：超写实、高品质、锐利的 8K 照片，自然的皮肤质感，细节丰富，使用 iPhone 16 Pro 拍摄。
```

</details>

<details><summary><b>俏皮猫耳闪光人像</b> · 机器翻译</summary>

```text
不要改变女孩的面部特征、眼形、眉毛、鼻子或嘴唇。保持 100% 的面部相似度。

画幅:3:4。超写实、高质量、清晰的 8K 照片,由 iPhone 16 Pro Max 拍摄。

主体与姿势:一位年轻 女性,造型俏皮,带有猫咪风格。中近景肖像,带有放松、抓拍式的 Pinterest 美学。她身体微微倾向镜头,肩膀自然倾斜,头部轻轻歪向一侧,一只手随意地触碰头发或锁骨。她的姿势应显得自然随性、放松、女性化且撩人,绝不僵硬或像证件照。她直视镜头,表情俏皮自信,嘟起柔软的飞吻唇,眼睛明亮而富有表现力,眼神甜美带着调皮。

服装与配饰:一件修身白色束身胸衣,细肩带,前襟挂钩扣。一个毛茸茸的白色猫耳发箍,内耳为柔软的粉色。叠戴的精致金色项链,配有小硬币吊坠,以及小号金色圈形耳环。

发型:浓密、蓬松的 头发,打造成松散柔和的沙滩波浪。中分,柔软的发丝自然环绕脸庞并垂落在肩上。

美甲:修长优雅的方形指甲,涂有亮泽的乳白色美甲。指甲整洁、女性化、光滑,在画面中清晰可见。

妆容:清新透亮的柔和精致妆容,肌肤光彩照人,蜜桃粉腮红,睫毛分明,淡淡的棕色眼影,纤细的上扬眼线,亮泽的裸桃色嘴唇,用黑色眼线笔在鼻尖画上一个小小的黑色三角形猫鼻子,并在每侧脸颊上以同样的铅笔手绘风格画三根精致的黑色猫胡须。

光线与镜头:直闪摄影,明亮的正面光线,打造出光彩照人的肌肤、清晰的对比,以及奢华的 Instagram 杂志大片质感。平视角度,构图自然随性。

背景与氛围:夜晚的花园,深色的枝叶繁茂的树木,温暖的金色小彩灯化作奶油般的焦外虚化。喜庆、年轻、俏皮、撩人、女性化、娇俏。时尚的 Pinterest 和 Instagram 美学,像一场别致的万圣节或主题派对。
```

</details>

<details><summary><b>俏皮鱼眼抓拍人像</b> · 机器翻译</summary>

```text
GPT Image 2.5 on ChatGPT

提示词:

根据我上传的自拍照,创作一张写实的鱼眼镜头照片,完整保留她的面部特征。她坐在一扇风化的绿色木门前的门阶上,穿着米色风衣、象牙白高领毛衣和浅蓝色牛仔裤。一只好奇的虎斑白猫占据右侧前景,鼻子被夸张放大,眼神生动。柔和的日光,自然的质感,俏皮的抓拍氛围,超写实摄影,16:9 横向画幅,无文字。
```

</details>

<details><summary><b>保留面部的镜子自拍</b></summary>

```text
充当一款高级图像生成模型。你的任务是生成一张年轻女性在镜前自拍的图像，并严格保留其面部特征。

面部特征保留要求：
- 使用参考面部，确保完全一致。
- 保留以下细节：
  - 脸型
  - 眉毛与眼部结构
  - 自然妆容风格
  - 唇形与唇色
  - 发际线与发型

主体细节：
- 性别：女性  
- 描述：一位年轻女性在室内优雅下蹲，对着镜子拍摄自拍照。
- 姿势：
  - 身体姿态：低蹲姿势，单膝前伸，身体略微朝向镜子倾斜。
  - 头部：微微低头，目光注视手机屏幕。
  - 双手：
    - 右手持手机置于面部前方
    - 左手自然搭于膝盖上
  - 表情：柔和、平静的表情
- 发型：
  - 样式：深棕色长发，半扎马尾，配一枚小巧发夹
  - 质感：顺滑、直发

务必精准捕捉所描述的整体气质与风格，同时确保面部特征高度准确。
```

</details>

<details><summary><b>俯瞰雪山迷雾的玻璃温室图书馆</b> · 机器翻译</summary>

```text
一座宏大的维多利亚式玻璃温室,坐落在高山云雾之上的悬崖边,内部摆满从地板直达天花板的木质书架和悬挂的植物,清晨柔和的光线在窗格上的凝结水珠中折射,窗边有一把阅读椅和一架望远镜,铺着青苔的石板地面,电影感广角镜头,超精细,体积光,宁静的氛围
```

</details>

<details><summary><b>健身应用图标</b></summary>

```text
一款高级 iOS 跑步与健身应用的图标，采用风格化的抽象跑步者形象，由流动的渐变丝带构成，色彩从充满活力的珊瑚色过渡到鲜艳的洋红色。该形象通过拖尾运动元素暗示速度与前进动力。背景为深海军蓝，人物背后带有微妙的径向渐变，显得更亮。整体动态、充满活力、富有抱负。柔和的光线围绕人物，带有微妙的发光效果。圆角方形格式，1024x1024px。

遵循以下规格及附带的示例图标设计：

这些规格定义了顶级 iOS/macOS 应用中高级现代应用图标的视觉语言。目标是制作出感觉精致、令人难忘且配得上旗舰产品的图标。

---

## 1. 画布与形状

### 基础形状
- **格式:** 带有连续圆角的正方形（iOS“圆角矩形”）
- **圆角半径:** 约为图标宽度的 22-24%（模仿 Apple 的超椭圆）
- **宽高比:** 1:1
- **推荐分辨率:** 1024×1024px（可清晰缩放）

### 安全区域
- 将主要元素保持在画布中心 80% 的范围内
- 允许微妙的效果（发光、阴影）接近边缘但不超出

---

## 2. 背景处理

### 纯色背景
- **深色/黑色:** 纯黑 (#000000) 到深炭黑 (#1C1C1E) —— 营造戏剧感，使元素突出
- **鲜艳纯色:** 饱和的单色填充（电蓝色 #007AFF，暖橙色 #FF9500）
- **渐变背景:** 微妙的从上到下或径向渐变，增加深度

### 渐变类型（使用时）
| 类型 | 描述 | 示例 |
|------|-------------|---------|
| 线性 | 柔和过渡，通常顶部较亮 | 蓝天渐变 |
| 径向 | 中心发光效果，边缘较暗 | 聚光灯效果 |
| 角度 | 扫掠的颜色过渡 | 虹彩表面 |

### 纹理（微妙）
- 细密的垂直/水平线条，营造金属或织物质感
- 1-3% 不透明度的噪点颗粒，增加有机温暖感
- 避免与主符号竞争的重纹理

---

## 3. 色彩调色板

### 主色调特征
- **高饱和度:** 色彩鲜艳但不刺眼
- **深色丰富:** 黑色和海军蓝占据显著位置
- **选择性亮色:** 点缀色谨慎使用以增强冲击力

### 推荐色系

#### 冷色调
'''
海军蓝/深蓝:    #0A1628, #1A2744, #2D4A7C
电蓝色:     #007AFF, #5AC8FA, #64D2FF
紫色/紫罗兰:     #5E5CE6, #BF5AF2, #AF52DE
青绿色/青色:         #30D5C8, #5AC8FA, #32ADE6
'''

#### 暖色调
'''
橙色:            #FF9500, #FF6B35, #FF3B30
粉色/珊瑚色:        #FF6B8A, #FF2D55, #FF375F
桃色/鲑鱼色:      #FFACA8, #FF8A80, #FFB199
'''

#### 中性色
'''
纯黑:        #000000
柔和黑:        #1C1C1E, #2C2C2E
白色:             #FFFFFF
灰白色:         #F5F5F7, #E5E5EA
'''

### 色彩和谐规则
- 每个图标限制为 2-3 种主色调
- 使用互补或类似关系
- 一种颜色应占主导（60%），次要颜色（30%），点缀色（10%）

---

## 4. 光影与深度

### 光源
- **位置:** 左上或正上方（一致的 45° 角度）
- **质量:** 柔和、扩散 —— 无强烈阴影
- **效果:** 在上表面产生微妙高光，下方产生阴影

### 深度技巧

#### 高光
- 在 3D 形状的顶部边缘使用柔和的白/浅色渐变
- 作为小亮点的高光反射（不过度）
- 面向光线的边缘使用边缘光

#### 阴影
- **投影:** 柔和、扩散，10-20% 不透明度，轻微的 Y 偏移
- **内阴影:** 非常微妙，增加凹陷效果
- **接触阴影:** 更暗、更紧密的阴影直接位于物体下方

#### 分层
- 元素应显得浮在背景之上
- 使用大气透视（远处元素略显模糊）
- 重叠形状创造自然层次

---

## 5. 符号与图标

### 风格方法

#### A. 立体/3D 物体
- 柔和、圆润的形状，具有清晰的体积感
- 微妙的渐变暗示曲率
- 示例：纸飞机、打开的书、球体

#### B. 平面带深度提示
- 简化形状，带有策略性的阴影/高光
- 干净的几何形状，带有轻微渐变
- 示例：火焰图标、指南针表盘

#### C. 抽象/几何
- 重叠的半透明形状
- 相互锁定的形状，创造视觉趣味
- 示例：重叠的菱形、三角形组合

#### D. 玻璃质感/半透明
- 带有模糊的磨砂玻璃效果
- 形状显得透明
- 微妙的折射和色彩渗透

### 符号特征
- **简洁:** 在 16×16px 下可识别
- **平衡:** 视觉重量居中或有意动态
- **原创性:** 避免通用剪贴画感觉
- **隐喻:** 符号清晰关联应用功能

### 推荐符号比例
- 主符号：图标画布的 50-70%
- 在边缘留出呼吸空间
- 光学居中（可能与数学中心不同）

---

## 6. 材质与表面质感

### 哑光表面
- 可添加微妙纹理
- 颜色呈现坚实稳重

### 光泽/反射表面
- 明显的高光和反射
- 明暗区域对比增强
- 暗示玻璃、塑料或抛光金属材质

### 金属表面
- 模仿金属光泽的线性或径向渐变
- 银色/铬色使用冷色调，金色/青铜色使用暖色调
- 可选添加精细纹理线条

### 玻璃/半透明
- 降低不透明度（60-85%）
- 后方元素模糊效果
- 带浅色边缘的彩色色调
- 微妙的内部发光

### 纸张/布料
- 柔和、低调的颜色
- 非常微妙的纹理
- 暗示柔韧性的柔和阴影

---

## 7. 效果与润色

### 发光效果
- **外发光：** 明亮元素周围的柔和光晕，5-15%不透明度
- **内发光：** 微妙的边缘照明，营造体积感
- **彩色发光：** 与元素颜色匹配的色调发光（营造氛围）

### 反射
- 浮动物体下方微弱的倒影（非常淡）
- 光泽表面的环境反射
- 暗示光源的镜面高光

### 形状内的渐变
- 多色阶渐变实现复杂色彩过渡
- 径向渐变呈现球形外观
- 网格渐变实现有机、流畅的着色

### 模糊与景深
- 背景模糊用于分层构图
- 高斯模糊5-20px营造氛围效果
- 仅在暗示运动时使用运动模糊

---

## 8. 构图原则

### 视觉平衡
- **居中：** 符号位于视觉中心（经典、稳定）
- **动态：** 轻微偏移产生能量和动感
- **不对称：** 有意失衡，视觉上形成平衡

### 负空间
- 充足的留白/呼吸空间
- 背景是设计的一部分，而非空白
- 负空间可形成次要形状

### 焦点
- 一个明确的最高对比度/细节区域
- 视线应首先落在最重要的元素上
- 辅助元素视觉上退后

### 比例对比
- 大小元素的混合产生趣味
- 主符号占主导，细节微妙
- 避免使用大小相同的元素造成杂乱

---

## 9. 风格变化

### 极简暗色
- 黑色或极暗背景
- 单一明亮元素或单色符号
- 高对比度，戏剧性感觉
- 示例：火焰图标，股票图表

### 鲜艳渐变
- 多色渐变背景
- 上方为白色或浅色符号
- 充满活力，现代感
- 示例：Telegram，Books应用

### 柔和轻盈
- 轻盈、通透的背景（白色、淡色）
- 带柔和阴影的彩色符号
- 友好、亲切的感觉
- 示例：Altitude应用，手势图标

### 玻璃拟态
- 半透明、磨砂元素
- 不同透明度的分层形状
- 当代、精致的感觉
- 示例：快捷方式图标，重叠形状

### 3D渲染
- 逼真的3D物体
- 复杂的照明和材质
- 高端、真实的感觉
- 示例：球体、飞机、书籍
```

</details>

<details><summary><b>健身房镜前 UGC 照片</b></summary>

```text
{
  "category": "GYM_MIRROR_UGC",
  "subject": {
    "demographics": "成年女性，21–27 岁，具有土耳其人外貌特征，体格健美。",
    "hair": {
      "color": "深棕色",
      "style": "高马尾，略显凌乱",
      "texture": "可见发丝细节，带有汗湿感的碎发",
      "movement": "数缕发丝贴于额头附近"
    },
    "face": {
      "eyes": "明亮、充满活力",
      "skin_details": "真实毛孔，细微汗光",
      "makeup": "极简、自然妆容"
    },
    "clothing": {
      "outfit": "极简运动服套装（无品牌标识/文字）",
      "fit": "符合真实健美体型的合身剪裁，布料呈现自然微张力",
      "texture": "可见针织面料纹理"
    },
    "accessories": {
      "jewelry": ["小巧银质圆环耳环（可选）"]
    }
  },
  "pose": {
    "type": "镜面健身自拍氛围（不直接显示手机）",
    "orientation": "半身构图",
    "hands": "一只手臂自然放松，另一只手臂轻微屈肘（自然状态，非极端发力）",
    "gaze": "与镜中视线接触",
    "expression": "微微自豪的微笑"
  },
  "setting": {
    "environment": "健身房更衣区",
    "background_elements": [
      "带有真实污痕的镜面",
      "柔和的荧光顶灯照明",
      "背景设备呈虚化状态"
    ],
    "depth": "面部与躯干清晰锐利；背景柔化"
  },
  "camera": {
    "shot_type": "半身镜面人像",
    "angle": "略高的拍摄角度（典型休闲自拍视角）",
    "focal_length_equivalent": "24–28mm 手机广角等效焦距",
    "framing": "4:5",
    "focus": "面部焦点清晰，背景略柔和"
  },
  "lighting": {
    "source": "健身房荧光顶灯照明",
    "direction": "自上而下的主光，镜面提供柔和补光",
    "highlights": "真实汗光高光",
    "shadows": "下颌下方阴影柔和"
  },
  "mood_and_expression": {
    "tone": "积极向上、真实可感、自然随性",
    "expression": "自豪且友善"
  },
  "style_and_realism": {
    "style": "照片级真实感用户生成内容（UGC）",
    "imperfections": "轻微噪点，白平衡略有偏差"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "轻微",
    "motion_blur": "极少"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "品牌标识", "可读文字",
    "多余手指", "扭曲镜面",
    "塑料质感皮肤", "CGI 风格外观"
  ]
}
```

</details>

<details><summary><b>傍晚咖啡馆人像</b> · 机器翻译</summary>

```text
机位与构图：中近景人像（取景到胸部以上），平视角度拍摄。镜头略微偏移，使前景中包含桌子和咖啡杯。

姿势：一位年轻女子坐在户外咖啡馆的桌旁，身体微微前倾。她的头俏皮地向左肩倾斜，直视镜头，带着柔和友好的闭唇微笑。一只手自然地放在桌上。

发型：中分直发，自由地垂在肩上。

妆容：自然而精致的柔和魅力妆，带有细腻的黑色上扬眼线、分明的睫毛、修饰整齐的眉毛、温暖自然的腮红，以及柔和的灰粉色唇妆。

服装：黑色针织开衫或V领毛衣，内搭细肩带黑色吊带背心。

配饰：精致的多层金色项链，其中一条带有小星星吊坠，以及小号金色圈形耳环。

光线：温馨的傍晚光线，柔和的漫射光照亮她的脸。她右后方有一个明亮的红橙色光源（类似庭院取暖灯或灯笼），营造出温暖的光晕，并在她的头发上形成细腻的高光。

氛围与背景：轻松浪漫的傍晚咖啡馆露台。背景昏暗并柔和虚化，可见大片热带绿叶和优雅的户外咖啡馆元素。

细节：前景的绿色大理石桌上放着一套深海军蓝的陶瓷杯碟，盛有卡布奇诺或拿铁，饰有经典的树叶或爱心拉花。

不要改变她的面部特征、眼型、眉毛、鼻子或嘴唇。保持100%的面部相似度。

宽高比：3:4。超写实、高质量、锐利的8K照片，使用iPhone 16 Pro Max拍摄。
```

</details>

<details><summary><b>像素消散美食3D变形</b></summary>

```text
极简主义食物摄影，[1080x1080] —— 一个 ${food} 置于浅色哑光表面上，正处于向 3D 像素化形态转变的瞬间：一半保持完整原貌，另一半则有机地碎裂为若干大型悬浮立方体，这些立方体向外飘散，每个立方体均清晰呈现该食物的纹理、配料与色彩。影棚布光，配以柔和且逼真的阴影；景深较浅；构图与透视考究；细节高度写实；风格化几何抽象；立方体带有微妙的运动模糊；高分辨率；电影级特写镜头。
```

</details>

<details><summary><b>像素画提示词生成器</b></summary>

```text
充当一个像素艺术提示词生成器。当用户提供一个主题、场景、角色、物体或想法时，请使用以下风格生成详细的图像生成提示词：

- 块状的低分辨率像素艺术  
- 粗重的黑色轮廓线  
- 醒目的卡通形状  
- 大而富有表现力的眼睛  
- 柔和的赛璐珞着色，采用双色调阴影  
- 鲜艳饱和的色彩调色板  
- 泡泡糖粉红、天蓝、森林绿、日落橙作为点缀色  
- 使用抖动和交叉排线的纹理  
- 复古16位主机RPG美学  
- 可爱的、受kawaii风格启发的设计  
- 细微的粗粝细节  
- 柔和的背景散景光效  
- 梦幻怀旧的氛围  
- 呈现480p上采样后的视觉效果  
- 最近邻像素缩放算法  
- 清晰锐利的像素边缘，无抗锯齿处理  

规则：  
1. 保持用户提供的主题不变。  
2. 将其扩展为一个高度详细的图像生成提示词。  
3. 除非用户另有要求，否则仅输出最终提示词。  
4. 切勿提及任何在世的具体艺术家或受版权保护的风格。
```

</details>

<details><summary><b>儿童时装摄影</b></summary>

```text
全身，丰满的，美丽的儿童，新时装，随机服装，随机儿童，现代新风格，柔焦，景深，8k 照片，HDR，专业灯光，使用 Canon EOS R5 拍摄，DSLR，75mm 镜头
```

</details>

<details><summary><b>儿童蜡笔涂色风格</b></summary>

```text
一幅卡通 ${setting} 场景，使用蜡笔为 ${detail1}、${detail2} 和 ${detail3} 上色，风格如同学龄儿童所绘。
```

</details>

<details><summary><b>元素周期表可爱3D角色</b></summary>

```text
我希望创建一张 4K 图像，为元素周期表中的每种元素设计一个 3D 角色。我希望它们看起来可爱，但又具有独特的特征。
```

</details>

<details><summary><b>光轨中的低语</b></summary>

```text
你将使用所提供照片中的人物作为主要主体，执行图像编辑。保留他们原本的核心相貌特征。将主体 1（男性）转化为一名 1950 年代的侦探，将主体 2（女性）转化为一位迷人的爵士歌手。采用“长曝光”艺术风格，使时间仿佛流淌、弥散。主体 1 坐在角落卡座中，纹丝不动，轮廓锐利、神情专注；主体 2 则向前倾身低语，其动作被捕捉为一道优雅而幽灵般的动态模糊。背景中的乐手与舞者则被渲染为富有表现力的光迹与运动拖影，强化这对人物秘密会面周围喧嚣混乱的氛围。

{
  "title": "Whispers in Light Trails",
  "description": "一幅电影感十足的长曝光影像，呈现 1950 年代黑色电影（noir）场景，静止不动的侦探与动感十足的爵士俱乐部形成鲜明对比。",
  "prompt": "你将使用所提供照片中的人物作为主要主体，执行图像编辑。保留他们原本的核心相貌特征。将主体 1（男性）转化为一名 1950 年代的侦探，将主体 2（女性）转化为一位迷人的爵士歌手。采用“长曝光”艺术风格，使时间仿佛流淌、弥散。主体 1 坐在角落卡座中，纹丝不动，轮廓锐利、神情专注；主体 2 则向前倾身低语，其动作被捕捉为一道优雅而幽灵般的动态模糊。背景中的乐手与舞者则被渲染为富有表现力的光迹与运动拖影，强化这对人物秘密会面周围喧嚣混乱的氛围。",
  "details": {
    "year": "1952",
    "genre": "Long Exposure",
    "location": "一间狭小、烟雾弥漫的地下室爵士俱乐部，配有红色皮革卡座和一个小型舞台。",
    "lighting": [
      "昏暗的环境烛光",
      "背景中划过舞台的聚光灯光束",
      "面部柔和的高光"
    ],
    "camera_angle": "平视特写镜头，居中构图，1:1 画幅比例。",
    "emotion": [
      "隐秘的",
      "忧郁的",
      "强烈的"
    ],
    "color_palette": [
      "深琥珀色",
      "阴郁的炭黑色",
      "鲜活的猩红色光迹",
      "霓虹蓝色"
    ],
    "atmosphere": [
      "充满动能的",
      "朦胧的",
      "如梦似幻的",
      "黑色电影风格（Noir）"
    ],
    "environmental_elements": "丝滑顺滑的香烟烟雾轨迹、背景中黄铜乐器散发出的金色光束、人群模糊的运动痕迹。",
    "subject1": {
      "costume": "质感丰富的灰色风衣、软呢帽（fedora）以及一条松开的领带。",
      "subject_expression": "坚忍而强烈，目光笔直锁定前方。",
      "subject_action": "端坐不动，手持一杯威士忌。"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "凝固的动作",
        "清晰锐利的背景",
        "静止不动的烟雾",
        "日光"
      ],
      "exclude_styles": [
        "高速摄影",
        "卡通风格",
        "矢量艺术",
        "平光照明"
      ],
      "exclude_colors": [
        "粉彩色系的粉色",
        "明亮的绿色",
        "纯白色"
      ],
      "exclude_objects": [
        "智能手机",
        "现代麦克风",
        "数字腕表"
      ]
    },
    "subject2": {
      "costume": "一件闪亮的亮片晚礼服，配长及肘部的歌剧手套。",
      "subject_expression": "妩媚而急切，尽管因运动模糊而略显柔和。",
      "subject_action": "迅速前倾低语，形成动态拖影效果。"
    }
  }
}
```

</details>

<details><summary><b>公寓窗边夜晚随拍</b></summary>

```text
超写实风格的业余夜间照片，竖构图手机快照，拍摄自安卡拉一间小型公寓内部，镜头朝向一扇窗户，捕捉一条“iyi geceler”（晚安）推文所传递的氛围。相机位置较低且略微倾斜，仿佛由躺在或坐在沙发上的某人随手拍下。前景中可见一只磨损布面沙发的扶手和一条柔软毛毯，略微失焦。

中景中，一名27岁、具有土耳其人相貌特征的女性站在窗边，身形柔和、略带丰腴；她背部部分朝向镜头，一手持手机置于胸前高度，另一只手轻轻搭在窗框上。她穿着舒适、不暴露的居家服装：一件宽松的浅色连帽卫衣，搭配印有简洁图案的阔腿睡裤。她的金发自然垂落于背后。无法看清手机屏幕内容；仅见屏幕发出微弱的蓝光，映在她的脸庞与手上，暗示她刚刚发布了一条推文。

窗外，街道被一盏明亮的钠灯（橙黄色）照亮，使沿街建筑与停泊车辆泛出暖调辉光。一辆明黄色出租车停靠在路边，略有虚化。街道对面是一栋老式公寓楼，带有阳台，部分窗户漆黑，少数仍亮着灯。一家位于一层的小型Migros Jet或Şok超市招牌隐约可见，泛着柔和微光；远处还有一块模糊的蓝色Turkcell店铺招牌，以及更远处街道尽头一块极小的Ülker广告牌，均处于失焦状态。

室内仅开着一盏暖光落地灯，投下低矮而温馨的光线，与窗外冷调的蓝光形成对比。房间角落积聚着阴影；室内略显杂乱：一堆书、咖啡桌上一只马克杯、一支电视遥控器。竖构图略显随意：女子更靠近画面右侧边缘，部分窗框被裁切，顶部还闯入一盏灯罩——整体效果宛如一张真实、未经构图的手机快照。

暗部区域可见明显的高ISO噪点，窗外驶过的一辆汽车带有轻微运动模糊，且未施加强烈色彩分级——仅呈现自然混合的暖光与冷光。整个场面调度（mise-en-scène）应让人感受到安卡拉一间真实公寓里宁静的瞬间，恰在轻声对时间线道出“iyi geceler”后的数秒。
```

</details>

<details><summary><b>公寓镜前球衣自拍</b></summary>

```text
“现代公寓室内镜面自拍场景。一名年轻女性，留有长而自然卷曲的浅棕色头发，头戴一顶深色棒球帽（后方可见调节带），身穿黑色短袖足球衫（粉红色字体与数字‘10’），下着黑色高腰紧身裤。她背对镜头、面向镜子；面部大部分不可见（后视/三分之四背面视角）。  
她右手在肩高位置持有一部黑色智能手机，肘部弯曲约90°，手腕伸直，手机后置摄像头正对镜子，使镜中手机屏幕呈现相同场景（即‘手机套手机’递归反射）。左臂自然垂落于身侧。  
相机与构图：以镜面自拍视角从后方拍摄；镜头焦距等效26–28mm，机位高度约在人眼水平；竖版构图；画面裁切范围为大腿中部至头顶上方，构图中心对准球衣上的文字与数字。室内光线为柔和自然日光；无强烈阴影。  
环境：左侧为一扇白色门，配有金属杠杆式门把手；门旁为一段窄墙；门洞敞开，通向极简风格厨房（可见高柜式冰箱/烤箱立柱）；墙面为浅中性色调，地面为浅色。背景略微虚化但清晰可辨。  
服装细节须保留：球衣上“MESSI”字样以圆润粉红色字体呈现，位于硕大的粉红色“10”上方；粉红色线条风格保持一致；球衣版型略宽松；帽子为深色；紧身裤为哑光黑色；发长及背部中段，带有数缕松散卷曲。  
姿态与微角度：头部略向右倾斜，帽檐轻微向下倾角；双肩放松；骨盆正对镜子；脊柱保持中立位。右手握持稳固，指尖可见于手机远端边缘；手机边缘与镜框平行；手机大致居中于脊柱延长线上。  
布光：柔和自然室内光，白平衡中性，不使用闪光灯，无色彩偏移。所有反射均符合物理规律，无重复影像或错位现象。  
美学风格：干净、写实、未经滤镜处理、皮肤与织物纹理真实还原；球衣文字与手机主体锐利聚焦；颗粒感极低。  
裁切与画幅：主用3:4（竖版）；安全备选画幅为9:16与4:5，须确保球衣全部文字与数字完整呈现在画面内。”  
一致性锁定（不得更改）：  
同一女性：发长、发色、卷曲形态；深色棒球帽（含后方调节带）；黑色球衣（粉红色“MESSI”+“10”）；黑色紧身裤；右手肩高持手机；左臂自然下垂；镜面自拍（背面视角）；公寓/厨房整体布局；带金属杠杆式门把手的门；整体相机高度≈人眼水平；镜中手机屏幕可见递归反射。  
保持人物比例与体型；禁止瘦身/拉长处理。  
球衣文字颜色与字体须完全一致；禁止重新设计。  
维持环境几何结构与物体摆放位置。
```

</details>

<details><summary><b>共生体战衣时尚人像</b> · 机器翻译</summary>

```text
一张写实风格的年轻女性肖像，她留着中分的长蜜棕色头发，身穿黑色蜘蛛侠共生体战衣，战衣带有凸起的蛛网图案质感，胸前有金属灰色的蜘蛛标志。她以四分之三侧身姿势站立，双手放在胸前，目光直视镜头，眼神锐利。专业影棚灯光，阴影柔和，中灰色无缝背景。中景构图，竖构图。高细节的面料质感，电影感摄影风格，85mm 镜头，锐利对焦，杂志大片品质。
```

</details>

<details><summary><b>写实东京旅行 Vlog 人像</b> · 机器翻译</summary>

```text
创作一张写实的智能手机旅行 vlog 图像:一位虚构的 20 岁日本女性,在傍晚走过东京一条热闹的小街。

她有齐肩的黑发和柔和自然的刘海,暖棕色的眼睛,真实的皮肤质感,表情友善而放松。她穿着浅蓝色牛仔外套,内搭简单的白色上衣,下身是深色百褶裙,背着一个奶油色的小斜挎包。

她一只手拿着一杯透明杯装的冰抹茶,另一只手伸直手臂拍摄自己。使用广角前置摄像头视角,带有轻微的手机镜头畸变,构图自然随性、抓拍感强。

街道两旁是小餐馆和本地商店。行人在背景中自然地走动。温暖的店铺灯光和霓虹招牌在清冷的傍晚天空下开始亮起。

自然的身体比例,真实的双手,清晰的眼睛,均衡的肤色,纪实旅行摄影,无美颜滤镜,无可辨认的品牌标志,无水印,16:9 画幅。
```

</details>

<details><summary><b>写实人像</b></summary>

```text
超写实的美丽年轻女性照片，自然的皮肤质感，柔和的光线，面部细节清晰，85mm 镜头，照片级真实感，高细节，Instagram 模特
```

</details>

<details><summary><b>写实摄像头卧室场景</b></summary>

```text
{
  "subject": {
    "description": "一名年轻女性躺在床上，手持智能手机，神情平静且略带专注地看向屏幕。",
    "body": {
      "type": "女性，苗条体型",
      "details": "浅肤色，长金发，自然妆容，眼部和唇部轮廓分明",
      "pose": "侧卧在床上，上半身略微抬起，一只手臂将手机举在面前，另一只手臂 resting on the bed"
    },
    "face": {
      "expression": "中性，放松，略带专注",
      "gaze_direction": "看向她的手机屏幕",
      "head_tilt": "轻微低头"
    },
    "wardrobe": {
      "top": "黑色休闲T恤",
      "bottom": "柔软面料的睡裤短裤",
      "style": "舒适的室内休闲装 / 睡衣搭配"
    },
    "hair": "长金发，直发且略显蓬松，自然垂落在肩膀周围"
  },
  "scene": {
    "description": "通过笔记本电脑屏幕上的相机应用程序界面捕捉到的卧室场景。",
    "location": "室内卧室",
    "setting": "带有柔软毯子和枕头的床",
    "background_elements": "中性色调的墙壁，床铺略显凌乱，柔软的织物纹理",
    "lighting": "低环境光室内照明，带有柔和暖色调",
    "atmosphere": "舒适、私密、轻松的夜间氛围"
  },
  "environment": {
    "ambience": "光线昏暗、安静的室内环境",
    "style": "通过屏幕捕捉的 candid 数字画面",
    "depth_of_field": "屏幕内的主体清晰，整体略带柔化"
  },
  "camera": {
    "device": "笔记本电脑摄像头（类似 MacBook Photo Booth 风格）",
    "angle": "略高的屏幕视角",
    "aspect_ratio": "屏幕帧内 4:3",
    "framing": "主体出现在笔记本电脑显示屏内，笔记本边框部分可见",
    "focus": "中等对焦，典型的网络摄像头质量，略显柔和"
  },
  "interface": {
    "visible_ui": "屏幕上可见 Photo Booth 应用程序界面",
    "elements": "顶部栏显示 'Photo Booth' 文字，底部中央红色快门按钮，小型 UI 图标",
    "screen_effect": "轻微屏幕反光，像素柔和感，数字显示外观"
  },
  "image_quality": {
    "resolution": "类似网络摄像头的质量",
    "grain": "由于光线不足而可见的数字噪点",
    "sharpness": "略显柔和，细节不强",
    "compression_artifacts": "轻微的数字压缩伪影",
    "dynamic_range": "有限，阴影较暗，高光部分略显柔和"
  },
  "lighting": {
    "type": "低强度室内环境光",
    "quality": "柔和，略不均匀，暖色调",
    "effects": "柔和的阴影，面部上有微妙的高光"
  },
  "color_grading": {
    "tone": "温暖且柔和",
    "temperature": "略偏暖",
    "contrast": "低至中等",
    "saturation": "略微降低，自然的室内色调"
  },
  "rendering": {
    "style": "逼真的网络摄像头捕捉风格",
    "quality": "有意呈现不完美，具有屏幕截图的感觉",
    "skin_texture": "自然，因分辨率较低而略显柔化",
    "post_processing": "极少，保持原始网络摄像头外观"
  },
  "artifacts": {
    "screen_glare": "笔记本屏幕上有轻微反射",
    "noise_pattern": "可见的弱光噪点",
    "chromatic_aberration": "极轻微",
    "motion_blur": "无"
  },
  "constraints": {
    "focus_priority": "屏幕内的主体是主要焦点",
    "avoid": "过度锐利的 DSLR 外观、影棚灯光、人工滤镜"
  }
}
```

</details>

<details><summary><b>写实时尚与环境人像</b></summary>

```text
{
  "image_prompt": {
    "subject": {
      "type": "成年女性（21岁以上），与参考图像身份一致",
      "appearance": "白皙皮肤，长而凌乱的深色头发带有细微红色挑染，鼻环",
      "expression": "神情放松，直视镜头，嘴巴微张",
      "pose": "中景；双臂抬起；双手插入发间；肘部向外展开；姿态自信且随意"
    },
    "outfit": {
      "clothing": "土耳其国家足球队球衣",
      "details": "官方风格的土耳其国家队主场球衣：深红色基底，带有微妙的同色系织物纹理，干净的白色点缀，圆领设计。右胸位置有白色 Nike swoosh 标志，左胸位置有土耳其足协徽章（TFF 徽章，含新月与星）。无俱乐部徽章、无俱乐部赞助商标识、无 'Standard Chartered'、无 'Expedia'。面料呈现现代功能性聚酯材质质感，略带纹理，因动作自然产生褶皱。",
      "accessories": "手腕上佩戴黑色发圈"
    },
    "environment": {
      "location": "位于船或游艇内部，靠近窗框位置",
      "background": "晴朗天空下明亮的蓝色海洋；透过窗户可见远处多岩石的海岸线与悬崖；窗框清晰可见，有助于确立场景为从船内拍摄"
    },
    "lighting": {
      "type": "自然日光，明亮的白天光线",
      "shadows": "硬朗而真实的阳光阴影；皮肤与球衣上有清晰高光；头发呈现真实镜面反光；无影棚灯光反射"
    },
    "camera": {
      "capture_device": "智能手机或消费级相机",
      "framing": "中景（躯干与头部清晰可见），居中构图",
      "angle": "平视角度",
      "focus": "面部与球衣细节锐利对焦；背景稍柔和但仍可辨识",
      "look": "轻微自然柔化感，不过度锐化；具有真实手持拍摄感，无运动模糊"
    },
    "style": {
      "aesthetic": "随拍式 Instagram 网红风格，逼真写实，超精细细节，高分辨率，8K 视觉效果",
      "skin_rendering": "可见自然肌肤纹理与毛孔，无塑料般平滑处理，无重度修图",
      "color": "真实日光色彩，无电影感青橙色调分级，无人工滤镜",
      "quality": "干净、清晰、自然的摄影效果，面料行为与缝线真实可信"
    },
    "negative_prompt": "俱乐部标志、利物浦队徽、Nike 俱乐部球衣赞助商标识、Standard Chartered 文字、Expedia 文字、时尚大片影棚灯光、环形灯眼神光、过度摆拍姿势、塑料质感皮肤、过度磨皮面部、动漫、插画、CGI、人工背景、文字水印、拼写错误的标志、变形的队徽、多余肢体、扭曲的手部、不真实的人体结构、极端 HDR、电影级色彩分级"
  }
}
```

</details>

<details><summary><b>写实潮玩娃娃变身</b> · 机器翻译</summary>

```text
将这个女孩转换成写实的 Bratz 风格收藏级乙烯基玩偶，同时完全保留她的面容、身份、姿势、光线和原始背景。赋予她标志性的 Bratz 比例：超大的头部、巨大的杏仁形玻璃质感眼睛、小巧的鼻子、有光泽的嘴唇、纤细的腰身、修长的双腿，以及风格化的塑料手。光滑有光泽的乙烯基皮肤，高级合成纤维头发，华丽的 Y2K 时尚造型，逼真的模塑塑料细节，超写实玩具摄影，电影级布光，8K，照片级真实。不是卡通或动漫。

Negative: human proportions, human skin, small eyes, normal head, cartoon, anime, 2D art, changed background, different face, distorted anatomy.
```

</details>

<details><summary><b>写实猴子水果吃播</b> · 机器翻译</summary>

```text
创作一段超写实的 4K 真人实拍猴子水果吃播，主角水果为 [FRUIT]。

一只真实的猕猴坐在所指定水果的树上高处，身上挎着一个小号 Gucci 斜挎包，带着越南辣椒盐。

视频立即开始：猕猴自然地直接从树上摘下一整个 [FRUIT]，随后马上持续不断地吃起来。猕猴反复啃咬、咀嚼，并把 [FRUIT] 蘸上越南辣椒盐。

在整个视频中，水果必须始终严格保持为 [FRUIT]。它的自然形状、大小、颜色、果皮和质感必须与 [FRUIT] 在现实世界中的样子一致。

严格锁定水果身份：只能是 [FRUIT]。绝不用其他水果替换 [FRUIT]，绝不混入不同水果，也绝不让水果变成其他品种。

超写实的自然手机拍摄画面，自然日光，真实的猕猴行为，真实的水果质感，真实的咀嚼声，无 CGI，无卡通，无说话，无音乐，无文字，无水印。
```

</details>

<details><summary><b>写实竖版夜空</b></summary>

```text
生成一幅高度详细、逼真且具有美感的夜空图像。该图像应为竖屏构图，展现苍穹景象的辽阔与壮丽。确保画面引人注目，同时保持真实感，避免任何卡通或动画风格。重点描绘星星、星座，以及可能的银河，增强其自然魅力与生动性。
```

</details>

<details><summary><b>写实美食图生成</b></summary>

```text
以超写实美食摄影风格呈现的 ${FOOD_NAME:Fried chicken tenders with french fries} 图像，构图干净、诱人且专业，适用于餐厅菜单、宣传物料、数字屏幕及外卖平台。

该菜品以最具辨识度与理想上桌形态呈现，比例准确、细节高度逼真——包括自然的质感、酥脆的表面、湿润的内里、在适当位置可见的热气、光泽自然的酱汁，以及新鲜的食材。

布光柔和、可控且自然，灵感源自专业影棚美食摄影：高光均衡、阴影真实、色彩忠于实物，在不夸张的前提下强化新鲜感。

食物盛装于简洁雅致的盘子或碗中，摆盘极简，确保视觉焦点完全集中于菜品本身。背景干净且不抢镜（中性色台面、哑光深色背景，或柔和虚化的环境），以保障强对比度与高清晰度。

采用高端数码单反相机（DSLR）风格拍摄——浅景深、食物主体锐利对焦、镜头视角自然、分辨率极高。禁止插画、禁止风格化处理、禁止任何人工特效。

达到商用级写实水准，富有食欲感、值得信赖，可直接用于真实餐厅场景。

--ar 4:5
```

</details>

<details><summary><b>写实自拍人像</b></summary>

```text
{  
  "subject": {  
    "demographics": "年轻女性，约20–24岁，白人。",  
    "hair": {  
      "color": "灰金色至浅金色渐变。",  
      "style": "长发、直发带轻微波浪，层次剪裁，随意中分。",  
      "texture": "柔顺自然的发丝，略显凌乱，发根可见。",  
      "movement": "自然垂落于肩部与背部。"  
    },  
    "face": {  
      "shape": "椭圆脸型，下颌线柔和。",  
      "eyes": "杏仁眼，浅蓝/灰虹膜，配鲜明锐利的黑色上扬眼线。",  
      "nose": "小巧的鼻头，鼻梁柔和。",  
      "lips": "饱满丰润，粉玫瑰色，微张呈嘟嘴状表情。",  
      "skin_details": "鼻部与双颊布满明显而浓密的雀斑；肤质平滑但保留真实皮肤纹理；自然红晕。",  
      "micro_details": "右锁骨上方有一颗痣，左肩有一颗痣。"  
    },  
    "body_proportions": {  
      "build": "丰腴、曲线显著、胸部丰满。",  
      "chest": "胸部体积大，前凸显著，深沟清晰可见。",  
      "waist_to_chest_ratio": "胸围显著宽于腰围，体现沙漏型身材。",  
      "shoulders": "肩部柔和圆润，自然下斜。",  
      "dominance": "上躯干体积在画面中视觉上占据主导地位。"  
    },  
    "clothing": {  
      "top": "石墨灰色罗纹针织背心/吊带衫。",  
      "fit": "紧身贴身，充分包裹胸部体积，低圆领设计。",  
      "straps": "宽厚肩带，稳稳置于肩头。"  
    },  
    "accessories": {  
      "jewelry": [  
        "小巧的金色圆环耳环。",  
        "金色项链，坠有小巧字母‘G’吊饰。",  
        "一条更长的细金链，坠有造型鲜明的袋鼠吊饰。"  
      ]  
    }  
  },  
  "pose": {  
    "type": "手持自拍视角。",  
    "orientation": "正面特写，略带俯角。",  
    "head_position": "头部微微向被摄者右侧倾斜。",  
    "limbs": "右臂向前伸展（伸出画面外），暗示正手持相机。",  
    "gaze": "直视镜头，眼神魅惑且自信。",  
    "spine_curvature": "因胸部前凸而隐含轻微脊柱后仰弧度。"  
  },  
  "setting": {  
    "environment": "家庭浴室。",  
    "background_elements": "深棕/灰褐色亮面瓷砖墙面；左侧可见镀铬淋浴装置；右侧可见白色陶瓷马桶水箱顶部。",  
    "depth": "景深较浅，背景元素略微失焦。"  
  },  
  "camera": {  
    "shot_type": "特写，自拍肖像。",  
    "angle": "高角度（略高于眼平线），典型智能手机自拍角度。",  
    "focal_length": "等效24mm至28mm（智能手机广角镜头）。",  
    "framing": "胸部以上构图，截取至中段躯干。",  
    "focus": "眼部与面部焦点锐利，肩部略有焦点衰减。",  
    "perspective": "伸展手臂一侧呈现轻微透视缩短效果。"  
  },  
  "lighting": {  
    "source": "柔和、漫射的浴室顶置环境光。",  
    "direction": "前上方布光。",  
    "highlights": "额头、鼻尖、下巴及上胸部曲面呈现柔和镜面高光。",  
    "shadows": "下颌下方投下柔和阴影，并勾勒出乳沟深度。",  
    "quality": "自然、讨喜，无生硬对比。"  
  },  
  "mood_and_expression": {  
    "tone": "随意、妩媚、自信。",  
    "expression": "放松的嘟嘴表情，‘酷女孩’美学风格。",  
    "atmosphere": "私密、抓拍感。"  
  },  
  "style_and_realism": {  
    "style": "照片级真实感，社交媒体美学风格。",  
    "fidelity": "高保真皮肤纹理，无磨皮处理。",  
    "imperfections": "雀斑清晰可见，杂发可见，保留自然肤色差异。"  
  },  
  "colors_and_tone": {  
    "palette": "中性色调（灰色、米色、肤色）为主，点缀蓝色（眼睛）与金色（首饰）。",  
    "skin_tone": "白皙至浅小麦色，暖调底色。",  
    "white_balance": "略偏暖，室内钨丝灯混合色温。",  
    "saturation": "自然饱和度，嘴唇与眼睛略显鲜艳。",  
    "contrast": "中等对比度。"  
  },  
  "technical_details": {  
    "aspect_ratio": "3:4",  
    "resolution": "高分辨率，细节锐利。",  
    "noise": "室内光线条件下手机图像传感器特有的轻微数字噪点。"  
  }  
}
```

</details>

<details><summary><b>写实阿尔卑斯湖畔小镇</b> · 机器翻译</summary>

```text
宁静的碧绿色湖畔边缘的风景如画的阿尔卑斯村庄，（迷人的欧洲建筑:1.2），赤陶瓦屋顶，经典瑞士风格建筑，一座显眼的钟楼尖顶直指天空，翠绿的树木沿水岸排列，巍峨的雪山（Alps:1.3）耸立在背景中，头顶是晴朗的蓝天和蓬松的白云，前景中一艘小木制摩托艇（细节纹理:1.1）正驶过轻柔的涟漪，明亮的自然日光，清新的氛围，（鲜艳的色彩:1.2），照片级写实，高分辨率摄影，旅行杂志美学，广角镜头，锐利对焦，宁静的夏日，细节丰富的风景，景深，电影级光照。
```

</details>

<details><summary><b>农夫市集抓拍</b></summary>

```text
{
  "category": "FARMERS_MARKET_PRODUCE_CANDID",
  "identity_lock": {
    "enabled": true,
    "priority": "ABSOLUTE_MAX",
    "instruction": "将身份严格锁定至参考图像。仅限21岁及以上成年人。不得更改面部。"
  },
  "subject": {
    "demographics": "成年女性，21–29岁，身份须与参考图像完全一致。",
    "hair": {
      "color": "与参考图像一致。",
      "style": "松散波浪卷，耳后别起",
      "texture": "发丝清晰可见，轻微毛躁",
      "movement": "行走时自然摆动"
    },
    "face": {
      "eyes": "眼睛须与参考图像完全一致；日光下呈现明亮的高光点",
      "skin_details": "毛孔清晰可见，阳光照射下呈现自然肤质纹理",
      "micro_details": "保留所有原有印记"
    },
    "clothing": {
      "outfit": "休闲黑色上衣 + 浅色夹克（无品牌标识或文字）",
      "fabric": "棉质/牛仔布织纹清晰可见"
    },
    "accessories": {
      "bag": "帆布手提袋（无品牌标识）",
      "jewelry": ["小巧银色圆环耳环"],
      "props": ["装有农产品的纸袋（无品牌标识）"]
    }
  },
  "pose": {
    "type": "行走中抓拍",
    "orientation": "半身像",
    "hands": "一只手提着农产品纸袋，另一只手调整手提袋肩带",
    "gaze": "边笑边直视镜头",
    "expression": "明亮、自然的微笑"
  },
  "setting": {
    "environment": "户外农贸市场",
    "background_elements": [
      "色彩缤纷的水果/蔬菜摊位（无清晰可读标识）",
      "柔和的人群虚化效果（无人脸可辨识）",
      "斑驳阳光"
    ],
    "depth": "主体清晰锐利；背景呈现生动散景效果"
  },
  "camera": {
    "shot_type": "半身生活风格照",
    "angle": "平视角度",
    "focal_length_equivalent": "26mm手机镜头或35mm杂志级镜头",
    "framing": "4:5画幅，主体偏构图中心",
    "focus": "面部清晰锐利；背景柔和虚化"
  },
  "lighting": {
    "source": "自然日光",
    "direction": "柔和的正面/侧前方光",
    "highlights": "自然的面部高光",
    "shadows": "下颌下方呈现柔和阴影"
  },
  "mood_and_expression": {
    "tone": "清新、愉悦、亲切可感",
    "atmosphere": "周末抓拍氛围"
  },
  "style_and_realism": {
    "style": "逼真摄影风格的Instagram生活照",
    "imperfections": "农产品纸袋边缘允许存在轻微运动模糊"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "resolution": "高分辨率",
    "noise": "低噪点",
    "mode_variants": {
      "amateur": "略带晃动感的抓拍构图，轻微HDR效果，裁切不完美",
      "pro": "干净利落的杂志级曝光，细节锐利，浅景深"
    }
  },
  "constraints": {
    "adult_only": true,
    "single_subject_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true,
    "no_readable_signage": true
  },
  "negative_prompt": [
    "可读文字", "品牌标识", "水印",
    "身份偏移", "面部变形",
    "多余手指", "扭曲的手部",
    "塑料质感皮肤", "过度平滑处理"
  ]
}
```

</details>

<details><summary><b>冬季杂志风拼贴海报</b></summary>

```text
{
  "meta_protocols": {
    "reference_adherence": {
      "instruction": "将提供的男性面部照片严格用作 reference_image。",
      "tolerance": "零偏差",
      "parameters": "以 100% 准确度保留该男性面部的确切比例、皮肤纹理、表情、年龄与身份。",
      "stylization_constraint": "不得进行任何美化、女性化或改变面部特征的操作。"
    },
    "format_style": "编辑类冬季海报风格多面板拼贴图",
    "aesthetic_quality": "即兴 iPhone 摄影（抓拍、温馨、写实）",
    "global_textures": "轻柔飘雪、细微模拟胶片颗粒感、轻微手持拍摄不稳定性"
  },
  "consistent_elements": {
    "subject_wardrobe": {
      "outerwear": "黑色剪裁合身的羊毛大衣",
      "top": "厚实针织毛衣（深色中性色调）",
      "bottom": "经典面料长裤",
      "footwear": "冬季皮革靴",
      "style_notes": "阳刚、优雅、低调的冬季风格"
    },
    "primary_device": {
      "model": "iPhone 17 Pro Max",
      "color": "银色",
      "usage": "在相关画面中由主体手持"
    },
    "color_palette": [
      "暖琥珀色",
      "炭黑色",
      "深棕色",
      "柔和的冬季灰色"
    ]
  },
  "layout_configuration": {
    "panel_1_top_left": {
      "scene_type": "冬日黄昏街道上一家店铺橱窗的倒影式拍摄",
      "lighting_and_atmosphere": "路灯、微弱的节日彩灯、冷空气凝结水汽、大衣面料上的温暖高光",
      "subject_action": "手持手机，部分遮挡面部",
      "optical_effects": "路过的行人呈模糊剪影、多重反射、自然玻璃畸变",
      "mood": "静谧、内省、都市阳刚气质"
    },
    "panel_2_top_right": {
      "scene_type": "巴黎咖啡馆外景肖像",
      "location_detail": "巴黎街头咖啡馆的户外桌旁",
      "camera_angle": "近距离、略低角度，以强化阳刚气场",
      "subject_pose": "自信就座，姿态放松，一只手臂搁在桌上",
      "action": "手持威士忌杯，正啜饮中",
      "wardrobe_visibility": "黑色大衣敞开，针织毛衣与面料长裤清晰可见",
      "motion_dynamics": "轻雪飘落，背景行人呈现柔和动态模糊",
      "lens_characteristics": "自然手持视角，附带细微的景深压缩效果"
    },
    "panel_3_bottom_right": {
      "scene_type": "城市人行道上的亲密俯拍自拍照",
      "lighting": "温暖的街灯照明与寒冷夜空气形成对比",
      "props": {
        "held_item": "外带咖啡杯",
        "accessories": "可见有线耳机"
      },
      "texture_focus": "精细呈现羊毛大衣纹理、针织毛衣纤维、细微皮肤颗粒感",
      "mood": "孤寂、沉思的冬夜氛围"
    }
  },
  "graphic_overlay": {
    "element": "极简 Spotify 风格迷你播放器",
    "content": "Flying - Anathema",
    "style": "扁平化、干净 UI，无阴影",
    "position": "轻盈悬浮于拼贴图中央区域"
  }
}
```

</details>

<details><summary><b>冬日日出雪谷上的红色缆车</b> · 机器翻译</summary>

```text
一座带大窗的小型复古红色缆车车厢悬挂在两根钢缆上，在冬日日出时分从左向右穿越积雪的阿尔卑斯山谷，一座高大的灰色钢制格构塔架立在画面左侧积雪的岩石露头上。车厢位于画面中心偏右、略高于中线的位置，银色的顶部吊架，窗户里映着温暖的光。缆绳从塔架向右上方呈平缓的斜线延伸。远在下方，一座小村庄坐落在深色松林旁，有八间屋顶积雪的木屋和一座带细长尖顶的白色教堂，三根烟囱升起缕缕轻烟。嶙峋的雪峰布满背景，峰顶被高山辉光染成粉色和金色，一层柔软的低云在峰下的山谷中飘动。金色阳光从右侧照来，淡蓝色的天空在地平线附近渐变为桃色，空中有几片细小的雪花闪烁。写实旅行摄影风格，清冽、宁静的氛围。宽幅横向 16:9。无人物，无文字，无标牌，无标志。
```

</details>

<details><summary><b>冰岛海滩教堂图生视频</b> · 机器翻译</summary>

```text
以第 2 步的图像“黄金时刻黑沙滩与玄武岩海蚀柱之上的红屋顶白教堂”作为精确的首帧，将其制作成一段平静的、${duration:6} 秒的电影感镜头。保持左三分之一处草地岬角上带红屋顶和尖塔的白色教堂、黑沙滩的弧度、右侧的四块玄武岩和海蚀柱、最左侧的低悬太阳、地平线以及取景，与图像完全一致。长长的白色海浪线从右侧涌向海滩，以薄薄的泡沫层漫上黑沙滩，再滑回去，留下湿润的光泽。镜头中段，一团白色浪花在高而嶙峋的海蚀柱底部迸裂，随后落回水中。橙色、粉色和紫色的云朵在天空中缓缓飘移，温暖的金色光辉保持稳定，岬角上的草在风中轻轻摇曳。镜头几乎静止，只有极轻微而缓慢的推进。自然、真实的运动，无剪切，无人物，无新物体，无文字。配有海浪翻涌、风声和远处海浪的声音。
```

</details>

<details><summary><b>冰岛黑沙滩教堂场景简报</b> · 机器翻译</summary>

```text
请扮演一位电影感风景设计师，撰写可直接用于生成图像和动态画面的场景简报。帮我设计一张主视觉镜头：在冰岛黑沙滩上方的草地岬角上，立着一座红屋顶的白色小木教堂，黄金时刻，深色玄武岩海蚀柱从海中耸起。这个镜头会先生成静态图像，再以该图像作为首帧制作成一段短视频。你的简报必须让静态图像富含可以自然运动的元素（海浪线涌来并漫上黑沙滩、泡沫退去、浪花在海蚀柱底部迸发、云朵缓缓飘移、暖光略有变化、草在风中摇曳），同时保持构图平静、清晰易读、便于制作动画。

我的初始选择：
- 教堂：${church:一座红色山形屋顶、带矮红色尖塔的白色小木教堂}
- 岬角：${headland:一处通向海滩的圆润绿色草地岬角}
- 海滩：${beach:一道绵长弯曲的细腻黑色火山沙滩}
- 海蚀柱：${stacks:近海处的几座深色玄武岩海蚀柱，一座高而嶙峋，其余是较小的尖塔状岩石和一块低矮的圆形岩石}
- 时间与光线：${time:黄金时刻，太阳低悬在地平线附近，零散的云朵被映成橙色、粉色和紫色}
- 视觉风格：${style:写实风景摄影，自然色彩}
- 氛围关键词：${mood:偏远、宁静、戏剧性、温暖}

请先用一条简短的消息向我询问缺失的信息：我偏好的机位（海滩上贴近水线的低机位、从沙丘上略微抬高的机位，或从悬崖小径俯拍）、教堂和海蚀柱各自位于画面的哪一侧、太阳的位置、海面的波涛有多汹涌，以及需要避免的内容（人物、车辆、天空中的无人机、需要令人信服地飞行的鸟、文字、标志，或对某张真实照片的复制）。

然后按以下章节输出简报：

1. **场景概览**：两三句话，描述这个地方、时间、光线和这一刻的感受。描写的是一个想象中的、具有冰岛南部海岸神韵的场景，而不是对某张具体照片或某座有名字的教堂的复制。

2. **教堂与岬角**：教堂在画面中的位置和大小、白色墙面、红色屋顶和尖塔、窗户和门、低角度阳光如何照亮它，以及其下草地岬角的形状和它与海滩相接的位置。

3. **海滩与海浪**：黑沙从前景开始的弧度、湿沙的倒影、海浪线的数量、海浪涌来的方向，以及泡沫漫上沙滩的距离。

4. **海蚀柱与景深**：海蚀柱的数量、形状和高度，从左到右的位置，浪花拍击的位置，以及从前景沙滩到地平线的景深层次。

5. **光线与天空**：太阳的位置和高度、天空的色彩渐变、云的形状及其受光情况、岬角和沙滩上的长影，以及海面上的任何薄雾。

6. **固定视觉细节**：一份编号列表，列出 8 到 10 个必须在静态图像和视频中保持一致的细节（教堂的位置和颜色、尖塔形状、岬角轮廓、海滩弧度、海蚀柱的数量和顺序、太阳位置、地平线、云的布局、机位、取景）。

7. **运动图谱**：一张表格，列出视频中所有可以运动的元素，列为：元素、运动类型、方向、速度（极慢、慢、中等）、运动幅度。需包含海浪线、沙滩上的泡沫、海蚀柱处的浪花、云、草、光线和镜头运动。整体运动要保持细微且符合物理规律，只有一个海浪方向和一个风向。

8. **提示词种子 A - 主视觉静态图像**：一条可直接粘贴使用的图像提示词，不超过 170 词，用于宽幅 16:9 横向画面，第一句话中包含岬角上的教堂、黑沙滩和海蚀柱，结尾为：no people, no text, no logos。

9. **提示词种子 B - 图生视频动画**：一条可直接粘贴使用的视频提示词，不超过 120 词，以主视觉静态图作为首帧，描述海浪涌来并漫上沙滩、海蚀柱处的浪花、云朵飘移、约 6 秒的一次极缓慢的镜头运动，并说明教堂、岬角、海蚀柱和取景必须与图像完全一致，不得出现新物体。

规则：不得以人物、动物或车辆为主体；不得出现文字、标牌或标志；不得有快速镜头运动或剪切；不得有违反物理规律的运动（海浪始终从海上来并向岸边破碎，泡沫沿斜坡滑回，岩石和教堂绝不移动或变形，太阳不会跳动）。请使用简短的段落和列表。
```

</details>

<details><summary><b>冷战 1962 间谍交接</b></summary>

```text
你将使用所提供照片中的人物作为主要主体，执行图像编辑任务。保留他们核心的相貌特征。创作一幅超写实、电影级品质的画面，描绘主体1（男性）与主体2（女性）在冷战时期于一座雾气弥漫的铁桥上秘密会面的情景。该图像须呈现为一部高预算大片的某一帧画面，采用 Arri Alexa 摄影机拍摄。运用电影化布光营造深邃的阴影与高光。画面高度精细，并采用浅景深效果。主体1正将一个秘密包裹递交给主体2。构图遵循电影化的 1:1 画幅比例。  

细节：  
{  
  "year": "1962",  
  "genre": "电影级写实主义",  
  "location": "午夜时分的格利尼克桥，被浓重的河雾笼罩，仅由昏暗的黄色路灯照明。",  
  "lighting": [  
    "体积雾效布光",  
    "黑色电影风格的明暗对比法（chiaroscuro）",  
    "轮廓边缘光（rim lighting）勾勒剪影",  
    "柔和的黄色钨丝灯暖光"  
  ],  
  "camera_angle": "平视中近景，采用浅景深，使主体从雾气弥漫的背景中清晰分离出来。",  
  "emotion": [  
    "充满悬念的",  
    "紧迫的",  
    "隐秘的"  
  ],  
  "color_palette": [  
    "钢蓝色",  
    "雾灰色",  
    "钨丝琥珀色",  
    "深黑色",  
    "鲜明的猩红色"  
  ],  
  "atmosphere": [  
    "寒冷的",  
    "紧张的",  
    "电影感的",  
    "神秘的"  
  ],  
  "environmental_elements": "自下方水面升腾盘旋的雾气、潮湿的铁质栏杆、远处一辆复古检查站车辆模糊不清的车头灯。",  
  "subject1": {  
    "costume": "一件纹理明显的炭灰色羊毛双排扣短大衣，衣领竖起以抵御寒风。",  
    "subject_expression": "焦虑不安，额头泛着汗光，双眼紧张地左右张望。",  
    "subject_action": "悄然将一份皮质卷宗沿栏杆滑向主体2。"  
  },  
  "negative_prompt": {  
    "exclude_visuals": [  
      "日光",  
      "阳光",  
      "现代汽车",  
      "手机",  
      "霓虹招牌"  
    ],  
    "exclude_styles": [  
      "卡通",  
      "3D 渲染",  
      "素描",  
      "动漫",  
      "印象派"  
    ],  
    "exclude_colors": [  
      "霓虹绿色",  
      "亮粉色",  
      "粉彩色系"  
    ],  
    "exclude_objects": [  
      "雨伞",  
      "人群",  
      "现代建筑"  
    ]  
  },  
  "subject2": {  
    "costume": "一件经典米色风衣，腰间系带，头戴一顶红色帽子。",  
    "subject_expression": "沉着冷静，目光锐利而富有算计。",  
    "subject_action": "伸出一只戴黑色皮手套的手，接住卷宗，同时警觉地回头张望。"  
  }  
}
```

</details>

<details><summary><b>凌乱书桌上的学习时刻</b></summary>

```text
{
  "subject": {
    "description": "一名在家中学习的快乐大学生，在一次随意的学习过程中被捕捉到。她的头发凌乱且未加打理，呈现出自然、真实的学生状态，但表情明亮且友好。",
    "body": {
      "type": "自然、年轻的体型。",
      "details": "姿势放松但坐姿端正，看起来舒适且专注，而非疲惫。双手自然地放在笔记本或笔记本电脑附近。",
      "pose": "坐在书桌前，面带微笑望向放置在书桌表面的相机。"
    }
  },
  "wardrobe": {
    "top": "舒适的日常服装，例如宽松T恤、舒适的毛衣或简单的长袖上衣。",
    "bottom": "适合在家学习的休闲短裤、运动裤或紧身裤。",
    "accessories": "配饰极少；可能手腕上戴着发圈，佩戴简约眼镜或小巧的耳钉。"
    }
  },
  "scene": {
    "location": "学生公寓或卧室内部。",
    "background": "书桌后方的墙面，书架、便签、照片或个人物品隐约可见。",
    "details": "书桌略显凌乱，上面有教科书、笔记本、散页纸张、笔、荧光笔、笔记本电脑以及一个咖啡杯或水瓶。杂乱感随意而实用，并非混乱无序。"
  },
  "camera": {
    "angle": "相机放置在书桌左角，与桌面齐高，略微向上并向主体倾斜。",
    "lens": "智能手机相机。",
    "aspect_ratio": "9:16",
    "framing": "书桌物品出现在前景中，营造出亲密的桌面视角，仿佛观看者正坐在桌前。"
  },
  "lighting": {
    "type": "来自台灯的柔和室内光与环境室光结合。",
    "quality": "温暖、均衡的光线，带有柔和的阴影，营造出舒适而积极的学习氛围。"
  }
}
```

</details>

<details><summary><b>几何巴龙头矢量图</b></summary>

```text
专注于尖锐獠牙和复杂冠冕的巴龙（Barong）头部抽象几何矢量图。运用黄金比例和几何形状的节奏性重复。结合蜡染云纹（Batik Megamendung）的有机曲线与包豪斯（Bauhaus）的锐利线条。采用精致的靛蓝与铜色配色方案。已验证：100% 矢量，可编辑路径，无光栅效果，无品牌标识。
```

</details>

<details><summary><b>创意小册子封面设计程序</b> · 机器翻译</summary>

```text
创建一个专业程序,用于制作不同颜色的小册子封面,并可添加图片来补充画面,这些图片有助于吸引读者的注意力,采用高级版式分布,可选择产品名称“”简要概述 60 字* “”作者“”和序列号的类型、颜色和字体格式 * 参照附带的设计,模拟出更具创意的设计,并可在上方输入数据
```

</details>

<details><summary><b>利维亚的杰洛特画像</b></summary>

```text
充当图像生成助手。你的任务是创建一个来自《The Witcher》系列的标志性角色杰洛特（Geralt of Rivia）的图像。

说明：  
- 创建一个细致且逼真的杰洛特形象。  
- 包含他标志性的白色头发和两把剑。  
- 展现他粗犷且随时准备战斗的外表。  
- 使用黑暗且具有中世纪奇幻风格的背景。  

确保图像能够捕捉到杰洛特作为怪物猎人以及该系列中复杂角色的本质。
```

</details>

<details><summary><b>别墅逆向施工分镜</b></summary>

```text
作为建筑可视化专家，专精于建筑设计与住宅改造。你的任务是创建一个由 10 个画面组成的分镜图，排列为 5x2 网格（两行五列）。每个画面应具有 9:16 的纵横比，采用竖向格式。所有图像之间必须保持一致的摄像机位置和拍摄角度。分镜图应反映施工状态的渐进变化，每一后续画面均基于前一画面逐步演变（图像到图像的连续性）。

通过遵循以下原则确保画面之间的连贯性：

1. **技术规格**：包含详细的摄像机设置、光照参数和构图要求。  
2. **精确定位**：使用网格坐标系统确保元素位置的一致性。  
3. **受控变更**：每帧仅允许指定的添加或移除操作。  
4. **视觉一致性**：保持摄像机位置、光照角度和透视关系固定不变。  
5. **施工顺序**：遵循逻辑清晰且符合现实的施工步骤序列。  
6. **移除限制**：仅可移除碎屑和破败物品。  
7. **添加限制**：仅可添加实用家具、植物、照明或其他物体，且必须固定位置。

分镜图整体纵横比为 45:32，图像内不得出现任何文字。

**特殊要求**：重写分镜提示词，严格遵守“减法原则”：仅基于现有结构进行元素移除。在所有元素被移除后，将地基恢复至自然、未经打理的状态。除最后一步恢复地面外，不得添加任何新元素。

**分镜序列**（顶行从左至右，底行从左至右）：

[Row 1, Col 1] Frame 1: 完整别墅，包含所有室内家具（沙发、桌椅）、窗帘、盆栽植物、地毯、艺术品、户外躺椅、遮阳伞、修剪整齐的绿色草坪、开花花坛、玻璃幕墙、完工外立面。背景：雪山和百年老树（树叶翠绿健康）。

[Row 1, Col 2] Frame 2: 移除所有软装——家具、窗帘、盆栽植物、地毯、艺术品 全部消失。房间为空，但地板/墙壁/天花板仍保持完工状态。露台为裸露石材，花坛变为裸土区域。雪山和树木保持不变。

[Row 1, Col 3] Frame 3: 移除所有室内饰面——地砖/木地板、墙面涂料/灰泥、吊顶、灯具 全部消失。露出原始混凝土地面和粗糙的墙体基层。上方暴露混凝土底面。雪山和树木保持不变。

[Row 1, Col 4] Frame 4: 移除整个玻璃外壳——所有玻璃板、窗框、门框、外墙覆层、保温层 全部消失。建筑完全敞开，露出草坪上的内部钢/混凝土柱结构。雪山和树木保持不变。

[Row 1, Col 5] Frame 5: 移除非承重砌体——所有隔墙、填充墙、女儿墙 全部消失。仅保留主要结构骨架：裸露的直立混凝土柱、钢梁和楼板，形成空旷的网格框架。雪山和树木保持不变。

[Row 2, Col 1] Frame 6: 结构坍塌成瓦砾——柱体/梁体/楼板倒塌至地面，形成散落的废墟堆（混凝土块、扭曲的钢筋、断裂的钢材）。混凝土基础部分透过瓦砾可见。直立框架已消失。雪山和树木保持不变。

[Row 2, Col 2] Frame 7: 移除所有瓦砾——混凝土块、钢筋、钢材、废弃物 全部清除。草坪无残留碎片。整个混凝土基础完全暴露，呈干净的矩形块体置于地面。雪山和树木保持不变。

[Row 2, Col 3] Frame 8: 移除混凝土基础——基础板被拆除并完全移除。留下空旷的挖掘坑，底部为压实土壤/基岩。无任何混凝土残留。雪山和树木保持不变。

[Row 2, Col 4] Frame 9: 移除人工景观——露台铺装、混凝土车道、修剪草坪、栽培土壤 全部移除。坑洞回填至原始标高。场地变为平坦的天然未开垦土壤和泥土区域。雪山和树木保持不变。

[Row 2, Col 5] Frame 10: 将地面恢复至自然状态——平坦土壤转变为崎岖不平的地形，露出岩石、土块和零星干枯杂草。地面呈现未经驯化的混乱状态。雪山和百年老树在位置、形状和叶色上保持完全一致（仍为翠绿健康）。明亮的自然日光贯穿始终。

**关键减法逻辑**：  
- Frames 1-9：只能移除前一帧中存在的元素。禁止任何添加。  
- Frame 10：仅将地面从人工状态恢复至自然状态。

**视觉锚点**：背景中的雪山轮廓和前景中的百年老树必须在所有画面中保持完全一致的位置、大小、形状和叶色（翠绿健康）。这些元素作为视觉连续性的参考基准。
**光照一致性**：所有画面必须使用明亮的自然日光。禁止使用黑暗、阴沉或暴风雨天气的光照效果，尤其是最后一帧。

**摄像机稳定性**：所有画面必须使用完全相同的摄像机角度、构图和景深。观看视角必须锁定不变。
```

</details>

<details><summary><b>刺猬邮差水彩绘本</b> · 机器翻译</summary>

```text
异想天开的儿童绘本插画,采用松散的水彩加细致的墨线:一只戴着芥末黄围巾和小巧蓝帽子的小刺猬邮递员,骑着红色自行车沿着秋日村庄里一条蜿蜒的鹅卵石小巷前行,皮挎包里塞满了用细绳捆好的信件。小巷两旁是歪歪斜斜的木框架小屋,有圆门和发光的窗户;一只松鼠在窗台上挥手,一只兔子在她的门阶前扫着枫叶。午后金色的光线,柔和的投影,橙色、铁锈色和赭色的落叶在淡蓝色的天空下旋舞。可见的冷压纸纹理,柔和的色彩晕染与沉淀颗粒感,留白的高光。宽幅横向构图,刺猬位于左下三分之一处,小巷向上蜿蜒通向山顶的风车。温馨、友善、怀旧的氛围,适合 3 至 7 岁儿童,无文字,无字母,无标志。
```

</details>

<details><summary><b>前卫幽灵分身人像</b></summary>

```text
一幅超写实 8K 电影级影棚肖像，构图自人物中腿部以上，呈现一位自信伫立于浓烈赭红色背景前的人物。主体身穿一件 oversized、肌理感极强的轰炸机夹克，夹克表面采用混搭抽象拼布图案，色调融合低饱和与高饱和的红、蓝、绿及米褐色；下装为宽松的土橄榄色工装裤，内搭白色 T 恤。布光为强烈正面光，投下清晰锐利的阴影，并凸显织物纹理。画面中一个标志性的艺术元素是：主体后方偏右位置，叠加一个半透明、带有运动模糊效果的幽灵分身，该分身呈水平方向疾速掠过，拖曳出缤纷色带，暗示高速运动或时间扭曲。背景保持统一，但带有微妙渐变，营造景深而不喧宾夺主。成片采用高端时尚杂志编辑风格拍摄：主体人物焦点锐利，景深极浅，影棚写实细节精准，整体传递出大胆、实验性、前卫的艺术氛围。
```

</details>

<details><summary><b>前卫黑白棚拍人像</b> · 机器翻译</summary>

```text
一张惊艳的黑白影棚人像照片,主角是一位美丽的年轻女子,留着带有淡淡挑染的长波浪发,五官精致,眉形分明,嘴唇自然,目光强烈地直视镜头。她坐在木凳上,背景是纯黑色的深色背景。她的姿势:右腿向上弯曲,脚踩在凳面上,左臂搭在抬起的膝盖上,右手轻轻触碰头部附近的头发。她穿着一件黑色蕾丝短款文胸上衣和浅色做旧破洞牛仔裤,膝盖处有磨损的破洞。专业影棚灯光,来自前侧方的柔和定向光,形成淡淡的伦勃朗式阴影。使用专业单反相机拍摄,85mm人像镜头,f/1.8光圈,中等景深。编辑级高级时尚摄影风格,艺术感的黑白人像,全身至四分之三身构图,相机略微仰拍。超精细,高分辨率,照片级写实,脸部和眼睛对焦锐利,自然的皮肤质感,电影感对比度。
```

</details>

<details><summary><b>副驾驶黄金时刻自拍</b></summary>

```text
{  
  "category": "CAR_PASSENGER_SEAT_SELFIE",  
  "identity_lock": {  
    "enabled": true,  
    "priority": "ABSOLUTE_MAX",  
    "instruction": "将身份严格锁定至参考图像。精确保留面部比例、五官特征与肤色。仅限21岁及以上成年人。"  
  },  
  "subject": {  
    "demographics": "成年女性，21–29岁，土耳其人外貌（需匹配参考图）。",  
    "hair": {  
      "color": "匹配参考图。",  
      "style": "松散，略带微风拂过感",  
      "texture": "可见单根发丝；少量飞毛",  
      "movement": "发丝自然垂落于肩部，带有细微动态感"  
    },  
    "face": {  
      "eyes": "眼部形状须与参考图完全一致；窗光在眼中形成明亮高光",  
      "skin_details": "可见毛孔，呈现温暖光泽；不进行柔化处理",  
      "micro_details": "精确保留所有细微痕迹"  
    },  
    "clothing": {  
      "top": "休闲黑色上衣或连帽衫（无任何标志/文字）",  
      "texture": "可见棉质织物纹理"  
    },  
    "accessories": {  
      "jewelry": ["小巧银色圆环耳饰"]  
    }  
  },  
  "pose": {  
    "type": "手持自拍氛围（不可显示手机）",  
    "orientation": "特写至半身构图",  
    "head_position": "头部微微倾向窗光方向",  
    "limbs": "一只手臂隐含于画外，暗示正持手机拍摄",  
    "gaze": "直视镜头",  
    "expression": "自信而放松的轻噘嘴（微妙自然，不夸张）"  
  },  
  "setting": {  
    "environment": "汽车乘客座位",  
    "background_elements": [  
      "座椅面料纹理清晰可见",  
      "窗光拉出的光斑条纹",  
      "车窗外景虚化（不可见可识别的文字标识）"  
    ],  
    "depth": "面部锐利清晰；背景呈柔和虚化"  
  },  
  "camera": {  
    "shot_type": "自拍风格人像",  
    "angle": "略高于眼平线",  
    "focal_length_equivalent": "24–28mm智能手机广角",  
    "framing": "3:4 或 4:5 构图，胸部以上裁切",  
    "focus": "双眼锐利清晰；肩部区域略有焦外衰减"  
  },  
  "lighting": {  
    "source": "黄金时刻阳光透过汽车车窗入射",  
    "direction": "侧前方暖调光源",  
    "highlights": "脸颊与发丝上呈现暖调高光",  
    "shadows": "下颌下方投射柔和阴影，对比度真实自然"  
  },  
  "mood_and_expression": {  
    "tone": "随意、自信、自然抓拍",  
    "atmosphere": "温暖的旅途瞬间"  
  },  
  "style_and_realism": {  
    "style": "照片级写实社交自拍",  
    "imperfections": "轻微噪点，白平衡略有轻微偏差"  
  },  
  "technical_details": {  
    "aspect_ratio": "4:5",  
    "resolution": "高分辨率",  
    "noise": "阴影区域含轻微颗粒感",  
    "mode_variants": {  
      "amateur": "构图略带轻微晃动感，面部以外区域有细微运动模糊，具备手机式HDR效果",  
      "pro": "曝光更干净，微对比度更锐利，但仍保持真实感"  
    }  
  },  
  "constraints": {  
    "adult_only": true,  
    "single_subject_only": true,  
    "no_text": true,  
    "no_logos": true,  
    "no_watermarks": true,  
    "no_readable_outside_signs": true  
  },  
  "negative_prompt": [  
    "身份偏移", "面部形变",  
    "扭曲的车内环境", "重复主体",  
    "多余手指", "解剖结构错误",  
    "可读文字", "标志", "水印",  
    "塑料质感皮肤", "过度柔化"  
  ]  
}
```

</details>

<details><summary><b>加拉塔塔复古黑白照片</b></summary>

```text
{
  "colors": {
    "color_temperature": "neutral",
    "contrast_level": "high",
    "dominant_palette": [
      "black",
      "white",
      "grey"
    ]
  },
  "composition": {
    "camera_angle": "wide shot",
    "depth_of_field": "deep",
    "focus": "Galata Tower",
    "framing": "加拉塔塔位于画面的上半部分中央，两侧由高大、深色的柏树垂直框起。"
  },
  "description_short": "一张来自伊斯坦布尔墓地的 vintage 黑白照片，画面中可见加拉塔塔和古老的木屋，并由高大的柏树框起。",
  "environment": {
    "location_type": "cityscape",
    "setting_details": "场景位于伊斯坦布尔的一个历史街区，可能是加拉塔。背景矗立着标志性的石砌加拉塔塔。中景是古老的、可能是木结构的奥斯曼时期建筑。前景是一片杂草丛生的区域，看起来像是墓地，地面突出着风化的墓碑或木桩。",
    "time_of_day": "afternoon",
    "weather": "clear"
  },
  "lighting": {
    "intensity": "strong",
    "source_direction": "side",
    "type": "natural"
  },
  "mood": {
    "atmosphere": "对过去的永恒而怀旧的一瞥。",
    "emotional_tone": "melancholic"
  },
  "narrative_elements": {
    "character_interactions": "中景可见两个人物，站在一栋建筑附近。他们的互动很少，更像是场景日常生活中的一部分，而非焦点。",
    "environmental_storytelling": "图像将坚固的石砌塔楼与腐朽的木结构和墓地并置，暗示了历史、记忆和时间流逝的主题。",
    "implied_action": "场景静止而安静，捕捉了历史城市中一个静止的瞬间。"
  },
  "objects": [
    "Galata Tower",
    "Cypress trees",
    "Wooden houses",
    "Tombstones",
    "Stone walls"
  ],
  "people": {
    "ages": [
      "adult"
    ],
    "clothing_style": "traditional Ottoman-era attire",
    "count": "2",
    "genders": [
      "male"
    ]
  },
  "prompt": "一张 vintage、高对比度的黑白照片，拍摄的是伊斯坦布尔历史悠久的加拉塔塔。标志性的石塔顶部呈圆锥形，在明亮的天空下矗立于背景之中。高大、深色、威严的柏树框起了整个画面。前景和中景是一片古老的墓地，布满风化的墓碑和破败的奥斯曼木屋，营造出一种历史感和忧郁氛围。光线是明亮的自然阳光，投下清晰的阴影。整体氛围永恒而怀旧。",
  "style": {
    "art_style": "realistic",
    "influences": [
      "19th-century photography",
      "travel photography",
      "documentary"
    ],
    "medium": "photography"
  },
  "technical_tags": [
    "black and white",
    "monochrome",
    "vintage photograph",
    "historical",
    "high contrast",
    "film grain",
    "Galata Tower",
    "Istanbul",
    "Ottoman architecture",
    "vertical composition"
  ],
  "use_case": "Historical and architectural studies, dataset for vintage photo restoration, cultural heritage documentation.",
  "uuid": "4b0a2894-4d0f-4bd1-82ee-5ee7cf81e135"
}
```

</details>

<details><summary><b>加里弗兰克风格墨线插画</b></summary>

```text
{
  "type": "illustration",
  "goal": "创作一幅宽幅电影感插画：一名孤独的牛仔坐在旧西部酒馆门前的木椅上，时值黄昏。画面以精细的手绘墨线勾勒轮廓，并覆盖浓郁的数字上色。技法融合大胆的黑色墨水轮廓线与深邃、多层、完整渲染的色彩表现，呈现出高端杂志插画与图像小说艺术中常见的戏剧性写实风格。",

  "work_surface": {
    "type": "单幅插画，横向构图",
    "aspect_ratio": "16:9 宽屏电影比例",
    "medium": "黑色墨水线稿搭配全数字色彩渲染 —— 线稿具有传统手绘墨线的自信笔触质感，色彩则具备受油画影响的数字绘画的深度"
  },

  "rendering_technique": {
    "line_work": {
      "tool_feel": "传统蘸水笔与画笔在纸上的墨水质感 —— 自信、果断的笔触，带有自然的线条粗细变化。不追求矢量般干净，也不追求潦草松散。在精准控制中保留有机的温暖感。",
      "outer_contours": "粗黑墨线轮廓（等效3-4pt）清晰勾勒出人物与主要物体。这些轮廓线赋予画面强烈的图形冲击力 —— 即使在缩略图尺寸下，剪影依然清晰可辨。",
      "interior_detail": "细墨线（1-2pt）用于面部特征、皮革缝线、木纹、布料褶皱、皱纹、发丝等细节。此类内部细节是高端插画与简单卡通之间的分水岭 —— 对表面纹理与形态的极致关注。",
      "spotted_blacks": "战略性使用大块实色墨黑区域 —— 门廊遮檐下的深影、帽檐内部、背心最深的褶皱处。这些黑色块面创造强烈的图形对比，稳定画面构图。",
      "hatching": "极少使用。仅在必要处（如门廊天花板底面、深色布料褶皱）出现，为紧密、受控的平行线。绝不松散或装饰性。阴影主要通过色彩而非排线来定义。"
    },

    "color_work": {
      "approach": "在墨线之上进行完整渲染、多层叠加的数字绘画。非平涂，非赛璐珞上色。每个表面都有连续的色调渐变 —— 仿佛每一块区域都以油画习作的精细程度绘制。",
      "skin": "多色调表现。暖褐色基底，下颌线与眼窝处带有冷调阴影，鼻部与阳光照射的颧骨略带红润，眉弓与颧骨有精确的高光。皮肤呈现风霜感且富有生命力。",
      "materials": "每种材质需区别呈现。皮革在光滑区域有轻微蜡质光泽，在磨损处呈哑光粗糙感。牛仔布可见细微的斜纹肌理。金属（扣具、枪、马刺）具有锐利的镜面高光。木材展现木纹、积尘与岁月包浆。棉质衬衫呈现柔和的漫射透光感。",
      "shadow_color": "关键：阴影并非仅是基础色的加深。阴影向冷蓝色-紫色偏移（#2d2d44, #3a3555）。棕色皮背心的阴影不是深棕色，而是带有蓝紫色底调的深棕。这种阴影中的色彩偏移营造出氛围深度与电影般的丰富感。",
      "light_color": "夕阳直射处，表面叠加温暖的琥珀金色调（#FFD280, #E8A848）。这是叠加效果 —— 金色光层覆盖在固有色之上，使受光面呈现辉光。"
    },

    "detail_density": "极高。观者应能放大画面并发现新细节：门廊木板上的单个钉头、皮革上特定的裂纹图案、帽檐褶皱中积尘的方式、威士忌杯口的一处微小缺口、靴底的磨损痕迹。这种对细节的密集观察呈现，营造出一个真实人物所处的真实场景的沉浸感。",

    "DO_NOT": [
      "不要使用平涂色块 —— 每个表面都需有色调渐变",
      "不要使用赛璐珞上色或硬边色块",
      "不要使用卡通比例或夸张手法",
      "不要使用动漫或漫画渲染惯例",
      "不要使用柔边喷枪融合而模糊墨线",
      "不要使用水彩透明或边缘晕染效果",
      "不要使用照片级写实渲染 —— 墨线必须清晰可见且为核心",
      "不要使用潦草、粗糙或未完成感的线条质量",
      "不要使用粉彩或饱和度低的褪色色彩 —— 色调应浓郁而深邃"
    ]
  },

  "color_palette": {
    "sky": {
      "upper": "#1a1a3e 深靛蓝 —— 夜幕自上而降",
      "middle": "#6B3A5E 带灰的紫紫褐过渡色",
      "lower_horizon": "#E8A040 至 #FF7B3A 灿烂的琥珀色到橙色日落余晖"
    },
    "saloon_wood": {
      "lit": "#A0784C 温暖的老化木材，沐浴在夕阳中",
      "shadow": "#5C3A20 门廊遮檐下的深棕色",
      "weathered": "#8B7355 褪色的灰褐色木板"
    },
    "ground": {
  
      "lit": "#D4B896 金色光线下温暖的沙色尘土",
      "shadow": "#7A6550 光照不到处的冷棕色"
    },
    "cowboy": {
      "hat": "#6B5B4F 深色带尘的棕色，边缘较浅呈尘色 #8B7B6F",
      "skin": "#B8845A 风吹日晒的棕褐色，深褶皱处为 #8B6B42",
      "shirt": "#C8B8A0 因岁月和尘土泛黄的褪色米白色",
      "vest": "#3C2A1A 深色磨损皮革，最深褶皱处接近黑色",
      "jeans": "#4A5568 褪色的深蓝灰色牛仔布，膝盖处有 #7B8898 的尘土高光",
      "boots": "#5C3A20 深色皮革，带有 #8B6B42 的磨损痕迹",
      "buckle": "#D4A574 古铜色金属扣，反射出一道锐利的落日余晖",
      "gun_metal": "#4A4A4A 深灰色钢材，仅有一条锐利的高光线条"
    },
    "light_sources": {
      "sunset": "#FFD280 至 #FF8C42 — 来自左侧的主导性黄金时刻暖光",
      "saloon_interior": "#FFA040 来自摇摆门后方的琥珀色油灯辉光"
    }
  },

  "lighting": {
    "concept": "黄金时刻 — 太阳刚好位于左侧地平线上方。温暖的琥珀色光线以近乎水平的角度扫过整个场景。每一个凸起的表面都仿佛在燃烧。每一道阴影都被拉得极长。空气本身也呈现出可见的暖意。这是最具戏剧性的自然光照条件 — 在此以文艺复兴时期明暗对照法（chiaroscuro）绘画的庄重感，转化为墨线与色彩的表现形式。",

    "key_light": {
      "source": "位于地平线附近的落日，从左侧低角度照射",
      "color": "#FFD280 温暖的琥珀金色",
      "direction": "近乎水平，从左向右扫射",
      "effect_on_cowboy": "牛仔面部和身体右侧被温暖的光线照亮 — 每一道风霜的皱纹、每一根胡茬的细节都在金色光线下清晰可见。左侧则陷入冷蓝色至蓝紫色的阴影中。形成强烈的半明半暗肖像效果。",
      "effect_on_environment": "长长的影子向右投射在布满尘土的地面上。朝向阳光的木质表面泛出琥珀色光芒。空气中的尘埃颗粒在光线中闪烁，如同漂浮的金色火花。"
    },

    "fill_light": {
      "source": "上方黄昏天空的环境光",
      "color": "#6B7B9B 冷调蓝紫色",
      "effect": "为阴影区域填充冷色调。避免纯黑色出现 — 阴影中仍可见细节，但整体偏蓝紫色调。这种主光与补光之间的冷暖对比造就了画面的丰富性。"
    },

    "accent_light": {
      "source": "从酒馆内部溢出的油灯光芒，穿过摇摆门和窗户",
      "color": "#FFA040 温暖的琥珀色",
      "effect": "在牛仔的帽檐后缘和肩部形成轮廓光。使人物与背景分离。同时在门廊地板上投下几何形状的窗格光影。"
    },

    "shadow_treatment": {
      "coverage": "画面中 45-55% 的区域处于阴影之下",
      "cast_shadows": "牛仔的长影向右横跨街道。门廊顶篷在酒馆立面上投下坚硬的水平阴影。椅子腿投下细长的阴影线条。",
      "face_shadows": "半脸照明。右侧温暖且细节丰富。左侧为冷色阴影 — 眼窝深陷，颧骨形成锐利的阴影边缘，从明到暗过渡处可见胡茬的点状纹理。",
      "atmospheric": "可见的尘埃微粒漂浮在夕阳光束中。在光中呈现金色，在阴影中则不可见。营造出厚重温暖空气的氛围感。"
    }
  },

  "scene": {
    "composition": "宽银幕电影构图。牛仔略微偏左居中 — 位于黄金分割点。酒馆立面占据背景右侧三分之二空间。布满尘土的街道向左延伸至地平线与落日方向。这种不对称构图 — 右侧为坚实的建筑结构，左侧为空旷的荒野 — 强化了情感上的孤独感。一个孤独的身影，伫立于文明（酒馆）与荒野（开阔沙漠）之间的边界。",
    
    "the_cowboy": {
      "position": "坐在酒馆前门廊的一张粗糙木椅上",
      "pose": "身体后仰，重心落在椅子后腿上。左脚平放于门廊地板。右脚踝搭在左膝上 — 姿态放松，不慌不忙。右手松松地握着一个短款威士忌杯，杯子搁在右膝上，杯中酒已饮去一半。左手 resting on the chair arm or thigh。头部微微低垂，但目光直视前方地平线 — 那是一种历经沧桑才有的‘千码凝视’。肩膀宽阔但未显紧张。肢体语言传达出：我虽在休息，但从不松懈。"
  
      "face": "这必须是一张具体的面孔，而非泛泛的牛仔形象。中年，40至50岁之间。方下巴，胡茬下仍可见清晰的下颌线。深陷的眼睛位于突出的眉骨之下——眼神锐利、警觉，因夕阳强光而微微眯起。三天未刮的胡茬，深色中夹杂着下巴处的灰白。饱经风霜的皮肤——眼角放射状的深刻鱼尾纹，额头横向的皱纹，鼻唇沟已变成永久性的深沟。左颧骨上有一道愈合的疤痕——细而白，陈旧。鼻子略歪，是很久以前骨折所致，鼻梁上有凸起。嘴唇薄，呈中性直线——既非皱眉，也非微笑。这张脸经历了数十年艰苦的户外生活，每一道褶皱都诉说着过往。",
      "clothing_detail": "宽边牛仔帽，深灰棕色，布满尘土，磨损严重——帽顶有凹痕，帽檐边缘微微卷曲且磨损起毛，帽带上可见一圈汗渍。褪色的米白色棉质衬衫，袖子卷至前臂中段，露出被阳光晒黑的手臂，肌腱与静脉清晰可见。衬衫外搭一件深色皮背心，使用痕迹明显——表面部分开裂，缝线在接缝处清晰可见，有些区域因多年使用而变得哑光。褪色的深蓝灰色牛仔裤，膝盖和大腿处因磨损而颜色更浅，布满灰尘。宽皮带配古董黄铜扣——扣环捕捉到一束锐利的夕阳光线。右臀处佩戴枪套，深色陈旧皮革枪套，木质枪柄可见，金属部分有反光。深棕色皮靴，磨损刮花，鞋跟略显磨损，脚踝处马刺带已扣紧。",
    },

    "the_saloon": {
      "architecture": "经典的西部边疆酒馆。两层木结构建筑，带有假立面（ facade 高于实际屋顶线，使其看起来更宏伟）。由粗糙锯切的木板建成，部分木板因年代久远而变形。入口上方有一块招牌：'SALOON'，暗红色背景上是褪色的金色字母——油漆开裂，角落处剥落，其中一个字母比其他更褪色。",
      "entrance": "中央设有摆动式双门（batwing doors），微微敞开。从门缝中透出温暖的琥珀色光芒——来自内部油灯与活动的光亮。你无法清晰看到内部，只能感受到门后蕴藏的温暖与喧嚣。",
      "windows": "入口两侧各有一扇窗户。玻璃肮脏，透出内部温暖的光晕。其中一块玻璃有一道斜向裂纹。",
      "porch": "贯穿建筑宽度的木制门廊。木板经风化呈灰色（阳光晒褪色处）与深棕色（人行踩踏磨光处）。部分木板轻微翘曲，少数钉头突出。粗凿的木柱支撑着门廊顶檐。",
      "details": "门前有一根拴马桩，系着一匹马的缰绳——绳索紧绷，暗示马匹刚出画面。拴马桩旁有一个木制水槽，表面泛绿。门边放着一个木桶。所有物体表面都覆盖着一层薄薄的沙漠尘土。"
    },
  "constraints": {
    "must_include": [
      "通篇可见粗黑墨线轮廓——这是带色彩的线稿，而非绘画",
      "丰富多层的色彩，每处表面均有色调渐变",
      "所有阴影区域呈现冷蓝色至蓝紫色调（不仅仅是基础色变暗）",
      "夕阳直射处为温暖的琥珀金色光线",
      "面部极度精细，具有特定个体特征——疤痕、皱纹、骨骼结构",
      "材质区分明显——皮革、木材、金属、织物、皮肤均呈现不同质感",
      "夕阳光束中可见大气尘埃颗粒",
      "尘土地面上投下长长的戏剧性阴影",
      "酒馆内部透出的暖光作为轮廓光/强调光",
      "左侧为广阔开放空间，与右侧坚实的酒馆结构形成对比"
    ],
    "must_avoid": [
      "任何类型的卡通或漫画风格",
      "动漫或漫画渲染惯例",
      "无渐变的平涂色彩",
      "柔化喷枪效果掩盖墨线",
      "摄影写实主义——必须可见墨水线稿",
      "无特征的泛化面孔——必须是特定人物",
      "任何看起来干净或崭新的物品——所有物件均需显示年代与磨损",
      "浑浊的暗色调——夕阳提供丰富温暖的光线",
      "僵硬摆拍姿势——应为自然放松的人体姿态",
      "水彩透明感或边缘晕染技法"
    ]
  },

  "negative_prompt": "anime, manga, chibi, cartoon, caricature, flat colors, cel-shading, minimalist, photorealistic photograph, 3D CGI render, soft airbrush, watercolor, pastel colors, sketchy rough lines, generic face, clean new clothing, bright neon, blurry, low resolution, stiff pose, modern elements, vector art, simple illustration, children's book style, pop art, abstract"
```

</details>

<details><summary><b>动态天气雷达图:布雷西亚风暴</b></summary>

```text
充当一名气象视频制作人。你的任务是为意大利北部制作一段动画天气雷达地图，聚焦于布雷西亚省。你的视频应包含：  
- 一张清晰标注的地图，西侧为Inzino，东侧为Sarezzo。  
- 一个类似飓风的旋转风暴系统，带有旋转的云带。  
- 雷达上以蓝色、绿色、黄色和红色表示强降雨区域。  
- 运动箭头显示风暴从Inzino向东移动至Sarezzo。  
- 真实的气象雷达纹理和卫星图像叠加。  
- 戏剧性但专业的电视天气预报图形。  
- 流畅的动画帧，确保观看体验无缝衔接。  

你的任务是确保该动画既具信息性又视觉吸引人，适合用于电视天气预报。
```

</details>

<details><summary><b>动漫恶魔红瞳肖像</b> · 机器翻译</summary>

```text
动漫男孩，白色短发，苍白的皮肤，黑色衬衫，特写肖像，中性表情，柔和的阴影，极简背景，发光的恶魔红色眼睛，暗红色的巩膜血丝，眼周有若隐若现的红色光晕，锐利的瞳孔，强烈的目光，电影级光效，高细节，戏剧性对比
```

</details>

<details><summary><b>动画标志标题卡片揭示</b> · 机器翻译</summary>

```text
电影感片头动画。深海军蓝背景,带有细微的粒子效果。
醒目的白色粗体大字 "MARMARA MPDS" 出现,带有青色发光效果,PDS 逐字母依次出现,颜色效果只作用于 PDS 字母,M 字母保持白色。
其下方较小的文字 "Fikirleri Projeye Dönüştürüyoruz" 淡入。
未来感、极简的科技美学。不要出现人物。
```

</details>

<details><summary><b>包豪斯风帆船赛海报</b> · 机器翻译</summary>

```text
五艘挂着醒目三角帆的帆船在平静的蓝色海湾上竞速，驶向一座小小的港口栈桥，画成包豪斯风格的几何海报，只用圆形、三角形、矩形和直线构成。船帆是扁平的原色红、黄、黑三角形，船体是纤细的黑白梯形，一个巨大的红橙色太阳圆盘低低地挂在右侧地平线上方。海面是钴蓝、藏青和浅蓝的层层水平色带，用小白色半圆表示波浪，几条细斜线暗示着风。一座由叠放的矩形构成的简洁白色栈桥从左边缘伸出，前景有一个黑色圆形浮标。背景是米白色带纹理的纸张，边缘锐利硬朗，色彩平涂无渐变，带有细微的丝网印刷颗粒感和轻微的油墨套印错位，不对称的平衡感强烈，天空留有大量负空间。现代主义 1920 年代的设计精神，简洁而欢快。宽幅横向 16:9。无人物，无文字，无字母，无数字，无标志。
```

</details>

<details><summary><b>北欧木屋客厅日间视角</b> · 机器翻译</summary>

```text
写实的室内建筑摄影，一间温暖的北欧小木屋客厅，约 3.5 乘 4.5 米，从入口门直对远处的窗户拍摄，相机位于视线高度（1.4 米），24mm 镜头，竖直线条完全垂直。墙面是竖向排列的白色刷漆浅色松木板，天花板为拱形，带有外露的浅色木梁，地板是宽板浅橡木。远端墙面正中是一扇黑框三格大观景窗，窗外是在柔和的阴天冬日光线下被积雪覆盖的松林；窗下是一个深进深的窗边座位，配燕麦色亚麻坐垫和两个芥末黄抱枕。远端左侧角落里，一棵种在陶土盆里的橄榄树。沿左侧墙面，是一张低矮的鼠尾草绿毛圈布面三人沙发，带三个坐垫和纤细的胡桃木腿，一条芥末黄针织毯搭在靠近窗户的那一端扶手上；沙发上方是两块长长的悬浮式浅橡木搁架，上面放着书、小号白色陶瓷花瓶和一株垂吊的绿萝。右侧墙面上，一台小型黑色铸铁燃木炉，立在深灰色板岩炉台上，一根黑色烟囱管升向天花板，炉内未点火；炉子前方更靠近相机的位置，是一个嵌入式柴火壁龛，里面堆着桦木柴；炉子后方靠近窗户的一侧，是一把锈橙色皮革吊带扶手椅，黑色钢框，朝向炉子倾斜摆放，椅后是一盏带锥形灯罩的黄铜落地阅读灯。中央是一张圆形胡桃木咖啡桌，放在带细炭灰色条纹的奶油色羊毛地毯上，桌上放着两本叠放的书和一只带斑点的小陶瓷碗。咖啡桌上方的木梁上悬挂着一盏大号白色宣纸球形吊灯。色板为暖白、浅橡木色、鼠尾草绿、锈橙色、芥末黄和炭灰色。氛围平静、通透、惹人喜爱，柔和的自然日光和轻柔的阴影，毛圈布、皮革、羊毛和木纹的质感真实，高端室内杂志摄影。无人物，无文字，无标志，无杂物。16:9 宽幅构图。
```

</details>

<details><summary><b>北欧木屋客厅黄昏反向视角</b> · 机器翻译</summary>

```text
写实的室内建筑摄影，还是第 2 步中的那间北欧小木屋客厅，现在从相反方向拍摄：相机位于嵌入式窗边座位上，在黄昏时分朝入口墙一侧回望房间，视线高度（1.2 米），24mm 镜头，竖直线条垂直。保持每个固定设计细节完全一致：竖向排列的白色刷漆松木板墙面，带两根外露浅橡木梁的白色拱形天花板，宽板浅橡木地板，以及铺在地板中央、带黑色点状边框的奶油色平织地毯。

此视角的左侧（即第 2 步中的右侧墙面）：两块长长的悬浮式浅橡木搁架，装在黑色支架上，上面放着陶土花瓶、小号白色陶瓷罐、叠放的书、一盆小盆栽和一株垂吊的绿萝；搁架下方是一个浅橡木餐边柜，抽屉和柜门为平板面，立在纤细的锥形腿上，柜面摆着两只哑光鼠尾草灰色陶瓷花瓶和几件小陶瓷；餐边柜上方是一盏黑色摇臂壁灯，已开启，散发温暖的光晕；靠近相机的地板上放着一只编织海草篮，里面搭着一条芥末黄针织毯。

此视角的右侧（即第 2 步中的左侧墙面）：一张浅灰色双人布艺沙发，带纤细的胡桃木腿，一条芥末黄针织毯搭在扶手上，另有一个芥末黄的纹理抱枕；沙发后面是一棵种在白色花盆里的纤细橄榄树。

远端墙面，新出现的可见内容：白色刷漆松木板的入口墙，右侧是一扇带黑色杠杆式把手的素白镶板门，三个黑色衣帽钩，其中一个挂着一件炭灰色羊毛大衣，还有一张小号浅橡木长凳，凳上铺着羊皮垫，凳下放着棕色皮靴；角落里立着一盏白色宣纸球形落地灯，散发柔和的光。

光线：蓝调时刻，来自相机身后积雪森林窗户的冷调黄昏光线，与壁灯和纸灯的温暖琥珀色光晕相混合。色板为暖白、浅橡木色、浅灰、芥末黄、陶土色、鼠尾草灰和炭灰色；羊毛、针织、陶瓷和木材的质感真实；平静的斯堪的纳维亚室内杂志摄影。无人物，无文字，无标志，无杂物。16:9 宽幅构图。
```

</details>

<details><summary><b>医生引导学生登上书阶</b> · 机器翻译</summary>

```text
为一位医生创建一个程序：他通过科学书籍，以一级一级台阶的形式为大学生铺路，为他们照亮通往成功的道路……另一方面，"成功"一词的出现令世界为之着迷
```

</details>

<details><summary><b>医疗AI分诊助手标志设计</b> · 机器翻译</summary>

```text
我正在围绕 Anaelle 打造一个品牌。Anaelle 是一款 AI 分诊助手,通过整理化验和影像报告、总结冗长的门诊信函并标记优先事项,来减轻全科医生收件箱的负担。我需要一个现代、简洁的蓝白配色标志,既能立刻传达"医疗科技"的感觉,又保持干净、专业。
```

</details>

<details><summary><b>午夜旋律之谜</b></summary>

```text
{
  "title": "午夜旋律之谜",
  "description": "一个迷人的动画黑色场景，一位粗犷的侦探在一家风格化的1950年代俱乐部里盘问一位迷人的爵士歌手。",
  "prompt": "你将使用所提供照片中的人物作为主要主体进行图像编辑。保留他们核心的相貌特征，但要进行风格化处理。将主体1（男性）和主体2（女性）转化为一部高预算动画电影中的角色。主体1是一位愤世嫉俗的私家侦探，主体2是一位耀眼的酒吧歌手。他们坐在一家烟雾缭绕、装饰艺术风格的爵士俱乐部中弯曲的丝绒卡座里。整体美学必须具有鲜明的'Disney Character'风格，包含平滑的阴影、富有表现力的大眼睛，以及一种梦幻般的电影光芒。",
  "details": {
    "year": "1950年代黑色电影时代",
    "genre": "Disney Character",
    "location": "蓝调音符酒吧，一家具有装饰艺术建筑风格、配有豪华红色丝绒卡座、背景处设有舞台的风格化爵士俱乐部。",
    "lighting": [
      "电影级聚光灯效果",
      "柔和的体积雾气",
      "来自台灯的温暖金色辉光",
      "冷蓝色环境背光"
    ],
    "camera_angle": "中近景，与视线齐平，以两人之间的小圆桌为中心构图。",
    "emotion": [
      "好奇",
      "俏皮的怀疑",
      "魅力"
    ],
    "color_palette": [
      "深靛蓝",
      "宝石红",
      "琥珀金",
      "棕褐色调"
    ],
    "atmosphere": [
      "神秘",
      "浪漫",
      "奇想",
      "烟雾弥漫"
    ],
    "environmental_elements": "旋转的风格化烟雾形状，背景中有一支复古麦克风，桌上有一只装饰着 garnish 的水晶杯。",
    "subject1": {
      "costume": "一件经典的米色风衣，衣领竖起，搭配同色系的软呢帽和松开的领带。",
      "subject_expression": "挑眉并带着一丝冷笑，看起来既怀疑又着迷。",
      "subject_action": "手持一本小型记者笔记本和一支铅笔，略微前倾身体靠在桌面上。"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "照片级真实感",
        "粗糙纹理",
        "血液",
        "血腥",
        "污垢",
        "噪点"
      ],
      "exclude_styles": [
        "动漫",
        "赛博朋克",
        "素描",
        "恐怖",
        "水彩"
      ],
      "exclude_colors": [
        "霓虹绿",
        "亮粉红"
      ],
      "exclude_objects": [
        "智能手机",
        "现代科技",
        "汽车"
      ]
    },
    "subject2": {
      "costume": "一件闪闪发光的及地红色晚礼服，配有白色歌剧长度手套和珍珠项链。",
      "subject_expression": "带着狡黠而自信的微笑，眼睑低垂，扮演着蛇蝎美人的角色。",
      "subject_action": "优雅地用手套托着下巴，直视着侦探。"
    }
  }
}
```

</details>

<details><summary><b>午夜线人</b></summary>

```text
{
  "title": "午夜线人",
  "description": "一个紧张的黑色电影时刻，描绘一位女性私家侦探在烟雾缭绕的地下爵士俱乐部里等待线索。",
  "prompt": "你将使用所提供照片中的人物作为主要主体进行图像编辑。保留她的核心相貌特征。将该主体（女性）转变为一名机智敏锐的1950年代私家侦探，坐在一家灯光昏暗、烟雾弥漫的爵士俱乐部的卡座里。图像必须是超写实且电影级质量，唤起黑色电影黄金时代的氛围。使用戏剧性灯光突出皮肤纹理和织物细节。关键词：写实、电影级灯光、高度细节化、Arri Alexa 拍摄、景深、体积雾、真实物理效果。",
  "details": {
    "year": "1954",
    "genre": "电影级写实主义",
    "location": "丝绒音符（The Velvet Note），芝加哥一家拥挤的地下爵士酒廊，配有红色丝绒卡座，背景远处有一处朦胧的小型舞台。",
    "lighting": [
      "明暗对比（Chiaroscuro）",
      "穿透烟雾的体积光束",
      "温暖的钨丝台灯",
      "发丝轮廓光"
    ],
    "camera_angle": " eye-level medium close-up, shallow depth of field focusing strictly on the subject's eyes.",
    "emotion": [
      "怀疑",
      "警觉",
      "忧郁"
    ],
    "color_palette": [
      "深邃阴影黑",
      "琥珀金",
      "酒红",
      "烟草棕"
    ],
    "atmosphere": [
      "性感撩人",
      "神秘莫测",
      "压抑逼仄",
      "黑色电影（Noir）"
    ],
    "environmental_elements": "浓密的香烟烟雾在空中盘旋，桌上有一杯半空的琥珀色威士忌，背景中隐约可见一位低音提琴手的模糊剪影。",
    "subject1": {
      "costume": "一件结构分明的米色风衣披在深色鸡尾酒裙外，佩戴皮手套，头戴一顶宽檐软呢帽，微微前倾。",
      "subject_expression": "锐利而戒备的眼神，目光扫视着房间，双唇紧抿成一条直线。",
      "subject_action": "一只手放在桌上一个牛皮纸文件夹上，另一只手悬停在她的威士忌酒杯旁。"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "日光",
        "现代科技",
        "智能手机",
        "休闲服装",
        "明亮阳光",
        "蓝天"
      ],
      "exclude_styles": [
        "卡通",
        "3D 渲染",
        "动漫",
        "素描",
        "印象派",
        "过度饱和"
      ],
      "exclude_colors": [
        "荧光绿",
        "亮粉红",
        "青色"
      ],
      "exclude_objects": [
        "汽车",
        "出鞘的武器",
        "动物"
      ]
    }
  }
}
```

</details>

<details><summary><b>半骷髅艺术妆容人像</b> · 机器翻译</summary>

```text
一张女性肩部裸露的人像照片,背景为深色中性影棚背景。相机位于视平线高度。女子面朝镜头,呈清晰的四分之三侧面,头部从她自己的视角略微向右转,使脸部两侧精致的妆容都清晰可见。她的肩膀和脖子也在画面中。
妆容(主要焦点):

极其精致、富有艺术感的半骷髅妆,执行得非常精确。面部在垂直方向上被视觉分为两半。
脸部左侧(观者视角):华丽而美丽,搭配浓郁的紫色渐变眼影、精准的黑色眼线、非常长而浓密的假睫毛,以及线条整齐的眉毛。
脸部右侧(观者视角):带有粉紫渐变的骷髅结构。眼窝涂成粉色和紫色。眼窝、颧骨和下颌的轮廓用由闪亮的紫色小水钻或闪粉构成的纤细线条勾勒。鼻腔同样以紫色渐变突出。
嘴唇:分为两个对比鲜明的半边。一半涂哑光紫色口红,骷髅牙齿用紫色水钻勾勒轮廓。另一半涂有光泽的粉棕色口红。
发型:华丽的中长波浪发垂落在肩上。主发色与参考图完全一致,面部周围点缀着大片鲜艳的紫色发束,类似浓烈的挑染或渐变效果。头发整齐柔顺,额头上方的一缕紫色发丝形成优雅的波浪。
服装与身体:裸露的肩膀和脖子。她穿着无肩带上衣或束腰胸衣,大部分不可见。细闪粉或亮片覆盖在肩膀和脖子的皮肤上,在灯光下闪闪发光。
配饰:可见一枚小巧精致的耳钉。肩部没有可见的首饰,以便将焦点集中在妆容上。
灯光:柔和的灯光,突出妆容质感、水钻、闪粉和眼影,同时为头发增添光泽。闪粉和水钻上的高光营造出闪烁的效果。深色中性背景。
氛围与情绪:华丽、艺术、神秘、自信。一款结合恐惧与美丽的现代万圣节妆容。神秘而迷人。
不要改变参考图像中的面部特征或身份。保留确切的脸型、眼睛、鼻子、嘴唇和其他显著特征。
格式:3:4。

写实、高质量、清晰的 8K 照片,使用 iPhone 16 Pro Max 拍摄。

深色背景。
```

</details>

<details><summary><b>华丽恐怖时尚人像</b> · 机器翻译</summary>

```text
一张电影感的竖构图人像摄影作品,主角是一位二十代末的美丽年轻女性,拥有运动型沙漏身材,暖橄榄色肌肤,带有淡淡的雀斑,一头中分的深棕色长波浪发。她颧骨分明,下颌线利落,嘴唇丰满,目光强烈地直视镜头,神情严肃、自信,略带神秘感。她身穿一件短款粗针织毛衣,上面是森林绿与酒红色的宽横条纹(弗莱迪·克鲁格风格),搭配紧身黑色人造革高腰迷你裙和黑色渔网袜。她佩戴多层金色链条项链、大号金色圆环耳环和一枚戒指。她的右手叉腰、手肘向外,左手拿着一个饱经风霜的白色曲棍球面具(杰森·沃赫斯风格),面具带有污垢和血迹细节,紧贴她脸部的左侧。在柔和虚化的背景中,一个戴着白色迈克尔·迈尔斯面具、身穿深色连体工作服的男性身影站在她身后偏左的位置,半隐于阴影之中。场景是一间昏暗的卧室,两侧可见灰色凌乱的床单,墙壁为深灰色,右上角挂着一块黑色窗帘。戏剧性的低调影棚布光,以柔光箱作为主光,从正面略偏上方打光,辅助光极少,形成深邃的阴影,光线充足的主体与昏暗氛围的背景形成强烈对比。使用专业全画幅无反相机拍摄,85mm 镜头,f/2.0,平视中景竖构图,浅景深,背景人物略微虚化,对焦清晰地落在主体的脸部和眼睛上,高端电影感恐怖魅惑摄影风格,万圣节杂志大片美学,杀人狂电影偶像混搭主题,黑暗而性感的氛围,饱和的绿色与红色对比深沉的中性色调,超写实,高细节。
```

</details>

<details><summary><b>博物馆台阶全身照</b></summary>

```text
{
  "category": "MUSEUM_STEPS_FULLBODY",
  "subject": {
    "demographics": "成年女性，21–27 岁，土耳其人外貌，艺术气息。",
    "hair": {
      "color": "深棕色",
      "style": "松散波浪卷，一缕发丝别于耳后",
      "texture": "自然发丝，略带轻微飞毛"
    },
    "face": {
      "eyes": "沉思而温暖",
      "skin_details": "保留自然肤质纹理，不作柔化处理"
    },
    "clothing": {
      "outfit": "极简时尚黑色穿搭 + 轻薄外套（无任何品牌标识）",
      "fabric": "织物经纬纹理清晰可见"
    },
    "accessories": {
      "jewelry": ["银色圆环耳饰"]
    }
  },
  "pose": {
    "type": "坐姿全身像",
    "orientation": "坐在台阶上，双脚踝交叉",
    "hands": "一只手轻放于膝盖，另一只手靠近下巴",
    "gaze": "柔和眼神接触，平静从容",
    "posture": "放松而端庄"
  },
  "setting": {
    "environment": "博物馆建筑外部台阶",
    "background_elements": [
      "石材表面呈现真实孔隙与自然磨损痕迹",
      "柔和日光",
      "背景中无可读铭牌或标识"
    ],
    "depth": "主体清晰锐利，背景柔和虚化"
  },
  "camera": {
    "shot_type": "全身人像照",
    "angle": "略低角度拍摄，凸显优雅感",
    "focal_length_equivalent": "35–50mm 编辑风格镜头等效焦距",
    "framing": "4:5 构图",
    "focus": "面部与双手清晰锐利，背景柔和"
  },
  "lighting": {
    "source": "自然日光",
    "direction": "柔和前侧光",
    "shadows": "阴影柔和、真实"
  },
  "mood_and_expression": {
    "tone": "艺术感、宁静、自信",
    "expression": "浅淡微笑，眼神沉思"
  },
  "style_and_realism": {
    "style": "照片级写实风格的编辑类生活方式影像",
    "imperfections": "保留自然发丝飞毛等细节"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "极轻微噪点",
    "sharpness": "面部细节清晰锐利"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "可读文字", "品牌标识", "水印",
    "多余手指", "扭曲变形的台阶",
    "塑料质感皮肤", "CGI 渲染效果"
  ]
}
```

</details>

<details><summary><b>卧室全身镜前自拍</b></summary>

```text
一张超逼真的照片：一名25岁女性在温馨卧室中，用全身镜拍摄一张自拍照；她身穿超大号连帽衫与机车短裤；床铺凌乱；午后温暖的窗光洒入；她单手握持一部普通 iPhone 拍摄；随手手持拍摄；自动曝光；画面略带数码噪点；构图略有瑕疵；无影棚灯光；呈现日常业余 Instagram 风格；皮肤纹理自然；镜头略有污痕；色彩未经修饰
```

</details>

<details><summary><b>卧室镜前自拍图像解析</b></summary>

```text
{  
  "image_analysis": {  
    "environment": {  
      "type": "室内",  
      "location_type": "卧室或起居区",  
      "spatial_depth": "通过镜子呈现的反射景深",  
      "background_elements": "大型黑色平板电视（镜中反射）、洁净的白色墙面、深色地板或地毯"  
    },  
    "camera_specs": {  
      "lens_type": "智能手机主摄（广角）",  
      "angle": "平视高度，正对镜面的反射视角",  
      "perspective": "全身照（裁切至膝盖处）",  
      "focus": "主体身体部位清晰对焦",  
      "framing": "垂直人像构图，置于圆形镜框内"  
    },  
    "lighting": {  
      "condition": "柔和日光／窗光",  
      "sources": [  
        {  
          "source_id": 1,  
          "type": "自然窗光",  
          "direction": "来自左侧（主体右侧）",  
          "color_temperature": "冷白／中性白",  
          "intensity": "中等",  
          "effect_on_subject": "在右臂、右肩及右髋部形成柔和高光；在躯干左侧投下柔和阴影，凸显肌肉轮廓"  
        }  
      ],  
      "shadows": "柔和、弥散的阴影，勾勒出腹肌与锁骨线条"  
    },  
    "subject_analysis": {  
      "identity": "年轻女性（面部被手机遮挡）",  
      "orientation": "正对镜面",  
      "emotional_state": "自信、悦纳身体",  
      "sensuality": "中等；突出体型与健身成果",  
      "posture": {  
        "general_definition": "站立姿态，‘对立式平衡’（Contrapposto）站姿（重心落于单腿）",  
        "feet_placement": "不可见（已被裁切）",  
        "hand_placement": "左手持手机遮挡面部，右臂自然垂于身侧",  
        "visible_extent": "从头顶至大腿中部"  
      },  
      "head_details": {  
        "hair": {  
          "color": "深棕色",  
          "style": "长发、披散、略带波浪",  
          "texture": "丝滑",  
          "interaction_with_face": "垂落于双肩，衬托手机轮廓"  
        },  
        "face": {  
          "definition": "被智能手机遮挡",  
          "visible_features": "无明确可见面部特征"  
        }  
      },  
      "body_details": {  
        "body_type": "苗条／运动型／紧实",  
        "skin_tone": "白皙／苍白",  
        "neck_area": {  
          "visibility": "可见，纤细",  
          "details": "受光照影响，胸锁乳突肌轮廓清晰"  
        },  
        "shoulder_area": {  
          "shape": "方正但精致",  
          "posture": "放松"  
        },  
        "chest_area": {  
          "ratio_to_body": "比例协调",  
          "visual_estimate": "小至中等尺寸",  
          "bra_status": "穿着运动文胸／文胸背心（bralette）",  
          "nipple_visibility": "由衬垫／面料完全遮盖",  
          "shape": "自然、挺拔"  
        },  
        "midsection": {  
          "belly_button": "可见，呈纵向椭圆形",  
          "muscle_definition": "可见‘11’字形腹肌（腹白线清晰可见）",  
          "ratio_to_chest": "更窄",  
          "ratio_to_hips": "显著收窄（沙漏型轮廓）"  
        },  
        "hip_area": {  
          "ratio_to_waist": "曲线明显，宽于腰围",  
          "shape": "圆润",  
          "width": "中等"  
        },  
        "leg_area": {  
          "thighs": "光滑，可见轻微大腿间隙",  
          "knees": "不可见"  
        }  
      },  
      "attire": {  
        "upper_body": {  
          "item": "文胸背心／短款上衣（crop top）",  
          "style": "细肩带、前幅褶皱／抽褶设计、圆领",  
          "color": "深橄榄绿",  
          "fabric": "棉质或合成纤维混纺，哑光质感",  
          "fit": "紧身／贴身"  
        },  
        "lower_body": {  
          "item": "男孩短裤／热裤（boy shorts / hot pants）",  
          "style": "宽幅罗纹腰头、短裤腿",  
          "color": "深橄榄绿（同系列配套）",  
          "fabric": "罗纹针织纹理",  
          "fit": "紧身／塑形"  
        }  
      },  
      "accessories": {  
        "jewelry": "左手（持手机手）佩戴一枚简约戒指",  
        "tech": "智能手机，外壳为浅粉／蜜桃色"  
      }  
    },  
    "objects_in_scene": [  
      {  
        "object": "镜子",  
        "description": "大型圆形壁挂镜，配细黑色边框",  
        "role": "自拍照的构图框架",  
        "ratio": "主导画面构成"  
      },  
      {  
        "object": "电视机",  
        "description": "大型平板电视，黑色，处于关闭状态",  
        "position": "镜中背景反射，位于主体后方",  
        "role": "背景杂项／环境提示"  
      }  
    ],  
    "negative_prompts": [  
      "面部可见",  
      "丑陋",  
      "肥胖",  
      "病态",  
      "残缺",  
      "跨性别者（tranny）",  
      "跨性别（trans）",  
      "跨性别者（trannsexual）",  
      "插画",  
      "卡通",  
      "动漫",  
      "绘画",  
      "素描",  
      "低质量",  
      "JPEG 伪影",  
      "颗粒感",  
      "文字",  
      "水印",  
      "签名",  
      "背景杂乱",  
      "布光不佳"  
    ]  
  }  
}
```

</details>

<details><summary><b>印刷级图像优化</b> · 机器翻译</summary>

```text
增强所提供的已上传图像,提升其锐度、曝光、清晰度、质量和整体视觉冲击力,同时保留其核心设计元素。确保完成后的图像适合在专业和数字场景中展示。

你的任务是:
- 需要做好安排,以 4K 分辨率打印该图像。

你将:
- 使用高分辨率且色彩准确的技术,确保打印质量。
- 调整图像,使其更具吸引力和市场价值。

规则:
- 保持至少 300 DPI 的打印分辨率。
- 避免过于复杂的设计,以免分散对图像焦点的注意。
```

</details>

<details><summary><b>印象派都市孤独</b></summary>

```text
{
  "colors": {
    "color_temperature": "暖色",
    "contrast_level": "中等",
    "dominant_palette": [
      "棕色",
      "橙色",
      "紫色",
      "黄色",
      "灰色"
    ]
  },
  "composition": {
    "camera_angle": "平视角度",
    "depth_of_field": "中等",
    "focus": "一个穿着深色外套正在吸烟的人",
    "framing": "主体位于画面右侧偏中心位置，电车轨道形成的强烈引导线将视线引向城市景观深处。"
  },
  "description_short": "一幅印象派风格的画作，描绘黄昏时分，一人身穿深色外套站在城市电车轨道旁吸烟，远处街灯闪烁发光。",
  "environment": {
    "location_type": "城市景观",
    "setting_details": "黄昏或黎明时分的城市街道，有向远方延伸的电车轨道。街道两旁是发光的路灯，背景中可见一辆电车和其他人物。",
    "time_of_day": "傍晚",
    "weather": "晴朗"
  },
  "lighting": {
    "intensity": "中等",
    "source_direction": "混合方向",
    "type": "混合光源"
  },
  "mood": {
    "atmosphere": "孤独的城市沉思",
    "emotional_tone": "忧郁"
  },
  "narrative_elements": {
    "character_interactions": "主角独处，正在观察城市景象。虽有其他远处人物，但未描绘任何直接互动。",
    "environmental_storytelling": "暮色中的城市街道、发光的灯光和电车轨道暗示着等待或过渡的时刻，也许是工作日结束之际。该场景唤起一种城市匿名性与内省的感受。",
    "implied_action": "此人正在等待，可能是在等电车。吸烟的动作暗示在继续前行之前的一段暂停或反思时刻。"
  },
  "objects": [
    "人物",
    "大衣",
    "电车轨道",
    "路灯",
    "烟雾",
    "电车",
    "建筑物"
  ],
  "people": {
    "ages": [
      "成人"
    ],
    "clothing_style": "厚重的冬季大衣",
    "count": "1",
    "genders": [
      "男性"
    ]
  },
  "prompt": "一幅印象派风格的油画，描绘一个身穿深色厚重大衣的孤独身影，从背后视角呈现。此人站在电车轨道旁，向微凉的空气中呼出一缕烟雾。场景为黄昏时分的城市街道，天空泛着温暖的橙黄色调。远处的街灯在街道上投下柔和温暖的光芒，并映照在金属轨道上。画面采用厚重且富有质感的笔触，营造出忧郁而沉思的氛围。",
  "style": {
    "art_style": "印象派写实主义",
    "influences": [
      "写实主义",
      "印象派",
      "城市景观"
    ],
    "medium": "绘画"
  },
  "technical_tags": [
    "油画",
    "厚涂法",
    "印象派",
    "城市景观",
    "黄昏",
    "明暗对比",
    "引导线",
    "孤独",
    "质感"
  ],
  "use_case": "艺术史数据集、风格迁移模型训练、印象派绘画技法分析。",
  "uuid": "03c9a7a0-190f-4afa-bb32-1ed1c05cc818"
}
```

</details>

<details><summary><b>卷发女生镜前自拍</b></summary>

```text
{
  "image_analysis": {
    "environment": {
      "type": "室内",
      "location_type": "浴室或卧室（由镜子和水槽边缘指示）",
      "spatial_depth": "由于镜面反射造成浅景深",
      "background_elements": "灰色粉刷墙，左侧为白色门框或窗框边缘，右侧为电源插座，部分可见白色水槽"
    },
    "camera_specs": {
      "lens_type": "智能手机广角镜头（反射）",
      "angle": "与镜子相对的平视角度",
      "perspective": "自拍反射",
      "focus": "主体对焦清晰，背景反射略显柔和"
    },
    "lighting": {
      "condition": "自然日光混合室内环境光",
      "sources": [
        {
          "source_id": 1,
          "type": "自然窗光",
          "direction": "从左侧（主体的右侧）",
          "color_temperature": "冷/中性日光",
          "intensity": "中等到高",
          "effect_on_subject": "突出罗纹上衣的纹理，照亮面部轮廓和躯干，形成柔和的腰部渐变光影"
        }
      ],
      "shadows": "主体身体右侧（远离窗户一侧）以及胸部下方投下柔和阴影"
    },
    "subject_analysis": {
      "identity": "年轻女性（面部部分被头发和角度遮挡）",
      "orientation": "身体向左倾斜45度，头部转向左侧侧面",
      "emotional_state": "平静、专注、随意自信",
      "visual_appeal": "美观、健美、自然",
      "posture": {
        "general_definition": "直立站立，臀部轻微摆动",
        "feet_placement": "画面中不可见",
        "hand_placement": "左手持手机（可见），右臂垂于体侧（部分可见）",
        "visible_extent": "从头顶到上臀部/大腿"
      },
      "head_details": {
        "hair": {
          "color": "深棕色 / 浓咖啡色",
          "style": "齐肩，层次剪裁",
          "texture": "卷发 / 波浪，蓬松，凌乱时尚感",
          "interaction_with_face": "发丝垂落前额并勾勒颧骨，部分遮挡眼睛"
        },
        "ears": "被头发覆盖",
        "face": {
          "definition": "侧脸轮廓",
          "forehead": "部分被卷发覆盖",
          "eyebrows": "深色，拱形，自然粗细（部分可见）",
          "nose": "鼻梁挺直，鼻尖微翘",
          "mouth": "嘴唇放松，闭合，下唇丰满",
          "chin": "轮廓分明，柔和曲线",
          "expression": "中性，专注于镜中反射",
          "makeup": "极简或自然妆容"
        }
      },
      "body_details": {
        "body_type": "外胚型-中胚型混合（苗条但曲线明显）",
        "skin_tone": "浅橄榄色 / 白皙",
        "neck": "纤细，锁骨略可见",
        "shoulders": "窄肩，放松状态",
        "chest_area": {
          "ratio_to_body": "与纤细体型成比例",
          "visual_estimate": "中等胸部尺寸",
          "undergarment_indications": "无明显肩带痕迹；可能无内衣或无缝内衣",
          "nipple_visibility": "因面料厚度未明确显现",
          "shape_in_clothing": "紧身面料支撑下的自然泪滴形"
        },
        "midsection": {
          "belly_button": "可见，垂直方向",
          "ratio": "纤细腰身，腹肌线条清晰（可见腹白线）",
          "relation_to_chest": "明显窄于胸部（暗示沙漏型身材）",
          "relation_to_hips": "向内收窄后向外扩展至臀部"
        },
        "hips_area": {
          "ratio_to_waist": "比腰部宽",
          "visibility": "顶部曲线可见",
          "width": "中等扩张"
        }
      },
      "attire": {
        "upper_body": {
          "item": "长袖短款上衣",
          "style": "亨利领带纽扣（可见3颗，顶部未扣），罗纹针织纹理",
          "color": "浅棕色 / 灰褐色 / 摩卡色",
          "fit": "贴身 / 紧身",
          "fabric_drape": "胸部拉伸贴合，腰部紧贴，袖口至手腕"
        },
        "lower_body": {
          "item": "裤子 / 紧身裤（仅腰带）",
          "color": "炭灰色",
          "style": "低腰",
          "material": "针织或棉混纺",
          "visibility": "仅腰带和上臀部区域可见"
        },
        "accessories": {
          "hands": "左手无名指戒指（细环）",
          "wrist": "无可见饰品"
        }
      }
    },
    "objects_in_scene": [
      {
        "object": "智能手机",
        "description": "黑色外壳，多个摄像头镜头（类似 iPhone Pro 型号）",
        "function": "拍摄设备",
        "position": "左手持握，图像右侧"
    "color": "Black"
  },
  {
    "object": "Mirror",
    "description": "Reflective surface containing the entire subject",
    "function": "Medium for the selfie",
    "position": "Foreground plane"
  },
  {
    "object": "Electrical Outlet",
    "description": "Standard white wall outlet",
    "position": "Background, right side behind subject",
    "color": "White"
  },
  {
    "object": "Sink",
    "description": "White ceramic basin edge",
    "position": "Bottom right corner",
    "color": "White"
  }
],
"negative_prompts": [
  "blur",
  "noise",
  "distortion",
  "deformed hands",
  "missing fingers",
  "extra limbs",
  "bad anatomy",
  "overexposed",
  "underexposed",
  "cartoon",
  "illustration",
  "watermark",
  "text"
]
}
}
```

</details>

<details><summary><b>历史建筑研究图版</b></summary>

```text
一幅关于 ${historic_site_name} 的复古风格建筑信息图，融合艺术性与技术清晰度：画面中央为精细的正立面图，其后衬以简洁的线描风格 ${location} 风景；图中配有带标注的尺寸线，示例数值如 “${height_value_1}” 和 “${height_value_2}”。整幅作品四周环绕 2–3 个特写细节框，以及一个标有“场地平面图 – ${location}”的面板；整体采用钢笔墨线排线技法绘制于暖色调陈年纸张之上，营造出手工绘制的建筑研究图之质感。
```

</details>

<details><summary><b>厚涂油画压抑怒意肖像</b></summary>

```text
厚涂油画风格的伊朗女性肖像，粗犷的笔触，深红与赭石色。面部近乎静止，但眉头紧锁低压，双眸睁大灼灼不眨，下眼睑紧绷——怒火压抑于肌肤之下。画布底层隐约可见一个潦草手绘的矩形框，内有颤抖的手写字迹：“خفه شدم از سکوت”。
```

</details>

<details><summary><b>原理科普等距微缩模型</b></summary>

```text
创建一个清晰的、45°俯视等距微型3D教育立体模型，用于解释[PROCESS / CONCEPT]。

使用柔和精细的纹理、逼真的PBR材质以及自然柔和的灯光效果。

构建一个阶梯式或分层的立体模型底座，展示该过程的每个阶段，并用细微的箭头或路径连接。

包含小型风格化人物在每个阶段进行互动（无需面部细节）。

使用干净纯色的${background_color}背景。
在画面正上方中央，以大号粗体文字显示${process_name}，其正下方显示一段简短解释性副标题，并在其下方放置一个极简的象征性图标。

所有文字必须自动匹配背景对比度（白色或黑色）。
```

</details>

<details><summary><b>厨房晨光抓拍</b></summary>

```text
{
  "category": "KITCHEN_MORNING_WINDOWLIGHT",
  "identity_lock": {
    "enabled": true,
    "priority": "ABSOLUTE_MAX",
    "instruction": "仅以输入的参考图像作为唯一身份来源。精确保留面部结构、眼型/眼间距、鼻梁/鼻尖、唇形、下颌线、颧骨、发际线、眉毛、肤色/底色，以及所有具有辨识度的特征标记。不得进行美颜处理，不得改变种族/年龄感知。仅限成年人（21 岁及以上）。"
  },
  "subject": {
    "demographics": "成年女性，21–29 岁，土耳其外貌特征 / 地中海气质（必须与参考图像一致）。",
    "hair": {
      "color": "发色须与参考图像完全一致。",
      "style": "蓬松、略带凌乱的晨间发型；几缕发丝自然修饰脸庞。",
      "texture": "可见单根发丝、细微的飞毛、真实呈现的发根。",
      "movement": "自然垂落；发梢可有轻微动态感。"
    },
    "face": {
      "shape": "脸型须与参考图像完全一致。",
      "eyes": "眼睛形状须与参考图像完全一致；呈现自然高光；不可出现诡异锐化。",
      "lips": "唇形须与参考图像完全一致；可见自然纹理线条。",
      "skin_details": "高保真毛孔细节、晨间微妙光泽；禁止磨皮处理。",
      "micro_details": "精确保留参考图像中的斑点/雀斑/痣等所有微小特征。"
    },
    "clothing": {
      "top": "柔软宽大 T 恤或休闲背心（无任何 Logo，无文字）。",
      "fit": "宽松剪裁，略带褶皱，呈现真实垂坠感。",
      "texture": "可见棉质织纹，允许存在细微起球。"
    },
    "accessories": {
      "jewelry": ["小巧银质耳环（可选，需呈现真实反光）"]
    }
  },
  "pose": {
    "type": "自然抓拍式生活场景",
    "orientation": "半身，身体微微倚靠操作台",
    "head_position": "头部略倾斜；下巴放松",
    "hands": "一只手持马克杯；另一只手将发丝拨至耳后（双手解剖结构准确）",
    "gaze": "接近直视镜头（略偏离轴线，模拟自然抓拍瞬间）",
    "expression": "慵懒柔和的微笑，传递温馨晨间氛围"
  },
  "setting": {
    "environment": "家庭厨房",
    "background_elements": [
      "配有薄纱窗帘的窗户，柔化日光",
      "操作台上散落少许碎屑/咖啡勺（无品牌标识）",
      "绿植或水果碗（无清晰可读标签）",
      "柔和杂乱虚化（审美得体，真实可信）"
    ],
    "depth": "主体清晰锐利；背景柔和虚化，呈现自然景深层次"
  },
  "camera": {
    "shot_type": "半身人像",
    "angle": "略高于眼平线，手持拍摄",
    "focal_length_equivalent": "24–28mm 智能手机广角（业余风格） 或 35–50mm（专业风格）",
    "framing": "4:5 Instagram 信息流比例，非对称构图",
    "focus": "眼部/面部清晰锐利；肩部及背景渐次虚化",
    "perspective": "自然透视；无人脸畸变"
  },
  "lighting": {
    "source": "柔和窗边日光 + 微弱室内反射光",
    "direction": "侧前方柔和光线，轻柔勾勒颧骨轮廓",
    "highlights": "眼部、鼻梁、嘴唇呈现自然镜面高光",
    "shadows": "下颌下方与发际线处呈现柔和边缘阴影",
    "quality": "温暖、舒适、真实的晨间光线"
  },
  "mood_and_expression": {
    "tone": "温馨、私密、亲切可感",
    "expression": "柔和微笑配灵动眼神",
    "atmosphere": "未经策划的日常抓拍感"
  },
  "style_and_realism": {
    "style": "照片级写实风格社交平台生活影像",
    "fidelity": "高细节皮肤纹理与单根发丝表现；禁止任何形式平滑处理",
    "imperfections": "阴影区域允许存在轻微噪点"
  },
  "colors_and_tone": {
    "palette": "暖调中性色 + 柔和日光色调",
    "white_balance": "略偏暖的室内/日光混合白平衡",
    "contrast": "中等对比度，符合真实动态范围",
    "saturation": "自然饱和度"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "resolution": "高分辨率",
    "noise": "阴影区域含轻微真实传感器噪点（grain）",
    "mode_variants": {
      "amateur": "iPhone 抓拍感：画面略有倾斜、构图不完美、轻微噪点、面部以外区域存在细微运动模糊",
      "pro": "杂志级生活影像：曝光更干净、高光控制精准、微对比度清晰、浅景深"
    }
  },
  "constraints": {
    "adult_only": true,
    "single_subject_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true,
    "no_readable_labels": true
  },
  "negative_prompt": [
    "身份漂移", "面部变形", "美颜滤镜", "瓷肌效果", "过度平滑",
    "CGI", "卡通", "动漫",
    "多余手指", "扭曲的手部", "重复人物",
    "可读文字", "Logo", "水印"
  ]
}
```

</details>

<details><summary><b>参考图4K写实增强</b></summary>

```text
"基于所提供参考图像的超高清 4K 增强。必须完全忠实于原始面部解剖结构、比例和身份。表情、视线、姿态、相机角度、构图和透视需保持零偏差。服装、头发、皮肤和背景元素的结构、位置和设计必须保持不变。以自然真实感恢复细粒度细节。增强毛孔、细纹、发丝、睫毛、织物编织纹理、接缝和材质边缘，不引入任何风格化处理。精确保留原始色彩科学、白平衡和色调关系，与拍摄时一致。光照方向、强度、对比度和阴影行为必须与源图像完全匹配，仅提升清晰度并扩展动态范围。不得重新打光，不得重塑形体。去除所有颗粒。应用受控锐化和高频细节重建。在保留真实纹理的前提下，消除压缩伪影和噪点。不得平滑处理，不得出现塑料感皮肤，不得产生人工光泽。面部特征在整个图像中必须保持一致，解剖结构连贯，边缘清晰稳定。负面约束：不得扭曲，不得面部漂移，不得添加或缺失解剖结构，不得修改手部，不得变形，不得改变透视，不得添加文字或图形，不得幻构细节，不得进行风格化渲染。输出结果必须呈现为真实可信、照片级真实的放大图像，与参考图像完全一致，仅更清晰、更锐利、分辨率更高。"
```

</details>

<details><summary><b>参考图人像渲染</b></summary>

```text
STYLE NAME: "Sang-o-Sayeh Render"（原创风格 — 不得参照任何已知艺术风格、滤镜、动漫、Pixar、漫画或绘画传统）

SUBJECT: 精确重现参考照片中的同一男性 — 相同身份，完全可辨认：细长清瘦的脸型，轮廓分明的下颌线并带有短而深色的胡茬，深陷的深棕色眼睛呈现出平静而强烈的目光，笔直的鼻梁，短而富有纹理的黑发，自然向上蓬松，高挑纤细的体型（四肢修长，肩宽与身高的比例狭窄）。其相貌必须一眼即可识别为他本人。

RENDER LANGUAGE（原创部分）：
- 一种尚未存在的混合媒介：皮肤渲染效果类似哑光手工抛光陶瓷，表面带有微弱的雕刻状地形等高线，沿面部结构走向分布 — 非绘画感、非3D塑料感、非赛璐珞着色。
- 头发处理为雕塑式石墨纤维：单根发丝简化为5–7条方向性带状结构，带有干木炭质感的细微颗粒。
- 服装布料表现为折纸亚麻材质：外部具有锋利的折纸褶皱，但每道褶皱内部保留柔软编织纹理。
- 人物边缘带有1–2像素宽的暖铜色细线，仿佛该角色被从场景中剪下后重新插入。
- 色彩逻辑：去饱和的骨白色、深墨藏青、原始陶土色，以及唯一一处氧化铜色作为点缀。除阴影内部外无渐变，阴影本身溶解为细腻的纸张肌理而非纯黑色。
- 光照：单一不可见的顶部光源，阴影以平坦的几何形状投射，边缘略带撕裂感 — 阴影作为图形元素存在，而非光学现象。

POSE / WARDROBE（每幅图像可变）：放松的对立平衡站姿，双手自然垂放，或一只手调整袖口；现代无领立体剪裁衬衫搭配收窄西裤 — 轮廓当代化、无品牌标识、 timeless（永恒感）。

ENVIRONMENT：极致极简虚空 — 单一无缝的骨白色平面与陶土色调地面相接，仅在膝部高度设有一条细水平铜线作为唯一场景元素。别无他物。负空间占画面70%。

MOOD：安静的自信，雕塑般的静止感，博物馆展品般的存在感。

STRICT NEGATIVES：禁止写实摄影风格，禁止卡通夸张，禁止提及任何已知艺术风格名称，禁止复杂背景，禁止出现干扰主体的道具，禁止改变面部身份，禁止更改身体比例。
```

</details>

<details><summary><b>双人合成家庭肖像</b> · 机器翻译</summary>

```text
扮演一位专注于家庭肖像的数字艺术家。你的任务是将两个人合成为一幅完整的家庭肖像。

你将:
- 融合 ${person1} 和 ${person2} 的特征、表情与服装风格,但不改变他们的面部或独特的面部特征。
- 确保肖像自然、和谐。
- 使用与家庭主题相契合的背景,例如温馨的客厅或户外花园。

规则:
- 在融合风格的同时,保留每个人的独特特征。
- 不得修改或改变 ${person1} 和 ${person2} 的面部特征。
- 使用柔和、温暖的色调,营造家庭般温馨、亲切的氛围。
- 最终图像应显得专业且具有视觉吸引力。
```

</details>

<details><summary><b>双孔雀莲池蜡染图案</b> · 机器翻译</summary>

```text
一幅传统印度尼西亚蜡染纺织图案,描绘双孔雀相对而立于莲池旁,以靛蓝和奶油白两色呈现。孔雀居于画面中央,脖颈呈镜像的 S 形曲线,扇形尾羽填满点状的 isen 纹样,翅膀上点缀着小型花卉圆章。它们周围是椭圆形的莲池,池中有盛开的莲花、莲叶,以及用重复几何图案填充而成的小鱼。一道经典的蜡染边框环绕布面:交错的 kawung 与 ceplok 图形,并带有蜡防染色产生的细密裂纹。色调限定为深靛蓝、柔和的奶油色底色,以及少量淡灰蓝色晕染。线条带有手绘的不规则感,可见蜡染裂纹质感和布料织纹,平面装饰性布局,适合用于织物。无人物,无现代物品,无文字,无签名。
```

</details>

<details><summary><b>双重曝光人像</b></summary>

```text
一幅以${name:sunny forest}为背景的双重曝光人像。左侧侧脸轮廓剪影，仅呈现人物的头部与肩部。该剪影内部完全填充以森林景致，富有纵深感。在此场景深处，在自然元素之间，同一人物再次以全身形象出现，并与环境融为一体。外部背景为明亮、过曝的纯白光线。光线从剪影边缘微妙地向内晕染，营造出强烈的辉光与高对比度效果。高分辨率，电影感，柔光，真实质感，清晰细节。
```

</details>

<details><summary><b>双鹤山湖掐丝珐琅盘</b> · 机器翻译</summary>

```text
一张近距离的棚拍照片，一只圆形掐丝珐琅盘居中置于 16:9 画面中，放在深炭灰色亚麻布上。首先是主体：两只日式风格的仙鹤，白色身体、黑色脖颈、红色头冠，自左向右飞过深钴蓝色的山间湖面，每个形状都由细细的凸起金丝格框勾勒，格内填满光亮的珐琅。鸟儿身后是层叠的靛蓝与青绿色山峦、一条浅奶油色云带，以及深绿色珐琅制成的小岛松树。盘沿是连续的牡丹与菊花纹饰边框，用珊瑚红、金色和翡翠绿表现。金属工艺细节：细小的金丝格壁捕捉着高光，每个格子内的珐琅略呈弯月面，窑烧后的玻璃质表面带有柔和的镜面反射，外圈足处隐约露出铜胎。左侧柔和的侧光，亚麻布上有轻柔的接触阴影，浅景深，仙鹤最为清晰。手工珐琅器的写实产品摄影，饱和的真实珐琅色彩，宁静的博物馆工艺氛围。不是珐琅的绘画：而是实际拍摄的实物。没有文字，没有款识字母，没有水印，没有手。
```

</details>

<details><summary><b>发条蜂鸟与黄铜花</b> · 机器翻译</summary>

```text
由黄铜和珐琅制成的精巧发条蜂鸟的微距摄影,正在啜饮一朵盛开的黄铜兰花的花蜜,可见细小的齿轮和蓝宝石般的眼睛,柔和的影棚灯光,浅景深,超精细的金属质感,优雅的蒸汽朋克美学
```

</details>

<details><summary><b>变身毛绒玩偶</b></summary>

```text
将主体或图像转化为具有柔软质感和圆润形状的可爱毛绒形式。如果图像中包含人物，请保留其显著特征，以确保主体仍可被识别。否则，将物体或动物转化为使用毛毡或珊瑚绒质感的可爱毛绒玩具。应呈现温暖的毛毡或珊瑚绒外观、简洁的形状，以及精心设计的眼睛、嘴巴和面部细节。使用温馨的柔彩色或中性色系、平滑的阴影和细微的缝线，以唤起手工制作毛绒玩具的感觉。赋予其友好的、可爱的面部表情、略微 oversized 的头部、短小的四肢，以及柔软、适合拥抱的轮廓。最终图像应显得迷人、具有收藏感，宛如真正的毛绒玩具。它应显得可爱、温暖人心且令人想要拥抱，同时仍清晰保留原始主体的可识别性。
```

</details>

<details><summary><b>古罗马章鱼渔船地面马赛克</b> · 机器翻译</summary>

```text
一张宽幅、略微俯拍的照片，拍的是在一处地中海别墅遗址庭院中出土的古罗马地面马赛克，马赛克占据画面的大部分，采用 16:9 横向构图。马赛克呈现一幅生动的海洋场景，由数千块手工切割的小块石材和玻璃镶嵌片拼成：画面中央是一只大章鱼，呈赤陶红与焦橙色，卷曲的触手以深炭色镶嵌片勾勒轮廓，吸盘以奶油色点出；周围游动着带条纹的鲷鱼、一条海鳗、一只龙虾、鱿鱼，以及一只跃出水面的海豚，色调为石板灰、赭色和柔和的青绿色；画面上方有两艘挂着方帆的小木渔船，桨手画成简单的深色剪影，正在撒网，渔网在画面中弯出一道弧线；水面用成排的浅奶油色和柔和蓝灰色镶嵌片表现，排成轻柔的波浪线，顺着动物的形体走向。整幅画面由黑白相间的波浪卷纹边框和红、赭、奶油三色的辫状绞索纹带环绕。表面呈现真实的岁月痕迹：镶嵌片略有不平，几处缺损露出灰色的砂浆底层，有细微的裂纹，一个角落的颜色褪去，覆有一层薄薄的沙尘，破损的边缘长着几簇干草。低角度的温暖傍晚阳光从左侧掠过地面，使每一块镶嵌片都捕捉到光线并投下细小的阴影，一根断裂石柱的柔和影子落在一个角落上。边缘周围是风化的石灰岩铺地、一根石柱的柱础，以及几片赤陶罐碎片。考古纪实摄影，真实色彩，细节清晰，氛围宁静而永恒。不要出现人物，不要文字，不要字母，不要铭文，不要签名，不要水印。
```

</details>

<details><summary><b>可定制头像风格生成器</b></summary>

```text
充当头像定制专家。你擅长将照片转化为多种风格的个性化头像。

你的任务是：  
- 接收用户上传的照片，并据此生成头像。  
- 允许用户从多种风格中进行选择，例如卡通、写实、动漫等。  
- 提供针对发型、眼睛、配饰等特征的定制选项。

规则：  
- 确保每种风格均输出高质量结果。  
- 尊重用户的输入与隐私。

变量：  
- ${style:cartoon} —— 待生成头像的风格  
- ${photo} —— 用户上传的照片
```

</details>

<details><summary><b>可打印销售物料配图</b></summary>

```text
充当专业图像创作者。您是生成高质量、富有冲击力图像的专家，所生成图像适用于印刷与销售场景。

您的任务是：
- 创建视觉效果惊艳、可直接用于印刷的图像。
- 确保每张图像均具备销售所需的冲击力与吸引力。
- 聚焦于如下主题：${theme:product promotion}（产品推广）、${style:modern}（现代风格）。

您将：
- 采用高分辨率与色彩精准的技术，确保印刷质量。
- 量身定制图像，使其兼具吸引力与市场适销性。

规则：
- 保持印刷分辨率为至少 300 DPI。
- 避免过于复杂的设计，以免分散图像主体焦点。
```

</details>

<details><summary><b>台球酒吧参考图场景</b> · 机器翻译</summary>

```text
{
  "meta_data": {
    "task_type": "text_to_image_with_reference",
    "version": "v1.0",
    "priority": "high"
  },
  "technical_constraints": {
    "identity_preservation": {
      "enabled": true,
      "reference_mode": "strict",
      "parameters": {
        "use_reference_face_only": true,
        "identity_lock": true,
        "preserve_facial_features": true,
        "preserve_skin_texture": true,
        "avoid_face_morphing": true,
        "preservation_strength": 1
      }
    },
    "output_settings": {
      "aspect_ratio": "9:16",
      "resolution_target": "ultra_high_res",
      "render_engine_style": "photorealistic"
    }
  },
  "creative_prompt": {
    "scene": {
      "location": "光线昏暗的台球酒吧",
      "background": "深色天花板,红白相间的墙面条纹,后方有几张桌椅,低光氛围,带有细微的胶片颗粒感",
      "key_props": [
        "绿色台呢的台球桌(前景)",
        "头顶的复古红色台球灯(温暖的红色光晕)",
        "散落在球桌上的台球",
        "球杆(由主体手持)"
      ]
    },
    "subject": {
      "type": "年轻成年女性",
      "identity_instruction": "主体必须与上传的参考照片100%一致(相同的面部、比例、年龄和身份)。不得出现身份漂移。",
      "pose": "倚靠在台球桌边缘;一只手撑在桌上;另一只手竖直握着球杆;髋部微微外顶;头部微微倾斜;视线向上并看向一侧",
      "expression": "酷、自信、略带挑逗",
      "wardrobe": {
        "top": "带肩带的豹纹束腰/抹胸上衣",
        "bottom": "黑色迷你短裙",
        "accessories": "简约首饰(小圈形或耳钉款耳环)"
      },
      "details": {
        "nails": "红色指甲油",
        "hair": "长发、蓬松、波浪卷",
        "makeup": "夜场精致妆容:清晰的眼线/睫毛,暖色腮红,裸棕色唇妆"
      }
    },
    "camera_and_lighting": {
      "shot_style": "写实的夜生活闪光灯照片 + 酒吧环境光",
      "camera": "全画幅单反相机",
      "lens": "35mm 或 50mm",
      "aperture": "f/1.8",
      "shutter_speed": "1/80s",
      "iso": "800",
      "lighting": {
        "primary": "机顶闪光灯(主体清晰,自然衰减,真实的阴影)",
        "secondary": "头顶红色灯光的光晕 + 昏暗的环境补光",
        "look": "高对比度,可控的镜面高光,无过曝的白色"
      },
      "color_grading": "温暖的红色调,肤色自然,细微的胶片颗粒感",
      "focus": "眼睛和面部锐利无比,浅景深,柔和的背景虚化"
    }
  },
  "negative_prompt": [
    "不同的人",
    "身份改变",
    "面部变形",
    "多余的人物",
    "多余的肢体",
    "多余的手指",
    "糟糕的手部",
    "畸形的解剖结构",
    "扭曲的球杆",
    "扭曲的台球桌",
    "文字",
    "标志",
    "水印",
    "卡通",
    "动漫",
    "插画",
    "过度平滑的皮肤",
    "塑料感皮肤",
    "低分辨率",
    "模糊的面部",
    "闪光灯高光过曝"
  ]
}
```

</details>

<details><summary><b>各国建筑微缩场景</b></summary>

```text
“Create an isometric miniature 3D diorama representing the iconic architecture of ${country_name} through ${famous_structure}. Use a 45° top-down view.

Apply clean soft textures and realistic PBR materials.
Lighting feels balanced and natural. The raised base includes nearby streets, landscape features, and cultural details linked to the structure. Add tiny stylized locals and visitors with heavy facial details.

Background stays solid ${background_color}. Top center text shows ${country_name} in bold. Second line shows ${structure_name}. Place a minimal architecture icon below. Text color adjusts for contrast.”
```

</details>

<details><summary><b>合成波沙漠公路老爷车</b> · 机器翻译</summary>

```text
一辆空无一人的樱桃红复古敞篷车停在笔直沙漠公路的路肩上,时值日落,以复古合成波(synthwave)风格呈现。公路延伸至灭点,一轮巨大的条纹太阳半沉于地平线之下,太阳带有艳粉、橙色和黄色的条带。发光的洋红色网格线铺满沙漠地面,高大的巨柱仙人掌以深色剪影立在道路两旁。低矮的紫色群山带着霓虹青色的轮廓光,勾勒出地平线。天空从顶部的深紫罗兰色渐变为太阳附近的珊瑚色,点缀着几颗柔和的星星和细长的水平云带。镀铬保险杠和车身弯曲的尾鳍映出粉色与青绿色的反光;虚线中心线隐隐发光。干净的 1980 年代复古未来主义外观,细微的胶片颗粒和柔和的泛光,电影感宽幅构图。无人物,无文字,无标志,无车牌字符。
```

</details>

<details><summary><b>合规DALL-E绘图</b></summary>

```text
请根据下面的详细说明生成图片。如果请求涉及版权或违反内容政策的元素，请用类似但符合要求的视觉效果替代。我的详细图像描述是
```

</details>

<details><summary><b>吉卜力风格动漫角色</b></summary>

```text
一个温馨的手绘风格动漫男性角色，灵感来自柔和怀旧的日本动画。  
他有着温暖的棕色眼睛、温柔的微笑，及肩的深色微卷发，身穿浅米色柔软开衫，内搭浅色柔和的连衣裙。  
他坐在一张木制书桌前，桌上放着一本标有“Savings Plan”的笔记本，旁边是一杯小茶。  
温暖的金色夕阳透过窗户洒入，形成柔和的阴影，背景细节丰富，氛围宁静，电影级构图，高度细致，4k插画，充满温馨感，平静的情绪。
```

</details>

<details><summary><b>吸睛小册子封面设计</b> · 机器翻译</summary>

```text
创建一个专业程序,用于制作不同颜色的小册子封面,并可添加图片来补充画面,有助于吸引读者的注意力,采用高级版式分布,可选择产品名称“”简要概述 60 字* “”作者“”序列号“”的类型、颜色和字体格式,参照附带的设计,模拟出更具创意的设计,并可在上方输入数据" 我想要一个像附图那样出自独特创意的创意设计
```

</details>

<details><summary><b>吹制钴蓝花瓶的玻璃匠</b> · 机器翻译</summary>

```text
逼真的环境人像:在洒满阳光的石砌工坊里,一位中年玻璃吹制师正转动长钢吹管末端一只发光的钴蓝色花瓶。熔融的玻璃散发出橙金色的热光,照亮她专注的面庞、皮围裙、卷起的衣袖,以及推到灰白发间的有色护目镜。她身后炉口燃烧得明亮,午后的阳光从高高的拱形窗射入尘埃弥漫的空气,照亮漂浮的微粒和热浪的波动。木架上摆着琥珀色、青绿色和烟绿色的成品碗,捕捉着柔和的轮廓光。使用全画幅相机,35mm 镜头,f/2 光圈,平视角度,三分法构图,发光的花瓶位于画面左三分之一处,浅景深,冷调的窗光与暖调的炉火形成丰富的对比。纪实手工艺摄影,真实的皮肤质感,平静而虔诚的氛围,无文字,无标志。
```

</details>

<details><summary><b>咖啡馆人像提示词</b></summary>

```text
{
  "subject": {
    "description": "一位年轻、有吸引力的金发女性，头发向后梳平，编成松散的侧边辫子，右脸颊轻轻靠在手上，目光直视镜头，表情平静、自然，略带沉思。面部特征均衡且美观，皮肤清晰光滑。",
    "position": "坐在伊斯坦布尔一家咖啡馆的木桌旁，面朝镜头。",
    "pose": "头部轻靠在右手上，手肘放在桌上；左臂放松地置于桌面。",
    "expression": "平静、自然，略带沉思，目光柔和。",
    "clothing": {
      "top": "黑色细肩带背心，简约贴身款式。"
    },
    "accessories": "多个小巧的金色圈形耳环，手指上戴着细戒指，首饰极简，左手前臂内侧有一个小的手写体纹身（文字：'no pain'）。",
    "hair": "金发，整齐地向后梳理，编成一条松散的辫子垂落在左肩，带有轻微自然的碎发。",
    "skin_details": "皮肤清晰、光滑、健康，具有细微的自然质感，几乎没有瑕疵，不做重度修图。"
  },
  "scene": {
    "description": "白天的一家现代咖啡馆/酒吧内部。吧台和架子清晰可见，上面摆满了酒瓶和玻璃器皿，但空间看起来整洁，不显拥挤。",
    "location": "土耳其伊斯坦布尔的一家现代咖啡馆。",
    "setting": "室内咖啡馆，日光照明。",
    "background_elements": "架子上的酒瓶、玻璃器皿、木质纹理、透进日光的大窗户，几乎看不到或完全无人；若有人影，仅表现为模糊的轮廓，无明显特征。",
    "lighting": "柔和的自然日光从窗户照入，结合室内柔和的环境光。",
    "atmosphere": "轻松、宁静、现代都市氛围，不过于繁忙。"
  },
  "technical_details": {
    "shot_type": "中近景。",
    "perspective": " eye-level，自然手持视角，仿佛由坐在同一张桌旁的另一个人拍摄。",
    "focal_length": "智能手机广角镜头（约等效26mm）。",
    "depth_of_field": "浅景深，主体清晰对焦，背景柔和虚化，呈现自然的散景效果。",
    "composition": "主体略微偏离中心，构图平衡，包含来自架子的垂直线条和柔和的背景结构。",
    "colors": "中性与自然色调，温暖的木棕色，首饰的柔和金色，色彩平衡真实。",
    "camera_type": "iPhone 13 后置摄像头",
    "camera_behavior": "自然的智能手机图像处理，轻微边缘锐化，真实的 HDR 效果，无任何人工滤镜",
    "resolution": "标准手机照片质量，非超锐利，细节略带柔化",
    "image_characteristics": {
      "grain": "非常细微的数字噪点",
      "dynamic_range": "平衡的 HDR，高光和阴影控制得当",
      "sharpness": "适中，不过于 crisp",
      "compression": "压缩伪影极少，接近原始拍摄效果"
    }
  },
  "constraints": {
    "background_people": "避免出现清晰可见或细节明确的人物；只允许存在模糊不清的形状",
    "focus_priority": "脸部必须是最清晰的部分",
    "avoid": "背景中出现人造面孔、过度处理的皮肤、Instagram 风格滤镜、过度锐化、电影感 DSLR 视觉效果"
  }
}
```

</details>

<details><summary><b>咖啡馆窗边特写</b></summary>

```text
{
  "category": "CAFE_WINDOW_SEAT_CLOSEUP",
  "subject": {
    "demographics": "成年女性，21–27 岁，土耳其人外貌。",
    "hair": {
      "color": "深棕色",
      "style": "松散波浪卷，一缕发丝自然别于耳后",
      "texture": "单根发丝清晰可见，略带毛躁感",
      "movement": "数缕发丝自然垂落至前方"
    },
    "face": {
      "shape": "柔和的椭圆形",
      "eyes": "富有表现力、温暖，呈现自然湿润眼线细节",
      "makeup": "自然‘洁净’妆容，眼线细腻，腮红柔和",
      "skin_details": "毛孔可见，肌肤呈现自然光泽，无磨皮处理",
      "micro_details": "额头附近可见细小的绒毛"
    },
    "clothing": {
      "top": "休闲针织衫或合身T恤（无文字图案）",
      "texture": "织纹清晰可见，褶皱真实自然"
    },
    "accessories": {
      "jewelry": ["小巧银色圆环耳环"]
    }
  },
  "pose": {
    "type": "桌旁抓拍式肖像",
    "orientation": "特写／半身构图",
    "head_position": "头部微微倾斜",
    "hands": "一只手轻托下颌，手指放松且解剖结构准确",
    "gaze": "接近直视镜头，面带柔和微笑",
    "posture": "双肩放松，身体略微前倾"
  },
  "setting": {
    "environment": "靠窗的温馨咖啡馆",
    "background_elements": [
      "桌面上的陶瓷杯",
      "玻璃窗上的水汽凝结",
      "盘中细微的碎屑（体现微妙真实感）",
      "背景顾客呈虚化效果（面部不可辨识）"
    ],
    "depth": "浅景深，暖色调散景"
  },
  "camera": {
    "shot_type": "人像摄影",
    "angle": "略高于 eye level（营造随意手持拍摄感）",
    "focal_length_equivalent": "26mm 手机镜头 或 50mm 专业人像镜头",
    "framing": "4:5 构图，面部与肩部占据画面主体",
    "focus": "双眼锐利清晰，背景柔和虚化"
  },
  "lighting": {
    "source": "漫射式窗外日光 + 温暖室内环境光",
    "direction": "柔和侧光勾勒颧骨轮廓",
    "highlights": "鼻梁与嘴唇上呈现自然高光",
    "shadows": "下颌下方投下柔和阴影，对比度真实自然",
    "quality": "柔美、讨喜、温馨"
  },
  "mood_and_expression": {
    "tone": "温暖、亲切、私密",
    "expression": "柔和微笑，眼神灵动",
    "atmosphere": "强调触感的真实日常抓拍氛围"
  },
  "style_and_realism": {
    "style": "Instagram 生活方式风格的摄影写实主义",
    "fidelity": "高细节还原（睫毛、毛孔、单根发丝）",
    "imperfections": "允许存在自然噪点，白平衡可略有偏差"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "阴影区域带有轻微类手机颗粒感",
    "motion_blur": "面部无动态模糊；背景允许极微量动态模糊"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "过度平滑", "塑料质感皮肤", "诡异双眼",
    "手部畸形", "多余手指",
    "可读文字", "商标/Logo", "水印",
    "CGI", "卡通", "动漫"
  ]
}
```

</details>

<details><summary><b>品牌时尚摄影</b></summary>

```text
“生成一张电影感的低角度镜头画面，展现一位高定时尚人物置身于奢华背景之中，突出无可挑剔的街头风格与设计师品牌标识，显著体现 Gucci 的优雅气质，以及自然光泽的肤色。”
```

</details>

<details><summary><b>哥特吸血鬼镜中倒影人像</b> · 机器翻译</summary>

```text
主体与构图:一位哥特/吸血鬼风格的年轻女子坐在一面古董镜子前。照片从她身后略偏一侧拍摄(过肩视角),观者看到的是女子的背影,而她的脸和身体正面则映在镜中。

姿势:女子身体微微前倾靠近镜子。她的一只手留着黑色长指甲,正触摸着镜面玻璃,仿佛在端详自己的倒影,或与之互动。

机位与视角:中景,从身后 45 度角拍摄(过肩镜头)。镜头聚焦于镜中的倒影,营造出画面的纵深感以及神秘、窥视般的感觉。

服装与配饰:

- 黑色连衣裙或上衣,深领口、长袖。
- 脖子上戴一条黑色天鹅绒或蕾丝choker项圈。
- 又长又尖的黑色细跟鞋式美甲。

妆容:

- 锐利、轮廓分明的眼线。
- 深红/酒红色哑光口红。

发型:直发,中分略带凌乱感,自然垂落在肩头和背后。

光线:柔和、昏暗、温暖的烛光摄影。光线来自下方和侧面,形成戏剧化的阴影,让肌肤泛起温暖的金色光泽。

装饰与环境:

- 一面巴洛克/维多利亚风格的大型椭圆形镜子,带有厚重、华丽的深棕色雕花木质或金属镜框。
- 镜子旁点着滴蜡的黑色蜡烛。
- 背景中是浓郁的红/酒红色天鹅绒帷幔。
- 左下角可见骷髅或头骨的细节。

氛围与情绪:哥特、神秘、吸血鬼式、扑朔迷离又带有感性气息的氛围,具有黑暗奇幻美学,灵感来自黑暗学院/吸血鬼哥特风。

重要:不要改变参考图中的面部特征或身份。保持确切的面部结构、眼睛、鼻子、嘴唇及其他显著的面部特征。

画幅:3:4
画质:写实、高品质、锐利的 8K 照片,自然的皮肤质感,细节丰富,使用 iPhone 16 Pro 拍摄。
```

</details>

<details><summary><b>哥特红宝石颈链人像</b> · 机器翻译</summary>

```text
一幅哥特风格年轻女性的特写肖像,与视线齐平拍摄,着重表现她优雅的颈部和锁骨线条。

机位与姿势:相机位于她正前方,模特的脸转向四分之三侧面。她的头微微偏离镜头并轻轻倾斜,目光若有所思地向下并投向侧面。她的姿态放松,同时突出裸露双肩的纤细之美。

服装:女子身穿黑色紧身胸衣上衣或连衣裙,深领口,露肩。领口边缘装饰着精致的半透明黑色蕾丝。胸部中央隐约可见一处黑色系带细节。

配饰:构图的主要视觉焦点是紧贴颈部的精致哥特风项圈。项圈底部由带有花卉几何图案的黑色蕾丝制成。长短不一的细黑色金属链条系在蕾丝下缘,自由垂落。饰品正中央是一颗浓郁血红色的大椭圆形宝石,形似红宝石,镶嵌在复古的暗色金属底座中。

发型:头发在脑后挽成高高的、刻意凌乱的浪漫发髻。几缕纤细、微卷的发丝被留下来,优雅地垂落在脸颊、太阳穴和后颈旁。

妆容:哥特魅惑美学,带有淡淡的颧骨修容。眼睛以烟熏眼妆强调,使用暖调深棕色和勃艮第红眼影,营造出深邃而强烈的眼神。嘴唇涂着哑光口红,为浓郁的深红勃艮第色。

光线:主光源从正面柔和地照亮她的脸、颈部和肩膀,在锁骨和下巴下方形成优美的阴影。背景中,温暖的琥珀橙色轮廓光将模特与背景分离开来。

氛围与背景:深色神秘的背景,带有强烈的虚化效果和深邃的焦外光斑。右侧可见模糊的暖色灯光,如同摇曳的烛光。

情绪:暗黑浪漫、神秘主义、吸血鬼美学、神秘感、优雅的忧郁。画面传达出一种平静而危险的魅力。

不要改变面部特征或身份。

3:4画幅。
写实、高质量、清晰的8K照片,使用iPhone 16 Pro拍摄。
```

</details>

<details><summary><b>哥特蕾丝红光环人像</b> · 机器翻译</summary>

```text
整体构图与镜头角度:

电影感的四分之三侧面肖像,一名女子背对镜头而坐,回眸望向肩后。以略微低角度拍摄,突出戏剧化的构图和优雅的身体线条。

主体与姿势:

- 身体姿态:背部呈优雅而戏剧化的 S 形曲线,下背部有轻柔的弧度,从肩膀到臀部过渡流畅。
- 手臂位置:她的左臂完全伸展并搭在地面上,形成一条通向画面中心的斜线。另一只手臂藏在身后。
- 面部与视线:她向右转头,露出侧脸,回眸望向肩后,神情平静而神秘。

服装与风格:

- 连衣裙:一件奢华的白色蕾丝束身连衣裙或连体衣,复古哥特风格。
- 束身衣细节:深开的背部,配有精致的黑色交叉系带,与白色蕾丝形成美丽的对比,并露出肌肤。修长精致的蕾丝袖子完善了整体造型。

发型与妆容:

- 发型:极长、蓬松、卷曲的头发,从背后和一侧肩膀垂落至腰部或臀部。头发显得浓密、柔软、飘逸,与精致的蕾丝形成美丽的质感对比。
- 妆容:优雅的哥特式妆容,突出面部轮廓,浓郁的深红色经典口红,眉形锐利分明

光线与氛围:

- 灯光风格:戏剧化的高对比度影棚灯光。
- 红色光晕效果:头部上方和后方强烈的红色背光营造出火焰般的光晕,照亮长发的边缘。红光在她的肩膀和面部轮廓上微微反射。
- 主光:柔和的冷色调光线照亮她的身体和裙子,突出精致的蕾丝质感和束身衣系带。背景保持完全的深黑色。

情绪与环境:

- 情绪:神秘、性感、优雅、哥特且忧郁。
- 地面:完全黑色的哑光地面,没有地毯、毛皮、羽毛、白色绒毛或装饰元素。表面朴素、深色、无缝,自然地融入黑色背景。
- 氛围:神秘、近乎玄幻的夜间影棚场景,带有戏剧化的红色照明、深邃的阴影和奢华的暗黑浪漫美学。

面部保留:完全保留参考照片中的面部特征、身份、面部结构和比例。不要改变或重塑她的脸。

画质:超写实、锐利的 8K 摄影,具有细腻的蕾丝质感、真实的皮肤、自然的发丝和电影感光线。

画面比例:竖幅 3:4。
```

</details>

<details><summary><b>哥特魅影夜景人像</b> · 机器翻译</summary>

```text
一位哥特魅惑(Goth Glam)风格的女子,以 3:4 竖幅拍摄,带有夜间摄影效果。
姿势与身体曲线:

女子站立着,随意地将背靠在一棵粗大的树干上。她的身体形成优雅柔和的 S 形曲线。她的头微微向下并偏向一侧,低垂的目光带着忧郁,营造出神秘而疏离的氛围。她的左手优雅地搭在臀部,轻触裙子的面料,右臂自然松弛地垂在身侧。她的右腿略向前伸,微妙地强调出臀线。
外貌、妆容与发型:

发型:浓密的披肩发,中分,自由地垂落在肩上和背后。

妆容:以强烈对比为基调。肤色完美均匀,并以浓郁的深红/酒红色哑光口红加以强调。眼部以淡淡的深色妆容和细眼线勾勒,颧骨轻轻修容。

细节:亮黑色美甲。
服装与配饰:

她穿着黑色露肩哥特束腰上衣。心形领口装饰着精致的黑色蕾丝,中央有一个小小的缎面蝴蝶结。袖子由半透明黑色网纱制成,宽松地贴合手臂,末端是宽大的荷叶边。服装下半部分是蓬松的黑色轻质面料半身裙,下面隐约可见黑色半透明尼龙连裤袜。唯一的配饰是一条细银链,配有极简的深色吊坠。
灯光、相机角度与氛围:

灯光:在一片漆黑中,强烈的直射闪光灯正对主体,营造出夜间 iPhone 闪光灯拍摄的效果。这产生了最大的对比:女子被明亮照亮,而背景完全沉入黑暗。
相机角度:正面视角,相机大约位于胸部高度。经典的中全景,取景到膝盖。
氛围与背景:

神秘、浪漫、略带阴郁的暗黑浪漫(Dark Romance)美学。背景中仅被闪光灯照亮的是树皮的质感和几根细细的光秃树枝,逐渐隐没在夜晚森林或公园的绝对黑暗中。
不要改变参考图像中的面部特征或身份。保留确切的面部、面部结构、眼睛、鼻子、嘴唇和其他显著特征。
格式:3:4。

写实、高质量、清晰的 8K 照片,使用 iPhone 16 Pro 拍摄。
```

</details>

<details><summary><b>哭泣女人开场场景</b> · 机器翻译</summary>

```text
帮我生成这个场景。场景 1.1:⁠夜晚一条黑暗、孤寂的乡间土路,两旁是扭曲、多节的树木,苍白的月光下有一条浑浊的河。浓雾贴近地面飘浮,电影感打光,阴森的氛围,黑暗恐怖电影风格,高细节,8k --ar
```

</details>

<details><summary><b>唯美日落</b></summary>

```text
8K 超高清美学，浪漫，日落，黄金时刻光线，温暖的电影色调，柔和辉光，舒适的冬日氛围，自然真实的感情，浅景深，胶片质感，高细节
```

</details>

<details><summary><b>喀斯特云雾空舟水墨画</b> · 机器翻译</summary>

```text
薄雾笼罩的石灰岩喀斯特山峰耸立在平静的河面之上，一艘空无一人的木质舢板停泊在芦苇丛中，以传统中国水墨山水画的形式绘于宣纸上。高耸圆润的山峰隐没在层层叠叠的薄雾里，从前景的浓墨渐变为远处淡灰的剪影。一棵虬曲的松树紧贴最近的悬崖，松针以迅疾的枯笔画出。带有弧形编织篷顶的小舢板停靠在左下方岸边，在静止的水面上留下淡淡的倒影。天空与河面留出大片空白的纸面，湿墨相接之处有柔和的墨晕晕开，远处有几只鸟，如细小的笔触轻轻一挑。黑灰单色水墨，仅在船篷上点一抹淡淡的暖赭色。可见宣纸纤维质感，宽幅横向手卷构图，画面边到边铺满整个画幅，宁静沉思的氛围。无人物，无文字，无书法，无印章，无落款。
```

</details>

<details><summary><b>喜马拉雅寺院图生视频</b> · 机器翻译</summary>

```text
以第 2 步的图像 "Cliffside Himalayan Monastery with Prayer Flags at Misty Dawn" 作为精确的首帧,将其制作成一段平静的、时长 ${duration:6} 秒的电影感镜头。左侧山崖上的寺院建筑、右侧的岩石尖塔、每一串经幡的系点、河流、峡谷、雪峰和取景都要与图像完全一致。经幡在从左向右吹的微风中持续飘动、起伏,始终系在各自的绳串上。峡谷中的白色雾带从左向右缓缓飘移,在若干处轻轻变薄,多露出一点青绿色的河流。屋顶香炉升起的细细香烟随风向同一方向柔和地上升并弯曲。金色的光线缓缓增强,洒在白墙、金色屋顶装饰和雪峰上。镜头朝寺院做一次非常缓慢、平稳的推进。自然、写实的运动,无剪辑,无新物体,无人物,无文字。
```

</details>

<details><summary><b>喜马拉雅悬崖寺院场景简报</b> · 机器翻译</summary>

```text
扮演一名电影级环境设计师,撰写可直接用于图像生成和动态生成的场景简报。请帮我设计一个英雄镜头:一座悬挂在山崖上、挂着串串经幡的小型寺院。这个镜头会先生成静态图像,再以该图像为首帧制作成一段短视频。你的简报必须让静态图像中包含丰富的、可以自然运动的元素(飘动的经幡、飘移的云雾、升起的香烟、远在下方的瀑布或河流、变化的光线、几只远处的飞鸟),同时保持构图平静、便于做动画。

我的初始选择:
- 山地环境:${setting:Himalayan gorge with a river far below and snow peaks behind}
- 时间与天气:${time:misty dawn after a clear night}
- 寺院外观:${monastery:small whitewashed buildings with red-brown upper walls, dark roofs, and gold roof ornaments}
- 视觉风格:${style:photoreal travel and landscape photography}
- 氛围关键词:${mood:serene, airy, sacred, quiet}

请先用一条简短的消息向我询问缺失的信息:我偏好的相机视角(从峡谷对面的山脊上、从下方小径仰望、或从与寺院齐平的岩台上)、河流和峡谷谷底应露出多少,以及需要避免的内容(人物、僧侣、游客、标牌、现代建筑、缆线、某座真实存在的寺院)。

然后按以下部分撰写简报:

1. **场景概述**:两三句话,描述地点、时间、光线和这一刻的感受。描述的是一座想象中的寺院,而不是照搬某座有名字的真实寺院。

2. **寺院与山崖**:建筑数量及其在山崖岩台上的布局、墙面颜色、窗户排列、屋顶和金色装饰、台阶或木桥、建筑如何坐落在岩石上、山崖的质感与植被(刺柏、松树、苔藓),以及寺院在画面中的位置。

3. **经幡**:共有几串、每串系在哪里(屋顶、岩石尖塔、旗杆)、在画面中延伸的方向、颜色顺序(蓝、白、红、绿、黄)、大小,以及下垂的程度。注明经幡随风飘动,但其系点绝不移动。

4. **峡谷与景观**:远在下方的河流或瀑布、森林覆盖的山坡、侧面山脊、雪峰,以及从前景到背景的景深层次。

5. **光线与氛围**:太阳的方向和颜色、峡谷中的雾带及其高度、山峰周围的云丝、屋顶香炉升起的香烟,以及光线如何照在白墙和金色装饰上。

6. **固定视觉细节**:一份编号列表,列出 8 到 10 个必须在静态图像和视频中保持一致的细节(寺院所在一侧与位置、建筑数量、经幡系点与方向、河流位置、山峰形状、太阳所在一侧、雾的高度、相机位置、取景)。

7. **运动图**:一张表格,列出视频中所有可以运动的元素,列为:元素、运动类型、方向、速度(极慢、慢、中等)、运动幅度。包括相机运动。保持整体运动细微且符合物理规律,经幡、雾和烟使用同一个风向。

8. **提示词种子 A - 英雄静态图像**:一条可直接粘贴使用的图像提示词,不超过 170 个单词,用于 16:9 宽幅横向画面,第一句话中包含寺院、山崖、经幡和峡谷,结尾为:no people, no text, no signs, no logos。

9. **提示词种子 B - 图生视频动画**:一条可直接粘贴使用的视频提示词,不超过 120 个单词,以英雄静态图为首帧,描述约 6 秒内一个缓慢的相机运动以及运动图中的自然运动,并说明寺院、山崖、经幡系点、群山和取景要与图像完全一致,不得出现新物体。

规则:不以人物作为主体,不出现文字、标牌或标志,不使用快速的相机运动或剪辑,不出现违背物理规律的运动(经幡会飘动和起伏但始终保持系着,雾和烟与经幡随同一股风飘移,水往低处流)。使用简短的段落和列表。
```

</details>

<details><summary><b>困在史前丛林的维多利亚时空旅人</b></summary>

```text
你将使用所提供照片中的人物作为主要主体，执行一次图像编辑。须保留其核心相貌特征。画面描绘了主体1——一位困顿不堪的维多利亚时代时间旅行者——正站在浓密、雾气弥漫的史前丛林中，检查一枚结构复杂的黄铜计时器。图像必须达到超写实摄影级别，且细节极为丰富，精准呈现磨损丝绒的纹理、沁出汗水的皮肤以及湿漉漉的热带叶片。采用电影级布光：斑驳的阳光穿透林冠，在主体身上投下光影；整体风格仿照高预算电影，以 ARRI Alexa 摄影机拍摄，景深极浅。  

{
  "prompt": "你将使用所提供照片中的人物作为主要主体，执行一次图像编辑。须保留其核心相貌特征。画面描绘了主体1——一位困顿不堪的维多利亚时代时间旅行者——正站在浓密、雾气弥漫的史前丛林中，检查一枚结构复杂的黄铜计时器。图像必须达到超写实摄影级别，且细节极为丰富，精准呈现磨损丝绒的纹理、沁出汗水的皮肤以及湿漉漉的热带叶片。采用电影级布光：斑驳的阳光穿透林冠，在主体身上投下光影；整体风格仿照高预算电影，以 ARRI Alexa 摄影机拍摄，景深极浅。",
  "details": {
    "year": "白垩纪晚期（经由1890年抵达）",
    "genre": "电影级写实主义",
    "location": "一片浓密潮湿的丛林地面，遍布巨型蕨类与远古苏铁。",
    "lighting": [
      "透过林冠洒落的斑驳阳光",
      "大气体积雾效",
      "高对比度阴影"
    ],
    "camera_angle": "平视特写镜头，焦点集中于面部与手持装置。",
    "emotion": [
      "恐慌",
      "紧迫感",
      "难以置信"
    ],
    "color_palette": [
      "深翠绿色",
      "泥泞棕褐色",
      "黯淡黄铜金色",
      "浓郁酒红色"
    ],
    "atmosphere": [
      "潮湿",
      "危险",
      "令人窒息",
      "酷热难耐"
    ],
    "environmental_elements": "巨型蕨类羽状叶、悬浮的史前昆虫、潮湿地面升腾的水汽、背景中一个模糊的巨大轮廓正在移动。",
    "subject1": {
      "costume": "一套撕裂且沾满泥浆的维多利亚时代三件套丝绒西装，一条松垮的领巾，颈部挂着一副黄铜蒸汽朋克护目镜。",
      "subject_expression": "双眼圆睁、绝望惊惶，额头上渗出细密汗珠。",
      "subject_action": "双手急切地敲击手中一枚发光冒烟的黄铜计时器玻璃表盘。"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "现代建筑",
        "铺装道路",
        "电子手表",
        "运动鞋",
        "塑料"
      ],
      "exclude_styles": [
        "卡通",
        "素描",
        "油画",
        "动漫",
        "低分辨率"
      ],
      "exclude_colors": [
        "霓虹蓝",
        "荧光粉"
      ],
      "exclude_objects": [
        "汽车",
        "现代武器"
      ]
    }
  }
}
```

</details>

<details><summary><b>图像画质修复增强</b> · 机器翻译</summary>

```text
超写实图像修复与增强。将上传的模糊/低质量图像修复为清晰、干净、高细节的照片级效果,同时完全保留原图。

100% 保留身份、面部结构、年龄、肤色、表情、视线、头发、胡须、牙齿、姿势、身体比例、服装、配饰、背景、取景、相机角度、光线方向和构图。

不要重新设计、美化、风格化、替换、移除、添加、重新诠释,或让人物看起来不同。不要凭空创造人工特征、虚假细节、过于完美的皮肤、带有 AI 感的纹理或合成感。
只提升技术质量:自然的锐度、清晰度、逼真的面部/纹理细节、皮肤毛孔、发丝、眼睛、嘴唇、服装质感、减少像素化、对比度、层次感、动态范围以及光线平衡,且不改变原有的氛围。

仅限照片级真实。不要美颜滤镜、塑料感皮肤、过度锐化、夸张的 HDR 或虚假细节。

保持一切完全不变。只提升图像质量。
```

</details>

<details><summary><b>图像画质增强</b></summary>

```text
充当高级图像质量增强工具。你的任务是将上传的图像质量提升至 Full HD 分辨率，并应用锐化技术，同时不改变任何原始细节。你将：
- 使用高级算法将分辨率提升至 Full HD。
- 应用锐化技术以提高图像清晰度。
- 保持原始图像的完整性。
- 确保增强后的图像除清晰度和分辨率提升外，保留所有原始细节。
```

</details>
