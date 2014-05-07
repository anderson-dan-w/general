#!/usr/bin/python3

from collections import defaultdict, Counter
import re
from xml.sax.saxutils import unescape

DATA_DIR = "/home/dwanderson/EN746_ML/proj_data/"
CS_POSTS = DATA_DIR + "cs_data/Posts.xml"
LING_POSTS = DATA_DIR + "lang_data/Posts.xml"

entities = {"&#xA;":" ", "&quot;":" "}
def read_in(fname):
    questions = []
    with open(fname) as fh:
        lines = str(fh.read()).split("\n")
    for line in lines:
        match = re.search('PostTypeId="1".*?Body="(.*?)"', line)
        if match is not None:
            text = unescape(match.group(1), entities).upper()
            text, _ = re.subn("<.*?>", " ", text)
            text, _ = re.subn("[^A-Z]", " ", text)
            text, _ = re.subn(" +", " ", text)
            text, _ = re.subn("^ | $", "", text)
            questions.append(text)
    return questions

def unigram_counts(lines):
    counter = Counter()
    for line in lines:
        counter.update(line.split(" "))
    return counter

def bigram_counts(lines):
    counter = Counter()
    for line in lines:
        words = line.split(" ")
        counter.update(" ".join(words[i:i+2]) for i in range(len(words) - 1))
    return counter

print("Getting linguistic unigram and bigram counts")
_lt = read_in(LING_POSTS)
LU = unigram_counts(_lt)
LB = bigram_counts(_lt)

print("Getting comp sci unigram and bigram counts")
_ct = read_in(CS_POSTS)
CU = unigram_counts(_ct)
CB = bigram_counts(_ct)

LU_top100 = [w[0] for w in LU.most_common(100)]
LB_top100 = [w[0] for w in LB.most_common(100)]
CU_top100 = [w[0] for w in CU.most_common(100)]
CB_top100 = [w[0] for w in CB.most_common(100)]

inter_lu_cu = set(LU_top100).intersection(CU_top100)
inter_lb_cb = set(LB_top100).intersection(CB_top100)

lu_not_cu = set(LU_top100).difference(CU_top100)
cu_not_lu = set(CU_top100).difference(LU_top100)
lb_not_cb = set(LB_top100).difference(CB_top100)
cb_not_lb = set(CB_top100).difference(LB_top100)
