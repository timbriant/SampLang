grammar SampL;

startCompile: (newStatement '.')+;

newStatement: (printFunction | variableDeclaration);

printFunction: 'output'  expression;

variableDeclaration: 'var' variableDeclarator (',' variableDeclarator)*;
//fix expression
variableDeclarator: variableDeclaratorId ('=' variableInitializer)?;
variableDeclaratorId: Identifier ('[' ']')*;
variableInitializer: expression;

//expression can be int or string or double.
expression: literal;

literal: StringLiteral | IntegerLiteral;


//literals
StringLiteral: '"' StringCharacters? '"' | '\'' StringCharacters? '\'';
IntegerLiteral: Digit Digit*;
fragment Digit: '0' | NonZeroDigit;
fragment NonZeroDigit: [1-9];

Identifier: [a-zA-Z$_] ([a-zA-Z0-9$_])*;
fragment StringCharacters: StringCharacter+;
fragment StringCharacter: ~["\\];
WS  :  [ \t\r\n\u000C]+ -> skip;

//edit var dec