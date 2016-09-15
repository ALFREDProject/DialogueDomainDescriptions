from argparse import ArgumentParser
import codecs
import os
import re


DDD_NAME_PATTERN = r"^\s*\#(?P<ddd_name>.*)$"

def parse_args():
    parser = ArgumentParser(description="Split the global interactiontests per DDD and generate a new test file for each. Indicate DDD-specific tests with a line such as: '# ddd_name'")
    parser.add_argument("files", metavar="file", help="the location of the interaction test file", nargs="+")
    parser.add_argument("--output-directory", "-o", help="the location of the split files", default=".")
    return parser.parse_args()

def main():
    args = parse_args()
    files = args.files
    for file_ in files:
        split_file(file_, args.output_directory)

def split_file(path, output_directory):
    lines = []
    current_ddd = ""
    with codecs.open(path, 'r', encoding="utf-8") as f:
        for line in f:
            if not is_line_indicating_ddd(line):
                lines.append(line)
                continue
            elif not current_ddd:
                lines = []
                current_ddd = ddd_name_of_line(line)
                continue

            write_to_ddd_file_in_directory(lines, path, current_ddd, output_directory)
            lines = []
            current_ddd = ddd_name_of_line(line)

        if lines and current_ddd:
            write_to_ddd_file_in_directory(lines, path, current_ddd, output_directory)

def write_to_ddd_file_in_directory(lines, original_file, ddd, output_directory):
    original_file_name = os.path.basename(original_file)
    new_file_name = path_of_new_ddd_specific_test_file(original_file_name, ddd)
    new_file_path = os.path.join(output_directory, new_file_name)
    write_lines_to_new_file(new_file_path, lines)

def path_of_new_ddd_specific_test_file(original_file_name, ddd_name):
    new_file_name = "%s_%s" % (ddd_name, original_file_name)
    return new_file_name

def write_lines_to_new_file(name, lines):
    directory = os.path.dirname(name)
    if not os.path.exists(directory):
        os.makedirs(directory)
    with codecs.open(name, 'w', encoding="utf-8") as f:
        for line in lines:
            f.write(line)

def is_line_indicating_ddd(line):
    return _ddd_name_regexp_match(line) is not None

def ddd_name_of_line(line):
    match = _ddd_name_regexp_match(line)
    unformatted_name = match.group("ddd_name")
    name = re.sub("\W", "", unformatted_name)
    return name

def _ddd_name_regexp_match(string):
    return re.match(DDD_NAME_PATTERN, string)

if __name__ == "__main__":
    main()