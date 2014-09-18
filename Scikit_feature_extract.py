#! /usr/bin/env python

from __future__ import division
import re
import random
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.cluster.util import cosine_distance
from operator import itemgetter

def preprocess(fnin, fnout):
  fin = open(fnin, 'rb')
  fout = open(fnout, 'wb')
  buf = []
  id = ""
  category = ""
  for line in fin:
    line = line.strip()

    if line.find("-- Document Separator --") > -1:
      if len(buf) > 0:
        # write out body,
        body = re.sub("\s+", " ", " ".join(buf))
        fout.write("%s\t%s\t%s\n" % (id, category, body))
      # process next header and init buf
      id, category, rest = map(lambda x: x.strip(), line.split(": "))
      buf = []
    else:
      # process body
      buf.append(line)
  fin.close()
  fout.close()

def train(fnin):
  docs = []
  cats = []
  fin = open(fnin, 'rb')
  for line in fin:
    id, category, body = line.strip().split("\t")
    docs.append(body)
    cats.append(category)
  fin.close()
  v=CountVectorizer(min_df=1,stop_words="english")
  pipeline = Pipeline([
    ("vect", v),
    ("tfidf", TfidfTransformer(use_idf=False))])
  tdMatrix = pipeline.fit_transform(docs, cats)
  return tdMatrix, cats


def main():
  preprocess("corpus.txt", "sccpp.txt")
  tdMatrix, cats = train("sccpp.txt")

if __name__ == "__main__":
  main()