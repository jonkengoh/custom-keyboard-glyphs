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


if __name__ == "__main__":
    main()