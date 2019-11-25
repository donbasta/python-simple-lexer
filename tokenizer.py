from imp_lexer import *

#Tokenizer
file = open('test.txt')
characters = file.read()
file.close()
tokens = imp_lex(characters)
tokenized = []
for token in tokens:
    tokenized.append(token)

file2 = open('tokenized_test.txt', 'w')

for token in tokenized:
    file2.write(str(token[1])+" ")

file2.close()