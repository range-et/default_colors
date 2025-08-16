def create_csharp_template(
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
    hand_color="#FFCBA4",
):
    template = f"""
    namespace Utility
    {{
        public static class ColorPalette
        {{
            // Predefined colors
            public static readonly Color Background;
            public static readonly Color PrimaryText;
            public static readonly Color SecondaryText;

            // Annotation colors
            public static readonly Color Information1;
            public static readonly Color Information2;
            public static readonly Color Information3;

            public static readonly Color Warning1;

            public static readonly Color Alert;

            public static readonly Color Highlight;
            public static readonly Color Disabled;

            public static readonly Color Start;
            public static readonly Color Hand;
            public static readonly Color Foot;
            public static readonly Color Finish;

            // Other predefined properties
            public static readonly float LowOpacity;
            public static readonly float HighOpacity;

            // Static constructor to initialize colors
            static ColorPalette()
            {{
                // Base
                Background = ColorFromHex("{background_color}");
                PrimaryText = ColorFromHex("{primary_text_color}");
                SecondaryText = ColorFromHex("{secondary_text_color}");

                // Annotation colors
                Information1 = ColorFromHex("{information_1_color}");
                Information2 = ColorFromHex("{information_2_color}");
                Information3 = ColorFromHex("{information_3_color}");

                Warning1 = ColorFromHex("{warning_color}");
                Alert = ColorFromHex("{alert_color}");

                Highlight = ColorFromHex("{highlight_color}");
                Disabled = ColorFromHex("{disabled_color}");

                Start = ColorFromHex("{start_color}");
                Hand = ColorFromHex("{hand_color}");
                Foot = ColorFromHex("{foot_color}");
                Finish = ColorFromHex("{end_color}");

                // set the cpossible opacities
                LowOpacity = 0.2f;
                HighOpacity = 0.8f;
            }}

            // Create RGB color from 0-255 values
            private static Color ColorFromRGB(int r, int g, int b)
            {{
                r = Mathf.Clamp(r, 0, 255);
                g = Mathf.Clamp(g, 0, 255);
                b = Mathf.Clamp(b, 0, 255);

                return new Color(r / 255f, g / 255f, b / 255f);
            }}

            // Converts a hex color code to a Color object
            public static Color ColorFromHex(string hexCode)
            {{
                if (hexCode.StartsWith("#"))
                {{
                    hexCode = hexCode.Substring(1); // Remove the '#' if present.
                }}

                if (hexCode.Length != 6)
                {{
                    throw new System.ArgumentException("Invalid hex color code. It should be 6 characters long.");
                }}

                // Parse the red, green, and blue components from the hex string.
                float r = int.Parse(hexCode.Substring(0, 2), System.Globalization.NumberStyles.HexNumber) / 255f;
                float g = int.Parse(hexCode.Substring(2, 2), System.Globalization.NumberStyles.HexNumber) / 255f;
                float b = int.Parse(hexCode.Substring(4, 2), System.Globalization.NumberStyles.HexNumber) / 255f;

                return new Color(r, g, b, 1f); // Default alpha is 1 (fully opaque).
            }}
        }}
    }}
    """
    return template
