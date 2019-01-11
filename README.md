## VeryGoodScannerExtension

# Usage

function clone_pdf_without_skew(
    :param filename (str): the location & name of your pdf file
    :param end_tag (str): appended to the end of new pdf file
    :param skew_degrees (float): ¯\_(?)_/¯
) -> :return None: the modified file is saved, not returned

# Roadmap

DONE: Quickly put something together to rotate PDFs which "works."

TODO: Figure out what is wrong with the PDF lib rotation methods or documentation.

TODO: Auto-detect correct rotation from page minimum enclosing rectangle. [will introduce OpenCV dependency]

TODO: Command-line parser.

TODO: Executable distribution.
