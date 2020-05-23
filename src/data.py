binops = {
    'assign': '=',
    'plus': '+',
    'minus': '-',
    'mult': '*',
    'pluseq': '+=',
    'mineq' : '-=',
    'equals': '==',
    'notequals': '!=',
    'lessthan': '<',
    'greaterthan': '>',
    'lessequal': '<=',
    'morequal': '>=',
    'modulo': '%'
}

defaultCompiler = "clang"

lib = r"""#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define x_b(X) _Generic((X),char *: x_print_string,int: x_print_int,float: x_print_float,default: x_print_int)(X)
#define x_c(...) var_int((f_args){__VA_ARGS__})
#define x_d(...) var_str((f_args){__VA_ARGS__})
const char* strin_base(char* prompt){char str[40];printf("%s", prompt);scanf("%[^\n]%*c", str);return &str;}
int intin_base(char* prompt){int i;printf("%s",prompt);scanf("%d",&i);return i;}
typedef struct{char* input;}f_args;
const char* var_str(f_args in){char* prompt = in.input ? in.input : "";return strin_base(prompt);}
int var_int(f_args in){char* prompt = in.input ? in.input : "";return intin_base(prompt);}
void x_print_int(int n){printf("%d", n);}
void x_print_float(float n){printf("%g",n);}
void x_print_string(char* s){printf("%s",s);}
char* stradd(const char *s1, const char *s2){char *result=malloc(strlen(s1)+strlen(s2)+1);strcpy(result,s1);strcat(result,s2);return result;}
/*--------BEGIN X PROGRAM----------*/
"""



'''
x (normal x): main function, reserved
X (capital x): print
х (cyrillic): integer input
ӽ (nivkh) : string input
 python3 main.py | clang -x c - -o main -w && ./main

 https://repl.it/repls/HandmadeAdmiredProduct

 
'''