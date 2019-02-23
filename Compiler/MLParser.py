# Generated from ML.g4 by ANTLR 4.7.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\17")
        buf.write("^\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\5\2\36\n\2\3\2\3\2\5\2\"\n\2\3\2\3\2\3\2\3\2\5\2")
        buf.write("(\n\2\3\3\3\3\3\4\3\4\3\4\3\4\5\4\60\n\4\3\5\3\5\3\6\3")
        buf.write("\6\3\6\7\6\67\n\6\f\6\16\6:\13\6\3\6\3\6\3\7\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\3\t\5\tF\n\t\3\t\3\t\7\tJ\n\t\f\t\16\t")
        buf.write("M\13\t\3\t\3\t\3\n\3\n\3\n\5\nT\n\n\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\5\13\\\n\13\3\13\2\2\f\2\4\6\b\n\f\16\20\22")
        buf.write("\24\2\2\2\\\2\26\3\2\2\2\4)\3\2\2\2\6/\3\2\2\2\b\61\3")
        buf.write("\2\2\2\n\63\3\2\2\2\f=\3\2\2\2\16@\3\2\2\2\20B\3\2\2\2")
        buf.write("\22P\3\2\2\2\24[\3\2\2\2\26\27\5\4\3\2\27\30\7\3\2\2\30")
        buf.write("\31\5\6\4\2\31\32\7\3\2\2\32\33\5\6\4\2\33\35\7\3\2\2")
        buf.write("\34\36\5\b\5\2\35\34\3\2\2\2\35\36\3\2\2\2\36\37\3\2\2")
        buf.write("\2\37!\7\3\2\2 \"\5\n\6\2! \3\2\2\2!\"\3\2\2\2\"#\3\2")
        buf.write("\2\2#$\7\3\2\2$\'\5\16\b\2%&\7\3\2\2&(\5\20\t\2\'%\3\2")
        buf.write("\2\2\'(\3\2\2\2(\3\3\2\2\2)*\7\r\2\2*\5\3\2\2\2+\60\7")
        buf.write("\16\2\2,-\7\16\2\2-.\7\4\2\2.\60\7\16\2\2/+\3\2\2\2/,")
        buf.write("\3\2\2\2\60\7\3\2\2\2\61\62\7\16\2\2\62\t\3\2\2\2\63\64")
        buf.write("\7\5\2\2\648\7\r\2\2\65\67\5\f\7\2\66\65\3\2\2\2\67:\3")
        buf.write("\2\2\28\66\3\2\2\289\3\2\2\29;\3\2\2\2:8\3\2\2\2;<\7\6")
        buf.write("\2\2<\13\3\2\2\2=>\7\3\2\2>?\7\r\2\2?\r\3\2\2\2@A\7\13")
        buf.write("\2\2A\17\3\2\2\2BC\7\7\2\2CE\7\r\2\2DF\5\24\13\2ED\3\2")
        buf.write("\2\2EF\3\2\2\2FK\3\2\2\2GH\7\3\2\2HJ\5\22\n\2IG\3\2\2")
        buf.write("\2JM\3\2\2\2KI\3\2\2\2KL\3\2\2\2LN\3\2\2\2MK\3\2\2\2N")
        buf.write("O\7\6\2\2O\21\3\2\2\2PQ\7\b\2\2QS\7\r\2\2RT\5\24\13\2")
        buf.write("SR\3\2\2\2ST\3\2\2\2T\23\3\2\2\2UV\7\t\2\2VW\7\16\2\2")
        buf.write("W\\\7\n\2\2XY\7\t\2\2YZ\7\r\2\2Z\\\7\n\2\2[U\3\2\2\2[")
        buf.write("X\3\2\2\2\\\25\3\2\2\2\13\35!\'/8EKS[")
        return buf.getvalue()


