# Generated from ML.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MLParser import MLParser
else:
    from MLParser import MLParser

# This class defines a complete listener for a parse tree produced by MLParser.
class MLListener(ParseTreeListener):

    # Enter a parse tree produced by MLParser#specification.
    def enterSpecification(self, ctx:MLParser.SpecificationContext):
        pass

    # Exit a parse tree produced by MLParser#specification.
    def exitSpecification(self, ctx:MLParser.SpecificationContext):
        pass


    # Enter a parse tree produced by MLParser#datasetname.
    def enterDatasetname(self, ctx:MLParser.DatasetnameContext):
        pass

    # Exit a parse tree produced by MLParser#datasetname.
    def exitDatasetname(self, ctx:MLParser.DatasetnameContext):
        pass


    # Enter a parse tree produced by MLParser#selection.
    def enterSelection(self, ctx:MLParser.SelectionContext):
        pass

    # Exit a parse tree produced by MLParser#selection.
    def exitSelection(self, ctx:MLParser.SelectionContext):
        pass


    # Enter a parse tree produced by MLParser#testdata.
    def enterTestdata(self, ctx:MLParser.TestdataContext):
        pass

    # Exit a parse tree produced by MLParser#testdata.
    def exitTestdata(self, ctx:MLParser.TestdataContext):
        pass


    # Enter a parse tree produced by MLParser#model.
    def enterModel(self, ctx:MLParser.ModelContext):
        pass

    # Exit a parse tree produced by MLParser#model.
    def exitModel(self, ctx:MLParser.ModelContext):
        pass


    # Enter a parse tree produced by MLParser#optional_model.
    def enterOptional_model(self, ctx:MLParser.Optional_modelContext):
        pass

    # Exit a parse tree produced by MLParser#optional_model.
    def exitOptional_model(self, ctx:MLParser.Optional_modelContext):
        pass


    # Enter a parse tree produced by MLParser#job.
    def enterJob(self, ctx:MLParser.JobContext):
        pass

    # Exit a parse tree produced by MLParser#job.
    def exitJob(self, ctx:MLParser.JobContext):
        pass


    # Enter a parse tree produced by MLParser#special.
    def enterSpecial(self, ctx:MLParser.SpecialContext):
        pass

    # Exit a parse tree produced by MLParser#special.
    def exitSpecial(self, ctx:MLParser.SpecialContext):
        pass


    # Enter a parse tree produced by MLParser#optional_special.
    def enterOptional_special(self, ctx:MLParser.Optional_specialContext):
        pass

    # Exit a parse tree produced by MLParser#optional_special.
    def exitOptional_special(self, ctx:MLParser.Optional_specialContext):
        pass


    # Enter a parse tree produced by MLParser#parameter.
    def enterParameter(self, ctx:MLParser.ParameterContext):
        pass

    # Exit a parse tree produced by MLParser#parameter.
    def exitParameter(self, ctx:MLParser.ParameterContext):
        pass


