import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--files', metavar = '', help = 'requires a filename as input')
args = parser.parse_args()

class svgCleanup:

    def __init__(self, filename):
        self.filename = filename

    def linkCorrection(self):

        pattern1 = re.compile(r'|')
        pattern2 = re.compile(r'')
        updated_file = ''

        print(f"Working on: {self.filename}", end = ' ')

        try:
            with open(self.filename, 'r+') as file:
                data = file.read()
                updated_file = re.sub(pattern1, r'./', data)
                updated_file = re.sub(pattern2, r'', updated_file)

            with open(self.filename, 'w+') as file:
                file.write(updated_file)

            print("Done")

        except Exception as e:
            print("FAILED:", e.args)

if args.files:
    svg = svgCleanup(args.files)
    svg.linkCorrection()
else:
    print("No argument and filename was given.")
