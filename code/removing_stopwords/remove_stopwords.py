import os

# Directory containing stopwords files
stopwords_directory = "/Users/kausik/Documents/Project BlackCoffer/StopWords"

# Initialize a list to store stopwords
stopwords_list = []

with open("/Users/kausik/Documents/Project BlackCoffer/StopWords/StopWords_Currencies.txt",'rb') as file:
    stopwords_from_file = [line.strip() for line in file.readlines()]
    stopwords_list.extend(stopwords_from_file)

# Loop through each file in the stopwords directory
for filename in os.listdir(stopwords_directory):
    if filename.endswith('.txt') and filename!="StopWords_Currencies.txt":
        file_path = os.path.join(stopwords_directory, filename)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                stopwords_from_file = [line.strip() for line in file.readlines()]
                stopwords_list.extend(stopwords_from_file)
        except UnicodeDecodeError:
            print(f"Error decoding file {filename}. It may have a different encoding.")

# Create a set of stopwords for faster lookup
stopwords_set = set(stopwords_list)

# Function to remove stopwords from text
def remove_stopwords(text):
    words = text.split()
    cleaned_words = [word for word in words if word.lower() not in stopwords_set]
    cleaned_text = ' '.join(cleaned_words)
    return cleaned_text

# Directory containing text files to be cleaned
input_directory = "/Users/kausik/Documents/Project BlackCoffer/contents"
output_directory = "/Users/kausik/Documents/Project BlackCoffer/clean_files"

# Loop through each text file in the input directory, clean it, and save to the output directory
for filename in os.listdir(input_directory):
    if filename.endswith('.txt'):
        input_path = os.path.join(input_directory, filename)
        output_path = os.path.join(output_directory, filename)

        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read()

        cleaned_content = remove_stopwords(content)

        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(cleaned_content)

# Print the number of stopwords loaded
print(len(stopwords_set))
