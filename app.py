import os
import json
from nltk import Tree
from flask import Flask
from flask import request
from nltk.parse import CoreNLPParser

app = Flask(__name__)

CORENLP_URL = os.getenv('CORENLP_URL')

parser = CoreNLPParser(url=CORENLP_URL)

@app.route('/', methods = ['POST'])
def extractByLabel(): 
  text = request.form['text']
  label = request.form['label']

  tree = list(parser.raw_parse(text))
  subtexts = []

  for subtree in tree[0].subtrees():
    if subtree.label()==label:
      subtexts.append(' '.join(subtree.leaves()))

  return json.dumps({
    "subtexts": subtexts,
    "fulltext": ' '.join(tree[0].leaves())
  })


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')