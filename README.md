# Machine Learning Language and Compiler for Python
***Generate Python Code capable of conducting Machine Learning Routines***

## Motivation

Machine Learning algorithms are handy tools for Data Scientists. Creating a model capable of working on a dataset is a tedious proccess and may be of hard understanding to newcomers. With that in mind, this project was created.

## What is a Machine Learning Language?

In general, a language is a grammar formatted structure capable of describing something. In this case, the 'something' is a Machine Learning routine. That being said, an entire routine can be described with a "words" of this language.

## What is this Compiler?

A compiler is a program that reads text from a string or from a file, interprets the language it was written in and translates it into something else. What language is that? The Machine Learning Language, of course! And what is this 'something else'? Python Code!

# Installation
## Requirements

 - Python 3 as default python installation
 - Module antlr4-python3-runtime >= 4.7.2
 - Module Scikit-learn version >= 0.18.2
 - Module Pandas version >= 0.20.3
 - Module Matplotlib >= 2.0.2
 - Module Seaborn >= 0.9.0
 - Module Numpy >= 1.13.1+mk1



## Download
To download and use the project, simply type the following code in your terminal of choice:

    git clone https://github.com/HFrajacomo/Machine-Learning-Compiler

# The Language

As the compiler interprets the language to generate Python Code, one must first understand the language's syntax. A text that is correctly structured and understood by the compiler is organized in the following structure:

|  Dataset Name  | Attributes Range | Labels Range | Percentage of Test Data | Models | Special Settings                    |
|----------------|-------------------------------|-----------------------------|---------|--------| ----|

### ***All fields are comma separated***

| Field | Description  |
|--|--|
| Dataset Name | A string describing the name of the input dataset  |
| Atributes Range | A column number (starting at 0) that represents the attribute column in the dataset. For multiple attributes, use "X:Y", X being the first column of attributes and Y the column after the last attribute. 
| Labels Range | In single-label datasets, it's a number representing the label column. In multi-label datasets, it's a "X:Y" range, similar to the Attributes Range one.
| Percentage of Test Data | A number from 1 to 99 representing the dataset percentage left to validate the models. Defaults to 25 if not infomed
| Models | A list of model abbreviations delimited by commas and contained into brackets ([])
| Job | 'class' for Classification tasks and 'regression' for Regression tasks
| Special Settings | A list of modes used to alter the machine learning proccess and data visualization. Each mode is a string starting with an hyphen (-), separated by commans and contained into brackets ([]). Some modes accept arguments inside parenthesis (()).

### Examples

The following lines in this language are accepted:

| Text                | Generated Code Description |
|---------------------------------|--|
| `"data.csv, 1, 2, 25, [dt], class"` | Generates a Decision Tree for data.csv that uses column 1 as an attribute to predict column 2 and separates 25% of the dataset as training data |
| `"data.csv, 1:8, 8, 10, [dt, nn], class"` | Generates a Decision Tree and a Neural Network that uses column 1 to 7 as attributes to predict column 8 and separates 10% of the dataset as training data
| `"data.csv, 1:8, 8:10, , [all], regression, [-run(10)]"` | Generates all available models to do regression using columns 1 to 7 to predict columns 8 and 9. Defaults to leaving 25% of the dataset as training data and uses -run to run 10 different copies of these trained models.


## Models Specification

Right now, the models supported are: *Decision Trees, Random Forests and Neural Networks.*

The "Models" field interprets the models as:
| Model | Interpreted Abbreviation | Model Settings |
|--|--|--|
| Decision Tree | dt | A simple decision tree. The settings are always default |
| Neural Network | nn | The network always has 3 Hidden Layers of size **(n_attributes/2)+1**
| Random Forest | rf | The Forest is generated with **(n_attributes/3)+2** trees
| All Models | all | Generates code for all available Models

## Special Settings Specification

There are a few settings that can totally change the way the code works or is generated. These can be found in the following table:

| Setting | Interpreted Abbreviation | Arguments? | Description |
|--|--|--|--|
| No Arguments | [] or simply nothing | no | By default, the code prints out the precision_score of the models in classification mode and the Mean_squared_error of regression mode models |
| Run Mode | -run | Numeric | Set the amount of copies of the chosen models will be run. Defaults to 10 if no arguments are given.
| Execute | -exe | no | Compiles and executes the generated code
| To Csv | -tocsv | no | Instead of printing results, write them all to a .csv file
| To graph | -graph | no | Plots the results into a graph. May be incompatible with other Special Settings
| Feature Importance | -fi | Either (tree) or (forest)| Trains a model to figure out how important each Attribute is to classify the labels. Ignores all Models inputted and generates either a Decision Tree or a Random Forest. If no argument is given, defaults to Random Forest


# Usage

For the compiler to read text from a file, do:

    python MLCompiler.py -f <filepath>

For the compiler to read text from a string, do:

    python MLCompiler.py -s "<string>"
