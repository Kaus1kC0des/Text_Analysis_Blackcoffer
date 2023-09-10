import os
import nltk
from nltk.tokenize import sent_tokenize,word_tokenize
from nltk.corpus import stopwords
# nltk.download('punkt')
# nltk.download('stopwords')

swords = []
stopwords_directory = "/Users/kausik/Documents/Project BlackCoffer/StopWords"
for filename in os.listdir(stopwords_directory):
    if filename.endswith('.txt'):  # Make sure to process only .txt files
        file_path = os.path.join(stopwords_directory, filename)
        with open(file_path, 'rb') as file:  # Open in binary mode
            content = file.read()

            # Specify the correct encoding if known (e.g., 'latin-1')
            try:
                # Assuming 'content' is a string containing the file content
                stops = set([line.replace('\r', '') for line in content.decode('utf-8').split('\n')])
                swords.append(stops)
            except UnicodeDecodeError:
                with open("/Users/kausik/Documents/Project BlackCoffer/code/removing_stopwords/errors.txt",'w') as f:
                    f.write(f"{filename}")
                    f.close()
                print(f"Error decoding file {filename}. It may have a different encoding.")

# Assuming you have a list of sets named 'stopwords_list'
# Merge all sets into a single list without sets
merged_stopwords = []
for stopword in swords:
    merged_stopwords.extend(stopword)

for i in os.listdir("/Users/kausik/Documents/Project BlackCoffer/contents"):
    with open(i,'r') as file:
        uncleaned_content = file.read()
    file.close()

    cleaned = [word for word in uncleaned_content if word not in merged_stopwords]
    with open(f"/Users/kausik/Documents/Project BlackCoffer/clean_files/{i}",'w') as f:
        f.write(cleaned)
    f.close()


# 'merged_stopwords' now contains all stopwords in a single list


print(len(merged_stopwords))
# print(swords)