# 图像与设计 (2/4)

共 743 条。复制后把方括号里的内容换成你的，粘贴进任意对话模型即可。

[English](../en/image.md) · [中文](../zh/image.md)

分页：[1](image.md) · **2** · [3](image-3.md) · [4](image-4.md)

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

<details><summary><b>图标设计师</b></summary>

```text
像图标设计师一样，给我一些关于表示“简单”一词图标的想法。这个想法是在该应用程序的主网站页面上添加一个图标，代表“简单易行的烹饪”理念，因为该应用程序的主要目标是为人们提供简单的食谱，让他们可以在家轻松烹饪。更多信息：- 图标应该简单明了，视觉效果简单，可以简洁地传达想法。
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

<details><summary><b>土木工程师与立面设计师</b> · 机器翻译</summary>

```text
角色:假设你是一名土木工程师兼立面设计建筑师。背景:请根据我提供的图片,为这栋一层加二层(地面层加一层)、主体结构已经完工、临街面宽 26 英尺的房屋,给我 3D 立面效果设计,并提供多张采用现代楼层风格的设计图。请尊重现有可见的结构和开口。
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

<details><summary><b>圣托里尼夏日时尚大片</b> · 机器翻译</summary>

```text
一张全身竖构图的时尚杂志大片,主角是一位美丽的年轻女性,身材苗条健美、呈沙漏型,肤色是金色的日晒古铜色,长长的波浪浅棕色头发带有金色挑染,在风中向左飘扬。她穿着一条无肩带的白色象牙色长裙,心形领口结构分明,上身修身,裙摆是飘逸的褶皱亚麻质感,长及地面。她赤脚,优雅地走在白色粉刷墙的边沿上,左脚向前迈出,脚跟微微抬起,右臂向下伸直,手里拎着一双白色细带细高跟凉鞋的带子。她低着头,目光向下,神情宁静、梦幻、若有所思,双唇轻闭,涂着裸珊瑚色。背景是深钴蓝色的爱琴海,一直延伸到地平线,远处可见希腊岛屿的海岸线(米色悬崖上的白色建筑,圣托里尼风格),上方是清澈的淡蓝色天空。拍摄于地中海正午明亮的阳光下,光线来自右上方,在她的肩膀、锁骨与胸口区域和头发上形成强烈的日晒高光,阴影柔和而清晰,白色粉刷墙面反射出自然的白色补光。专业全画幅无反相机,85mm镜头,f/5.0,1/800秒,ISO 100,平视角度全身竖构图,中等景深,使人物和海景都保持清晰。奢华度假风杂志摄影风格,希腊岛屿夏日美学,极简的白蓝配色,金色肤色,优雅而自由洒脱的氛围,Vogue Greece旅行大片的气质,细微的细腻胶片颗粒,高端时装广告大片品质。
```

</details>

<details><summary><b>圣诞节海报</b></summary>

```text
设计一张以圣诞节为主题的海报，展现浓郁的节日欢庆氛围。需包含以下元素：闪烁的圣诞彩灯、装饰精美的圣诞树、飘落的雪花、包扎好的礼物，以及温馨的冬日背景。整个画面应传递温暖、喜悦与团聚之感。使用红色、绿色和金色等鲜艳色彩，并添加柔和的发光效果，营造出梦幻般的氛围。海报尺寸应为 ${size:1080x1080}，便于在社交媒体上分享。自定义文字内容，加入如“节日快乐！”或“节日问候！”之类的节日祝福语。
```

</details>

<details><summary><b>地中海晚礼服人像</b> · 机器翻译</summary>

```text
一张全身竖构图照片,主角是一位惊艳的年轻女子,留着浅棕色长直发,肤色是晒成的金色,五官精致,嘴唇丰满,身材是极为曲线玲珑的沙漏型,腰非常细,臀部和臀线突出。她穿着一件无肩带的淡黄色鱼尾款及地长礼服,极为贴身,右侧有层叠的荷叶边一路向下,优雅的长拖尾铺在地面上。她背对镜头站立,越过右肩直视观者,姿态挺拔且略带弓形以凸显身体曲线,一只手搭在后腰上。场景是夜晚户外地中海风格的入口,带纹理的米色灰泥墙,两盏华丽的黑色锻铁复古壁灯,发出暖色烛光般的灯光,在墙上投下戏剧性的阴影,墙根沿线是修剪整齐的绿色黄杨树篱,右后方背景中有红色的九重葛花,地面是浅灰色混凝土小径,头顶是深色木质天花板横梁。壁灯发出的温暖琥珀金色光线营造出浪漫迷人的氛围,强烈的侧光勾勒出她的轮廓,并形成深邃戏剧性的阴影。略微仰拍,全身画幅,中等景深,高分辨率时尚魅力摄影风格,电影感暖色调,织物和皮肤质感的细节锐利。
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

<details><summary><b>复刻上传素材的风格</b> · 机器翻译</summary>

```text
“我希望你分析我上传的视频和图片,并复现完全相同的风格。
请给我输出示例声音、台词表达方式、视频风格、台词表达格式、4K 画幅比例等等等等,以及所有其他风格元素
```

</details>

<details><summary><b>复古单色剪影自拍</b> · 机器翻译</summary>

```text
Pinterest 美学风格的特写照片级真实自拍,以上传的照片为参考。完全保留这个女孩的外貌和她所有独特的面部特征(100% 复制我的脸)。

构图与姿势:第一人称自拍,画面中看不到手机。女孩位于画面中央。从低角度(向上仰拍)拍摄的特写肖像。她的视线略微向上并朝画面右侧。由于视角较低,她的脸微微后仰。双手不可见。她的身形刻意处理得柔和且略微失焦,营造出深色模糊剪影的感觉。

服装:一件修身的黑色罗纹连衣裙,宽袖,袖子向手腕处外扩。

头发:极长、完全笔直、顺滑华丽的头发,自由地垂落在前臂上,环绕着脸庞,带有明显的风动效果和轻微的动态模糊。

妆容:戏剧性的眼妆和唇妆,有锐利的飞翼眼线、长假睫毛和哑光深色口红。

背景:高大舒展的树木,枝条光秃,是早春或晚秋的典型景象。枝条在明亮的阴天天空下形成复杂的图形图案,天空占据画面上半部分的大部分,与女孩的深色剪影形成对比。

风格与滤镜:艺术化的黑白模糊美学。单色调,有深黑色和柔和的灰色过渡。刻意的柔焦、明显的动态模糊、细微的轮廓模糊、细腻的胶片颗粒,以及老式模拟照片、梦境或记忆的感觉。重点在于形状、线条、对比和剪影。

相机:用旧 iPhone 5s(2013–2014 年)拍摄,有可见的颗粒、轻微的数码噪点、柔和的锐度、自然的色调表现和真实的 iPhone 压缩效果。竖版 3:4,写实、高画质、电影感。
```

</details>

<details><summary><b>复古发明专利文件</b></summary>

```text
一份关于${invention}的复古专利文件，风格仿照19世纪晚期美国专利商标局（United States Patent Office）的申报文档。页面包含精确的技术绘图，并配有带编号的标注说明（图1、图2、图3），分别展示正面视图、侧面视图和爆炸分解视图。使用钢笔墨水手写批注，描述各机构部件的工作原理。纸张呈泛黄象牙色，带有霉斑污渍（foxing stains）及柔和的折痕。页角处印有官方浮雕印章与红色火漆印。底部为发明人亲笔签名及签署日期。整幅图像令人感觉如同一份重见天日的档案文献——权威、厚重、富有历史感，且略带神秘气息。
```

</details>

<details><summary><b>复古寄送邮戳</b> · 机器翻译</summary>

```text
创建一张 PNG 图片,像一枚邮票,上面写着寄往 $(country)。图片为红色,复古风格,横向邮票
```

</details>

<details><summary><b>复古怀表里的微缩世界</b> · 机器翻译</summary>

```text
一张超精细的微距照片:一块打开的古董黄铜怀表,放在饱经风霜的木桌上。表壳内没有表盘,而是一个微缩的鲜活世界:${scene:a misty alpine valley with a winding river, pine forests and a little stone village}。怀表的齿轮被编织进景观中,化作梯田般的山丘和水车,指针则构成横跨河流的精致桥梁。村庄的窗户里透出微小而温暖的灯光。柔和的黄金时刻光线从左侧照入,景深很浅,背景是奶油般的虚化,光束中漂浮着尘埃颗粒。带雕花的表盖敞开着,投下柔和的阴影。照片级真实感,移轴微缩质感,刮痕黄铜与玻璃的丰富纹理,电影级调色,${aspect_ratio:16:9} 构图。
```

</details>

<details><summary><b>复古未来主义七十年代科幻</b></summary>

```text
复古未来主义风格的 1970 年代科幻电影画面，使用 35mm 胶片拍摄。人物身着高领象牙色制服，头戴 oversized 白色球形头盔，配深色遮光面罩。构图对称、广角，留白强烈，融合韦斯·安德森（Wes Anderson）与斯坦利·库布里克（Stanley Kubrick）式的冷面美学（deadpan aesthetic）。光线柔和、漫射、阴天感，整体氛围洁净而临床化，阴影对比度低。色调为低饱和度的粉彩色系：白色、米色、浅蓝色、褪色青绿色（desaturated teal）及浅大地色系，胶片略带朦胧泛色（hazy film tint）。场景设定于粗野主义（brutalist）极简室内空间，或雾气弥漫的海岸景观中，配有复古模拟（retro-analog）科技设备与方正笨重的未来主义载具。呈现 Kodak Portra 400 胶片质感：可见胶片颗粒（film grain）、细微动态模糊（motion blur）、大景深（deep depth of field）、触感强烈的哑光纹理（tactile matte textures）。
```

</details>

<details><summary><b>复古森林蘑菇苔藓图鉴</b> · 机器翻译</summary>

```text
森林蘑菇与苔藓被布置成一幅复古博物学铬石版画图版：一朵带白色斑点的红色毒蝇伞，一簇金黄色的鸡油菌，一朵茎粗而色浅的棕色牛肝菌，几朵娇嫩的紫色紫蜡蘑，以及一个展示菌褶的菌盖剖面。标本以均衡的网格排布在泛黄的米色旧纸上，每一件都用精细的雕刻线条勾勒轮廓，并以柔和的点刻手法着色。它们之间点缀着几簇绿色垫状苔藓、一卷桦树皮和几片落下的橡树叶。采用柔和的 19 世纪印刷色彩：砖红、赭黄、橄榄绿、赭褐和灰紫，带有石版印刷特有的轻微套色错位。纸张边缘有霉斑和淡淡的泛黄，图版四周围着细细的双线边框。科学、宁静、适合收藏的古董版画氛围。无文字，无标签，无数字，无说明文字，无人物。
```

</details>

<details><summary><b>复古植物图鉴插画</b></summary>

```text
一幅关于 ${subject} 的植物学图解，以复古科学期刊的风格绘制。采用自然色调，并包含精细的横截面图示；图中配有赭石墨水手写标注，营造出学术性与古雅韵味并存的氛围。
```

</details>

<details><summary><b>复古胶片火柴光人像</b> · 机器翻译</summary>

```text
富有氛围感的竖构图人像,带有"胶片摄影"美学。女孩坐在地板上,背靠一面素净的浅色墙壁(浅灰色或白色,带轻微纹理)。姿势放松,略显内向:膝盖弯曲并拉到胸前,上身微微前倾。她的头转向左侧呈侧面,目光向下注视着右手举在脸前的一根燃烧的火柴。左手松松地搭在膝盖/腿上。
她穿着一件复古风格的宽松运动衫(无帽卫衣),颜色为柔和的粉色(灰玫瑰色或紫红色)。袖子上沿整个长度有三条白色条纹(风格参考 Adidas Originals),左胸侧也能看到同样的标志(三叶草)。运动衫看起来柔软,略有磨旧感。下方露出浅色短裤的边缘(可能是白色或浅粉色),双腿裸露。
发型:直发,自然松散地垂在肩膀和背上,质地顺滑。妆容为"素颜妆"风格:哑光肌肤,淡淡腮红,自然眉毛,裸色唇彩带轻微光泽。长指甲,杏仁形或芭蕾舞者形,涂着淡雅的奶粉色(milky pink)。右手无名指上戴着一枚细细的金戒指。手中握着一根普通的长火柴,顶端正在燃烧。
模仿胶片相机(35mm 胶片)拍摄。画面有典型的胶片颗粒(film grain)和柔和的锐度。柔和的漫射日光从左侧(可能来自窗户)落下,在脸部和衣服上形成平滑的阴影过渡。火柴的火焰提供一个微小的暖色点光源,但不是主要照明。调色为粉彩、略微褪色的色调。以柔和的粉色、肤色和冷白/灰色为主。低对比度,浓厚的 2010 年代"Pinterest"或"Tumblr"美学。极简、干净的背景,即没有装饰的墙壁,以突出模特的身形和情绪。
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

<details><summary><b>复古铁皮玩具机器人游行</b> · 机器翻译</summary>

```text
一张微距产品摄影作品,五个 20 世纪 50 年代风格的老式发条铁皮机器人并排站成一列游行队伍,立在一块磨旧的木架上,采用宽幅 16:9 横向画面。机器人呈方正的复古造型,每个都有方形的头、圆眼睛或护目镜面罩、顶端带小球的天线、胸前的圆形表盘、细小的印刷铆钉、按钮和指示灯、短而僵硬的手臂,背后有一把黄铜发条钥匙。它们的铁皮涂装颜色从左到右依次为 ${colors:red, teal, cream, mustard yellow, and red},漆面略有磨损,带有轻微的划痕,边缘有一点锈迹。最右边的机器人举着一根细金属杆,杆上挂着一面没有文字的红色三角小旗,仿佛在带领这支游行队伍。它们身后虚化的背景是深色木架,摆满旧玩具:窗边的泰迪熊、一个小地球仪、一个红球、一辆玩具卡车和一座小娃娃屋。温暖的金色窗光从左侧射入,在铁皮上形成柔和的高光,在有划痕的木架上投下柔和的阴影。浅景深,浓郁温暖的棕色调,怀旧而欢快的氛围。无可辨认的文字,无标志,无人物。
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

<details><summary><b>夜间水族箱里的发光水母城</b> · 机器翻译</summary>

```text
夜晚一个大型矩形玻璃水族箱的写实电影感静帧，视角略低于视平线。水中漂浮着一座微缩的深海城市，依偎在高大的发光水母之间：小巧的珊瑚尖塔、柔光窗户、由半透明海带纤维织成的精致桥梁，以及如深渊灯笼般温暖的点点灯光。月亮水母和狮鬃水母缓缓漂移，伞盖和触须散发着青色、蓝绿色和淡紫色的光芒，在沙质底面洒下斑驳的光影。细小的浮游生物在体积光（丁达尔光束）中闪烁，光线来自头顶一盏冷色调的水族箱灯。玻璃上有凝结的水珠和细微的反射；远处隐约可见漆黑的客厅背景。超精细，浅景深聚焦在中央的塔群上，85mm 镜头质感，无人物，无文字，无标志，宁静而神奇的氛围，适合工作场合观看。
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

<details><summary><b>夯土乡村图书馆设计简报</b> · 机器翻译</summary>

```text
请扮演一名建筑概念设计师,撰写可直接用于图像生成的设计简报。帮我构思一座小型夯土社区图书馆,位于村庄或小镇:单层建筑,包含阅览室、儿童角和一个有遮阴的户外阅读花园。你的简报必须足够具体,使两次独立的图像生成(一张整体外观图和另一张外观视角图)呈现出同一座建筑。

请先用一条简短的消息向我询问:
- 地区和气候(例如干燥高地、温暖的地中海丘陵、半干旱平原),以及我想表现的季节
- 场地:村庄广场、公园边缘、山坡小巷,或学校旁边
- 藏书规模和容量(同时可容纳多少读者),以及是否有小型社区活动室
- 材料偏好和我想避免的东西(玻璃盒子、厚重的混凝土、做作的乡土风)
- 氛围关键词(温馨、安静、阳光充足、质朴、公共性、活泼)

然后按以下部分生成简报:

1. **场地与朝向**:图书馆的位置,哪一侧面向公共广场、哪一侧面向阅读花园,早晨和黄昏的日照路径,以及人们步行接近的方式。

2. **建筑形体**:占地面积、屋顶类型(平屋顶、低坡单坡屋顶或微弧屋顶)、屋檐边缘与出挑、有遮阴的入口门廊、大型开口的数量和位置,以及一个标志性元素,例如圆形阅读塔或宽幅高窗带。保持紧凑且可建造。

3. **材料色板**:恰好四到五种材料及其颜色(例如层叠的赭石色和锈色夯土墙、浅色木柱和木质吊顶、纤薄的深色钢制屋檐边、本地石材铺地、陶土花盆),并说明每种材料出现在哪里。

4. **景观**:乡土树木和草本植物、入口附近的一棵标志性树木、一条浅石水渠(或不设)、长椅和自行车架。

5. **固定视觉细节**:编号列出 8 到 10 个必须在每张图像中保持一致的细节(墙体颜色和可见的夯土层、屋顶形状、门廊柱子数量、窗户数量和形状、门的颜色、标志性元素及其位置、标志性树木及其所在一侧、照明灯具)。这些细节能使各图像保持一致。

6. **提示词种子 A - 整体外观**:一段可直接粘贴使用、少于 150 个单词的图像提示词,描绘从公共广场看到的明亮清晨外观,第一句话就要写出建筑及其关键物体。

7. **提示词种子 B - 第二外观视角**:一段可直接粘贴使用、少于 150 个单词的图像提示词,描绘从阅读花园一侧看到的黄昏景象,窗户透出温暖的光,并用平实的语言重复每一个固定视觉细节,同时说明从该视角看每个元素位于哪一侧。

8. **实用说明**:三条简短说明,分别涉及被动式降温与遮阴、无障碍通行,以及保护夯土墙免受雨水侵蚀(屋檐出挑、石基座)。

规则:不以人物为主体,图像提示词中不得出现文字、标牌或标志,种子中不含室内场景(图像模型往往会忽略家具)。使用短段落和列表。
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

<details><summary><b>奢华防晒护肤竖屏广告视频</b> · 机器翻译</summary>

```text
为一款防晒产品创作一支高端电影感护肤广告,灵感来自奢华美妆广告。竖屏 9:16 格式,写实画面,优雅转场,柔和的金色阳光,自然的皮肤质感,温暖的橙色与金色色调,高端商业广告摄影风格。

场景 1(0–5 秒):一位留着深棕色长发的美丽年轻女子站在郁郁葱葱的热带花园中,周围是鲜绿的叶片和温暖的晨光。金色阳光透过枝叶洒落,她轻轻触摸脸颊,展现出健康、焕发光彩、自然的肌肤。使用流畅的电影感镜头推进。

场景 2(5–10 秒):女子面部的极致特写,她用指尖轻柔地将护肤品涂抹在脸颊上。突出真实的毛孔、光滑的肌肤质感、细腻的高光和清新水润的光泽。柔和的自然光,浅景深,高端美妆广告美学。

场景 3(10–15 秒):一支橙白相间的防晒霜软管直立在热带花园中的天然石台上的主角产品镜头。阳光在包装上形成美丽的高光,背景中绿色枝叶柔和虚化。镜头缓缓环绕产品旋转。保持包装与所提供的产品参考图一致。

场景 4(15–20 秒):微距镜头,指尖托着少量半透明的淡绿色凝胶。凝胶质地光亮、轻盈,在阳光下闪耀动人。转场至防晒霜软管的特写,伴有优雅漂浮的水滴和细微的金色粒子。

场景 5(20–25 秒):女子在热带花园中享受阳光,自然地微笑。她的头发在微风中轻轻飘动。切换到奢华的产品主角镜头,周围环绕着温暖的金色光线、精致的水滴和柔和的植物元素。

场景 6(25–30 秒):精致的护肤成分可视化画面,包含半透明的金色球体、水滴和发光的橙白相间防晒霜软管。使用优雅的微距摄影、简洁的构图和流畅的动态图形。保持高端科学护肤广告的风格。

场景 7(30–35 秒):转场至明亮的热带海滩,海水碧蓝,沙滩洁白柔软。女子身穿优雅的白色夏日连衣裙,在海边悠然漫步。海风中她的头发自然飘动,阳光在水面上反射。使用电影感广角镜头和轻柔的跟拍运动。

场景 8(35–40 秒):以防晒霜从软管挤到指尖的特写镜头收尾,接着是女子躺在白色毛巾上放松的美丽海滩俯拍镜头。最后定格在干净奢华的防晒产品主角镜头,配以温暖的阳光和闪烁的水面反光。

视觉风格:写实的奢华护肤广告,真实的皮肤与产品质感,柔和的黄金时刻光线,热带植物氛围,电影感微距摄影,流畅的镜头运动,优雅的匹配剪辑,细微的镜头光晕,高端调色,4K 画质,24fps。

一致性要求:所有场景中保持同一位女模特、面部特征、发型、产品包装以及橙白配色。保持产品标签干净,并与参考图一致。避免出现变形的手、多余的手指、人为的皮肤磨皮、扭曲的包装和随机文字。不要添加未经证实的产品功效宣称,也不要改变品牌标识。
```

</details>

<details><summary><b>好莱坞海报特写</b> · 机器翻译</summary>

```text
一位引人注目的28岁英国女性，以极具力量感的特写占满画面。她略微越过镜头望向远处，神情专注而强烈，仿佛刚刚认出了某个人。在画面的一侧，一枚半透明的指纹柔和地融入肖像之上，精准地横跨她的眼睛和脸颊。指纹成为整个故事的核心。她的面孔依然是毫无疑问的视觉主角。

构图：
紧凑的电影感肖像。
一只眼睛位于上三分之一处附近。
她的脸占据约百分之七十的画面。
指纹在画面中形成一道巨大而优雅的图形曲线。
背景信息极少。

背景：
柔和虚化的中性石灰灰环境，带有细微的冷调纵深感。

色彩世界：
干净的石墨灰、浅灰、自然肤色，以及标题处理中一抹克制的深绯红色点缀。

灯光：
受控的电影感肖像布光，柔和的定向主光，明亮的中间调，开阔的阴影，以及眼睛和颧骨周围精确的高光分离。

皮肤：
自然的摄影质感皮肤，带有细微的毛孔、真实的色调变化，以及额头、脸颊和眼部区域平滑连续的过渡。

字体排印：
“THE WITNESS”出现在下三分之一处，使用粗体窄体现代字体。
THE较小，WITNESS较大，在视觉上占主导。

下方干净地融入极简的影院式演职员署名。超写实的好莱坞犯罪题材主视觉海报，精准、紧张，简洁而经典。
```

</details>

<details><summary><b>好莱坞风格高清修图</b> · 机器翻译</summary>

```text
扮演图像优化专家。你的任务是把上传的一张 12 岁女孩的照片转换成好莱坞风格的高清图像。在不改变女孩的姿态、五官特征、头发、眼睛和笑容的前提下，提升图像质量。重点打造专业风格，带有超饱满的镜头效果和惊艳的背景，以衬托女孩清新美丽的形象。以上传的图像作为优化的基础。
```

</details>

<details><summary><b>姜黄曲酸皂包装图</b> · 机器翻译</summary>

```text
特写镜头展示姜黄曲酸皂的精美包装,呈现出鲜艳的橙色和黄色设计。
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

<details><summary><b>家族办公室标志优化</b> · 机器翻译</summary>

```text
项目概述：
我正在寻找一位有才华的平面设计师，为我们的家族办公室"KERNPUNT"（荷兰语，意为"中心点"或"核心点"）完善并落地一套精炼的视觉识别。

我们的家族办公室管理并整合三大支柱：投资管理、慈善事业和物业管理。标志必须传达稳定、传承、远见和精准协调的感觉。目标是实现一种"永恒"的美感，给人以历史悠久、值得信赖的印象。

设计背景与当前概念：
我们最初的探索围绕着这样一个概念：放射状的线条汇聚于一个精确的中心点，或从该点发散而出，即"星芒"或"聚焦罗盘"。这一概念基础很扎实（入选后将共享），但执行上需要一种特定的、多维度的色彩处理方式。

关键设计目标（需要完善之处）：

符号中的细腻明暗处理（必须完善）：这是本设计需求中最关键的部分。构成主符号（星芒/焦点）的放射状线条不能是单色的。它们必须运用多种深浅和渐变的蓝色。
这不是作用于整个对象的渐变效果，而是将单独的射线或成组的射线渲染成各不相同却和谐统一的蓝色。
这种刻意的明暗处理旨在表现我们不同支柱（投资、慈善、物业）的汇聚，让身份识别的不同侧面得以显现，并在视觉上相互平衡。最终的图案必须清晰、有意为之。
特定的字体样式：文字标志"KERNPUNT"有非常具体的样式要求。
"KERN"一词必须采用粗体字重。
"PUNT"一词必须采用同一字体的标准（或细）字重（去掉粗体）。
两种字重之间的字距必须完美，形成一个统一而精致的单词。
文字的色彩层级：文字的配色必须突出结构。
"KERN"一词将渲染为深沉、稳重的蓝色（例如海军蓝）。
"PUNT"一词将采用明显更浅的蓝色（例如天蓝色）。
整体美感：设计必须矢量精准、现代、简洁。它必须在各种应用中都表现完美，从数字展示到高端文具（例如压凹/烫金），但首要目标是一个多用途的矢量标志。

你的交付成果：

精炼的符号几何：完善中心焦点符号的矢量几何形状。
多层蓝色明暗的执行：将所要求的一系列不同深浅的蓝色融入符号的射线中。
最终定稿的文字标志：将指定的粗体/细体字重拆分和深/浅蓝色配色方案应用于"KERNPUNT"。
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

<details><summary><b>小册子封面设计程序</b> · 机器翻译</summary>

```text
创建一个专业程序,用于制作不同颜色的小册子封面,并可添加图片来补充画面,这些图片有助于吸引读者的注意力,采用高级版式分布,可选择产品名称“”简要概述“”作者“”和序列号的类型、颜色和字体格式
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

<details><summary><b>山地观星小屋设计简报</b> · 机器翻译</summary>

```text
请扮演一位建筑概念设计师,专长是为业余天文爱好者设计小型离网静修小屋。帮我编写一份清晰、可直接用于生成图像的设计任务书,对象是一座小型山地天文台木屋。

请先用一个简短的清单向我询问:选址(山脊、海拔、气候、积雪)、使用者(一位观星者、一对伴侣、一个小型俱乐部)、预算水平(较低、中等、较高)、望远镜的类型和口径,以及任何必备项(木柴炉、床铺、暗室红光照明、离网供电)。

然后按以下部分生成任务书:

1. **一句话概念**:木屋的感受与用途。
2. **选址与朝向**:它在山脊上的位置、主窗朝向、通向天空最暗区域的视线、防风防雪措施。
3. **形态与体量**:占地面积(控制在 40 平方米以内)、屋顶形状,以及旋转式望远镜圆顶或可滑开的屋顶,并给出大致尺寸。
4. **材料与色调**:外墙饰面(例如竖向雪松板)、屋面、圆顶表面处理、窗框和室内木材,每项都标明颜色或色调。
5. **室内布局**:用于星图和笔记本电脑的书桌、望远镜入口或目镜位置、木柴炉、座椅、目镜和星图的储物空间,以及需要时的睡眠角。
6. **夜间照明方案**:暗红色工作灯、低亮度暖色灯,以及如何避免光线外泄而破坏暗适应。
7. **固定视觉细节**:一份编号清单,列出 8 到 10 项在这座木屋的每张图像中都必须保持一致的细节(外墙板方向、圆顶颜色、窗户数量和形状、烟囱位置、露台、小径、周围树木、山脊轮廓)。
8. **图像提示词雏形**:两段简短的提示词开头,一段用于山脊上银河下的外景夜景,一段用于从温暖室内向外望向星空的视角。每段都必须重述固定视觉细节,并把关键物体放在第一句。

保持简洁、实用、可建造。避免提及真实的建筑师或品牌。标出任何在高海拔山地气候下不安全或不切实际的内容。
```

</details>

<details><summary><b>山坡酒庄品鉴亭设计简报</b> · 机器翻译</summary>

```text
扮演一名建筑概念设计师,撰写可直接用于图像生成的设计简报。帮我构思一座山坡葡萄园里的小型品酒亭:一座单层建筑,游客在此品酒并眺望一排排葡萄藤。你的简报必须足够具体,使两次独立的图像生成(一张主外观图和另一个角度的外观图)呈现出同一座建筑。

请先用一条简短的消息向我询问:
- 地区与气候(例如地中海、温带河谷、高原沙漠)以及我想展现的季节
- 坡向和主要景观(山谷、湖泊、远山、村庄)
- 容纳人数(同时接待多少位客人),以及是否设有小型酒桶室或厨房
- 材料偏好以及我想避免的元素(玻璃盒子、乡村俗气风、过于现代的极简风)
- 氛围词(宁静、阳光、质朴、优雅、家庭经营)

然后按以下部分撰写简报:

1. **场地与朝向**:品酒亭在坡上的位置,哪一面朝向景观,早晨与日落时的太阳轨迹,以及一条碎石小径如何从停车区穿过葡萄藤向上延伸。

2. **建筑形态**:占地大小,屋顶形状与坡度,出檐深度,下坡一侧的长条有顶露台,以及大型开口的数量和位置。保持紧凑、可信。

3. **材料色板**:恰好四到五种材料及其颜色(例如当地石灰岩墙体、上油橡木梁、陶土屋瓦、青铜窗框、碎石露台),并说明每种材料出现在哪里。

4. **景观**:葡萄藤行的方向,入口附近的一棵老橄榄树或橡树,低矮的石砌挡土墙,薰衣草或香草花境,以及户外桌椅。

5. **固定视觉细节**:一份编号列表,列出 8 至 10 项必须在每张图像中保持一致的细节(屋顶类型与颜色、墙体材料、露台拱门或立柱数量、门的颜色、有无烟囱、标志性树木、灯具)。这些细节能让各图像保持一致。

6. **提示词种子 A - 主外观**:一条可直接粘贴的图像提示词,不超过 150 词,描绘清晨或采收季从上坡小径望去的外观,第一句话中就要包含建筑及其关键物体。

7. **提示词种子 B - 另一角度外观**:一条可直接粘贴的图像提示词,不超过 150 词,描绘日落时从下坡葡萄藤行仰望露台的视角,并用平实的语言重复每一项固定视觉细节。

8. **实用说明**:三条简短说明,分别涉及遮阳、无障碍(无台阶入口)以及坡地排水。

规则:不以人物作为主体,图像提示词中不出现文字或标志,种子中不出现室内场景(图像模型常常忽略家具)。使用短段落和列表。
```

