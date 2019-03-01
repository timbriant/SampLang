# Generated from SampL.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SampLParser import SampLParser
else:
    from SampLParser import SampLParser

# This class defines a complete generic visitor for a parse tree produced by SampLParser.

class SampLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SampLParser#startCompile.
    def visitStartCompile(self, ctx:SampLParser.StartCompileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampLParser#newStatement.
    def visitNewStatement(self, ctx:SampLParser.NewStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampLParser#printFunction.
    def visitPrintFunction(self, ctx:SampLParser.PrintFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampLParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:SampLParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampLParser#variableDeclarator.
    def visitVariableDeclarator(self, ctx:SampLParser.VariableDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampLParser#variableDeclaratorId.
    def visitVariableDeclaratorId(self, ctx:SampLParser.VariableDeclaratorIdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampLParser#variableInitializer.
    def visitVariableInitializer(self, ctx:SampLParser.VariableInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampLParser#expression.
    def visitExpression(self, ctx:SampLParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SampLParser#literal.
    def visitLiteral(self, ctx:SampLParser.LiteralContext):
        return self.visitChildren(ctx)



del SampLParser