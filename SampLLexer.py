# Generated from SampL.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\5")
        buf.write(".\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\3\3\3\3\5\3\27\n\3\3\3\3\3\3\3\5")
        buf.write("\3\34\n\3\3\3\5\3\37\n\3\3\4\6\4\"\n\4\r\4\16\4#\3\5\3")
        buf.write("\5\3\6\6\6)\n\6\r\6\16\6*\3\6\3\6\2\2\7\3\3\5\4\7\2\t")
        buf.write("\2\13\5\3\2\4\4\2$$^^\5\2\13\f\16\17\"\"\2\60\2\3\3\2")
        buf.write("\2\2\2\5\3\2\2\2\2\13\3\2\2\2\3\r\3\2\2\2\5\36\3\2\2\2")
        buf.write("\7!\3\2\2\2\t%\3\2\2\2\13(\3\2\2\2\r\16\7q\2\2\16\17\7")
        buf.write("w\2\2\17\20\7v\2\2\20\21\7r\2\2\21\22\7w\2\2\22\23\7v")
        buf.write("\2\2\23\4\3\2\2\2\24\26\7$\2\2\25\27\5\7\4\2\26\25\3\2")
        buf.write("\2\2\26\27\3\2\2\2\27\30\3\2\2\2\30\37\7$\2\2\31\33\7")
        buf.write(")\2\2\32\34\5\7\4\2\33\32\3\2\2\2\33\34\3\2\2\2\34\35")
        buf.write("\3\2\2\2\35\37\7)\2\2\36\24\3\2\2\2\36\31\3\2\2\2\37\6")
        buf.write("\3\2\2\2 \"\5\t\5\2! \3\2\2\2\"#\3\2\2\2#!\3\2\2\2#$\3")
        buf.write("\2\2\2$\b\3\2\2\2%&\n\2\2\2&\n\3\2\2\2\')\t\3\2\2(\'\3")
        buf.write("\2\2\2)*\3\2\2\2*(\3\2\2\2*+\3\2\2\2+,\3\2\2\2,-\b\6\2")
        buf.write("\2-\f\3\2\2\2\b\2\26\33\36#*\3\b\2\2")
        return buf.getvalue()


class SampLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    StringLiteral = 2
    WS = 3

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'output'" ]

    symbolicNames = [ "<INVALID>",
            "StringLiteral", "WS" ]

    ruleNames = [ "T__0", "StringLiteral", "StringCharacters", "StringCharacter", 
                  "WS" ]

    grammarFileName = "SampL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


