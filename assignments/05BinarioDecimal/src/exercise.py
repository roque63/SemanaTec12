# Nombre:
# Matricula:
# Carrera:
# Fecha:
"""
Diseña y códifica un programa en Python que haga lo siguiente: 

Datos de Entrada:
El programa ya tiene 1 matriz con la información de las Series de una plataforma (ya no tienes que ingresarla)
- cada renglón de cada  matriz se organiza de la siguiente forma
       Nombre ,            clase,    código,      País,  duracion_min,        fecha,     calificación
['I Am Not an Animal', 'Animation',   '11.164',     'GB',      '349',         '10/05/04',          '9.5']
la matriz podría tener cualquier otra información - no siempre tendra la misma,
solo por cuestiones de tiempo se tienen esa opcion - debes programar tu solución para que
funcione para cualquier otro contenido de la matriz no únicamente para el actual,
de lo contrario TU SOLUCIÓN NO TENDRÁ valor, no SE TOMARA EN CUENTA (0 PTOS.).
Salidas:
El programa debe desplegar un listado como se muestra en el README.md del problema y en la parte inferior de este archivo,
 con una numeración de 1 hasta n(la cantidad de renglones de la matriz)
el programa debe tener la programación para calcular lo siguiente usando los datos de la matriz 
       - NOTA IMPORTANTE - debes diseñar tu solución para que funcione para cualquier otro contenido de la matriz 
         no únicamente para el actual, de lo contrario TU SOLUCIÓN NO SE TOMARÁ EN CUENTA(0 PTOS).
    - Contar y desplegar la cantidad de series para cada clase (TIP - contar la cantidad total de la misma clase, usa listas)
    - Calcula al momento de desplegar la frecuencia relativa = cantidad_total_misma_clase / total de elementos matriz
    - Contar y desplegar la cantidad total de elementos de la matriz.  
    - Calcular y desplegar el promedio de todas calificaciones
       (TIP - usa un acumulador - inicializar antes del ciclo e i
       
def main():
    series = [['I Am Not an Animal', 'Animation', '11.164', 'GB', '349', '10/05/04', '9.5'],
    ['Chernobyl', 'Drama', '46.429', 'US', '595', '06/05/19', '8.6'],
    ['Rick and Morty', 'Animation', '132.429', 'US', '1395', '02/12/13', '8.5'],
    ['Breaking Bad', 'Drama', '161.35', 'US', '3560', '20/01/08', '8.4'],
    ['Hunter x Hunter', 'Animation', '136.761', 'JP', '152', '02/10/11', '8.3'],
    ['Sherlock', 'Crime', '35.74', 'GB', '1885', '25/07/10', '8.3'],
    ['Planet Earth II', 'Documentary', '17.744', 'GB', '348', '06/11/16', '8.3'],
    ['Peaky Blinders', 'Crime', '59.824', 'GB', '572', '12/09/13', '8.3'],
    ['Stranger Things', 'Drama', '81.441', 'US', '2671', '15/07/16', '8.3'],
    ['DEATH NOTE', 'Animation', '56.677', 'JP', '599', '04/10/06', '8.3'],
    ['Avatar: The Last Airbender', 'Animation', '15.668', 'US', '552', '21/02/05', '8.3'],
    ['The Twilight Zone', 'Drama', '12.384', 'US', '295', '02/10/59', '8.3'],
    ['The Wire', 'Crime', '30.153', 'US', '869', '02/06/02', '8.3'],
    ['Gravity Falls', 'Animation', '40.365', 'US', '298', '15/06/12', '8.3'],
    ['The Sopranos', 'Drama', '25.922', 'US', '846', '10/01/99', '8.3'],
    ['Neon Genesis Evangelion', 'Animation', '29.844', 'JP', '233', '04/10/95', '8.3'],
    ['The Marvelous Mrs. Maisel', 'Comedy', '23.354', 'US', '105', '16/03/17', '8.3'],
    ['Young Justice', 'Animation', '30.096', 'US', '121', '26/11/10', '8.3'],
    ['Band of Brothers', 'Drama', '19.555', 'GB', '1500', '09/09/01', '8.2'],
    ['Futurama', 'Animation', '40.574', 'US', '919', '28/03/99', '8.2']]
    
    
    
    
    print("Total de series:", total)
    print("Promedio:", round(promedio, 2))
    
    
    
if __name__=='__main__':
    main()
    
    
"""
La salida del programa debe ser exactamente :
```
1 I Am Not an Animal Animation
2 Chernobyl Drama
3 Rick and Morty Animation
4 Breaking Bad Drama
5 Hunter x Hunter Animation
6 Sherlock Crime
7 Planet Earth II Documentary
8 Peaky Blinders Crime
9 Stranger Things Drama
10 DEATH NOTE Animation
11 Avatar: The Last Airbender Animation
12 The Twilight Zone Drama
13 The Wire Crime
14 Gravity Falls Animation
15 The Sopranos Drama
16 Neon Genesis Evangelion Animation
17 The Marvelous Mrs. Maisel Comedy
18 Young Justice Animation
19 Band of Brothers Drama
20 Futurama Animation
Animation 9 45.0%
Drama 6 30.0%
Crime 3 15.0%
Documentary 1 5.0%
Comedy 1 5.0%
Total de series: 20
Promedio: 8.38
```
"""
