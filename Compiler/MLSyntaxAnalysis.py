from antlr4.error.ErrorListener import ErrorListener
from antlr4 import *
import math


class MLSyntaxAnalysis(ErrorListener):
	def syntaxError(self, recognizer, o, line, column, msg, e):
		value = o.text
		message = msg
		symbols = []

		print("Line " + str(line) + ": ", end="")
		if(value == "<EOF>" and message[0:10] == "mismatched"):
			print("Job parameter has to be either 'class' or 'regression'\n")
		elif(value == "[" and message[0:10] == "mismatched"):
			print("features/classes range or training data size missing\n")
		elif(message[0:10] == "extraneous"):
			print("Erroneous value '" + value + "' found")
		elif(message[-5:] == "IDENT" and message[0:10] == "mismatched" and value.isdigit()):
			print("Dataset name is missing")
		elif(message[0:7] == "missing"):
			split = message.split("'")[1]
			print("Expected '" + split + "' next to '" + value + "'\n")
		elif(message[-3:] == "NUM" and message[0:10] == "mismatched"):
			print("Number is expected instead of '" + value + "'\n")
		elif(message[-5:] == "IDENT" and message[0:10] == "mismatched"):
			print("Name expected next to '" + value + "'\n")
		else:
			print("Syntax Error\n")
		exit()