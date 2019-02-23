grammar ML;

specification: datasetname ',' atr=selection ',' tar=selection ',' (tst=testdata)? ',' (mod=model)? ',' job (',' special)?;

datasetname: IDENT;
selection: NUM  | num1=NUM ':' num2=NUM;
testdata: NUM;
model: '[' IDENT optional_model* ']';
optional_model: ',' IDENT;
job: TYPE_OF_JOB;
special: '[-' IDENT parameter? (',' optional_special)* ']';
optional_special: '-' IDENT parameter?;
parameter: '(' NUM ')' | '(' IDENT ')';

TYPE_OF_JOB: 'class' | 'regression';
LINE_COMMENT: '//' ~[\r|\n]* -> skip;
IDENT: ([a-z] | [A-Z] | '_')+ ([a-z] | [A-Z] | '_' | '.' | [0-9])*;
NUM: ('-')? [0-9]+;
IGNORECHAR: ('\r' |'\n' | '\t' | ' ') -> skip;