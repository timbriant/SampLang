grammar SampLang;
r   : 'print' '(' ID ')';
ID  : [a-zA-Z0-9]+;
WS  : [ \t\r\n]+ -> skip ;