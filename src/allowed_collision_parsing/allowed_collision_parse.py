import argparse
import re

def parse_allowed_collisions(file):
    '''
    Method to parse an input srdf file and output the allowed collisions in the file in TMKit expected format.
    :param file: the srdf file to parse
    :return: The parsed string
    '''

    parsed_str = ''
    with open(file, 'r') as read_file:
        for line in read_file:
            if 'disable_collisions' in line:
                link1 = re.search('link1=(\S+)', line).group(1)
                link2 = re.search('link2=(\S+)', line).group(1)
                parsed_str += 'allow_collision ' + link1 + ' ' + link2 + ';\n'

    return parsed_str


parser = argparse.ArgumentParser(description='Parse an srdf file to extract allowed collisions in the format required by TMKit')
parser.add_argument('file', type=str, help='the srdf file to be parsed')

args = parser.parse_args()

if args.file:
    print(parse_allowed_collisions(args.file))
else:
    print("No file provided")
