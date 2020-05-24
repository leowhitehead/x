from lark import Transformer, Lark
from base64 import b64encode
from sys import stderr, exit
import re
from grammar import grammar
from data import *

class parser(Transformer):
    def library(self, items):
        return "\n".join(map(str, items))

    def function(self, items):
        if type(items[0]) != str:
            fname = 'main'
        else:
            fname = items[0]
        return f"int {fname}({items[1]}){items[2]}"

    def params(self, items):
        return ','.join(items)

    def comp_stmt(self, items):
        statements = ''.join(map(str, items))
        return f"{{{statements}}}"
    
    def cond_stmt(self, items):
        return f"if({items[0]}){items[1]}"

    def loop_stmt(self, items):
        return f"while({items[0]}){items[1]}"

    def ret_stmt(self, items):
        return f"return {items[0]};"

    def def_stmt(self, items):
        if isstring(items[1]):
            vartype = "char*"
        else:
            vartype = "int"
        if type(items[0]) != str:
            error("Cannot reference builtin 'x'")
        return f"{vartype} {items[0]} = {items[1]};"

    def expr_stmt(self, items):
        return f"{items[0]};"

    def noop_stmt(self, items):
        return ";"

    def number(self, items):
        return items[0]

    def string(self, items):
        return items[0]

    def brack_expr(self, items):
        return f"({items[0]})"

    def ident_expr(self, items):
        ident = items[0]
        if ident == 'main':
            error("Cannot reference builtin 'x'")
        else:
            return ident
    
    def fcall_expr(self, items):
         return f"{items[0]}({items[1]})"

    def args(self, items):
        return ','.join(items)

    def x_a(self, items):
        return "main"

    def x_b(self, items):
        return "x_b"

    def x_c(self, items):
        return "x_c"

    def x_d(self, items):
        return "x_d"

    def x_e(self, items):
        return "x_e"

    def x_f(self, items):
        return "x_f"

    def x_g(self, items):
        return "x_g"

    def x_h(self, items):
        return "x_h"

    def x_i(self, items):
        return "x_i"

    def x_j(self, items):
        return "x_j"

    def x_k(self, items):
        return "x_k"

    def x_l(self, items):
        return "x_l"

    def x_m(self, items):
        return "x_m"

    def x_n(self, items):
        return "x_n"

    def x_o(self, items):
        return "x_o"

    def x_p(self, items):
        return "x_p"

    def x_q(self, items):
        return "x_q"

    def x_r(self, items):
        return "x_r"

    def x_s(self, items):
        return "x_s"

    def x_s(self, items):
        return "x_s"
    
    def x_t(self, items):
        return "x_t"

    def x_u(self, items):
        return "x_u"
    
    def x_v(self, items):
        return "x_v"

    def x_w(self, items):
        return "x_w"

    def x_x(self, items):
        return "x_x"

    def x_y(self, items):
        return "x_y"

    def x_z(self, items):
        return "x_z"

    def x_aa(self, items):
        return "x_aa"

    def x_ab(self, items):
        return "x_ab"

    def x_ac(self, items):
        return "x_ac"

    def x_ad(self, items):
        return "x_ad"

    def x_af(self, items):
        return "x_af"

    def x_ag(self, items):
        return "x_ag"

    def x_ah(self, items):
        return "x_ah"

    def x_ai(self, items):
        return "x_ai"

    def x_aj(self, items):
        return "x_aj"

    def x_ak(self, items):
        return "x_ak"

    def x_al(self, items):
        return "x_al"

    def x_am(self, items):
        return "x_am"

    def x_an(self, items):
        return "x_an"

    def x_ao(self, items):
        return "x_ao"

    def x_ap(self, items):
        return "x_ap"

    def x_aq(self, items):
        return "x_aq"

    def x_ar(self, items):
        return "x_ar"

    def bin_expr(self, items):
        operator = binops[items[1].data]
        if isstring(items[0]) and isstring(items[2]) and operator == '+':
            return f"stradd({items[0]},{items[2]})"
        return f"{items[0]}{operator}{items[2]}"
    
    def ternary_expr(self, items):
        return f"{items[0]}?{items[1]}:{items[2]}"

def isstring(string):
    return string[0] == string[-1] == "\"" \
    or string.startswith("stradd(") and string.endswith(")") \
    or string.startswith("x_d(") and string.endswith(")")

def parse(source):
    source = re.sub(r'\/\*.+\*\/', '', source)  #remove comments
    x_parser = Lark(grammar, start='library', parser='lalr', transformer=parser())
    try:
        tree = x_parser.parse(source)
    except Exception as e:
        print("Invalid Syntax:")
        err = str(e).split('\n')
        print(err[2])
        print(err[3])
        exit(1)
    return b64encode((lib+tree).encode('utf-8')).decode() #convert to base64 to make piping easier

def error(err):
    print(err, file=stderr)
    exit(1)