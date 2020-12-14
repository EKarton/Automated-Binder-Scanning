import subprocess
import argparse
from os.path import isfile, join, isdir, dirname

import os
from os import mkdir

from find_units import has_front_pages_dir, has_back_pages_dir
from merge import merge_pages, get_scanned_pages, get_scan_number
from make_pdf import make_pdf
from merge_pdf import merge_pdfs, get_unit_number

def get_path():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "path",
        metavar="P",
        type=str,
        default=".",
        help="The path containing the front and Back pages directories",
    )
    args = parser.parse_args()

    return args.path


if __name__ == "__main__":
    cur_path = get_path()

    if not has_front_pages_dir(cur_path):
        raise Exception("Cannot find 'Front pages' directory")

    if not has_back_pages_dir(cur_path):
        raise Exception("Cannot find 'Back pages' directory")


    if not isdir(join(cur_path, "Merged pages")):
        mkdir(join(cur_path, "Merged pages"))

    merge_pages(
        join(cur_path, "Front pages"),
        join(cur_path, "Back pages"),
        join(cur_path, "Merged pages"),
    )

    make_pdf(join(cur_path, "Merged pages"), join(cur_path, "Booklet.pdf"))