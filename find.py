import argparse

parser = argparse.ArgumentParser()

# Positional arguments
parser.add_argument("args", nargs="1")

# Flags
parser.add_argument("-x", help="Test flag 1", action="store_true")
parser.add_argument("-y", help="Test flag 2", action="store_true")
parser.add_argument("-z", help="Test flag 3", action="store_true")

# Options
parser.add_argument("-name")
parser.add_argument("-b")
parser.add_argument("-c")


args = parser.parse_args()

output = []
