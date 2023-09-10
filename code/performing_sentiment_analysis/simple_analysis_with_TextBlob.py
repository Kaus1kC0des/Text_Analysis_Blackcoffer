from textblob import TextBlob
import os
import csv

file_path = "/Users/kausik/Documents/Project BlackCoffer/clean_files"
out = "/Users/kausik/Documents/Project BlackCoffer/Input and Output/results_textblob.csv"

with open(out,'w') as csvfile:
    headers = ["Filename","Polarity","Subjectivity"]
    writer = csv.DictWriter(csvfile,fieldnames=headers)
    writer.writeheader()

    for i in os.listdir("/Users/kausik/Documents/Project BlackCoffer/clean_files"):
        if i.endswith(".txt"):
            try:
                with open(os.path.join(file_path, i), 'r') as file:
                    text = file.read()
                    blob = TextBlob(text)
                    sentiment = blob.sentiment
                    writer.writerow({"Filename":i,"Polarity":sentiment.polarity,"Subjectivity":sentiment.subjectivity})
                    file.close()
            except Exception as e:
                print(f"An error occurred {e}")
        else:
            print(f"Could not read {i}")