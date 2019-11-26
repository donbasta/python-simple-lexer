from imp_lexer import *

#Menuliskan hasil Tokenizer sebuah file ke dalam file line untuk diteruskan ke CYK_Parser

def create_token(sentence):

    file = open(sentence)
    characters = file.read()
    file.close()
    tokens = imp_lex(characters)
    tokenized = []
    for token in tokens:
        tokenized.append(token)

    file2 = open('tokenized_test.txt', 'w')

    for token in tokenized:
        file2.write(str(token)+" ")

    file2.close()

if __name__ == "__main__":

    create_token('test.txt')