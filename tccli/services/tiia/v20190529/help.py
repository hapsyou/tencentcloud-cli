# -*- coding: utf-8 -*-
DESC = "tiia-2019-05-29"
INFO = {
  "RecognizeCar": {
    "params": [
      {
        "name": "ImageBase64",
        "desc": "图片的BASE64值；\nBASE64编码后的图片数据大小不超过3M，支持PNG、JPG、JPEG、BMP格式，暂不支持GIF格式。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片的 ImageUrl、ImageBase64必须提供一个，如果都提供，只使用ImageUrl。\n\n图片URL地址。支持的图片格式：PNG、JPG、JPEG、BMP，暂不支持GIF格式。支持的图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。"
      }
    ],
    "desc": "腾讯云车辆属性识别可对汽车车身及车辆属性进行检测与识别，目前支持11种车身颜色、20多种车型、300多种品牌、4000多种车系+年款的识别，同时支持对车标的位置进行检测。"
  },
  "DetectLabel": {
    "params": [
      {
        "name": "ImageUrl",
        "desc": "图片的URL地址。"
      },
      {
        "name": "ImageBase64",
        "desc": "图片经过base64编码的内容。与ImageUrl同时存在时优先使用ImageUrl字段。 \n图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 \n非腾讯云存储的Url速度和稳定性可能受一定影响。"
      }
    ],
    "desc": "传入一张图片，识别出图片中存在的物体，并返回物体的名称（分类）、置信度，一张图片会给出多个可能的标签。"
  },
  "AssessQuality": {
    "params": [
      {
        "name": "ImageUrl",
        "desc": "图片URL地址。 \n图片限制： \n• 图片格式：PNG、JPG、JPEG。 \n• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 \n建议：\n• 图片像素：大于50*50像素，否则影响识别效果； \n• 长宽比：长边：短边<5； \n接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。"
      },
      {
        "name": "ImageBase64",
        "desc": "图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。"
      }
    ],
    "desc": "评估输入图片在视觉上的质量，从多个方面评估，并同时给出综合的、客观的清晰度评分，和主观的美观度评分。"
  },
  "DetectProduct": {
    "params": [
      {
        "name": "ImageUrl",
        "desc": "图片URL地址。 \n图片限制： \n• 图片格式：PNG、JPG、JPEG。 \n• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 \n建议：\n• 图片像素：大于50*50像素，否则影响识别效果； \n• 长宽比：长边：短边<5； \n接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。"
      },
      {
        "name": "ImageBase64",
        "desc": "图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。"
      }
    ],
    "desc": "本接口支持识别图片中包含的商品，能够输出商品的品类名称、类别，还可以输出商品在图片中的位置。支持一张图片多个商品的识别。"
  },
  "ImageModeration": {
    "params": [
      {
        "name": "Scenes",
        "desc": "本次调用支持的识别场景，可选值如下：\n1. PORN，即色情识别\n2. TERRORISM，即暴恐识别\n3. POLITICS，即政治敏感识别\n\n支持多场景（Scenes）一起检测。例如，使用 Scenes=[\"PORN\", \"TERRORISM\"]，即对一张图片同时进行色情识别和暴恐识别。"
      },
      {
        "name": "ImageUrl",
        "desc": "图片URL地址。 \n图片限制： \n • 图片格式：PNG、JPG、JPEG。 \n • 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 \n • 图片像素：大于50*50像素，否则影响识别效果； \n • 长宽比：长边：短边<5； \n接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。"
      },
      {
        "name": "Config",
        "desc": "预留字段，后期用于展示更多识别信息。"
      },
      {
        "name": "Extra",
        "desc": "透传字段，透传简单信息。"
      },
      {
        "name": "ImageBase64",
        "desc": "图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段。"
      }
    ],
    "desc": "本接口提供多种维度的图像审核能力，支持色情和性感内容识别，政治人物和涉政敏感场景识别，以及暴恐人物、场景、旗帜标识等违禁内容的识别。"
  },
  "EnhanceImage": {
    "params": [
      {
        "name": "ImageUrl",
        "desc": "图片URL地址。 \n图片限制： \n• 图片格式：PNG、JPG、JPEG。 \n• 图片大小：所下载图片经Base64编码后不超过4M。图片下载时间不超过3秒。 \n建议：\n• 图片像素：大于50*50像素，否则影响识别效果； \n• 长宽比：长边：短边<5； \n接口响应时间会受到图片下载时间的影响，建议使用更可靠的存储服务，推荐将图片存储在腾讯云COS。"
      },
      {
        "name": "ImageBase64",
        "desc": "支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。图片经过base64编码的内容。最大不超过4M。与ImageUrl同时存在时优先使用ImageUrl字段"
      }
    ],
    "desc": "传入一张图片，输出清晰度提升后的图片。\n\n可以消除图片有损压缩导致的噪声，和使用滤镜、拍摄失焦导致的模糊。让图片的边缘和细节更加清晰自然。\n\n"
  },
  "DetectCelebrity": {
    "params": [
      {
        "name": "ImageUrl",
        "desc": "图片的URL地址。支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      },
      {
        "name": "ImageBase64",
        "desc": "图片经过base64编码的内容。与ImageUrl同时存在时优先使用ImageUrl字段。 \n图片存储于腾讯云的Url可保障更高下载速度和稳定性，建议图片存储于腾讯云。 \n非腾讯云存储的Url速度和稳定性可能受一定影响。\n支持PNG、JPG、JPEG、BMP，不支持 GIF 图片。"
      }
    ],
    "desc": "传入一张图片，可以识别图片中包含的人物是否为公众人物，如果是，输出人物的姓名、基本信息、脸部坐标。\n\n支持识别一张图片中存在的多个人脸，针对每个人脸，会给出与之最相似的公众人物。"
  }
}