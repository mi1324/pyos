import requests
import json
import base64

url = "https://qr.api.cli.im/create/fastChangeMhConf"

# 二维码内容
content = "https://mhimg.clewm.net/cli/images/beautify/new/logo/音频-0210.png"  # 换成你的实际内容，如 "https://example.com"

mh_config = {
    "logourl": "https://mhimg.clewm.net/cli/images/beautify/new/logo/音频-0210.png",
    "logoshape": "no",
    "logo_pos": "0",
    "logo_shadow": 1,
    "logow": 90,
    "logoh": "auto",
    "data": content,
    "level": "H",
    "transparent": 0,
    "bgcolor": "#ffffff",
    "forecolor": "https://mhimg.clewm.net/cli/images/beautify/new/forecolor/16.png",
    "blockpixel": "12",
    "embed_text_fontfamily": "simhei.ttc",
    "eye_use_fore": "1",
    "qrcode_eyes": "circle_circle",
    "outcolor": "#000000",
    "incolor": "#000000",
    "body_type": "17",
    "qr_rotate": "0",
    "fontfamily": "simhei.ttc",
    "logosize": 70,
    "logo_dealed": "",
    "logo_bg_type": 0,
    "foretype": 1,
    "forecolor2": "",
    "nomargin": 0,
    "version": 1
}

payload = {
    "code_type": "3",
    "mh_str": json.dumps(mh_config, ensure_ascii=False),
    "code_tplid": "1115476481",
    "style_size_id": "61",
    "uid": "0",
    "params_ass_info": json.dumps(
        [{"web_url": content, "qr_name": content}], ensure_ascii=False
    )
}

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15",
    "Referer": "https://cli.im/text",
    "Origin": "https://cli.im",
    "Content-Type": "application/x-www-form-urlencoded",
}

resp = requests.post(url, data=payload, headers=headers)
result = resp.json()

if result.get("code") == 1 and result["data"].get("img_base64"):
    

    import base64

    img_base64 = result["data"]["img_base64"]

    # 去掉 data:image/png;base64, 前缀
    if img_base64.startswith("data:image/"):
        img_base64 = img_base64.split(",", 1)[1]  # 关键：取列表第二个元素

    # 解码并保存
    img_data = base64.b64decode(img_base64)
    with open("qrcode.png", "wb") as f:
        f.write(img_data)
    print("✅ 二维码已保存到 qrcode.png")



