import argparse

from docitesort.utils import get_references, get_citations, get_citations_shine, sort_citations

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, required=True)
args = parser.parse_args()

citations = get_citations(args.file)
citation_shine = get_citations_shine(citations)
citations_sorted = sort_citations(citations, citation_shine)


references = get_references(args.file)
references_sorted = [None] * len(citation_shine)
for dst, src in enumerate(citation_shine):
    references_sorted[dst] = references[src - 1]

print("Before")
print(citations)
for par in references:
    print(par.text)
print("After")
print(citations_sorted)
for par in references_sorted:
    print(par.text)
