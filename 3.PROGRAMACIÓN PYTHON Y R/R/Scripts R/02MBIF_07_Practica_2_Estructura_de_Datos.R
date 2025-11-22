# Pr?ctica 2 - Estructura de Datos

# Parte 1

# Para ingresar el vector v= ( 1, 3, 5, 7, 9, 11, 13, 15), se puede utilizar 
# la funci?n seq(a,b,by=n) donde a es el valor inicial, b el valor final y 
# n el valor de separaci?n entre los n?meros del intervalo [a,b]

# obtener ayuda sobre la funci?n seq
# generar el vector v

# Respuesta
v<-seq(1,15,by=2)



# Para generar el vector u=(11,11,11,11,11,11,11), se puede usar la funci?n
# rep(n, r), donde n es el n?mero de la entrada que se repite y r es la 
# cantidad de veces que se repite n

# Obtener ayuda sobre rep
# generar el vector u

# Respuesta

u<-rep(11,7)

############################################################################
# Estructuras de datos: 2. Matrices
#
# las matrices son una extensi?n de los vectores n?mericos o de caracteres. 
# Se trata de vectores at?micos con dimensiones, es decir n?mero de filas y 
# de columnas. Al igual que en el caso de vectores, los elementos deben 
# ser del mismo tipo
############################################################################

# Crear una matriz vac?a con 2 filas y 3 columnas
# y almacenarlo en un objeto llamado m
# Respuesta

m<-matrix(nrow=2, ncol=3)

# ver el contenido de la matriz m
# Respuesta

m
[,1] [,2] [,3]
[1,]   NA   NA   NA
[2,]   NA   NA   NA

# Ver las dimensiones de  la matriz m
# Respuesta

dim(m)

# Ver la clase de m
# Respuesta

class(m)

# Ver el tipo de m
# Respuesta

typeof(m)

###########################################################################
# Crear una matriz de 2 filas y 4 columnas inicializada
# con los valores del 1 al 16 de 2 e 2, y almacenarla en el objeto n
#

# Respuesta

n<-matrix(seq(1,16, by=2), nrow=2, ncol=4)

# Ver el contenido de la matriz n
# Respuesta

n
[,1] [,2] [,3] [,4]
[1,]    1    5    9   13
[2,]    3    7   11   15

# Ver la clase de n
# Respuesta
class(n)


# Ver el tipo de los elementos de n
# Respuesta

typeof(n)

# Ver el tipo de los elementos de la  fila 1 
# Respuesta
typeof(n[1,])


# Ver el contenido de la fila 2 
# Respuesta

n[2,]

# Crear los siguientes vectores usando la funci?n seq
# vector1: 1,3,5,7,9,11 
# vector2: 2,4,6,8,10,12
# Respuesta
vector1<-seq(1,11,by=2)
vector2<-seq(2,12,by=2)


# Crear la matrix A de 2 x 6 combinando vector1 y vector2
# Respuesta

A<-rbind(vector1,vector2)

# Crear la matrix B de 6 x 2 combinando vector1 y vector2
# Respuesta

B<-cbind(vector1,vector2)

# Sumar A y la transpuesta de B
# Respuesta

A+t(B)

# Multiplicar A x B
# Respuesta

A*t(B)
#con el producto matricial si sale 
A%*%B 

# Multiplicar A por el escalar 3
# Respuesta

A*3
[,1] [,2] [,3] [,4] [,5] [,6]
vector1    3    9   15   21   27   33
vector2    6   12   18   24   30   36

# Verificar cu?les elementos de A son pares
# Respuesta


# ?Cu?ntos elementos de A son pares?
# Respuesta



# Extraer con una sola instrucci?n los elementos 
# A[1,1], A[1,3] y A[1,5]
# Respuesta

A[1,c(1,3,5)]


# Dadas las siguientes matrices
A<-matrix(c(1:12), nrow = 4 , ncol = 3)
B<-matrix(c(0,2,0,3,4,3,1,5,1,0,0,1),nrow = 3,ncol= 4)
I<- diag(3)
O<- matrix(c(rep(0,4)), ncol=2, nrow=2)

# Realizar las siguientes operaciones:
# Suma de matrices
# Respuesta

    

# Producto matricial AxB
# Respuesta

A*t(B)
[,1] [,2] [,3]
[1,]    0   10    0
[2,]    6   24   30
[3,]    3   35   11
[4,]    0    0   12
# Producto de la constante 2 y la matriz A
# Respuesta
A*2

[,1] [,2] [,3]
[1,]    2   10   18
[2,]    4   12   20
[3,]    6   14   22
[4,]    8   16   24

####################################################################
#
# LISTAS
#

# Dados los siguientes objetos, crear una lista L

x = c(45, 12, 56, 14, 16)
y = c("Coche", "Bicicleta")
z = matrix(1:12, ncol = 4)
# Respuesta
L =list(x,y,z)


# Ver contenido de L
L
# o para verlo más claro 
str(L)
# Respuesta

List of 3
$ : num [1:5] 45 12 56 14 16
$ : chr [1:2] "Coche" "Bicicleta"
$ : int [1:3, 1:4] 1 2 3 4 5 6 7 8 9 10 ...


# Observar los resultados de las siguientes instrucci?nes
# Primer objeto de la lista
L[1]

# Primer objeto de la lista
L[[1]]

# Primer elemento del primer objeto de la lista
L[[1]][1]
unlist(L[1])[1] # Equivalente

# Primera columna del tercer objeto
L[[3]][, 1]

# Segundo elemento de la primera columna
# del tercer objeto de la lista
L[[3]][, 1][2]
L[[3]][2, 1] # Equivalente

# Asignar nombre a los objetos de una lista
names(L)=c('A','B','C')
L

# Otra forma de acceder a los objetos es usando los nombres
# Primer objeto de la lista
L["A"]

# Primer objeto de la lista
L$A


# n?mero de objetos de la lista
length(L) 

# n?mero de elementos del primer objeto
length(L[[1]]) 


