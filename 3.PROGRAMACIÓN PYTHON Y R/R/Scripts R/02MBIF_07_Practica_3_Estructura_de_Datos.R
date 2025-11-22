# Pr?ctica 3 - Estructuras de Datos
# Parte 1

# No es usual crear un data frame a mano pero lo haremos para 
# entender en qu? consiste esta estructura de datos

# Crear un data frame (personal.df) para almacenar los siguientes datos:
# Maria,Martinez,54,M
# Pedro,Rodriguez,25,H
# Juan Carlos,Martin,45,H
# Ana Maria,Gomez,28,M
# Marian,Fernandez,34,M
# Emely,Arizaleta,61,M

# los campos o columnas del data frame (personal.df) ser?n identificados como:
# nombre, apellido, edad, sexo

personal.df <- data.frame(nombre=c("Maria","Pedro","Juan Carlos","Ana Maria","Marian","Emely"),
                          apellido=c("Martinez","Rodriguez","Martin","Gomez","Fernandez","Arizaleta"),
                          edad=c(54,25,45,28,34,61),
                          sexo=c("M","H","H","M","M","M"))


# Explorar las caracter?sticas de personal.df usando funciones como class,
# typeof, str, summary, head, dim, colnames, rownames




# Explorar las caracter?sticas de cada uno de los campos del data frame
# Revisar funciones sapply o lapply
# Como argumentos pasamos el nombre del objeto y la funci?n que queremos 
# aplicar

lapply(personal.df,class)


# Despu?s de un tiempo de la creaci?n de personal.df se da cuenta que necesita
# agregar un nuevo campo (columna) a su data frame
# estado civil con los siguientes valores:
# (C,C,D,S,C,V)
# Agregar el nuevo campo a personal.df


personal.df$estado_civil = c("C","C","D","S","C","V")
print(personal.df)



# Creaci?n de un data frame (personal.df1) a partir de un archivo de tipo texto
# 
# Revisar las funciones read.csv() y read.table()
# El archivo a usar para la creaci?n del data frame es personal.csv
# Antes de crear el data frame es conveniente ver la estructura del
# archivo personal: 
# - tiene o no cabecera que identifica cada campo 
# - separador de campos

personal.df1<-read.csv('/Users/marta/Desktop/3.PROGRAMACIÓN PYTHON Y R/R/Archivos Datos/personal.csv', header=TRUE, sep=",", quote="\"", dec=".", fill=FALSE)
print(personal.df1)

personal.df1<-data.frame(personal.df1)


# Visualizar el objeto creado

print(personal.df1)


# Buscar todos los registros que cumplen con la siguiente condici?n
# Mujer de m?s de 40 a?os



# ?Cu?ntas mujeres cumplen con esta condici?n?



# Usar la funci?n summary() con el personal.df1 y revisar que
# informaci?n nos provee

summary(personal.df1)
nombre            apellido              edad           sexo           estado_civil      
Length:6           Length:6           Min.   :25.00   Length:6           Length:6          
Class :character   Class :character   1st Qu.:29.50   Class :character   Class :character  
Mode  :character   Mode  :character   Median :39.50   Mode  :character   Mode  :character  
                                      Mean   :41.17                                        
                                      3rd Qu.:51.75                                        
                                      Max.   :61.00 

# Crear un data frame cruce1.df con los datos del archivo
# CruceCovid_1.csv

cruce1.df<-read.csv('/Users/marta/Desktop/3.PROGRAMACIÓN PYTHON Y R/R/Archivos Datos/CruceCovid_1.csv', header=TRUE, sep=",", quote="\"", dec=".", fill=FALSE)
> print(cruce1.df)


# Parte 2 - Factores

# Permiten almacenar datos como niveles

# El data frame personal.df1 contiene el campo sexo y estado_civil que 
# podemos manejar como factores

# Convertir el campo sexo del data frame personal.df1 al tipo factor



# Ver los niveles del campo sexo y el n?mero de niveles



# Ventaja de trabajar con un factor a la hora de graficar

boxplot(personal.df1$edad ~ personal.df1$sexo)


