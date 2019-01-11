"""Fixes the pdf page skews which only the best scanners produce!"""
from PyPDF2 import PdfFileReader, PdfFileWriter
import math


SKEW_DEGREES = -1
END_TAG = "_fixed"
TEST_PDF = "./data/scan.pdf"


def clone_pdf_without_skew(filename: str, *,
                           end_tag: str = END_TAG,
                           skew_degrees: float = SKEW_DEGREES) -> None:
    """Modifies each page in a pdf with a rotation and saves it to a new file!"""
    def fix_page_skew(page) -> None:
        """Modifies the page with a rotation!"""
        page.addTransformation(get_rotation_matrix(skew_degrees))

    with open(filename, 'rb') as full_pdf:
        reader = PdfFileReader(full_pdf, strict=False)
        writer = PdfFileWriter()
        writer.appendPagesFromReader(reader, after_page_append=fix_page_skew)
        out_location = f"{filename[:-4]}{end_tag}.pdf"
        with open(out_location, 'wb') as outfile:
            writer.write(outfile)


def get_rotation_matrix(rotation: float) -> list:
    """Returns the transformation matrix for the given rotation!"""
    rotation = -math.radians(rotation)
    return [math.cos(rotation), math.sin(rotation), -math.sin(rotation), math.cos(rotation), 0, 0]


def _test_scan_correction() -> None:
    """Tests the core program!"""
    clone_pdf_without_skew(TEST_PDF)


def main() -> None:
    """Runs the core program!"""
    _test_scan_correction()


if __name__ == "__main__":
    main()
