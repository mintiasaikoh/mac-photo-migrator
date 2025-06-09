import tkinter as tk
from PIL import Image, ImageDraw, ImageFont
import os

# アイコン画像の生成（512x512）
def create_app_icon():
    # 画像サイズ
    size = 512
    
    # 新しい画像を作成（背景色：グラデーション風）
    img = Image.new('RGB', (size, size), color='white')
    draw = ImageDraw.Draw(img)
    
    # グラデーション背景
    for i in range(size):
        color_value = int(255 - (i / size * 100))
        color = (70, 130, 180, 255)  # SteelBlue
        draw.rectangle([(0, i), (size, i+1)], fill=(70, 130, 180))
    
    # 円形の背景
    margin = 50
    draw.ellipse([margin, margin, size-margin, size-margin], fill='white')
    
    # カメラアイコン風のデザイン
    camera_color = (70, 130, 180)
    
    # カメラ本体
    body_left = 150
    body_top = 200
    body_right = 360
    body_bottom = 300
    draw.rounded_rectangle([body_left, body_top, body_right, body_bottom], 
                          radius=20, fill=camera_color)
    
    # レンズ
    lens_center_x = (body_left + body_right) // 2
    lens_center_y = (body_top + body_bottom) // 2
    lens_radius = 40
    draw.ellipse([lens_center_x - lens_radius, lens_center_y - lens_radius,
                  lens_center_x + lens_radius, lens_center_y + lens_radius],
                 fill='white')
    draw.ellipse([lens_center_x - lens_radius + 10, lens_center_y - lens_radius + 10,
                  lens_center_x + lens_radius - 10, lens_center_y + lens_radius - 10],
                 fill=camera_color)
    
    # 矢印（移行を表す）
    arrow_start_x = 320
    arrow_y = 250
    arrow_length = 60
    draw.polygon([(arrow_start_x, arrow_y - 10),
                  (arrow_start_x, arrow_y + 10),
                  (arrow_start_x + arrow_length - 20, arrow_y + 10),
                  (arrow_start_x + arrow_length - 20, arrow_y + 20),
                  (arrow_start_x + arrow_length, arrow_y),
                  (arrow_start_x + arrow_length - 20, arrow_y - 20),
                  (arrow_start_x + arrow_length - 20, arrow_y - 10)],
                 fill='orange')
    
    # テキスト
    try:
        # システムフォントを使用
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 36)
    except:
        font = None
    
    text = "Photo"
    if font:
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_x = (size - text_width) // 2
        draw.text((text_x, 350), text, fill=camera_color, font=font)
    
    # PNG形式で保存
    icon_path = "icon.png"
    img.save(icon_path, "PNG")
    print(f"アイコンを作成しました: {icon_path}")
    
    # ICNSファイル用に複数サイズを作成
    sizes = [16, 32, 64, 128, 256, 512]
    for s in sizes:
        resized = img.resize((s, s), Image.Resampling.LANCZOS)
        resized.save(f"icon_{s}x{s}.png", "PNG")
    
    print("各サイズのアイコンを作成しました")

if __name__ == "__main__":
    create_app_icon()
