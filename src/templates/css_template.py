def create_css_template(
    background_color="#ffffff",
    primary_text_color="#000000",
    secondary_text_color="#212529",
    information_1_color="#80ffdb",
    information_2_color="#48bfe3",
    information_3_color="#5390d9",
    warning_color="#ffba08",
    alert_color="#d00000",
    highlight_color="#ffd60a",
    disabled_color="#6c757d",
    start_color="#00ff00",
    end_color="#ff0000",
    foot_color="#964B00",
    hand_color="#FFCBA4"
):
    return f"""
:root {{
    --background: {background_color};
    --primary-text: {primary_text_color};
    --secondary-text: {secondary_text_color};
    --information-1: {information_1_color}; 
    --information-2: {information_2_color};
    --information-3: {information_3_color};
    --warning: {warning_color};
    --alert: {alert_color};
    --highlight: {highlight_color};
    --disabled: {disabled_color};
    --start: {start_color};
    --finish: {end_color};
    --foot: {foot_color};
    --hand: {hand_color};
}}
"""
