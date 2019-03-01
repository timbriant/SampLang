from antlr4 import *
from antlr4.tree.Trees import Trees
from SampLLexer import SampLLexer
from SampLListener import SampLListener
from SampLParser import SampLParser
from SampLVisitor import SampLVisitor
import sys

#create static variable for collecting the output


class SampLCustomVisitor(SampLVisitor):
    def visitPrintFunction(self, ctx):
        #visit stringcharacters on stringliteral
        print("OMG")
        return self.visitChildren(ctx)
        #expression = ctx.expression()
    def visitExpression(self, ctx):
        print("aaaa")

def main():
    lexer = SampLLexer(StdinStream())
    stream = CommonTokenStream(lexer)
    parser = SampLParser(stream)
    tree = parser.startCompile()
    visitor = SampLCustomVisitor()
    visitor.visit(tree)
    #printer = SampLListener()
    #walker = ParseTreeWalker()
    #walker.walk(printer, tree)
    print(Trees.toStringTree(tree, None, parser))

if __name__ == '__main__':
    main()