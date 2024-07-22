import re

def count_words(filename):
    # Read the file and convert all text to lowercase
    with open(filename, 'r') as file:
        text = file.read().lower()
    
    # Remove non-alphanumeric characters and split into words
    words = re.findall(r'\b\w+\b', text)
    
    # Initialize an empty dictionary to store word frequencies
    word_counts = {}
    
    # Count frequencies of each word
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Sort words by frequency in reverse order
    sorted_words = sorted(word_counts, key=lambda w: word_counts[w], reverse=True)
    
    # Display the words and their frequencies
    for word in sorted_words:
        print(f'{word}: {word_counts[word]}')

# Example usage:
filename = './LICENSE.txt'  # Replace with your file path
count_words(filename)
