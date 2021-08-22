from PyPDF2 import PdfFileMerger, PdfFileReader
from os.path import join, basename

from find_units import find_units


def get_unit_number(unit_dir_path):
    split_name = basename(unit_dir_path).split(" ")

    if len(split_name) is 1:
        return 0

    return int(split_name[1])


def merge_pdfs(pdf_filepaths, output_pdf):
    mergedObject = PdfFileMerger()

    for filepath in pdf_filepaths:
        mergedObject.append(PdfFileReader(filepath, "rb"))

    mergedObject.write(output_pdf)


if __name__ == "__main__":
    course = "GGR 272"
    units = find_units(course)
    units = sorted(units, key=get_unit_number)

    unit_booklets = [join(unit, "Booklet.pdf") for unit in units]

    merge_pdfs(unit_booklets, course + " Scanned Notes.pdf")
