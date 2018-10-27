import pandas as pd
import os
import io
from HindiTokenizer import Tokenizer

dir_path = os.path.dirname(os.path.realpath(__file__))

corpusdir = './data/' # Directory of corpus.

def raw():
    for _, dirs, _ in os.walk(corpusdir):
        for dir in dirs:
            for _, _, files in os.walk(corpusdir + dir):
                for file in files:
                    file_text = io.open(corpusdir + dir + "/" + file, "r", encoding="utf-8")
                    print(file_text.read())

def read(dir):
    for _, _, files in os.walk(corpusdir + dir):
        for file in files:
            file_text = io.open(corpusdir + dir + "/" + file, "r", encoding="utf-8")
            print(file_text.read())

def topics(dir):
    for _, _, files in os.walk(corpusdir + dir):
        print(files)

def fileids():
    files_ret = []
    for dir in os.listdir(corpusdir):
        try:
            files = os.listdir(corpusdir + dir + "/")
            for file in files:
                files_ret.append(dir + "/" + file)
        except:
            print("")

    return files_ret




