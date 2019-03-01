# Generated from SampL.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\5")
        buf.write("\20\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\3\4\2\2\5\2\4\6\2\2\2\f\2\b\3\2\2\2\4\13\3\2\2\2\6")
        buf.write("\r\3\2\2\2\b\t\7\3\2\2\t\n\5\4\3\2\n\3\3\2\2\2\13\f\5")
        buf.write("\6\4\2\f\5\3\2\2\2\r\16\7\4\2\2\16\7\3\2\2\2\2")
        return buf.getvalue()


class SampLParser ( Parser ):

    grammarFileName = "SampL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'output'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "StringLiteral", "WS" ]

    RULE_p = 0
    RULE_expression = 1
    RULE_literal = 2

    ruleNames =  [ "p", "expression", "literal" ]

    EOF = Token.EOF
    T__0=1
    StringLiteral=2
    WS=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SampLParser.ExpressionContext,0)


        def getRuleIndex(self):
            return SampLParser.RULE_p

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP" ):
                listener.enterP(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP" ):
                listener.exitP(self)




    def p(self):

        localctx = SampLParser.PContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(SampLParser.T__0)
            self.state = 7
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
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
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
        self.enterRule(localctx, 4, self.RULE_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            self.match(SampLParser.StringLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





