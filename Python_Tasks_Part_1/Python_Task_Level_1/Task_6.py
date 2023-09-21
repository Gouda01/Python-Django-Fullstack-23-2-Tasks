
# Create a function that takes a sentence and word and remove the word from the sentence

def sentence_remove_word (sentence,word) :
    words = sentence.split(' ')
    new_words = []
    for w in words :
        if w !=  word :
            new_words.append(w)
    
    print(' '.join(new_words))

sentence = input('Enter your sentence : ')
word = input('Enter your word you want to remove : ')
sentence_remove_word(sentence,word)