class MLParser ( Parser ):

    grammarFileName = "ML.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "':'", "'['", "']'", "'[-'", "'-'", 
                     "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "TYPE_OF_JOB", "LINE_COMMENT", "IDENT", 
                      "NUM", "IGNORECHAR" ]

    RULE_specification = 0
    RULE_datasetname = 1
    RULE_selection = 2
    RULE_testdata = 3
    RULE_model = 4
    RULE_optional_model = 5
    RULE_job = 6
    RULE_special = 7
    RULE_optional_special = 8
    RULE_parameter = 9

    ruleNames =  [ "specification", "datasetname", "selection", "testdata", 
                   "model", "optional_model", "job", "special", "optional_special", 
                   "parameter" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    TYPE_OF_JOB=9
    LINE_COMMENT=10
    IDENT=11
    NUM=12
    IGNORECHAR=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SpecificationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.atr = None # SelectionContext
            self.tar = None # SelectionContext
            self.tst = None # TestdataContext
            self.mod = None # ModelContext

        def datasetname(self):
            return self.getTypedRuleContext(MLParser.DatasetnameContext,0)


        def job(self):
            return self.getTypedRuleContext(MLParser.JobContext,0)


        def selection(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLParser.SelectionContext)
            else:
                return self.getTypedRuleContext(MLParser.SelectionContext,i)


        def special(self):
            return self.getTypedRuleContext(MLParser.SpecialContext,0)


        def testdata(self):
            return self.getTypedRuleContext(MLParser.TestdataContext,0)


        def model(self):
            return self.getTypedRuleContext(MLParser.ModelContext,0)


        def getRuleIndex(self):
            return MLParser.RULE_specification

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecification" ):
                listener.enterSpecification(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecification" ):
                listener.exitSpecification(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecification" ):
                return visitor.visitSpecification(self)
            else:
                return visitor.visitChildren(self)




    def specification(self):

        localctx = MLParser.SpecificationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_specification)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.datasetname()
            self.state = 21
            self.match(MLParser.T__0)
            self.state = 22
            localctx.atr = self.selection()
            self.state = 23
            self.match(MLParser.T__0)
            self.state = 24
            localctx.tar = self.selection()
            self.state = 25
            self.match(MLParser.T__0)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MLParser.NUM:
                self.state = 26
                localctx.tst = self.testdata()


            self.state = 29
            self.match(MLParser.T__0)
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MLParser.T__2:
                self.state = 30
                localctx.mod = self.model()


            self.state = 33
            self.match(MLParser.T__0)
            self.state = 34
            self.job()
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MLParser.T__0:
                self.state = 35
                self.match(MLParser.T__0)
                self.state = 36
                self.special()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DatasetnameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(MLParser.IDENT, 0)

        def getRuleIndex(self):
            return MLParser.RULE_datasetname

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDatasetname" ):
                listener.enterDatasetname(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDatasetname" ):
                listener.exitDatasetname(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDatasetname" ):
                return visitor.visitDatasetname(self)
            else:
                return visitor.visitChildren(self)




    def datasetname(self):

        localctx = MLParser.DatasetnameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_datasetname)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(MLParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SelectionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.num1 = None # Token
            self.num2 = None # Token

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(MLParser.NUM)
            else:
                return self.getToken(MLParser.NUM, i)

        def getRuleIndex(self):
            return MLParser.RULE_selection

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelection" ):
                listener.enterSelection(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelection" ):
                listener.exitSelection(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSelection" ):
                return visitor.visitSelection(self)
            else:
                return visitor.visitChildren(self)




    def selection(self):

        localctx = MLParser.SelectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_selection)
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(MLParser.NUM)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                localctx.num1 = self.match(MLParser.NUM)
                self.state = 43
                self.match(MLParser.T__1)
                self.state = 44
                localctx.num2 = self.match(MLParser.NUM)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TestdataContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(MLParser.NUM, 0)

        def getRuleIndex(self):
            return MLParser.RULE_testdata

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTestdata" ):
                listener.enterTestdata(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTestdata" ):
                listener.exitTestdata(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTestdata" ):
                return visitor.visitTestdata(self)
            else:
                return visitor.visitChildren(self)




    def testdata(self):

        localctx = MLParser.TestdataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_testdata)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(MLParser.NUM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(MLParser.IDENT, 0)

        def optional_model(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLParser.Optional_modelContext)
            else:
                return self.getTypedRuleContext(MLParser.Optional_modelContext,i)


        def getRuleIndex(self):
            return MLParser.RULE_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModel" ):
                listener.enterModel(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModel" ):
                listener.exitModel(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModel" ):
                return visitor.visitModel(self)
            else:
                return visitor.visitChildren(self)




    def model(self):

        localctx = MLParser.ModelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_model)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(MLParser.T__2)
            self.state = 50
            self.match(MLParser.IDENT)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MLParser.T__0:
                self.state = 51
                self.optional_model()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 57
            self.match(MLParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_modelContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(MLParser.IDENT, 0)

        def getRuleIndex(self):
            return MLParser.RULE_optional_model

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptional_model" ):
                listener.enterOptional_model(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptional_model" ):
                listener.exitOptional_model(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_model" ):
                return visitor.visitOptional_model(self)
            else:
                return visitor.visitChildren(self)




    def optional_model(self):

        localctx = MLParser.Optional_modelContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_optional_model)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(MLParser.T__0)
            self.state = 60
            self.match(MLParser.IDENT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JobContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_OF_JOB(self):
            return self.getToken(MLParser.TYPE_OF_JOB, 0)

        def getRuleIndex(self):
            return MLParser.RULE_job

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJob" ):
                listener.enterJob(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJob" ):
                listener.exitJob(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJob" ):
                return visitor.visitJob(self)
            else:
                return visitor.visitChildren(self)




    def job(self):

        localctx = MLParser.JobContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_job)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(MLParser.TYPE_OF_JOB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SpecialContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(MLParser.IDENT, 0)

        def parameter(self):
            return self.getTypedRuleContext(MLParser.ParameterContext,0)


        def optional_special(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MLParser.Optional_specialContext)
            else:
                return self.getTypedRuleContext(MLParser.Optional_specialContext,i)


        def getRuleIndex(self):
            return MLParser.RULE_special

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSpecial" ):
                listener.enterSpecial(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSpecial" ):
                listener.exitSpecial(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSpecial" ):
                return visitor.visitSpecial(self)
            else:
                return visitor.visitChildren(self)




    def special(self):

        localctx = MLParser.SpecialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_special)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(MLParser.T__4)
            self.state = 65
            self.match(MLParser.IDENT)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MLParser.T__6:
                self.state = 66
                self.parameter()


            self.state = 73
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==MLParser.T__0:
                self.state = 69
                self.match(MLParser.T__0)
                self.state = 70
                self.optional_special()
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 76
            self.match(MLParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Optional_specialContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENT(self):
            return self.getToken(MLParser.IDENT, 0)

        def parameter(self):
            return self.getTypedRuleContext(MLParser.ParameterContext,0)


        def getRuleIndex(self):
            return MLParser.RULE_optional_special

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOptional_special" ):
                listener.enterOptional_special(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOptional_special" ):
                listener.exitOptional_special(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptional_special" ):
                return visitor.visitOptional_special(self)
            else:
                return visitor.visitChildren(self)




    def optional_special(self):

        localctx = MLParser.Optional_specialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_optional_special)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.match(MLParser.T__5)
            self.state = 79
            self.match(MLParser.IDENT)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MLParser.T__6:
                self.state = 80
                self.parameter()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(MLParser.NUM, 0)

        def IDENT(self):
            return self.getToken(MLParser.IDENT, 0)

        def getRuleIndex(self):
            return MLParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = MLParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_parameter)
        try:
            self.state = 89
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.match(MLParser.T__6)
                self.state = 84
                self.match(MLParser.NUM)
                self.state = 85
                self.match(MLParser.T__7)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.match(MLParser.T__6)
                self.state = 87
                self.match(MLParser.IDENT)
                self.state = 88
                self.match(MLParser.T__7)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





