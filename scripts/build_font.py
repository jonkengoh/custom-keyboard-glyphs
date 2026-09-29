import json
import sys
from pathlib import Path

import fontforge


def main() -> None:
    config = json.loads(sys.argv[1])

    font_config = config["font"]
    glyph_config = config["glyphs"]
    alphabet = config["alphabet"]

    font = fontforge.font()
    font.fontname = font_config["name"]
    font.familyname = font_config["name"]
    font.fullname = font_config["name"]
    font.em = font_config["units_per_em"]

    glyph_directory = Path(glyph_config["directory"])

    for character, filename in alphabet.items():
        glyph = font.createChar(ord(character))
        glyph.width = font_config["default_advance_width"]
        glyph.importOutlines(str(glyph_directory / filename))

    output_path = Path("build") / f"{font_config['name']}.ttf"
    output_path.parent.mkdir(parents=True, exist_ok=True)

    font.generate(str(output_path))
    font.close()


if __name__ == "__main__":
    main()