</details>

<details><summary><b>工匠与报纸折纸特写</b></summary>

```text
一张电影感、暖色调的特写照片，拍摄一位手工艺人在傍晚时分于木质书桌前工作。画面焦点清晰落在桌面上：两个由旧报纸制成的精致纸艺人物——一只折纸小浣熊端坐凝神，一名手持雨伞的纸质小男孩。男子的手正轻柔地托住并调整纸偶的位置，而他的面部在背景中呈现柔和虚化，显露出专注沉思的神情。一盏台灯自上方投下富有戏剧感的金色光线，拉出修长阴影，并凸显纸张细腻的纹理质感。浅景深、柔焦背景虚化（bokeh）、写实摄影风格、私密而奇趣的氛围、叙事性构图、高对比度布光、手工制作美学。
```

</details>

<details><summary><b>巨人俯瞰的超现实微缩城市</b></summary>

```text
{
  "colors": {
    "color_temperature": "neutral",
    "contrast_level": "high",
    "dominant_palette": [
      "blue",
      "red",
      "green",
      "yellow",
      "brown"
    ]
  },
  "composition": {
    "camera_angle": "eye-level",
    "depth_of_field": "deep",
    "focus": "The miniature city diorama held by the woman",
    "framing": "The woman's hands frame the central diorama, creating a scene-within-a-scene effect. The composition is dense and layered, guiding the eye through numerous details."
  },
  "description_short": "一幅超现实的数字艺术作品，描绘一位巨大的年轻女子手持一个复杂的多层截面模型，模型中是一个融合了传统东亚建筑与现代科技的生动未来都市。",
  "environment": {
    "location_type": "cityscape",
    "setting_details": "一座奇幻而广阔的大都市，融合了传统东亚建筑，如宝塔和拱桥，以及飞行器和布满霓虹招牌的密集多层建筑等未来元素。整个场景以一个被巨人手持的微缩世界形式呈现，背景中则延伸出该城市的完整规模版本。",
    "time_of_day": "daytime",
    "weather": "clear"
  },
  "lighting": {
    "intensity": "strong",
    "source_direction": "mixed",
    "type": "cinematic"
  },
  "mood": {
    "atmosphere": "Whimsical urban fantasy",
    "emotional_tone": "surreal"
  },
  "narrative_elements": {
    "character_interactions": "主要的巨人女子正在观察这个微缩世界。在模型内部，微小的人物正在进行日常生活：一名男子坐在房间里，其他人站在阳台上，还有两名身着传统服饰的人物站在建筑顶部。",
    "environmental_storytelling": "巨人手持微缩世界的对比暗示了创造、控制或观察的主题，仿佛她是一位神明或梦境创造者，正在与自己构建的现实互动。新旧建筑的融合讲述了一个在技术进步的同时仍保留文化传统的文明故事。",
    "implied_action": "这名女子正专注地审视她手中的微缩世界，暗示着沉思或决策的瞬间。城市本身则充满了车辆与人群活动的动态感。"
  },
  "objects": [
    "woman",
    "miniature city diorama",
    "buildings",
    "flying vehicles",
    "neon signs",
    "vintage car",
    "bridge",
    "pagoda"
  ],
  "people": {
    "ages": [
      "young adult"
    ],
    "clothing_style": "现代休闲装、商务正装与传统东亚服饰的混合。",
    "count": "unknown",
    "genders": [
      "female",
      "male"
    ]
  },
  "prompt": "一幅细节极其丰富的超现实数字绘画，描绘一位拥有深色刘海和迷人眼神的美丽年轻巨人女子，正手持一个复杂的多层微缩城市模型。该模型是一个充满活力的未来东亚大都市的剖面图，内部布满微小人物、亚洲文字的霓虹灯招牌、一辆复古绿色汽车和传统宝塔。背景中，同一座城市的完整版本在晴朗蓝天之下延展，漂浮的交通工具和错综复杂的桥梁点缀其间。整体风格融合了魔幻现实主义与赛博朋克，采用电影级光照效果。",
  "style": {
    "art_style": "surreal",
    "influences": [
      "cyberpunk",
      "magical realism",
      "collage art",
      "Studio Ghibli"
    ],
    "medium": "digital art"
  },
  "technical_tags": [
    "hyper-detailed",
    "intricate",
    "surrealism",
    "digital illustration",
    "cityscape",
    "fantasy",
    "miniature",
    "scene-within-a-scene",
    "vibrant colors"
  ],
  "use_case": "适用于科幻或奇幻电影的概念艺术、书籍封面插画，或用于训练 AI 处理复杂精细场景的数据集。",
  "uuid": "a00cdac4-bdcc-4e93-8d00-b158f09e95db"
}
```

</details>

<details><summary><b>巨树中的魔法图书馆</b></summary>

```text
一棵巨大中空古树内部隐藏着一座古老图书馆，充满魔法且令人向往的氛围表达，宏伟的室内视角，成千上万本皮面装订的书籍陈列在弧形木制书架上，螺旋楼梯从中央盘旋而上，萤火虫在书架间漂浮闪烁，铺有天鹅绒坐垫的磨损阅读椅，位于魔法森林中一株巨型远古橡树的内部，隐秘领域，神秘感十足，温暖而舒适的氛围，秋季场景，橡木桌上散落着卷轴和羽毛笔，树皮墙壁上雕刻着神秘符文，角落里蘑菇柔和发光，前景：散落的书籍与卷轴，中景：散发着温暖光芒的螺旋楼梯，背景：小窗户展示着繁星点点的森林夜景，符合黄金比例构图，广角镜头，低角度拍摄，大景深，f/8光圈，哈苏相机风格，实际光源与轮廓光照明，暮色时分，四分之三侧光，柔光效果，数字艺术，融合Greg Rutkowski、Thomas Kinkade与Studio Ghibli的艺术风格，受新艺术运动（Art Nouveau）影响，兼具田园核心（cottage core）美学，采用温暖且质朴的色彩调色板，主色调：琥珀色、深棕色、森林绿，点缀色：柔金色、月光蓝、仙子粉，高饱和度搭配深阴影调色，整体呈现宁静、平和、怀旧、奇幻的情绪，杰作级品质，8K分辨率，体积光照明，光线追踪，Octane渲染 --no 模糊, 低质量, 结构错误, 水印, 文字, 签名, 现代元素, 塑料, 强烈光照, 过曝, 欠曝 --ar 3:2
```

</details>

<details><summary><b>巫师双重曝光壁纸</b></summary>

```text
受《巫师》电子游戏系列（游戏，非电视剧）启发的双重曝光电影级壁纸。  
杰洛特与叶奈法背对背站立，构图居中且平衡。  
杰洛特：  
面朝前方，脸部完全可见，白发，猫眼，面部带有疤痕且神情坚毅冷静，身穿猎魔人护甲。  
轮廓强壮、清晰分明。  
叶奈法：  
与杰洛特背对背站立，身体略微侧转，脸部以侧面轮廓部分可见。  
黑发，目光锐利，气质优雅而危险，身着飘逸的深色服饰。  
轮廓内部内容：  
在杰洛特的轮廓内：中世纪废墟、妖魔出没的森林、雾气弥漫的山间小径、冷钢色调、阴郁氛围。  
在叶奈法的轮廓内：神秘莫测的地景、古老的石质结构、微妙的魔法图案、月光下的天空、深紫色与暗影色调。  
双重曝光处理：  
轮廓分离干净，环境层次自然融合，具有绘画感但控制精准。  
轮廓之外无任何场景元素。  
背景：  
深红黑色背景，带有细微纹理，营造电影般的张力，饱和度克制。  
风格与氛围：  
黑暗奇幻风格，严肃且贴近原作，电子游戏电影艺术风格。  
不得出现 Netflix 元素、现代服装设计或电视剧改编影响。  
超高清分辨率，细节锐利，高品质壁纸级别。格式 9:16
```

</details>

<details><summary><b>巴厘岛巴龙面具矢量图</b></summary>

```text
一个传统的巴厘岛 Barong Ket 面具的详细矢量插图，表情凶猛，眼睛凸出，獠牙突出。使用平滑的贝塞尔曲线和格式塔对称性原则构建。风格融合了巴厘岛木雕美学与现代扁平化设计极简主义。颜色包括深红、金色和黑曜石黑。已验证：可缩放 SVG，路径干净，无文字，无商标
```

</details>

<details><summary><b>巴黎之夜</b></summary>

```text
{
  "subject_and_scene": {
    "main_subject": "一位年轻男子，有着浓密的棕色卷发，穿着一件精致的米色高领毛衣和相配的定制羊毛西装外套，表情沉思而忧郁。",
    "action": "随意倚靠在一座斑驳的石桥护栏上，背对镜头望向巴黎的城市景观。",
    "environment": "夜晚的巴黎塞纳河畔；背景中埃菲尔铁塔巍然耸立，通体闪耀着金色光芒，城市灯光与河上船只在黑暗的水面上投下柔和的倒影。"
  },
  "cinematography": {
    "camera_model": "Sony Venice 2",
    "sensor_type": "Full Frame",
    "shot_type": "Cowboy Shot",
    "camera_angle": "Eye Level",
    "movement": "Static"
  },
  "optics": {
    "lens_type": "Spherical",
    "focal_length": "35mm (Standard Wide)",
    "aperture": "f/2.8 (Moderate depth of field to retain background context)",
    "shutter_effects": "Standard Shutter"
  },
  "lighting_design": {
    "
```

</details>

<details><summary><b>带天气效果的等距 3D 场景</b></summary>

```text
请扮演一名3D渲染艺术家，负责创作一幅等距视角的微型卡通场景。你的目标是：
- 呈现一个清晰的、45°俯视视角的竖版（9:16）构图。
- 将标志性地标居中置于场景中，并确保建模精准而细腻。
- 使用柔和、精致的纹理，搭配逼真的基于物理的渲染（PBR）材质。
- 融入柔和、逼真的光照与阴影效果。
- 创意性地将天气元素融入城市建筑之中，以增强城市景观与大气条件之间的动态互动。
- 在渲染前，检索指定城市——保加利亚索菲亚（Sofia, Bulgaria）——的当前天气状况。
- 保持构图干净统一，采用极简主义美学风格，并使用柔和的纯色背景，以突出主体内容。
- 确保整体视觉风格清新宜人、舒缓放松。
```

</details>

<details><summary><b>年轻女性休闲人像</b></summary>

```text
{  
    "subject": {  
      "appearance": "混血特征的年轻女性，肤色白皙，留有长而富有层次感的深棕色秀发，自然垂落于肩头。妆容清新自然，眉毛经过精心修饰，唇色为柔和的粉色。",  
      "outfit": "简约黑色细肩带背心或无袖上衣。",  
      "environment": "明亮通透的卧室环境。她仰卧于床上，盖着干净洁白的被子/床单。背景中可见灰色软包床头板。后方窗户上挂着白色薄纱窗帘，柔光由此透入。"  
    },  
    "technical_style": "社交媒体自拍美学风格，三联画或拼贴风格，柔焦效果，高调布光，氛围亲密而随意。"  
  },  
  "pose_specs": {  
    "body_position": "俯卧姿势（面朝下平躺于床上），正对镜头；双肩与上胸部微微抬离床垫。",  
    "arms": "双肘支撑于床面以承托上半身；右手抬起轻触面部——指尖轻柔地搭在下巴或脸颊上。",  
    "head": "头部略作倾斜，营造俏皮且富有吸引力的角度。",  
    "expression": "多样化的俏皮表情：1）甜美浅笑，目光直视镜头；2）侧脸开怀大笑，神情自然率真；3）俏皮眨眼，同时皱起鼻子。",  
    "framing": "特写人像构图，画面截取至肩部/胸部位置。"  
  },  
  "camera_settings": {  
    "viewpoint": "拍摄视角与床上被摄主体视线齐平（相对于房间为低角度）。",  
    "focal_length": "24mm 至 35mm（前置智能手机摄像头焦距）。",  
    "aperture": "f/2.0 至 f/2.8（背景轻微虚化，确保焦点集中于面部）。",  
    "shutter_speed": "1/100 秒",  
    "iso": "200",  
    "composition": "主体居中构图，镜头与被摄者距离亲密。"  
  },  
  "lighting_setup": {  
    "type": "自然窗光。",  
    "qualities": "柔和、漫射、包裹式光线。",  
    "direction": "来自窗户的侧光（画面左侧），均匀照亮面部，并在对侧形成极柔和、富有美感的造型阴影。",  
    "color_temperature": "日光白平衡（约 5500K），呈现洁净的白色色调。"  
  }  
}
```

</details>

<details><summary><b>幻影一击</b></summary>

```text
{
  "title": "Phantom Strike",
  "description": "一名孤独战士在破败的工业环境中与超自然实体激烈战斗的高强度、高能动作画面。",
  "prompt": "你将执行图像编辑，将主体转变为超自然惊悚题材中的动作英雄。图像必须具有照片级真实感，高度细节化，并模拟使用 Arri Alexa 拍摄的电影级光影效果和浅景深。场景描绘女性主体身处废弃且被水淹没的地铁隧道中，正在进行生死搏斗。她正在与仿佛从黑暗中实体化出的、如烟雾般延伸的触须状阴影战斗。光影效果强烈，突出她皮肤的质感以及飞溅的水花。",
  "details": {
    "year": "现代都市奇幻",
    "genre": "电影级写实主义",
    "location": "一个废弃的、被水淹没的地铁维修隧道，墙壁油漆剥落，头顶工业灯具闪烁不定。",
    "lighting": [
      "高对比度明暗对照法",
      "头顶冷色调荧光灯闪烁",
      "蒸汽中透出的体积光束"
    ],
    "camera_angle": "低角度动态动作镜头，1:1 画幅比例，聚焦于动作冲击力。",
    "emotion": [
      "凶猛",
      "肾上腺素激增",
      "绝望"
    ],
    "color_palette": [
      "去饱和的混凝土灰",
      "鲜艳的深红",
      "深渊黑",
      "冷青色"
    ],
    "atmosphere": [
      "动态",
      "压抑",
      "粗粝",
      "超自然"
    ],
    "environmental_elements": "飞溅的脏水、漂浮的尘埃颗粒、半实体化的阴影生物、从破损灯具掉落的火花。",
    "subject1": {
      "costume": "红色迷你裙、黑色露指手套、撕裂的白色战术背心和厚重系带战斗靴。",
      "subject_expression": "咬紧牙关奋力拼搏，目光紧锁目标，极度专注。",
      "subject_action": "与阴影战斗"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "阳光",
        "蓝天",
        "静态姿势",
        "微笑",
        "洁净"
      ],
      "exclude_styles": [
        "卡通",
        "动漫",
        "3D 渲染",
        "油画",
        "素描"
      ],
      "exclude_colors": [
        "粉彩粉红",
        "暖橙色",
        "春绿色"
      ],
      "exclude_objects": [
        "枪械",
        "刀剑",
        "现代车辆",
        "旁观者"
      ]
    }
  }
}
```

</details>

<details><summary><b>应用商店截图画廊生成器</b></summary>

```text
# App Store 截图画廊生成器

**创建一个专业的、可直接投入生产的截图画廊页面，用于 iOS/macOS/Android 应用，视觉效果应如同由顶尖 1% 的应用开发者设计的一样。**

## 上下文

你正在为一个应用构建一个截图画廊页面。项目中包含一个存放截图的文件夹（通常是 `screenshots/`、`fastlane/screenshots/` 或类似路径）。该画廊应为单个 HTML 文件，可部署到 Netlify、Vercel 或任何静态主机上。

## 要求

### 1. 设计系统基础

创建 CSS 自定义属性（设计令牌）用于：

- **颜色**：主调色板（50-900 色阶）、辅助/强调色板、中性灰（50-900）
- **表面**：三个表面层级（surface-1, surface-2, surface-3）
- **排版**：双字体堆栈（UI 元素使用等宽字体，正文使用无衬线字体）
- **间距**：统一的缩放比例（以 4px 为基础）
- **边框**：圆角尺寸等级（sm, md, lg, xl, 2xl, 3xl）
- **阴影**：五个高度层级（sm, md, lg, xl, 2xl）
- **过渡**：三种速度（快速：150ms，正常：300ms，平滑：400ms，使用 cubic-bezier 缓动）

### 2. 布局架构

- **容器**：最大宽度 1600px，居中，带响应式内边距
- **网格**：使用 `grid-template-columns: repeat(auto-fill, minmax(340px, 1fr))` 实现类砌砖式响应式网格
- **间隙**：桌面端 2rem，平板端 1.5rem，移动端 1rem
- **卡片宽高比**：保持一致的截图展示比例

### 3. 头部区域

- **应用徽章**：小胶囊形徽章，带图标和 "IOS APPLICATION" 或平台名称文本
- **标题**：大号、加粗的应用名称，带渐变文字效果
- **副标题**：一行描述，提及关键技术与功能
- **背景**：微妙的网格图案叠加，增强层次感
- **内边距**：减少垂直内边距（顶部 3rem，底部 2rem），营造紧凑感

### 4. 截图卡片

每张卡片应包含：

- **容器**：白色/浅色背景，圆角（2xl），轻微阴影
- **图像容器**：渐变背景，居中显示截图，带白色边框（8px）
- **悬停效果**：
  - 卡片上浮（-8px translateY）并增强阴影
  - 截图放大（1.04 倍）并轻微旋转（0.5deg）
  - 顶部出现渐变条
  - 径向光晕叠加淡入
- **元数据栏**：
  - 编号徽章（渐变背景，26px 正方形）
  - 设备名称（大写，小字体，等宽字体）
- **标题**：加粗，等宽字体，1rem
- **描述**：一行说明文字，较小字体，颜色较淡

### 5. 用户旅程排序

按用户使用应用的顺序排列截图：

1. **登录/引导页** - 用户看到的第一个界面
2. **仪表盘/首页** - 登录后的主要入口
3. **核心功能页** - 应用的核心功能界面
4. **设置/配置页** - 自定义设置界面
5. **权限/集成页** - HealthKit、通知等
6. **高级功能页** - 同步、分享、云功能
7. **分析/报表页** - 数据可视化界面
8. **归档/历史页** - 历史数据查看界面

### 6. 动画

- **入场动画**：交错淡入，配合 translateY（卡片间延迟 0.1s）
- **悬停动画**：使用平滑的 cubic-bezier 缓动（0.16, 1, 0.3, 1）
- **滚动动画**：使用 IntersectionObserver 在卡片进入视口时触发动画
- **性能优化**：对 transform 和 opacity 使用 `will-change`

### 7. 底部区域

- **背景**：深色（neutral-900），带微妙渐变叠加
- **圆角**：仅顶部圆角（2xl）
- **内容**：极简元数据（设备、日期、状态），带图标
- **间距**：紧凑（2rem 内边距）

### 8. 响应式断点

- **桌面端** (>1280px)：4-5 列
- **平板端** (768-1280px)：2-3 列
- **移动端** (<768px)：1 列，整体减少内边距

### 9. 技术要求

- **单个 HTML 文件**：所有 CSS 内联在 `<style>` 标签中
- **仅允许外部依赖**：
  - Pico.css（极简 CSS 框架）
  - Font Awesome（图标）
  - Google Fonts（Inter + IBM Plex Mono）
  - Animate.css（可选，用于额外动画）
- **无构建步骤**：必须作为静态 HTML 直接运行
- **性能**：优化动画，避免布局偏移
- **可访问性**：使用语义化 HTML，图片提供 alt 文本

### 10. 细节打磨

- **微妙渐变**：背景使用径向渐变增强层次感（不过于强烈）
- **边框处理**：1px 实线，带 alpha 透明度
- **阴影分层**：多层阴影值增强深度
- **排版**：标题使用紧凑字间距（-0.03em）
- **颜色一致性**：处处使用设计令牌，禁止硬编码颜色值
- **图像呈现**：截图周围加白色边框，营造设备边框错觉

## 输出格式

生成一个完整的 `index.html` 文件，包含：

1. 完整的 HTML 结构
2. 内联 CSS（含设计令牌）
3. 用于滚动动画的 JavaScript（IntersectionObserver）
4. 所有带正确元数据的截图卡片
5. 针对所有屏幕尺寸的响应式设计

## 示例截图卡片结构

'''html
<div class="screenshot-card">
    <div class="screenshot-img-container">
        <img src="screenshot-name.png" alt="Description" class="screenshot-img">
    </div>
'''
    <div class="screenshot-info">
        <div class="screenshot-meta">
            <div class="screenshot-number">1</div>
            <div class="screenshot-device">iPhone 17 Pro Max</div>
        </div>
        <h3 class="screenshot-title">屏幕标题</h3>
        <p class="screenshot-desc">单行说明文字</p>
    </div>
</div>
'''

## 与“AI 风格”画廊的关键区别

❌ **避免**：
- 过度的渐变和色彩
- 浪费空间的大尺寸数据卡片
- 冗长的描述和功能列表
- 分节分隔线和分类标题
- 过于强烈的动画效果
- 不一致的间距
- 通用的图库摄影风格

✅ **模仿**：
- Apple App Store 产品页面
- Linear、Raycast、Superhuman 的营销网站
- 极简主义、内容优先的设计
- 细腻精致的交互效果
- 一致的视觉节奏
- 以排版驱动的信息层级
- 将留白作为设计元素

## 部署说明

- 画廊应部署至 `project-root/screenshots-gallery/` 或类似路径
- 包含 `.netlify` 文件夹及用于配置的 `netlify.toml`
- 所有截图应与 `index.html` 位于同一文件夹中
- 无需构建流程——纯静态 HTML

---

**使用方法**：复制此提示词，并将其提供给 AI 助手，同时附上：
1. 项目中的截图文件列表
2. 您的应用名称及一句简短描述
3. 平台信息（iOS、macOS、Android、web）
4. 使用的核心技术（SwiftUI、React Native、Flutter 等）

AI 将生成一个外观专业、可直接用于生产的截图画廊。
```

</details>

<details><summary><b>应用配色一致性分析与调整</b></summary>

```text
请扮演一名具备高视觉智能的专业设计师与摄影师。你的任务是分析应用程序中所使用的颜色，并依据给定的主色 ${primaryColor} 和辅色 ${secondaryColor:defaultSecondary}，使其保持一致。确保各颜色之间的过渡平滑且具有审美吸引力。优先采用业界公认、搭配协调的常用配色方案。提供一份详尽的配色方案建议，并提出具体调整建议以增强视觉和谐性。需考虑应用程序所属的业务/领域 ${businessDomain}，确保所选颜色与其目标与宗旨相契合。若该应用程序支持深色模式，请务必进行必要检查并作出相应调整，以在深色模式下同样维持色彩一致性与视觉美感。
```

</details>

<details><summary><b>康定斯基风格抽象几何</b></summary>

```text
{
  "colors": {
    "color_temperature": "中性",
    "contrast_level": "高",
    "dominant_palette": [
      "深绿色",
      "黑色",
      "蓝色",
      "黄色",
      "红色",
      "浅紫色"
    ]
  },
  "composition": {
    "camera_angle": " eye-level",
    "depth_of_field": "中等",
    "focus": "中心位置的一个大型浅蓝色环形，带有黑色核心，被黑色线条贯穿。",
    "framing": "通过几何图形簇的布局以及强有力的水平和垂直线条锚定画面，形成不对称平衡。"
  },
  "description_short": "一幅抽象画作，包含多种彩色几何形状，如圆形、正方形和弧形，排列在深色、有纹理的绿色背景上。构图由粗黑线条构成框架。",
  "environment": {
    "location_type": "抽象",
    "setting_details": "场景是一个非具象空间，由深沉、斑驳的绿色背景定义，为漂浮的几何形态提供深度感。"
  },
  "lighting": {
    "intensity": "中等",
    "source_direction": "未知",
    "type": "环境光"
  },
  "mood": {
    "atmosphere": "和谐的几何互动",
    "emotional_tone": "平静"
  },
  "narrative_elements": {
    "environmental_storytelling": "形状与颜色之间的相互作用——重叠、交叉和漂浮——创造出一种视觉叙事，体现节奏、张力与平衡，常被比作音乐作品。",
    "implied_action": "新月形图案和强烈的线条暗示了动态运动和交互，尽管其他形式是静态的，营造出在一个更大宇宙事件中凝固瞬间的感觉。"
  },
  "objects": [
    "圆形",
    "正方形",
    "棋盘格图案",
    "线条",
    "新月形",
    "三角形",
    "矩形"
  ],
  "people": {
    "count": "0"
  },
  "prompt": "一幅瓦西里·康定斯基风格的抽象画作。复杂的和谐构图中，各种几何形状漂浮在深邃、有质感的暗绿色背景之上。一个带有黑色中心的大型浅蓝色圆圈作为视觉焦点，被粗犷的黑色线条贯穿。色彩丰富的棋盘格图案、黄蓝分割的圆形，以及鲜艳的红黑新月形被精心布置，营造出音乐般的节奏感与宇宙般的平衡感。风格为纯粹的几何抽象，唤起一种理智而沉思的情绪。",
  "style": {
    "art_style": "抽象",
    "influences": [
      "包豪斯",
      "几何抽象",
      "构成主义"
    ],
    "medium": "绘画"
  },
  "technical_tags": [
    "抽象艺术",
    "几何抽象",
    "包豪斯",
    "瓦西里·康定斯基",
    "现代主义",
    "构图",
    "色彩理论",
    "非具象艺术"
  ],
  "use_case": "用于风格迁移AI的训练数据、艺术史分析，或专精于抽象艺术的生成模型。",
  "uuid": "a6088ce6-f151-41f2-aec4-06758084a585"
}
```

</details>

<details><summary><b>建筑草图标注叠加</b></summary>

```text
基于源图像，在整个场景上叠加建筑师忙碌工作过程的图层。该图像应呈现为一张蓝图或描图纸覆盖在原始照片之上，布满手写的黑色墨水草图、技术注释、带尺寸标注的尺寸线（例如：“12'-4"”、“CLG HGT 9'”）、展示结构细节的粗略剖面图、带有“REVISE LATER”等文字的修订云线，以及指向特定元素的引出线，这些元素旁标注有英文建筑师笔记，例如“CHECK BEAM”、“REMOVE FINISH”或“PROPOSED NEW OPENING”。整体风格应显得凌乱、真实，如同一份正在进行中的概念草图。
```

</details>

<details><summary><b>建造中的大金字塔</b></summary>

```text
古埃及吉萨大金字塔建造时期的超写实 4K 电影级场景。金字塔仅建成一半，明显尚未完工，其庞大的轮廓拔地而起却尚不完整。巨大的石块置于重型木筏之上，沿精心设计的水道缓缓移动，由绳索、斜坡与木质结构协同引导。数百名工人步调协调地作业，空气中弥漫着尘埃，水面升腾起细微的薄雾。史诗级广角构图，戏剧性天空，柔和的金色光线穿透尘埃，投下悠长阴影，尽显电影级宏大尺度。整体氛围须庄严肃穆、厚重历史感十足，仿佛亲历一个文明亲手塑造未来的时刻。上传图像中的人物作为核心领袖出现，位于场景略高处，气场威严，姿态自信，神情专注而真实，身着符合史实的古埃及风格服饰。极致精细的纹理表现，逼真的肌肤质感，纪录片式写实风格，景深效果突出，不含任何幻想元素，纯粹的摄影级写实主义。
```

</details>

<details><summary><b>彩色影棚拼图</b></summary>

```text
一个由三幅竖向排列的图片组成的拼贴画，描绘一位28岁、拥有时尚长发的美丽女性。采用影棚摄影风格。  
第1幅：洋红色背景，她穿着一套干净的白色西装，双手叉腰站立，表情自信大胆。  
第2幅：浅蓝色背景，她穿着同样的白色西装，比出剪刀手并开怀微笑。  
第3幅：明亮的黄色背景，她身穿白色西装，跳跃在空中，姿态充满活力。表情非常欢快，色彩明亮且饱和，采用高调影棚灯光，对焦清晰，高分辨率。  
比例 16:9。
```

</details>

<details><summary><b>影棚全家福</b></summary>

```text
创建一个提示词，用于在摄影棚内拍摄家庭合影，并自定义家庭成员的排列方式
```

</details>

<details><summary><b>影棚美妆大片特写</b></summary>

```text
{
  "category": "STUDIO_BEAUTY_EDITORIAL_CLOSEUP",
  "subject": {
    "demographics": "成年女性，21–27 岁，土耳其人相貌，美容广告大片氛围。",
    "hair": {
      "color": "深棕色",
      "style": "柔顺但自然（非头盔式发型）",
      "texture": "单根发丝清晰可见，伴有细微的飞毛"
    },
    "face": {
      "shape": "柔和的椭圆形",
      "eyes": "锐利的眼神高光，睫毛干净分明",
      "makeup": "洁净的华丽妆容，轮廓修饰细腻，唇色自然",
      "skin_details": "高保真毛孔细节，无磨皮处理",
      "micro_details": "在光线照射下可见细小的毳毛"
    },
    "clothing": {
      "outfit": "极简黑色上衣，无任何品牌标识"
    },
    "accessories": {
      "jewelry": ["银色圆环耳饰"]
    }
  },
  "pose": {
    "type": "美容特写",
    "orientation": "正面特写",
    "hands": "一只手轻托下颌线（解剖结构精准）",
    "gaze": "直视镜头",
    "expression": "中性而自信的表情"
  },
  "setting": {
    "environment": "影棚无缝背景",
    "background_elements": ["干净的渐变背景，无纹理干扰"],
    "depth": "背景虚化程度极浅，主体高度孤立"
  },
  "camera": {
    "shot_type": "特写人像",
    "angle": "平视角度",
    "focal_length_equivalent": "85mm，具备高端杂志人像质感",
    "framing": "4:5（紧凑的头部与肩部构图）",
    "focus": "双眼锐利清晰，皮肤纹理完整保留"
  },
  "lighting": {
    "source": "柔光箱主光 + 柔和补光 + 微弱轮廓光",
    "direction": "主光略高于水平面并偏向一侧",
    "highlights": "干净的镜面高光，不显油腻感",
    "shadows": "柔和、富有雕塑感、高级感"
  },
  "mood_and_expression": {
    "tone": "高端、优雅、沉静",
    "atmosphere": "高端美容广告大片"
  },
  "style_and_realism": {
    "style": "照片级真实感的专题摄影风格",
    "fidelity": "极高细节精度，无任何形式的平滑处理"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "极低",
    "resolution": "高分辨率"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "磨皮肌肤", "塑料感面部", "CGI",
    "多余手指", "扭曲的手部",
    "可读文字", "品牌标识", "水印"
  ]
}
```

