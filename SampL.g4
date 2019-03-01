grammar SampL;

p: 'output'  expression;

variableDeclaration: 'var' variableDeclarator (',' variableDeclarator)*;
//fix erpression
variableDeclarator: variableDeclaratorId ('=' variableInitializer)?;
variableDeclaratorId: Identifier ('[' ']')*;
variableInitializer: expression;

//expression can be int or string or double.
expression: literal '.';

literal: StringLiteral;

StringLiteral: '"' StringCharacters? '"' | '\'' StringCharacters? '\'';


Identifier: [a-zA-Z$_] ([a-zA-Z0-9$_])*;
fragment StringCharacters: StringCharacter+;
fragment StringCharacter: ~["\\];
WS  :  [ \t\r\n\u000C]+ -> skip;