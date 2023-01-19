import sys
import pathlib

ROOT_PATH = "Path/to/the/cloned/repo"
DATA_PATH = "Path/to/dir/which/containg/data/folder"


def get_repo_path():
    return pathlib.Path(REPO_PATH)

def get_data_path():
    return pathlib.Path(DATA_PATH)
