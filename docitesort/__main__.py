import argparse

from docitesort.utils import get_references, get_citations

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, required=True)
args = parser.parse_args()

citations = get_citations(args.file)
print(citations)
references = get_references(args.file)

for par in references:
    print(par.text)
