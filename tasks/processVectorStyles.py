#!/usr/bin/env python

from optparse import OptionParser
import os
import sys
import json
import shutil

prog = os.path.basename(__file__)
base_dir = os.path.join(os.path.dirname(__file__), "..")
version = "3.0.0"
help_description = """\
Converts colormaps to JSON files
"""

parser = OptionParser(usage="Usage: %s <config_file> <vector_styles_input_dir> <output_dir>" % prog,
                      version="%s version %s" % (prog, version),
                      epilog=help_description)

(options, args) = parser.parse_args()
if len(args) != 3:
    parser.error("Invalid number of arguments")

config_file = args[0]
vector_styles_input_dir = args[1]
output_dir = args[2]

with open(config_file) as fp:
    config = json.load(fp)
skips = config.get("skipPalettes", [])

def copy_file(file):
    input_file = os.path.join(root, file)
    id = os.path.splitext(os.path.basename(input_file))[0]
    if id in skips:
        sys.stderr.write("%s:  WARN: [%s] %s\n" % (prog, input_file,
                "Skipping"))
        return

    if input_file.endswith('.json'):
        shutil.copy(input_file, output_dir)

# Main
file_count = 0
error_count = 0

for root, dirs, files in os.walk(vector_styles_input_dir):
    for file in files:
        try:
            file_count += 1
            copy_file(file)
        except Exception as e:
            sys.stderr.write("%s: ERROR: [%s] %s\n" % (prog, file, str(e)))
            error_count += 1

print "%s: %d error(s), %d file(s)" % (prog, error_count, file_count)

if error_count > 0:
    sys.exit(1)
