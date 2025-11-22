# Cálculos básicos en R
2*3
10-3

# Asignación de valores a una variable
x<-2*3

# Consultando el contenido de un objeto
x

# Creando un vector
myvector <- c(8, 6, 9 ,10 ,5)

# Consultando un vector
myvector

# Accediendo a un elemento de un vector
myvector[4]

# Definiendo una lista
mylist <- list(seq='GATTACA', seq2='acgttaacga', myvector)

# Accediendo a elementos de la lista
mylist$seq
mylist$seq2
mylist[[2]]
mylist[[3]]

# Elementos nombrados de una lista
attributes(mylist)

# Tablas
mynames <- c("Mary", "John", "Ann", "Sinead", "Joe", "Mary", "Jim", "John", "Simon")
table(mynames)

# Creando un objeto tabla
mytable <- table(mynames)

# Accediendo a una tabla
mytable[[4]]
mytable[['John']]

# Funciones en R
log10(100)

# Ayuda en R
help('log10')

help.search('desviation')
RSiteSearch('desviation')

# Cálculos sobre objetos
mean(myvector)

# Creando una función
myfunction <- function(x) {return(20+x*x)}

# Ejecutando la función
myfunction(10)
myfunction(25)