def capitalize_all_words(sentence):
    return ' '.join(word.capitalize() for word in sentence.split()) 

sentence = "hello world python"
print(capitalize_all_words(sentence))