# Práctica 1 - Estructura de Datos

############################################################################
# Creación y modificación de objetos
# Vectores
############################################################################

# Para crear un objeto y asignarle un nombre usamos los operadores
# de asignación <- o =

# Podemos usar cualquiera de los dos símbolos pero traten de usar solo
# uno de ellos

# Asignar el valor 15 a un objeto que llamaremos mio
mio<-15

# Asignar el valor 2 a un objeto que llamaremos mio2
mio2-<2


# Llevar a cabo algunas de las operaciones aritméticas usando los dos
# objetos antes creados +,-,*,/,%%,**,/, %/%




# Crear los siguientes objetos con distintos tipos de datos

cadena = "Hola, Mundo!"
numero = 15L
valor = 15
es_cierto = TRUE
complejo = 4+2i

# Usar las funciones class(), typeof(), length(), attributes(), str() con los
# distintos objetos y observar el resultado que se obtiene para cada caso

typeof(cadena)
typeof(numero)
typeof(valor)
typeof(es_cierto)
typeof(complejo)

class(numero)
class(valor)

attributes(cadena)

# ¿Es R case-sensitive? (sensitivo a las minúscula sy mayúsculas)
# ¿ Puedes asignar valores a un objeto x y otro diferente a un objeto X?

typeof(CADENA)

x=89
X=103
x+X

############################################################################
# Estructuras de datos: 1. Vectores atómicos
#
# Un vector es una colección de elementos del mismo tipo (caracter,
# numérico, decimal, lógico, complejo)
############################################################################

# Creación de Vectores
# Crear un vector vacío y de nombre vacio
vacio<-vector()


# ¿Cuál es el tipo de vacio?

logical

# Crear el vector vec_car1 como un vector de caracteres y longitud 10

ven_car1<-vector("character",length=10)

# Revisar la ayuda de la función vector() y ver cómo crear vectores de 
# distintos tipos de datos especificando el modo atómico (entero, 
# complejo, etc.)



# Crear un vector vacío para 10 elementos de tipo entero

vacio<-vector("integer",length=10)

# Crear un vector vacío para 5 elementos de tipo lógico 

vacio<-vector("logical",length=5)


# Creación de Vector númerico con valores 

vector=c(1L,2L,5L,10L,12L)

# Crear un vector de nombre logico cuyos elementos sean valores lógicos
# de TRUE y FALSEl

logico=c(TRUE,FALSE,TRUE,TRUE,FALSE,TRUE)

# Examinar las características del objeto lógico
typeof(logico)
class(logico)
length(logico)
str(logico)
attributes(logico)

# Crear el vector identificado como nombre que contiene los nombres
# Maria, Pedro, Cristina, Nestor

nombre<-c("Maria","Pedro","Cristina","Nestor")


# Agregar elementos a un vector
# Para agregar elementos a un vector ya existente
# podemos usar la función c() de concatenar

x=1:10         # vector numérico con una secuencia del 1 al 10
x=c(x,21:30)   # concatenamos otra secuencia del 21 al 30
x

# Agregar al vector de nombres de personas, agregar los siguientes
# nombres al inicio del vector
# Luis, Javier, Mariana
# Respuesta
nombre<-c("Luis" , "Javier", "Mariana", nombre)


#Mostrar todos los elementos del vector nombre menos el segundo elemento
nombre[-2]

#Mostrar todos los elementos del vector nombre menos el segundo y el
# cuarto elemento

nombre[-c(2,4)]


# R soporta valores de MISSING VALUE
# Se representan como NA (Not Available)

d=c(1,2,NA,6,7)
d

# Hay funciones que permiten verificar si el objeto tiene
# elementos no disponibles

is.na(d)
anyNA(d)

# ¿Se pueden mezclar tipos en un vector? 
# Todos los elementos de un vector son iguales.
# si mezclamos tipos, R hará una conversión al tipo que mejor se
# adecue a los elementos que contiene

diferentes=c(1L,1.5,"Hola que tal")
diferentes

# Se puede controlar la conversión indicando explícitamente el tipo
# as.numeric()
# as.character()
# as.complex()

# convertir el objeto item a caracteres
item = c(12,23,567,8)

as.character(item)


# convertir el objeto item1 a numérico, ¿qué resultado obtenemos?
item1 = c("12","23","567","a")

as.numeric(item1)
#Resultado
[1]  12  23 567  NA
Warning message:
  NAs introduced by coercion 

# Obtención de elementos de un vector o SUbsetting
# Podemos extraer elementos de un vector indicando la posición o
# índice dentro del vector. EN R las posiciones se enumeran desde
# el valor 1. Muchos lenguajes de programación lo hacen desde el
# valor 0
# Para obtener un valor en particular colocamos entre corchetes
# el índice que nos interesa

valores=c(8150,100234,5040,9000)
 # devuelve el segundo elemento del vector

# También podemos indicar rangos usando [inicio:final]
# o usar la función de concatenación para extraer el grupo de
# elementos que nos interesan c(1,4,3)

# extraer los elementos que se encuentran desde la posición 2 hasta la 4
# usando las dos alternativas indicadas anteriormente

> valores[2:4]
[1] 100234   5040   9000

> valores[c(2,3,4)]
[1] 100234   5040   9000

# También podemos extraer aquellos elementos o las posiciones
# dentro del vector que cumplan con ciertas condiciones 

# Extraer del objeto valores aquellos elementos que sean mayores que 8000
# Observar la diferencia en el resultado de las siguientes instrucciones

valores>8000 #da como resultado: 
[1]  TRUE  TRUE FALSE  TRUE

valores[valores>8000] #da como resultado:
[1]   8150 100234   9000


# para obtener las posiciones de los elementos que cumplen con la
# condición usamos la función which()

which(valores>8000)
[1] 1 2 4
# ¿qué obtenemos si ejecutamos valores[which(valores>8000)]

valores[which(valores>8000)]

# Operaciones estadísticas sobre vectores
# Aplicar las siguientes funciones sobre vectores
# mean()
# median()
# max()
# min()
# quantile()
# cor()
# cumsum()
# cumprod()
# diff()

# Aplicar alguna de estas funciones a vectores

