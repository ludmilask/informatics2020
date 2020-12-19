import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", required=True, type=str)
parser.add_argument("--surname", required=True, type=str)
parser.add_argument("--middle_name", default=None, type=str)
parser.add_argument("--age", required=True, type=int)
parser.add_argument("--sex", required=True, choices=['F', 'M'])
parser.add_argument("--married", default=False, action='store_true')
parser.add_argument("--hobbies", default=None, nargs='*')

with open("journal.txt", "a") as output_f:
    output_f.write(json.dumps(vars(parser.parse_args())))