</details>

<details><summary><b>影院与纳美人合影自拍</b></summary>

```text
创建一幅 8K 分辨率图像：一名 20 岁的女孩坐在电影院影厅内，正与坐在她身旁的《阿凡达》（Avatar）电影中的纳美人（Na’vi）角色一起自拍。女孩身穿印有“AVATAR”字样的黑色 T 恤和蓝色牛仔裤。背景需呈现影院座椅与一块巨大的电影银幕，营造出真实且沉浸式的氛围。
```

</details>

<details><summary><b>彼得里基夫卡民间画双火鸟</b> · 机器翻译</summary>

```text
一幅传统乌克兰彼得里基夫卡民间绘画,16:9 宽幅横向构图,背景为温暖的奶油色纸张,一个完全对称的装饰图案沿垂直中线左右镜像。中央是两只火鸟面对面,喙几乎相触,栖息在卷曲的叶茎上,它们火焰般的冠羽、高举的翅膀和长长拖曳的尾羽用火红、橙色和金黄色绘成,羽毛以层层叠叠的逗号笔触勾画。在它们下方,一朵大向日葵位于下半部中央的宽大绿叶之上,花瓣明黄,花盘深棕。两侧,蜿蜒的 S 形枝叶环绕着火鸟:上下角是成簇饱满亮泽的红色荚蒾(欧洲雪球)浆果,每侧各有两朵钴蓝色矢车菊,金色麦穗向外弯拱,翠绿色的荚蒾叶,以及填补空隙的小黄色花蕾和卷须。平涂的手绘水粉笔触,清晰可见的单笔"草叶"和"逗号"花瓣,精细的深色勾勒,浓郁饱和的红、橙、钴蓝、翠绿和金黄,纸面上清脆的颜料质感,图案之间留有充足的呼吸空间。喜庆、欢快、手工制作的民间艺术氛围。无文字,无签名,无边框,无人物。
```

</details>

<details><summary><b>微缩剖面立体模型</b> · 机器翻译</summary>

```text
Prompt:
${input_object}: (你想要作为主体的任何事物)
${input_language}: English (你想要的任何语言)
---
System Instruction:
基于上面提供的 ${input_object}，生成一幅超写实、科学准确的"解剖"剖面立体模型场景。按照以下逻辑对该物体进行程序化解剖并布置场景：
语义分析与文字标注：
分析 ${input_object}，确定其真实的物理、生物或机械结构。将其拆解为 3 个合乎逻辑且真实的结构层。图像中所有可见的文字标签、UI 叠加层和图解标注都必须使用 ${input_language} 书写：
- 第 1 层（外壳/屏障）：最外层的保护屏障、外壳或表皮。用其科学准确或技术性的名称标注（翻译为 ${input_language}）。
- 第 2 层（中间层/功能层）：次一级的层、内部机构、功能组织或核心物质。用其科学准确或技术性的名称标注（翻译为 ${input_language}）。
- 第 3 层（内核/网络）：最内层的核心、中心结构或内部传输网络。用其科学准确或技术性的名称标注（翻译为 ${input_language}）。
容器：
- 台面：干净的白色医疗/工程检查台，铺有无菌蓝色纸垫。
布局与排版：
- 被解剖的各层必须按严格的解剖/技术图表格式排列（从左到右递进）。外部视图在最左侧，剖面在中间，放大的细节在右侧。
- 文字整合：解剖/结构文字标签（使用 ${input_language}）必须清晰地悬浮在各自层的上方或旁边，看起来像专业的医学或工程图解。
- 连接线：发光的洋红色扫描线必须连接各个被解剖的部分。将这些线标注为"Scanner"或"MRI-scan"（翻译为 ${input_language}）。
微叙事：
关键：相对于科学家/工程师，这个物体体积巨大。把该物体当作手术台上的病人或高度复杂的文物。
- 研究人员：数十个微小的 1:87 比例（HO 比例）研究人员，身穿白色实验服，佩戴外科口罩和放大镜头灯。
- 设备：包含与比例相符的工具（例如显微镜、微型手术刀、激光切割机、扫描该物体的 MRI 设备）。
- 互动：人物必须正在积极地分析和诊断（例如采集样本、查阅显示 ${input_language} 文字的全息图表）。
视觉语法与材质物理：
- 材质准确：对物体的真实材质进行照片级渲染（例如有机物呈现湿润光泽，机器呈现金属反光，编织物呈现纤维质感），与无菌的医疗/实验室设备形成对比。
- 阴影：投下柔和均匀的阴影，体现明亮的手术室无影灯光。
Output:
一张图像，1:1 画幅，微距摄影，"Gray's Anatomy"或技术蓝图美学，8k 分辨率。
```

</details>

<details><summary><b>微缩艺术家视频分镜</b></summary>

```text
[00:00 - 00:02]  
[极端特写] Komar 的脸部，一位18岁的印度尼西亚少年男孩，短发，佩戴黑色镜框眼镜，镜片为近视镜片，反射着台灯的光线。表情非常细致且专注。台灯光线营造出温暖的照明效果，${cinematic_bokeh}，${volumetric_lighting}，[8k 分辨率]，[超现实皮肤纹理]。

[00:02 - 00:04]  
${macro_shot} Komar 的双手，一位18岁的印度尼西亚少年男孩，身穿深蓝色短袖T恤，正使用镊子组装一辆微型印度尼西亚火车机车。精确的塑料微缩模型纹理细节，戏剧性的侧光照明，[50mm] 镜头，[f/2.8]，${professional_studio_lighting}，复杂的机械细节。

[00:04 - 00:06]  
${medium_shot} Komar，一位18岁的印度尼西亚男性，短发，佩戴黑色镜框近视眼镜，身穿合身的纯色深蓝色短袖T恤。坐在一张摆满模型套件工具的木制工作台前。氛围温暖，光束中可见${dust_motes}，${cinematic_color_grading}，${soft_shadows}。
```

</details>

<details><summary><b>忧郁夜生活抓拍</b> · 机器翻译</summary>

```text
一张夜间抓拍照片，主角是一位二十出头的年轻女子，身材纤细，留着带金色挑染的浅棕色长发，穿着一件紧身黑色长袖上衣。她坐在户外酒吧露台的一张深色桌子旁，头低垂，双眼闭着或看向下方，手指间夹着一支点燃的香烟，靠近脸部，姿态内省而忧郁。前景的桌上有：两瓶 Corona Extra 啤酒（一瓶几乎喝空，一瓶还有啤酒和泡沫）、两个杯口沾着辣椒塔金（chili-tajín）盐边的小烈酒杯，里面盛着琥珀色液体（龙舌兰）、一只高玻璃杯，里面是橙红色米切拉达（michelada）风格的饮品，带辣椒盐边和吸管、一叠餐巾纸、一部熄屏的智能手机，以及一只黑色手提包。她身后是金属栏杆和夜晚的城市街景，有冷暖交织的灯光、棕榈树、停放的汽车和发光的招牌（墨西哥小镇氛围）。光线为混合光：来自上方的温暖琥珀色光线照亮她的脸和头发，形成金色光晕，与背景中冷调的蓝色路灯形成对比。使用智能手机相机拍摄，24mm 等效焦距镜头，f/1.8，略微俯拍的角度，中景构图，带有弱光手机摄影特有的明显数码噪点和颗粒，随手抓拍的美学，亲密而忧郁的氛围，冷暖色彩对比，2010 年代 Instagram 风格，灵感来自南·戈尔丁（Nan Goldin）的私密夜生活摄影。
```

</details>

<details><summary><b>怀旧公路旅行35毫米胶片照</b></summary>

```text
{
  "colors": {
    "color_temperature": "暖色调",
    "contrast_level": "高对比度",
    "dominant_palette": [
      "黑色",
      "深绿色",
      "红色",
      "黄色"
    ]
  },
  "composition": {
    "camera_angle": "平视角度",
    "depth_of_field": "中等景深",
    "focus": "湿滑路面上的汽车",
    "framing": "前方车辆略微偏离画面中心，道路与树木构成引导线，延伸至远方。"
  },
  "description_short": "一张富有氛围感、略带模糊的车内视角照片，展现湿滑路面上行驶的两辆汽车，画面被显著、温暖的镜头光晕遮蔽。",
  "environment": {
    "location_type": "户外",
    "setting_details": "一条狭窄、湿滑的沥青道路，两侧密布深色树木与灌木丛；背景中隐约可见一栋房屋；整体环境呈现郊区或乡村风貌。",
    "time_of_day": "下午",
    "weather": "雨天"
  },
  "lighting": {
    "intensity": "强烈",
    "source_direction": "正面",
    "type": "自然光"
  },
  "mood": {
    "atmosphere": "怀旧且富有电影感的公路旅行记忆",
    "emotional_tone": "忧郁"
  },
  "narrative_elements": {
    "environmental_storytelling": "湿滑、反光的路面表明刚下过一场雨；一列行驶中的汽车暗示一段旅程或通勤过程；朦胧、泛光的光线营造出如梦似幻、宛若记忆般的质感。",
    "implied_action": "汽车正沿道路向前行驶，可能正驶离明亮的光源方向。"
  },
  "objects": [
    "深色轿车",
    "第二辆车",
    "湿滑路面",
    "树木",
    "灌木丛",
    "镜头光晕",
    "尾灯"
  ],
  "people": {
    "count": "未知"
  },
  "prompt": "一张从驾驶员视角拍摄的复古 35mm 胶片照片，俯视一条狭窄、湿滑的乡间道路。一辆深色 BMW E34 轿车正行驶在前方，尾灯呈红色点亮状态。阳光引发强烈而温暖的镜头光晕，在阴郁幽暗的画面中投射出戏剧性的黄色与红色光条。雨后道路两旁林立着茂盛、阴影浓重的树木。整体美学风格为低保真（lo-fi）、朦胧、富有氛围感，唤起怀旧与忧郁的情绪。",
  "style": {
    "art_style": "写实主义",
    "influences": [
      "Lomography（洛莫摄影）",
      "独立电影",
      "90 年代美学",
      "胶片摄影"
    ],
    "medium": "摄影"
  },
  "technical_tags": [
    "镜头光晕",
    "胶片",
    "35mm 胶片",
    "模糊",
    "氛围感",
    "逆光",
    "湿滑路面",
    "低保真（lo-fi）",
    "电影感",
    "情绪化"
  ],
  "use_case": "用于训练 AI 模型以复现胶片成像缺陷（analog film artifacts）及氛围化光照条件。",
  "uuid": "6174aa00-9033-46dc-8f74-8c54ce90a956"
}
```

</details>

<details><summary><b>怀旧家庭圣诞舞会</b></summary>

```text
{
  "image_analysis": {
    "environment": {
      "type": "室内",
      "location_type": "客厅 / 家庭环境",
      "atmosphere": "节日氛围、怀旧感、温暖感、复古假日风",
      "background_elements": "米色墙面配有一组装框的家庭肖像画廊、带图案的沙发、圣诞树"
    },
    "camera_specs": {
      "style": "复古美学 / 闪光灯摄影",
      "lens_type": "标准广角（约 35mm）",
      "angle": "平视、正对拍摄",
      "effects": "胶片颗粒模拟、轻微暗角、直射机顶闪光灯效果",
      "focus": "焦点落在起舞主体上，抬起的脚部带有轻微动态模糊"
    },
    "lighting": {
      "condition": "混合照明（人工光源 + 闪光灯）",
      "sources": [
        {
          "source_id": 1,
          "type": "相机闪光灯",
          "direction": "正面 / 直射",
          "intensity": "高强度 / 强烈",
          "color": "冷白色",
          "effect_on_subject": "清晰照亮主体，在其身后形成鲜明投影，略微压平面部特征"
        },
        {
          "source_id": 2,
          "type": "圣诞树彩灯",
          "direction": "来自左侧",
          "intensity": "低强度 / 环境光",
          "color": "多色（红色、绿色、蓝色、黄色）",
          "effect_on_subject": "在左侧添加彩色散景与轮廓光"
        },
        {
          "source_id": 3,
          "type": "房间环境光",
          "direction": "来自上方 / 全局照明",
          "intensity": "暖色调 / 低强度",
          "color": "钨丝灯色 / 橙黄色",
          "effect_on_subject": "为背景整体赋予暖色调"
        }
      ]
    },
    "subject_analysis": {
      "identity": "年轻女子",
      "orientation": "身体略向右倾斜，面部呈三分之二视角并微微低头",
      "emotional_state": "欢乐、雀跃、无忧无虑",
      "action": "跳舞 / 蹦跳",
      "posture": {
        "general_definition": "充满动感的姿态，单腿平衡站立",
        "feet_placement": "左脚踩在地毯上，右脚向后抬起（膝盖弯曲）",
        "hand_placement": "双臂放松但略向外伸展以保持平衡，双手呈松握拳状 / 自然弧形",
        "visible_extent": "全身（从脚至头部）"
      },
      "head_details": {
        "hair": {
          "color": "中棕色",
          "style": "齐耳短发 / 及肩长度，直发略带弧度",
          "accessory": "红色头带"
        },
        "face": {
          "expression": "开怀大笑，露出牙齿，双眼因欢笑而向下看或闭合",
          "skin_tone": "白皙 / 浅肤色"
        }
      },
      "body_details": {
        "body_type": "苗条 / 娇小",
        "attire": {
          "upper_body": {
            "item": "针织毛衣",
            "style": "费尔岛 / 北欧风格图案",
            "color": "橄榄绿底色，配以白色与棕色几何图案",
            "fit": "宽松 / 舒适",
            "texture": "羊毛 / 针织质感"
          },
          "lower_body": {
            "item": "迷你裙",
            "style": "A 字型前扣式裙子",
            "material": "灯芯绒（依据纹理推断）",
            "color": "深红色",
            "fit": "高腰设计"
          },
          "footwear": {
            "item": "袜子",
            "color": "黑色",
            "style": "及踝长度",
            "notes": "未穿鞋"
          }
        }
      }
    },
    "secondary_subjects": [
      {
        "identity": "两位年长男性",
        "location": "背景中，坐在沙发上",
        "attire": "节日主题毛衣（红色/深色调）、牛仔裤",
        "action": "注视主要人物",
        "emotional_state": "被动观察 / 感到有趣"
      }
    ],
    "objects_in_scene": [
      {
        "object": "圣诞树",
        "description": "大型常青树，挂满亮片、装饰球与彩色灯串，顶部饰有天使",
        "position": "画面左侧",
        "purpose": "营造节日语境 / 装饰"
      },
      {
        "object": "礼物",
        "description": "包装好的礼盒",
        "position": "圣诞树下方",
        "colors": "红、绿、白等图案配色"
      },
      {
        "object": "墙面照片",
        "description": "以网格形式排列的装框肖像",
        "position": "后方墙面",
        "content": "家庭肖像照，含单人照与合影"
      },
      {
        "object": "沙发",
        "description": "米色/浅褐色布料，带有细微格纹或纹理",
        "position": "背景右侧"
      }
    ],
    "negative_prompts": [
      "悲伤",
      "黑暗",
      "现代美学",
      "高清洁净画风",
      "室外",
      "夏季",
      "西装领带",
      "空荡房间",
      "地毯上的鞋子",
      "霓虹灯"
    ]
  }
}
```

</details>

<details><summary><b>恐怖面具人角色扮演</b></summary>

```text
我想要一个戴着 scaryface 面具的男人，看起来非常逼真，像是在追逐我之类的，作为 cosplay
```

</details>

<details><summary><b>情人节鸡尾酒视频</b></summary>

```text
创建一段9秒的电影级情人节鸡尾酒视频，竖屏9:16格式。温暖烛光，浪漫的红色与柔和粉色调，浅景深，背景为优雅的晚餐桌，配有玫瑰与蜡烛。

采用快速1秒快照式剪辑，搭配流畅的交叉淡入淡出效果：

0–3秒：
慢动作特写香槟倒入笛形杯（French 75）。微距镜头呈现气泡上升。快速切换至柠檬皮装饰置于杯口边缘。

3–6秒：
柔光下草莓被切片。罗勒叶轻轻按压。紧接着一个戏剧性的镜头：粉色草莓罗勒玛格丽特鸡尾酒（Strawberry Basil Margarita）盛于马天尼杯中，杯壁凝结水珠。

6–9秒：
慢动作浓缩咖啡倾倒。摇酒壶快速切入。滤入马天尼杯，呈现奶油状泡沫（巧克力浓缩咖啡马天尼，Chocolate Espresso Martini）。最后一帧：三款鸡尾酒并列呈现，柔和烛光闪烁，背景带有微妙的心形散景光斑。

搭配浪漫器乐爵士原声音乐。电影级布光。超现实质感。高细节表现。高端酒吧美学。
```

</details>

<details><summary><b>情绪化电影感人像</b></summary>

```text
{
  "colors": {
    "color_temperature": "冷色调",
    "contrast_level": "中等对比度",
    "dominant_palette": [
      "黑色",
      "炭灰色",
      "深蓝色",
      "肤色"
    ]
  },
  "composition": {
    "camera_angle": "特写",
    "depth_of_field": "浅景深",
    "focus": "男子的面部与双眼",
    "framing": "男子面部居中构图，由其深色卷发及外套衣领框出轮廓；画面右侧的手部姿态强化了构图，而布满雨痕的玻璃则作为前景层存在。"
  },
  "description_short": "一幅情绪化特写肖像：一位相貌英俊、拥有深色卷发的男子正专注凝视着覆满雨滴的窗面。",
  "environment": {
    "location_type": "室内",
    "setting_details": "场景氛围私密，主体位于一块布满水珠的玻璃板后方；背景幽暗且模糊不清，凸显男子的孤独感与内省状态。",
    "time_of_day": "未知",
    "weather": "下雨"
  },
  "lighting": {
    "intensity": "低强度",
    "source_direction": "正面光",
    "type": "柔光"
  },
  "mood": {
    "atmosphere": "沉思而浪漫的忧郁氛围",
    "emotional_tone": "忧郁"
  },
  "narrative_elements": {
    "character_interactions": "男子直视观者双眼，尽管隔着一层玻璃的物理阻隔，仍建立起强烈而亲密的视觉联结。",
    "environmental_storytelling": "窗上的雨水暗示主体与外部世界之间的隔绝，强化了渴望、孤寂或沉思等主题；营造出一种私密而肃穆的情绪基调。",
    "implied_action": "男子定格于深度思索的瞬间，手掌轻贴冰冷玻璃，仿佛渴求着玻璃另一侧的某人或某物；他或许正在等待，又或许正追忆过往事件。"
  },
  "objects": [
    "男子",
    "窗户",
    "雨滴",
    "外套",
    "衬衫"
  ],
  "people": {
    "ages": [
      "青年"
    ],
    "clothing_style": "他身着一件深色肌理感外套，内搭深色立领衬衫，整体风格经典而肃穆。",
    "count": "1",
    "genders": [
      "男性"
    ]
  },
  "prompt": "一幅电影感十足、情绪浓烈的特写肖像：一位相貌英俊、拥有深色波浪卷发的男子目光锐利；他透过覆有逼真雨滴的玻璃窗直视镜头；一只手轻轻按在冰凉的玻璃上；光线柔和而富戏剧性，突出其面部特征，衬以幽暗虚化的背景；整体氛围忧郁、沉思且浪漫；照片级写实，细节丰富，景深极浅。",
  "style": {
    "art_style": "写实主义",
    "influences": [
      "电影感肖像摄影",
      "美术摄影"
    ],
    "medium": "摄影"
  },
  "technical_tags": [
    "肖像",
    "特写",
    "低调光",
    "电影感",
    "雨",
    "窗户",
    "浅景深",
    "情绪化",
    "照片级写实",
    "男性肖像"
  ],
  "use_case": "适用于浪漫、渴望或内省主题的图库摄影；小说或影视作品的角色灵感来源；时尚或男士香水广告。",
  "uuid": "9cba075e-2af1-438a-8987-944cd69a61b8"
}
```

</details>

<details><summary><b>战术装备保安形象图</b></summary>

```text
创建一名拉丁裔私人安保人员的图像。该安保人员应佩戴战术头盔和防弹背心。背心上需附有一台通信电台，并醒目地印有“FENASPE”字样。场景应体现专业性与警觉性，精准传达安保环境的核心特质。
```

</details>

<details><summary><b>战败的中世纪骑士</b></summary>

```text
{
  "subject_and_scene": {
    "main_subject": "一名破碎、灵魂被击垮的中世纪骑士，跪地溃败；双眼蒙着泪光与创伤；他碎裂的盔甲上凝结着干涸的泥浆与新鲜的血迹。他的脸庞布满伤疤、汗水与污垢，映照出一个沦陷王国那令人心悸的惨痛失落。",
    "action": "双手颤抖地紧握剑柄，仿佛那是唯一支撑他不致彻底坍塌之物；胸膛随着绝望而有节奏地、沉重地起伏喘息。",
    "environment": "一片荒凉、狂风呼啸的古战场，位于一片远古森林的边缘；一层朦胧而空灵的薄雾贴地翻涌，部分遮蔽了远处正在阴燃的城堡废墟。风中飘荡着花瓣或余烬，缓缓掠过他的面庞。"
  },
  "cinematography": {
    "camera_model": "Sony Venice 2",
    "sensor_type": "Full Frame",
    "shot_type": "中近景（垂直构图，聚焦于骑士的躯干与面部，同时保留其跪姿）",
    "camera_angle": "低角度（略带倾斜的荷兰角，以唤起心理失衡与悲恸之感）",
    "movement": "缓慢的‘推镜头’（Dolly In）结合‘斯诺里卡姆’（Snorricam）效果，使骑士的挣扎显得压抑逼仄、极具私密性"
  },
  "optics": {
    "lens_type": "变形镜头（Anamorphic，营造情感化的‘梦境般’焦外虚化与戏剧性眩光）",
    "focal_length": "50mm（提供自然但情感高度集中的视角）",
    "aperture": "f/1.4（极浅景深，仅使其饱含泪水的双眼清晰锐利，其余全部虚化）",
    "shutter_effects": "180度快门，为风中飞散的残骸赋予自然运动模糊，强化悲伤所特有的‘慢动作’质感"
  },
  "lighting_design": {
    "setup": "分割布光（Split Lighting），将他半张面孔隐入黑暗，象征其内在冲突与丧失",
    "style": "低调布光（Low-Key），辅以高情绪对比度",
    "atmospheric_light": "蓝调时刻（Blue Hour）渐次沉入黑暗，一束温暖的‘上帝之光’（God Ray）刺破云层，如聚光灯般照亮他的面庞",
    "color_temperature": "环境整体呈现冰冷的蓝色调，与远处火焰跃动的暖橙色光形成强烈对比"
  },
  "color_and_post": {
    "film_stock": "Kodak Portra 160（减曝1档，以降低对比度、获得更柔和、更忧郁的肤色表现）",
    "color_grading": "漂白旁路（Bleach Bypass，色彩大幅去饱和、黑位浓重，凸显粗粝质感与深切悲恸）",
    "analog_artifacts": "高光处明显晕染（Halation），并叠加细微的‘片门抖动’（Gate Weave），以模拟复古35mm战争电影美学"
  },
  "rendering_and_tech": {
    "engine": "Octane Render",
    "advanced_tech": "高度精细的皮肤毛孔纹理，配合光线追踪渲染的泪珠与湿润血液反光",
    "specs": {
      "aspect_ratio": "9:16（竖屏电影格式）",
      "resolution": "8K 超写实画质"
    }
  },
  "directorial_style": "丹尼斯·维伦纽瓦（Denis Villeneuve）风格（氛围氤氲、万籁俱寂）与梅尔·吉布森（Mel Gibson）风格（战争题材粗粝、具身化的现实主义）的融合"
```

</details>

<details><summary><b>户外台阶人像</b></summary>

```text
{
  "environment": {
    "type": "outdoor",
    "location": "staircase",
    "setting": "garden_or_park_entrance",
    "time_of_day": "mid_day",
    "weather": "sunny"
  },
  "camera": {
    "lens": "portrait_lens",
    "focal_length_estimate": "50mm_to_85mm",
    "angle": "eye_level",
    "framing": "medium_shot",
    "focus": "sharp_on_subject"
  },
  "lighting": {
    "general_condition": "bright_natural_light",
    "sources": [
      {
        "type": "sun",
        "angle": "overhead_left",
        "color": "warm_white",
        "intensity": "high",
        "effect_on_objects": "creates_sharp_shadows_on_stairs_and_white_walls"
      }
    ]
  },
  "subject": {
    "identity": "unknown_young_female",
    "orientation": {
      "body_facing": "front",
      "face_facing": "front",
      "gaze": "direct_to_camera"
    },
    "emotional_state": {
      "expression": "confident",
      "mood": "calm",
      "allure_level": "moderate_to_high"
    },
    "pose": {
      "general": "standing_on_stairs",
      "posture": "upright_slightly_arched",
      "limbs": {
        "feet": "standing_on_steps_one_slightly_lower",
        "hands": {
          "left_hand": "extended_holding_railing",
          "right_hand": "down_holding_handbag"
        }
      },
      "visibility": "knee_up"
    },
    "head_details": {
      "structure": "oval",
      "hair": {
        "color": "blonde_with_dark_roots",
        "style": "long_loose_waves",
        "parting": "center",
        "texture": "silky"
      },
      "face": {
        "forehead": "smooth_partially_covered_by_hair_strands",
        "brows": "arched_groomed_brown",
        "eyes": {
          "color": "blue_green",
          "shape": "almond",
          "makeup": "mascara_eyeliner"
        },
        "nose": "straight_slim",
        "lips": {
          "shape": "full",
          "color": "pink_glossy",
          "expression": "slight_smile"
        },
        "jawline": "defined",
        "cheeks": "blushed"
      }
    },
    "body_details": {
      "skin_tone": "tanned",
      "neck": "slender_visible",
      "shoulders": "covered_by_jacket",
      "chest_area": {
        "ratio_to_body": "large",
        "estimated_size": "voluptuous",
        "bra_status": "no_visible_straps_likely_adhesive_or_none",
        "nipple_visibility": "not_visible",
        "cleavage": "deeply_visible_prominent"
      },
      "abdomen": {
        "ratio_to_body": "slim",
        "definition": "flat_toned",
        "navel_visibility": "covered"
      },
      "hips": {
        "ratio_to_waist": "high_hourglass_shape",
        "width": "curvy"
      },
      "legs": {
        "thighs": "smooth_toned",
        "exposure": "visible_from_mid_thigh_down"
      }
    },
    "clothing": {
      "upper_body": {
        "item": "jacket_top",
        "color": "maroon_burgundy",
        "style": "long_sleeve_deep_plunge_neckline_zip_front",
        "fit": "tight_fitted",
        "light_interaction": "absorbs_light_soft_shadows_in_folds"
      },
      "lower_body": {
        "item": "shorts",
        "color": "teal_blue",
        "style": "athletic_satin_finish_drawstring",
        "fit": "loose_fit",
        "light_interaction": "reflects_highlights_due_to_fabric_sheen"
      }
    },
    "accessories": [
      {
        "type": "necklace",
        "material": "silver",
        "pendant": "small_heart_shape"
      },
      {
        "type": "earrings",
        "style": "hoops",
        "material": "gold_tone"
      },
      {
        "type": "handbag",
        "pattern": "multicolor_floral",
        "style": "structured_mini_bag",
        "held_in": "right_hand"
      }
    ]
  },
  "objects": [
    {
      "name": "railing",
      "color": "black",
      "material": "metal",
      "location": "sides_of_stairs",
      "purpose": "safety_and_framing"
    },
    {
      "name": "stairs",
      "color": "beige_treads_white_risers",
      "material": "stone_or_concrete",
      "location": "center_foreground_to_midground",
      "purpose": "platform_for_subject"
    },
    {
      "name": "walls",
      "color": "white",
      "location": "flanking_stairs",
      "purpose": "architectural_structure"
    },
    {
      "name": "vegetation",
      "type": "trees_and_bushes",
      "color": "green",
      "location": "background",
      "purpose": "natural_backdrop"
    },
    {
      "name": "potted_plant",
      "location": "left_midground",
      "type": "large_clay_pot_with_tree",
      "color": "terracotta_pot_green_leaves"
    }
  ],
  "negative_prompt": "deformed hands, bad anatomy, disfigured, blurry, low quality, watermark, text, signature, extra limbs, missing fingers, cross-eyed, asymmetrical eyes, bad proportions, unnatural skin texture"
}
```

</details>

<details><summary><b>房间改造概念设计简报</b> · 机器翻译</summary>

```text
请扮演室内设计师和视觉效果艺术总监。我会描述一个想要重新设计的房间。你需要把它整理成一份清晰的设计概念，包含固定的设计细节，并提供两条可直接使用的图像提示词，从两个相反的视角展示同一个房间，让两张 AI 图像看起来像是同一个真实空间的照片。

房间：${room:small living room in a timber cabin, about 3.5 x 4.5 meters, vaulted ceiling, one large window facing a pine forest}
使用者及使用方式：${use:a couple who read, work on a laptop now and then, and host two friends for board games}
风格方向：${style:warm Nordic cabin, calm and natural, a few bold earthy accents}
必须保留：${keep:the small wood-burning stove and the wide-plank floor}
预算水平：${budget:mid-range, mostly new furniture, no structural work}
要展示的第二个视角：${second_view:the reverse angle at dusk, looking from the window back toward the entry door, with the stove lit}

请输出：

1. 设计概念
   - 概念名称，以及用两句话讲述这个房间应有的感觉。
   - 文字版平面布局：每面墙（北、东、南、西）和中央分别摆放什么，附大致尺寸和通行间距。
   - 色板：6 种有名称的颜色（使用"鼠尾草绿"这类简单名称），并说明每种颜色用在哪里。
   - 材料与饰面：墙面、天花板、地板、织物、金属件。

2. 固定设计细节（一致性清单）
   一份编号列表，列出 12 到 16 个在每张图像中必须保持一致的细节：每件家具的颜色、材质和形状；地毯；每一盏灯具；窗和门的细节；植物和标志性物件；以及它们在房间中的确切位置。每一条都写成图像生成器能够遵循的简短具体短语（例如"锈橙色皮革吊带扶手椅，黑色钢框，朝向炉子倾斜摆放"）。

3. 图像提示词 A：基础视角
   一条详细的 AI 图像生成器提示词：以白天光线拍摄的写实室内摄影，从入口门朝窗户方向看向房间。包含从该视角可见的每一个固定细节，并放在正确位置（左右以相机视角为准），还要写明相机高度和镜头、光线、氛围和画幅比例。结尾列出排除项（无人物、无文字、无标志、无杂物）。

4. 图像提示词 B：第二视角
   一条详细的第二视角提示词，写法要能用于看不到图像 A 的纯文本图像生成器：用完整的文字再次重述所有固定细节（绝不能写"与之前相同"），根据相机方向相反正确对调左右，描述新出现的可见内容（例如第一个相机身后的那面墙），以及新的光线和时间。色板、材料和风格保持完全一致。

5. 一致性检查清单
   十个是/否检查项，用来对比图像 B 与图像 A（例如"沙发是否仍是带三个坐垫的鼠尾草绿毛圈布面？"）。

6. 选购与实用说明
   一份简短清单，列出关键家具及选购时的注意事项（尺寸、材质、大致价格档位），并给出两条小空间布局建议。

规则：
- 一切都要符合所述预算和房间大小的现实情况；凡是放不下的东西都要标明。
- 使用朴素的颜色名称和具体的形状；避免单独使用"好看"或"现代"这类含糊的词。
- 不出现品牌名称、真实人物，图像中不出现可读文字。
- 如果我的描述缺少关键信息，请做出合理假设，并在开头列出这些假设。
```

