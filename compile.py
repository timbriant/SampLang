from antlr4 import *
from antlr4.tree.Trees import Trees
from SampLLexer import SampLLexer
from SampLListener import SampLListener
from SampLParser import SampLParser
import sys

#create static variable for collecting the output


class HelloPrintListener(SampLListener):
    def enterLiteral(self, ctx):
        #visit stringcharacters on stringliteral
        print(ctx.StringLiteral())

def main():
    lexer = SampLLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = SampLParser(stream)
    tree = parser.p()
    printer = HelloPrintListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    print(Trees.toStringTree(tree, None, parser))

if __name__ == '__main__':
    main()