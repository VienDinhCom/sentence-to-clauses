from nltk import Tree
import requests
import json

string = 'The soul should have someone it can respect, by whose example it can make its inner sanctum more inviolable.'

parse_str = requests.post('http://corenlp.run/?properties={"annotators":"parse"}', data = {'data': string}).json()['sentences'][0]['parse']


t = Tree.fromstring(parse_str)

subtexts = []
for subtree in t.subtrees():
    if subtree.label()=="SBAR":

        print(subtree.leaves())

        #print subtree.leaves()
        subtexts.append(' '.join(subtree.leaves()))
print(subtexts)

presubtexts = subtexts[:]       # ADDED IN EDIT for leftover check

for i in reversed(range(len(subtexts)-1)):
    subtexts[i] = subtexts[i][0:subtexts[i].index(subtexts[i+1])]

for text in subtexts:
    print(text)

# ADDED IN EDIT - Not sure for generalized cases
leftover = presubtexts[0][presubtexts[0].index(presubtexts[1])+len(presubtexts[1]):]
print(leftover)