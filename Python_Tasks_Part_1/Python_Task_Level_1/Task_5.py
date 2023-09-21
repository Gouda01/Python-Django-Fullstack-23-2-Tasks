

# Create a function that takes a sentence and prints how many words in the sentence (do not count the spaces)

def sentence_len (sentence) :
    words = sentence.split(' ')
    
    print(len(words))

sentence = input('Enter your sentence : ')
sentence_len(sentence)