'''
NAME
    Contenido_ATCG.py

VERSION
    2.0

AUTHOR
    Daniela Goretti Castillo León <danigore22@gmail.com>

DESCRIPTION
    Este programa lee una secuencia de ADN dada por el usuario y cuenta el contenido de las bases A, C, G y T que tiene
    esa secuencia.

CATEGORY
    Análisis de secuencias de ADN

USAGE
    Contenido_ATCG.py [sin opciones]
  - El usuario da la secuencia que se va a analizar y al leerse se imprime el contenido de las bases en la pantalla.

ARGUMENTS
    [sin argumentos]

INPUT
    Secuencia dada por el usuario en la consola.

OUTPUT
    Cantidad de A:  7 , cantidad de C:  5 , cantidad de G:  7 , cantidad de T:  6 (los valores de las bases dependen de
    la secuencia que se haya otorgado).


EXAMPLES
    Example 1: Se tiene la secuencia AAGGAUGTCGCGCGTTATTAGCCTAA (que representa el input del programa), la cual es
    anotada por el usuario y es guardada en una variable llamada adn. Posteriormente se calcula el contenido de cada
    base mediante las variables cantidad_de_A (que cuenta el número de A's que hay en la secuencia), cantidad_de_C (que
    cuenta el número de C's), cantidad_de_T (que cuenta el número de bases T), y cantidad_de_G (que cuenta el número de
    G's). Estas variables utilizan el método .count en la variable dna para contar cuántas veces aparece cada una de las
    bases. Al final, se imprime el contenido de adeninas, citosinas, guaninas y timinas que hay en la secuencia:
    Cantidad de A:  7 , cantidad de C:  5 , cantidad de G:  7 , cantidad de T:  6

GITHUB LINK
    La liga de Github del programa es: https://github.com/Danigore25/python_class/blob/master/src/Contenido_ATCG.py

'''

# Este programa calcula el contenido de las bases 'A', 'C', 'T' y 'G' de una secuencia.

print('Por favor escriba la secuencia de DNA: \n')   # En esta parte se pide al usuario la secuencia de DNA que se va
# a analizar.
dna = input()    # dna es una variable que guarda la secuencia que escribe el usuario.
cantidad_de_A = (dna.count('A'))   # La variable cantidad_de_A cuenta con el método count que permite contar el
# contenido de 'A' que hay en la secuencia.
cantidad_de_C = (dna.count('C'))    # La variable cantidad_de_C usa el método count para contar las 'C' que tiene la
# secuencia.
cantidad_de_T = (dna.count('T'))    # La variable cantidad_de_T calcula el contenido de 'T' que hay en la secuencia.
cantidad_de_G = (dna.count('G'))    # La variable cantidad_de_G cuenta las 'G' que se encuentran en la secuencia.

print("Cantidad de A: ", cantidad_de_A, ", cantidad de C: ", cantidad_de_C, ", cantidad de G: ", cantidad_de_G,
      ", cantidad de T: ", cantidad_de_T)
# Al final se imprime el contenido de cada base que existe en la secuencia.
