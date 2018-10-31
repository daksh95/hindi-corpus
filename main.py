import hindicorpus as hc
import os

print("\n\nPrint all text available: ")
print(hc.raw())

print("\n\nPrint all fileids: ")
print(hc.fileids())

print("\n\nPrint all word tokens: ")
print(hc.tokenize())

print("\n\nPrint all sentence tokens: ")
print(hc.sent_tokenize())

print("\n\nPrint all text in a particular file: ")
print(hc.raw("Technology/Artificial Intelligence.txt"))

print("\n\nPrint all word tokens without stopwords in a particular file: ")
print(hc.tokenize("Technology/Artificial Intelligence.txt", True))

print("\n\nPrint all word tokens with stopwords in a particular file: ")
print(hc.tokenize("Technology/Artificial Intelligence.txt", False))

print("\n\nPrint all sentence tokens in a particular file: ")
print(hc.sent_tokenize("Technology/Artificial Intelligence.txt"))

print("\n\nSearch for files with keyword: ")
print(hc.fileids_search("मशीनों"))