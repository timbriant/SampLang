# Generated from SampL.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\f")
        buf.write("\61\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write("\b\t\b\3\2\3\2\3\2\3\3\3\3\3\3\3\3\7\3\30\n\3\f\3\16\3")
        buf.write("\33\13\3\3\4\3\4\3\4\5\4 \n\4\3\5\3\5\3\5\7\5%\n\5\f\5")
        buf.write("\16\5(\13\5\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\2\2\t\2\4")
        buf.write("\6\b\n\f\16\2\2\2,\2\20\3\2\2\2\4\23\3\2\2\2\6\34\3\2")
        buf.write("\2\2\b!\3\2\2\2\n)\3\2\2\2\f+\3\2\2\2\16.\3\2\2\2\20\21")
        buf.write("\7\3\2\2\21\22\5\f\7\2\22\3\3\2\2\2\23\24\7\4\2\2\24\31")
        buf.write("\5\6\4\2\25\26\7\5\2\2\26\30\5\6\4\2\27\25\3\2\2\2\30")
        buf.write("\33\3\2\2\2\31\27\3\2\2\2\31\32\3\2\2\2\32\5\3\2\2\2\33")
        buf.write("\31\3\2\2\2\34\37\5\b\5\2\35\36\7\6\2\2\36 \5\n\6\2\37")
        buf.write("\35\3\2\2\2\37 \3\2\2\2 \7\3\2\2\2!&\7\13\2\2\"#\7\7\2")
        buf.write("\2#%\7\b\2\2$\"\3\2\2\2%(\3\2\2\2&$\3\2\2\2&\'\3\2\2\2")
        buf.write("\'\t\3\2\2\2(&\3\2\2\2)*\5\f\7\2*\13\3\2\2\2+,\5\16\b")
        buf.write("\2,-\7\t\2\2-\r\3\2\2\2./\7\n\2\2/\17\3\2\2\2\5\31\37")
        buf.write("&")
        return buf.getvalue()


class SampLParser ( Parser ):

    grammarFileName = "SampL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'output'", "'var'", "','", "'='", "'['", 
                     "']'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "StringLiteral", "Identifier", "WS" ]

    RULE_p = 0
    RULE_variableDeclaration = 1
    RULE_variableDeclarator = 2
    RULE_variableDeclaratorId = 3
    RULE_variableInitializer = 4
    RULE_expression = 5
    RULE_literal = 6

    ruleNames =  [ "p", "variableDeclaration", "variableDeclarator", "variableDeclaratorId", 
                   "variableInitializer", "expression", "literal" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    StringLiteral=8
    Identifier=9
    WS=10

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
            self.state = 14
            self.match(SampLParser.T__0)
            self.state = 15
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
        self.enterRule(localctx, 2, self.RULE_variableDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(SampLParser.T__1)
            self.state = 18
            self.variableDeclarator()
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SampLParser.T__2:
                self.state = 19
                self.match(SampLParser.T__2)
                self.state = 20
                self.variableDeclarator()
                self.state = 25
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
        self.enterRule(localctx, 4, self.RULE_variableDeclarator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.variableDeclaratorId()
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==SampLParser.T__3:
                self.state = 27
                self.match(SampLParser.T__3)
                self.state = 28
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
        self.enterRule(localctx, 6, self.RULE_variableDeclaratorId)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(SampLParser.Identifier)
            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==SampLParser.T__4:
                self.state = 32
                self.match(SampLParser.T__4)
                self.state = 33
                self.match(SampLParser.T__5)
                self.state = 38
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
        self.enterRule(localctx, 8, self.RULE_variableInitializer)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
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
        self.enterRule(localctx, 10, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.literal()
            self.state = 42
            self.match(SampLParser.T__6)
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
        self.enterRule(localctx, 12, self.RULE_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(SampLParser.StringLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