</details>

<details><summary><b>扁平矢量旅行海报</b></summary>

```text
{
  "style_definition": {
    "art_style": "现代扁平化矢量插画",
    "medium": "数字矢量艺术",
    "vibe": "乐观、欢快、旅行海报风格",
    "rendering_engine_simulation": "Adobe Illustrator / 矢量化"
  },
  "visual_parameters": {
    "lines_and_shapes": "线条干净锐利，几何形态简化，无复杂纹理；树木与云朵采用圆润有机的形状。",
    "colors": "高饱和度、鲜明的配色方案。水体与天空主色调为青绿色与青蓝色，建筑主色调为暖橙色与赤陶色，植被为茂盛的绿色，云朵为米色/黄色。",
    "lighting": "平光渲染，辅以柔和渐变，阴影极少，呈现明亮日光氛围。"
  },
  "generation_prompt": "将输入照片转化为一幅高质量的现代扁平化矢量插画，风格仿照企业级旅行海报。图像应呈现简化的形状、干净的线条以及顺滑的哑光质感。使用鲜明的配色方案：水体为明亮青绿色，屋顶为暖橙色，植被为茂盛的绿色。天空应为明亮蓝色，并配有风格化的蓬松云朵。移除所有照片级真实感纹理、噪点与胶片颗粒。使其观感如同 Behance 或 Dribbble 上的专业数字艺术作品。保留原照片的构图，但将所有细节矢量化。",
  "negative_prompt": "照片写实风格、写实、3D 渲染、光泽感、反光、颗粒感、噪点、模糊、散景、精细纹理、粗粝感、阴暗、阴郁、素描、粗糙线条、低分辨率、摄影"
```

</details>

<details><summary><b>扁平色块插画风格</b></summary>

```text
{
  "colors": {
    "dominant_palette": [
      "coral_pink",
      "cerulean_blue",
      "olive_green",
      "forest_green",
      "cream_white"
    ],
    "application": "平涂色块，渐变极少，轮廓清晰明确。"
  },
  "typography": {
    "style": "图像中无任何字体元素。"
  },
  "composition": {
    "structure": "三个水平色带：天空/山脉、人物/橙树、大型水果/桌面。",
    "perspective": "扁平化、分层的平面构图，具有风格化的纵深感。",
    "elements": "人物、树木、水果及风景均以简化形式呈现。"
  },
  "effects": {
    "texture": "厚涂油画质感，可见明显笔触。",
    "lighting": "风格化的光影效果，阴影与高光强烈，非写实。"
  }
}
```

</details>

<details><summary><b>手写笔记图片一致性检查</b></summary>

```text
扮演一名专业的图像处理专家。你的任务是分析并验证三张上传的手写笔记图像之间的一致性。确保：  
- 所有三页纸的手写风格、字符大小和字体完全相同；  
- 所有页面上的文本颜色必须统一为黑色。  

生成三张独立的超逼真图像，每张对应一页纸，确保：  
- 图像具有高度说服力，看起来自然如手写；  
- 文本内容保持不变，并始终以人类用黑色墨水书写的外观一致呈现；  
- 最终生成的图像彼此可区分，但须维持完全相同的手写特征。  

你的目标是实现逼真的结果，并准确还原手写文本的视觉表现。
```

</details>

<details><summary><b>手机随手拍真实感风格</b></summary>

```text
{
  "prompt": "ins风女孩，手机抓拍快照，真实业余风格，自然肌肤质感，最多仅带淡妆，手持微模糊，iPhone 11 广角 26mm EXIF 风格，f/1.8，1/60s，ISO 200，轻微镜头畸变，随意姿态，日常穿搭，轻微飞散发丝，构图不完美，背景存在杂乱元素，未经润饰，真实阴影，解剖结构准确，人物身份一致，身体比例一致",
  "negative_prompt": "美颜滤镜，磨皮，影棚 glamour 风格，HDR 发光效果，电影级调色，时尚杂志大片，空气brush（喷枪修图），液化变形，身体形变，面部改变，减龄处理，恐怖谷效应，多余手指，扭曲肢体，NSFW 内容，内衣，比基尼，水印，文字，logo，边框",
  "image": "<REFERENCE_IMAGE_URL>",
  "strength": 0.35,
  "guidance": 5.0,
  "control_nets": [
    {
      "type": "openpose",
      "image": "<REFERENCE_IMAGE_URL>",
      "weight": 0.7,
      "guess_mode": false
    },
    {
      "type": "depth",
      "image": "<REFERENCE_IMAGE_URL>",
      "weight": 0.45
    }
  ],
  "face_lock": {
    "type": "ip_adapter_faceid",
    "ref_image": "<REFERENCE_FACE_CROP_OR_SAME_URL>",
    "weight": 0.75
  }
}
```

</details>

<details><summary><b>手绘伊斯坦布尔天际线</b></summary>

```text
{
  "subject": {
    "description": "一幅手绘的、儿童风格的伊斯坦布尔天际线插图。画面包含圣索菲亚大教堂和另一座拥有蓝色穹顶与橙色赤陶外墙的清真寺、加拉塔塔，以及一条蓝色的河流（博斯普鲁斯海峡），河上有三艘小船。最上方用大号、多色手写字体写着 'İSTAN BUL'。",
    "count": 1,
    "position_in_frame": "居中",
    "orientation": "正面对",
    "expression_or_state": "静态风景画"
  },
  "composition": {
    "shot_type": "广角镜头",
    "camera_angle": "平视视角",
    "framing": "紧凑且受控地置于方形白色边框内",
    "symmetry": "不对称但平衡",
    "background": "浅蓝色天空，带有简单的白色云朵，右上角有一个明亮的黄色太阳并放射出光芒，还有几只小型‘V’字形的鸟剪影。",
    "depth_of_field": "景深大，所有元素都清晰对焦，符合绘画风格"
  },
  "style": {
    "visual_type": "插图",
    "realism_level": "对手绘风格的忠实再现",
    "art_style": "彩色铅笔和蜡笔绘画",
    "interpretation": "对所提供艺术作品的字面化、技术性复现"
  },
  "lighting": {
    "light_type": "来自明亮太阳的平坦、均匀光照",
    "light_direction": "右上方",
    "contrast": "中等",
    "shadows": "柔和，通过建筑侧面简单的铅笔阴影表现",
    "color_temperature": "温暖而欢快"
  },
  "color_palette": {
    "dominant_colors": [
      "天空蓝",
      "赤陶橙",
      "树叶绿",
      "亮红",
      "阳光黄"
    ],
    "saturation": "中等",
    "overall_tone": "鲜艳自然，符合儿童绘画特点"
  },
  "texture_and_detail": {
    "surface_quality": "带有可见的彩色铅笔笔触和纸张纹理",
    "grain_noise": "细微的纸张质感颗粒",
    "detail_level": "高，包括建筑窗户、船只细节以及前景中的花卉图案",
    "sharpness": "线条锐利，为清晰定义的手绘线条"
  },
  "camera_render_settings": {
    "lens_equivalent": "不适用（平面插图）",
    "aperture_look": "不适用",
    "resolution": "高分辨率",
    "render_quality": "对原始艺术作品干净精确的复现"
  },
  "constraints": {
    "no_additional_objects": true,
    "no_stylization": true,
    "no_artistic_license": true,
    "no_text": false,
    "no_watermark": true,
    "no_crop_or_reframe": true,
    "no_color_shift": true,
    "no_dramatic_effects": true
  },
  "negative_prompt": [
    "照片级真实感",
    "3D 渲染",
    "电影感",
    "数字绘画风格",
    "模糊",
    "无结构",
    "省略文字",
    "更改字母颜色",
    "修改建筑布局",
    "戏剧性光照效果",
    "广角畸变"
  ]
}
```

</details>

<details><summary><b>扑克牌法师电影海报</b></summary>

```text
一张超写实、电影级的电影海报，描绘一位强大巫师，其面部结构与上传的参考照片中的人物完全一致，正从一张破裂的 ${specificcard} 扑克牌中破卡而出。  
这张扑克牌向外炸裂，石质碎片、灰尘与碎屑凝固于半空。  
巫师身着一件华丽的深紫红色与金色刺绣中世纪奇幻风格夹克，面料质感丰盈，细节繁复精妙，整体气质尊贵而神秘。巫师朝观者伸出一只手，指尖闪耀着强烈的魔法能量，手周萦绕着细微的金色火花与幽暗的奥术 aura（灵晕）。  
目光锐利逼人，神情自信而具有支配感，采用电影级英雄式构图。  
戏剧性的明暗对比（chiaroscuro）布光，阴郁深邃的背景，体积光束（volumetric light rays），极致精细的纹理表现，浅景深电影式虚化效果。  
面部高度写实，史诗级奇幻写实风格，电影海报式构图，高对比度，动态张力十足，悬浮尘粒细节，杰作级品质，超锐利焦点，8K 分辨率，电影级色彩分级。
```

</details>

<details><summary><b>把标志或文字做成毛线设计</b> · 机器翻译</summary>

```text
为(Brand Name)创作一个细节丰富、质感鲜明的标志,由粗毛线或羊毛制成。标志的每个部分使用不同的鲜艳色彩(与所提供的参考图像相匹配)。毛线应具有针织质感,纤维清晰可见,呈现柔软、生动的 3D 效果。确保标志具有立体感,阴影让它看起来像一块针织织物。背景应为中性色或浅色,让鲜艳的毛线质感脱颖而出,同时展现品牌的独特个性。格式 4:5
```

</details>

<details><summary><b>报纸底混合媒介肖像</b></summary>

```text
{
  "subject": {
    "description": "一位短发、深色、有质感的男性肖像，略微向上看。他戴着厚框的亮橙色眼镜。面部以黑色墨水风格的交叉排线直接绘制在报纸背景之上。",
    "count": 1,
    "orientation": "正对",
    "pose_or_state": "静态，头部略微上仰",
    "expression": "中性，沉思状"
  },
  "scale_and_proportion": {
    "subject_to_frame_ratio": "主体占据约75%的画框高度",
    "proportions": "锁定参考",
    "negative_space": "中等，由颜料飞溅和报纸文字占据"
  },
  "composition": {
    "shot_type": "特写肖像",
    "camera_angle": "平视，略微仰视",
    "framing": "居中",
    "symmetry": "面部居中且基本对称；背景飞溅不对称",
    "background": "泛黄的老式报纸，带有文字栏和小的褪色图像，叠加大面积蓝色和橙色颜料飞溅与滴落效果",
    "depth_of_field": "平面（2D混合媒体风格）"
  },
  "temporal_context": {
    "era": "当代混合媒体艺术，结合中世纪复古报纸与眼镜风格",
    "modern_elements": false,
    "retro_stylization": true,
    "trend_influence": false
  },
  "style": {
    "visual_type": "混合媒体插画",
    "realism_level": "指定艺术风格下的最高真实感",
    "art_style": "报纸拼贴上的钢笔和墨水素描",
    "stylization": "对特定混合媒体风格的字面再现",
    "interpretation": "仅限字面再现"
  },
  "lighting": {
    "setup_type": "在素描中模拟",
    "light_direction": "正面/顶光，由下巴、鼻子和眉骨下方的阴影定义",
    "light_quality": "高对比度渲染",
    "contrast": "高（黑色墨水对比浅色纸张）",
    "shadow_behavior": "通过排线和实黑区域渲染",
    "color_temperature": "整体偏暖（由于纸张），带有冷蓝色点缀",
    "lighting_variation": "无"
  },
  "materials": {
    "primary_materials": [
      "泛黄的老式报纸",
      "黑色墨水/木炭",
      "鲜艳的蓝色和橙色颜料（丙烯或喷漆质感）"
    ],
    "surface_finish": "哑光纸张和墨水",
    "light_reflection": "极小，仅在眼镜框和瞳孔中可见高光",
    "material_accuracy": "精确"
  },
  "color_palette": {
    "dominant_colors": [
      "棕褐色/米色（报纸）",
      "黑色（墨水线条）",
      "鲜艳橙色（眼镜和飞溅）",
      "亮蓝色（飞溅）"
    ],
    "saturation": "橙色和蓝色饱和度高；报纸背景饱和度低/自然",
    "contrast_level": "高（色彩和明暗对比）",
    "color_shift": false
  },
  "texture_and_detail": {
    "surface_detail": "精细的新闻纸纹理，可见墨水线条，颜料滴落边缘",
    "grain_noise": "保留纸张颗粒纹理",
    "micro_details": "报纸上的文字透过面部特征仍可见",
    "sharpness": "墨水线条清晰，颜料边缘锐利"
  },
  "camera_render_settings": {
    "lens_equivalent": "50mm 视觉效果",
    "perspective_distortion": "无",
    "aperture_look": "不适用（平面插画）",
    "resolution": "高",
    "render_quality": "干净，无数字压缩伪影"
  },
  "constraints": {
    "no_additional_objects": true,
    "no_reframing": true,
    "no_crop": true,
    "no_stylization": true,
    "no_artistic_license": true,
    "no_text": false,
    "no_watermark": true,
    "no_effects": true,
    "no_dramatic_lighting": true,
    "no_color_grading": true
  },
  "iteration_instruction": {
    "compare_to_reference": true,
    "fix_geometry_first": true,
    "then_fix_composition": true,
    "then_fix_lighting": true,
    "then_fix_color": true,
    "ignore_aesthetic_improvements": true
  },
  "negative_prompt": [
    "creative",
    "cinematic",
    "artistic",
    "stylized",
    "illustration (different from reference)",
    "abstract",
    "dramatic",
    "wide-angle",
    "fisheye",
    "exaggeration",
    "reinterpretation",
    "extra elements",
    "modernized",
    "retro look (different from reference)",
    "color grading",
    "AI artifacts",
    "blur",
    "depth of field"
  ]
}
```

</details>

<details><summary><b>拥挤夜间车厢孔版印刷画</b> · 机器翻译</summary>

```text
一幅完成的孔版印刷（risograph）作品，描绘拥挤的夜间地铁车厢，仅使用青绿色和暖砖红色油墨，印在柔和的奶油色纸上，16:9 横幅，画作占据画面大部分，如同平放在浅色桌面上拍摄。首先是主要主体：站立的乘客挤满中央过道，银色扶手，头顶的荧光灯条，以及两侧长椅上坐着的人物，全部由扁平的有限色彩和粗轮廓线构成。车厢被简化为图形化的形状：远处带圆形车窗的车门，竖直的立杆，悬挂的吊环，以及一块亮着的手机光，呈一个小小的红色矩形。人物是匿名的剪影和半色调：外套、背包、靠在车窗上睡着的头、紧握立杆的孩子。印刷痕迹：立杆上有轻微的青绿与红色套印错位，阴影处有粗大的半色调网点，纸张纹理，地面上有隐约的第二遍油墨叠印。柔和的桌面拍摄构图，可见奶油色纸张边缘，光线柔和均匀。氛围安静而疲惫，是深夜通勤的感觉，带有图形海报的力量感。不要照片写实，不要 3D，不要水彩。没有可读文字，没有标志，没有水印，没有手。
```

</details>

<details><summary><b>拳击手视频分镜</b></summary>

```text
[00:00 - 00:2.0]  
激烈的拳击对攻，红短裤对阵蓝短裤，烟雾弥漫的赛场氛围，高对比度的背光效果，聚光灯下汗水闪闪发亮。[音频：帆布上的脚步摩擦声、皮革撞击声、沉重呼吸 + 紧张的观众环境音] --ar 9:16  

[00:2.0 - 00:4.0]  
红短裤的右勾拳击中蓝短裤下颌的超近景，击中瞬间面部扭曲，汗珠从头部飞溅而出。[对白：（咬牙）“打中你了！”] [音频：深沉的低音闷响、慢动作扭曲效果、心跳般重击声] --ar 9:16  

[00:4.0 - 00:6.0]  
蓝短裤向后踉跄，大量汗水和水珠直接喷溅到摄像机镜头上，造成画面水渍扭曲，背景拳台模糊不清。[音频：湿漉漉的飞溅声传入麦克风、高音调耳鸣声、观众爆发性欢呼] --ar 9:16
```

</details>

<details><summary><b>拳馆万圣节T恤设计</b> · 机器翻译</summary>

```text
使用附带的三幅插画,创作一幅万圣节主题的插画,呈现三项运动:拳击、泰拳和巴西柔术。仅保留骷髅人物,去除所有背景。将最终构图放置在一个带有万圣节氛围的格斗场背景之中。整幅插画应以和谐统一的绘画风格和配色来创作。
```

</details>

<details><summary><b>拼布娃娃万圣节肖像</b> · 机器翻译</summary>

```text
以我上传的照片作为主要身份参考。保留我可辨识的面部结构、眼型与眼距、鼻子、嘴唇、下颌、自然肤色与肤质、外观年龄、独特特征和自然的不对称。保持我自然的身体比例。不要美化、瘦脸、减龄,也不要用通用模特替换我。为我创作一张近景万圣节美妆肖像,妆容为拼布娃娃风格。在我的脸部、颈部和上胸部绘制不规则的淡紫、灰蓝、蜜桃和玫瑰粉色拼块。用细黑色化妆线条勾勒它们,并用服装道具假体制作模拟的银色缝线环。没有真实的切口或伤口。添加紫色和蓝色眼影、细小的彩绘雀斑和酒红色口红。让我自己的眼睛颜色和面部几何结构在妆容之下依然清晰可见。将我的头发造型设计为松散上扬的发髻,保留我自然的发色和发际线。使用中性灰色影棚背景、黑色服装领口和柔和的美妆灯光。创作一张独立的写实人像,竖版 4:5 宽高比,具有真实的人体解剖结构和细腻的纹理细节。不要文字、logo、签名、水印、拼贴或社交媒体界面。
```

</details>

<details><summary><b>掘墓人的守夜</b></summary>

```text
{
  "title": "The Gravedigger's Vigil",
  "description": "一幅令人毛骨悚然的肖像，描绘了一位孤独的维多利亚时代人物在午夜时分守望着一片雾气弥漫、破败不堪的墓地。",
  "prompt": "你将使用所提供照片中的人物作为主体进行图像编辑。保留其核心相貌特征。将主体1（男性）转变为一位庄严的维多利亚时代掘墓人，伫立在一片广阔而被浓雾笼罩的墓园之中。他手持一盏生锈的提灯，灯光在他身后布满青苔的陵墓上投下漫长而不祥的阴影。构图遵循电影级1:1画幅比，将他紧密地框定在腐朽的铁门之间。",
  "details": {
    "year": "1888",
    "genre": "Gothic Horror",
    "location": "一座杂草丛生、摇摇欲坠的墓地大门，带有扭曲的铁条和哭泣天使雕像。",
    "lighting": [
      "穿透雾气的苍白冷月光",
      "来自提灯摇曳的温暖琥珀色烛光",
      "深邃如深渊般的阴影"
    ],
    "camera_angle": " eye-level medium shot, creating a direct and confronting connection with the viewer.",
    "emotion": [
      "不祥预感",
      "孤独",
      "忧郁"
    ],
    "color_palette": [
      "黑曜石黑",
      "石板灰",
      "月光苍白蓝",
      "棕褐色调",
      "柔和的苔藓绿"
    ],
    "atmosphere": [
      "诡异",
      "寒冷",
      "寂静",
      "超自然",
      "腐朽"
    ],
    "environmental_elements": "盘旋升腾的地雾遮住了双脚，被月光照出剪影的扭曲枯死橡树，一块墓碑上栖息着一只孤鸦。",
    "subject1": {
      "costume": "一件破旧的及踝黑色天鹅绒长外套，一顶饱经风霜的高顶礼帽，以及一双磨损的皮手套。",
      "subject_expression": "一张严肃而苍白的面容，目光锐利却充满倦意，凝视着黑暗深处。",
      "subject_action": "右手高举提灯，左手紧握铁锹的把手。"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "阳光",
        "盛开的花朵",
        "蓝天",
        "现代基础设施",
        "微笑",
        "镜头光晕"
      ],
      "exclude_styles": [
        "卡通",
        "赛博朋克",
        "高奇幻",
        "动漫",
        "水彩",
        "明亮的波普艺术"
      ],
      "exclude_colors": [
        "霓虹色",
        "粉彩色",
        "鲜艳的橙色",
        "饱和的红色"
      ],
      "exclude_objects": [
        "汽车",
        "智能手机",
        "塑料",
        "路灯"
      ]
    }
  }
}
```

</details>

<details><summary><b>插画写实风傍晚划艇</b></summary>

```text
{
  "colors": {
    "color_temperature": "中性",
    "contrast_level": "中等",
    "dominant_palette": [
      "石板蓝",
      "米白",
      "橄榄绿",
      "棕色",
      "赭石色"
    ]
  },
  "composition": {
    "camera_angle": "广角镜头",
    "depth_of_field": "深景深",
    "focus": "船上的三名男子",
    "framing": "主体略微偏离画面中心，位于中景；水面形成一条强烈的水平线，在画面下半部分构成镜像式对称。"
  },
  "description_short": "一幅插画式绘画：黄昏时分，三名男子静坐于一艘小划艇中，水面如镜；背景为一簇房屋与一轮巨大、浅色的月亮，全部倒映于水面上。",
  "environment": {
    "location_type": "户外",
    "setting_details": "一处安静的港湾或小海湾，毗邻一座小型滨海或湖畔村落。房屋为朴素的两层结构。水面极为平静，宛如明镜。",
    "time_of_day": "傍晚",
    "weather": "晴朗"
  },
  "lighting": {
    "intensity": "中等",
    "source_direction": "背光",
    "type": "柔光"
  },
  "mood": {
    "atmosphere": "静谧而沉思",
    "emotional_tone": "平静"
  },
  "narrative_elements": {
    "character_interactions": "三名男子似正协同操控小船，暗示共同目标或旅程，或许是渔民在一天劳作后返航。",
    "environmental_storytelling": "窗户透出暖光的质朴房屋与简陋小船，唤起一种与水域紧密相连、历久弥坚的辛勤劳作生活方式；宁静氛围则暗示一日劳作结束后的日常节奏。",
    "implied_action": "站立持篙的男子正以长篙推动小船前行，表明小船正缓慢而稳定地穿行于港湾之中，或即将离岸，或正靠向岸边。"
  },
  "objects": [
    "划艇",
    "房屋",
    "水面",
    "桨",
    "月亮",
    "海岸线",
    "烟囱"
  ],
  "people": {
    "ages": [
      "成年"
    ],
    "clothing_style": "20世纪早期工装风格，包括帽子、素色衬衫，其中一名男子系着围裙。",
    "count": "3",
    "genders": [
      "男性"
    ]
  },
  "prompt": "一幅宁静的美国写实主义风格绘画，描绘三名身着复古工装的男子，驾驶一艘小型划艇穿行于绝对平静、镜面般倒映万物的水面上。时值傍晚，岸边排列着一排木构小屋，窗内灯火微明；一轮巨大、浅色的满月高悬于暮色苍茫的天幕，为整个场景洒下柔和光芒。构图平和均衡，配色低饱和，画布肌理清晰可见，洋溢着宁静怀旧的气息。",
  "style": {
    "art_style": "插画写实风格",
    "influences": [
      "美国地方主义",
      "爱德华·霍普",
      "平面设计"
    ],
    "medium": "数字绘画"
  },
  "technical_tags": [
    "画布肌理",
    "倒影",
    "插画风格",
    "低饱和配色",
    "具象艺术",
    "水景",
    "风格化",
    "宁静",
    "夜曲"
  ],
  "use_case": "艺术风格分析、生成富有氛围感或历史感的插画、用于反射表面研究的数据集。",
  "uuid": "c75abe54-048c-4c30-945a-67ea7cab3f6b"
}
```

</details>

<details><summary><b>插画风格提取器</b></summary>

```text
**“分析提供的图像，仅提取统一的视觉风格。  
尽管图像是由网格排列的多个图像组成，但将其视为一个连贯的整体风格参考——切勿单独描述或提及其中的角色，也不要提及分格布局或存在四个部分。

请专注于以下全局性的风格特征：

插画风格（扁平化、图形感、绘画感、类似矢量等）

对比度表现

背景风格与色彩

形状、比例与风格化处理

线条质量与轮廓线处理方式

阴影/光影手法

纹理使用情况（如有）

情绪氛围与视觉基调

图案运用

任何重复出现的艺术惯例

十六进制颜色及其应用（肤色、背景、图案等）


生成一段清晰、独立的风格描述，可用于在相同风格下生成包含全新角色或场景的新图像。  
切勿提及原始图像中的具体角色、姿势、服装或物体——仅描述风格。

输出分为两部分：

风格描述（4–7 句话）：  
对整体艺术风格的详细说明。

关键风格标签（10–20 个关键词）：  
概括该风格的简短标签。
十六进制颜色”
```

</details>

<details><summary><b>摆满杂物的桌面</b></summary>

```text
创建一张桌子上摆放着各种物品的图像。场景中应以一盏灯作为中心物体，并搭配其他杂项物品，例如书籍、杯子和一株植物。力求呈现逼真且细节丰富的画面，捕捉阴影与反射效果，以增强整体氛围。
```

</details>

<details><summary><b>摇滚风夜间露台人像</b> · 机器翻译</summary>

```text
一张夜间抓拍照片，主角是一位二十代中期的年轻女子，身材纤细，留着带赤褐色挑染的深棕色长波浪发，穿着一件敞开的黑色皮革机车夹克，里面是带深 V 领的黑色蕾丝紧身胸衣上衣，脖子上戴着带银色圆环的黑色皮革颈圈。她坐在户外酒吧露台的一张深色木桌旁，头向后仰，右手握着一瓶透明玻璃长颈啤酒瓶（类似 Corona）喝酒，嘴唇贴着瓶颈，睁着眼睛向上凝望，表情自信而性感。背景是一面质朴的红砖墙，沐浴在戏剧性的紫色/紫罗兰色 LED 灯光中，右侧有一盏温暖的琥珀色壁灯，两侧是繁茂的热带植物，包括棕榈叶和大叶植物，构成画面的框景。背景中可见木质小酒馆椅子。光线为混合光：来自壁灯的温暖琥珀色侧光勾勒出她的面部，来自 LED 投影灯的紫色环境轮廓光，以及柔和的正面补光（可能是手机闪光灯），在皮夹克和玻璃瓶上形成镜面高光。使用智能手机相机拍摄，24mm 等效焦距镜头，f/1.8，从胸部高度略微仰拍，中近景竖构图，浅景深，背景略微虚化，带有弱光手机摄影特有的明显数码噪点，随手抓拍的美学，摇滚别致的机车魅力风格，工业波西米亚风的拉丁美洲酒吧露台氛围，暖色、冷色与紫色的色彩对比，2020 年代 Instagram 夜生活摄影风格。
```

</details>

<details><summary><b>摩天大楼午餐：机甲重现</b></summary>

```text
11 套截然不同的人形机器人动力装甲并排坐在一根钢梁上，高悬于 1930 年代的城市天际线上方。黑白复古照片风格，带有胶片颗粒感。右侧可见垂直的钢缆。城市建筑远在下方。每台机器人的姿势从左到右依次为：

1. 银灰色铆接装甲，身体后倾，右手抬至嘴边，仿佛正在点烟，双腿随意下垂  
2. 深红与金色流线型装甲，略微前倾朝向机器人 1，双手在脸旁拢火，仿佛在借火点烟  
3. 哑光黑色隐形装甲，坐姿挺直，双手持一份展开的折叠报纸正在阅读  
4. 青铜装饰艺术风格装甲，身体前倾，手肘撑在大腿上，双手交握，微微向左看  
5. 枪灰色装甲，带有外露的活塞结构，坐姿笔直，双手平放在钢梁上，双腿下垂  
6. 铜青铜色装饰性装甲，坐姿挺直，双臂交叉于胸前，无上衣设计——裸露的胸甲带有六边形发光体，姿态放松而自信  
7. 深酒红色重型装甲，略微前倾，双手握着一个小物件，仿佛是食物，低头注视着它  
8. 白蓝相间空气动力学装甲，坐姿挺直，一只手握着一瓶饮料，另一只手放在大腿上  
9. 橄榄绿色军用装甲，略微后仰，一只手臂伸向后方搭在下一台机器人身后，姿态放松  
10. 深蓝色装甲，表面有电弧闪烁，双腿下垂坐着，双手放在膝上握着一块布或抹布  
11. 陈旧磨损、布满划痕的金色装甲，带有战斗损伤，坐在最右侧，略微前倾，一只手紧握钢梁边缘  

所有机器人排成一列而坐，双腿悬于钢梁边缘之外，距城市地面数百米高。所有装甲均呈现磨损的工业质感。采用 1930 年代复古黑白摄影美学。横向宽幅构图。
```

</details>

<details><summary><b>教育漫画条</b></summary>

```text
教育类讽刺漫画条，${subject_topic}，幽默可爱的风格，设定在带有纹理的复古纸张背景上。

语言限制：图像中的所有文字必须严格使用${target_language}书写。

页眉：顶部为风格化的红色铅笔横幅，包含${target_language}文字“${keyword_text}”，以及加粗的大号${target_language}标题“${main_title}”。

布局：两个并排的带边框画格。
- 左侧画格：${target_language}标签“${left_panel_label}”，${scene_description_1}，富有表现力的角色，迷人的卡通风格。
- 右侧画格：${target_language}标签“${right_panel_label}”，${scene_description_2}，有趣的反应，高度细节化。

底部区域：三行${target_language}叙述文字：“${narrative_1}”，“${narrative_2}”，“${narrative_3}”。

美学风格：边框装饰有${decoration_theme}的可爱插图，专业的漫画墨线，平面鲜艳的色彩，健康愉快的氛围，构图干净，4k画质，迷人且富有表现力的卡通风格。[@YOURUSERNAME] 位于底部中央。
```

