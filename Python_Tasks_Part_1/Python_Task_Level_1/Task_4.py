
# Create a function that takes a sentence and prints the sentence without duplicated words

def sentence_no_duplicate (sentence) :
    words = sentence.split(' ')
    new_words = []
    for w in words :
        if w not in new_words :
            new_words.append(w)
    
    print(' '.join(new_words))

sentence = input('Enter your sentence : ')
sentence_no_duplicate(sentence)