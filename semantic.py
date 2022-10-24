# Import spacy
import spacy
nlp = spacy.load('en_core_web_md')

# SECTION ONE

# Enter test words as variables
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# SECTION TWO

tokens = nlp('cat apple monkey banana')

# Create a nested loop to cycle through the list to compare all contents
for token1 in tokens:
        for token2 in tokens:
                print(token1.text, token2.text, round(token1.similarity(token2),2))

# SECTION THREE

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
             "Hello, there is my car",
             "I've lost my car in my car",
             "I'd like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
        similarity = nlp(sentence).similarity(model_sentence)
        print(f"{sentence} - {similarity}")

# Write a note on what you found interesting about the similarities between cat, monkey, and banana

'''
 It is interesting that cat is 59% similar to monkey
 but monkey is only 40% similar to banana despite length similarity
 This is likely due to them both being animals
'''

# Think of an example of your own

# Enter test words as variables
word1 = nlp("motorbike")
word2 = nlp("car")
word3 = nlp("bicycle")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

'''
 Motorbike and car are 71%, Car and bicycle 63%, and motorbike and bicycle 83%.
 This is interesting as car and motorbikes are both motor vehicles, but bicycle and
 motorcycle are both 2 wheeled, and that seems to take precedence.
'''

# Run the example file and change the language model en_core_web_sm and write
# a note on what you notice the difference is from en_core_web_md

'''
Going from md to sm reduces all similarities in the recipes to complaints comparison
by an average of 80%, a maximum of 440% and a minimum of 2%, i.e. the results are wildly different.

This suggests that en_core_web_md is more accurate.
'''
