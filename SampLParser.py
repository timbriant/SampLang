# Generated from SampL.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\r")
        buf.write("?\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\3\2\3\2\6\2\30\n\2\r\2\16\2\31")
        buf.write("\3\3\3\3\5\3\36\n\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\7\5\'")
        buf.write("\n\5\f\5\16\5*\13\5\3\6\3\6\3\6\5\6/\n\6\3\7\3\7\3\7\7")
        buf.write("\7\64\n\7\f\7\16\7\67\13\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n")
        buf.write("\2\2\13\2\4\6\b\n\f\16\20\22\2\3\3\2\n\13\2:\2\27\3\2")
        buf.write("\2\2\4\35\3\2\2\2\6\37\3\2\2\2\b\"\3\2\2\2\n+\3\2\2\2")
        buf.write("\f\60\3\2\2\2\168\3\2\2\2\20:\3\2\2\2\22<\3\2\2\2\24\25")
        buf.write("\5\4\3\2\25\26\7\3\2\2\26\30\3\2\2\2\27\24\3\2\2\2\30")
        buf.write("\31\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\3\3\2\2\2\33")
        buf.write("\36\5\6\4\2\34\36\5\b\5\2\35\33\3\2\2\2\35\34\3\2\2\2")
        buf.write("\36\5\3\2\2\2\37 \7\4\2\2 !\5\20\t\2!\7\3\2\2\2\"#\7\5")
        buf.write("\2\2#(\5\n\6\2$%\7\6\2\2%\'\5\n\6\2&$\3\2\2\2\'*\3\2\2")
        buf.write("\2(&\3\2\2\2()\3\2\2\2)\t\3\2\2\2*(\3\2\2\2+.\5\f\7\2")
        buf.write(",-\7\7\2\2-/\5\16\b\2.,\3\2\2\2./\3\2\2\2/\13\3\2\2\2")
        buf.write("\60\65\7\f\2\2\61\62\7\b\2\2\62\64\7\t\2\2\63\61\3\2\2")
        buf.write("\2\64\67\3\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\66\r\3\2")
        buf.write("\2\2\67\65\3\2\2\289\5\20\t\29\17\3\2\2\2:;\5\22\n\2;")
        buf.write("\21\3\2\2\2<=\t\2\2\2=\23\3\2\2\2\7\31\35(.\65")
        return buf.getvalue()


class SampLParser ( Parser ):

    grammarFileName = "SampL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'output'", "'var'", "','", "'='", 
                     "'['", "']'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "StringLiteral", "IntegerLiteral", "Identifier", "WS" ]

    RULE_startCompile = 0
    RULE_newStatement = 1
    RULE_printFunction = 2
    RULE_variableDeclaration = 3
    RULE_variableDeclarator = 4
    RULE_variableDeclaratorId = 5
    RULE_variableInitializer = 6
    RULE_expression = 7
    RULE_literal = 8

    ruleNames =  [ "startCompile", "newStatement", "printFunction", "variableDeclaration", 
                   "variableDeclarator", "variableDeclaratorId", "variableInitializer", 
                   "expression", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    StringLiteral=8
    IntegerLiteral=9
    Identifier=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartCompileContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SampLParser.NewStatementContext)
            else:
                return self.getTypedRuleContext(SampLParser.NewStatementContext,i)


        def getRuleIndex(self):
            return SampLParser.RULE_startCompile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartCompile" ):
                listener.enterStartCompile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartCompile" ):
                listener.exitStartCompile(self)




    def startCompile(self):

        localctx = SampLParser.StartCompileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_startCompile)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.newStatement()
                self.state = 19
                self.match(SampLParser.T__0)
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==SampLParser.T__1 or _la==SampLParser.T__2):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewStatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def printFunction(self):
            return self.getTypedRuleContext(SampLParser.PrintFunctionContext,0)


        def variableDeclaration(self):
            return self.getTypedRuleContext(SampLParser.VariableDeclarationContext,0)


        def getRuleIndex(self):
            return SampLParser.RULE_newStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewStatement" ):
                listener.enterNewStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewStatement" ):
                listener.exitNewStatement(self)




    def newStatement(self):

        localctx = SampLParser.NewStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_newStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SampLParser.T__1]:
                self.state = 25
                self.printFunction()
                pass
            elif token in [SampLParser.T__2]:
                self.state = 26
                self.variableDeclaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintFunctionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SampLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SampLParser.RULE_printFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintFunction" ):
                listener.enterPrintFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintFunction" ):
                listener.exitPrintFunction(self)




    def printFunction(self):

        localctx = SampLParser.PrintFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_printFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(SampLParser.T__1)
            self.state = 30
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclarator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SampLParser.VariableDeclaratorContext)
            else:
                return self.getTypedRuleContext(SampLParser.VariableDeclaratorContext,i)


        def getRuleIndex(self):
            return SampLParser.RULE_variableDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaration" ):
                listener.enterVariableDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaration" ):
                listener.exitVariableDeclaration(self)




    def variableDeclaration(self):

        localctx = SampLParser.VariableDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(SampLParser.T__2)
            self.state = 33
            self.variableDeclarator()
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SampLParser.T__3:
                self.state = 34
                self.match(SampLParser.T__3)
                self.state = 35
                self.variableDeclarator()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclaratorContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variableDeclaratorId(self):
            return self.getTypedRuleContext(SampLParser.VariableDeclaratorIdContext,0)


        def variableInitializer(self):
            return self.getTypedRuleContext(SampLParser.VariableInitializerContext,0)


        def getRuleIndex(self):
            return SampLParser.RULE_variableDeclarator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclarator" ):
                listener.enterVariableDeclarator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclarator" ):
                listener.exitVariableDeclarator(self)




    def variableDeclarator(self):

        localctx = SampLParser.VariableDeclaratorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variableDeclarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.variableDeclaratorId()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SampLParser.T__4:
                self.state = 42
                self.match(SampLParser.T__4)
                self.state = 43
                self.variableInitializer()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableDeclaratorIdContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SampLParser.Identifier, 0)

        def getRuleIndex(self):
            return SampLParser.RULE_variableDeclaratorId

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableDeclaratorId" ):
                listener.enterVariableDeclaratorId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableDeclaratorId" ):
                listener.exitVariableDeclaratorId(self)




    def variableDeclaratorId(self):

        localctx = SampLParser.VariableDeclaratorIdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_variableDeclaratorId)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(SampLParser.Identifier)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SampLParser.T__5:
                self.state = 47
                self.match(SampLParser.T__5)
                self.state = 48
                self.match(SampLParser.T__6)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableInitializerContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SampLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SampLParser.RULE_variableInitializer

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableInitializer" ):
                listener.enterVariableInitializer(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableInitializer" ):
                listener.exitVariableInitializer(self)




    def variableInitializer(self):

        localctx = SampLParser.VariableInitializerContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variableInitializer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(SampLParser.LiteralContext,0)


        def getRuleIndex(self):
            return SampLParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = SampLParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.literal()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def StringLiteral(self):
            return self.getToken(SampLParser.StringLiteral, 0)

        def IntegerLiteral(self):
            return self.getToken(SampLParser.IntegerLiteral, 0)

        def getRuleIndex(self):
            return SampLParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = SampLParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            _la = self._input.LA(1)
            if not(_la==SampLParser.StringLiteral or _la==SampLParser.IntegerLiteral):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





