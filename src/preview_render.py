from PIL import Image, ImageDraw, ImageFont
import os

def render_palette(data: dict, out_path: str, width: int = 2000, height: int = 2000):
    """
    Render a color spec JSON (using the schema you provided) into a preview image.
    - json_path: path to your colors.json
    - out_path: where to save the PNG
    - width/height: canvas size
    """

    d = data["Default_Colors"]
    g = d["General_UI_Colors"]
    info = d["Information_Indicators"]
    warn = d["Warnings_and_Alerts"]
    hl = d["Highlights_and_Disabled"]
    move = d["Movement_Colors"]

    # Base colors
    bg = tuple(g["Background"]["rgb"])
    primary = tuple(g["Primary_Text"]["rgb"])
    secondary = tuple(g["Secondary_Text"]["rgb"])

    # Canvas
    img = Image.new("RGB", (width, height), bg)
    draw = ImageDraw.Draw(img)

    # Fonts (falls back gracefully if DejaVuSans isn’t available)
    try:
        font_main = ImageFont.truetype("Helvetica", 64)
        font_sub  = ImageFont.truetype("Helvetica", 52)
        font_small= ImageFont.truetype("Helvetica", 40)
    except Exception as e:
        print(e)
        font_main = ImageFont.load_default()
        font_sub  = ImageFont.load_default()
        font_small= ImageFont.load_default()

    # Layout helpers
    x_margin, y = 100, 80
    line_gap, block_gap = 14, 64

    def add_line(text, color, font):
        nonlocal y
        draw.text((x_margin, y), text, fill=tuple(color), font=font)
        y += int(font.size + line_gap)

    def add_pair(head, color, sub=None, sub_color=None):
        nonlocal y
        add_line(head, color, font_main)
        if sub:
            add_line(sub, sub_color if sub_color else secondary, font_sub)
        y += block_gap - line_gap

    # Sections (mirrors your sample layout)
    add_pair(g["Primary_Text"]["name"], primary, g["Secondary_Text"]["name"], secondary)

    add_pair(f'{info["Information_1"]["name"]} - System status',    info["Information_1"]["rgb"])
    add_pair(f'{info["Information_2"]["name"]} - Secondary information', info["Information_2"]["rgb"])
    add_pair('Secondary Text - Successful operations', info["Information_3"]["rgb"])

    add_pair(f'{warn["Warning_1"]["name"]} - Caution', warn["Warning_1"]["rgb"])
    add_pair(f'{warn["Alert_1"]["name"]} - Critical Alert', warn["Alert_1"]["rgb"])

    add_pair(f'{hl["Highlight"]["name"]} 1 - Temp focus', hl["Highlight"]["rgb"])
    add_pair(f'{hl["Disabled"]["name"]} 1 - Inactive',    hl["Disabled"]["rgb"])

    add_pair('Start Indicator - Start a move / line / waypoint', move["Start"]["rgb"])
    add_pair('Hand / Position / upper body waypoint',            move["Hand"]["rgb"])
    add_pair('Foot / Position / lower body waypoint',            move["Foot"]["rgb"])
    add_pair('Finish Indicator - finish move / line / waypoint', move["Finish"]["rgb"])

    # “Background” tag in the top-right
    tag = "Background"
    tw, th = draw.textbbox((0,0), tag, font=font_small)[2:]
    draw.text((width - tw - 40, 24), tag, fill=secondary, font=font_small)

    # save
    img.save(os.path.join(out_path, "rendered_palette.png"), "PNG")