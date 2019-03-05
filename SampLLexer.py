# Generated from SampL.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\r")
        buf.write("d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\5\t9\n\t\3\t\3\t\3\t\5\t>\n\t\3\t\5\tA\n\t")
        buf.write("\3\n\3\n\7\nE\n\n\f\n\16\nH\13\n\3\13\3\13\5\13L\n\13")
        buf.write("\3\f\3\f\3\r\3\r\7\rR\n\r\f\r\16\rU\13\r\3\16\6\16X\n")
        buf.write("\16\r\16\16\16Y\3\17\3\17\3\20\6\20_\n\20\r\20\16\20`")
        buf.write("\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\2\27\2\31\f\33\2\35\2\37\r\3\2\7\3\2\63;\6\2&&")
        buf.write("C\\aac|\7\2&&\62;C\\aac|\4\2$$^^\5\2\13\f\16\17\"\"\2")
        buf.write("g\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\37\3\2\2\2\3!\3\2\2\2\5#\3\2\2\2")
        buf.write("\7*\3\2\2\2\t.\3\2\2\2\13\60\3\2\2\2\r\62\3\2\2\2\17\64")
        buf.write("\3\2\2\2\21@\3\2\2\2\23B\3\2\2\2\25K\3\2\2\2\27M\3\2\2")
        buf.write("\2\31O\3\2\2\2\33W\3\2\2\2\35[\3\2\2\2\37^\3\2\2\2!\"")
        buf.write("\7\60\2\2\"\4\3\2\2\2#$\7q\2\2$%\7w\2\2%&\7v\2\2&\'\7")
        buf.write("r\2\2\'(\7w\2\2()\7v\2\2)\6\3\2\2\2*+\7x\2\2+,\7c\2\2")
        buf.write(",-\7t\2\2-\b\3\2\2\2./\7.\2\2/\n\3\2\2\2\60\61\7?\2\2")
        buf.write("\61\f\3\2\2\2\62\63\7]\2\2\63\16\3\2\2\2\64\65\7_\2\2")
        buf.write("\65\20\3\2\2\2\668\7$\2\2\679\5\33\16\28\67\3\2\2\289")
        buf.write("\3\2\2\29:\3\2\2\2:A\7$\2\2;=\7)\2\2<>\5\33\16\2=<\3\2")
        buf.write("\2\2=>\3\2\2\2>?\3\2\2\2?A\7)\2\2@\66\3\2\2\2@;\3\2\2")
        buf.write("\2A\22\3\2\2\2BF\5\25\13\2CE\5\25\13\2DC\3\2\2\2EH\3\2")
        buf.write("\2\2FD\3\2\2\2FG\3\2\2\2G\24\3\2\2\2HF\3\2\2\2IL\7\62")
        buf.write("\2\2JL\5\27\f\2KI\3\2\2\2KJ\3\2\2\2L\26\3\2\2\2MN\t\2")
        buf.write("\2\2N\30\3\2\2\2OS\t\3\2\2PR\t\4\2\2QP\3\2\2\2RU\3\2\2")
        buf.write("\2SQ\3\2\2\2ST\3\2\2\2T\32\3\2\2\2US\3\2\2\2VX\5\35\17")
        buf.write("\2WV\3\2\2\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\34\3\2\2\2")
        buf.write("[\\\n\5\2\2\\\36\3\2\2\2]_\t\6\2\2^]\3\2\2\2_`\3\2\2\2")
        buf.write("`^\3\2\2\2`a\3\2\2\2ab\3\2\2\2bc\b\20\2\2c \3\2\2\2\13")
        buf.write("\28=@FKSY`\3\b\2\2")
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
    IntegerLiteral = 9
    Identifier = 10
    WS = 11

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'.'", "'output'", "'var'", "','", "'='", "'['", "']'" ]

    symbolicNames = [ "<INVALID>",
            "StringLiteral", "IntegerLiteral", "Identifier", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "StringLiteral", "IntegerLiteral", "Digit", "NonZeroDigit", 
                  "Identifier", "StringCharacters", "StringCharacter", "WS" ]

    grammarFileName = "SampL.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


