import argparse
parser = argparse.ArgumentParser()
# Positional arguments -- user provides list of files to concatenate
parser.add_argument('files', nargs='*')
# Flags
parser.add_argument("-b", "--number-nonblank", help="number nonempty output lines", action="store_true")
parser.add_argument("-n", "--number", help="number all output lines", action="store_true")
parser.add_argument("-E", "--show-ends", help="display $ at end of each line", action="store_true")
parser.add_argument("-T", "--show-tabs", help="display TAB characters as →", action="store_true")
parser.add_argument("-S", "--show-spaces", help="display space characters as ·", action="store_true")

args = parser.parse_args()

output = []

for item in args.files:
    try:
        file = open(item)
    except FileNotFoundError:
        raise FileNotFoundError
    output.append(file.readline())

# Optional behaviors

# -b, --number-nonblank
if args.number_nonblank:
    line_num = 1
    for i, line in enumerate(output):
        output[i] = str(line_num) + " " + output[i]
        line_num += 1
# -n, --number
elif args.number:
    line_num = 1
    for i, line in enumerate(output):
        if output[i] != "":
            output[i] = str(line_num) + " " + output[i]
            line_num += 1

# -E, --show-ends
if args.show_ends:
    for i, line in enumerate(output):
        output[i] = output[i][:-1] + "$" + output[i][-1:]
        line_num += 1

# -T, --show-tabs
if args.show_tabs:
    for i, line in enumerate(output):
        output[i] = output[i].replace("\t", "→")

# -S, --show-spaces
if args.show_spaces:
    for i, line in enumerate(output):
        output[i] = output[i].replace(" ", "·")

output = "".join(output)
print(output)
