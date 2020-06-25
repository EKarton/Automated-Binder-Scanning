from os.path import isfile, join, isdir

import os, sys

import argparse


def list_subfolders(dir_path):
    return [f for f in os.scandir(dir_path) if f.is_dir()]


def has_subdir(dir_path, subfolder_name):
    for f in list_subfolders(dir_path):
        if f.name == subfolder_name:
            return True

    return False


def has_front_pages_dir(dir_path):
    return has_subdir(dir_path, "Front pages")


def has_back_pages_dir(dir_path):
    return has_subdir(dir_path, "Back pages")


def has_merged_pages_dir(dir_path):
    return has_subdir(dir_path, "Merged pages")


def find_units(cur_dir_path):
    if (
        has_front_pages_dir(cur_dir_path)
        and has_back_pages_dir(cur_dir_path)
        and has_merged_pages_dir(cur_dir_path)
    ):
        return [cur_dir_path]

    results = []
    for subfolder in list_subfolders(cur_dir_path):
        results += find_units(subfolder.path)

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "directory", type=str, help="The root directory to start searching for"
    )
    opts = parser.parse_args(sys.argv[1:])

    print(*find_units(opts.directory))
