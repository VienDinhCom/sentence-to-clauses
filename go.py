from nltk.parse import CoreNLPParser
from nltk import Tree

parser = CoreNLPParser(url='http://localhost:9000')

s = 'That is, wanting the past to be more than what it was (different, better, still here, etc.) or wanting the future to unfold exactly as you expect (with hardly a thought as to how that might affect other people).'

t = list(parser.raw_parse(s))



subtexts = []

for subtree in t[0].subtrees():
    if subtree.label()=="SBAR":
        subtexts.append(' '.join(subtree.leaves()))


print(' '.join(t[0].leaves()))

print('\n')

for i in range(len(subtexts)):
    print(subtexts[i])

# If I have to love someone,
# I have to love the one
# who loves me 
# like I love her.