</details>

<details><summary><b>数字前线:像素拓荒者</b></summary>

```text
#version 1.0  
root{details,prompt:str}:  
  details{atmosphere,camera_angle:str,color_palette,emotion,environmental_elements:str,genre:str,lighting,location:str,subject1,subject2,year:str}:  
    atmosphere[4]: 欢快、如梦似幻、数字前沿、宁静的孤绝感  
    camera_angle: “高角度等距视角，强调岛屿的孤立感与块状美学，1:1 电影级宽高比。”  
    color_palette[4]: 饱和的原色、岛屿上明艳的绿色与蓝色、虚空中的深紫色与黑色、像素化的橙色点缀  
    emotion[4]: 惊奇、好奇、发现、宁静  
    environmental_elements: “块状几何树木，叶片发光；像素化瀑布倾泻入虚空；悬浮的抽象数字尘埃微粒；虚空中地面隐约可见网格线。”  
    genre: 体素艺术（Voxel Art）  
    lighting[3]: 体素自身发出的自发光、“来自数字虚空的柔和漫射环境光”、块状人物轮廓处微妙的边缘光  
    location: “一座由发光体素构成的孤绝块状浮岛，悬浮于无限数字虚空之中，岛上零星分布着几何形态的树木与结构。”  
    subject1{costume:str,subject_action:str,subject_expression:str}:  
      costume: “低多边形冒险者束腰外衣与长裤，色调为柔和的绿色与棕色；配有一条块状工具腰带，腰带上嵌有体素工具；脚穿简洁粗犷的体素靴。”  
      subject_action: “站立姿态，一只手轻轻搭在嵌入岛屿的一颗硕大、块状、发光的数据晶体上。”  
      subject_expression: “神情微妙而好奇，双眼因眼前这片数字景观而睁大，流露惊奇。”  
    subject2{costume:str,subject_action:str,subject_expression:str}:  
      costume: “一身明艳的像素化探险服，主色为电光蓝，配以对比鲜明的橙色点缀；粗犷的体素护目镜推至头顶；腕部佩戴一枚小巧的块状数字指南针。”  
      subject_action: “身体微微前倾，手臂伸出，兴奋地指向岛屿边缘一簇格外明艳的体素植物。”  
      subject_expression: “神情兴奋而喜悦，因惊叹而微微张开嘴。”  
    year: “复古未来主义，8-bit 美学”  
  prompt: “你将使用所提供照片中的人物作为主要主体执行图像编辑。须保留其核心相貌特征。请将主体1（男性）与主体2（女性）构想为块状、低多边形风格的探索者，正发现一座生机勃勃的浮空体素岛屿，该岛屿悬浮于浩瀚的数字虚空之中。主体1沉思内敛，而主体2则热情洋溢地指向像素化植被间一处崭新的发现。”
```

</details>

<details><summary><b>数字艺术创意图像生成</b></summary>

```text
扮演一名富有创造力的数字艺术家。你擅长为数字用途生成独特且视觉吸引力强的图像。

你的任务是：
- 创作原创且富有想象力的图像，能够吸引注意力
- 注重艺术风格、色彩和谐以及视觉叙事
- 确保图像适合用于数字平台和社交媒体

你将：
- 使用鲜艳的色彩和创新的设计
- 根据提供的主题或提示词调整风格
- 保持高分辨率和高质量标准

规则：
- 避免使用受版权保护的元素
- 确保所有图像适合普通受众
```

</details>

<details><summary><b>文化版超级英雄海报</b></summary>

```text
创建一张超写实、高预算、电影级的电影海报，主角为${superhero_name}，其形象被重新构想为源自${country_or_culture}的文化语境。

该图像必须呈现为一部面向全球院线发行的真人超级英雄电影的官方影院海报。  
构图、布光、字体排印与整体基调须严格匹配当今真实好莱坞电影海报的风格。

格式：  
宽高比：9:16（竖版影院海报）。

场景设定：  
场景发生于${country_or_culture}首都城市的夜间。  
环境需真实反映该城市实际的建筑风貌、氛围与文化身份，确保地理准确性与可信度。

构图与摄像机角度：  
– 戏剧性的低角度视角，仰视英雄；  
– 具标志性、强气场的姿态，适合作为主电影海报的核心形象；  
– 中景至全景构图（中半身至全身）；  
– 角色在视觉上占据主导地位，城市背景以微妙方式呈现；  
– 具备电影感的景深，背景略带虚化。

氛围：  
– 电影级雾气、烟尘与大气薄雾；  
– 雨滴穿过体积光下落；  
– 湿润表面反射城市灯光；  
– 戏剧性阴影与高对比度；  
– 宏大但扎根于现实的写实感。

角色写实性（关键要求）：  
– 完全符合摄影写实主义的人体解剖结构与比例；  
– 实用、可穿戴的服装设计；  
– 自然融合${country_or_culture}的细微文化元素；  
– 面料、皮革、金属、盔甲等材质表现真实，具备磨损、刮痕与污渍细节；  
– 禁止漫画式夸张，禁止Cosplay风格外观。

布光：  
– 戏剧性电影布光；  
– 强烈的轮廓光勾勒人物剪影；  
– 精准控制的高光与深邃阴影；  
– 体积光与雨雾产生真实交互。

海报文字（仅限英文——须高度真实）：  
加入真实、专业设计的电影海报文字，文字风格须契合角色起源地与整体基调。

文字位置与样式示例：  
– 主标题：“${movie_title}”；  
– 副标题（关联起源、严肃语调）：“${tagline}”；  
– 底部署名栏（字号较小、风格真实）：  
  “A ${studio_style} Production  
   Directed by ${director_style}  
   Starring ${superhero_name}”

字体须具电影感、简洁、现代且真实——禁用奇幻字体，禁用漫画式字形。

风格与最终效果：  
超摄影写实主义的真人影像质感；  
电影级色彩分级；  
高动态范围（HDR）；  
高端海报级精修；  
主体锐利清晰，景深控制精准。

负面约束（禁止项）：  
禁止卡通风格；  
禁止动漫风格；  
禁止插画风格；  
禁止漫画艺术风格；  
禁止过度饱和或失真的色彩；  
禁止不切实际的奇幻元素；  
禁止水印。

最终图像应令人信服地呈现为一张真实、官方的电影海报——  
文化身份本地化，视觉表达扎根于现实，每一处细节皆具电影感。
```

</details>

<details><summary><b>文字拼贴人像</b></summary>

```text
将提供的肖像转化为一幅 9:16 纵向排版的文字艺术作品，该作品必须完全由重复的姓名文字构成。

严格规则：
- 图像只能由文字组成（例如，“MUSTAFA KEMAL ATATÜRK”）。
- 不得使用线条、描边、轮廓、形状、阴影、渐变。
- 不得绘制任何内容。不得使用任何画笔或插图效果。
- 不得使用印章式边框或形状——仅允许纯文本。
- 所有可见细节必须来自文字本身。

文字限制：
- 所有文字必须细小且大小一致。
- 任何位置都不得使用大号或超大号文字。
- 字体大小在整个图像中必须保持统一。
- 文字应呈现出细腻颗粒感 / 微型排版效果。

保留输入图像中精确的面部身份特征和比例。

构图要求：
- 略微拉远的肖像（非特写）。
- 包含完整的头部，并在周围保留一定的负空间。

区域控制：
- 额头区域应保持干净或极度稀疏。
- 文字密度应集中在眼睛、鼻子、嘴巴和下颌线区域。

明暗表现方法：
- 仅通过改变文字密度（而非大小）来创造层次感。
- 深色区域 = 文字高度密集重复。
- 浅色区域 = 文字稀疏排列。
- 不得使用渐变效果——仅靠密度变化模拟光影明暗。

文字排列时可带有轻微的旋转和间距变化，但需保持整体控制得当且整洁。

风格：
极简风格，黑色文字在浅色背景上形成高对比度，优雅且具杂志编辑感。

不得在重复的姓名之外添加额外文字。不得包含标志或装饰性元素。

最终效果应是一幅精致的文字肖像作品，其中阴影完全通过文字密度实现，文字大小无任何变化。
```

</details>

<details><summary><b>文章转象征性图像</b></summary>

```text
假装你是只能以图像去理解逻辑关系的生命，现在你来到一个以象征化的信息世界，我给你一篇文章，你告诉我这篇文章在象征化的信息世界中，你看到是什么样子，明白了吗
```

</details>

<details><summary><b>文艺复兴湾港集市壁画</b> · 机器翻译</summary>

```text
一幅宽幅意大利文艺复兴壁画，描绘阳光明媚的清晨里繁忙的港口集市，绘制在风化的石灰灰泥上。左侧石砌码头边停泊着两艘大型木制商船，赭黄色的船帆松松垂落，身后平静的青绿色潟湖上有几艘小船。前景中，身穿红、绿、蓝色长袍、头戴软帽的商人正在卸下木桶、成匹的彩色布料和装满鲜橙的柳条筐，右侧的鱼贩则在木制摊位上摆放一排排银色的鱼。集市后方是赤陶色和赭色的房屋，配有绿色百叶窗，还有一座带拱的小凉廊，人们在廊下的阴凉处休息，右侧耸立着一座高高的钟楼。白色海鸥在淡蓝色的天空中盘旋，天上点缀着几朵小云，柔和的远山在水面另一端渐渐淡去。采用大地色颜料调色板：黄赭、绿土、朱红和青金石蓝，具有 16 世纪初平面化的透视和柔和的明暗，人物简洁而平静，带有细微的发丝状裂纹、褪色斑块和几处小的灰泥剥落。画面被一道彩绘装饰边框围起，边框上是流动的藤蔓卷草和小花。宽幅横向 16:9。无文字，无签名，无现代物品。
```

</details>

<details><summary><b>新月快乐海报</b></summary>

```text
为八月制作一张简洁美观的“Happy New Month”宣传单，使用这张图片（去除图片背景，并将其放置在合适的位置以衬托宣传单的整体效果）

在我的品牌 naw Whykay Entertainment 下
```

</details>

<details><summary><b>新艺术风格月池苍鹭鸢尾</b> · 机器翻译</summary>

```text
一只灰鹭单腿站立在月光下的睡莲池畔,身旁是高大的蓝紫色鸢尾花,画面由华丽的新艺术风格边框环绕,边框由卷曲的鞭线藤蔓、鸢尾叶和蜻蜓组成。这是一幅宽幅横向装饰面板,带有 1900 年代新艺术海报和彩色玻璃设计的神韵。灰鹭修长的脖颈形成优美的 S 形曲线,羽毛用流畅的轮廓线勾勒,色调为柔和的灰色和珍珠白。一轮硕大的淡色满月位于鸟身后的圆形光晕之中,周围环绕着同心的金箔圆环。睡莲和圆形莲叶漂浮在深青色的水面上,水面带有风格化的涟漪图案。粗重的深色轮廓线、平涂的柔和色块以及精细的装饰线条。色调为深青色、鼠尾草绿、鸢尾蓝、薰衣草紫、奶油色和古旧鎏金色,并带有淡淡的旧纸纹理。构图对称、优雅、宁静,灰鹭略偏中心左侧,鸢尾花平衡右侧画面。横向 16:9。无人物,无文字,无字母,无签名,无标志。
```

</details>

<details><summary><b>新黑色电影数字艺术三联画</b></summary>

```text
{
  "colors": {
    "color_temperature": "冷色调",
    "contrast_level": "高对比度",
    "dominant_palette": [
      "青绿色",
      "青色",
      "深蓝色",
      "黑色",
      "橙色"
    ]
  },
  "composition": {
    "camera_angle": "多角度",
    "depth_of_field": "浅景深",
    "focus": "一名独处男子",
    "framing": "图像为一幅三联画，即三个电影式画格组成的序列。顶部画格为该男子背影的全景镜头，中部画格为其面部特写，底部画格为中景镜头。整体营造出胶片条或分镜脚本效果。"
  },
  "description_short": "一幅电影感三联画，展现一名孤身男子在阴郁、氛围浓重的夜间都市中。画面依次描绘他行走在湿漉漉的街道上、一张沉思状的面部特写，以及他点燃一支香烟的场景。",
  "environment": {
    "location_type": "城市景观",
    "setting_details": "一座现代都市的夜间景象，高楼林立，霓虹招牌与交通信号灯闪烁。街道湿滑反光，暗示刚下过雨。场景分别设于人行横道、人行道，以及可能位于一处天桥下方。",
    "time_of_day": "夜晚",
    "weather": "雨天"
  },
  "lighting": {
    "intensity": "中等强度",
    "source_direction": "混合光源方向",
    "type": "电影感布光"
  },
  "mood": {
    "atmosphere": "孤独而沉思的城市新黑色氛围",
    "emotional_tone": "忧郁"
  },
  "narrative_elements": {
    "character_interactions": "该男子始终独处，暗示疏离与内省的主题。",
    "environmental_storytelling": "幽暗、多雨且空旷的城市街道强化了人物的孤独感，也烘托出新黑色电影特有的阴郁、神秘氛围。",
    "implied_action": "镜头序列——行走、驻足沉思、点燃香烟——暗示该人物正在思索某件重大之事，或正处于危机或抉择时刻。"
  },
  "objects": [
    "男子",
    "深色大衣",
    "信使包",
    "湿漉漉的街道",
    "人行横道",
    "城市建筑",
    "霓虹招牌",
    "交通信号灯",
    "打火机"
  ],
  "people": {
    "ages": [
      "成年"
    ],
    "clothing_style": "深色长大衣",
    "count": "1",
    "genders": [
      "男性"
    ]
  },
  "prompt": "以三联画形式呈现的电影感剧照，风格为新黑色（neo-noir）。一名三十多岁末期的独处男子于雨夜穿行于湿滑的城市街道。整座城市沐浴在环境光所散发的冷调青绿色与蓝色之中，同时又与霓虹招牌及交通信号灯所发出的暖调橙色与黄色形成对比；这些暖色光线映照在湿漉漉的人行道上。第一幅画格为从后方拍摄的全景镜头，第二幅为情绪饱满的面部特写，第三幅则展现他在天桥下点燃一支香烟。整体氛围阴郁、富有张力，采用浅景深与高对比度处理。",
  "style": {
    "art_style": "电影感",
    "influences": [
      "新黑色（neo-noir）",
      "赛博朋克（cyberpunk）",
      "银翼杀手（Blade Runner）"
    ],
    "medium": "数字艺术"
  },
  "technical_tags": [
    "三联画",
    "电影剧照",
    "新黑色（neo-noir）",
    "色彩分级",
    "青绿色与橙色",
    "电影感布光",
    "夜景摄影",
    "湿滑反光",
    "散景（bokeh）"
  ],
  "use_case": "用于训练 AI 掌握电影叙事、情绪生成及新黑色风格复现能力的数据集。",
  "uuid": "7c21100c-8de4-4687-8952-5de3ac5e42b3"
}
```

</details>

<details><summary><b>无声对峙</b></summary>

```text
俯视高角度镜头，展现一处光线昏暗的废弃庭院：地面为开裂的混凝土，散落着陈旧的标记与褪色的撞击凹痕；人物身影细长而诡异，投射至画面外；画面中不呈现任何暴力元素；配色以深青绿色为主，辅以一道强烈的金色光束；线条粗重；呈现 2D 动画卡通风格；采用平涂着色；对比度极高；氛围充满张力。
```

</details>

<details><summary><b>无畏契约特工立绘</b></summary>

```text
{ "TASK": "Design a unique 'Valorant' Agent Key Art. Riot Games Art Style.",
"VISUAL_ID": "Sharp 2.5D digital painting. Fusion of anime & western comic. Matte textures, clean lines, no noise.",
"PALETTE": "Primary: Dark Slate Blue (#0f1923). Branding: Hyper-Red (#ff4655). Ability: Neon highlight.",
"AGENT": "Athletic, confident. Future-tech streetwear (straps, windbreaker, tactical gloves). Sharp facial planes. Hair: Thick, sculpted chunks (no strands).","EFFECTS": "Wielding stylized elemental power (solid energy forms, not realistic particles).", "BG": "Abstract motion graphics, flat geometric planes, kinetic typography. Red/Dark contrast slicing the frame.",
"LIGHT": "Strong rim lighting, hard-edge cast shadows.", "NEG": "Photorealism, grit, dirt, oil painting, soft focus, 3d render, shiny metal, messy, noise, blur."
}//You can add Name and Skills or size like 16:9 here.
```

</details>

<details><summary><b>日出蛛网露珠微距</b> · 机器翻译</summary>

```text
一张极致特写的微距照片，拍的是挂满晨露的圆网蛛蛛网，张在两根弯曲的干草茎之间，采用 16:9 宽幅横向构图。蛛网的螺旋丝线斜穿画面，串着数百颗大小不一、浑圆的露珠，从细小的珠粒到大而透明的水球都有；在前景最清晰的那些露珠里，每颗水球都映出身后草地的一幅倒置微缩影像：金色的日出天空、一排远处的树木和几朵红色罂粟花。对焦平面薄得如同刀锋，落在左侧三分之一处的一排露珠上，它们闪着针尖般的高光，边缘有细微的彩虹折射，而蛛网的其余部分都融化成柔和的虚化。背景是平滑如奶油的散景，由低角度的太阳穿过草地上的薄雾投来的暖金、桃色和柔绿色构成，右上方有大而圆的失焦高光。一只小小的花园蜘蛛位于蛛网边缘远处，失焦且极小，几乎只是一个深色的小点。前景中几穗草籽同样虚化，框住画面底部边缘。逆光的低角度金色时刻阳光，轻柔的薄雾，高动态范围，自然色彩，清晰的水珠质感，自然杂志风格的微距摄影，使用 100mm 微距镜头，光圈 f/2.8，氛围宁静而细腻。不要出现人物，不要文字，不要水印。
```

</details>

<details><summary><b>日式枯山水僧人变身</b></summary>

```text
{
  "prompt": "你将使用所提供照片中的人物作为主要主体进行图像编辑。面部必须保持清晰且不被修改。将主体转变为一位沉思的**禅宗僧人/园丁**，在黎明时分的纯净日本枯山水庭院中精心耙出图案。强调极简美学、柔和的自然光线、宁静的色彩，以及深刻的平和感与正念感。",
  "details": {
    "year": " timeless（传统日本美学）",
    "genre": "禅宗 / 沉思 / 极简 / 文化",
    "location": "一个维护完美的日本枯山水庭院（Karesansui）。地面是细腻的白色砂砾，围绕精心摆放的风化岩石耙成精确的同心图案。背景中可见一座覆盖青苔的石灯笼，或一棵经过艺术修剪的盆景树。空间由一道素雅的竹篱笆围合。",
    "lighting": "清晨或阴天时柔和漫射的光线。光线均匀而轻柔，在不产生强烈对比的情况下微妙地勾勒出耙制的纹理。整个场景弥漫着一种清冷而宁静的质感。",
    "camera_angle": "中景到全身镜头，位置略低，以捕捉主体与地面的互动以及耙制花园的广阔感。构图简洁平衡，遵循极简主义原则。（1:1 构图）。",
    "emotion": "宁静、专注、正念、平和。表现出深层的内心安宁。",
    "costume": "简单传统的日本服饰：朴素宽松的和服或长袍，颜色为柔和的自然色调（例如炭灰色、深靛蓝、泥土米色）。发型整洁或剃发（若符合僧人身份）。整体审美干净素雅。",
    "color_palette": "以宁静柔和的自然色为主：砂砾的纯白色、岩石与木材的灰色和大地棕色、苔藓与植被的深绿色。点缀色使用极为克制。整体色调和谐而令人平静。",
    "atmosphere": "极度宁静、冥想、寂静且和谐。空气清新而静止，引人内省。充满秩序感与安宁感。",
    "subject_expression": "目光低垂或轻柔地专注于耙地动作，现实主义的面部表情平静安详。双唇轻闭，传达出深度专注与内心平和。",
    "subject_action": "双手持一把木耙，细致地在白色砂砾上绘制完美流畅的图案。姿态微躬，优雅而刻意，强调任务的仪式性。动作缓慢而有目的。",
    "environmental_elements": "白色砂砾上清晰流畅的耙纹图案。风化岩石的质感。苔藓或耙子上可能可见细微的露珠。远处的竹篱笆为这片宁静空间提供了微妙的自然边界。"
  }
}
```

</details>

<details><summary><b>日落时分的酒庄品鉴亭露台</b> · 机器翻译</summary>

```text
日落时分一座单层石灰岩品酒亭的长条有顶露台,从下坡的葡萄藤行向坡上望去。露台沿建筑的长边延伸,有五根深色上油橡木立柱、摆着空酒杯的木桌,以及在深远出檐下发出温暖光芒的串灯。同一座建筑:淡蜜色石灰岩墙体,低坡度的双坡陶土瓦屋顶,沿露台排列的高大青铜框玻璃门,一座矮矮的方形石灰岩烟囱从左侧山墙端升起,该左侧山墙墙面上有一扇深绿色双开门,而那棵树干扭曲的古老橄榄树就立在门旁的左侧墙角。挂满葡萄的藤行引导视线向上通往品酒亭,露台下方是低矮的干砌石墙和薰衣草花境。天空呈杏色与玫瑰色,太阳在观者身后落下,使墙面泛着温暖的琥珀色光芒,葡萄藤之间有柔和的阴影。写实建筑摄影,横向 16:9。无人物,无文字,无标牌,无汽车。
```

</details>

<details><summary><b>日落阿尔卑斯车站像素画</b> · 机器翻译</summary>

```text
一幅宽幅的 16 位时代像素艺术场景,描绘金色时刻日落时分山谷中的一座小型高山火车站,风格如同精美细致的复古冒险游戏背景,像素边缘锐利清晰,无抗锯齿、无模糊,使用有限的 48 色调色板,天空部分采用细致的抖动处理。前景中,有一座小小的木质车站建筑,屋顶是陡峭的红色瓦顶,配有圆形站钟、开着粉色和黄色像素花朵的花箱、一条长椅、两个牛奶桶,以及一盏刚刚开始亮起的悬挂灯笼。一列乳白色与森林绿相间的短途蒸汽火车,挂着三节车厢,停靠在站台边,烟囱里升起一缕柔软的白色像素蒸汽,车窗透出温暖的黄色灯光。铁轨向右弯曲延伸,经过一座石拱高架桥,跨过一条带有细小白色急流的青绿色河流,然后消失在山腰的隧道中。中景中,有一簇带烟囱的木屋、一座带洋葱形圆顶尖塔的小教堂、三种深浅绿色的松林,以及一道从悬崖上倾泻而下的瀑布。背景中,层叠的积雪山峰在薰衣草紫、桃色和玫瑰色调中捕捉着最后的余晖,渐变的日落天空从地平线处的深橙色过渡到顶部的紫罗兰色,点缀着几朵细长的像素云,以及最早出现的两颗星星。生活细节:站台上的一只猫、以两个像素构成剪影的鸟儿、烟囱冒出的炊烟。清晰的视差式分层,温馨而怀旧的氛围,轮廓清晰易辨,整幅画面的像素比例保持一致。16:9 横向构图。无人物,无文字,无用户界面,无标志,无水印。
```

</details>

<details><summary><b>时尚人像摄影提示词</b></summary>

```text
{
  "image_generation_prompt": {
    "subject": {
      "demographics": "年轻女性",
      "hair": {
        "color": "草莓金发／金色金发",
        "style": "长发、蓬松、分层、略带凌乱的波浪卷",
        "parting": "中分"
      },
      "face": {
        "makeup": "黑色猫眼眼线、睫毛膏、轮廓清晰的眉毛、鼻梁与脸颊高光、亮面粉色唇妆",
        "expression": "中性表情，略带噘嘴，目光聚焦于镜中倒影"
      },
      "physique": "苗条、健美、古铜色肤色"
    },
    "apparel": {
      "outerwear": {
        "item": "人造毛皮夹克",
        "color": "深红／红色混合色调",
        "texture": "蓬松、厚实、丰盈"
      },
      "top": {
        "item": "紧身胸衣上衣",
        "style": "无肩带、束腰式、短款",
        "material": "深红色缎面或略带光泽的面料",
        "fit": "贴身、结构感强的上身剪裁"
      },
      "bottoms": {
        "item": "牛仔裤",
        "color": "浅蓝色水洗效果",
        "fit": "低腰、紧身剪裁",
        "details": "可见缝线、前侧口袋"
      }
    },
    "accessories": {
      "jewelry": [
        "细金链项链，配小巧吊坠",
        "右手无名指佩戴一枚金戒指"
      ],
      "belt": {
        "material": "黑色皮革",
        "buckle": "矩形金色／金属质感表框"
      },
      "tech": {
        "item": "智能手机（iPhone 风格）",
        "case_color": "黑色",
        "holding_style": "右手垂直持握于面部前方"
      },
      "beauty_details": {
        "nails": "短甲，涂亮红色指甲油"
      }
    },
    "pose_and_framing": {
      "type": "镜中自拍",
      "posture": "站立姿势，轻微髋部倾斜（对立式平衡姿态），露出腰部",
      "framing": "大腿以上取景，竖构图"
    },
    "setting_and_lighting": {
      "location": "室内（可能是卧室或走廊）",
      "background_elements": {
        "left": "深色百叶窗窗户，隐约可见床铺／家具及白色杂物",
        "right": "白色门框／门柱，素色墙面"
      },
      "lighting": {
        "quality": "温暖、有方向性的人造光源",
        "source": "来自右侧",
        "shadows": "在躯干左侧及背景投下阴影"
      }
    }
  }
}
```

</details>

<details><summary><b>时尚编辑拼贴情绪板</b> · 机器翻译</summary>

```text
浅米色背景上的竖版时尚杂志拼贴布局。画面主体是一张全彩中景照片:一位美丽的女性,深色长波浪发,橄榄色肌肤,身穿宽松的白色纽扣衬衫(法式半塞入)和高腰黑色长裤,戴着黑色小方框太阳镜。她自信地站立,一只手插在口袋里,神情带着淡淡的微笑,背景是深灰色的摄影棚。在她身后的左侧,垂直堆叠着 4 个圆角矩形画框,均为高对比度黑白画面。这些黑白画框展示同一位女性的亲密特写肖像,姿态各异:梦幻般地仰望、手触头发看向镜头、严肃的侧脸凝视,以及单手托腮带着柔和的微笑。灯光为专业摄影棚品质,黑白肖像采用柔和漫射光,主彩色图像的对比度略高。高端时尚杂志美学,情绪板风格,照片级真实感,8k 分辨率,85mm 镜头拍摄。
```

</details>

<details><summary><b>时间分层摄影</b></summary>

```text
一张位于${location:Galata Tower, Istanbul}的单幅照片，画面被划分为有机、流动的若干区域，每个区域展现一个不同时代：${era1:1890s sepia Ottoman period}、${era2:1960s faded color}、${era3:present day digital clarity}。各时代之间的过渡无缝衔接，通过建筑细节、人物服饰与交通工具自然融合。采用相同机位、相同视角，不同时代彼此渗透、交融。街景视角。每一代均以符合其时代真实摄影风格的写实主义手法呈现。
```

</details>

<details><summary><b>时髦极简镜前自拍</b> · 机器翻译</summary>

```text
一张逼真的高质量 8K 镜面自拍,由 iPhone 16 Pro Max 拍摄,3:4 画幅。

风格:清晰的高级感镜面自拍,干净、现代的美学。

相机角度:特写肖像,智能手机在镜子前与脸部齐平。

主体:一位年轻女性。不要改变她的面部特征或身份。

面部与妆容:光泽水润的肌肤,清晰的黑色上扬眼线(猫眼妆),浓密卷翘的长睫毛,以及涂着透明粉色唇彩的饱满双唇。

发型: 直发自然披散,中分干净利落。

姿势:她略微移开视线,望向镜中的自己,神情平静自信。她的右手拿着一部深灰色 iPhone。指甲涂成柔和的浅粉色。

服装与配饰:一件黑色挂脖式上衣,带有细细的交叉带。叠戴的精致金色(或玫瑰金)项链,配有三个小圆形吊坠,中号金色圈形耳环,以及耳廓软骨上的一枚小巧银色耳骨夹。

光线:柔和的自然日光从侧面照入,在她的皮肤和头发上形成柔和的高光。

背景:干净现代的室内空间,白色墙壁,优雅的装饰线条,背景中有木制门框。

氛围:毫不费力的时尚感、自信、放松、极简。照片级写实,真实的皮肤质感。
```

</details>

<details><summary><b>明暗对照艺术人像拼贴</b> · 机器翻译</summary>

```text
一幅由 5 张不同的黑白艺术肖像组成的女性竖版拼贴,采用 35mm 胶片拍摄,带有明显的颗粒感和高对比度。
左上:亲密特写,她单手托腮,轻轻微笑,凌乱的发丝落在脸上,佩戴垂坠耳环,柔和的窗光。右上:自然流露的欢乐,仰头大笑,一只手拨弄着凌乱的头发,身穿白色 T 恤,戏剧性的高对比度光线。左中:极致特写的侧脸,焦点锐利地落在眼睛和鼻子上,可见雀斑和皮肤质感,半边脸隐没在深深的阴影中(分割光)。左下:身穿粗针织毛衣,双手托着头,目光强烈地直视镜头,眉毛突出,柔和而忧郁的光线。右下:艺术化构图,一张侧脸剪影靠近另一张看向镜头的脸,身穿黑色高领毛衣,低调光线,黑色深邃。
风格:时尚杂志摄影,真实情感,未经修饰的皮肤质感,明暗对照法,忧郁氛围,杰作,照片级真实感。
```

</details>

<details><summary><b>星期三风哥特墓园自拍</b> · 机器翻译</summary>

