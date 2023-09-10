import nltk
from textblob import TextBlob
import pandas
import csv
import numpy
import glob

positive_file = "/Users/kausik/Documents/Project BlackCoffer/MasterDictionary/positive-words.txt"
negative_file = "/Users/kausik/Documents/Project BlackCoffer/MasterDictionary/negative-words.txt"

positive_words = []
negative_words = []

try:
    with open(positive_file, 'r', encoding='utf-8') as file:
        positive_words.extend(file.read().splitlines())
except UnicodeDecodeError:
    try:
        with open(positive_file, 'r', encoding='latin-1') as file:
            positive_words.extend(file.read().splitlines())
    except Exception as e:
        print(f"Error reading positive words: {e}")

try:
    with open(negative_file, 'r', encoding='utf-8') as file:
        negative_words.extend(file.read().splitlines())
except UnicodeDecodeError:
    try:
        with open(negative_file, 'r', encoding='latin-1') as file:
            negative_words.extend(file.read().splitlines())
    except Exception as e:
        print(f"Error reading negative words: {e}")

print("Positive Words read from the file:")
print(positive_words)

print("Negative Words read from the file:")
print(negative_words)