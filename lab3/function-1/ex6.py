def reverse_words(sentence):
    words = sentence.split()  
    reversed_sentence = " ".join(words[::-1])  
    return reversed_sentence

word= input("word:")
print(reverse_words(word))