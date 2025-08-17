import json
import os
import argparse

from templates.c_sharp_template import create_csharp_template
from templates.css_template import create_css_template
from preview_render import render_palette

def load_json(json_path):
    with open(json_path, "r") as file:
        data = json.load(file)
    return data


def prepare_templates(json_data):
    background_color = (
        json_data.get("Default_Colors", {}).get("General_UI_Colors", {}).get("Background", {}).get("hex", "#ffffff")
    )
    primary_text_color = (
        json_data.get("Default_Colors", {}).get("General_UI_Colors", {}).get("Primary_Text", {}).get("hex", "#ffffff")
    )
    secondary_text_color = (
        json_data.get("Default_Colors", {}).get("General_UI_Colors", {}).get("Secondary_Text", {}).get("hex", "#ffffff")
    )
    information_1_color = (
        json_data.get("Default_Colors", {})
        .get("Information_Indicators", {})
        .get("Information_1", {})
        .get("hex", "#ffffff")
    )
    information_2_color = (
        json_data.get("Default_Colors", {})
        .get("Information_Indicators", {})
        .get("Information_2", {})
        .get("hex", "#ffffff")
    )
    information_3_color = (
        json_data.get("Default_Colors", {})
        .get("Information_Indicators", {})
        .get("Information_3", {})
        .get("hex", "#ffffff")
    )
    warning_color = (
        json_data.get("Default_Colors", {}).get("Warnings_and_Alerts", {}).get("Warning_1", {}).get("hex", "#ffffff")
    )
    alert_color = (
        json_data.get("Default_Colors", {}).get("Warnings_and_Alerts", {}).get("Alert_1", {}).get("hex", "#ffffff")
    )
    highlight_color = (
        json_data.get("Default_Colors", {})
        .get("Highlights_and_Disabled", {})
        .get("Highlight", {})
        .get("hex", "#ffffff")
    )
    disabled_color = (
        json_data.get("Default_Colors", {}).get("Highlights_and_Disabled", {}).get("Disabled", {}).get("hex", "#ffffff")
    )
    start_color = json_data.get("Default_Colors", {}).get("Movement_Colors", {}).get("Start", {}).get("hex", "#ffffff")
    end_color = json_data.get("Default_Colors", {}).get("Movement_Colors", {}).get("Finish", {}).get("hex", "#ffffff")
    foot_color = json_data.get("Default_Colors", {}).get("Movement_Colors", {}).get("Foot", {}).get("hex", "#ffffff")
    hand_color = json_data.get("Default_Colors", {}).get("Movement_Colors", {}).get("Hand", {}).get("hex", "#ffffff")

    # Prepare the C# template
    csharp_code = create_csharp_template(
        background_color=background_color,
        primary_text_color=primary_text_color,
        secondary_text_color=secondary_text_color,
        information_1_color=information_1_color,
        information_2_color=information_2_color,
        information_3_color=information_3_color,
        warning_color=warning_color,
        alert_color=alert_color,
        highlight_color=highlight_color,
        disabled_color=disabled_color,
        start_color=start_color,
        end_color=end_color,
        foot_color=foot_color,
        hand_color=hand_color,
    )

    # Prepare the CSS template
    css_code = create_css_template(
        background_color=background_color,
        primary_text_color=primary_text_color,
        secondary_text_color=secondary_text_color,
        information_1_color=information_1_color,
        information_2_color=information_2_color,
        information_3_color=information_3_color,
        warning_color=warning_color,
        alert_color=alert_color,
        highlight_color=highlight_color,
        disabled_color=disabled_color,
        start_color=start_color,
        end_color=end_color,
        foot_color=foot_color,
        hand_color=hand_color,
    )

    return {"c_sharp": csharp_code, "css": css_code}


if __name__ == "__main__":
    # load the json file
    argparse.ArgumentParser(description="Visualize color data from JSON")
    parser = argparse.ArgumentParser(description="Visualize color data from JSON")
    parser.add_argument("--json_path", type=str, required=True, help="Path to the JSON file")
    parser.add_argument("--visualize", action="store_true", default=True, help="Visualize colors from JSON")
    parser.add_argument("--output_path", type=str, default="build/", help="Path to the output files")

    args = parser.parse_args()

    # first check if build folder exists
    if not os.path.exists(args.output_path):
        os.makedirs(args.output_path)
    else:
        print("Output directory already exists")
        # if directory exists then delete the contents
        for filename in os.listdir(args.output_path):
            file_path = os.path.join(args.output_path, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)

    try:
        json_data = load_json(args.json_path)
        print("Loaded JSON data")
        
        if args.visualize:
            try:
                render_palette(json_data, args.output_path)
                print("Rendered color palette image")
            except Exception as e:
                print(f"Error rendering palette: {e}")
        
        # Generate C# and CSS code
        code = prepare_templates(json_data)
        print("Generated code")

        # save out the code
        with open(os.path.join(args.output_path, "ColorPalette.cs"), "w") as f:
            f.write(code["c_sharp"])
        with open(os.path.join(args.output_path, "ColorPalette.css"), "w") as f:
            f.write(code["css"])
        print("Saved code")

    except Exception as e:
        print(f"Error loading JSON: {e}")


    