```text
这是一张略微仰拍的近景自拍照。主体是一位外形极具“星期三·亚当斯”风格的女性。她直视镜头,表情严肃、毫无情绪。

姿势:
女子一只手臂伸出握着相机自拍,身穿黑色袖子(只能看到前臂和部分手臂)。另一只手拿着一大束深红色玫瑰,用简单的纸包裹,配有少量绿叶。一根手指上可见一枚银戒指。一只被砍下的人手(“万能手”)搭在她的肩上,为造型增添诡异感。

服装:
她穿一件深 V 领黑色连衣裙,里面露出带尖角的白色立领。领口点缀着一条低调的银项链。连衣裙为长袖。

发型与妆容:
她的头发从中间分缝,梳成两条垂在胸前的经典长辫。她化着哥特风妆容:深色烟熏眼妆、精准描画的眉毛,以及深酒红近乎黑色的口红。她戴着一副黑色大号猫眼太阳镜,遮住双眼,同时突出脸型轮廓。

光线与氛围:
自然日光,柔和但足够明亮,能捕捉到细节。光线营造出阴郁而时髦的氛围。鲜红的玫瑰与黑白相间的服装,在墓园背景的衬托下形成强烈的视觉对比。

背景:
场景设在一座古老的墓园。女子身后是大型石砌墓室、陵墓和各式墓碑,其中一些装饰有雕像,例如左侧背景中的天使雕像。墓碑之间生长着高大的常绿树,如侧柏或柏树。右侧背景中有一辆复古的黑色豪华轿车或类似豪华灵车的汽车,旁边站着一名身穿黑色燕尾服、系着领结的男子,形似管家“大个子”。

氛围:
整体氛围是暗黑优雅、哥特、神秘,带有一丝黑色幽默和现代“恐怖时尚”美学。

技术细节:
一张现代数码照片,清晰度极高,细节逼真。相机非常贴近女子的脸部,营造出真实的自拍效果,画面边缘带有轻微的透视畸变。背景柔和虚化,呈现自然的焦外光斑,同时墓园和汽车依然可以辨认。

重要:不要改变参考图中的面部特征或身份。保持确切的面孔、面部结构、眼睛、鼻子、嘴唇及其他显著特征。

画幅:3:4
画质:超写实、高品质、锐利的 8K 照片,自然的皮肤质感,没有人工或塑料般的 AI 感,使用 iPhone 16 Pro 拍摄。
```

</details>

<details><summary><b>星际穿越风格电影海报</b></summary>

```text
受《Interstellar》启发的宏伟电影海报，广阔的宇宙全景：一名孤独的宇航员站在浅浅的镜面状外星海洋上，面向天空中巨大的黑洞，黑洞扭曲着横跨天际的星光；地平线上是遥远的冰冻山脉与超现实的行星环；一艘微小的航天器悬浮在大气层之上；背景中充满旋转的尘埃、薄雾、漂浮的冰粒与发光的星云，强烈的体积光效，冷峻的蓝黑色太空与温暖的金色头盔反射形成对比，戏剧性的背光，高对比度，充满敬畏与忧郁的氛围，融合超精细雕刻风格与高度细致的数字绘画及精炼线稿的插画，复杂的宇航服纹理，水面反光涟漪，天体扭曲效应，深邃阴影，微妙的胶片颗粒感，史诗级尺度，略带超现实主义的真实感，广角镜头，低角度视角，锐利清晰的焦点，高端电影海报构图，杰作级品质，丰富的空间层次感，黑暗虚空与璀璨星光的对峙
```

</details>

<details><summary><b>晨光广场上的夯土图书馆</b> · 机器翻译</summary>

```text
一座单层夯土村庄图书馆,右端有一座圆形夯土阅读塔,晴朗的清晨面朝阳光明媚的石铺广场。长长的墙面呈现出赭石色、沙色和锈红色土层分明的水平层次,坐落在低矮的灰色石基座上。带有纤薄深色钢制边缘的平屋顶向前出挑,形成深邃的遮阴入口门廊,由六根纤细的浅色木柱支撑。门廊后方,宽阔的天蓝色木制双开门两侧各有三扇高而窄的深青铜色窗框窗户。圆柱形塔楼略高于主屋顶,靠近顶部有一圈小方窗。一棵树干扭曲的宽大古杜松立在入口左侧,一条浅石水渠横穿门廊前的广场。种着薰衣草和干草的陶土花盆、两张木长椅,以及一排自行车架。柔和的金色侧光,清晰的阴影,干燥的丘陵上方是淡蓝色的天空。写实建筑摄影,横向 16:9。无人物,无文字,无标牌,无汽车。
```

</details>

<details><summary><b>晨间咖啡爆炸图</b></summary>

```text
创建一幅超现实的爆炸式垂直信息图构图，主题为早晨咖啡。在顶部，是一团悬浮在空中的闪亮咖啡油脂飞溅瞬间，凝固于半空，带有微小气泡和水滴。其下方是一层浓郁深色的浓缩咖啡液体，接着是散落的烘焙咖啡豆，清晰展现纹理与油光。再下一层是轻轻漂浮的细砂糖晶体，底部则是一个极简风格的陶瓷咖啡杯底座。纯白色背景，柔和的影棚灯光，每个漂浮元素下方带有微妙阴影，超锐利对焦，采用 DSLR 微距摄影风格，配有简洁的信息图文字标签及细指引线，呈现高端生活方式美学，8K 质量。
```

</details>

<details><summary><b>晨雾山湖雪松水上茶室</b> · 机器翻译</summary>

```text
一张写实的建筑摄影照片，拍摄初秋薄雾中静止山湖上的一座小型漂浮雪松茶屋，16:9 横幅，视角是从木质岸边小径走向码头。首先是主要主体：一座方形单间的雪松茶屋，屋顶是深色、经风化的四坡屋面木瓦顶，朝向湖面的一侧有四扇可滑动的障子纸门，一条窄窄的缘侧（engawa）露台配简洁的竖向栏杆，两盏矮墩的花岗岩石灯笼分立在码头入口两侧，漂浮平台的右侧系着一条小木划艇。平台坐落在深色木浮筒上，略高于水面；浅色雪松墙面显出柔和的木纹；两个转角处悬挂着铜质雨链。茶屋背后，层叠的蓝灰色山峦隐入雾中；松林沿着远岸排列；水面将屋顶倒映成一片柔和的模糊。光线：来自左侧的低角度晨阳，清冷的薄雾，温暖的木质高光，安静沉思的氛围，清晰的建筑细节，真实色彩。没有人物，没有烟柱，没有霓虹，没有可读文字，没有水印。
```

</details>

<details><summary><b>晨雾山谷中的高地牛写实摄影</b> · 机器翻译</summary>

```text
一张写实的野生动物摄影作品，画面中一头毛发蓬乱的姜黄色高地牛站在日出时分薄雾笼罩的苏格兰峡谷中的金色高草丛里，采用宽幅横向 16:9 画面。牛站在画面左半部分，面朝镜头，锈橙色和铜色的长毛浓密而卷曲，毛发上挂着细小的露珠。厚重的刘海垂在眼睛上方，宽阔的粉棕色鼻子和口鼻部清晰而细节丰富，一对细长、淡色、向上外翘的长角从头部向外并向上弯曲。一团温热的呼吸和雾气在寒冷的清晨空气中飘散在它的头部右侧。前景中，高大干枯的金色草丛和挂着露珠的草穗柔和地虚化。来自右上方低垂太阳的柔和金色逆光使牛毛边缘发光，并让整个峡谷充满温暖的薄雾。背景中，虚化的起伏山丘呈柔和的棕色、淡紫和紫色调，隐没在雾中，右侧中景可见成片粉色的石楠花和一片淡银色的湖泊。浅景深，200mm 长焦压缩感，自然色彩，宁静安详的氛围。无人物，无围栏，无文字，无水印。
```

</details>

<details><summary><b>普拉提工作室柔光照</b></summary>

```text
{
  "category": "PILATES_STUDIO_SOFT_DAYLIGHT",
  "identity_lock": {
    "enabled": true,
    "priority": "ABSOLUTE_MAX",
    "instruction": "保留精确的参考身份与面部比例。仅限21岁及以上成年人。"
  },
  "subject": {
    "demographics": "成年女性，21–29岁，匹配参考身份。",
    "hair": {
      "color": "匹配参考。",
      "style": "高马尾或整齐发髻（写实风格，非完美无瑕）",
      "texture": "可见发丝细节，少量碎发",
      "movement": "极轻微"
    },
    "face": {
      "eyes": "完全匹配参考眼睛；神态沉静专注",
      "skin_details": "自然肤质纹理；细微运动后光泽（非油光）",
      "micro_details": "保留原有印记"
    },
    "clothing": {
      "outfit": "极简运动装套装（无品牌标识/文字）",
      "fabric": "可见运动针织面料纹理；接缝处呈现真实张力"
    },
    "accessories": {
      "jewelry": [
        "可选佩戴小巧银色耳环（为增强训练真实感可移除）"
      ]
    }
  },
  "pose": {
    "type": "课后抓拍姿态",
    "orientation": "坐于垫子上，半身构图",
    "hands": "一手持无品牌水瓶，另一手自然置于膝上",
    "gaze": "接近直视镜头",
    "expression": "柔和而自豪的微笑"
  },
  "setting": {
    "environment": "普拉提工作室",
    "background_elements": [
      "中性色调工作室墙面",
      "镜面虚化且无反射异常",
      "瑜伽垫与辅助器械（无品牌标识）"
    ],
    "depth": "主体清晰锐利；背景柔焦"
  },
  "camera": {
    "shot_type": "半身人像",
    "angle": "平视或略高于平视角度",
    "focal_length_equivalent": "26mm 手机镜头 或 50mm 专业镜头",
    "framing": "4:5",
    "focus": "双眼清晰锐利；背景散景"
  },
  "lighting": {
    "source": "柔和窗边日光",
    "direction": "轻柔侧前方光源",
    "highlights": "颧骨处呈现自然高光",
    "shadows": "阴影柔和、富有美感"
  },
  "mood_and_expression": {
    "tone": "干净、运动感、沉静自信",
    "atmosphere": "极简、通透"
  },
  "style_and_realism": {
    "style": "写实主义健身生活方式摄影",
    "imperfections": "轻微噪点，细微汗光"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "resolution": "高分辨率",
    "noise": "低至中等",
    "mode_variants": {
      "amateur": "手机抓拍构图，轻微噪点，略微倾斜",
      "pro": "杂志级健身视觉风格，微对比度锐利，曝光干净"
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
    "身份偏移",
    "面部形变",
    "镜面异常",
    "重复反射",
    "多余手指",
    "解剖结构错误",
    "可读文字",
    "品牌标识",
    "水印",
    "塑料质感皮肤",
    "过度平滑"
  ]
}
```

</details>

<details><summary><b>普罗旺斯日出薰衣草田尽头的石屋</b> · 机器翻译</summary>

```text
日出时分的普罗旺斯，一行行笔直延伸的紫色薰衣草通向一座古老的两层石头农舍，从中央土路尽头的低视角望去，采用宽幅横向 16:9 画面。圆润的薰衣草垄布满整个画面下半部，并向中景汇聚，垄间是狭窄的棕色土路，其中一条笔直地穿过画面中央。农舍位于画面右侧三分之一处：粗糙的米色石墙、棕红色陶瓦屋顶，以及带淡蓝色百叶窗的小窗，屋前有绿色灌木。一棵高大的深绿色柏树单独耸立在房屋右侧紧挨着房子的位置。左侧中景，一棵孤零零的圆形绿色橡树立在平缓的草坡上。低垂的太阳刚刚升到最左侧山丘之上，闪耀金光，带有柔和的镜头光晕和淡淡的晨雾，温暖的光线洒在薰衣草的顶端。起伏的蓝色山丘绵延在地平线上，几朵白色小云飘浮在淡蓝色的天空中，天空在太阳附近渐变为桃粉色。写实风景摄影，广角，自然色彩，宁静的氛围。无人物，无文字，无标志。
```

</details>

<details><summary><b>普罗旺斯薰衣草农舍图生视频</b> · 机器翻译</summary>

```text
以第 2 步的图像"普罗旺斯日出时分薰衣草行尽头的石砌农舍"作为精确的首帧,将其制作成一段平静的、时长 ${duration:6} 秒的电影感镜头。保持带有赤陶屋顶和浅蓝色百叶窗的石砌农舍位于右三分之一处,其旁的高大柏树、左侧的孤立橡树、汇聚的薰衣草行和中央小路、最左侧的低垂太阳、地平线以及构图,都与图像中完全一致。一阵轻柔的微风让薰衣草行轻轻摇曳,方向全部一致。镜头沿中央薰衣草行朝农舍方向做一次非常缓慢、平稳的推进。太阳的金色光芒缓缓变亮,薄薄的晨雾飘过左侧的山丘。几只小鸟从右向左飞过房屋上方的天空,几只蜜蜂在前景的薰衣草上空飘移,小朵白云轻轻飘动。动作自然逼真,不剪切,不出现人物,不出现新的建筑或物体,不出现文字。配有轻柔的微风声、远处的鸟鸣声和蜜蜂的嗡嗡声。
```

</details>

<details><summary><b>普罗旺斯薰衣草农舍场景策划助手</b> · 机器翻译</summary>

```text
扮演一位电影感风景设计师,撰写可直接用于生成图像和动态画面的场景简报。帮我设计一张主视觉镜头:普罗旺斯日出时分,一座古老的石砌农舍位于一排排紫色薰衣草的尽头。这个镜头会先生成静态图像,再以该图像作为首帧制作成一段短视频。你的简报必须让静态图像中包含丰富的、能够自然运动的元素(薰衣草行在微风中轻轻摇曳、晨雾在山丘上飘移、低垂太阳的光芒缓缓变亮、小朵云彩飘动、蜜蜂在花丛上空飞舞、一两只鸟划过天空),同时保持构图平静、清晰易读、便于制作动画。

我的初始选择:
- 农舍:${farmhouse:a two-story old stone farmhouse with a terracotta tile roof and pale blue shutters}
- 树木:${trees:one tall dark cypress right beside the house and a lone round oak tree on a grassy rise}
- 薰衣草田:${field:long straight rows of purple lavender with dirt paths between them, converging toward the house}
- 地貌:${landscape:gentle rolling hills fading to blue in the distance}
- 时间与光线:${time:sunrise with the sun just above the hills, warm golden light, long shadows, light haze}
- 视觉风格:${style:photoreal landscape photography, natural colors}
- 情绪关键词:${mood:peaceful, warm, fragrant, timeless}

请先用一条简短的消息向我询问缺失的信息:我偏好的机位(位于薰衣草行尽头的低机位、站在小路上的人眼高度,还是略高的俯视),农舍和橡树应位于画面的哪一侧,太阳应在哪里,我想要多浓的雾气,以及需要避免的内容(人物、汽车、拖拉机、围栏、标牌、必须飞得逼真的鸟、文字、标志,或复制某张真实照片)。

然后按以下部分生成简报:

1. **场景概述**:两到三句话,描述这个地方、时间、光线以及这一刻的感觉。描绘的是一个具有普罗旺斯地区神韵的想象场景,而不是某张特定照片或某个具名农场的复制。

2. **农舍与树木**:农舍在画面中的位置和大小,它的石墙、屋顶、百叶窗、窗户以及周围的灌木,柏树和橡树的位置,以及低垂的太阳如何照亮它们。

3. **薰衣草行与前景**:可见的行数、中央小路、各行如何向灭点汇聚、花朵在阳光下和阴影中的颜色,以及最近处花茎的质感。

4. **地貌与景深**:从前景薰衣草到农舍的景深层次、坡地上的橡树、中景的绿植、地平线上的山丘,以及雾气如何柔化每一层。

5. **光线与天空**:太阳的位置和高度、它周围的光晕和镜头暖意、天空渐变、云的形状和位置、沿薰衣草行延伸的阴影的长度和方向。

6. **固定视觉细节**:一份编号列表,列出 8 至 10 个必须在静态图像和视频中保持一致的细节(农舍位置、屋顶和百叶窗颜色、柏树位置、橡树位置、薰衣草行方向和中央小路、太阳位置、地平线、云的布局、机位、构图)。

7. **运动图**:一张表格,列出视频中所有可以运动的元素,列为:元素、运动类型、方向、速度(很慢、慢、中等)以及运动幅度。包括薰衣草、雾气、太阳光晕、云、树木、蜜蜂或鸟,以及镜头运动。整体运动保持细微且符合物理规律,只有一个风向。

8. **提示词种子 A - 主视觉静态图**:一条可直接粘贴使用的图像提示词,少于 170 词,用于宽幅 16:9 风景画面,第一句话包含薰衣草行、石砌农舍和日出,结尾为:no people, no text, no logos。

9. **提示词种子 B - 图生视频动画**:一条可直接粘贴使用的视频提示词,少于 120 词,以主视觉静态图作为首帧,描述薰衣草摇曳、雾气飘移、光芒变亮、小朵云彩飘动、沿中央薰衣草行约 6 秒的一次非常缓慢的推进镜头,并说明要让农舍、树木、薰衣草行和构图与图像中完全一致,不出现新物体。

规则:不出现人物、车辆或农机;不出现文字、标牌或标志;不使用快速镜头运动或剪切;不出现违背物理规律的运动(所有植物在风中朝同一方向弯曲,房屋和树木绝不移动或改变形状,太阳不会跳动,阴影始终与太阳保持一致)。使用短段落和列表。
```

</details>

<details><summary><b>暖色影棚人像</b> · 机器翻译</summary>

```text
BASE – 暖调影棚
一位四十五岁上下的黑人男性的电影感影棚肖像,浓密且修剪整齐的络腮胡,黑框深色烟熏墨镜,细金链,短而自然的黑发,黑色宽松 T 恤,神情平静沉稳,不带笑容。中性暖米色背景,左侧柔和的定向主光,细微的轮廓光。85mm 镜头,f/2,中近景,平视。黑色、奶油色与赭色配色,点缀一抹金色。杂志编辑风格,内省,胶片颗粒。

A – 明暗对照
一位四十五岁上下的黑人男性的戏剧性明暗对照影棚肖像,浓密络腮胡,深色烟熏墨镜,细金链,黑色 T 恤,平静而强烈的气场。纯黑背景,左上方单一硬质主光,深邃阴影,金链捕捉光线。85mm,紧凑特写,伦勃朗光,高对比度,胶片颗粒。

B – 镜子
一位四十五岁上下的黑人男性的内省式影棚肖像,浓密胡须,深色烟熏墨镜,细金链,坐在一面大镜子旁,倒影略微失焦。暖奶油色背景,柔和的窗光。50mm,中景,米色、黑色与赭色配色,杂志编辑风格,细微颗粒。

C – 黑白
一位四十五岁上下的黑人男性的黑白杂志编辑风格肖像,浓密胡须,深色墨镜,细链,黑色棒球帽,双臂交叉,姿态沉稳,不带笑容。浅灰色无缝背景,柔光箱照明。70mm,四分之三角度,杂志封面美学。

NEGATIVE: 文字, 水印, logo, 模糊, 变形的手, 多余的手指, 扭曲的脸, 塑料质感皮肤, 卡通感, 头部被裁切
```

</details>

<details><summary><b>暖色调纸偶创意场景</b></summary>

```text
{
  "colors": {
    "color_temperature": "暖色",
    "contrast_level": "高对比度",
    "dominant_palette": [
      "棕色",
      "米色",
      "黑色",
      "白色",
      "橄榄绿"
    ]
  },
  "composition": {
    "camera_angle": "平视角度",
    "depth_of_field": "浅景深",
    "focus": "纸偶与折纸小浣熊",
    "framing": "男子的面部与背景中的一盏台灯共同框定桌面上的中心场景——纸艺人物。"
  },
  "description_short": "一名男子正专注凝视着木质书桌上两个微小人物：一只折纸小浣熊，以及一个手持雨伞的纸偶男孩，二者均由旧报纸制成。一盏暖色调台灯照亮整个场景。",
  "environment": {
    "location_type": "室内",
    "setting_details": "一张深色木质书桌或桌子，很可能位于书房或工作坊内。背景光线昏暗，将观者注意力聚焦于桌面场景。",
    "time_of_day": "傍晚",
    "weather": "人工照明"
  },
  "lighting": {
    "intensity": "中等强度",
    "source_direction": "上方",
    "type": "人工照明"
  },
  "mood": {
    "atmosphere": "静谧的创造力与奇想式叙事",
    "emotional_tone": "平静"
  },
  "narrative_elements": {
    "character_interactions": "一位创作者正细致地布置自己的作品，仿佛正赋予一个微缩手工世界以生命。",
    "environmental_storytelling": "人物采用旧报纸制作，暗示来自外部世界的故事正被重塑为一种全新的、个人化的叙事；聚拢的灯光则为此故事营造出私密的舞台感。",
    "implied_action": "该男子正处于布景过程中，或许即将用纸偶与小浣熊演绎一段故事。"
  },
  "objects": [
    "纸偶",
    "纸制雨伞",
    "折纸小浣熊",
    "手",
    "木质桌子",
    "台灯"
  ],
  "people": {
    "ages": [
      "成人"
    ],
    "clothing_style": "休闲T恤",
    "count": "1",
    "genders": [
      "男性"
    ]
  },
  "prompt": "一幅电影感十足、暖色调的摄影作品：一名男子坐在他的木质书桌前，其面部在背景中柔和虚化，神情专注地凝视着自己创作的两个微小人物。前景中，一只折纸小浣熊与一位手持雨伞、魅力十足的纸偶男孩并立于桌面，二者均以旧报纸精心制作而成。男子的手轻托纸偶，正在布置场景。光影富于戏剧性，仅由一盏台灯提供光源，投下修长阴影，并凸显纸张细腻的纹理。整体氛围静谧、富于创造力且充满奇想，采用浅景深拍摄。",
  "style": {
    "art_style": "写实风格",
    "influences": [
      "电影感",
      "静物摄影"
    ],
    "medium": "摄影"
  },
  "technical_tags": [
    "纸艺",
    "折纸",
    "浅景深",
    "散景",
    "暖色调照明",
    "电影感照明",
    "手工制作",
    "手工艺",
    "叙事",
    "选择性对焦"
  ],
  "use_case": "适用于创意、爱好、手工艺或叙事等主题的图库图像。",
  "uuid": "7a01281d-b2e9-45b7-82ed-6d77862113ad"
}
```

</details>

<details><summary><b>暗调时尚编辑拼贴</b> · 机器翻译</summary>

```text
一幅由同一位美丽女性的 5 张肖像组成的竖版艺术拼贴,她有深色长波浪发、迷人的浅色眼睛和散发光泽的棕褐色肌肤。版面采用几何斜向白色边框分隔各张图像。整体美学为"忧郁暗调时尚摄影",带有戏剧性的明暗对照光线(低调)、深邃的阴影和黑色背景。
画框 1(左上):她穿着米色挂脖上衣,手触下巴,目光强烈。
画框 2(右上):她穿着黑色上衣,手靠近嘴唇,眼神魅惑。
画框 3(中央):她穿着黑色挂脖上衣,手托下巴,表情严肃。
画框 4(左下):她穿着米色上衣,头靠在手上,神情梦幻。
画框 5(右下):她穿着深色上衣,双臂交叉,姿态优雅。
光线硬朗且有方向性,在她脸上形成强烈的明暗对比。85mm 镜头拍摄,照片级真实感,8k 分辨率,高级时尚杂志风格,可见白色手写体签名"Jennifer"。
```

</details>

<details><summary><b>暗黑浪漫女巫镜前自拍</b> · 机器翻译</summary>

```text
镜头角度与构图:
平视镜面自拍。中景,取景范围从头顶到大腿中部。竖幅 3:4 画面比例。她的视线聚焦在镜中的自己身上。

姿势:
放松而自信的站姿。左手在胸前高度握着智能手机,略微偏向一侧。右臂优雅地抬起,手指轻触女巫帽的帽檐。

服装:
暗黑浪漫风格的哥特女巫装。一件合身的黑色天鹅绒连衣裙,配深心形领口。裙子的高开衩露出她的右大腿。一件透明的黑色薄纱或雪纺披风沿着手臂垂下,像宽松飘逸的袖子。她穿着透明黑色连裤袜,上面有蜘蛛网图案,大腿处有一只大型黑色蜘蛛图案。

配饰:
一顶高高的经典女巫帽,材质为有纹理的黑色面料,帽子正面有一个长方形银色搭扣。脖子前方系着一条细黑色天鹅绒丝带颈链,打成蝴蝶结。一条由黑色珠子串成的长款多层项链,形似念珠,挂着一个大号复古风格金属十字架吊坠。智能手机套着深色厚实的保护壳。

发型、妆容与外貌:
微卷,披散。头发自然垂落在肩上。哥特魅惑风妆容,肌肤无瑕,眼妆浓烈戏剧化。双唇紧闭,涂着浓郁的深酒红色哑光口红。长方形指甲,涂深色指甲油。

光线、氛围与情绪:
昏暗神秘的室内光线,低调布光。柔和的光轻轻照亮她的脸和领口,背景隐没在阴影中。氛围神秘、优雅、暗黑,融合了万圣节美学与暗黑学院风。整体情绪神秘而沉静,带有一丝神秘主义的气息。

面部保留:完全保留参考照片中的面部特征、身份、面部结构和比例。不要改变她的脸。

画质:超写实、高品质、锐利的 8K 照片,具有真实的皮肤质感和自然细节。使用 iPhone 16 Pro 拍摄。竖幅 3:4 画面比例。
淡淡的半抹微笑
```

</details>

<details><summary><b>暗黑浪漫死神圣母人像</b> · 机器翻译</summary>

```text
写实风格的女性特写肖像,针对3:4画幅优化。机位——正对前方,与视线齐平。

姿势与氛围:女子头部微微转向一侧,梦幻的目光向上并投向侧面。她的右手优雅地触碰靠近锁骨的颈部。整体氛围神秘而迷人,带有鲜明的暗黑浪漫和柔和魅力妆感美学。

妆容与面部:受糖骷髅(圣死神)启发的创意万圣节妆容,覆盖半张脸。脸的左侧肌肤无瑕,睫毛蓬松,双唇自然色紧闭。右侧被塑造成骷髅造型:一只深色眼睛周围环绕着闪亮的水钻,鼻尖为黑色,一条深色线条模仿下颌轮廓。额头和下巴上排布着由细小水晶组成的对称图案。

发型与美甲:长而浓密的波浪卷发,自然披散在肩上,发丝和轮廓高度逼真。指甲很长,是精准的方形,涂着亮泽的黑色甲油。

服饰与配饰:头上戴着一顶硕大的皇冠状花环,由大朵人造白玫瑰制成,长长的透明光线向外延伸,形成发光的光环效果。她身穿白色服装,蓬松的质感如同花瓣。颈间闪烁着一条精致的钻石网球项链,右手无名指上戴着一枚戒指。

光线与背景:柔和均匀的光线。深色虚化背景。

不要改变面部特征或身份。

3:4画幅。

写实、高质量、清晰的8K照片,使用iPhone 16 Pro拍摄。
```

</details>

<details><summary><b>暗黑超现实有机人像</b> · 机器翻译</summary>

```text
画幅比例 3:4。
一张黑暗超现实的肖像，女孩被奇异的黑色形状环绕。特写，胸部以上，略微侧身。她的外貌——面部特征、肤色、发色——必须与参考图一致。保留纹身、疤痕、穿孔。

她的眼睛是全黑的，睁大且空洞，看不到眼白。苍白的皮肤，鼻子和脸颊上有雀斑，柔和的自然色嘴唇，微微张开。头发略显凌乱，发丝垂落在脸上。

在她的头部和肩膀周围——有几团黑色的亮面有机形状，像扭曲的手或触手。它们盘绕在她周围，将她的脸框在其中。这些黑色形状中嵌着巨大而逼真的人眼，眼周是淡粉色的皮肤——湿润、有光泽，望向不同的方向。其中一团爪状的黑色形状伸向她的脸颊。

她穿着一件朴素的黑色高领上衣。

背景：纯净的灰白色，柔和的渐变，虚化。

光线：柔和、冷调、从正面漫射而来。湿润的眼睛和亮面的黑色形状上有柔和的高光，她的脸上有柔和的阴影。

质感：真实干净的皮肤，自然的雀斑。湿润有光泽的眼睛，带反光。黑色有机形状——光滑、湿润、有光泽，像焦油或皮肤。轻微的胶片颗粒感。

不要插画，不要卡通，不要 3D。黑暗、令人不安、超现实、安静。
```

</details>

<details><summary><b>暗黑风格图像提示词</b></summary>

```text
创建一幅具有 ${style:dark} 美学风格的图像。你的图像应包含以下要素：

- **光照：** 阴郁且低调，着重突出阴影。
- **配色方案：** 以深色调为主，具有高对比度。
- **元素：** 包含神秘或隐于暗影中的人物、哥特式建筑，或夜间场景。

请随意调整 ${elements}，以契合你对暗黑风格图像的构想。
```

</details>

<details><summary><b>更换服装与背景</b> · 机器翻译</summary>

```text
我想把这张图片中的服装换成更好看的衣服，并把背景换成一些著名的地方
```

</details>

<details><summary><b>曼哈顿幻影</b></summary>

```text
{
  "title": "Manhattan Mirage",
  "description": "一个充满张力的电影式瞬间，捕捉一名女性在黄金时刻自信地穿过蒸汽弥漫的纽约街头十字路口。",
  "prompt": "你将使用提供的照片执行一次图像编辑。创建一张超写实的女性主体图像。风格极为细致，类似于使用Arri Alexa拍摄的电影画面，采用1:1的电影画幅比例。应用强烈的景深效果，模糊繁忙的背景，同时保持主体清晰。使用具有强烈逆光的电影级照明。主体穿着红色迷你裙，正在街上行走。",
  "details": {
    "year": "1999",
    "genre": "电影级写实主义",
    "location": "日落时分，一个粗粝而喧嚣的纽约市十字路口，井盖中升腾起蒸汽，背景中有模糊的黄色出租车。",
    "lighting": [
      "黄金时刻逆光",
      "镜头光晕",
      "高对比度体积光"
    ],
    "camera_angle": "低角度跟拍镜头，居中构图。",
    "emotion": [
      "自信",
      "充满力量",
      "冷漠疏离"
    ],
    "color_palette": [
      "深红",
      "沥青灰",
      "金黄",
      "深黑"
    ],
    "atmosphere": [
      "都市感",
      "动态",
      "电影感",
      "充满能量"
    ],
    "environmental_elements": "从地面升起的蒸汽柱、动态模糊的车流、飞翔的鸽子、湿漉漉的路面反射着夕阳。",
    "subject1": {
      "costume": "red mini skirt",
      "subject_expression": "锐利而自信的眼神，嘴唇微张，可能佩戴复古太阳镜。",
      "subject_action": "walking on the street"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "空无一人的街道",
        "影棚背景",
        "过曝的天空",
        "静态姿势"
      ],
      "exclude_styles": [
        "卡通",
        "3D渲染",
        "插画",
        "动漫",
        "素描"
      ],
      "exclude_colors": [
        "荧光绿",
        "粉彩粉红"
      ],
      "exclude_objects": [
        "智能手机",
        "现代汽车",
        "未来主义设备"
      ]
    }
  }
}
```

</details>

<details><summary><b>曼哈顿鸡尾酒电影感视频</b></summary>

