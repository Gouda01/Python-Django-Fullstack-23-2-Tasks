
# Create a function takes a sentence and a word and prints how many time the word used in the sentence

def sentence_remove_word (sentence,word) :
    words = sentence.split(' ')

    word_count = 0
        
    for w in words :
        if w == word :
            word_count += 1
    
    print(word_count)

sentence = input('Enter your sentence : ')
word = input('Enter your word you want to count in sentence : ')
sentence_remove_word(sentence,word)