import argparse
import os
from pathlib import Path

from generate_ros_meta_snapcraft_file import main as gen


def is_dir(path: str) -> Path:
    if os.path.exists(path) and os.path.isdir(path):
        return Path(path)
    raise OSError(f"{path} is not a directory!")

def main(args=None):
    parser = argparse.ArgumentParser(
        description="Generate a snapcraft.yaml file for all ROS foundational snap."
    )
    parser.add_argument(
        "-p",
        "--path",
        type=is_dir,
        required=False,
        help="Output path for generated files.",
    )
    parser.add_argument(
        "-s",
        "--snap",
        help="Run snapcraft for the generated files.",
        action="store_true"
    )

    parsed_args = parser.parse_args(args=args)

    if not parsed_args.path:
        parsed_args.path = Path("snaps")
        os.makedirs(parsed_args.path, exist_ok=True)


    matrix={
        "noetic": ["ros-core", "ros-base", "robot", "desktop"],
        "foxy": ["ros-core", "ros-base", "desktop"],
        "humble": ["ros-core", "ros-base", "desktop"],
    }

    for rosdistro, variants in matrix.items():
        for variant in variants:

            folders = [
                parsed_args.path / f'{rosdistro}_{variant.replace("-", "_")}',
                parsed_args.path / f'{rosdistro}_{variant.replace("-", "_")}_dev'
            ]

            for folder in folders:

                os.makedirs(folder, exist_ok=True)

                gen_args = ["-r", rosdistro, "-v", variant, "-p", str(folder), "-q"]
                if "dev" in folder.stem:
                    gen_args.append("-d")
                if parsed_args.snap:
                    gen_args.append("-s")

                gen(gen_args)


if __name__ == "__main__":
    main()

