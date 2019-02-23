# Generated from ML.g4 by ANTLR 4.7.2
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\17")
        buf.write("a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n>\n\n\3\13\3\13\3\13\3\13")
        buf.write("\7\13D\n\13\f\13\16\13G\13\13\3\13\3\13\3\f\6\fL\n\f\r")
        buf.write("\f\16\fM\3\f\7\fQ\n\f\f\f\16\fT\13\f\3\r\5\rW\n\r\3\r")
        buf.write("\6\rZ\n\r\r\r\16\r[\3\16\3\16\3\16\3\16\2\2\17\3\3\5\4")
        buf.write("\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\3\2\7\5\2\f\f\17\17~~\5\2C\\aac|\7\2\60\60\62;C\\aac")
        buf.write("|\3\2\62;\5\2\13\f\17\17\"\"\2f\2\3\3\2\2\2\2\5\3\2\2")
        buf.write("\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2")
        buf.write("\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27")
        buf.write("\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\3\35\3\2\2\2\5\37\3")
        buf.write("\2\2\2\7!\3\2\2\2\t#\3\2\2\2\13%\3\2\2\2\r(\3\2\2\2\17")
        buf.write("*\3\2\2\2\21,\3\2\2\2\23=\3\2\2\2\25?\3\2\2\2\27K\3\2")
        buf.write("\2\2\31V\3\2\2\2\33]\3\2\2\2\35\36\7.\2\2\36\4\3\2\2\2")
        buf.write("\37 \7<\2\2 \6\3\2\2\2!\"\7]\2\2\"\b\3\2\2\2#$\7_\2\2")
        buf.write("$\n\3\2\2\2%&\7]\2\2&\'\7/\2\2\'\f\3\2\2\2()\7/\2\2)\16")
        buf.write("\3\2\2\2*+\7*\2\2+\20\3\2\2\2,-\7+\2\2-\22\3\2\2\2./\7")
        buf.write("e\2\2/\60\7n\2\2\60\61\7c\2\2\61\62\7u\2\2\62>\7u\2\2")
        buf.write("\63\64\7t\2\2\64\65\7g\2\2\65\66\7i\2\2\66\67\7t\2\2\67")
        buf.write("8\7g\2\289\7u\2\29:\7u\2\2:;\7k\2\2;<\7q\2\2<>\7p\2\2")
        buf.write("=.\3\2\2\2=\63\3\2\2\2>\24\3\2\2\2?@\7\61\2\2@A\7\61\2")
        buf.write("\2AE\3\2\2\2BD\n\2\2\2CB\3\2\2\2DG\3\2\2\2EC\3\2\2\2E")
        buf.write("F\3\2\2\2FH\3\2\2\2GE\3\2\2\2HI\b\13\2\2I\26\3\2\2\2J")
        buf.write("L\t\3\2\2KJ\3\2\2\2LM\3\2\2\2MK\3\2\2\2MN\3\2\2\2NR\3")
        buf.write("\2\2\2OQ\t\4\2\2PO\3\2\2\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2")
        buf.write("\2S\30\3\2\2\2TR\3\2\2\2UW\7/\2\2VU\3\2\2\2VW\3\2\2\2")
        buf.write("WY\3\2\2\2XZ\t\5\2\2YX\3\2\2\2Z[\3\2\2\2[Y\3\2\2\2[\\")
        buf.write("\3\2\2\2\\\32\3\2\2\2]^\t\6\2\2^_\3\2\2\2_`\b\16\2\2`")
        buf.write("\34\3\2\2\2\13\2=EKMPRV[\3\b\2\2")
        return buf.getvalue()


class MLLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    TYPE_OF_JOB = 9
    LINE_COMMENT = 10
    IDENT = 11
    NUM = 12
    IGNORECHAR = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "':'", "'['", "']'", "'[-'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "TYPE_OF_JOB", "LINE_COMMENT", "IDENT", "NUM", "IGNORECHAR" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "TYPE_OF_JOB", "LINE_COMMENT", "IDENT", "NUM", 
                  "IGNORECHAR" ]

    grammarFileName = "ML.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


