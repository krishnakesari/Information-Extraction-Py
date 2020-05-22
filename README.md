# Applied Text Mining

Regular Expressions

Meta Characters :  Character Matches

Regex Character | Notes
--- | --- 
.  | Wild card, matches a single character
^  | Start of a string
$  | end of a string
[ ] | matches one of the set of characters within [ ]
[a - z] | matches one of the range of characters a,b,....z
[^abc] | matches a character that is not a,b, or, c
a|b  | matches either a or b, where a and b are strings

## Scoping/ Operators

() : Scoping for operators
\ : Escape character for special characters (\t, \n, \b)
\b : Matches word boundary
\d : Any digit, equal to [0-9]
\D : Any non-digit, equivalent to [^0-9]
\s : Any whitespace, equivalent to [ \t\n\r\f\v]
\S : Any non-whitespace, equivalent to [^ \t\n\r\f\v]
\w : Alphabetic character, equivalent to [a-zA-Z0-9_]
\W : Non-Alphabetic character, equivalent to [^a-zA-Z0-9_]

## Repetitions
* : matches zero or more occurrences
+ : matches one or more occurrences
? : matches zero or one occurrences
{n} : exactly n repetitions, n >= 0
{n,} : at least n repetitions
{,n} : at most n repetitions
{m,n}: at least m and at most n repetitions



