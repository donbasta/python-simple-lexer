import os.path
import argparse
import grammar_converter
import tokenizer

class Tree:

    def __init__(self, symbol, left, right=None):
        self.symbol = symbol
        self.left = left
        self.right = right

class Parser:

    def __init__(self, grammar, sentence):

        self.parse_table = None
        self.prods = {}
        self.grammar = None
        self.grammar_from_file(grammar)
        self.__call__(sentence)

    def __call__(self, sentence, parse=False):

        if os.path.isfile(sentence):
            tokenizer.create_token(sentence)
            with open('tokenized_test.txt') as inp: #sentence : test.txt
                self.input = inp.readline().split()
                if parse:
                    self.parse()
        else:

            file = open('test.txt', 'w')
            file.write(sentence)
            file.close()

            tokenizer.create_token('test.txt')

            with open('tokenized_test.txt') as inp:
                self.input = inp.readline().split()

    def grammar_from_file(self, grammar):
        self.grammar = grammar_converter.convert_grammar(grammar_converter.read_grammar(grammar))

    def parse(self):
       
        length = len(self.input)
        self.parse_table = [[[] for x in range(length - y)] for y in range(length)]

        for i, word in enumerate(self.input):
            for rule in self.grammar:
                if f"'{word}'" == rule[1]:
                    self.parse_table[0][i].append(Tree(rule[0], word))
        for words_to_consider in range(2, length + 1):
            for starting_cell in range(0, length - words_to_consider + 1):
                for left_size in range(1, words_to_consider):
                    right_size = words_to_consider - left_size

                    left_cell = self.parse_table[left_size - 1][starting_cell]
                    right_cell = self.parse_table[right_size - 1][starting_cell + left_size]

                    for rule in self.grammar:
                        left_nodes = [n for n in left_cell if n.symbol == rule[1]]
                        if left_nodes:
                            right_nodes = [n for n in right_cell if n.symbol == rule[2]]
                            self.parse_table[words_to_consider - 1][starting_cell].extend(
                                [Tree(rule[0], left, right) for left in left_nodes for right in right_nodes]
                            )

    def verdict(self, output=True):
        start = self.grammar[0][0] #Simbol pertama di grammar CNF
        if len(self.input) > 0:
            final_nodes = [n for n in self.parse_table[-1][0] if n.symbol == start]
            if final_nodes:
                print()
                print("ACCEPTED")
            else:
                print()
                print("SYNTAX ERROR")
        else:
            print("ACCEPTED")


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("grammar",
                           help="File containing the grammar or string directly representing the grammar.")
    argparser.add_argument("sentence",
                           help="File containing the sentence or string directly representing the sentence.")
    args = argparser.parse_args()

    CYK = Parser(args.grammar, args.sentence)
    CYK.parse()
    CYK.verdict()