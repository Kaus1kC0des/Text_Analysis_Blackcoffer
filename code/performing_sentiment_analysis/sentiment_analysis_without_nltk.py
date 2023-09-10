import nltk
from textblob import TextBlob
import pandas
import csv
import numpy
import glob
import os
import time

start = time.time()

positive_file = "/Users/kausik/Documents/Project BlackCoffer/MasterDictionary/positive-words.txt"
negative_file = "/Users/kausik/Documents/Project BlackCoffer/MasterDictionary/negative-words.txt"

positive_words = []
negative_words = []

total_positive = 0
total_negative = 0
total_words = 0


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
directory_path = "/Users/kausik/Documents/Project BlackCoffer/clean_files"
for filename in os.listdir(directory_path):
    if filename.endswith(".txt"):  # Process only text files
        file_path = os.path.join(directory_path, filename)

        try:
            with open(file_path, 'r') as file:
                words = file.read().split()
                total_words += len(words)
                total_positive += len([word for word in words if word.lower() in positive_words])
                total_negative += len([word for word in words if word.lower() in negative_words])
        except Exception as e:
            print(f"Error reading file '{filename}': {e}")
total_neutral = total_words - total_positive - total_negative
print(f"The total positive count is {total_positive}")
print(f"The total negative count is {total_negative}")
print(f"The total neutral word count is {total_neutral}")
print(f"The total word count is {total_words}")

print(f"Positive percentage = {(total_positive/(total_words-total_neutral))*100}%")
print(f"Negative percentage = {(total_negative/(total_words-total_neutral))*100}%")

print(f"Total time taken is {time.time()-start}")