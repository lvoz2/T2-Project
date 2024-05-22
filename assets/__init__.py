"""
    Author:     H Foxwell
    Date:       14/May/2024
    Purpose:
        To dynamically load all assets into a single dictionary so
        that they can be used in the program without causing path
        errors.
"""
from pathlib import Path
from pygame import Surface, image, Rect

# Global Variables
GAME_ASSETS: dict[str, dict[str, Surface | int | Rect]] = {}


def __iterate_files(directory: Path, image_types: tuple):
    """
        Iterates over files in a directory adding them 
        to the game assets. Recursively calls itself when
        a sub-directory is found

    Args:
        directory (Path): Path to sub-directory
        image_types (tuple): tuple of valid image file types
    """
    for item in Path.iterdir(directory):
        if item.is_file and item.suffix in image_types:
            asset = image.load(item)
            GAME_ASSETS[item.stem]["image"] = asset
            GAME_ASSETS[item.stem]["height"] = asset.get_height()
            GAME_ASSETS[item.stem]["width"] = asset.get_width()
            GAME_ASSETS[item.stem]["rect"] = asset.get_rect()

        # if a sub-folder is found
        elif item.is_dir():
            __iterate_files(item, image_types)


def load_assets():
    """
    Searches the local directory for assets
    using current working directory.
    """
    # Constants
    cwd: Path = Path.cwd()
    assets_folder = Path.joinpath(cwd, "assets")
    image_types = (".jpg", ".png")

    # Verify assets folder exists
    if not assets_folder.exists():
        raise FileNotFoundError(f"Assets directory not found: {assets_folder}")

    # Iterate over files in the directory adding    \
    #   each image to the dictionary. Images will  \
    #   be added by the file name, sans the suffix
    __iterate_files(assets_folder, image_types)
