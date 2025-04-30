#!/usr/bin/env python3
"""
ttf_to_js.py - Convert a .ttf font file into a JavaScript module with Base64 embedding.

Author: OG0N
License: MIT
"""


import base64
import os
import argparse
import sys

def convert_ttf_to_js(ttf_path: str, js_output_path: str, var_name: str = "customFont"):
    """Converts a .ttf file to a JavaScript module with embedded Base64 data URI."""
    if not os.path.isfile(ttf_path):
        raise FileNotFoundError(f"Font file not found: {ttf_path}")

    try:
        with open(ttf_path, "rb") as font_file:
            encoded_font = base64.b64encode(font_file.read()).decode('utf-8')
    except Exception as e:
        raise RuntimeError(f"Failed to read font file: {e}")

    js_content = f"""// Auto-generated from {os.path.basename(ttf_path)}
// Embedded TTF font as Base64 for web usage.

const {var_name} = {{
  name: "{os.path.basename(ttf_path)}",
  data: "data:font/ttf;base64,{encoded_font}"
}};
// Embedded TTF font as Base64 for web usage.

const {var_name} = {{
  name: "{os.path.basename(ttf_path)}",
  data: "data:font/ttf;base64,{encoded_font}"
}};

export default {var_name};
"""

    try:
        with open(js_output_path, "w", encoding="utf-8") as js_file:
            js_file.write(js_content)
    except Exception as e:
        raise RuntimeError(f"Failed to write JS file: {e}")

    print(f"✅ JavaScript file successfully created at: {js_output_path}")

def main():
    parser = argparse.ArgumentParser(description="Convert a TTF font file into a JS module.")
    parser.add_argument("ttf", help="Path to the .ttf font file")
    parser.add_argument("-o", "--output", help="Output .js file path (default: <ttf_basename>.js)")
    parser.add_argument("-v", "--var", help="JavaScript variable name (default: customFont)", default="customFont")

    args = parser.parse_args()

    js_output_path = args.output or os.path.splitext(os.path.basename(args.ttf))[0] + ".js"

    try:
        convert_ttf_to_js(args.ttf, js_output_path, args.var)
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
