import subprocess
from os.path import isfile, join, isdir, dirname

import os

from find_units import find_units
from merge import merge_pages, get_scanned_pages, get_scan_number
from make_pdf import make_pdf
from merge_pdf import merge_pdfs, get_unit_number

if __name__ == "__main__":

    # Map directories to binder names
    binder_to_units = {}

    # Make pdfs for each unit
    for unit in find_units("."):
        merge_pages(
            join(unit, "Front pages"),
            join(unit, "Back pages"),
            join(unit, "Merged pages"),
        )

        make_pdf(join(unit, "Merged pages"), join(unit, "booklet.pdf"))

        binder_dir_path = dirname(unit)
        if binder_dir_path not in binder_to_units:
            binder_to_units[binder_dir_path] = []
        binder_to_units[binder_dir_path].append(unit)

    # Merge pdfs of all units per binder to one pdf
    for binder in binder_to_units:
        units = binder_to_units[binder]
        units = sorted(units, key=get_unit_number)

        unit_booklets = [join(unit, "Booklet.pdf") for unit in units]

        merge_pdfs(unit_booklets, join(binder, "Scanned Binder.pdf"))

        # Delete the unit booklets
        for unit_booklet in unit_booklets:
            os.remove(unit_booklet)




    