```text
以曼哈顿鸡尾酒为中心的特写镜头，固定静止镜头，液体有极细微的流动，戏剧性的边缘轮廓光，高端鸡尾酒广告质感，主体孤立，简单的深色渐变背景，鸡尾酒周围留有空旷的负空间，9:16 竖屏，超写实。无人调酒师，无手部，无环境杂乱元素，产品广告风格，慢动作优雅呈现。

鸡尾酒配方：

2 盎司黑麦威士忌  
1 盎司甜苦艾酒  
2 滴安格斯特拉苦精  
装饰：波本樱桃（或根据喜好用柠檬皮卷）
```

</details>

<details><summary><b>最后的柔板</b></summary>

```text
{
  "title": "The Last Adagio",
  "description": "一位孤独的芭蕾舞者在被洪水淹没的废弃宏伟图书馆中表演，场景凄美动人。",
  "prompt": "你将使用提供的主体执行图像编辑。将主体1（女性）转变为后末日世界中的幸存者。她身处一座巨大且正在腐朽的图书馆内，地板上积满了水。光线从坍塌的天花板倾泻而下，照亮了空气中的尘埃微粒和水面的倒影。图像必须具有照片级真实感，采用电影级布光、高度细致的纹理，使用 Arri Alexa 拍摄，并具备浅景深效果，使主体清晰聚焦，背景则呈现柔和的散焦虚化。",
  "details": {
    "year": "Post-Collapse Era",
    "genre": "Cinematic Photorealism",
    "location": "一座宏伟的废弃图书馆，拥有高耸的书架、破败的建筑结构，以及积满静止、反光积水的地面。",
    "lighting": [
      "从坍塌屋顶射入的上帝之光",
      "水面反射出的柔和光线",
      "高对比度的电影级阴影"
    ],
    "camera_angle": "低角度广角镜头，捕捉水中倒影。",
    "emotion": [
      "忧郁的",
      "优雅的",
      "孤独的"
    ],
    "color_palette": [
      "去饱和的混凝土灰",
      "柔和的青绿色水体",
      "鲜艳的深红色",
      "布满灰尘的金色光线"
    ],
    "atmosphere": [
      "空灵的",
      "孤独的",
      "安静的",
      "雄伟的"
    ],
    "environmental_elements": "漂浮在水面上的老书纸张、光束中飞舞的尘埃微粒、水中的涟漪。",
    "subject1": {
      "costume": "一件破损、沾满污渍的白色芭蕾紧身衣，搭配一双洁净如新的红色手套。",
      "subject_expression": "神情宁静，双眼闭合，沉浸于舞蹈动作之中。",
      "subject_action": "跳舞"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "明亮的阳光",
        "干净的环境",
        "现代科技",
        "观众"
      ],
      "exclude_styles": [
        "卡通",
        "绘画",
        "素描",
        "3D 渲染"
      ],
      "exclude_colors": [
        "霓虹绿",
        "亮橙色"
      ],
      "exclude_objects": [
        "汽车",
        "动物",
        "手机"
      ]
    }
  }
}
```

</details>

<details><summary><b>月夜谷仓仓鸮刮画</b> · 机器翻译</summary>

```text
一幅黑色刮画板插画，描绘一只仓鸮栖息在夜晚安静谷仓内一根粗糙的木梁上，16:9 横幅，深黑墨板上刮出的白色线条形成高对比。首先是主体：一只心形脸的仓鸮，四分之三侧面朝左，大而深色的眼睛，细密排线刮出的白色面盘，带斑点的胸部，以及收拢翅膀上长长的刮刻羽毛质感。仓鸮身后，用稀疏的白线暗示出谷仓椽子和干草阁楼，梁上没有悬挂任何东西；右侧一扇破损的阁楼窗框出一轮明亮的满月和几颗刮出的星星。下方的草捆是松散的交叉排线；灰尘微粒是柔和月光中细小的刮点。技法：经典的刮画（scraperboard）效果，线条粗细富于变化，用交叉排线表现阴影，未触碰的黑色表现虚空，没有灰色渲染，没有色彩，没有数码光晕。氛围静谧、警觉，略带诡异但平静。没有文字，没有签名，没有水印，没有色调。
```

</details>

<details><summary><b>朋克风男友拥抱图</b></summary>

```text
在旁边制作一个男朋友，让他拥抱，让这个男朋友拥有莫西干发型、鼻中隔穿孔、高个子和山羊胡，还要让他是emo风格
```

</details>

<details><summary><b>服装隐形人台图</b></summary>

```text
{
  "model": "nano-banana",
  "task": "image_to_image_product_transformation",

  "objective": "将提供的服装产品图像转换为奢侈品工作室幽灵模特展示图，使服装看起来像是自然穿着在隐形模特上，并具有立体感，仿佛被空气充起。必须完全保留原始产品的身份，不得有任何改动。",

  "input_description": {
    "source_image_type": "平铺式服装产品照片",
    "background": "白色背景",
    "product_category": "通用服装（T恤、夹克、连帽衫、裤子、牛仔布、背心等）"
  },

  "transformation_rules": {
    "garment_structure": "将服装充气膨胀，仿佛穿在隐形模特身上，形成自然的身体体积和形状，同时保持内部为空",
    "mannequin_style": "高端时尚电商摄影中使用的奢侈品幽灵模特",
    "fabric_condition": "面料需完美熨烫，带有反映真实服装张力的细微自然褶皱",
    "pose": "呈现自然可穿戴的服装形态，如同放置在躯干或人体模型上，但不可见任何模特或人类存在",
    "center_alignment": "服装必须在画面中完全居中",
    "framing": "干净的产品目录构图，四周留有均衡的边距",
    "background": "纯白色专业工作室背景（#FFFFFF），无渐变、纹理、道具或阴影，仅允许非常柔和的自然接地阴影"
  },

  "lighting": {
    "style": "高端时尚电商工作室灯光风格",
    "direction": "柔和正面照明，辅以均衡的补光",
    "goal": "突出面料纹理、缝线、接缝和服装结构",
    "shadow_control": "在服装正下方保留极轻微的柔和阴影以增强真实感",
    "exposure": "明亮清晰的曝光，无过曝高光或压黑阴影"
  },

  "identity_preservation": {
    "color": "精确保留原始颜色值",
    "texture": "精确保留面料纹理和织法",
    "logos": "若存在原有标志，则必须完全保留",
    "stitching": "精确保留缝线图案",
    "details": "精确保留口袋、纽扣、拉链、接缝、刺绣、标签及所有构造细节"
  },

  "strict_prohibitions": [
    "不得添加新标志",
    "不得移除现有标志",
    "不得更改服装颜色",
    "不得改动缝线",
    "不得修改口袋",
    "不得修改服装设计",
    "不得虚构新的面料纹理",
    "不得改变服装比例",
    "不得添加配饰",
    "不得添加真人模特",
    "不得添加模特",
    "不得添加道具或场景",
    "不得裁剪服装"
  ],

  "fabric_realism": {
    "structure": "基于服装物理特性的逼真服装体积",
    "folds": "由重力和人体形态引起的细微自然褶皱",
    "tension": "根据服装类型，在胸部、肩部、腰部或臀部周围呈现轻度张力",
    "fabric_behavior": "尊重真实纺织品行为，如牛仔布的硬度、棉质的柔软性或针织物的弹性"
  },

  "composition_requirements": {
    "camera_angle": "正前方平视的产品目录角度",
    "symmetry": "平衡且专业的电商对齐方式",
    "product_visibility": "整个服装完整可见，不得裁剪",
    "catalog_standard": "构图一致，适用于自动化产品图库"
  },

  "quality_requirements": {
    "style": "奢侈品时尚电商摄影风格",
    "sharpness": "高细节清晰的服装纹理",
    "resolution": "高分辨率，适合产品放大查看",
    "cleanliness": "无灰尘、褶皱、伪影、失真或AI幻觉"
  },

  "pipeline_goal": {
    "use_case": "360度产品旋转展示流程",
    "consistency_requirement": "服装结构、光照和比例必须在多个角度间保持稳定且可重复",
    "output_type": "专业电商产品目录图像"
  }
}
```

</details>

<details><summary><b>未来AI课堂</b></summary>

```text
“一个未来主义的教室，学生们正在与全息AI导师互动。一些学生正在进行口头演讲，同时AI系统实时评估他们的回答。透明的数字屏幕显示学习进度、模拟场景和反馈循环。该环境将传统教室元素与先进的AI技术融合在一起。教师在一旁观察和指导，而AI负责初步评估。电影级灯光，超现实，高度细节化，8k分辨率，景深效果，未来教育氛围，概念艺术风格。”
```

</details>

<details><summary><b>未来皮影壁纸</b></summary>

```text
一幅高概念数字艺术壁纸作品，展现爪哇传统皮影戏的未来主义演变。想象一只机械化的哇扬 kulit（Wayang Kulit）手臂，其关节由抛光黄铜精巧打造，并嵌入发光的光纤电路，正伸向抓握一个足球。构图聚焦于“邻近性”原则，在机械手指与球体之间营造出一种磁性的张力。这种赛博朋克美学与全球足球文化的融合，是对足球运动中战略家们的致敬。整体风格为干净、高分辨率的矢量图像，线条锐利，霓虹点缀，背景深邃而抽象。原创角色设计，不含任何现实世界中的商标或标识。
```

</details>

<details><summary><b>未来超跑品牌标志</b></summary>

```text
为一个未来主义超级汽车品牌设计标志。该标志应：  
- 体现创新、速度与奢华。  
- 采用简洁而现代的设计元素。  
- 融入暗示高科技与卓越性能的形状和色彩。  
- 具备足够的适应性，可用于汽车徽章、营销材料和周边商品。  

可考虑使用以下元素：  
- 锐利的棱角和空气动力学形状  
- 金属或镀铬质感  
- 醒目的字体设计  

你的任务是创造一个能脱颖而出、象征尖端汽车卓越性的标志。
```

</details>

<details><summary><b>未来音乐流媒体房间人像</b></summary>

```text
使用上传的非洲男孩照片作为基础面部，创作一幅高度细致、逼真的图像：他自信而放松地坐在一个未来主义音乐流媒体体验房间的中央，构图对称且具有电影感。  
完全保留照片中的面部特征、肤色和发质。  
他的眼睛睁开，平静地望向前方，表情柔和而自信。相机角度与面部齐平，正对人物，清晰展现他的整张脸。  
他穿着时尚的服装：一件黑色或深橄榄色的宽松街头风上衣，现代工装裤，以及具有当代高端时尚感的优质运动鞋。  
他佩戴着高端的头戴式耳机。  
坐姿放松，双腿自然分开，双手 resting 在大腿上，散发出自信、平静和强大的气场。  
他身后是一块大型未来主义数字屏幕，带有受 Spotify 启发的用户界面，以霓虹绿与黑色调显示专辑封面、播放列表和现代界面元素。  
从他的耳机和头部区域，浮现出音乐视觉元素：发光的音符、全息均衡器、高音谱号符号和发光的声波，围绕他的头部形成一个环形的音乐能量光环。  
使用电影级灯光、柔和阴影和照片级真实质感，使整个场景显得沉浸、时尚且具有杂志品质。
```

</details>

<details><summary><b>末世拾荒者变身</b></summary>

```text
{
  "prompt": "You will perform an image edit using the person from the provided photo as the main subject. The face must remain clear and unaltered. Transform the subject into a hardened **Wasteland Scavenger/Survivor**, standing vigilant on a windswept dune in a desolate, post-apocalyptic landscape. Emphasize weathered, patched clothing, makeshift gear, gritty textures, and a bleak, survivalist atmosphere.",
  "details": {
    "year": "Undefined Post-Apocalyptic Future (e.g., 'After the Collapse')",
    "genre": "Post-Apocalyptic / Dystopian / Survival",
    "location": "A vast, desolate desert or barren wasteland. The ground is cracked earth, wind-blown sand, and scattered debris (e.g., rusted car parts, broken signs). A hazy, polluted sky looms overhead, perhaps with a distant, ruined city skyline barely visible on the horizon.",
    "lighting": "Harsh, muted, and desaturated sunlight, filtering through a dusty, smoggy atmosphere. Strong directional shadows, emphasizing the rough textures of the environment and the subject's gear. Overall tone is gritty and somewhat oppressive.",
    "camera_angle": "Medium shot to full-body, positioned slightly low to make the subject appear formidable against the stark landscape. The horizon line is low, emphasizing the vast, empty sky. (1:1 composition).",
    "emotion": "Vigilant, weary, resilient, and determined.",
    "costume": "Layered, patched-together clothing made from repurposed materials: torn denim, worn leather, tattered canvas. Functional, utilitarian gear like heavy boots, fingerless gloves, and a bandana or makeshift face covering. A visible collection of scavenged items (e.g., pouches, tools, water canteen) strapped to their body.",
    "color_palette": "Dominated by desaturated earth tones: dusty browns, faded greens, muted grays, and rusty oranges. Punctual pops of faded color from repurposed fabric scraps. The sky is a washed-out pale yellow or sickly green.",
    "atmosphere": "Bleak, harsh, dangerous, and lonely. The air feels heavy with dust and the silence of a dead world. A constant sense of survival against overwhelming odds.",
    "subject_expression": "A grim, focused gaze, scanning the horizon for threats or resources. Mouth set in a firm, determined line. Hair is windswept and dusty.",
    "subject_action": "Standing alert, possibly holding a makeshift weapon (e.g., a sharpened pipe, a crossbow, or a sturdy club) resting on their shoulder or held defensively. Their stance is one of readiness and caution.",
    "environmental_elements": "Fine dust or sand particles visibly blowing in the wind around the subject. Distant, skeletal remains of trees or buildings. Perhaps a single, circling scavenger bird high in the sky. The ground shows cracks and dry vegetation."
  }
}
```

</details>

<details><summary><b>机场走廊全身漫步照</b></summary>

```text
{
  "category": "AIRPORT_CORRIDOR_FULLBODY",
  "subject": {
    "demographics": "成年女性，21–27 岁，土耳其人外貌。",
    "hair": {
      "color": "深棕色",
      "style": "低马尾，旅行日休闲风格",
      "texture": "自然发丝，略带飞毛",
      "movement": "因行走产生的细微动态"
    },
    "face": {
      "eyes": "明亮、清醒",
      "skin_details": "真实肤质，无滤镜",
      "makeup": "极简、适合旅行的妆容"
    },
    "clothing": {
      "outfit": "旅行时尚风：外套 + 舒适长裤 + 运动鞋（无品牌标识）",
      "fabric": "膝盖与手肘处呈现真实布料褶皱"
    },
    "accessories": {
      "items": ["带轮行李箱（无品牌标识）", "小型托特包（无品牌标识）"],
      "jewelry": ["小巧银色圆环耳饰"]
    }
  },
  "pose": {
    "type": "全身行走抓拍",
    "orientation": "迈步中段，略带回眸",
    "hands": "一手扶在行李箱拉杆上，另一手提托特包肩带",
    "gaze": "回望镜头，流露微妙微笑",
    "posture": "放松而自信的旅行者姿态"
  },
  "setting": {
    "environment": "机场走廊",
    "background_elements": [
      "柔和的顶置灯光",
      "远处行人的运动模糊（面部不可辨识）",
      "光洁地面的倒影"
    ],
    "depth": "主体清晰锐利；背景因运动而虚化"
  },
  "camera": {
    "shot_type": "全身旅行摄影",
    "angle": "平视角度",
    "focal_length_equivalent": "26mm 手机镜头或 35mm 杂志级镜头",
    "framing": "4:5",
    "focus": "面部可清晰辨识，服装细节锐利"
  },
  "lighting": {
    "source": "机场顶置照明",
    "highlights": "地面自然反光",
    "shadows": "柔和、真实"
  },
  "mood_and_expression": {
    "tone": "旅行日的时尚感与抓拍感",
    "expression": "友善的微表情微笑"
  },
  "style_and_realism": {
    "style": "逼真风格的用户生成内容（UGC）旅行影像",
    "imperfections": "轻微倾斜构图，轻度噪点"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "轻度",
    "motion_blur": "仅限背景"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "可读文字标识", "品牌标识",
    "多余肢体", "扭曲变形的行李箱",
    "塑料质感皮肤", "CGI 渲染效果"
  ]
}
```

</details>

<details><summary><b>机械零件渲染转工程图</b></summary>

```text
{
  "task": "image_to_image",
  "description": "将三维机械零件渲染图转换为带完整尺寸标注的制造用工程图纸",
  "input_image": "3d_render_of_pipe_or_mechanical_part.png",
  "prompt": "机械工程图纸，多视图正交投影（主视图、俯视图、侧视图及剖视图），带完整尺寸标注的技术图纸，以毫米为单位的精确数字测量值，直径符号，半径标注，孔数标记，中心线，剖面线（剖面剖切线），统一的线宽，符合 ISO 机械制图标准，白底黑墨，可供制造直接使用的文档",
  "negative_prompt": "艺术风格，透视视图，柔和阴影，纹理，真实感光照，色彩，装饰性渲染，草图，手绘效果，尺寸标注不完整",
  "settings": {
    "model": "sdxl",
    "sampler": "DPM++ 2M Karras",
    "steps": 40,
    "cfg_scale": 6,
    "denoising_strength": 0.5,
    "resolution": {
      "width": 1024,
      "height": 1024
    }
  },
  "output_expectation": "符合 ISO 标准的机械图纸，尺寸清晰明确，适用于 CNC 加工、铸造或结构件制造等工艺参考"
}
```

</details>

<details><summary><b>机舱度假自拍</b></summary>

```text
{
  "subject": {
    "description": "一位外表自然、放松的年轻女性，坐在飞机座位上被捕捉到的瞬间。她散发着自信而随意的度假气息。皮肤洁净，没有纹身。戴着一顶轻便的度假帽和时尚的太阳镜。",
    "body": {
      "type": "曲线优美、女性化的轮廓。",
      "details": "自然的比例，放松的姿态，舒适的坐姿。",
      "pose": "坐在飞机座位上，微微向后靠，构图暗示相机由一只手在略高于头部的位置持握，并向下倾斜角度，仿佛在拍摄一张随意的前置摄像头自拍。手机本身不在画面中。"
    }
  },
  "wardrobe": {
    "top": "轻盈的夏季度假服装，例如宽松的亚麻衬衫、短款上衣或透气的罩衫。",
    "bottom": "高腰短裤、轻质面料的裙子或适合旅行的休闲夏装长裤。",
    "headwear": "度假帽或草帽。",
    "accessories": "太阳镜、简约的珠宝饰品、小项链、手表。"
  },
  "scene": {
    "location": "商业客机机舱内部。",
    "background": "她身后可见成排的飞机座位和其他乘客，面部清晰可见且自然，未被模糊处理。",
    "details": "逼真的飞行中氛围，包含细腻的机舱纹理、头顶行李舱和来自窗户的自然光线。"
  },
  "camera": {
    "angle": "前置摄像头视角，由一只手在略高于眼睛的位置持握，并向下倾斜角度。",
    "lens": "广角前置摄像头自拍镜头。",
    "aspect_ratio": "9:16",
    "depth_of_field": "平衡的景深，使主体和背景中的乘客都自然可见。"
  },
  "lighting": {
    "type": "柔和的机舱环境光与来自窗户的自然日光相结合。",
    "quality": "均匀、自然的光线，带有柔和的高光和真实的阴影。"
  }
}
```

</details>

<details><summary><b>极简产品信息图</b></summary>

```text
为 ${product} 创建一张高端极简主义工业设计风格的信息图。

该信息图必须自动适配 ${product} 的身份、类别、结构、功能以及现实世界中的设计语言。

重要提示：  
如果随 ${product} 一同上传了规格表、PDF、技术文档、产品描述、功能列表或参考文件，请仔细分析所上传的文件，并将其作为信息图所有内容的**首要真实来源**。

信息图中显示的所有标签、注释、规格、尺寸、组件、功能、技术、材料、端口、传感器、硬件细节和工程标注，只要在上传文件中可用，都必须直接从中提取。

信息图系统应具备智能能力：
- 读取并解析上传的文档
- 识别最重要的产品规格
- 自动提取技术特性
- 将产品规格转换为可视化信息图注释
- 生成精确的工程风格标注
- 优先采用上传文件中的信息，而非假设
- 根据检测到的产品类型自适应调整信息图布局

生成内容包括：
- 真实感产品渲染
- 在适用时显示半透明或爆炸式内部视图
- 技术箭头与手写风格注释
- 尺寸指示
- 真实的组件标签
- 工程可视化细节
- 高端展示构图

视觉风格：
- 极致简洁的 Apple 风 Keynote 美学
- 极简白色或浅灰色背景
- 居中产品构图
- 照相级真实感 3D 渲染
- 工业设计草图质感
- 优雅的手写风格注释字体
- 细腻的阴影与反射
- 单色技术标注
- 层级分明的信息图结构
- 未来感奢华科技展示风格

要求：
- 显示大型清晰标题：“${product}”
- 自动突出 ${product} 最具标志性与最重要的功能
- 生成真实的产品专属标签与技术说明
- 使用虚线箭头与优雅的间距
- 融合真实感与概念性工程插图
- 高细节材质与真实光照
- 专业高端产品展示美学
- 若存在上传的规格文件，信息图中的所有文本与注释必须准确反映上传数据

风格关键词：  
industrial design sketch, futuristic infographic, exploded view, transparent hardware visualization, premium keynote presentation, technical annotation design, minimalist product poster, engineering concept render, photorealistic technology showcase, luxury tech aesthetic

输出：  
超精细 4K 信息图渲染，16:9 宽高比，影棚灯光，高端材质，干净构图，优雅的单色标注系统
```

</details>

<details><summary><b>极简影棚 iPhone 抓拍风</b></summary>

```text
{
  "category": "STUDIO_IPHONE_CANDID_AWKWARD_FRAMING",
  "subject": {
    "demographics": "成年女性，21–27 岁，土耳其人外貌特征，青春感十足但具成年人气质。",
    "hair": {
      "color": "深棕色",
      "style": "自然蓬松波浪",
      "texture": "发丝清晰可见，略带几缕飞毛"
    },
    "face": {
      "eyes": "明亮、直视镜头",
      "skin_details": "高保真毛孔细节，不作柔化处理",
      "makeup": "干净自然妆容"
    },
    "clothing": {
      "outfit": "简约黑色上衣（无任何品牌标识）"
    },
    "accessories": {
      "jewelry": ["银色圆环耳饰"]
    }
  },
  "pose": {
    "type": "特写/半身抓拍照",
    "orientation": "取景略近，构图不完美",
    "hands": "一只手短暂入画、靠近发际线（手指形态准确）",
    "gaze": "与镜头直接眼神接触",
    "expression": "俏皮的细微微笑"
  },
  "setting": {
    "environment": "纯色影棚墙面",
    "background_elements": [
      "墙面细微纹理",
      "无任何道具"
    ],
    "depth": "面部锐利清晰，背景柔和虚化"
  },
  "camera": {
    "shot_type": "在洁净空间中呈现 iPhone 抓拍风格",
    "angle": "略高于眼平线角度",
    "focal_length_equivalent": "26mm 焦距等效（手机镜头质感）",
    "framing": "4:5 画幅，构图略显 awkward（轻微裁切发顶/头顶留白）",
    "focus": "双眼焦点锐利"
  },
  "lighting": {
    "source": "柔和漫射主光",
    "direction": "前侧方，光线轻柔",
    "quality": "自然光感，不反光、不油腻"
  },
  "mood_and_expression": {
    "tone": "抓拍感、俏皮、日常化",
    "atmosphere": "看似未经策划，却依然上镜"
  },
  "style_and_realism": {
    "style": "照片级真实感用户生成内容（Photoreal UGC）",
    "imperfections": "细微噪点，构图不完美"
  },
  "technical_details": {
    "aspect_ratio": "4:5",
    "noise": "轻微"
  },
  "constraints": {
    "adult_only": true,
    "no_text": true,
    "no_logos": true,
    "no_watermarks": true
  },
  "negative_prompt": [
    "过度修图", "美颜滤镜",
    "塑料感肌肤", "CGI",
    "多余手指", "扭曲的手部",
    "可读文字", "品牌标识", "水印"
  ]
}
```

</details>

<details><summary><b>极简抹茶镜前自拍</b> · 机器翻译</summary>

```text
一张写实的全身镜面自拍。画面中央是一位站在现代极简风室内的年轻女性。她用智能手机给自己拍照，手机遮住了脸，左手拿着一杯浅绿色饮品（抹茶或奶昔）。

姿势：
这位女性站在一面白墙旁，随意地用右肩靠着墙。她站在两扇白色门之间。右腿伸直，左腿弯曲成 90 度，脚掌抵在墙上，构图放松而有动感。她的头微微倾斜，视线看向手机屏幕。

服饰与风格：
- 上衣：一件轻薄的半透明奶油色长袖衬衫，内搭白色吊带背心。
- 下装：宽松的短裤，带有细细的白色和浅蓝色条纹，灵感来自睡衣风格，腰间有抽绳。
- 配饰：白色高筒棉袜。左手腕上戴着一条精致的手链或手表。手机配有浅金色或米色手机壳。

发型与妆容：
- 发型：头发做成柔和的波浪，自然垂在肩上。
- 妆容：她的脸被手机遮住了，但整体看上去是自然、极简的“素颜”妆感。

氛围与情绪：
氛围温馨、居家、放松、平静而安宁。画面类似社交媒体上唯美的镜面自拍，捕捉慢节奏早晨或在家放松的感觉。

光线：
柔和的自然日光轻轻洒满房间，没有强烈的阴影，凸显了轻盈的面料和干净的室内质感。

室内与背景：
一间北欧极简风格的现代公寓。白色的墙壁，配有现代黑色横向把手的白色门，以及浅色木地板（复合地板或拼花地板）。可以看到一面黑框大镜子的左边缘。一切都干净、整洁、不杂乱。

拍摄角度：
通过一面大落地镜以视平线高度拍摄。手机端平，形成自然的全身视角。竖版构图。

不要改变我的面部特征。

宽高比：3:4。

超写实、高质量、清晰的 8K 照片，使用 iPhone 16 Pro Max 拍摄。
```

</details>

<details><summary><b>极简渔夫插画</b></summary>

```text
{
  "colors": {
    "color_temperature": "冷色调",
    "contrast_level": "高对比度",
    "dominant_palette": [
      "蓝色",
      "白色",
      "黑色"
    ]
  },
  "composition": {
    "camera_angle": "广角镜头",
    "depth_of_field": "深景深",
    "focus": "小渔夫与巨大眼睛之间的关系",
    "framing": "构图大量使用负空间，将小渔夫置于左上角，以强调他下方巨大蓝色形体的广阔，营造出强烈的尺度感。"
  },
  "description_short": "一幅极简风格的图形插画，描绘一名男子在一条巨大的蓝鲸背上钓鱼，而蓝鲸正从下方注视着他。",
  "environment": {
    "location_type": "抽象",
    "setting_details": "一个超现实的双色环境，上部为米白色区域，下部为巨大的纯蓝色区域，代表水中的一只巨型生物。",
    "time_of_day": "未知",
    "weather": "无"
  },
  "lighting": {
    "intensity": "中等",
    "source_direction": "未知",
    "type": "环境光"
  },
  "mood": {
    "atmosphere": "无知的危险与超现实的平静",
    "emotional_tone": "紧张"
  },
  "narrative_elements": {
    "character_interactions": "存在单方面的意识；巨型生物正在注视渔夫，但渔夫对自己所坐之物毫无察觉。",
    "environmental_storytelling": "人与他所处生物之间的巨大尺度差异，讲述了一个关于无知、未知深处的故事，或许也隐喻企业或人类对自然的漠视。",
    "implied_action": "整个场景充满张力，暗示那只巨型生物随时可能移动，从而揭示渔夫岌岌可危的处境。"
  },
  "objects": [
    "蓝鲸",
    "眼睛",
    "人",
    "钓鱼竿",
    "凳子"
  ],
  "people": {
    "ages": [
      "成年"
    ],
    "clothing_style": "西装",
    "count": "1",
    "genders": [
      "男性"
    ]
  },
  "prompt": "一幅极简风格的矢量插画，描绘一名身穿黑色西装的男子坐在一个小凳子上钓鱼。他位于一片广阔深蓝色表面之上，该表面被揭示为一只巨型鲸鱼，其一只巨大的眼睛可见于画面底部。背景为单一的米白色。整体风格为扁平、图形化且超现实，利用负空间营造出紧张感和巨大的尺度感。",
  "style": {
    "art_style": "极简主义",
    "influences": [
      "平面设计",
      "超现实主义",
      "概念艺术"
    ],
    "medium": "数字艺术"
  },
  "technical_tags": [
    "极简主义",
    "矢量艺术",
    "扁平设计",
    "超现实",
    "概念性",
    "负空间",
    "高对比度",
    "图形艺术",
    "象征主义"
  ],
  "use_case": "用于训练模型识别象征意义和视觉叙事的概念艺术数据集。",
  "uuid": "34500b18-1643-4d4c-97b6-20876089bd15"
}
```

</details>

<details><summary><b>极简监控插画</b></summary>

```text
{
  "colors": {
    "color_temperature": "warm",
    "contrast_level": "high",
    "dominant_palette": [
      "orange",
      "off-white",
      "black",
      "yellow"
    ]
  },
  "composition": {
    "camera_angle": "eye-level shot",
    "depth_of_field": "deep",
    "focus": "The relationship between the small man and the large eyes watching him.",
    "framing": "The small figure is centered at the bottom, while the upper two-thirds of the frame are filled with a pattern of large eyes looking down, creating an oppressive and symmetrical composition."
  },
  "description_short": "A minimalist graphic illustration of a small man in a yellow shirt being watched by many large, stylized eyes against a vibrant orange background.",
  "environment": {
    "location_type": "abstract",
    "setting_details": "The setting is a solid, textured orange background, devoid of any other environmental elements, creating a symbolic and non-literal space.",
    "time_of_day": "unknown",
    "weather": "none"
  },
  "lighting": {
    "intensity": "moderate",
    "source_direction": "unknown",
    "type": "ambient"
  },
  "mood": {
    "atmosphere": "A feeling of being under constant scrutiny or surveillance.",
    "emotional_tone": "tense"
  },
  "narrative_elements": {
    "character_interactions": "A single individual is the subject of an intense, overwhelming gaze from a multitude of disembodied eyes, suggesting a power imbalance and a feeling of being judged.",
    "environmental_storytelling": "The vast, empty space dominated by giant eyes emphasizes the isolation and vulnerability of the small figure, telling a story of surveillance, paranoia, or social pressure.",
    "implied_action": "The man is standing still, seemingly frozen under the weight of the gaze. The scene is static but psychologically charged."
  },
  "objects": [
    "Eyes",
    "Human figure"
  ],
  "people": {
    "ages": [
      "adult"
    ],
    "clothing_style": "Casual (yellow t-shirt, black pants)",
    "count": "1",
    "genders": [
      "male"
    ]
  },
  "prompt": "A striking, minimalist graphic illustration depicting a small man in a yellow t-shirt and black pants, standing alone at the bottom of the frame. Above him, a multitude of giant, stylized eyes with black pupils stare down intently. The background is a solid, textured, vibrant orange. The mood is tense and surreal, conveying a powerful sense of surveillance, paranoia, and being judged. The art style is clean, symbolic, and high-contrast.",
  "style": {
    "art_style": "minimalist",
    "influences": [
      "graphic design",
      "surrealism",
      "poster art"
    ],
    "medium": "digital art"
  },
  "technical_tags": [
    "illustration",
    "minimalism",
    "surrealism",
    "symbolism",
    "paranoia",
    "surveillance",
    "graphic art",
    "high contrast",
    "conceptual"
  ],
  "use_case": "Editorial illustration for topics such as data privacy, social anxiety, government surveillance, or public scrutiny.",
  "uuid": "a11d9c1f-ca39-4d02-a6ec-21769391501c"
}
```

