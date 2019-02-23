# Generated from ML.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MLParser import MLParser
else:
    from MLParser import MLParser

# This class defines a complete generic visitor for a parse tree produced by MLParser.

class MLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MLParser#specification.
    def visitSpecification(self, ctx:MLParser.SpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#datasetname.
    def visitDatasetname(self, ctx:MLParser.DatasetnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#selection.
    def visitSelection(self, ctx:MLParser.SelectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#testdata.
    def visitTestdata(self, ctx:MLParser.TestdataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#model.
    def visitModel(self, ctx:MLParser.ModelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#optional_model.
    def visitOptional_model(self, ctx:MLParser.Optional_modelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#job.
    def visitJob(self, ctx:MLParser.JobContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#special.
    def visitSpecial(self, ctx:MLParser.SpecialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#optional_special.
    def visitOptional_special(self, ctx:MLParser.Optional_specialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MLParser#parameter.
    def visitParameter(self, ctx:MLParser.ParameterContext):
        return self.visitChildren(ctx)



del MLParser