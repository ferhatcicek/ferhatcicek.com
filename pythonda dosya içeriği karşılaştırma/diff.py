import difflib
from pathlib import Path

first_file_lines = Path('fileA.txt').read_text().splitlines()
second_file_lines = Path('fileB.txt').read_text().splitlines()

html_out = difflib.HtmlDiff().make_file(first_file_lines, second_file_lines)
Path('diff_output.html').write_text(html_out)
