# no tengo que decir que tipo de variable es
x=5
txt= " esto es un texto"
print(x,txt)

# Python es caseSensitive (interpreta minuscula y mayuscula como diferente)
y=2
Y="TEXTO"
print(y,Y)
 
 
#puede empezar con una letra o un guion bajo ( underscore)

variable=2
_variable=3
print(variable, _variable)

# Una vairable NO PUEDE empezar con numero


var=3
Var=4
print(var,Var)

# no se puede utilizar palabras reservadas ( que python usa como su sintaxis)

# multiasignacion
r,s,t=1,2,3
a=b=c=10
print(t,s,r)
print(a,b,c)