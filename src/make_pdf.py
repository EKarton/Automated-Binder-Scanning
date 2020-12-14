from os.path import isfile, join, isdir

import os, sys

import argparse

import img2pdf

from merge import get_scanned_pages, get_scan_number


def make_pdf(image_dir, output_filepath):

    # Verify that the directory exists
    assert isdir(image_dir)

    # Get a sorted list of the images
    images = get_scanned_pages(image_dir)
    images = sorted(images, key=get_scan_number)

    # Attach the file directory to each image
    images = list(map(lambda image: join(image_dir, image), images))

    # Merge all the images into a single PDF file
    with open(output_filepath, "wb") as output_file:
        output_file.write(img2pdf.convert(images))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=str, help="The directory with scanned images")
    parser.add_argument(
        "output_file", type=str, help="The output filepath for the PDF file"
    )
    opts = parser.parse_args(sys.argv[1:])

    make_pdf(opts.directory, opts.output_file)
