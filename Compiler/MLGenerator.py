import os

class MLGenerator():
	progress = []
	file = None
	n_atr = 0
	first_atr_pos = 0
	last_atr_pos = 0
	identation_level = 0
	special_modes = {}
	command = ""
	rawname = ""

	def __init__(self, lista):
		self.progress = lista
		name = os.path.splitext(self.progress[0])[0]
		self.rawname = name
		self.file = open(os.getcwd() + "\ML_" + name + ".py", "w")
		self.command = "python " + os.getcwd() + "\ML_" + name + ".py"
		self.getSpecialModes()

	def getAmountofRuns(self):
		if("run" in self.special_modes):
			return self.special_modes["run"]
		else:
			return 1

	def getAmountofModels(self):
		if("all" in self.progress[0]):
			return "3"
		else:
			return str(len(self.progress[0]))
	
	def executeScript(self):
		os.system(self.command)

	def getSpecialModes(self):
		for element in self.progress[-1]:
			aux = element.split("(")
			if(len(aux) == 2):
				self.special_modes[aux[0]] = aux[1]

	def autoIdent(self):
		return "\t" * self.identation_level

	def addIdent(self):
		self.identation_level += 1

	def subIdent(self):
		self.identation_level -= 1

	def setIdent(self, num=0):
		self.identation_level = num

	def write(self, text=""):
		self.file.write(self.autoIdent() + text + "\n")

	# Writes for loop in -run mode
	def runMode(self):
		if("run" in self.special_modes):
			self.write("for i in range(0, " + self.special_modes["run"] + "):")
			self.addIdent()

	def generationMessage(self):
		self.file.write("# Generated with MLCompiler #\n\n")

	def generateImports(self):
		self.write("# Imports #")
		self.write("import pandas as pd")
		if("tocsv" in self.progress[-1]):
			self.write("import numpy as np")
		if("graph" in self.progress[-1]):
			self.write("import seaborn as sns; sns.set(style='ticks', color_codes=True)")
			self.write("import matplotlib.pyplot as plt")
		self.write("from datetime import datetime")
		self.write("from sklearn.model_selection import train_test_split")

		if(self.progress[5] == 'class'):
			self.write("from sklearn.metrics import precision_score")
			for element in self.progress[4]:
				if(element == "dt" or "fi" in self.special_modes):
					if("fi" in self.special_modes):
						if(self.special_modes["fi"] == "tree"):
							self.write("from sklearn.tree import DecisionTreeClassifier")
					else:		
						self.write("from sklearn.tree import DecisionTreeClassifier")
				if(element == "nn"):
					self.write("from sklearn.neural_network import MLPClassifier")
				if(element == "rf" or "fi" in self.special_modes):
					if("fi" in self.special_modes):
						if(self.special_modes["fi"] == "forest"):
							self.write("from sklearn.ensemble import RandomForestClassifier")
					else:
						self.write("from sklearn.ensemble import RandomForestClassifier")

				if(element == "all" and not "fi" in self.special_modes):
					self.write("from sklearn.tree import DecisionTreeClassifier")
					self.write("from sklearn.neural_network import MLPClassifier")
					self.write("from sklearn.ensemble import RandomForestClassifier")
		else:
			self.write("from sklearn.metrics import mean_squared_error")
			for element in self.progress[4]:
				if(element == "dt" or "fi" in self.special_modes):
					if("fi" in self.special_modes):
						if(self.special_modes["fi"] == "tree"):
							self.write("from sklearn.tree import DecisionTreeRegressor")
					else:		
						self.write("from sklearn.tree import DecisionTreeRegressor")
				if(element == "nn"):
					self.write("from sklearn.neural_network import MLPRegressor")
				if(element == "rf" or "fi" in self.special_modes):
					if("fi" in self.special_modes):
						if(self.special_modes["fi"] == "forest"):
							self.write("from sklearn.ensemble import RandomForestRegressor")
					else:
						self.write("from sklearn.ensemble import RandomForestRegressor")
				
				if(element == "all"):
					self.write("from sklearn.tree import DecisionTreeRegressor")
					self.write("from sklearn.neural_network import MLPRegressor")
					self.write("from sklearn.ensemble import RandomForestRegressor")
				

		self.write("\n")

	def generateTableLoading(self):
		self.write("# Dataset Loading #")
		self.write("data = pd.read_csv(\"" + self.progress.pop(0) + "\", sep=',')")
		self.write("\n")

	def generateXYSeparation(self):
		self.write("# Feature vs Class Separation #")
		if(isinstance(self.progress[0], list)):
			self.write("X = data[data.columns[" + self.progress[0][0] + ":" + self.progress[0][1] + "]]")
		else:
			self.write("X = data[data.columns[" + self.progress[0] + "]]")
		
		text = self.progress.pop(0)
		if(len(text) == 1):
			self.n_atr = int(text)
			self.first_atr_pos = int(text)
			self.last_atr_pos = int(text)
		else:
			self.n_atr = int(text[1]) - int(text[0])
			self.first_atr_pos = int(text[1])
			self.last_atr_pos = int(text[0])

		if(isinstance(self.progress[0], list)):
			self.write("y = data[data.columns[" + self.progress[0][0] + ":" + self.progress[0][1] + "]]")
		else:
			self.write("y = data[data.columns[" + self.progress[0] + "]]")

		self.progress.pop(0)
		self.write("\n")

	def generateHoldout(self):
		self.write("# Holdout #")
		self.write("X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=int(datetime.now().timestamp()), test_size=" + str(int(self.progress.pop(0))/100) + ")")
		self.write("\n")

	def generateModels(self):

		if("fi" in self.special_modes):
			if(self.special_modes["fi"] == "tree"):
				self.progress[0] = ["dt"]
			else:
				self.progress[0] = ["rf"]

		self.write("# Machine Learning Models Training and Evaluation #")
		if("tocsv" in self.progress[2] and not "fi" in self.special_modes):
			self.write("ac_index = 0")			
		if("graph" in self.progress[2]):
			self.write("accumulator = []")
			self.write("graph_labels = []\n")
		if("tocsv" in self.progress[2] and "fi" in self.special_modes):
			self.write("atr_acc = []\n")
		elif("tocsv" in self.progress[2]):
			self.write("to_file = [[] for i in range(" + self.getAmountofModels() + ")]")
			self.write("csv_labels = []\n")

		if("dt" in self.progress[0] or "all" in self.progress[0]):
			if(self.progress[1] == 'class'):
				self.write("# Decision Tree Classifier #\n")
				self.runMode()
				self.write("cls = DecisionTreeClassifier(random_state=int(datetime.now().timestamp()))")
				self.write("cls.fit(X_train, y_train)")

				if("fi" in self.special_modes and self.special_modes["fi"] == "tree"):
					if("tocsv" in self.progress[-1]):
						self.write("atr_acc.append(cls.feature_importances_)")
					else:
						self.write("print(data.columns[i] + ': ' + str(cls.feature_importances_[i]))")
					if("graph" in self.progress[-1]):
						self.write("accumulator.append(cls.feature_importances_[i])")

				else:
					self.write("y_pred = cls.predict(X_test)")
					if("tocsv" in self.progress[-1]):
						self.write("to_file[ac_index].append(str(precision_score(y_test, y_pred, average='micro')))\n")
					elif(not "graph" in self.progress[-1]):
						self.write("print('Decision Tree Precision: ' + str(precision_score(y_test, y_pred, average='micro')))\n")
					if("graph" in self.progress[-1]):
						self.write("accumulator.append(str(precision_score(y_test, y_pred, average='micro')))")

				self.setIdent()
				self.write("print()")
				if("graph" in self.progress[2]):
					self.write("graph_labels.append(['Decision Tree'] * " + self.getAmountofRuns() + ")")
				if("tocsv" in self.progress[2] and not "fi" in self.special_modes):
					self.write("csv_labels.append('Decision Tree')")
					self.write("ac_index += 1\n")
			else:
				self.runMode()
				self.write("# Decision Tree Regressor #\n")
				self.runMode()
				self.write("cls = DecisionTreeRegressor(random_state=int(datetime.now().timestamp()))")
				self.write("cls.fit(X_train, y_train)")

				if("fi" in self.special_modes and self.special_modes["fi"] == "tree"):
					if("tocsv" in self.progress[-1]):
						self.write("atr_acc.append(cls.feature_importances_)")
					else:
						self.write("print(data.columns[i] + ': ' + str(cls.feature_importances_[i]))")
					if("graph" in self.progress[-1]):
						self.write("accumulator.append(cls.feature_importances_[i])")

				else:
					self.write("y_pred = cls.predict(X_test)")
					if("tocsv" in self.progress[-1]):
						self.write("to_file[ac_index].append(str(mean_squared_error(y_test, y_pred)))\n")
					elif(not "graph" in self.progress[-1]):
						self.write("print('Decision Tree MSE: ' + str(mean_squared_error(y_test, y_pred)))\n")
					if("graph" in self.progress[-1]):
						self.write("accumulator.append(str(mean_squared_error(y_test, y_pred)))")
	
				self.setIdent()
				self.write("print()")
				if("graph" in self.progress[2]):
					self.write("graph_labels.append(['Decision Tree'] * " + self.getAmountofRuns() + ")")
				if("tocsv" in self.progress[2] and not "fi" in self.special_modes):
					self.write("csv_labels.append('Decision Tree')")
					self.write("ac_index += 1\n")

		if("nn" in self.progress[0] or "all" in self.progress[0]):

			if(self.progress[1] == 'class'):
				self.write("# Neural Network Classifier #\n")
				self.runMode()
				self.write("cls = MLPClassifier(hidden_layer_sizes=" + str((int(self.n_atr/2)+1,) * 3) + ")")
				self.write("cls.fit(X_train, y_train)")
				self.write("y_pred = cls.predict(X_test)")
				if("tocsv" in self.progress[-1]):
					self.write("to_file[ac_index].append(str(precision_score(y_test, y_pred, average='micro')))\n")
				elif(not "graph" in self.progress[-1]):
					self.write("print('Neural Network Precision: ' + str(precision_score(y_test, y_pred, average='micro')))\n")
				if("graph" in self.progress[-1]):
					self.write("accumulator.append(str(precision_score(y_test, y_pred, average='micro')))")

				self.setIdent()
				self.write("print()")
				if("graph" in self.progress[2]):
					self.write("graph_labels.append(['Neural Network'] * " + self.getAmountofRuns() + ")")
				if("tocsv" in self.progress[2] and not "fi" in self.special_modes):
					self.write("csv_labels.append('Neural Network')")
					self.write("ac_index += 1\n")
			else:
				self.write("# Neural Network Regressor #\n")
				self.runMode()
				self.write("cls = MLPRegressor(hidden_layer_sizes=" + str((int(self.n_atr/2)+1,) * 3) + ")")
				self.write("cls.fit(X_train, y_train)")
				self.write("y_pred = cls.predict(X_test)")
				if("tocsv" in self.progress[-1]):
					self.write("to_file[ac_index].append(str(mean_squared_error(y_test, y_pred)))\n")
				elif(not "graph" in self.progress[-1]):
					self.write("print('Neural Network MSE: ' + str(mean_squared_error(y_test, y_pred)))\n")
				if("graph" in self.progress[-1]):
					self.write("accumulator.append(str(mean_squared_error(y_test, y_pred)))")

				self.setIdent()
				self.write("print()")
				if("graph" in self.progress[2]):
					self.write("graph_labels.append(['Neural Network'] * " + self.getAmountofRuns() + ")")
				if("tocsv" in self.progress[2] and not "fi" in self.special_modes):
					self.write("csv_labels.append('Neural Network')")
					self.write("ac_index += 1\n")

		if("rf" in self.progress[0] or "all" in self.progress[0]):
			if(self.progress[1] == 'class'):
				self.write("# Random Forest Classifier #\n")
				self.runMode()
				self.write("cls = RandomForestClassifier(n_estimators=" + str(int(self.n_atr/3)+2) + ")")
				self.write("cls.fit(X_train, y_train)")

				if("fi" in self.special_modes and self.special_modes["fi"] == "forest"):
					if("tocsv" in self.progress[-1]):
						self.write("atr_acc.append(cls.feature_importances_)")
					else:
						self.write("for j in range(0, " + str(self.first_atr_pos) + "):")
						self.addIdent()
						self.write("print(data.columns[j] + ': ' + str(cls.feature_importances_[j]))")
						self.setIdent()
					if("graph" in self.progress[-1]):
						self.write("for j in range(0, " + str(self.first_atr_pos) + "):")
						self.addIdent()
						self.write("accumulator.append(cls.feature_importances_[i])")
						self.setIdent()
				else:
					self.write("y_pred = cls.predict(X_test)")
					if("tocsv" in self.progress[-1]):
						self.write("to_file[ac_index].append(str(precision_score(y_test, y_pred, average='micro')))\n")
					elif(not "graph" in self.progress[-1]):
						self.write("print('Random Forest Precision: ' + str(precision_score(y_test, y_pred, average='micro')))\n")
					if("graph" in self.progress[-1]):
						self.write("accumulator.append(str(precision_score(y_test, y_pred, average='micro')))")

				self.setIdent()
				self.write("print()")
				if("graph" in self.progress[2]):
					self.write("graph_labels.append(['Random Forest'] * " + self.getAmountofRuns() + ")")
				if("tocsv" in self.progress[2] and not "fi" in self.special_modes):
					self.write("csv_labels.append('Random Forest')")
					self.write("ac_index += 1\n")
			else:
				self.write("# Random Forest Regressor #\n")
				self.runMode()
				self.write("cls = RandomForestRegressor(n_estimators=" + str(int(self.n_atr/3)+2) + ")")
				self.write("cls.fit(X_train, y_train)")

				if("fi" in self.special_modes and self.special_modes["fi"] == "forest"):
					self.write("for i in range(0, " + str(self.first_atr_pos) + "):")
					self.addIdent()
					if("tocsv" in self.progress[-1]):
						self.write("atr_acc.append(cls.feature_importances_)")
					else:
						self.write("print(data.columns[i] + ': ' + str(cls.feature_importances_[i]))")
					if("graph" in self.progress[-1]):
						self.write("accumulator.append(cls.feature_importances_[i])")

				else:
					self.write("y_pred = cls.predict(X_test)")
					if("tocsv" in self.progress[-1]):
						self.write("to_file[ac_index].append(str(mean_squared_error(y_test, y_pred)))\n")
					elif(not "graph" in self.progress[-1]):
						self.write("print('Random Forest MSE: ' + str(mean_squared_error(y_test, y_pred)))\n")
					if("graph" in self.progress[-1]):
						self.write("accumulator.append(str(mean_squared_error(y_test, y_pred)))")
				
				self.setIdent()
				self.write("print()")
				if("graph" in self.progress[2]):
					self.write("graph_labels.append(['Random Forest'] * " + self.getAmountofRuns() + ")")
				if("tocsv" in self.progress[2] and not "fi" in self.special_modes):
					self.write("csv_labels.append('Random Forest')")
					self.write("ac_index += 1\n")

	def generateCsv(self):
		self.write("\n## CSV Saving ##\n")
		if(self.first_atr_pos == self.last_atr_pos):
			slice_range = str(self.first_atr_pos)
		else:
			slice_range = str(self.last_atr_pos) + ":" + str(self.first_atr_pos)

		if("fi" in self.special_modes):
			self.write("out_csv = pd.DataFrame(atr_acc, columns=data.columns[" + slice_range + "])")
		else:
			self.write("out_csv = pd.DataFrame()")
			self.write("for i in range(0, len(to_file)):")
			self.addIdent()
			self.write("out_csv.insert(loc=len(out_csv.columns), column=csv_labels[i], value=to_file[i])")
			self.setIdent()
		self.write("out_csv.to_csv('" + self.rawname + "_Analysis.csv', index=False)")

	def generateGraph(self):
		self.write("\n# Graph Creation #\n")

		self.write("aux_labels = []")
		self.write("while graph_labels:")
		self.addIdent()
		self.write("aux_labels.extend(graph_labels.pop(0))\n")
		self.setIdent()

		self.write("ax = sns.stripplot(x=aux_labels, y=accumulator)")
		self.write("plt.xlabel('Model')")
		self.write("plt.ylabel('Score')")
		self.write("plt.show()")
	

	def generateCode(self):
		self.generationMessage()
		self.generateImports()
		self.generateTableLoading()
		self.generateXYSeparation()
		self.generateHoldout()
		self.generateModels()
		if("tocsv" in self.progress[-1]):
			self.generateCsv()
		if("graph" in self.progress[-1]):
			self.generateGraph()
		self.file.close()
