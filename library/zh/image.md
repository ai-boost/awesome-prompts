# 图像与设计 (1/3)

共 453 条。复制后把方括号里的内容换成你的，粘贴进任意对话模型即可。

[English](../en/image.md) · [中文](../zh/image.md) · [在线搜索复制](https://agentcraft.dev/zh/prompts/image/)

分页：**1** · [2](image-2.md) · [3](image-3.md)

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

<details><summary><b>ChatGPT 生成 Midjourney 咒语</b></summary>

```text
staring up into the infinite celestial library, endless {{item_2}}, flying {{item_1}}, {{adjective_1}}, sublime, cinematic lighting, watercolor, mc escher, dark souls, bloodborne, matte painting

This is only an example, come up with new ideas, art styles, etc.

So this is the Dynamic Prompt Format.

I want you to write the perfect dynamic prompt for me to query Midjourney with one message, and include some dynamic variables where you see fit.You may use the following guide to help you: Midjourney Rules (this was too long to add to the post)

Write a detailed dynamic prompt for "IMAGE_IDEA"
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

<details><summary><b>Midjourney 提示词生成器</b></summary>

```text
我要你充当 Midjourney 人工智能程序的提示词生成器。你的任务是提供细致且富有创意的描述，以激发 AI 生成独特而有趣的图像。请记住，该 AI 能够理解广泛的语言，并能诠释抽象概念，因此请尽可能发挥想象力，尽可能详尽地进行描述。例如，你可以描述一座未来主义城市的场景，或一片充满奇异生物的超现实景观。你的描述越细致、越富想象力，最终生成的图像就越有趣。以下是你的第一个提示词：“一片野花田绵延至视野尽头，每一朵花都拥有不同的颜色与形状。远处，一棵巨树巍然矗立于 landscape 之上，其枝干如触手般向上伸展，直指天空。”
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

<details><summary><b>SVG 设计师</b></summary>

```text
我希望你充当一名 SVG 设计师。我将要求你创建图像，而你将为此图像编写 SVG 代码，再将该代码转换为 base64 数据 URL，最后向我返回一个仅包含指向该数据 URL 的 Markdown 图像标签的响应。请勿将 Markdown 放入代码块中。仅发送 Markdown，不附加任何文字。我的第一个请求是：给我一张红色圆形的图像。
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

<details><summary><b>前卫幽灵分身人像</b></summary>

```text
一幅超写实 8K 电影级影棚肖像，构图自人物中腿部以上，呈现一位自信伫立于浓烈赭红色背景前的人物。主体身穿一件 oversized、肌理感极强的轰炸机夹克，夹克表面采用混搭抽象拼布图案，色调融合低饱和与高饱和的红、蓝、绿及米褐色；下装为宽松的土橄榄色工装裤，内搭白色 T 恤。布光为强烈正面光，投下清晰锐利的阴影，并凸显织物纹理。画面中一个标志性的艺术元素是：主体后方偏右位置，叠加一个半透明、带有运动模糊效果的幽灵分身，该分身呈水平方向疾速掠过，拖曳出缤纷色带，暗示高速运动或时间扭曲。背景保持统一，但带有微妙渐变，营造景深而不喧宾夺主。成片采用高端时尚杂志编辑风格拍摄：主体人物焦点锐利，景深极浅，影棚写实细节精准，整体传递出大胆、实验性、前卫的艺术氛围。
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

<details><summary><b>双重曝光人像</b></summary>

```text
一幅以${name:sunny forest}为背景的双重曝光人像。左侧侧脸轮廓剪影，仅呈现人物的头部与肩部。该剪影内部完全填充以森林景致，富有纵深感。在此场景深处，在自然元素之间，同一人物再次以全身形象出现，并与环境融为一体。外部背景为明亮、过曝的纯白光线。光线从剪影边缘微妙地向内晕染，营造出强烈的辉光与高对比度效果。高分辨率，电影感，柔光，真实质感，清晰细节。
```

</details>

<details><summary><b>变身毛绒玩偶</b></summary>

```text
将主体或图像转化为具有柔软质感和圆润形状的可爱毛绒形式。如果图像中包含人物，请保留其显著特征，以确保主体仍可被识别。否则，将物体或动物转化为使用毛毡或珊瑚绒质感的可爱毛绒玩具。应呈现温暖的毛毡或珊瑚绒外观、简洁的形状，以及精心设计的眼睛、嘴巴和面部细节。使用温馨的柔彩色或中性色系、平滑的阴影和细微的缝线，以唤起手工制作毛绒玩具的感觉。赋予其友好的、可爱的面部表情、略微 oversized 的头部、短小的四肢，以及柔软、适合拥抱的轮廓。最终图像应显得迷人、具有收藏感，宛如真正的毛绒玩具。它应显得可爱、温暖人心且令人想要拥抱，同时仍清晰保留原始主体的可识别性。
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

<details><summary><b>各国建筑微缩场景</b></summary>

```text
“Create an isometric miniature 3D diorama representing the iconic architecture of ${country_name} through ${famous_structure}. Use a 45° top-down view.

Apply clean soft textures and realistic PBR materials.
Lighting feels balanced and natural. The raised base includes nearby streets, landscape features, and cultural details linked to the structure. Add tiny stylized locals and visitors with heavy facial details.

Background stays solid ${background_color}. Top center text shows ${country_name} in bold. Second line shows ${structure_name}. Place a minimal architecture icon below. Text color adjusts for contrast.”
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

<details><summary><b>唯美日落</b></summary>

```text
8K 超高清美学，浪漫，日落，黄金时刻光线，温暖的电影色调，柔和辉光，舒适的冬日氛围，自然真实的感情，浅景深，胶片质感，高细节
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

<details><summary><b>图像画质增强</b></summary>

```text
充当高级图像质量增强工具。你的任务是将上传的图像质量提升至 Full HD 分辨率，并应用锐化技术，同时不改变任何原始细节。你将：
- 使用高级算法将分辨率提升至 Full HD。
- 应用锐化技术以提高图像清晰度。
- 保持原始图像的完整性。
- 确保增强后的图像除清晰度和分辨率提升外，保留所有原始细节。
```

</details>

<details><summary><b>图像转 JSON 分析报告</b></summary>

```text
{
  "meta": {
    "source_image": "user_provided_image",
    "analysis_timestamp": "2024-07-30T12:00:00Z",
    "analysis_model": "image_to_json_v1.0",
    "overall_confidence": 0.99
  },
  "camera_and_exif": {
    "camera_make": "unknown",
    "camera_model": "unknown",
    "lens_model": "unknown",
    "focal_length_mm": 50,
    "aperture_f_stop": 11.0,
    "shutter_speed_s": 0.004,
    "iso_value": 1600,
    "white_balance_mode": "n/a (monochrome)",
    "exposure_compensation_ev": 0,
    "orientation": "portrait",
    "resolution_px": "800x995",
    "color_profile": "grayscale"
  },
  "scene_environment": {
    "scene_type": "outdoor, open area, temporary event setup",
    "time_of_day": "daytime",
    "season": "unknown",
    "weather_conditions": "overcast, diffused light",
    "temperature_appearance": "neutral, slightly cool",
    "environment_distance_depth": {
      "foreground_depth_m": 2.0,
      "midground_depth_m": 15,
      "background_depth_m": 60
    },
    "environment_description": "large, empty, open-air paved area or auditorium floor with hundreds of dark folding chairs arranged in irregular rows, under even, diffused daylight. A solitary figure is seated in the foreground, facing the chairs.",
    "ground_material": "rough concrete or asphalt",
    "ambient_objects": [
      {
        "id": "env_obj_chair_array",
        "type": "folding chairs (hundreds)",
        "position_relative_to_subject": "in front, distant to far-distant",
        "approx_distance_m": 5.0,
        "height_m": 0.8,
        "width_m": 0.45,
        "material": "metal frame, dark plastic/vinyl seat and back",
        "color_dominant": "#4A4A4A",
        "texture": "smooth seat/back, metallic frame, slight sheen",
        "occlusion": "partial due to overlapping rows from high angle perspective"
      }
    ],
    "air_properties": {
      "humidity_estimate": 0.6,
      "haze_level": 0.15,
      "fog_density": 0.0,
      "color_tint": "n/a (monochrome)"
    }
  },
  "spatial_geometry_and_distances": {
    "camera_position": {
      "x_m": 0,
      "y_m": 25.0,
      "z_m": -8.0
    },
    "camera_angle_degrees": {
      "pitch": -75,
      "yaw": 0,
      "roll": 0
    },
    "subject_to_camera_distance_m": 26.2,
    "object_to_object_distances": [
      {
        "object_a": "subject_01",
        "object_b": "env_obj_chair_array_nearest_row",
        "distance_m": 5.0
      },
      {
        "object_a": "subject_01",
        "object_b": "env_obj_chair_array_furthest_row",
        "distance_m": 60.0
      }
    ],
    "height_reference_scale": {
      "known_reference": "person",
      "height_m": 1.75,
      "pixel_to_meter_ratio": 0.0109
    }
  },
  "subjects_and_anatomy": {
    "people_detected": 1,
    "subjects": [
      {
        "id": "subject_01",
        "category": "human",
        "age_estimate": 40,
        "gender_appearance": "male",
        "body_posture": "seated, back to camera, looking forward",
        "height_estimate_m": 1.75,
        "shoulder_width_m": 0.48,
        "body_proportions": {
          "head_height_ratio": 0.125,
          "torso_to_leg_ratio": 0.5
        },
        "facial_structure": {
          "face_shape": "unknown",
          "jawline_definition": "unknown",
          "skin_tone": "n/a (monochrome)",
          "facial_expression": "unknown",
          "eye_color": "unknown",
          "hair_color": "dark",
          "hair_style": "short, neatly combed",
          "facial_feature_asymmetry": "unknown"
        },
        "position_in_scene": {
          "relative_position": "bottom-center frame",
          "depth_layer": "foreground-midground transition",
          "ground_contact": "seated on chair, chair legs on ground",
          "orientation_to_camera": "180 degrees rotated away from camera (back to camera)"
        },
        "clothing": [
          {
            "item": "suit jacket",
            "color": "#1A1A1A",
            "material": "wool blend",
            "fit": "tailored",
            "pattern": "plain",
            "texture": "smooth matte"
          },
          {
            "item": "trousers",
            "color": "#1A1A1A",
            "material": "wool blend",
            "fit": "tailored",
            "pattern": "plain",
            "texture": "smooth matte"
          },
          {
            "item": "chair",
            "color": "#333333",
            "material": "metal frame, dark plastic/vinyl seat",
            "fit": "standard folding chair",
            "pattern": "none",
            "texture": "smooth seat, metallic frame"
          }
        ]
      }
    ]
  },
  "lighting_analysis": {
    "main_light_source": {
      "type": "natural diffused light",
      "direction": "overhead, omnidirectional",
      "intensity_lux": 8000,
      "softness": "extremely soft",
      "color_temp_k": "n/a (monochrome)"
    },
    "secondary_lights": [],
    "shadow_properties": {
      "present": true,
      "softness": "very soft, barely perceptible"
    "direction_degrees": 180,
    "tint_color": "n/a (monochrome)"
  },
  "reflections": {
    "present": false
  },
  "mood_descriptor": "庄重、孤立、期待、广阔、极简主义、沉思"
},
"color_texture_and_style": {
  "dominant_palette": [
    "#E6E6E6",
    "#CCCCCC",
    "#AAAAAA",
    "#4A4A4A",
    "#1A1A1A"
  ],
  "palette_description": "单色配色方案，深黑色与亮白色之间具有高对比度，并辅以广泛的中灰色调。整体印象鲜明且具图形感。",
  "saturation_level": "n/a (monochrome)",
  "contrast_level": "高",
  "color_temperature_description": "n/a (monochrome)",
  "texture_map": "整个图像中可见高频颗粒/噪点",
  "grain_quality": "细腻、清晰、胶片质感",
  "microtexture": "地面有明显粗糙感，西装上有细微织物纹理，椅子表面光滑",
  "tone_balance": "强烈的黑色、明亮的白色以及丰富的中间色调，赋予图像一种图形化、近乎抽象的特质。"
},
"composition_and_geometry": {
  "rule_of_thirds_alignment": false,
  "symmetry_type": "非对称平衡，底部中央的人物与上方庞大、重复、半对称的椅子图案形成对比",
  "leading_lines_present": true,
  "framing_description": "高角度俯拍镜头，孤独的主体位于画面底部中央，向上凝视着似乎无尽的空椅子阵列，这些椅子占据了图像上三分之二的空间。该构图强调了尺度感、孤立感和期待感。",
  "depth_layers": [
    "前景（主体前方的空地）",
    "中景（主体及最近的椅子）",
    "背景（远处成排的椅子，逐渐融入大气透视）"
  ],
  "perspective_type": "高角度正交视角，带有轻微线性透视以表现深度",
  "depth_of_field_strength": "景深大，从前景到背景的所有元素均清晰对焦。"
},
"environmental_relationships": {
  "subject_environment_interaction": {
    "stance": "主体坐在一把椅子上，位于画面底部中央，面向前方那片广阔而寂静的空椅子群。",
    "shadow_cast_on": "主体和椅子正下方的地面上，非常微弱且弥散。",
    "proximity_to_objects": [
      {
        "object_id": "env_obj_chair_array_nearest_row",
        "distance_m": 5.0,
        "interaction_type": "视觉对峙、象征性观众、焦点所在"
      }
    ],
    "environmental_scale_perception": "个体主体在庞大重复的空椅子图案面前显得渺小而孤立，营造出强烈的尺度感和潜在的重要性。"
  },
  "acoustic_environment_estimate": "寂静、空旷，若在室内或大型开放空间中可能带有回声，突出安静的沉思或期待氛围。",
  "temperature_feel": "由于材质（混凝土、金属）和弥散光线的影响，体感温度为微凉至凉爽，中性。"
},
"output_and_generation_parameters": {
  "target_similarity": 0.99,
  "schema_completeness": "保留所有部分，缺失数据标记为 'unknown' 或 'n/a'",
  "color_fidelity": "黑白表现中的色调准确性为高优先级",
  "distance_precision_m": 0.5,
  "pose_accuracy": 0.05,
  "facial_geometry_precision": 0.002
},
"privacy_and_safety": {
  "face_blurring": false,
  "pii_detected": false,
  "notes": "由于主体朝向（背对相机）以及图像本身的性质，未见可识别的面部特征或个人信息。"
}
```

</details>

<details><summary><b>图片风格模仿</b></summary>

```text
上传您的图像，通过模仿指定风格对其进行转换。该图像将被调整以匹配所选的美学风格，例如：

- **风格选项：** 复古棕褐色、现代抽象、水彩画等。
- **调整项：** 色彩方案、纹理、对比度及其他视觉元素，以实现期望的外观。

请明确指定您希望模仿的风格，以获得最佳效果。
```

</details>

<details><summary><b>土耳其模特美妆分析板</b></summary>

```text
{
  "prompt": "一张极简主义时尚杂志风格的美容分析图，主角为一位土耳其女性模特，脸型为均衡的椭圆至心形，下颌线柔和清晰。具有微妙的地中海–安纳托利亚面部特征。中性灰色背景，干净的影棚灯光，高度写实。\n\n顶部区域：正面无妆容肖像，呈现自然的皮肤质感并略带暖色调，未化妆，头发向后梳理，表情中性。一条细蓝色轮廓线勾勒出脸型。\n\n右侧图文布局标题为 'FACE'，包含描述面部特征的小型项目符号列表：均衡的椭圆脸型、柔和突出的颧骨、女性化的下颌线、略微尖锐但自然的下巴、笔直到微微拱起的鼻梁、富有表现力的杏仁形眼睛。\n\n中部区域：两张标注为 'barefaced'（无妆）的影棚肖像，一张正面视角，一张四分之三侧面视角，造型极简，柔光漫射照明，呈现逼真的皮肤细节。\n\n底部区域：两张以“带妆”为标签的镜像自拍风格图像，肌肤光泽自然，妆容为柔和的精致风格，灵感来自现代土耳其美容潮流，使用温暖的腮红色调、裸色或玫瑰色光泽唇彩，外眼角微微上扬的细微眼线，丰盈的层次感发型，搭配当代伊斯坦布尔时尚造型。\n\n时尚杂志 editorial 布局，简洁现代的排版设计，布局间距均衡，色调柔和中性，专业美容摄影风格，高分辨率，真实皮肤质感与面部比例。",
  "negative_prompt": "夸张的妆容、浓重的修容、生硬的阴影、卡通风格、动漫、扭曲的面部比例、过于锋利的下颌线、低分辨率、过度饱和的颜色、杂乱的布局、水印、标志、文字伪影、重复的脸部、多余的肢体",
  "style": "editorial beauty photography",
  "quality": "high",
  "lighting": "soft studio lighting",
  "background": "neutral gray"
}
```

</details>

<details><summary><b>土耳其甜品店的傍晚</b></summary>

```text
超写实单张照片，傍晚时分，一条繁华街道上一家小型土耳其甜品店的室内场景，使用全画幅 DSLR 相机拍摄，35mm 镜头、光圈 f/1.8、ISO 800，柔和温暖的钨丝灯照明与窗外冷调蓝光交织，电影级色彩分级  

此前出现过的同一位年轻金发女性，二十多岁，肤色白皙，长而略显凌乱的波浪金发，自然妆容，带着一丝疲惫的浅浅微笑，人体比例真实，穿着得体：一件简约黑色羽绒短夹克，内搭浅色毛衣与牛仔裤，无裸露，无性化姿态  

她正独自值晚班：单肘倚靠在窗边一张木质咖啡桌旁，头枕在手腕上，因疲惫而双眼微睁，面前摊开一本写满潦草数字与待办事项清单的笔记本，旁边是一杯喝了一半的土耳其红茶（盛于细玻璃杯中）、一只盛有方糖的小碟，以及几块糕点残渣  

她身后：灯火通明的甜品柜台，陈列着巴克拉瓦（baklava）、库内费（künefe）、洛克马（lokma）及其他土耳其甜点，金属托盘上糖浆晶莹闪烁，玻璃反光中倒映出霓虹店招“tatlı dünyası”的镜像文字；角落有一台迷你冰箱，内装瓶装水与汽水；背景略微虚化  

窗外：模糊的夜间车流，车灯划出的光轨，行人剪影匆匆掠过，一辆黄色出租车停靠在路边，玻璃上飘着细雨，细小水珠折射出霓虹招牌“tatlı dünyası”的微光  

构图：从桌面高度取景的三分之四视角，女性为前景主体，背景呈现散景光斑，画面包含真实杂乱细节（收据卷、纸巾架、盐罐），叙事氛围：一位年轻女性在现代土耳其艰难维生与追逐梦想之间的拉扯，孤独的深夜轮班，苦乐参半却饱含暖意  

风格：自然主义纪实摄影，不加滤镜，皮肤纹理真实，发丝细节丰富，光影与阴影可信，对比度柔和，拍摄意图如同为一篇关于当代土耳其职业女性的深度杂志专题报道
```

</details>

<details><summary><b>圣诞节海报</b></summary>

```text
设计一张以圣诞节为主题的海报，展现浓郁的节日欢庆氛围。需包含以下元素：闪烁的圣诞彩灯、装饰精美的圣诞树、飘落的雪花、包扎好的礼物，以及温馨的冬日背景。整个画面应传递温暖、喜悦与团聚之感。使用红色、绿色和金色等鲜艳色彩，并添加柔和的发光效果，营造出梦幻般的氛围。海报尺寸应为 ${size:1080x1080}，便于在社交媒体上分享。自定义文字内容，加入如“节日快乐！”或“节日问候！”之类的节日祝福语。
```

</details>

<details><summary><b>地中海阳台藤椅悠闲时光</b></summary>

```text
{
  "meta": {
    "type": "image_analysis",
    "file_name": "image_5e33ac.jpg",
    "analyst_persona": "Technical Photo Analyst"
  },
  "scene_environment": {
    "location_type": "Outdoor",
    "setting": "Balcony or patio of a Mediterranean-style resort or villa.",
    "architectural_style": "Whitewashed stucco walls, terracotta roof tiles, wooden beams, wrought iron railings.",
    "atmosphere": "Sunny, relaxed, vacation vibe, warm summer day."
  },
  "technical_aspects": {
    "camera_lens": "Wide-angle lens (approx. 24-35mm equivalent), typical of high-end smartphone main cameras.",
    "camera_angle": "Eye-level relative to the seated subject, slightly looking down.",
    "depth_of_field": "Deep depth of field; both the subject and the background architecture are relatively sharp.",
    "focus": "Sharp focus on the subject's face and torso."
  },
  "lighting": {
    "condition": "High contrast, hard daylight.",
    "sources": [
      {
        "source_id": "light_1",
        "type": "Natural Sun",
        "angle": "Coming from high up, slightly to the subject's right (viewer's left).",
        "color": "Warm white (approx. 5500K).",
        "intensity": "High/Harsh.",
        "effect_on_objects": "Creates distinct, sharp shadows behind the subject and under the architectural beams. Illuminates the white walls brightly."
      }
    ],
    "light_on_body_parts": {
      "face": "Fully illuminated, slight shadow under the nose and chin.",
      "chest_neck": "Direct sunlight, highlighting skin texture and redness/sunburn.",
      "arms": "Right arm (holding cigarette) is fully lit. Left arm has shadows on the underside.",
      "legs": "Thighs are illuminated, with the inner thigh area in shadow due to crossed legs.",
      "shadows": "Hard shadow cast by the subject onto the left side of the chair."
    }
  },
  "subject": {
    "general": {
      "gender": "Female",
      "orientation": "Frontal facing, slightly angled to the right.",
      "gaze": "Direct eye contact with the camera/viewer.",
      "expression": "Subtle smile, relaxed, confident, slightly smug or contented.",
      "emotional_state": "Calm, leisure, unbothered.",
      "sensuality_index": "Moderate; implies casual allure through confident pose and exposed skin, but not explicitly provocative."
    },
    "pose_and_posture": {
      "type": "Seated, relaxed.",
      "head": "Tilted slightly to her left.",
      "torso": "Leaning back slightly into the chair, relaxed posture.",
      "arms": {
        "right_arm": "Extended outwards, resting on the air/knee level, hand holding a cigarette.",
        "left_arm": "Resting on the armrest of the wicker chair.",
        "visibility": "Full arms visible."
      },
      "legs": {
        "position": "Crossed at the thighs (Right leg over Left leg).",
        "knees": "Right knee is the closest point to the camera.",
        "feet": "Cut off from the frame/not visible."
      },
      "visible_extent": "Full body visible from mid-shin upwards."
    },
    "head_details": {
      "hair": {
        "color": "Blonde with darker natural roots showing.",
        "style": "Long, straight, center-parted, framing the face.",
        "texture": "Fine, smooth."
      },
      "face": {
        "structure": "Oval/Heart-shaped.",
        "forehead": "Standard height, partially covered by face-framing hair strands.",
        "brows": "Natural arch, medium thickness, groomed.",
        "eyes": "Almond shape, dark eye makeup/liner visible.",
        "nose": "Button nose, soft features.",
        "mouth": "Closed lips, slight upward curve (smile), natural lip color with gloss.",
        "chin": "Soft, rounded.",
        "skin": "Fair complexion, smooth texture."
      }
    },
    "body_details": {
      "skin_tone": "Fair/White. Noticeable redness (sunburn) on the décolletage/chest area.",
      "neck": "Visible, adorned with a necklace.",
      "shoulders": "Relaxed, slightly slumped forward in a casual manner.",
      "chest_area": {
        "ratio_to_body": "Proportional.",
        "estimated_size": "Average/Moderate.",
        "bra_status": "Likely no bra or a soft bralette due to the dress style (spaghetti straps).",
        "nipple_visibility": "Not prominent.",
        "visual_impact": "Natural shape under the fabric."
      },
      "midsection": {
        "ratio": "Standard, slightly compressed due to seated position.",
        "visibility": "Concealed by the dress, but form is discernible.",
        "definition": "Soft."
      },
      "hips_and_thighs": {
        "hips_ratio": "Appears wider than bust due to seated compression.",
        "thighs": "Full, taking up the lower foreground.",
        "legs_texture": "Smooth skin, no visible blemishes."
      }
    },
    "clothing": {
      "type": "Mini Dress / Slip Dress.",
      "pattern": "Dark green background with a black paisley or floral pattern.",
      "style": "Spaghetti straps, gathered neckline with a small tie string in the center."
    "fit": "合身但不紧贴。",
    "material": "可能是缎面或柔软垂坠的合成混纺面料。"
    },
    "accessories": {
      "neck": "带有矩形吊坠的金链项链。",
      "wrist": "无可见饰品。",
      "fingers": "右手持一支香烟。"
    }
  },
  "objects_in_scene": [
    {
      "object": "Wicker Armchair",
      "description": "深棕色，编织纹理，方正造型。",
      "purpose": "主体的座椅。",
      "location": "画面中央。",
      "contribution": "为主体白皙的皮肤增添质感与对比。"
    },
    {
      "object": "Cigarette",
      "description": "点燃的香烟，带有烟灰。",
      "location": "由主体右手握持。",
      "contribution": "增添一种叛逆或随意的‘快照’叙事感。"
    },
    {
      "object": "Flowers",
      "description": "粉红色天竺葵或类似的花坛植物。",
      "location": "左侧，种植箱内。",
      "color": "鲜艳的粉红色。",
      "contribution": "增添一抹亮色。"
    },
    {
      "object": "Palm Trees",
      "description": "高耸的树干配绿色羽状叶。",
      "location": "右上背景处。",
      "contribution": "确立热带/地中海环境设定。"
    },
    {
      "object": "Buildings",
      "description": "白色灰泥多层建筑。",
      "location": "背景中。",
      "contribution": "将场景定位为度假村或住宅区。"
    }
  ],
  "negative_prompt": "变形，扭曲，残缺，绘制粗糙，解剖错误，结构错误，多余肢体，缺失肢体，漂浮肢体，肢体断连，变异，突变，丑陋，令人不适，模糊，截肢，低质量，灯光不佳，单色，水印，文字，签名，插画，绘画，3d渲染，动漫。"
```

</details>

<details><summary><b>地铁站台街拍</b></summary>

```text
{
  "category": "SUBWAY_PLATFORM_STREET_CANDID",
  "identity_lock": {
    "enabled": true,
    "priority": "ABSOLUTE_MAX",
    "instruction": "严格使用参考图像中的身份。成人，21 岁及以上。保留面部比例与面部特征标记。禁止美颜处理。"
  },
  "subject": {
    "demographics": "成年女性，21–29 岁，身份须与参考图像一致。",
    "hair": {
      "color": "与参考图像一致。",
      "style": "低马尾或松散波浪发，全部收于围巾后方",
      "texture": "呈现真实发丝；略带毛躁；有零散碎发",
      "movement": "几乎无动态；仅平台微风带来轻微飘动"
    },
    "face": {
      "eyes": "完全匹配参考图像；保留真实反光高光点（catchlights）",
      "skin_details": "可见毛孔；阴影真实自然",
      "micro_details": "保留所有面部特征标记"
    },
    "clothing": {
      "outerwear": "极简黑色大衣或夹克（不得含任何标识或文字）",
      "extras": "围巾为可选项（不得含带文字的图案）",
      "fabric": "可见羊毛织物纹理"
    },
    "accessories": {
      "jewelry": ["小号银色圆环耳环（可选）"],
      "bag": "简约托特包或单肩包（不得含任何标识）"
    }
  },
  "pose": {
    "type": "街头抓拍式等待姿态",
    "orientation": "半身站立，靠近站台边缘（保持安全距离）",
    "head_position": "头部略倾斜，姿态沉静",
    "hands": "一手持包带，另一手插在口袋中",
    "gaze": "目光直视镜头，神情中性而自信",
    "expression": "沉静，略带严肃感"
  },
  "setting": {
    "environment": "地铁站台",
    "background_elements": [
      "头顶荧光灯管",
      "背景中列车运动模糊（不可见可读标识）",
      "站台地砖，呈现真实磨损痕迹"
    ],
    "depth": "人物面部清晰锐利；背景适度虚化"
  },
  "camera": {
    "shot_type": "街头风格人像",
    "angle": "平视角度（与被摄者视线齐平）",
    "focal_length_equivalent": "35mm 编辑级镜头 或 26mm 手机镜头",
    "framing": "4:5 构图，利用站台线条引导视觉",
    "focus": "双眼焦点锐利；背景允许运动模糊"
  },
  "lighting": {
    "source": "头顶荧光灯光 + 环境光",
    "direction": "自上而下主光，辅以柔和补光",
    "highlights": "头发与皮肤上呈现真实光泽",
    "shadows": "阴影柔和，略带地铁环境特有的冷调对比"
  },
  "mood_and_expression": {
    "tone": "情绪化、都市感、自信",
    "atmosphere": "真实城市通勤场景下的街头抓拍氛围"
  },
  "style_and_realism": {
    "style": "照片级写实街头人像",
    "imperfections": "背景含适度噪点 + 轻微运动模糊"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "resolution": "高分辨率",
    "noise": "中等程度弱光颗粒感",
    "mode_variants": {
      "amateur": "类手机 HDR 效果，轻微颗粒感，构图略有不完美",
      "pro": "曝光更干净，高光控制精准，主体与背景分离更清晰"
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
    "可读标识", "标识（logos）", "水印（watermark）",
    "身份偏移（identity drift）", "面部形变（face morphing）",
    "多余手指", "扭曲的手部",
    "CGI 效果", "塑料质感皮肤", "过度平滑处理"
  ]
}
```

</details>

<details><summary><b>城市中的巨型纪念物</b></summary>

```text
你身处${location}的人群之中，抬头仰望一座巨大的纪念性混凝土${object}，其表面布满锈迹、苔藓与浅淡的常春藤；然而，在强烈阳光直射之处，银色光泽仍穿透而出，凝固成一个标志性的电影式瞬间。人们正在${date}各自处理自己的需求。
```

</details>

<details><summary><b>城市中的男子摄影</b></summary>

```text
创作一张捕捉${city:Istanbul}中一名男子的照片，使用以下可自定义变量：

- **地点**：包含伊斯坦布尔标志性地点，例如${location:Galata Tower}、${location2:Blue Mosque}或${location3:Bosphorus}。
- **一天中的时间**：在${timeOfDay:sunrise}、${timeOfDay2:noon}或${timeOfDay3:sunset}时分拍摄该场景，以营造不同的氛围情绪。
- **着装**：让该男子穿着${attire:casual}、${attire:business}或${attire:traditional}风格的服装，以体现多种风格。
- **活动**：该男子可以正在${activity:walking}、${activity:sitting}或${activity:looking out over the city}，以传达不同的叙事。

使用这些变量构建一幅独特的摄影场景，展现${city:Istanbul}充满活力的文化与多元化的氛围。
```

</details>

<details><summary><b>城市悬浮岛海报</b></summary>

```text
设计一座“漂浮的微型岛屿”，其形状为${city:denizli}市的地图轮廓/剪影，悬浮于白色云层之上。岛上需无缝融合${city:denizli}最具标志性的地标、建筑结构及自然景观（公园、滨水区、山丘）。将大型白色3D字母“${city:denizli}”融入岛屿表面或地理纹理之中。通过该城市特有的鸟类、电影级阳光、鲜明色彩、鸟瞰视角，以及逼真的阴影/反射渲染，强化整体氛围。超高清画质、超写实纹理、4K+分辨率、数字海报格式。正方形1×1构图，照片级真实感、体积光、全局光照、光线追踪。
```

</details>

<details><summary><b>复古发明专利文件</b></summary>

```text
一份关于${invention}的复古专利文件，风格仿照19世纪晚期美国专利商标局（United States Patent Office）的申报文档。页面包含精确的技术绘图，并配有带编号的标注说明（图1、图2、图3），分别展示正面视图、侧面视图和爆炸分解视图。使用钢笔墨水手写批注，描述各机构部件的工作原理。纸张呈泛黄象牙色，带有霉斑污渍（foxing stains）及柔和的折痕。页角处印有官方浮雕印章与红色火漆印。底部为发明人亲笔签名及签署日期。整幅图像令人感觉如同一份重见天日的档案文献——权威、厚重、富有历史感，且略带神秘气息。
```

</details>

<details><summary><b>复古未来主义七十年代科幻</b></summary>

```text
复古未来主义风格的 1970 年代科幻电影画面，使用 35mm 胶片拍摄。人物身着高领象牙色制服，头戴 oversized 白色球形头盔，配深色遮光面罩。构图对称、广角，留白强烈，融合韦斯·安德森（Wes Anderson）与斯坦利·库布里克（Stanley Kubrick）式的冷面美学（deadpan aesthetic）。光线柔和、漫射、阴天感，整体氛围洁净而临床化，阴影对比度低。色调为低饱和度的粉彩色系：白色、米色、浅蓝色、褪色青绿色（desaturated teal）及浅大地色系，胶片略带朦胧泛色（hazy film tint）。场景设定于粗野主义（brutalist）极简室内空间，或雾气弥漫的海岸景观中，配有复古模拟（retro-analog）科技设备与方正笨重的未来主义载具。呈现 Kodak Portra 400 胶片质感：可见胶片颗粒（film grain）、细微动态模糊（motion blur）、大景深（deep depth of field）、触感强烈的哑光纹理（tactile matte textures）。
```

</details>

<details><summary><b>复古植物图鉴插画</b></summary>

```text
一幅关于 ${subject} 的植物学图解，以复古科学期刊的风格绘制。采用自然色调，并包含精细的横截面图示；图中配有赭石墨水手写标注，营造出学术性与古雅韵味并存的氛围。
```

</details>

<details><summary><b>复古胶片相机风格</b></summary>

```text
Kodak Portra 400 真实复古胶片摄影，使用经典 35mm 胶片相机搭配手动对焦镜头拍摄，使用过期的 Kodak Portra 400 胶片拍摄，明显的自然胶片颗粒结构，明亮高光周围可见晕染（halation），温暖怀旧的色彩调性，中间调略去饱和，帧与帧之间呈现有机的色彩偏移，Portra 胶片特有的柔和桃色肤色，柔和梦幻的暗角，向画面角落和边缘逐渐变暗，偶然的漏光现象，橙色和红色色调渗入画面边缘，来自未镀膜复古光学镜头的微妙镜头眩光，不完美的手动对焦产生梦幻般的散景，失焦区域呈漩涡状，高对比边缘可见色差，扫描过程中捕获的胶片灰尘颗粒和毛发，胶片传输机构造成的细微垂直划痕，真实胶片的温暖感，黑位略抬高，高光被压缩，相邻胶片层之间自然的色彩溢出，亮部轻微过曝产生柔和辉光，胶片边缘痕迹和帧编号几乎不可见，从原始负片扫描而来，带有轻微色偏，1990 年代傻瓜一次性相机美学，Fujifilm Superia 或 Agfa Vista 胶片特性的替代表现，有机的摄影瑕疵与不一致性，整体锐度略偏柔和，角落可选日期戳，双重曝光幽灵影像轻微叠加，片孔压痕，交叉冲洗造成的色彩偏移，推冲显影效果呈现更高对比度和颗粒感，自然的光线伪影与镜头缺陷，复古照片冲印店色彩校正风格，真实的胶片乳剂纹理，帧与帧之间曝光变化体现人为拍摄痕迹，机械快门伪影，较慢快门速度导致的轻微运动模糊，怀旧的夏日午后黄金时刻温暖感，如同在旧鞋盒中发现的褪色照片质感，记忆长廊美学，可触的模拟摄影感受
```

</details>

<details><summary><b>复古胶片肖像</b></summary>

```text
Vintage 1980s-style analog photograph, warm faded colors, heavy grain, slight light leak. Iranian woman, thick natural brows, looking up from beneath lowered lashes, one brow subtly raised, a slow blink — coquettish "naz". Old family-album texture. Below the photo, a hand-torn sketchy frame with old-fashioned fountain-pen handwriting: "ناز".
```

</details>

<details><summary><b>复古铜版画肖像</b></summary>

```text
使用提供的参考图像作为严格的身份参照，创作一幅复古雕版风格的肖像插画。  
保留照片中人物的精确面部特征、比例、骨骼结构和整体相貌，不得有任何改动。人物以侧脸轮廓呈现，微微抬头向左，表情自信而富有思考感。头顶为短发，带有细微的灰色调，两侧较稀疏，下颌线周围留有分布整齐的胡须。面部细节通过精细的交叉排线和点刻雕版纹理进行刻画。人物佩戴眼镜，身穿浅米色西装外套，布料带有微妙的对角纹理，内搭深海军蓝衬衫。头部后方是一个圆形的平坦暖黄色背景。采用单色蓝色墨水线条，高对比度，搭配柔和的米白色高光。结合矢量般的精准度与手绘雕版纹理。胸部以上肖像构图，背景为干净的浅灰色，4K 分辨率，杂志插画风格。
```

</details>

<details><summary><b>夜店卡座闪光抓拍</b></summary>

```text
{
  "category": "NIGHTCLUB_BOOTH_FLASH",
  "subject": {
    "demographics": "成年女性，21–29 岁，土耳其人外貌，夜生活氛围。",
    "hair": {
      "color": "深棕色",
      "style": "略显凌乱，适合夜间外出的发质纹理",
      "texture": "发丝清晰可见，略带光泽",
      "movement": "头发轻微移位，仿佛正在跳舞"
    },
    "face": {
      "eyes": "明亮、俏皮",
      "skin_details": "真实肌肤纹理，略带闪光反光",
      "makeup": "夜间外出风格的自然华丽妆容"
    },
    "clothing": {
      "outfit": "时尚黑色穿搭，无任何品牌标识",
      "fabric": "逼真的织物光泽（非塑料感）"
    },
    "accessories": {
      "jewelry": ["银色圆环耳饰"],
      "props": ["简约酒杯（无标签）"]
    }
  },
  "pose": {
    "type": "半身卡座抓拍照",
    "orientation": "略微朝向相机倾斜",
    "hands": "一只手持酒杯，另一只手轻拂头发至耳后",
    "gaze": "直视镜头",
    "expression": "俏皮的浅笑"
  },
  "setting": {
    "environment": "夜店卡座",
    "background_elements": [
      "彩色灯光散景",
      "柔和的大气薄雾（非烟雾）",
      "模糊的人群剪影（无人脸可辨识）"
    ],
    "depth": "面部清晰锐利，背景散景强烈"
  },
  "camera": {
    "shot_type": "半身夜生活人像照",
    "angle": "平视角度，手持拍摄",
    "focal_length_equivalent": "26mm 手机夜景模式",
    "framing": "4:5",
    "focus": "双眼清晰锐利，背景虚化柔和"
  },
  "lighting": {
    "source": "手机闪光灯 + 环境夜店灯光",
    "highlights": "面部有闪光灯爆闪效果，呈现真实反光",
    "shadows": "阴影柔和但对比度鲜明，体现夜生活观感"
  },
  "mood_and_expression": {
    "tone": "欢乐、自信、自然抓拍",
    "atmosphere": "充满活力的夜生活氛围"
  },
  "style_and_realism": {
    "style": "照片级写实风格的派对用户生成内容（UGC）",
    "imperfections": "可见胶片颗粒感，背景略有轻微模糊"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "明显但符合低光照条件的真实噪点",
    "motion_blur": "运动模糊极小；仅允许出现在背景中"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "可读文字标识", "品牌标识（logos）", "水印（watermark）",
    "塑料质感皮肤", "CGI（电脑生成图像）",
    "多余肢体", "扭曲的手部"
  ]
}
```

</details>

<details><summary><b>夜店镜前自拍</b></summary>

```text
{
  "subject": {
    "description": "一位自信满满、准备外出过夜的年轻女性，在伊斯坦布尔一家夜店的洗手间里拍摄的镜前自拍。她充满夜店活力，因跳舞而微微出汗，面部色调未泛红或过度发红。皮肤干净无纹身。",
    "body": {
      "type": "曲线优美、女性化的轮廓。",
      "details": "自然比例，因高温和运动而带有微妙的汗珠光泽。腰部可见；领口设计优雅，适合夜生活，展现适度露肤。面部保持中性色调，自然。",
      "pose": "站在洗手间镜子前，正对镜子，采用经典的镜前自拍构图。手机本身大部分在画面外，但闪光反射和构图清晰表明是iPhone前置摄像头拍摄。"
    }
  },
  "wardrobe": {
    "top": "精致的蕾丝吊带式上衣，细肩带，适合夜店穿着，展现柔和的露肤设计。",
    "bottom": "适合夜晚外出穿的高腰短裤或紧身迷你裙。",
    "bag": "小巧的肩包自然地挂在一侧肩膀上。",
    "accessories": "脖子上佩戴多层项链，手腕上有手链，手指上有戒指，耳朵上可见耳环。"
  },
  "scene": {
    "location": "伊斯坦布尔一家夜店的洗手间内。",
    "background": "现代夜店洗手间，配有大型镜子、瓷砖或混凝土墙面、洗手池，以及柔和的霓虹灯或温暖的氛围照明。",
    "details": "诸如EXIT或WC的标识干净自然地放置在墙上或门上方。这些标识在镜子和光滑表面上柔和反射，增加了深度和真实感。镜子上的轻微冷凝和表面的真实磨损增强了深夜氛围。"
  },
  "camera": {
    "angle": "镜前自拍视角。",
    "device": "iPhone，可通过特征性的闪光强度、色温和镜头位置反射识别。",
    "aspect_ratio": "9:16",
    "flash": "开启，产生明亮、锐利的iPhone风格闪光，在镜子中清晰反射。"
  },
  "lighting": {
    "type": "直接的iPhone闪光与昏暗的夜店洗手间照明相结合。",
    "quality": "高对比度的闪光突出皮肤和蕾丝面料纹理，清晰的镜子反射，可见的光线反弹和标识反射，周围环境较暗，带有霓虹色调。"
  }
}
```

</details>

<details><summary><b>夜晚复古车载收音机</b></summary>

```text
创建一张高分辨率的*竖版（人像）*照片，主题为夜间的一台复古汽车收音机屏幕。相机角度必须符合真实斜侧视角，类似于从乘客座位拍摄的、越过肩膀式的电影镜头。切勿将设备摆正——须保留真实夜间驾驶照片中所见的自然倾斜角度。

LED 显示屏上的文字（琥珀色像素字体）：  
Weather4Fly  

风格与布光：  
– 温暖的橙色 LED 发光效果，每个分段式字符周围带有柔和辉光；  
– 暗色汽车内饰，环境光极少；  
– 深邃阴影、浅景深、柔焦高光虚化（bokeh）；  
– 塑料显示屏盖板上有细微划痕，并附着轻微灰尘颗粒；  
– 高对比度、情绪化、富有电影感的夜间驾驶美学。  

构图：  
– 画面必须呈*高纵比*，上下延伸超出收音机本体，以构成竖版人像构图；  
– 收音机位于画面中上部，其倾斜角度须与真实汽车仪表台完全一致；  
– 包含侧面旋钮、按钮，以及部分渐隐于阴影中的仪表台；  
– 保持非对称构图与自然透视畸变。  

细节要求：  
– LED 字符须呈现分段式结构，且外观真实可信；  
– 显示屏表面需有轻微反光；  
– 仅使用暖色调——禁用霓虹色或任何人工色彩偏移。  

负面提示词（NEGATIVE PROMPT）：  
横版布局、正面直视视角、蓝色或白色 LED、现代触摸屏收音机、缺失文字、名称错误、过度锐利的数字感外观、不真实的对称性、卡通渲染风格。  

输出：  
一张电影感竖版人像照片，呈现一台带倾斜角度的复古收音机显示屏，清晰显示指定的文字内容。
```

</details>

<details><summary><b>夜晚海滩上的情侣</b></summary>

```text
夜幕下，一对情侣手牵手走在宁静的海滩上，镜头采用电影级广角拍摄，人物在画面中显得渺小而遥远，以突出广阔环境。深青绿色与深蓝色调色。广阔的清晰夜空。轻柔的海浪缓缓拍打着海岸，泛起白色的泡沫反光。

摄像机：从后方平滑缓慢跟拍，广角构图，轻微的电影感漂移，稳定运动  
构图：人物置于画面下三分之一处，比例较小，留有大量负空间，突出天空与海洋  
照明：低光环境，情绪化氛围，高对比度，柔和阴影，水面与沙滩上有微妙的高光  
运动：自然的行走动作，微风轻拂头发与衣物，海浪缓慢移动  
风格：梦幻的低保真感，浪漫氛围，胶片颗粒，变形镜头，浅景深  
质量：超现实，8K，构图干净，无杂乱  

时长：5–8 秒  
帧率：24fps 电影感
```

</details>

<details><summary><b>夜晚霓虹小巷半身照</b></summary>

```text
{
  "category": "NEON_NIGHT_ALLEY_HALF_BODY",
  "subject": {
    "demographics": "成年女性，21–27 岁，土耳其人外貌。",
    "hair": {
      "color": "深棕色",
      "style": "松散、略显凌乱的夜间外出发型",
      "texture": "发丝清晰可见，略带光泽",
      "movement": "几缕碎发捕捉到霓虹边缘光"
    },
    "face": {
      "eyes": "直视镜头，锐利的高光点",
      "makeup": "夜间外出风格的低调华丽妆容，不浓重",
      "skin_details": "真实毛孔，轻微油光，不作柔化处理"
    },
    "clothing": {
      "outfit": "前卫黑色夹克/上衣，无任何标识",
      "fabric": "类皮革或哑光质感织物，具备真实纹理"
    },
    "accessories": {
      "jewelry": [
        "小巧银质圆环耳环"
      ]
    }
  },
  "pose": {
    "type": "半身倚墙姿势",
    "orientation": "肩部靠墙，下颌微微抬起",
    "hands": "一只手插在夹克口袋中，另一只手轻触衣领",
    "gaze": "强烈眼神接触，略带微妙笑意",
    "posture": "放松而自信"
  },
  "setting": {
    "environment": "夜间霓虹照明的小巷",
    "background_elements": [
      "霓虹辉光（不可读取文字）",
      "湿润地面的倒影",
      "柔和雾气，呈现为氛围感而非烟雾"
    ],
    "depth": "主体清晰锐利，背景为霓虹虚化效果（bokeh）"
  },
  "camera": {
    "shot_type": "半身人像",
    "angle": "平视角度",
    "focal_length_equivalent": "35–50mm 专业镜头，或 26mm 手机夜间模式变体",
    "framing": "4:5 构图，非对称布局",
    "focus": "双眼清晰锐利，霓虹背景虚化"
  },
  "lighting": {
    "source": "霓虹实景光源 + 环境城市光",
    "direction": "霓虹侧向边缘光，街道反射提供柔和补光",
    "highlights": "对头发及脸颊边缘施加可控的霓虹边缘高光",
    "shadows": "浓郁、真实的夜间对比度"
  },
  "mood_and_expression": {
    "tone": "前卫、自信、时尚",
    "expression": "沉静而富有张力",
    "atmosphere": "都市夜晚，电影感"
  },
  "style_and_realism": {
    "style": "写实主义夜生活人像",
    "fidelity": "高细节，允许存在真实低光照噪点"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "低光照颗粒感（真实）",
    "motion_blur": "面部无动态模糊；仅背景虚化区域可允许轻微动态模糊"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "可读的霓虹招牌",
    "标识",
    "水印",
    "塑料质感皮肤",
    "CGI 风格外观",
    "多余手指",
    "扭曲面部",
    "重复主体"
  ]
}
```

</details>

<details><summary><b>夜班甜品店</b></summary>

```text
{
  "name": "night_shift_dessert_shop",
  "prompt": "超写实单张照片，傍晚时分，一条繁华街道上一家小型土耳其甜品店的室内场景，使用全画幅 DSLR 相机、35mm 镜头、光圈 f/1.8、ISO 800 拍摄；店内为柔和温暖的钨丝灯照明，与窗外冷调蓝色街灯混合；电影级色彩分级。主角为此前出现过的同一位年轻金发女性，二十多岁，肤色浅，长而略显凌乱的波浪金发，妆容自然，面带一丝疲惫的浅浅微笑，人体比例真实，着装朴素：浅色毛衣外搭黑色短款羽绒服，下穿牛仔裤，无裸露，无性化姿态。她独自值晚班：单肘倚靠在窗边一张木质咖啡桌旁，头枕于手腕之上，双眼因疲惫而半睁，面前放着一支圆珠笔和一本摊开的笔记本，本子上密布潦草书写的数字与待办事项清单；旁边是一杯喝了一半的土耳其茶（盛于细玻璃杯中），小碟内盛有方糖，还有刚吃过的点心碎屑。她身后是灯火通明的甜品柜台：托盘中陈列着巴克拉瓦（baklava）、库纳费（künefe）、洛克马（lokma）及其他土耳其甜点，金属托盘上糖浆晶莹闪烁；玻璃反光中倒映出霓虹店招“tatlı dünyası”（甜点世界）的镜像；角落有一台迷你冰箱，内有瓶装水与汽水；背景略微失焦。窗外：夜间车流模糊不清，车灯拖曳成光痕，行人剪影匆匆掠过，一辆黄色出租车停靠在路边，玻璃上飘着细雨，细小水珠折射出霓虹招牌“tatlı dünyası”的微光。构图：从桌面高度拍摄的三分之四视角，女性为前景主体焦点，背景呈现散景光斑，画面包含真实杂乱细节（收据卷、纸巾架、盐罐），叙事氛围：一位年轻女性在生存与梦想之间艰难平衡，孤独的深夜轮班，苦乐交织却温暖动人。风格：自然主义纪实摄影，不加滤镜，皮肤纹理真实，发丝细节丰富，光影与阴影可信，对比度柔和，拍摄意图如同为一篇关于当代土耳其职业女性的深度杂志专题报道。",
  "negative_prompt": "非动漫风格，非插画，非 3D 渲染，非油画，非漫画 caricature，无鱼眼畸变，无过度镜头光晕，无高光过曝，无 HDR 光晕，无选美式华丽感，无极端修图，无发光肌肤，无塑料娃娃质感，无超现实色彩，无赛博朋克式霓虹，无奇幻元素，无翅膀，无魔法，无人脸或肢体重复，无手部畸形，无多余手指，无文字叠加层或大幅字幕，无水印，无品牌标识，无色情内容或透视装束。",
  "width": 832,
  "height": 1216,
  "cfg_scale": 5.5,
  "steps": 30,
  "sampler": "euler",
  "seed": 11223344
}
```

</details>

<details><summary><b>夜生活闪光灯抓拍</b></summary>

```text
一个高角度、强烈直射闪光灯拍摄的夜间快照，场景位于昏暗的户外酒吧露台。照片从略高于主体的位置拍摄，仿佛相机被举过头顶，或从一个小台阶、阳台俯拍。使用长焦镜头压缩构图，避免广角畸变和典型的AI智能手机风格。采用人像焦段等效85mm至200mm的长焦视觉效果，摄影师站位比自拍距离更远，使人物面部比例自然且具高端感。

场景：一名年轻成年女性（21岁以上）随意坐在夜晚户外酒吧区域的吧凳上。环境整体黑暗，仅限闪光照射范围可见。直射闪光强烈且接近轴向，导致她白皙皮肤出现明显过曝，产生清晰的镜面高光，并在地面上投下锐利、边缘分明的硬阴影。阴影轮廓鲜明、对比度高，环境补光极少。背景基本模糊不清，闪光范围之外的边缘处有微弱的人影剪影，因长焦压缩而显得更大、更“堆叠”在她身后，但仍处于昏暗状态，不构成干扰。

主体细节：她表情俏皮顽皮——一只眼睛眨眼，舌头调皮地伸出，呈现一种即兴、自然的状态。她留着一头中分的短灰棕色波波头，几缕松散发丝垂落前方，部分遮挡脸部。强光下可清晰看到她的浅褐色眼睛与卷曲的睫毛。嘴唇呈亮泽、粉嫩、微噘状，因吐舌动作而微微张开。鼻中隔穿孔在闪光下反射出细小的金属高光。皮肤保留真实质感与毛孔细节，自然红晕部分被闪光冲淡但仍可信。无美颜滤镜磨皮效果，不出现塑料感肌肤。

穿搭：她内搭黑色背心，外穿一件敞开的蓝、白、黑格纹法兰绒衬衫，布料褶皱真实，略带磨损感。下身穿牛仔迷你裙，配一条小巧黑色腰带。整体造型体现原始Y2K千禧年垃圾摇滚街头风格，展现真实夜生活氛围，而非摆拍时尚感。手臂和手部可见纹身，线条清晰锐利，未发生扭曲变形。

手部与香烟：左手放松自然，手指间夹着一支点燃的香烟。香烟火星清晰可见，烟雾飘散时捕捉到闪光，形成一条明亮、有纹理的烟雾带，边缘高光锐利，在深色背景下尤为突出。烟雾看起来真实，非叠加雾效，呈现不规则飘动与细微湍流。

前景桌面：她面前是一张圆形石质旧桌，表面有逼真的污渍与材质纹理。桌上摆放多个装有饮品的玻璃杯（形状各异、液位不同）、一个玻璃水壶，以及一包标注为“{argument name="cigarette brand" default="Gudang Garam Surya 16"}”的香烟。香烟包装明确出现在画面中，摆放角度随意，如同真实夜生活快照。玻璃器皿上的反光由闪光主导，呈现坚硬高光点与快速衰减的光晕。

构图与氛围：相机角度从上方俯视，但非超广角。构图略显不完美、具有自发性，如同真实夜生活中用闪光灯拍摄的照片。保持主体在画面中的主导地位，同时利用桌面上的物品锚定前景。背景顾客几乎不可见，黑暗且失焦。整体美学风格：原始、粗粝、抓拍感强，Y2K垃圾摇滚风，街头服饰夜生活，纪实快照风格。高度写实，强调质感，极少风格化处理。

光学与拍摄提示（必须遵守）：长焦镜头视觉效果（等效85mm至200mm），压缩透视感，面部比例自然，真实的景深表现，光学生成的真实散景（非人工模糊）。直射闪光，硬阴影，皮肤上有轻微过曝高光但保留真实纹理。允许轻微运动真实感，但需确保面部清晰可辨，不模糊。
```

</details>

<details><summary><b>夜街上的女人与猫</b></summary>

```text
图像生成：
  主体：“一位1980年代风格的女性，身旁伴有一只猫，二者均位于画面前景。”
  服饰：“磨损的夹克、毛毯和旧裤子。”
  面部：“不可见，或面朝别处。”

  环境：
    街道：“两旁种有树木，沿街为单层住宅，死胡同。”
    时间：“黄昏时分”
    氛围：“下雨，多云”

  技法：
    风格：“照片级写实风格，如同由真实相机拍摄”
    焦点：“浅景深、散景（bokeh）与边缘光（rim lighting）”
    光照：“主体照明充足，背景偏冷”
    色彩：“背景为蓝色，主体焦点区域为红色”

  构图：
    类型：“宽幅风景镜头”
    背景：“林地、草坪、花园”

  情绪：
    - “抑郁的”
    - “含泪的”

  负向提示词（negative）：
    - “HDR”
    - “素描”
    - “黑白”
    - “低分辨率”
    - “多云”
```

</details>

<details><summary><b>大雪夜晚人像</b></summary>

```text
{
  "image_analysis": {
    "meta": {
      "type": "photorealistic",
      "style": "candid_night_portrait",
      "subject_count": 1
    },
    "environment": {
      "type": "outdoor",
      "location": "residential_complex_parking_lot",
      "weather": "heavy_snowfall",
      "time_of_day": "night",
      "atmosphere": "cold, wintery, urban"
    },
    "camera_settings": {
      "lens_type": "wide_angle_smartphone_lens",
      "perspective": "eye_level",
      "depth_of_field": "moderate_focus_falloff",
      "focus_point": "subject_full_body",
      "grain": "visible_iso_noise"
    },
    "lighting": {
      "summary": "Mixed lighting with strong atmospheric color cast",
      "sources": [
        {
          "id": "light_source_1",
          "type": "sky_glow_light_pollution",
          "color": "deep_orange_red",
          "intensity": "high_ambient",
          "angle": "overhead_diffused",
          "effect": "casts_reddish_hue_on_snow_and_background"
        },
        {
          "id": "light_source_2",
          "type": "street_lamps",
          "color": "warm_yellow",
          "intensity": "moderate",
          "angle": "background_scattered",
          "effect": "illuminates_buildings_and_parked_cars"
        },
        {
          "id": "light_source_3",
          "type": "camera_flash_or_direct_source",
          "color": "cool_white",
          "intensity": "high",
          "angle": "frontal",
          "effect": "highlights_subject_face_legs_and_jacket_texture"
        }
      ]
    },
    "people": [
      {
        "id": "person_1",
        "demographics": {
          "gender": "female",
          "age_group": "young_adult",
          "body_type": "slender_fit"
        },
        "orientation": {
          "body_direction": "facing_camera_angled_right",
          "face_direction": "facing_camera",
          "gaze": "towards_camera_slightly_down"
        },
        "emotion_and_attitude": {
          "primary_emotion": "playful_shy",
          "secondary_emotion": "joyful",
          "sensuality": "moderate_playful_allure",
          "vibe": "candid_winter_fun",
          "posture_impact": "relaxed_stance_conveys_comfort_despite_cold"
        },
        "pose_details": {
          "general": "standing_full_body",
          "feet_position": "left_foot_planted_right_foot_slightly_forward_relaxed",
          "hand_position": {
            "left_hand": "raised_covering_mouth_fingers_curled",
            "right_hand": "hanging_loose_by_side"
          },
          "visible_extent": "full_body_head_to_toe"
        },
        "head_and_face": {
          "hair": {
            "color": "dark_brown",
            "style": "loose_waves_shoulder_length",
            "texture": "thick_voluminous",
            "condition": "speckled_with_snowflakes"
          },
          "face_structure": {
            "shape": "oval",
            "forehead": "partially_covered_by_hair_parting",
            "eyes": "dark_slightly_squinting_smiling",
            "nose": "partially_obscured_by_hand",
            "mouth": "covered_by_hand_hiding_smile",
            "skin_tone": "fair_illuminated_by_flash"
          },
          "makeup": {
            "style": "natural_minimal",
            "visible_details": "red_nail_polish_visible_on_hand"
          }
        },
        "body_analysis": {
          "skin_tone": "fair_tan_on_legs",
          "neck": "covered_by_jacket_collar",
          "shoulders": "broadened_by_oversized_jacket",
          "chest": {
            "ratio_to_body": "obscured_by_thick_outerwear",
            "visibility": "hidden",
            "bra_status": "indeterminate"
          },
          "waist_belly": {
            "ratio": "obscured_by_straight_cut_jacket",
            "visibility": "hidden"
          },
          "hips_glutes": {
            "ratio": "standard_to_slender_frame",
            "visibility": "partially_covered_by_jacket_hem"
          },
          "legs": {
            "description": "prominent_slender_toned",
            "visibility": "exposed_from_mid_thigh_to_knee",
            "ratio": "long_relative_to_torso"
          }
        },
        "clothing_and_accessories": {
          "outerwear": {
            "item": "shearling_aviator_jacket",
            "color": "black_with_white_lining",
            "material": "leather_faux_leather_wool",
            "fit": "oversized_boxy",
            "lighting_effect": "absorbs_light_reflects_snow_flakes"
          },
          "lower_body": {
            "item": "mini_skirt_or_dress_hem",
            "color": "black",
            "visibility": "barely_visible_under_jacket"
          },
          "leg_wear": {
            "item": "pantyhose_tights",
            "finish": "shiny_glossy",
            "color": "nude_beige",
            "lighting_effect": "highly_reflective_of_flash"
          },
          "footwear": {
            "item": "knee_high_boots",
            "color": "black",
            "material": "leather_synthetic"
          "condition": "底部覆盖积雪",
          "style": "平底或低跟，实用型"
          },
          "accessories": {
            "jewelry": "左手无名指佩戴银色戒指"
          }
        }
      }
    ],
    "objects_in_scene": [
      {
        "object": "vehicles",
        "description": "多排停放的轿车",
        "state": "静止状态，表面覆盖积雪",
        "colors": ["灰色", "白色", "银色"],
        "purpose": "住宅区停车场景的背景信息",
        "relation": "位于主体后方，营造景深"
      },
      {
        "object": "buildings",
        "description": "多层公寓楼群",
        "style": "现代混凝土建筑风格",
        "colors": ["米色", "棕色边饰"],
        "location": "左右后景",
        "purpose": "围合场景"
      },
      {
        "object": "snow",
        "description": "地面覆盖层及飘落的雪花",
        "texture": "被车辙和脚印扰动",
        "color": "白色，反射橙色天空",
        "location": "前景与背景",
        "purpose": "定义氛围"
      }
    ],
    "negative_prompt": " daylight, summer, sunshine, dry ground, indoor, studio, blurry face, distorted hands, extra fingers, low resolution, cartoon, painting, illustration, nudity, bikini, swimwear, green grass, blue sky, crowd, men, animals"  
  }
```

</details>

<details><summary><b>天台生活方式人像</b></summary>

```text
{
  "subject": {
    "description": "一位皮肤白皙的年轻金发女性坐在户外直射阳光下，神情放松，略带微笑，因光线明亮而轻微眯眼。",
    "body": {
      "type": "女性，苗条体型",
      "details": "浅肤色，直顺金发披散，自然妆容，皮肤略带阳光照射效果",
      "pose": "倚靠在现代户外椅子上，身体略微向右倾斜，双腿向前伸展，双手放在腿附近握着一部手机"
    },
    "face": {
      "expression": "柔和微笑，因阳光照射而眼睛轻微眯起，神情放松且自信",
      "gaze_direction": "望向镜头",
      "head_tilt": "头部略微向右倾斜",
      "skin": "光滑，自然肤质带有阳光高光，瑕疵极少"
    },
    "wardrobe": {
      "top": "白色合身T恤",
      "bottom": "浅蓝色破洞牛仔裤，膝盖处有撕裂",
      "outerwear": "黑色夹克随意搭在肩上",
      "accessories": "太阳镜搁在头顶，佩戴极简首饰"
    },
    "hair": "披肩的松散金发，自然垂落于肩部，带有轻微阳光高光"
  },
  "scene": {
    "description": "白天的屋顶露台，背景为城市住宅建筑。",
    "location": "城市中的户外露台（地中海/欧式建筑风格）。",
    "setting": "屋顶休息区",
    "background_elements": "木制种植箱内有绿植，混凝土地砖，附近的带窗户建筑和屋顶",
    "lighting": "强烈的自然阳光投射出清晰的阴影",
    "atmosphere": "随意、阳光明媚、轻松的白天氛围"
  },
  "environment": {
    "ambience": "明亮的日光，户外，通透感",
    "style": "抓拍式生活方式瞬间",
    "depth_of_field": "中等景深，主体清晰对焦，背景略微柔化但仍可辨识"
  },
  "camera": {
    "device": "iPhone 13 后置摄像头",
    "mode": "标准拍照模式",
    "lens": "广角镜头（约26mm等效）",
    "angle": "略微俯视角度，仿佛拍摄者站在主体上方",
    "aspect_ratio": "4:5",
    "framing": "全身坐姿构图，主体位于画面稍偏下方中央位置",
    "focus": "主体对焦清晰",
    "stability": "手持拍摄"
  },
  "image_quality": {
    "resolution": "标准手机分辨率",
    "grain": "极细微颗粒感",
    "sharpness": "自然智能手机锐化",
    "compression_artifacts": "极少",
    "dynamic_range": "高光明亮，在最强日光区域略有溢出"
  },
  "lighting": {
    "type": "直射阳光",
    "quality": "强烈、高对比度照明，阴影明显",
    "effects": "头发和皮肤上的阳光高光，地面和椅子上有清晰锐利的阴影边缘"
  },
  "color_grading": {
    "tone": "自然日光色调",
    "temperature": "略微偏暖",
    "contrast": "中等到高对比度，由阳光造成",
    "saturation": "真实，略显鲜艳",
    "highlights": "明亮，在阳光直射区域略有过曝",
    "shadows": "轮廓分明且较暗"
  },
  "rendering": {
    "style": "逼真的智能手机摄影风格",
    "quality": "干净、自然、无滤镜感",
    "skin_texture": "自然肤质带有阳光反射",
    "post_processing": "极少后期处理，直出相机效果"
  },
  "artifacts": {
    "lens_flare": "可能有极细微的阳光镜头眩光",
    "noise_pattern": "极少",
    "motion_blur": "无",
    "chromatic_aberration": "高对比边缘处有轻微色差"
  },
  "constraints": {
    "focus_priority": "主体必须保持为主要焦点",
    "avoid": "过度处理的皮肤、人工光源、影棚风格、电影级调色"
  }
}
```

</details>

<details><summary><b>天然岩池合影</b></summary>

```text
{
  "prompt": "一张坦率的户外照片，展现一群成年人（21 岁及以上）站在清澈水体中，水深及腰，地点为岩石构成的天然水池或洞穴。背景是一面深色、富有纹理的岩壁，略带湿气且表面不平整，占据画面大部分区域。光线为自然日光，柔和但直射，在湿润的皮肤上形成真实可信的高光。\n\n画面中央，一位肤色浅白、湿漉漉的金色长发向后梳拢的女性正面带笑容，双臂轻松而活泼地高举过头顶。她身穿一件青绿色连体泳衣，因浸水而颜色略深。\n\n前景中，另一位肤色浅白、深色湿发向后扎起的女性正侧身回眸望向镜头，下身穿着紫色比基尼底裤。她的背部与肩部水光闪烁。神情自信而随意。\n\n画面两侧，其他人部分入镜并被画框裁切：一人正弯曲手臂展示肌肉，另一人手持一个橙色物体，共同强化了即兴、结伴出游的氛围。整张图像毫无摆拍痕迹，自然真实，宛如度假途中抓拍的瞬间快照。肤色表现真实，可见清晰的高光与阴影，无重度修图。\n\n整体情绪轻松自在、充满活力，洋溢着夏日气息与冒险精神。构图略微偏离中心、略显不完美，进一步强化了坦率、真实生活的观感。",
  "scene_type": "在岩石天然水池或洞穴中拍摄的坦率户外旅行快照",
  "subjects": [
    {
      "role": "中心人物",
      "description": "一位肤色浅白、湿漉漉的金色长发向后梳拢的微笑女性，双臂轻松而活泼地高举过头顶",
      "wardrobe": "青绿色连体泳衣，因浸水而颜色略深",
      "pose_and_expression": "活泼、放松、面带欢快笑容"
    },
    {
      "role": "前景人物",
      "description": "一位肤色浅白、深色湿发向后扎起的女性，侧身回眸望向镜头，背部与肩部水光闪烁",
      "wardrobe": "紫色比基尼底裤",
      "pose_and_expression": "神情自信而随意，采用侧肩回眸姿态"
    },
    {
      "role": "侧边/背景人物群",
      "description": "其他人物部分入镜并被画框裁切，增强即兴结伴出游的氛围",
      "details": [
        "一人正弯曲手臂",
        "另一人手持一个橙色物体"
      ]
    }
  ],
  "environment": {
    "setting": "岩石天然水池或洞穴",
    "water": {
      "clarity": "清澈水体",
      "depth": "及腰深度",
      "surface_effects": "轻微水面反光，以及湿润皮肤上细微的微光效果"
    },
    "background": {
      "primary_element": "深色、富有纹理的岩壁",
      "surface_characteristics": "略带湿气、不平整、粗犷的质感",
      "framing": "岩壁占据画面大部分区域"
    }
  },
  "lighting": {
    "type": "自然日光",
    "quality": "柔和但直射",
    "effects": [
      "湿润皮肤上真实可信的高光",
      "可见的自然阴影与立体感",
      "无影棚灯光效果"
    ]
  },
  "composition": {
    "framing": "不完美、略微偏离中心的坦率式构图",
    "cropping": "画面两侧的人物部分入镜并被画框裁切",
    "vibe": "未经摆拍、捕捉瞬间的度假快照"
  },
  "style_and_quality_cues": [
    "自然摄影风格",
    "真实的皮肤质感",
    "无影棚灯光",
    "轻微水面反光",
    "随意、坦率的快照感",
    "纪实摄影 / 旅行摄影氛围",
    "无重度修图",
    "皮肤上可见的高光与阴影"
  ],
  "camera_and_capture_feel": {
    "device": "智能手机或消费级相机",
    "angle": "平视角度",
    "stability": "手持拍摄",
    "sharpness": "轻微柔焦感，无极端锐化",
    "color_and_processing": "自然日光色彩与真实色调，未经过度风格化处理"
  },
  "negative_prompt": "影棚灯光、时装模特姿势、夸张的人体解剖结构、塑料质感皮肤、过度平滑的面部、电影级调色、人工背景、CGI、插画风格"
}
```

</details>

<details><summary><b>奢华美妆产品信息图</b></summary>

```text
扮演一位杂志风格信息图设计师。你擅长将美容护理和化妆品产品的图像转化为奢华且高转化率的信息图。你的任务是：

- 从 ${websiteUrl:eliteprofessionaluae.com} 提取产品描述和使用方法信息。
- 加入 Elite Professional 标志，并保留每个产品的品牌标志。
- 将信息图设计成具有杂志编辑风格、奢华感强，适合在 Instagram 上保存和分享。
- 确保信息图极具说服力，能将观众转化为实际用户。

规则：
- 必须包含从官方网站获取的 Elite Professional 标志。
- 通过使用官方产品标志来保持品牌形象一致性。
- 追求高端奢华的视觉风格，以吸引成熟、讲究的受众。
- 设计时应旨在最大化社交媒体平台（如 Instagram）上的可分享性和互动性。
```

</details>

<details><summary><b>孤独哭泣人像</b></summary>

```text
{
  "image_description": {
    "subject": {
      "type": "年轻女性",
      "appearance": {
        "hair": "齐肩波浪棕发",
        "face": "脸颊微红，泪水湿润，烟熏淡妆，烈焰红唇",
        "expression": "令人心碎的恳求目光直视观众，显而易见的情感重量",
        "physique": "丰满、坚挺且硕大的胸部，曲线优美的双腿，性感而撩人的姿势"
      },
      "clothing": {
        "dress": "极短白色紧身连衣裙，无肩带，无袖，心形领口明显难以包裹其丰满胸部",
        "footwear": "红色漆皮高跟鞋"
      },
      "pose": "全身站立镜头，一只手放在臀部，另一只手轻轻拉扯短裙下摆，既迷人又脆弱的姿态"
    },
    "environment": {
      "setting": "现代昏暗的客厅",
      "foreground": "复杂图案的波斯风格地毯",
      "background": [
        "灰色布艺沙发配有图案靠垫",
        "深色木制咖啡桌，上面有一杯水和一支蜡烛",
        "现代三脚落地灯投射出柔和阴影",
        "远处有深色书架"
      ]
    },
    "technical_specs": {
      "angle": "略微低角度拍摄，以突出高度与存在感",
      "lighting": "来自左侧的柔和定向光，深邃阴影，皮肤和裙面材质上有微妙高光",
      "camera_style": "照片级真实感，电影摄影风格",
      "lens_effects": "浅景深，背景虚化（散景）",
      "quality": "8K分辨率，自然胶片颗粒，高度细致的纹理",
      "aspect_ratio": "9:16（竖屏格式）"
    }
  }
}
```

</details>

<details><summary><b>宁静瑜伽正念摄影</b></summary>

```text
# Serene Yoga & Mindfulness Lifestyle Photography

## 🧘 角色与目的
你是一位专业的**瑜伽与正念摄影专家**。你的任务是创作宁静、平和且具有美感的生活方式图像，捕捉健康、平衡与内在平静的氛围。

---

## 🌅 环境选择
从以下设置中选择**一项**：

### 选项 1：明亮的瑜伽工作室
- 极简主义设计，配有木地板
- 带有飘动的白色窗帘的大窗户
- 柔和的自然光透入
- 干净、令人平静的美学风格

### 选项 2：户外自然环境
- 花园、海滩、森林空地或公园
- 柔和的黄金时段或清晨光线
- 自然景观背景
- 宁静的自然环境

### 选项 3：家庭冥想空间
- 极简风格的房间布置
- 冥想坐垫和柔软的家具
- 植物和蜡烛
- 柔和的环境照明

### 选项 4：健康疗养中心
- 禅意风格的建筑
- 全程使用天然材料
- 大地色系与中性色调
- 宁静、如 sanctuary 般的氛围

---

## 👤 主体规格

### 外观
- **年龄**：20-50 岁
- **表情**：平静、专注、平和
- **肤色**：自然、有光泽的肤质，妆容极简
- **发型**：自然造型——发髻、马尾或披散

### 瑜伽体式（选择一项）
- 🧘 莲花坐（Padmasana）
- 🧘 下犬式（Adho Mukha Svanasan）
- 🧘 山式（Tadasana）
- 🧘 婴儿式（Balasana）
- 🧘 盘腿冥想（Sukhasana）
- 🧘 树式（Vrksasana）

### 或 冥想活动
- 双眼轻闭的呼吸练习
- 轻柔的拉伸与活动训练
- 正念静坐冥想

### 服装
- **类型**：舒适、透气的瑜伽服
- **颜色**：大地色系、白色、柔和的浅色（米色、鼠尾草绿、浅蓝）
- **风格**：极简、飘逸、无束缚感

---

## 🎨 视觉美学

### 照明
- 柔和、温暖、黄金时段的自然光
- 柔和的漫射光（无强烈阴影）
- 专业、讨人喜欢的照明效果
- 全程保持温暖的色温

### 色彩调色板
| 颜色 | Hex Code | 用途 |
|-------|----------|-------|
| 鼠尾草绿 | #9CAF88 | 主要强调色 |
| 暖米色 | #D4B896 | 中性基底色 |
| 天空蓝 | #B4D4FF | 次要强调色 |
| 赤陶色 | #C45D4F | 温暖点缀色 |
| 柔白 | #F5F5F0 | 光源基底色 |

### 构图
- **景深**：柔和的背景虚化（bokeh）
- **焦点**：主体清晰，背景宁静模糊
- **构图**：平衡、居中，留有呼吸空间
- **质量**：照片级真实感、电影感、4K 分辨率

---

## 🌿 可选包含元素

### 道具
- 冥想坐垫（zafu）
- 瑜伽垫（天然材料）
- 植物与花卉（兰花、莲花、竹子）
- 柔和的蜡烛（无香光晕）
- 水晶（紫水晶、白水晶）
- 瑜伽伸展带或毯子

### 天然材料
- 木质纹理与表面
- 石材与泥土元素
- 天然织物（棉、亚麻、大麻）
- 天然光源

---

## ❌ 应避免的内容

- ❌ 明亮、刺眼的荧光照明
- ❌ 杂乱或分散注意力的背景
- ❌ 现代健身房风格或重型设备
- ❌ 人工或塑料感强的元素
- ❌ 面部表情紧张或不适
- ❌ 别扭或不自然的瑜伽体式
- ❌ 强烈阴影与不讨喜的照明
- ❌ 激烈或冲突的色彩
- ❌ 繁杂、分散注意力的背景元素
- ❌ 现代科技或数字设备

---

## ✨ 质量标准

✓ **专业健康摄影品质**  
✓ **温暖、亲切、易接近的美学风格**  
✓ **真实、自然（非摆拍）的感觉**  
✓ **包容性表现**  
✓ **适用于印刷与数字用途**

---

## 📱 适用场景
- 瑜伽工作室网站与营销材料
- 健康类 App 封面图
- 冥想与正念博客
- 疗养中心宣传
- 社交媒体健康内容
- 心理健康与自我关怀资料
- 印刷材料（海报、宣传册、传单）
```

</details>

<details><summary><b>宁静秋日湖畔</b></summary>

```text
{
  "colors": {
    "color_temperature": "warm",
    "contrast_level": "medium",
    "dominant_palette": [
      "red",
      "light blue",
      "orange",
      "grey",
      "black"
    ]
  },
  "composition": {
    "camera_angle": "wide shot",
    "depth_of_field": "deep",
    "focus": "秋日树木及其在湖中的倒影",
    "framing": "构图适配 1:1 正方形格式，主要视觉重心的树木位于右侧，左侧由一名小渔夫平衡。水中的倒影在正方形画框内形成强烈的垂直对称。"
  },
  "description_short": "一幅宁静的插画，描绘一个人独自在平静的湖边垂钓，周围是鲜艳的红色和橙色秋叶树木，其色彩倒映在平静的水面上。",
  "environment": {
    "location_type": "landscape",
    "setting_details": "秋日雾气弥漫的一天，宁静的湖畔。湖岸由小石块组成，岸边生长着茂盛的秋叶植物。远处，一片林木覆盖的小山被薄雾部分遮蔽。",
    "time_of_day": "morning",
    "weather": "foggy"
  },
  "lighting": {
    "intensity": "moderate",
    "source_direction": "ambient",
    "type": "soft"
  },
  "mood": {
    "atmosphere": "宁静而沉思的秋日",
    "emotional_tone": "calm"
  },
  "narrative_elements": {
    "character_interactions": "一个孤独的身影正安静地垂钓，营造出与自然和平互动的氛围。",
    "environmental_storytelling": "鲜艳的深秋色彩与完全静止、如镜面般的水面，暗示着自然之美与宁静的短暂瞬间。孤独的渔夫强化了孤独与静思的主题。",
    "implied_action": "此人正在耐心垂钓，暗示着安静的等待与缓慢流逝的时间。"
  },
  "objects": [
    "autumn trees",
    "lake",
    "fisherman",
    "fishing rod",
    "rocks",
    "forest",
    "sky"
  ],
  "people": {
    "ages": [
      "adult"
    ],
    "clothing_style": "casual outdoor wear",
    "count": "1",
    "genders": [
      "unknown"
    ]
  },
  "prompt": "一幅美丽的数字插画，描绘宁静的秋日风景，采用 1:1 正方形格式。一名孤独的渔夫站在岩石湖岸上，面对平静如镜的湖面。右侧，枝叶繁茂的树木挂着火红与橙色的秋叶，垂向水面，其完美的倒影清晰映照于水中。构图在正方形画框内保持平衡，渔夫位于左侧，树木位于右侧。背景是淡蓝色天空下远处朦胧的山丘。艺术风格极简而富有图形感，采用平涂色彩与微妙纹理，传达出宁静而沉思的氛围。Ryo Takemasa 风格的艺术作品。",
  "style": {
    "art_style": "minimalist illustration",
    "influences": [
      "Japanese woodblock prints",
      "graphic design"
    ],
    "medium": "digital art"
  },
  "technical_tags": [
    "illustration",
    "minimalism",
    "landscape",
    "autumn",
    "reflection",
    "serenity",
    "flat color",
    "graphic design",
    "lakeside",
    "fishing",
    "square format",
    "1:1 aspect ratio"
  ]
}
```

</details>

<details><summary><b>定制海报与壁纸设计</b></summary>

```text
扮演一位专业的数字艺术家。你将创建一张具有卓越渲染质量的海报或壁纸。此过程需要用户上传一张作为设计基础的图片。请要求用户提供他们希望在海报中呈现的角色或人物设定。

你需要：
- 分析用户上传的图片，评估其风格与构图。
- 结合指定的角色，渲染生成一张海报或壁纸。
- 确保设计视觉效果出众，并具备高分辨率。

规则：
- 用户必须上传一张图片。
- 在开始设计前，必须与用户确认角色细节。
```

</details>

<details><summary><b>宝可梦大师换脸</b></summary>

```text
Take the input image, and use it is face and apply it to be Ash the Pokemon master image with his favorite character pikachu.
```

</details>

<details><summary><b>室内局部重绘参考提示词</b></summary>

```text
基于提供的参考图像，生成一个奢华温暖的室内场景。保持精确的构图、比例和摄像机角度。

厨房吧台：
	•	台面必须严格使用所提供的大理石参考图像。
	•	精确匹配颜色、纹理、纹路以及相对于吧台的实际比例。
	•	不得进行风格化、修改或重新诠释大理石材质。
	•	大理石应与吧台边缘、反射和环境照明自然融合。

吧台基座：温暖的天然木材。

装饰墙：浅灰色垂直条纹包覆，采用完全圆润的圆柱形轮廓（圆形，非方形，无锐利边缘）。

墙面划分：
	•	垂直方向：
	•	上部区域：占据墙面高度的上2/3，条纹直径为0.5 cm
	•	下部区域：占据墙面高度的下1/3，条纹直径为1 cm
	•	水平方向（沿墙面宽度）：
	•	上部区域覆盖墙面宽度的前三分之二
	•	下部区域覆盖剩余的三分之一
	•	过渡平滑，间距精确，符合建筑准确性。

地板：抛光白色卡拉拉大理石（Carrara marble）。
温暖的环境照明，柔和的间接隐藏光源，营造舒适而奢华的意大利风格高端室内空间。超现实主义建筑可视化。

AI 严格指令：精确匹配材质，完全遵循参考图像，保持比例，不得重新诠释或创建新图案，大理石必须在尺度上显得自然且真实。

⸻

Midjourney / 图像修复参数：

--v 6 --style raw --ar 3:4 --quality 2 --iw 2 --no artistic interpretation
```

</details>

<details><summary><b>家庭卡通贴纸</b></summary>

```text
{
  "prompt": "你将使用所提供照片中的人物作为主要主体进行图像编辑。面部必须保持清晰且不被修改。创作一幅可爱、幽默的卡通贴纸设计，描绘爸爸专注地编程，宝宝开心地干扰他的工作，妈妈则在一旁愉快地阅读，观察这 playful chaos。强调柔和的圆润线条、鲜艳的色彩以及夸张而迷人的表情，适合用于笔记本电脑贴纸。",
  "details": {
    "year": "当代（当前时代）",
    "genre": "卡通 / 奇想风 / 家庭幽默 / 可爱贴纸艺术",
    "location": "一个舒适、略带风格化的家庭环境——可能是客厅或家庭办公室。背景元素极简且柔和：一张舒适的扶手椅、一台显示抽象代码行的发光笔记本电脑屏幕，以及地板上可能有一个小而多彩的玩具。整体环境感觉温暖而宜人。",
    "lighting": "柔和、漫射的室内灯光，设计得明亮清晰，没有强烈的阴影，类似于儿童绘本插图。所有内容都充分照明以确保清晰度。",
    "camera_angle": "中等近景，聚焦于三位主体及其互动。构图应紧凑且呈圆形（或易于裁剪为圆形），适合贴纸使用，三位人物均需突出。（1:1 构图）",
    "emotion": "爸爸：滑稽地慌乱/专注；宝宝：快乐/顽皮；妈妈：宁静/ amused。",
    "costume": "简化、舒适的家居服饰。爸爸穿着带有微妙科技元素的图案T恤，妈妈穿着柔软的毛衣或衬衫，宝宝穿着可爱的印花连体衣或简单的婴儿服装。颜色明亮友好。",
    "color_palette": "由柔和的粉彩色调与更明亮、吸引人的色彩混合而成的欢快宜人配色方案。例如温暖的黄色、柔和的蓝色、薄荷绿色和玫瑰粉色。轮廓鲜明、干净。",
    "atmosphere": "温暖、充满爱意且 playful chaotic。捕捉有小孩子的日常生活中的日常幽默，强调喜悦与轻微的干扰。",
    "subject_expression": "爸爸：一只眉毛因沮丧而抬起，或略带喜剧性的痛苦表情，眼睛睁大但仍紧盯着屏幕，嘴巴微张呈现轻柔的‘哦不’表情。宝宝：睁大无辜而快乐的眼睛，张着嘴大笑或发出开心的咿呀声。妈妈：温柔而会心的微笑，眼角微微皱起，看着这一幕，或许正从书中抬头，面带甜美 amused 的表情。",
    "subject_action": "爸爸坐着，弯腰俯在笔记本电脑上，手指悬停在键盘上方。宝宝坐在他腿上或肩膀上，顽皮地伸手去够键盘，或轻轻拉扯他的头发/眼镜。妈妈舒适地坐在附近，手中捧着一本打开的书，从书中抬头望向爸爸和宝宝，目光温暖而幸福。",
    "environmental_elements": "风格化、简洁的元素：笔记本电脑屏幕上显示发光的‘错误’消息或抽象代码。桌上放着一个看似无辜的小婴儿玩具（例如摇铃或积木），稍微超出触及范围。妈妈的书本旁飘出 cheerful 的‘Zzzzz’，或周围有小心心/星星，象征她平静的状态。整个设计具有干净、粗犷的轮廓，非常适合用作贴纸。"
  }
}
```

</details>

<details><summary><b>家电展厅卡通争吵场景</b></summary>

```text
一个有趣的 3D 卡通场景，位于现代 Fresh 电器的展厅内。一台 Fresh 电风扇、一台 Fresh 空气冷却器和一台 Fresh 微波炉正像人类角色一样激烈而搞笑地争吵着。

Fresh 电风扇自豪地旋转着说：“我是夏日的超级明星！天气一热，大家就抢着来买我！”

Fresh 空气冷却器自信地微笑着回应：“别得意！我可不只是吹风……我真能降温！”

Fresh 微波炉突然插话，内部亮起光芒：“拜托！你们只在夏天受欢迎，而我全年无休——冬天、夏天，甚至斋月期间都在工作！”

电风扇笑道：“也许吧，但人们可会躲你的热气！”

微波炉回击道：“你们一停电就立刻罢工！”

空气冷却器举起双手说道：“喂喂喂……我们可都是 Fresh 家族的产品。真正的问题是顾客根本决定不了该先买我们中的哪一个！”

高度细致的 3D 卡通风格，表情丰富滑稽，色彩缤纷的展厅，漫画式对话气泡，轻松活泼的氛围，专业灯光，超写实渲染，幽默且适合全家观看的广告风格，高品质。
```

</details>

<details><summary><b>对话式 Logo 设计</b></summary>

```text
设计一个对话式流程，为用户的项目创建一个极简标志，利用其品牌颜色：#3a7eab、#cf4832 和 #d1d3d4。首先提出一组 10 个精心设计的是否问题，以澄清项目目标、目标受众、美学风格和设计偏好。收到回答后，评估是否需要进一步细节——如果需要，则继续提出有针对性的是否跟进问题，直到充分明确项目的性质和用户的期望为止。只有在收集到所有必要信息后，才使用所收集的回答作为推理步骤，生成详细的标志概念简报。

请求与推理顺序：
- 所有关于标志方向的推理、推导和理由必须在最终结论之前记录。
- 最终结论（标志简报/概念）必须始终出现在推理之后。
- 如果提供示例，始终先展示问答（推理），再展示最终标志概念。

流程步骤：
- 首先说明目标（使用指定的品牌颜色创建一个极简标志）。
- 提出 10 个依次进行的、深思熟虑的是否问题，旨在揭示关键细节（例如：项目领域、情绪氛围、几何/有机形状偏好、是否使用缩写字母、目标受众等）。
- 在每组答案之后，评估哪些内容尚不清晰。如有模糊或不完整的信息，需提出直接且相关的是否跟进问题。
- 一旦所有重要标准都已明确，总结引导出标志设计建议的推理过程（列出答案，陈述关键要点，解释这些如何影响你的建议）。
- 将极简标志概念作为最终输出——用简洁清晰的语言描述其视觉元素（非图像形式），引用选定的颜色，并将概念与推理步骤联系起来。

输出格式：
- 逐轮对话，始终根据先前的回答决定下一个问题，直到掌握足够信息。
- 在问答阶段结束时，输出一个 JSON 对象，包含两个主要字段：
  - "reasoning_steps"：一个有序列表，概述每个答案及从中得出的推论。
  - "logo_concept"：一段清晰简洁的文字，描述提议的极简标志（视觉元素、形状、颜色使用及其理由）。

示例（为说明而缩短；实际交流可能更长且更复杂）：

示例问答交换：
Q1: 您的项目是否与科技相关？  
A1: 是。  
Q2: 您品牌的氛围是否比严肃更偏向 playful（活泼）？  
A2: 否。  
...（根据需要继续提问和跟进）

最终输出示例：
{
  "reasoning_steps": [
    "项目与科技相关：表明应采用干净、结构化的符号。",
    "品牌氛围是严肃的：倾向于锐利线条和极简、非活泼的形式。",
    "偏好几何形状而非有机形状：将使用严格的几何结构。",
    "希望包含首字母：将考虑风格化的字母设计。"
    //... 根据相关情况进一步推理
  ],
  "logo_concept": "一个使用首字母以几何方式相互连接排列的极简标志。主色 #3a7eab 构成基础，辅以 #cf4832 的强调线条和 #d1d3d4 的微妙高光。设计干净利落且严肃，反映科技背景和品牌形象。"
}

重要提示：
- 在给出标志概念前，必须展示所有推理和中间思考过程。
- 若关键信息缺失或模糊，持续提出跟进问题。
- 最终描述段落（logo_concept）必须清晰、简洁，并具有视觉感。

---

重要提醒：  
通过是否问题持续收集项目信息，在给出标志概念前展示你的推理过程，并始终遵循输出的 JSON 结构。
```

</details>

<details><summary><b>导演风格九宫格</b></summary>

```text
创建一张单幅 3x3 网格图像（正方形，2048x2048，高细节）。  
中心图块（第 2 行，第 2 列）必须是上传的参考电影剧照的精确原图，不得有任何更改。不得重新诠释、重绘、重新打光、调色、裁剪、重新构图、风格化、锐化、模糊或以任何方式变换。必须完全保持原始状态。

导演识别规则  
如果上传的电影剧照的导演属于以下列出的 8 位导演之一，则该导演对应的图块必须是原始中心图块的完全复制品，不得有任何更改（相同的图像内容、相同的构图、相同的颜色、相同的光照、相同的纹理）。仅应用标签。  
其余图块遵循正常的重拍规则。

网格规则  
9 个等大图块组成整洁的 3x3 布局，图块之间为细而均匀的间隙。  
每个图块的左上角有一个简洁易读的标签，字体和大小一致，高对比度，无扭曲。  
中心图块标签：ORIGINAL  
其他图块标签必须完全如下：  
Alfred Hitchcock  
Akira Kurosawa  
Federico Fellini  
Andrei Tarkovsky  
Ingmar Bergman  
Jean-Luc Godard  
Agnès Varda  
Sergio Leone  
不得添加其他文字、标志、字幕或水印。  
保持 3x3 对齐完全笔直整洁。

身份与性别锁定（适用于所有非 ORIGINAL 图块）  
- 以原始中心图块作为每个人身份的唯一真实来源。  
- 保持人物数量及其角色/位置完全一致（不得互换人物身份）。  
- 不得更改任何人物的性别或性别呈现。禁止性别互换、性别转换、跨性别选角。  
- 保持每个人的关键身份特征一致：面部结构、发型长度/类型、面部毛发（不得出现或消失）、化妆程度（不得出现或消失）、身体比例、年龄范围、肤色以及显著特征（痣/疤痕/眼镜）。  
- 不得将一个人变为另一个人。不得融合面孔。不得将一个人拆分为两人。不得在不同人物间复制同一张脸。  
- 若任何身份属性模糊，应默认与原始图块完全一致。  
- 允许的更改仅限于每位导演的电影化处理：构图、镜头感、摄像机高度、景深、光照、调色、对比曲线、纹理、氛围和场景强调。身份必须锁定不变。  
禁止项：性别互换、女性化/男性化处理、添加/移除胡须、添加/移除口红、大幅改变发长、面部替换、身份漂移。

角色锚定  
- 人物 A = 原始图中最左侧人物，人物 B = 原始图中最右侧人物，人物 C = 原始图中居中/靠后人物，依此类推。  
- 每个图块必须保持人物 A/B/C 为相同个体（相同性别呈现和身份），仅进行电影化重拍。

内容规则（适用于非复制图块）  
所有图块之间需保持可识别的连续性（人物/地点/事件）。不得将身份变为不同人物。  
按导演差异调整：构图、镜头感、摄像机高度、景深、光照、色彩调性、对比曲线、纹理、美术设计强调、氛围。  
超清晰电影剧照（除非指定使用柔焦），光照一致，解剖结构正确，无重复面孔，无扭曲的手部，无透视错误，无故障伪影，标签清晰可读。

导演专属风格与色彩分级（每个图块强烈应用相应风格，除非适用复制规则）

Alfred Hitchcock  
调色板：低饱和中性色、冷灰、病态绿、深黑，偶尔点缀饱和红色。  
对比度：高对比度，锐利且充满悬疑感的阴影。  
纹理：经典的 35mm 清晰质感，紧张氛围。  
镜头/景深：35–50mm，控制景深，精确几何构图。  
布光/调度：受黑色电影影响的实用光源，硬光主光，窥视感构图，心理张力。

Akira Kurosawa  
调色板：泥土质感的低饱和棕/绿色；若有彩色则主色克制。  
对比度：强烈的色调分离，有力的黑色表现。  
纹理：粗粝的胶片颗粒，可触感元素（泥、雨、风）。  
镜头/景深：24–50mm，深焦，动态场面调度与强烈几何构图。  
布光/氛围：戏剧性的自然光，天气作为设计元素（雾、雨痕、逆光）。

Federico Fellini  
调色板：温暖琥珀色、嘉年华红色、奶油高光、粉彩色点缀。  
对比度：中等对比度，梦幻辉光与柔和泛光。  
纹理：柔焦扩散，戏剧化超现实光泽。  
镜头/景深：标准至广角，舞台化构图，丰富的背景布景。  
布光：表现力强，舞台感， whimsical yet melancholic mood（俏皮而忧郁的氛围）。

Andrei Tarkovsky  
调色板：低饱和的棕褐/橄榄色、冷青灰、低饱和度、陈旧色调。  
对比度：低至中等，柔和的高光过渡。  
纹理：有机颗粒感，雾气弥漫，水渍，老化表面。  
镜头/景深：50–85mm，沉思式构图，自然主义景深。  
布光/氛围：窗光，阴天感，诗意元素（雾、雨、烟），静谧张力。

Ingmar Bergman  
调色板：近乎单色的克制风格，冷灰、苍白肤色，极少色彩干扰。  
对比度：高对比度，面部轮廓分明，深邃阴影。  
纹理：干净、亲密、心理聚焦。
Lens/DOF：50–85mm，构图更紧凑，浅至中等景深。  
Lighting：主光强烈，明暗衰减明显，营造情感浓烈的肖像效果。

让-吕克·戈达尔  
Palette：中性色中点缀鲜明的三原色（红/蓝/黄），或刻意使用平淡的自然色调。  
Contrast：中等对比度，偶尔出现轻微过曝的高光。  
Texture：16mm/35mm胶片的粗粝质感，不完美却充满生命力。  
Lens/DOF：广角镜头，即兴的非中心构图。  
Lighting：呈现自然光感，街头/霓虹/实用光源，具有纪录片式新浪潮的即时感。

阿涅丝·瓦尔达  
Palette：温暖的自然日光，柔和的粉彩色调，真实的肤色表现，微妙的互补色。  
Contrast：中等对比度，柔和且具亲和力。  
Texture：可感知的生活化真实质感，细微的胶片颗粒。  
Lens/DOF：28–50mm，环境人像构图，保留场景背景信息。  
Lighting：自然主义风格，以人为本，亲密而不封闭的氛围。

赛尔乔·莱昂内  
Palette：阳光炙烤的金色、尘土飞扬的橙色、棕褐色、深邃阴影，偶尔点缀青绿色天空。  
Contrast：高对比度，强烈日光，明显的剪影效果。  
Texture：粗粝的尘土、汗水、皮革、风化表面，颗粒感显著。  
Lens/DOF：极广角（24–35mm）与极端特写并用；浅景深聚焦于眼睛/细节。  
Lighting/Mood：硬光照明，轮廓光，歌剧式张力，标志性的戏剧性阴影造型。

Output：仅输出一张最终的 3x3 网格图像。
```

</details>

<details><summary><b>小狗打高尔夫视频</b></summary>

```text
一部电影感十足的 9:16 竖屏视频，采用皮克斯（Pixar）风格基调，描绘一群卡通化的狗狗在明亮多彩的高尔夫球场上欢乐地打高尔夫。一只主要狗狗位于画面中央，直立站立，比例夸张，正处在挥动高尔夫球杆的瞬间，脸上带着兴奋的大笑容，而他的狗狗朋友们则以富有表现力的面部表情作出反应——欢呼、惊呼，或拿着迷你高尔夫配件。摄像机位于略低的角度，正对主角角色。角色动画流畅而富有玩趣，带有微妙的挤压与拉伸效果。温暖而充满活力的灯光，柔和的阴影，以及丰富饱和的色彩。背景略微虚化，呈现风格化的树木与云朵。镜头缓慢平稳地推近。无文字叠加，无人类出现——仅聚焦于狗狗们欢乐温馨的高尔夫时刻，细节清晰，眼神富有表现力，洋溢着轻松愉快的皮克斯式魅力。时长：10 秒。
```

</details>

<details><summary><b>小鸡破壳特写</b></summary>

```text
鸡蛋破裂的极端特写，稻草上的蛋壳纹理极度细致。刚孵化出的无羽毛小鸡，皮肤湿润、布满皱纹，呈粉红色。14mm超广角镜头带来戏剧性透视，超现实8K风格，电影级氛围。--ar 9:16
```

</details>

<details><summary><b>屋顶日落回眸半身照</b></summary>

```text
{
  "category": "ROOFTOP_SUNSET_LOOKBACK",
  "subject": {
    "demographics": "成年女性，21–27 岁，土耳其人相貌。",
    "hair": {
      "color": "深棕色",
      "style": "松散波浪卷，略带微风拂过感",
      "texture": "发丝清晰可见，面部周围有细碎飞发",
      "movement": "发丝被微风轻微扬起"
    },
    "face": {
      "shape": "柔和椭圆脸型",
      "eyes": "目光强烈却友善，直视镜头",
      "makeup": "自然轻奢妆效，水润肌肤，眼线细腻",
      "skin_details": "毛孔可见，真实光泽感，无磨皮处理"
    },
    "clothing": {
      "outfit": "极简黑色穿搭，外搭轻薄夹克（无文字/标识）",
      "fabric": "真实织物纹理，手肘处有自然褶皱"
    },
    "accessories": {
      "jewelry": ["小巧银色耳环"]
    }
  },
  "pose": {
    "type": "半身倚靠栏杆姿势",
    "orientation": "身体侧向远离镜头，头部转向后方直视相机",
    "head_position": "头部微微倾斜，下巴放松",
    "hands": "一只手自然搭在栏杆上，手指姿态自然",
    "gaze": "回眸对视，略带微妙笑意",
    "posture": "放松而自信"
  },
  "setting": {
    "environment": "屋顶场景，远处可见城市天际线",
    "background_elements": [
      "黄金时刻阳光光晕",
      "城市灯光初亮（散景效果）",
      "栏杆纹理清晰可见"
    ],
    "depth": "强烈景深分离：主体锐利清晰，天际线呈柔美散景"
  },
  "camera": {
    "shot_type": "半身人像",
    "angle": "平视或略低视角",
    "focal_length_equivalent": "35–50mm 编辑风格（或 26mm 手机变体）",
    "framing": "4:5 构图，主体偏构图中心",
    "focus": "双眼锐利清晰，背景呈奶油般柔焦散景"
  },
  "lighting": {
    "source": "黄金时刻阳光 + 微弱补光",
    "direction": "温暖轮廓光勾勒发丝与脸颊边缘",
    "highlights": "可控光晕，自然肌肤高光",
    "shadows": "柔和阴影，电影级层次分离"
  },
  "mood_and_expression": {
    "tone": "静谧奢华，自信从容",
    "expression": "浅淡笑意，沉静而富有张力",
    "atmosphere": "温暖、电影感、即兴自然"
  },
  "style_and_realism": {
    "style": "照片级写实风格，融合社交平台与杂志编辑质感",
    "fidelity": "发丝与肌肤细节高度还原，无平滑处理"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "轻微噪点",
    "motion_blur": "仅发梢处呈现极细微动态模糊"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "虚假天际线", "CGI 光晕", "塑料感肌肤",
    "多余手指", "扭曲变形的栏杆",
    "可读文字", "标识", "水印"
  ]
}
```

</details>

<details><summary><b>屋顶泳池黄昏人像</b></summary>

```text
{
  "pack_name": "BOLD - Rooftop Inferno / Golden Hour",
  "intent": "生成一张超写实、自然抓拍风格的 iPhone 式屋顶泳池人像，展现主导、自信的能量与杂志级质感，但不显得刻意摆拍或影棚布光。",
  "content_safety": {
    "age_requirement": "所有主体必须为成年人，21岁以上。",
    "nudity_level": "非暴露内容。仅限泳装。不可见乳头、乳晕或生殖器。不得有透明材质暴露敏感解剖结构。",
    "tone": "以自信为核心，不得色情。允许具有杂志感的‘吸睛陷阱’氛围，但需保持品位，不露骨。",
    "no_minor_look": true
  },
  "global_style_quality": {
    "photography_style": "RAW 抓拍风格的 iPhone 摄影",
    "realism": "超写实，强调质感，可见毛孔与自然皮肤细节",
    "resolution_hint": "8K 视觉效果（高细节、清晰纹理，非人工锐化）",
    "grading": "自然但受强光影响的高对比度，极少风格化处理，避免电影感的青橙色调",
    "retouching": "不进行重度修图，不出现塑料感皮肤，保留微纹理",
    "vibe": "网红与杂志风格融合，高端但未经滤镜修饰",
    "overall_mood_keywords": [
      "大胆",
      "主导",
      "无拘无束",
      "永恒",
      "高互动性",
      "值得截屏",
      "自信胜于性感"
    ]
  },
  "scene_setting": {
    "location_type": "豪华屋顶泳池",
    "key_background_elements": [
      "城市天际线",
      "玻璃栏杆",
      "无边泳池",
      "极少人群",
      "静谧奢华氛围"
    ],
    "time_of_day": "日落转入黄金时刻，带有火焰色调",
    "atmosphere_details": [
      "空气中仍残留热感",
      "太阳正在下落但仍炽热",
      "泳池水面泛着橙蓝光芒",
      "下方城市传来低沉嗡鸣",
      "远处城市灯光开始亮起"
    ],
    "crowd_control": {
      "crowd_level": "极少",
      "extras_behavior": "若有其他人物出现，必须处于远处、模糊且不引人注意。整体场景应传达出奢华的静谧感。"
    }
  },
  "subject": {
    "type": "单一主要人物",
    "gender_presentation": "女性化",
    "age": "成年人，21岁以上",
    "build": "运动型，女性力量感体型",
    "body_characteristics": {
      "waist": "纤细腰部，可见核心肌群收紧",
      "upper_body": "肩部与手臂线条分明，姿态挺拔",
      "legs": "通过姿势突出修长腿部线条",
      "pose_energy": "身体占据空间，稳重而具主导感"
    },
    "face": {
      "eyes": "大而自信的眼睛，直视或半眯眼凝视",
      "expression": "冷静、主导、无拘无束，不带表演性微笑",
      "freckles": "强光下可见轻微雀斑",
      "lips": "自然饱满的嘴唇，放松但坚定",
      "emotion_keywords": [
        "冷静主导",
        "毫无歉意的能量",
        "我知道这看起来怎样"
      ]
    },
    "skin": {
      "undertone": "浅中性肤色",
      "finish": "防晒霜叠加自然油光质感",
      "texture": "可见毛孔与真实微纹理",
      "highlights": "肩膀与锁骨处有阳光亲吻的高光",
      "avoid": [
        "过度平滑的脸部",
        "瓷质皮肤",
        "美颜滤镜模糊效果"
      ]
    },
    "hair": {
      "color": "深棕色",
      "style": "因炎热向后紧贴，略带湿润感",
      "mess_level": "可控的凌乱",
      "detail": "几缕松散发丝捕捉到黄金光线"
    },
    "tattoos": {
      "requirement": "胸部纹身必须完全可见且不作更改",
      "integrity_rules": [
        "不得修改纹身形状、线条、位置或密度",
        "不得添加新纹身",
        "不得移除纹身",
        "不得镜像翻转纹身，除非相机/镜面逻辑需要，即便如此也必须精确保留原设计"
      ],
      "role_in_styling": "纹身作为珠宝使用"
    }
  },
  "wardrobe": {
    "outfit": "黑色系带比基尼",
    "top": {
      "type": "小三角罩杯",
      "fit": "系带紧致，布料极少",
      "notes": "保持遮盖得体且不露骨；不得暴露乳头或乳晕。"
    },
    "bottom": {
      "type": "高腰剪裁底裤",
      "style": "80年代高胯设计",
      "notes": "保持得体构图；避免暴露过度。"
    },
    "styling_priority": "布料极简，表达最大化，自信胜于性感"
  },
  "scene_setup": {
    "position": "站立于泳池边缘",
    "stance": [
      "一只脚略微前伸",
      "臀部轻微偏移",
      "肩膀打开",
      "胸部前挺",
      "下巴微低或中性以体现主导感"
    ],
    "body_language": [
      "占据空间",
      "稳重",
      "坚定",
      "非为影棚拍摄摆姿，而是自然流露的力量感"
    ]
  },
  "props_flatlay_feel": {
    "required_props": [
      "手中握着太阳镜（未佩戴）",
      "画面中可见手机，作为自拍证据"
  
      "湿毛巾自然折叠在附近"
    ],
    "optional_props": [
      "一个极简风格的饮品杯放置在画面一侧远处（低调、奢华感，非派对氛围）"
    ],
    "prop_rules": [
      "道具上不可出现任何可见的品牌标识或徽标",
      "手机屏幕不可显示文字",
      "毛巾看起来应自然潮湿，而非刻意摆拍"
    ]
  },
  "camera_capture": {
    "camera_type": "智能手机",
    "phone_reference": "iPhone 风格拍摄，广角镜头质感",
    "lens_equivalent_mm": "24-28mm 等效（手机广角）",
    "preferred_feel": [
      "手持感",
      "轻微微震真实感",
      "适度柔化，非极致锐利",
      "高动态范围但不过度 HDR"
    ],
    "angle": {
      "primary": "低角度以营造强势主导感",
      "tilt": "轻微荷兰式倾斜，微妙而非夸张",
      "distance": "足够近以感受存在感，但不局促"
    },
    "framing": {
      "primary_crop": "从大腿中部至头部（主导性人像构图）",
      "alternate_crop": "腰部以上英雄式裁剪（纹身完整可见）",
      "composition_notes": [
        "人物剪影与天空形成强烈对比",
        "城市天际线可见但为次要元素",
        "无边泳池边缘线条干净且显高端",
        "玻璃栏杆增添奢华几何感"
      ]
    },
    "focus": {
      "subject_priority": "面部、纹身和皮肤纹理细节最清晰",
      "background": "天际线略柔和，可辨识但不干扰主体",
      "avoid": "避免看起来像单反相机造假的人工虚化；保持手机拍摄般的景深效果"
    }
  },
  "lighting": {
    "type": "强烈自然光，高对比度",
    "time_window": "金色时刻，带有炽热色调",
    "sun_behavior": {
      "sun_position": "太阳位置偏低，位于人物后方或侧后方，形成轮廓光",
      "lens_flare": "有意让阳光直射镜头产生光晕",
      "flare_intensity": "中等强度，可控，不致冲淡主体"
    },
    "skin_highlights": [
      "肩膀上有明亮高光",
      "锁骨处捕捉到光线",
      "防晒霜与天然油脂带来的细微镜面光泽"
    ],
    "shadow_character": "阴影清晰但不压黑；保留阴影中的纹理细节",
    "avoid": [
      "影棚灯光",
      "柔光箱反光",
      "平面化美容灯光"
    ]
  },
  "rendering_rules": {
    "must_have": [
      "真实可见的皮肤毛孔与微纹理",
      "织物张力与细绳行为自然",
      "水面反射微妙且可信",
      "高端屋顶材质（玻璃、石材、泳池边缘）具备真实镜面高光"
    ],
    "must_avoid": [
      "CGI 外观",
      "插画风格",
      "塑料感皮肤",
      "过度平滑的面部",
      "夸张的解剖结构",
      "不真实的比例",
      "多余的肢体或扭曲的手部",
      "虚假纹身或纹身偏移"
    ],
    "imperfection_cues": [
      "轻微手持构图不完美",
      "皮肤上有细小水珠",
      "几缕飘散的发丝",
      "毛巾上有细微褶皱"
    ]
  },
  
"prompt_text_master": "奢华屋顶泳池黄金时刻的超写实、自然 candid 风格 iPhone 拍摄人像，背景为炽热的日落色调。低角度主导视角，带有轻微荷兰倾斜，手持拍摄的真实感，轻微柔化效果如同真实手机照片，呈现高端无滤镜、注重纹理的视觉风格。画面中为一名成年女性（21岁以上），健美而富有女性力量感的体型，纤细腰身伴随核心紧绷，肩部与手臂线条分明，站姿突出修长腿部线条。表情冷静、强势、毫不在意，目光直接或半眯眼，不带表演性微笑，嘴唇自然放松但具主张力。强烈阳光下可见轻度雀斑。肤色为浅色中性底色，带有 SPF 防晒光泽与自然油脂反光，毛孔可见，微小肌肤纹理真实，肩部与锁骨处有阳光亲吻的高光，阴影清晰但未丢失细节。发色为深棕色，因炎热向后贴服，略湿且呈现受控的凌乱感，几缕松散发丝捕捉到金色光线。她站立于泳池边缘，一只脚微微前伸，臀部轻微偏移，肩膀打开、胸部前挺，身体姿态占据空间。穿着黑色系带上装比基尼：小型三角上衣配紧绷绳结，高腰 80 年代风格下装，极简但得体，非暴露式覆盖。胸部纹身必须完全可见，且形状、位置、线条与密度保持不变，纹身作为珠宝存在。场景为带玻璃栏杆的无边屋顶泳池，背后是城市天际线，人群稀少，呈现奢华静谧氛围。城市灯光开始微妙亮起。泳池水面反射出橙蓝色日落光影。道具：手中握着太阳镜（未佩戴），画面内可见手机作为自拍证据，附近折叠着一条湿毛巾，无品牌标识，手机屏幕无文字。 lighting：强烈的自然阳光，高对比度，有意的镜头光晕照射到镜头上，可控的光晕增添热度但不冲淡面部或纹身细节。构图：以天空为背景形成强烈剪影，天际线为次要元素，栏杆与泳池边缘呈现高级几何线条。最终情绪：冷静的支配感，沉稳的力量，自信超越性感，具有杂志级吸引力陷阱效果，大胆、永恒、高互动性的快照氛围。",
  "negative_prompt_master": "影棚灯光，柔光箱，环形灯反光，时尚广告姿势，过度摆拍的模特气息，夸张的解剖结构，不现实的比例，额外肢体，扭曲的手部，塑料质感皮肤，过度磨皮的面部，瓷娃娃外观，重度美颜滤镜，CGI，插画，动漫，绘画风格，人工背景，绿幕感，电影级青橙调色，过度HDR，文字，水印，标志，品牌标记，裸露，乳头，乳晕，生殖器明显可见，透视曝光，未成年，孩童特征，娃娃脸，诡异的眼睛，死板的眼神，过度锐化的微对比度，不真实的散景，对称纹身错误，纹身变形，纹身移除，新增纹身",
  "output_formats": [
    {
      "use_case": "Instagram feed editorial",
      "aspect_ratio": "4:5",
      "resolution_hint": "2160x2700 或更高",
      "framing": "从大腿中部到头部，上背景可见天际线，纹身居中"
    },
    {
      "use_case": "Stories/Reels thumbnail",
      "aspect_ratio": "9:16",
      "resolution_hint": "2160x3840 或更高",
      "framing": "腰部以上英雄构图，纹身完全可见，更强的镜头光晕线条"
    },
    {
      "use_case": "Square profile post",
      "aspect_ratio": "1:1",
      "resolution_hint": "2048x2048 或更高",
      "framing": "紧凑的腰部以上构图，主导性凝视，城市背景简化为最小散景"
    }
  ],
  "variants": [
    {
      "variant_name": "V1 - 最大化支配感，光晕可控",
      "changes_from_master": [
        "略微增强低角度效果",
        "保持光晕适中且干净，不冲淡面部细节",
        "让天际线略清晰但仍为次要元素"
      ],
      "prompt_addendum": "略微加强低角度权力构图，确保纹身完全清晰可辨，光晕控制得当避免面部泛白。"
    },
    {
      "variant_name": "V2 - 热浪质感升级，更具 candid 不完美感",
      "changes_from_master": [
        "仅在背景中引入轻微热浪 shimmer 效果",
        "在锁骨与肩部添加微小水滴",
        "手持拍摄的不完美感略增强"
      ],
      "prompt_addendum": "在背景中加入轻微热浪波动，肩部与锁骨上的微小水滴捕捉阳光，手持构图略显不完美，如同真实瞬间抓拍。"
    },
    {
      "variant_name": "V3 - 城市灯光亮起强调版",
      "changes_from_master": [
        "更明显可见的城市灯光开始亮起",
        "天空渐变更略暗",
        "保持主体曝光正确，避免 HDR 效果"
      ],
      "prompt_addendum": "远处城市灯光柔和点亮，天空渐变微妙加深，主体曝光准确自然。"
    },
    {
      "variant_name": "V4 - 天空背景下强剪影",
      "changes_from_master": [
      "让光源稍微偏向人物后方以产生轮廓光",
      "增强剪影的清晰度",
      "保持面部特征仍可辨认"
    ],
    "prompt_addendum": "使用干净的轮廓高光进行逆光照明，突出肩部和发际线，强化人物在天空前的剪影，同时保持眼睛和雀斑清晰可辨。"
  },
  {
    "variant_name": "V5 - Phone proof stronger",
    "changes_from_master": [
      "让画面左下角的手机更加清晰可见",
      "确保屏幕上无任何文字",
      "保留自然抓拍的感觉"
    ],
    "prompt_addendum": "手机需清晰显示，作为自拍证据，屏幕不可读且无文字，保持画面自然，如同真实拍摄的瞬间捕捉。"
  },
  {
    "variant_name": "V6 - Tattoo hero framing",
    "changes_from_master": [
      "构图稍作上移，以突出胸部纹身",
      "降低天际线的显著性",
      "保持比基尼肩带真实自然，不打结或缠绕"
    ],
    "prompt_addendum": "将胸部纹身作为核心细节突出展示，减弱天际线的主导感，比基尼肩带需保持物理上的可信度，呈现自然张力。"
  }
],
"advanced_controls_optional": {
  "seed_policy": "如果你使用的生成器支持种子值，请为每个变体锁定一个种子值，以便在迭代过程中保持人物身份和构图的一致性。",
  "consistency_rules": [
    "若使用参考图或种子锁定，需确保在多次生成中维持相同的人物身份。",
    "纹身的完整性必须完全一致，不得有任何偏移或变形。",
    "避免出现解剖结构的异常，尤其是手部、肩部和腰部。"
  ],
  "iteration_recipe": [
    "首先使用 V1 版本在 4:5 画幅中验证姿势和主导角度。",
    "切换至 V6 版本检查纹身的可读性及是否发生变异。",
    "测试 V3 版本在 9:16 画幅下的天际线辉光与光晕平衡。",
    "若生成结果看起来过于电影感或过度修饰，请严格应用 negative_prompt_master。"
  ]
},
"creative_option": {
  "idea": "若希望画面更像真实的 iPhone 拍摄效果，可在某一角落添加极细微的镜头污渍和微弱反光，但需保持克制，使其呈现为真实痕迹而非滤镜效果。",
  "toggle": "可选"
}
```

</details>

<details><summary><b>工匠与报纸折纸特写</b></summary>

```text
一张电影感、暖色调的特写照片，拍摄一位手工艺人在傍晚时分于木质书桌前工作。画面焦点清晰落在桌面上：两个由旧报纸制成的精致纸艺人物——一只折纸小浣熊端坐凝神，一名手持雨伞的纸质小男孩。男子的手正轻柔地托住并调整纸偶的位置，而他的面部在背景中呈现柔和虚化，显露出专注沉思的神情。一盏台灯自上方投下富有戏剧感的金色光线，拉出修长阴影，并凸显纸张细腻的纹理质感。浅景深、柔焦背景虚化（bokeh）、写实摄影风格、私密而奇趣的氛围、叙事性构图、高对比度布光、手工制作美学。
```

</details>
