"""
This file computes the average word length of the words in all the files and also the average length
of the sentences in the file as this is a part of the project requirement.
"""


import os
import time

start = time.time()

def find_avgs_of_file(file):
    total_word_count = 0
    total_word_length = 0
    total_sent_count = 0
    total_sent_length = 0

    with open(file,'r') as file:
        for line in file:
            if line:
                words = line.split()
                total_sent_count += 1
                total_sent_length += len(words)

            for word in words:
                word = word.strip(".,!'/[]()@#$%^&*-+=?{}|:;?/><")
                if word:
                    total_word_count += 1
                    total_word_length += len(word)

        return total_word_count,total_word_length,total_sent_count,total_sent_length

directory_path = "contents"
total_file = 0
total_word_len = 0
total_word_count = 0
total_sent_len = 0
total_sent_count = 0


fc = 0

for file in os.listdir(directory_path):
    if file:
        fc+=1
        file_path = os.path.join(directory_path, file)
        word_count, word_len, sen_count, sen_len = find_avgs_of_file(file_path)  # Use file_path
        total_word_len += word_len
        total_word_count += word_count
        total_sent_len += sen_len
        total_sent_count += sen_count


avg_wc = total_word_len/total_word_count

avg_sc = total_sent_len/total_sent_count

print(f"The average length of a sentence is: {avg_sc}")
print(f" The average length of a word is: {avg_wc}")
print(f"{fc} took {time.time()-start}")

