from antlr4 import *
from MLListener import MLListener
from MLParser import MLParser
from MLVisitor import MLVisitor


class MLSemantics(MLVisitor):
    errors = ""
    codegen = []

    # specification: datasetname atr=selection tar=selection (testdata)? (model)?;
    def visitSpecification(self, ctx:MLParser.SpecificationContext):
        self.codegen.append(self.visitDatasetname(ctx.datasetname()))
        self.codegen.append(self.visitSelection(ctx.selection(0)))
        self.codegen.append(self.visitSelection(ctx.selection(1)))

        if(ctx.tst != None):
            self.codegen.append(self.visitTestdata(ctx.testdata()))
        else:
            self.codegen.append("25")

        if(ctx.mod != None):
            self.codegen.append(self.visitModel(ctx.model()))
        else:
            self.codegen.append(["all"])

        self.codegen.append(self.visitJob(ctx.job()))

        if(ctx.special() != None):
            self.codegen.append(self.visitSpecial(ctx.special()))
        else:
            self.codegen.append([])


    # datasetname: 'dataset' '=' IDENT;
    def visitDatasetname(self, ctx:MLParser.DatasetnameContext):
        try:
            file = open(ctx.IDENT().getText(), "r")
            file.close()
        except:
            self.errors += "Line " + str(ctx.start.line) + ": " + "Filename or directory can't be found\n"
            return None
        return ctx.IDENT().getText()


    # selection: '[' NUM ']' | '[' num1=NUM ':' num2=NUM ']';
    def visitSelection(self, ctx:MLParser.SelectionContext):
        if(ctx.num2 == None):
            return ctx.NUM(0).getText()
        else:
            if(int(ctx.NUM(0).getText()) < int(ctx.NUM(1).getText())):
                return [ctx.NUM(0).getText(), ctx.NUM(1).getText()]
            else:
                self.errors += "Line " + str(ctx.start.line) + ": " + "Slice's end limiter must be bigger than the start limiter\n"


    # testdata: NUM;
    def visitTestdata(self, ctx:MLParser.TestdataContext):
        value = int(ctx.NUM().getText())
        if(value <= 0 or value >= 100):
            self.errors += "Line " + str(ctx.start.line) + ": " + "Test data percentage must be between 1 and 99\n"
        else:
            return ctx.NUM().getText()

    # model: IDENT optional_model*;
    def visitModel(self, ctx:MLParser.ModelContext):
        allowed_models = ["dt", "nn", "rf", "all"]

        ac = [ctx.IDENT().getText().lower()]
        for i in range(0, len(ctx.optional_model())):
            ac.append(self.visitOptional_model(ctx.optional_model(i)).lower())

        for element in ac:
            if(element in allowed_models):
                continue
            else:
                self.errors += "Line " + str(ctx.start.line) + ": " + "Model code \"" + element + "\" is invalid\n"
        
        ac = list(set(ac))
        if("all" in ac):
            ac = ["all"]

        return ac

    # optional_model: ',' IDENT;
    def visitOptional_model(self, ctx:MLParser.Optional_modelContext):
        return ctx.IDENT().getText()

    # job: TYPE_OF_JOB; # TYPE_OF_JOB: 'class' | 'regression';
    def visitJob(self, ctx:MLParser.JobContext):
        return ctx.TYPE_OF_JOB().getText()

    # special: '[-' IDENT parameter? (',' optional_special)? ']';
    def visitSpecial(self, ctx:MLParser.SpecialContext):
        allowed_special_modes = ["run", "exe", "fi", "br", "tocsv", "graph"]

        if(ctx.parameter() == None):
            ac = [ctx.IDENT().getText().lower()]
        else:
            ac = [ctx.IDENT().getText().lower() + self.visitParameter(ctx.parameter()).lower()]

        if(ctx.optional_special() != None):
            for i in range(0, len(ctx.optional_special())):
                ac.append(self.visitOptional_special(ctx.optional_special(i)))

        for element in ac:
            if(element.lower().split("(")[0] in allowed_special_modes):
                continue
            else:
                self.errors += "Line " + str(ctx.start.line) + ": " + "Special mode code \"" + element.split("(")[0] + "\" is invalid\n"
        
        ac = list(set(ac)) 

        ## Parameters Handling ##

        for i in range(0,len(ac)):
            ## Run ## 
            if(ac[i][0:3] == "run"):
                # If there is parameter input
                if(len(ac[i]) > 3):
                    aux = ac[i].split("(")[1]
                    if(not aux.isdigit() or int(aux) <= 0):
                        self.errors += "Line " + str(ctx.start.line) + ": -run mode accepts positive integers only\n"
                # Default
                else:
                    ac[i] = ac[i] + "(10"
            ## Exe ##
            elif(ac[i][0:3] == "exe"):
                # If there is parameter input
                if(len(ac[i])>3):
                    self.errors += "Line " + str(ctx.start.line) + ": -exe doesn't take parameters\n"
            ## FI (Feature Importance) ##
            elif(ac[i][0:2] == "fi"):
                # If there is parameter input 
                if(len(ac[i])>2):
                    aux = ac[i].split("(")[1]
                    if(aux != "tree" and aux != "forest"):
                        self.errors += "Line " + str(ctx.start.line) + ": -fi accepts only 'tree' and 'forest' options"
                # Default
                else:
                    ac[i] = ac[i] + "(forest"
            ## BR (Binary Relevance) ##
            elif(ac[i][0:2] == "br"):
                # If there is parameter input
                if(len(ac[i])>2):
                    self.errors += "Line " + str(ctx.start.line) + ": -br doesn't take parameters\n"
            ## tocsv ##
            elif(ac[i][0:5] == "tocsv"):
                # If there is parameter input
                if(len(ac[i])>5):
                    self.errors += "Line " + str(ctx.start.line) + ": -tocsv doesn't take parameters\n"
            elif(ac[i][0:5] == "graph"):
                # If there is parameter input
                if(len(ac[i])>5):
                    self.errors += "Line " + str(ctx.start.line) + ": -graph doesn't take parameters\n"
   
        ## Incompatible Parameters ## 
        
        aux = []
        for element in ac:
            aux.append(element.split("(")[0])

        if("fi" in aux and "graph" in aux):
            self.errors +=  "Line " + str(ctx.start.line) + ": -fi and -graph modes are incompatible\n"
        elif("fi" in aux and "br" in aux):
            self.errors += "Line " + str(ctx.start.line) + ": -fi and -br modes are incompatible\n"
        elif("br" in aux and "graph" in aux):
            self.errors += "Line " + str(ctx.start.line) + ": -br and -graph modes are incompatible\n"

        return ac

    # optional_special: '-' IDENT parameter?;
    def visitOptional_special(self, ctx:MLParser.Optional_specialContext):
        if(ctx.parameter()!=None):
            return ctx.IDENT().getText() + self.visitParameter(ctx.parameter())
        else:
            return ctx.IDENT().getText()

    # parameter: '(' NUM ')' | '(' IDENT ')';
    def visitParameter(self, ctx:MLParser.ParameterContext):
        if(ctx.NUM() != None):
            return "(" + ctx.NUM().getText()
        else:
            return "(" + ctx.IDENT().getText()