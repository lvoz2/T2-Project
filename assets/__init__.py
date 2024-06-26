"""
    Author:     H Foxwell
    Date:       14/May/2024
    Purpose:
        To dynamically load all assets into a single dictionary so
        that they can be used in the program without causing path
        errors.
"""
from pathlib import Path
from pygame import Surface, image
from typing import *


def __iterate_files(directory: Path, image_types: list[str]) -> Any:
    """
        Iterates over files in a directory adding them 
        to the game assets. Recursively calls itself when
        a sub-directory is found

    Args:
        directory (Path): Path to sub-directory
        image_types (list of strings): tuple of valid image file types
    """
    assets: Any = {} # I'm not giving this an explicit type hint because it will end up being an n-dimensional dict, where n could be any number
    for item in Path.iterdir(directory):
        if item.is_file() and item.suffix in image_types:
            assets[item.stem] = image.load(item)

        # if a sub-folder is found
        elif item.is_dir():
            assets[item.name] = __iterate_files(item, image_types)
    return assets


def load_assets() -> Any:
    """
    Searches the local directory for assets
    using current working directory.
    """
    # Constants
    cwd: Path = Path.cwd()
    assets_folder: Path = Path.joinpath(cwd, "assets")
    image_types: list[str] = [".jpg", ".png"]

    # Verify assets folder exists
    if not assets_folder.exists():
        raise FileNotFoundError(f"Assets directory not found: {assets_folder}")

    # Iterate over files in the directory adding    \
    #   each image to the dictionary. Images will  \
    #   be added by the file name, sans the suffix
    return __iterate_files(assets_folder, image_types)


GAME_ASSETS = load_assets()
