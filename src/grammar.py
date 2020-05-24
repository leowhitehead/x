#"It's like [I] tried to define a formal grammar based on fragments of a raw database dump from the QuickBooks file of 
# a company that's about to collapse in an accounting scandal."
# - XKCD 1695 Title text.

grammar = r"""?library: function*

function: "func" identifier "(" params ")" statement

?params: identifier | (identifier ",")*

statement: "{" statement* "}"                  -> comp_stmt
        | "if" "(" expression ")" statement    -> cond_stmt
        | "while" "(" expression ")" statement -> loop_stmt
        | "return" expression ";"              -> ret_stmt
        | "let" identifier "=" expression ";"  -> def_stmt
        | expression ";"                       -> expr_stmt
        | ";"                                  -> noop_stmt

identifier: "x" -> main
        |   "X" -> x_b //print
        |   "х" -> x_c //int input
        |   "ӽ" -> x_d //string input
        |   "Χ" -> x_e
        |   "χ" -> x_f
        |   "ҳ" -> x_g
        |   "𝔵" -> x_h
        |   "𝖝" -> x_i
        |   "𝔁" -> x_j
        |   "𝕩" -> x_k
        |   "𝚡" -> x_l
        |   "乂" -> x_m
        |   "ﾒ" -> x_n
        |   "✕" -> x_o
        |   "✖" -> x_p
        |   "✗" -> x_q
        |   "✘" -> x_r
        |   "🗙" -> x_s
        |   "🗴" -> x_t
        |   "ᚷ"  -> x_u
        |   "🅇"  -> x_v
        |   "𝗑"  -> x_w
        |   "𝖷"  -> x_x
        |   "𝐱"  -> x_y
        |   "𝐗"  -> x_y
        |   "𝕏"  -> x_z
        |   "𝘅"  -> x_aa
        |   "𝗫"  -> x_ab
        |   "𝑥"  -> x_ac
        |   "𝑋"  -> x_ad
        |   "𝚇"  -> x_af
        |   "𝒙"  -> x_ag
        |   "𝑿"  -> x_ah
        |   "🆇"  -> x_ai
        |   "𝔛"  -> x_aj
        |   "𝘹"  -> x_ak
        |   "𝘟"  -> x_al
        |   "𝓍"  -> x_am
        |   "𝒳"  -> x_an
        |   "𝖃"  -> x_ao
        |   "𝙭"  -> x_ap
        |   "𝙓"  -> x_aq
        |   "𝓧"  -> x_ar

expression: SIGNED_NUMBER                          -> number
        | STRING                                   -> string
        | "(" expression ")"                       -> brack_expr
        | identifier                               -> ident_expr
        | identifier "(" args ")"                  -> fcall_expr
        | expression binop expression              -> bin_expr
        | expression "?" expression ":" expression -> ternary_expr

binop: "="     -> assign
        | "+"  -> plus
        | "-"  -> minus
        | "*"  -> mult
        | "+=" -> pluseq
        | "-=" -> mineq
        | "==" -> equals
        | "!=" -> notequals
        | "%"  -> modulo
        | "<"  -> lessthan
        | ">"  -> greaterthan
        | "<=" -> lessequal
        | ">=" -> morequal
        | "&&" -> and
        | "||" -> or

?args: identifier | (expression ",")*

STRING: /"([ -!#-&(-~)])*"/

DIGIT: "0".."9"
HEXDIGIT: "a".."f"|"A".."F"|DIGIT

INT: DIGIT+
SIGNED_INT: ["+"|"-"] INT
DECIMAL: INT "." INT? | "." INT

_EXP: ("e"|"E") SIGNED_INT
FLOAT: INT _EXP | DECIMAL _EXP?
SIGNED_FLOAT: ["+"|"-"] FLOAT

NUMBER: FLOAT | INT
SIGNED_NUMBER: ["+"|"-"] NUMBER

WS: /[ \t\f\r\n]/+
%ignore WS"""
