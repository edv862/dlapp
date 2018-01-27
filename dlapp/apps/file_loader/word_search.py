# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 10:32:14 2018

@author: divey
"""
import docx2txt
import string
import re
import math

from .reader import pdf_2_string
from collections import Counter
from nltk import pos_tag, tokenize


WORD = re.compile(r'\w+')


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x]**2 for x in vec1.keys()])
    sum2 = sum([vec2[x]**2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


# Get text from docx file
def docx_2_string(filename):
    text = docx2txt.process(filename)
    return text


# Get text from txt file
def txt_2_string(filename):
    text = filename.read()
    return text.decode('utf-8')


def word_search(searchText, filename):
    ln1 = tokenize.sent_tokenize(searchText)

    extension = filename.name.split('.')[-1]
    if extension == 'docx':
        file = docx_2_string(filename)
    elif extension == 'txt':
        file = txt_2_string(filename)
    else:
        file = pdf_2_string(filename)

    ln2 = tokenize.sent_tokenize(file)

    #cosine similarity of two docs
    cou = 0
    maxi = []
    mn_c_cosine = []
    mn_c_x = []
    mn_c_i = []

    for x in range(0, len(ln1)):
        text1 = ln1[x]
        vector1 = text_to_vector(text1)
        #print  "text1;", text1

        for i in range(0, len(ln2)):
            text2 = ln2[i]
            vector2 = text_to_vector(text2)
            cosine1 = get_cosine(vector1, vector2)

            mn_c_cosine.append(cosine1)
            mn_c_x.append(x)
            mn_c_i.append(i)


    count = 0
    maximum11 = None
    maximum11a = []
    b = len(ln2)
    mn_ref = 0
    mn_ca = []
    text1 = []
    text2 = []

    for k in range(0, len(ln1)):
        for j in range(0, len(ln2)):
            # print "mn_cosine:", mn_c_cosine[(j+count)]
            mn_ca.append(mn_c_cosine[(j + count)])
        maximum11 = max(mn_ca)
        # print maximum11
        count = count + len(ln2)
        mn_ca = [0]
        maximum11a.append(maximum11)
        # print "maximum11a:", maximum11a

    count = 0
    for k in range(0, len(ln1)):
        for j in range(0, len(ln2)):
            if (mn_c_cosine[(j + count)] == maximum11a[k]):
                # print "text1:", ln1[k]
                text1.append(ln1[k])
                # print "text2:", ln2[j]
                text2.append(ln2[j])
                # print "_____"
        count = count + len(ln2)

    return text2[0]


# To test in python.
if __name__ == '__main__':
    raw_text1 = "right in line at"
    raw_text2 = "if consensus"

    filename1 = "set1.txt"
    filename2 = "set2.txt"

    print(word_search(raw_text1, filename1))
    print("-----------------")
    print(word_search(raw_text2, filename1))

    print("##################")

    print(word_search("subscriber", filename2))
    print("-----------------")
    print(word_search("4Q guidance", filename2))
    print("-----------------")
    print(word_search("cash spend", filename2))
