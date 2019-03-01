# Generated from SampL.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("Q\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\5\t\63\n\t\3\t\3\t")
        buf.write("\3\t\5\t8\n\t\3\t\5\t;\n\t\3\n\3\n\7\n?\n\n\f\n\16\nB")
        buf.write("\13\n\3\13\6\13E\n\13\r\13\16\13F\3\f\3\f\3\r\6\rL\n\r")
        buf.write("\r\r\16\rM\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write("\t\21\n\23\13\25\2\27\2\31\f\3\2\6\6\2&&C\\aac|\7\2&&")
        buf.write("\62;C\\aac|\4\2$$^^\5\2\13\f\16\17\"\"\2T\2\3\3\2\2\2")
        buf.write("\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r")
        buf.write("\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\31\3")
        buf.write("\2\2\2\3\33\3\2\2\2\5\35\3\2\2\2\7$\3\2\2\2\t(\3\2\2\2")
        buf.write("\13*\3\2\2\2\r,\3\2\2\2\17.\3\2\2\2\21:\3\2\2\2\23<\3")
        buf.write("\2\2\2\25D\3\2\2\2\27H\3\2\2\2\31K\3\2\2\2\33\34\7\60")
        buf.write("\2\2\34\4\3\2\2\2\35\36\7q\2\2\36\37\7w\2\2\37 \7v\2\2")
        buf.write(" !\7r\2\2!\"\7w\2\2\"#\7v\2\2#\6\3\2\2\2$%\7x\2\2%&\7")
        buf.write("c\2\2&\'\7t\2\2\'\b\3\2\2\2()\7.\2\2)\n\3\2\2\2*+\7?\2")
        buf.write("\2+\f\3\2\2\2,-\7]\2\2-\16\3\2\2\2./\7_\2\2/\20\3\2\2")
        buf.write("\2\60\62\7$\2\2\61\63\5\25\13\2\62\61\3\2\2\2\62\63\3")
        buf.write("\2\2\2\63\64\3\2\2\2\64;\7$\2\2\65\67\7)\2\2\668\5\25")
        buf.write("\13\2\67\66\3\2\2\2\678\3\2\2\289\3\2\2\29;\7)\2\2:\60")
        buf.write("\3\2\2\2:\65\3\2\2\2;\22\3\2\2\2<@\t\2\2\2=?\t\3\2\2>")
        buf.write("=\3\2\2\2?B\3\2\2\2@>\3\2\2\2@A\3\2\2\2A\24\3\2\2\2B@")
        buf.write("\3\2\2\2CE\5\27\f\2DC\3\2\2\2EF\3\2\2\2FD\3\2\2\2FG\3")
        buf.write("\2\2\2G\26\3\2\2\2HI\n\4\2\2I\30\3\2\2\2JL\t\5\2\2KJ\3")
        buf.write("\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2NO\3\2\2\2OP\b\r\2")
        buf.write("\2P\32\3\2\2\2\t\2\62\67:@FM\3\b\2\2")
        return buf.getvalue()


class SampLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    StringLiteral = 8
    Identifier = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'.'", "'output'", "'var'", "','", "'='", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "StringLiteral", "Identifier", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "StringLiteral", "Identifier", "StringCharacters", "StringCharacter", 
                  "WS" ]

    grammarFileName = "SampL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


