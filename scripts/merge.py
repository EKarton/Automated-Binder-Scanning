from os import listdir
from os.path import isfile, join, isdir

from shutil import copyfile

import re

SCANNED_FILE_PATTERN = re.compile("^Scan \\d+\\.jpeg$")


def get_scanned_pages(dir_, file_ext=".jpeg"):
    filenames = [
        f for f in listdir(dir_) if f.endswith(file_ext) and isfile(join(dir_, f))
    ]
    return filenames


def get_scan_number(filename):
    return int(filename.split(".")[0].split(" ")[1])


def merge_pages(frontpage_dir, backpage_dir, merged_dir):

    # Check if dirs exists
    assert isdir(frontpage_dir)
    assert isdir(backpage_dir)
    assert isdir(merged_dir)

    # Grab all the frontpage and backpage filenames
    frontpage_files = get_scanned_pages(frontpage_dir)
    backpage_files = get_scanned_pages(backpage_dir)

    # Check if the number of pages in frontpage_dir and backpage_dir is the same
    assert len(frontpage_files) == len(backpage_files)

    # Check if all files has a number
    for frontpage_file in frontpage_files:
        assert SCANNED_FILE_PATTERN.match(frontpage_file)

    for backpage_file in backpage_files:
        assert SCANNED_FILE_PATTERN.match(backpage_file)

    # Sort them
    frontpage_files = sorted(frontpage_files, key=get_scan_number)
    backpage_files = sorted(backpage_files, key=get_scan_number)

    # Increment front page file names by x2
    for frontpage_filename in frontpage_files:

        new_frontpage_filename = (
            "Scan " + str(get_scan_number(frontpage_filename) * 2) + ".jpeg"
        )

        old_filepath = join(frontpage_dir, frontpage_filename)
        new_filepath = join(merged_dir, new_frontpage_filename)

        print(old_filepath, "->", new_filepath)

        if isfile(new_filepath):
            raise ValueError("Merged File", new_filepath, "already exists!")

        copyfile(old_filepath, new_filepath)

    # Increment backpage file names by num_files - (i x 2 + 1)
    for backpage_filename in backpage_files:

        new_backpage_num = (
            2 * (len(backpage_files) - get_scan_number(backpage_filename)) - 1
        )

        new_backpage_filename = "Scan " + str(new_backpage_num) + ".jpeg"

        old_filepath = join(backpage_dir, backpage_filename)
        new_filepath = join(merged_dir, new_backpage_filename)

        print(old_filepath, "->", new_filepath)

        if isfile(new_filepath):
            raise ValueError("Merged File", new_filepath, "already exists!")

        copyfile(old_filepath, new_filepath)

    # Check that each file is named from 0 to 2 * len(backpage_files) - 1
    merged_files = get_scanned_pages(merged_dir)

    print(merged_files)

    not_found_indexes = set([i for i in range(0, 2 * len(backpage_files))])

    for filename in merged_files:
        not_found_indexes.remove(get_scan_number(filename))

    assert len(not_found_indexes) == 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "front_pages_directory",
        type=str,
        help="The directory with the front pages of scanned images",
    )
    parser.add_argument(
        "back_pages_directory",
        type=str,
        help="The directory with the back pages of scanned images",
    )
    parser.add_argument(
        "merged_pages_directory",
        type=str,
        help="The directory with the merged pages of scanned images",
    )
    opts = parser.parse_args(sys.argv[1:])

    merge_pages(
        opts.front_pages_directory,
        opts.back_pages_directory,
        opts.merged_pages_directory,
    )

