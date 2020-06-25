import subprocess
from os.path import isfile, join, isdir

from find_units import find_units
from merge import merge_pages
from make_pdf import make_pdf
from merge_pdfs import merge_pdfs

if __name__ == "__main__":
    for unit in find_units("."):
        merge_pages(join(unit, "Front pages"), join(unit, "Back pages"), join(unit, "Merged pages"))
        make_pdf(join(unit, "Merged pages"), join(unit, "booklet.pdf"))