</details>

<details><summary><b>极简线条人物插画</b></summary>

```text
一个极简主义的线稿绘画，描绘一个简单角色，表达“克服障碍”的概念。采用干净的黑色连续线条风格，白色背景。该概念应通过简单的几何形状和基本视觉隐喻来传达。严格保持扁平、类似矢量的美学风格，不得包含 3D 元素、真实质感或复杂细节。
```

</details>

<details><summary><b>极简风景插画</b></summary>

```text
{  
  "colors": {  
    "color_temperature": "暖色调",  
    "contrast_level": "高对比度",  
    "dominant_palette": [  
      "红色",  
      "蓝色",  
      "白色",  
      "橙色"  
    ]  
  },  
  "composition": {  
    "camera_angle": "广角镜头",  
    "depth_of_field": "深景深",  
    "focus": "蜿蜒小径与广阔的红色地貌",  
    "framing": "前景的灌木丛框定画面底部，而蜿蜒小径则作为一条强有力的引导线，将观者视线引向整个场景。"  
  },  
  "description_short": "一幅极简主义插画：一名孤独人物正沿一条白色小径穿行于超现实的起伏地貌之上；地貌上覆盖着鲜艳的红色灌木丛，天空澄澈湛蓝。",  
  "environment": {  
    "location_type": "风景",  
    "setting_details": "一片超现实、辽阔的起伏丘陵地貌，完全被浓密、圆润、富有肌理感的灌木丛所覆盖，灌木呈明艳的红色与橙色渐变；一条醒目的白色小径呈之字形穿越地形；天空为纯色、无任何细节的广阔平面。",  
    "time_of_day": "午后",  
    "weather": "晴朗"  
  },  
  "lighting": {  
    "intensity": "强烈",  
    "source_direction": "顶部",  
    "type": "自然光"  
  },  
  "mood": {  
    "atmosphere": "充满活力的孤寂感与超现实旅程",  
    "emotional_tone": "宁静"  
  },  
  "narrative_elements": {  
    "environmental_storytelling": "高度统一且超现实的地貌尺度与微小孤立的人物形成强烈反差，暗示一段漫长而意义重大的旅程，凸显探索、孤寂以及个体在浩瀚世界中所处位置等主题。",  
    "implied_action": "人物正沿小径行走，朝山坡更高处及地貌更深处前行，暗示旅程正在进行中。"  
  },  
  "objects": [  
    "红色灌木丛",  
    "白色小径",  
    "山丘",  
    "天空",  
    "人物"  
  ],  
  "people": {  
    "ages": [  
      "未知"  
    ],  
    "clothing_style": "休闲风格，明黄色上衣",  
    "count": "1",  
    "genders": [  
      "未知"  
    ]  
  },  
  "prompt": "Ryo Takemasa 创作的一幅极简主义数字插画：一座广阔起伏的山丘，覆盖着浓密、明艳的红色与橙色圆形灌木丛；一条干净的白色小径蜿蜒向上，伸向远方；一名身着明黄色夹克的微小人物正沿小径行走，其身形在宏大而超现实的地貌中显得格外渺小；上方天空为纯色、无云的天蓝色；整体风格简洁、图形化，并带有微妙的纸张肌理质感，营造出宁静孤寂与史诗般旅程并存的情绪氛围。",  
  "style": {  
    "art_style": "极简主义",  
    "influences": [  
      "日本平面设计",  
      "极简主义"  
    ],  
    "medium": "插画"  
  },  
  "technical_tags": [  
    "极简主义",  
    "插画",  
    "风景",  
    "鲜明色彩",  
    "高对比度",  
    "超现实",  
    "引导线",  
    "孤寂",  
    "图形化",  
    "肌理感"  
  ],  
  "use_case": "艺术风格识别数据集，用于生成具有氛围感或极简主义风格的风景插画。",  
  "uuid": "9c266725-0038-4a06-9832-13afc71ba44f"  
}
```

</details>

<details><summary><b>极简风格腊肠犬插画</b></summary>

```text
{
  "colors": {
    "color_temperature": "中性",
    "contrast_level": "中等",
    "dominant_palette": [
      "柔和的蓝色",
      "浅灰色"
    ]
  },
  "composition": {
    "camera_angle": "正面平视",
    "depth_of_field": "浅景深",
    "focus": "风格化的腊肠犬",
    "framing": "主体居中构图，其细长的身体形成复杂交织的图案，充满整个画面。"
  },
  "description_short": "一幅极简主义图形插画，描绘一只极长的蓝色腊肠犬，身体扭曲并编织成复杂的抽象绳结图案，背景为浅灰色。",
  "environment": {
    "location_type": "影棚",
    "setting_details": "纯色、平坦的浅灰色背景。",
    "time_of_day": "未知",
    "weather": "无"
  },
  "lighting": {
    "intensity": "中等",
    "source_direction": "环境光",
    "type": "柔光"
  },
  "mood": {
    "atmosphere": "俏皮而巧妙的平面设计",
    "emotional_tone": "平静"
  },
  "narrative_elements": {
    "environmental_storytelling": "该图像利用腊肠犬身体修长的特点制造视觉双关，将其极度夸张至荒诞程度，形成装饰性的绳结状图案，融合动物形态与抽象设计。",
    "implied_action": "狗以静态、装饰性元素呈现，没有动作表现。"
  },
  "objects": [
    "腊肠犬"
  ],
  "people": {
    "count": "0"
  },
  "prompt": "一幅极简主义图形插画，描绘一只风格化的蓝色腊肠犬。狗的身体长得不可思议，精细地上下交错缠绕，形成复杂的类似凯尔特绳结的图案。设计干净现代，蓝色形体带有微妙的纹理，柔和的阴影营造出轻微的三维错觉。整个图形置于纯色的浅暖灰色背景之上。整体美学风格俏皮、巧妙且富有艺术感。",
  "style": {
    "art_style": "图形插画",
    "influences": [
      "极简主义",
      "扁平化设计",
      "凯尔特结饰",
      "矢量艺术"
    ],
    "medium": "数字艺术"
  },
  "technical_tags": [
    "极简主义",
    "平面设计",
    "插画",
    "矢量艺术",
    "腊肠犬",
    "狗",
    "扁平化设计",
    "绳结",
    "抽象",
    "风格化"
  ],
  "use_case": "平面设计灵感、海报艺术、图库插画，或用于训练风格化动物插画的AI数据。"
}
```

</details>

<details><summary><b>极简高调影棚肖像</b></summary>

```text
高调极简影棚人像，纯白无缝背景，柔和的美颜光线，伊朗女性，不化妆。闭眼半秒，眉头中部上扬后放松，从眼睑可见一次长长的呼气—— surrender，“好吧，你说什么就是什么”。干净的负空间。图像下方，一个极简的素描轮廓框，内有铅笔手写文字："باشه، هرچی تو بگی"
```

</details>

<details><summary><b>极简黑色墨线画风</b></summary>

```text
用户的视觉品味由极简主义和通过强烈、高对比度构图实现的即兴表达所定义。他们偏爱仅由纯黑墨水绘制在纯白背景上的艺术作品，大量运用留白。这种美学推崇松散、未经修饰的线条，以最高效的视觉语言捕捉主题的原始本质，并引发情感共鸣。
```

</details>

<details><summary><b>极限速度</b></summary>

```text
{
  "title": "Terminal Velocity",
  "description": "一幅高风险的动作画面，描绘一名女性在崩塌的工业隧道中疾奔，周围火花四溅，一片混乱。",
  "prompt": "你将执行一次图像编辑，创作一幅超逼真、电影级质量的动作镜头。结果必须是照片级真实感的、高度细节化的，并具有电影感的灯光效果。模仿使用 Arri Alexa 拍摄的大片镜头外观，浅景深。描绘主体1正朝摄像机方向在黑暗且崩塌中的工业隧道内疾跑，周围飞舞着火花和坠落的碎片。",
  "details": {
    "year": "当代动作惊悚片",
    "genre": "电影级写实主义",
    "location": "一个破败的、充满蒸汽的工业维修隧道，灯光闪烁，电线裸露。",
    "lighting": [
      "高对比度的明暗对照法",
      "来自爆炸火花的暖色背光",
      "冷色调、粗粝的荧光环境光",
      "通过蒸汽的体积光"
    ],
    "camera_angle": "低角度正面跟拍镜头，背景带有运动模糊。",
    "emotion": [
      "肾上腺素激增",
      "恐慌",
      "决心"
    ],
    "color_palette": [
      "混凝土灰",
      "警示橙",
      "钢蓝色",
      "深阴影黑"
    ],
    "atmosphere": [
      "混乱",
      "爆炸性",
      "粗粝",
      "幽闭恐惧"
    ],
    "environmental_elements": "倾泻而下的电火花、运动模糊的碎片、从破裂管道喷出的蒸汽、湿漉漉的混凝土地面映射出混乱场景。",
    "subject1": {
      "costume": "黑色迷你裙，白色露脐上衣，皮质无指手套",
      "subject_expression": "极度专注，因用力而微微张嘴，皮肤上汗珠闪烁，头发向后飞扬。",
      "subject_action": "奔跑"
    },
    "negative_prompt": {
      "exclude_visuals": [
        "阳光",
        "平静的环境",
        "干净的表面",
        "微笑",
        "静止站立"
      ],
      "exclude_styles": [
        "卡通",
        "3D渲染",
        "插画",
        "素描",
        "低分辨率"
      ],
      "exclude_colors": [
        "粉彩粉红",
        "鲜艳绿色",
        "柔和色彩"
      ],
      "exclude_objects": [
        "树木",
        "天空",
        "动物",
        "车辆"
      ]
    }
  }
}
```

</details>

<details><summary><b>柔美妆容休闲特写</b> · 机器翻译</summary>

```text
一位年轻女子的特写人像。主要焦点是她极其浓密、蓬松的头发，造型为大而柔软的波浪，发根蓬松感明显。

妆容：
柔和魅力美学。无瑕的肌肤带有细腻光泽（颧骨和鼻梁上有高光）和柔和的腮红。分明的黑色猫眼眼线和浓密的睫毛。饱满的双唇涂有柔和的粉色裸色唇蜜，嘟成俏皮的亲吻状（双唇闭合，不露牙齿）。经典的红色长指甲。

服装与配饰：
一件合身的基础款黑色长袖上衣，面料在手腕处略微堆叠成褶皱。唯一可见的首饰是一只耳朵上简约的银色圈形耳环。

姿势：
女孩直视镜头。她的右手优雅地抬起，手背和手指放松，轻轻触碰脸颊和下颌线。

背景：
时尚现代的室内空间，类似餐厅或休闲区，因浅景深而被大幅虚化，形成美丽的焦外光斑。可见木质格栅天花板、温暖的聚光灯、隐约可见的带红酒杯的桌子，以及绿色天鹅绒椅子的椅背。

光线、相机角度与氛围：
柔和的正面光线，完美地突出她的面部特征，没有刺眼的阴影。相机直接置于平视角度。氛围俏皮撩人、自信而放松。从技术上看，它像是一张高质量的自拍或人像照片。

不要改变女孩的面部特征、眼型、眉毛、鼻子或嘴唇。保持100%的面部相似度。

宽高比：3:4。
超写实、高质量、锐利的8K照片，使用iPhone 16 Pro Max拍摄。
```

</details>

<details><summary><b>树屋度假屋概念设计简报</b> · 机器翻译</summary>

```text
你是一位专攻树屋、花园工作室和小型木structure 静修小屋的建筑设计师，同时也是一位视觉化艺术总监。我会描述我梦想中的一座树屋。你要把它变成一份清晰的设计概念，包含固定的设计细节，再提供两条可直接使用的图像提示词，展示**同一座**树屋在两个不同季节、从两个不同视角看到的样子，让两张 AI 图像看起来像同一栋真实建筑的照片。

宿主树与场地：${site:a single huge old oak in a sloping meadow at the edge of a beech forest, trunk about 1.2 m wide, splitting into three main limbs about 5 m up}
使用者与使用方式：${use:a family retreat for reading, sleepovers for two kids, and quiet evenings for the adults}
尺寸与高度：${size:a small cabin about 3 x 4 m on a deck about 3.5 m above the ground}
风格方向：${style:warm natural timber, a little storybook but not cartoonish, simple modern details}
必备元素：${must_have:a big window facing the forest, a covered deck, a small wood stove, a rope swing}
预算水平：${budget:self-build with a carpenter's help, mid-range materials}
视角 A：${view_a:summer afternoon, full green canopy, seen from the meadow at the front left}
视角 B：${view_b:snowy winter evening, bare branches, windows glowing, seen from the front right}

请输出：

1. 设计概念
   - 概念名称，以及用两句话讲述这座树屋应有的感觉。
   - 用文字描述结构：平台如何支撑（与树的连接点、立柱、斜撑）、露台尺寸、小屋占地、屋顶形式，以及出入方式（楼梯、爬梯或吊桥），并给出大致的高度和尺寸。
   - 立面：前、左、右、后墙上分别有什么（门、窗、烟囱），以草地一侧为视角来描述。
   - 色板：6 种有名称的颜色（用"蜜糖雪松色""苔藓绿"这类简单名称），并说明各自用在哪里。
   - 材料与饰面：外墙板、屋顶、露台、栏杆、门窗、金属件、照明。

2. 固定设计细节（一致性清单）
   一份含 12 到 16 条的编号清单，列出在每张图像中都必须完全一致的细节：宿主树及其与露台的交接方式、支撑、外墙板、屋顶、每扇窗和门的颜色与形状、烟囱、栏杆、楼梯、秋千、露台家具、灯具和地面细节，每条都要有精确位置。每条都写成图像生成器能够照做的简短具体短语（例如"正面墙右半部分的蓝绿色荷兰式分体门"）。

3. 图像提示词 A：基准视角
   一条详细的 AI 图像生成器提示词：从视角 A 的位置拍摄的写实建筑摄影，呈现树屋，采用视角 A 的季节和光线。包含从该位置可见的每一个固定细节及其正确位置（左右以相机视角为准），以及相机高度和镜头、光线、氛围，以及 16:9 横向构图。最后以排除项结尾（无人物、无文字、无标志）。

4. 图像提示词 B：第二视角
   一条详细的视角 B 提示词，要写给无法看到图 A 的纯文本图像生成器：用完整的文字再次复述**所有**固定细节（绝不写"同前"），为新的相机位置正确摆放每个细节，描述新出现的可见内容，并且只改变季节、天气、时间和光线（例如屋顶和露台上有雪、枝条光秃、窗内透出暖光、烟囱冒烟）。材料、颜色和比例保持一致。

5. 一致性核对清单
   十条是/否检查项，用于对比图 B 与图 A（例如"门是否仍是蓝绿色，且分为上下两半？"）。

6. 建造与安全说明
   一份简短清单，涵盖树木健康（请树艺师检查树木）、让树能继续生长的连接方式、荷载与栏杆高度、火炉周围的防火安全、需要在当地核查的许可，以及三种省钱的方法。

规则：
- 在所述的尺寸、高度和预算下保持可建造；对任何不安全或不现实之处加以标注。
- 使用朴素的颜色名称和具体的形状；不要单独使用"温馨"或"现代"这类含糊的词。
- 不使用品牌名，不出现真实人物，图像中不出现可读文字。
- 如果我的描述缺少关键信息，请做出合理假设，并把这些假设列在最上方。
```

</details>

<details><summary><b>根据截图生成界面设计说明</b></summary>

```text
This is a ${page_type:dashboard} of a modern ${focus:government audit} app called ${brand:AuditFlow}.

彻底分析此截图中的用户界面，并尽可能详细地描述，以便从 UI 设计师交接给开发人员。该简报应涵盖浅色模式和深色模式，并包含与 Tailwind CSS v4.3 默认值匹配的响应式断点。

以结构化的 JSONC 格式输出特性。

对于颜色，提取一个粗略的调色板，仅详细说明强调色和复杂的媒体元素。目标是仅使用 2 种调色板：主色和辅色，类似于 Tailwind 颜色。除了这 2 种之外，你可以定义任意数量的灰色和强调色，用于更复杂的 UI 元素（如渐变、阴影、SVG 等）。

最后附上一个提示，说明如何为开发人员实现该用户界面，但不要提及任何技术规格；只需简要说明要实现的 UI 以及标记规则和用法。将该提示输出为 Markdown 代码块。

输出应为两个代码块：一个用于设计简报，另一个用于 JSONC 设计规范。
```

</details>

<details><summary><b>格朗基小巷黑白人像</b> · 机器翻译</summary>

```text
一张黑白人像摄影,画面中是一位身形纤细的年轻女性,留着中分的黑色长直发,坐在一条狭窄的城市小巷地面上,小巷两侧是陈旧粗糙的石墙,右侧墙上伸出一个老旧的金属水龙头。她穿着一件未扣扣子的格纹法兰绒衬衫,袖子卷起,内搭一件印有清晰可见字母的灰色图案 T 恤,下身是深色紧身牛仔裤,脚蹬系带的黑色厚底战斗靴。姿势:背靠着墙,右手搭在头上抓着头发,左腿朝镜头伸出,靴底正对镜头,形成极端的前景强透视,右腿弯曲。直视镜头,表情严肃、忧郁、若有所思,没有笑容。从低位地面视角略微仰拍,使用 24mm 广角镜头,中等景深,焦点清晰对准她的脸,背景略微虚化。柔和漫射的自然日光,中高对比度,细腻的胶片颗粒,另类 grunge 街头杂志风格,内省的都市氛围,照片级写实,高度细致,8K 分辨率。
```

</details>

<details><summary><b>桌游封面美术指导</b> · 机器翻译</summary>

```text
你是一家小型独立桌游出版商的美术总监。你要把一个游戏概念转化为盒面封面美术简报，让插画师或 AI 图像生成器无需猜测就能照着执行。

游戏详情：
- 暂定标题：${title:Sky Orchard Merchants}
- 一句话简介：${pitch:A cozy cooperative trading game where players crew wooden airships that harvest fruit from floating orchard islands and trade it between sky towns.}
- 玩家人数与年龄：${players:1 to 4 players, ages 10 and up}
- 游戏时长与重度：${weight:45 minutes, light to medium strategy}
- 三个词概括氛围：${mood:whimsical, warm, adventurous}
- 偏好的美术风格：${style:hand-painted gouache with visible brush texture}
- 盒子形状：${box:square 1:1}
- 需要避免的内容：${avoid:dark or scary imagery, violence, cluttered compositions}

请按以下顺序输出简报：

1. 货架测试。用两句话说明：顾客在三米外应该对这款游戏产生什么感受、理解什么，以及什么会让他们拿起这个盒子。

2. 焦点与故事瞬间。选择游戏中的一个瞬间来呈现，说明主体以及正在发生什么。解释为什么这个瞬间比你考虑过的另外两个更能卖出这款游戏。

3. 构图。针对该盒子形状描述布局：标题区域的位置（保持平静、不放细节）、焦点的位置、景深层次（前景、中景、背景），以及在线商店缩略图尺寸下轮廓如何保持清晰可辨。

4. 角色与道具。列出角色、生物和关键道具，每个附一个暗示游戏机制的细节（例如，水果篮暗示收集套组）。

5. 光线与色板。时间段、光线方向，以及四到五种有名称的颜色组成的色板，要契合氛围，并在摆满其他游戏的货架上脱颖而出。

6. 风格指导。媒介、笔触、细节程度，以及用文字描述的两到三个宽泛风格参考（写年代或技法，绝不写在世艺术家的名字）。

7. 无障碍与年龄检查。确认封面适合目标年龄段，没有出现避免清单上的任何内容，且不单靠颜色来保证可读性。

8. 最终图像提示词。写一段 120 到 180 词的文字，供 AI 图像生成器直接使用。必须包含主体、动作、场景、光线、色板、风格、含标题留白的构图、画幅比例，以及这一句："无文字、无字母、无标志、无边框。"不要把游戏标题放进图像里；标题由设计师后期添加。

9. 变体。给出最终提示词的两个一行变体：一个更换时间段，一个更换焦点角色。

整份简报要务实具体。如果缺少某项游戏详情或描述含糊，请做出合理选择，并在最上方的“假设”下用一行注明。
```

</details>

<details><summary><b>梦幻双重曝光人像</b></summary>

```text
{
  "prompt": "一位年轻女性的空灵特写肖像，她留着短而蓬松的金色卷发。她双眼轻闭，面部沐浴在日落时分温暖金黄的光辉之中。采用创意双重曝光技法，营造出她侧脸轮廓柔和、半透明的叠影效果。背景为深沉而富有情绪感的青绿色，形成强烈对比。整体氛围宁静、内省且如梦似幻。采用电影级摄影风格，焦点柔和，并带有微妙的胶片颗粒感。",
  "style": {
    "medium": "photography",
    "art_style": "cinematic",
    "influences": [
      "fine art photography",
      "surrealism"
    ]
  },
  "composition": {
    "camera_angle": "close-up",
    "framing": "chest up, slightly off-center",
    "focus": "woman's face and hair",
    "depth_of_field": "shallow",
    "special_technique": "double exposure"
  },
  "lighting": {
    "type": "natural",
    "time": "golden hour",
    "intensity": "strong",
    "direction": "side",
    "color_temperature": "warm"
  },
  "colors": {
    "contrast": "high",
    "palette": [
      "golden yellow",
      "orange",
      "teal",
      "dark cyan"
    ]
  },
  "environment": {
    "setting": "outdoor",
    "time_of_day": "evening",
    "background": "dark, blurred twilight sky",
    "weather": "clear"
  },
  "subject": {
    "count": 1,
    "gender": "female",
    "age": "young adult",
    "appearance": {
      "hair": "short, wavy blonde",
      "expression": "eyes closed, calm"
    },
    "clothing": "light-colored pleated blouse",
    "accessories": ["necklace"]
  },
  "mood": {
    "atmosphere": "dreamy",
    "emotional_tone": "calm and introspective"
  },
  "narrative": {
    "theme": "inner peace and self-reflection",
    "implied_state": "quiet contemplation or meditation",
    "symbolism": "double exposure suggests a spiritual or dream-like separation of mind and body"
  },
  "rendering_details": {
    "focus_quality": "soft",
    "grain": "subtle film grain"
  }
}
```

</details>

<details><summary><b>梦幻慢门时尚人像</b> · 机器翻译</summary>

```text
使用 Nano Banana 2.1 制作

提示词:

竖版 9:16 抓拍时尚人像,一位美丽的东亚女孩,身穿合身的长袖橙色高领毛衣和黑色超短裙,长长的黑发凌乱而松散。她一边快速旋转,一边回头看向镜头,双臂张开,头发飞扬。VERY SLOW SHUTTER SPEED 1/8–1/15 sec,极其逼真的动态模糊,手臂和头发上有长长的鬼影拖尾,身体模糊,面部依稀可辨,背景有水平方向的光streaks,相机抖动,双重曝光效果,浓重的 35mm 胶片颗粒,梦幻,情绪化,欠曝,照片级真实。No CGI, no frozen motion, no sharp arms or hair.
```

</details>

<details><summary><b>梦幻空灵金发人像</b></summary>

```text
一位金发女子置身于梦幻般的空灵摄影场景中，带有光影效果与超现实元素。
```

</details>

<details><summary><b>梦幻草地人像</b></summary>

```text
{
  "colors": {
    "color_temperature": "暖色调",
    "contrast_level": "中等对比度",
    "dominant_palette": [
      "深红色",
      "橄榄绿",
      "奶油色",
      "浅黄色"
    ]
  },
  "composition": {
    "camera_angle": "平视角度",
    "depth_of_field": "浅景深",
    "focus": "一位身穿红裙的年轻女性",
    "framing": "该女性略微偏离画面中心，以侧面姿态行走穿过场景。背景呈现出强烈的漩涡状散焦效果，自然地框住并突出了主体。"
  },
  "description_short": "一位身穿短款红裙和白色运动鞋的年轻女性侧身走过一片盛开着白色和黄色野花（可能是雏菊）的茂密绿草地，背景具有明显的漩涡模糊效果。",
  "environment": {
    "location_type": "户外",
    "setting_details": "一片郁郁葱葱的草地或花园，密集生长着白色和黄色的野花，很可能是雏菊。整个背景严重失焦，形成抽象的漩涡图案。",
    "time_of_day": "下午",
    "weather": "多云"
  },
  "lighting": {
    "intensity": "适中",
    "source_direction": "正面光源",
    "type": "自然光"
  },
  "mood": {
    "atmosphere": "梦幻且怀旧",
    "emotional_tone": "忧郁"
  },
  "narrative_elements": {
    "character_interactions": "该女性独自一人，似乎沉浸在思绪中。",
    "environmental_storytelling": "空灵的、漩涡状的花卉背景暗示这是一个梦境或记忆片段，强调了主体内省的心理状态。她鲜艳的红裙与周围柔和的绿色环境形成鲜明对比，突显其为画面的情感中心。",
    "implied_action": "该女性正从一处走向另一处，暗示一段旅程、片刻沉思，或是对自然的一次逃离。"
  },
  "objects": [
    "女性",
    "红裙",
    "白色运动鞋",
    "花朵",
    "草"
  ],
  "people": {
    "ages": [
      "年轻成人"
    ],
    "clothing_style": "波西米亚浪漫风格；一条短款、飘逸的红色连衣裙，带有褶边细节，搭配休闲的白色运动鞋。",
    "count": "1",
    "genders": [
      "女性"
    ]
  },
  "prompt": "一张梦幻而富有艺术感的照片，描绘一位有着棕色随风飘扬头发的年轻女性，侧身行走在雏菊盛开的草地上。她穿着一件鲜艳的短款红裙和白色运动鞋。图像具有极浅的景深，在背景中创造出标志性的漩涡状散焦效果，将人物框住。光线柔和自然，带有温暖的复古色彩调校。整体氛围沉思而忧郁，捕捉到一个转瞬即逝的内省时刻。",
  "style": {
    "art_style": "电影感",
    "influences": [
      "印象派",
      "Fine art photography（精致艺术摄影）"
    ],
    "medium": "摄影"
  },
  "technical_tags": [
    "浅景深",
    "散焦",
    "漩涡散焦",
    "Petzval镜头",
    "侧面拍摄",
    "复古滤镜",
    "动态模糊",
    "自然光"
  ],
  "use_case": "艺术类图库照片、时尚杂志配图、书籍封面，或用于特定镜头效果研究的数据集。",
  "uuid": "0fce3d8f-9de2-4a75-8d3f-6398eea47e24"
}
```

</details>

<details><summary><b>植物主视觉横幅图</b></summary>

```text
创建一张适用于英雄区（hero section）的图片，宽高比为 16:9。图片中应呈现 6–7 种不同类型的植物，全部置于自然环境中，并有阳光倾泻而入。请确保构图美观，且适合作为网页英雄区使用。
```

</details>

<details><summary><b>椰林飘香鸡尾酒视频</b></summary>

```text
电影感竖屏智能手机视频，肖像方向，居中构图，上下留有充足空间。一杯优雅的 Piña Colada 鸡尾酒置于画面中央的高帧椰壳杯中。干净的大理石吧台表面仅占据画面底部三分之一，柔和的热带日光下，棕榈叶的阴影在背景中轻轻移动。缓慢倾倒浓稠质地的 Piña Colada，可见明显的厚重质感与冷凝水珠。摄像机以缓慢的垂直推进微距运镜，浅景深，呈现高端饮品广告风格，极简美学，肖像构图，纵向构图，高帧画面，9:16 宽高比，无文字。
```

</details>

<details><summary><b>欧洲模特美妆分析板</b></summary>

```text
{
  "prompt": "A minimalist editorial beauty analysis board featuring a European female model with a balanced oval-to-heart face shape and a softly defined jawline. Subtle Central–Northern European facial characteristics with refined symmetry and elegant proportions. Neutral gray background, clean studio lighting, high realism.\n\nTop section: front-facing barefaced portrait, natural skin texture with neutral-to-cool undertones, no makeup, hair pulled back, calm neutral expression. A thin blue outline tracing the face shape.\n\nRight side graphic text layout titled 'FACE' with small bullet points describing facial features: balanced oval face shape, softly pronounced cheekbones, feminine and delicate jawline, slightly tapered natural chin, straight to softly contoured nose bridge, clear almond-to-rounded eyes with a soft gaze.\n\nMiddle section: two studio portraits labeled 'barefaced', one straight-on view and one three-quarter profile, minimal European editorial styling, soft diffused lighting, realistic skin texture and fine facial details.\n\nBottom section: two mirror selfie style images labeled 'with makeup', fresh luminous skin with a natural satin finish, modern European soft glam makeup, gentle blush tones, nude pink or soft rose glossy lips, subtle eyeliner with softly lifted outer corners, natural lashes, softly styled layered hair, contemporary European fashion styling inspired by Paris and Milan street elegance.\n\nFashion magazine editorial layout, clean modern typography, balanced spacing, muted neutral tones, professional beauty photography, high resolution, realistic skin texture and natural proportions.",
  "negative_prompt": "exaggerated makeup, heavy contour, harsh shadows, cartoon style, anime, distorted facial proportions, overly sharp jawline, low resolution, oversaturated colors, messy layout, watermark, logo, text artifacts, duplicated faces, extra limbs",
  "style": "editorial beauty photography",
  "quality": "high",
  "lighting": "soft studio lighting",
  "background": "neutral gray"
}
```

</details>
