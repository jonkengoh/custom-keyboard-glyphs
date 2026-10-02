import json
import subprocess
import sys
from pathlib import Path

import yaml


FONTFORGE_SCRIPT = Path(__file__).with_name("build_font.py")


def main() -> None:
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python scripts/build.py <config.yaml>")

    config_path = Path(sys.argv[1]).resolve()

    with config_path.open("r", encoding="utf-8") as file:
        config = yaml.safe_load(file)

    config["glyphs"]["directory"] = str(
        (config_path.parent / config["glyphs"]["directory"]).resolve()
    )

    validate_config(config)

    config_json = json.dumps(config)

    subprocess.run(
        [
            "fontforge",
            "-script",
            str(FONTFORGE_SCRIPT),
            config_json,
        ],
        check=True,
    )

def validate_config(config: dict) -> None:
    if not isinstance(config, dict):
        raise SystemExit("Configuration error: root must be a mapping")

    font_config = config.get("font")
    if not isinstance(font_config, dict):
        raise SystemExit("Configuration error: 'font' must be a mapping")

    for key in ("name", "units_per_em", "default_advance_width"):
        if key not in font_config:
            raise SystemExit(
                f"Configuration error: missing 'font.{key}'"
            )

    glyph_config = config.get("glyphs")
    if not isinstance(glyph_config, dict):
        raise SystemExit("Configuration error: 'glyphs' must be a mapping")

    glyph_directory = glyph_config.get("directory")
    if not isinstance(glyph_directory, str):
        raise SystemExit(
            "Configuration error: 'glyphs.directory' must be a string"
        )

    alphabet = config.get("alphabet")
    if not isinstance(alphabet, dict):
        raise SystemExit("Configuration error: 'alphabet' must be a mapping")

    if not alphabet:
        raise SystemExit("Configuration error: 'alphabet' cannot be empty")

    if font_config["units_per_em"] <= 0:
        raise SystemExit(
            "Configuration error: 'font.units_per_em' must be positive"
        )

    if font_config["default_advance_width"] <= 0:
        raise SystemExit(
            "Configuration error: 'font.default_advance_width' must be positive"
        )

    for character, filename in alphabet.items():
        if not isinstance(character, str) or len(character) != 1:
            raise SystemExit(
                f"Configuration error: invalid alphabet character: {character!r}"
            )

        if not isinstance(filename, str):
            raise SystemExit(
                f"Configuration error: glyph filename for "
                f"{character!r} must be a string"
            )

        glyph_path = Path(glyph_directory) / filename

        if not glyph_path.is_file():
            raise SystemExit(
                f"Configuration error: glyph file not found: {glyph_path}"
            )


if __name__ == "__main__":
    main()