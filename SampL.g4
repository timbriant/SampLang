grammar SampL;

p: 'output'  expression;
expression: literal '.';
literal: StringLiteral;

variableDeclaration: 'var' variableDeclarator (',' variableDeclarator)*;
//fix erpression
variableDeclarator: variableDeclaratorId ('=' variableInitializer)?;
variableDeclaratorId: Identifier ('[' ']')*;


StringLiteral: '"' StringCharacters? '"' | '\'' StringCharacters? '\'';


fragment Identifier: [a-zA-Z$_] ([a-zA-Z0-9$_])*;
fragment StringCharacters: StringCharacter+;
fragment StringCharacter: ~["\\];
WS  :  [ \t\r\n\u000C]+ -> skip;