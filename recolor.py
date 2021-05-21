
import subprocess
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("out", help="file where to output the .png files", type=str)
parser.add_argument("colors", help="array of colors", nargs="+", type=str)

args = parser.parse_args()

print(args.colors)

for c in args.colors:
    subprocess.call(["bash", "recolor.sh", args.out, c])
 

