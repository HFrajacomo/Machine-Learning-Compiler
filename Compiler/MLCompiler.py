from antlr4 import *
from MLLexer import MLLexer
from MLListener import MLListener
from MLParser import MLParser
from MLVisitor import MLVisitor
from MLSemantics import MLSemantics
from MLGenerator import MLGenerator
from MLSyntaxAnalysis import MLSyntaxAnalysis
import argparse

parser = argparse.ArgumentParser(description='Compiler for Python Machine Learning Models', add_help=True)
parser.add_argument('-s','--string', dest='string', type=str, required=False)
parser.add_argument('-f','--file', dest='filepath', type=str, required=False)
args = parser.parse_args()

# Text Parsing
if(args.string != None):
	text = InputStream(args.string)
elif(args.filepath != None):
	text = FileStream(args.filepath)

# Lexic Analysis
lexer = MLLexer(text)
stream = CommonTokenStream(lexer)

# Syntax Analysis
parser = MLParser(stream)
parser._listeners = [MLSyntaxAnalysis()]
tree = parser.specification()


# Semantic Analysis
semantics = MLSemantics()
semantics.visit(tree)

if(semantics.errors):
	print(semantics.errors)
	exit()

print(semantics.codegen)
# Code Generation
generator = MLGenerator(semantics.codegen)
generator.generateCode()
print("Compilation Successful!\n")

if("exe" in generator.progress[-1]):
	generator.executeScript()
