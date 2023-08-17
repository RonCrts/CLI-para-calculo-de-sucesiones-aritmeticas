# CLI-para-calculo-de-sucesiones-aritmeticas
Una sencilla aplicación de CLI que funciona para calculas sucesiones aritméticas mediante consola usando un script de python.

COMANDO
1) set-sequence: debe incluir los siguientes argumentos --n, --a1, --d, --nth-term

--n refiere al numero de terminos de la sucesion 
--a1 refiere al primer termino de la sucesion 
--d refiere a la diferencia comun de la sucesion 
--nth-term refiere al valor que se utilizara para mostrar al termino que se encuentre en la posicion que especifica este valor dentro de la sucesion 

El script retornara por consola la sucesion, si esta es aritmetica, si es ascendente, si es descendente, el termino en la posicion n y la suma de todos los terminos de la sucesion (ademas se mostrara el tiempo de ejecucion de cada uno de los procesos).

Ejemplo: 
ejecuto el siguiente comando: python arithmetic_sequence.py set-sequence --n 20 --a1 45 --d 12 --nth-term 56 y la consola devuelve esto

Sequence: [ 45.  57.  69.  81.  93. 105. 117. 129. 141. 153. 165. 177. 189. 201.
 213. 225. 237. 249. 261. 273.]
Execution time: 0.0052013397216796875 seconds
Is Arithmetic: True
Execution time: 0.2815861701965332 seconds
Is Ascending: True
Execution time: 0.26279163360595703 seconds
Is Descending: False
Execution time: 0.2521700859069824 seconds
56th term: 705.0
Execution time: 0.35741448402404785 seconds
Sum of terms: 2730.0
Execution time: 0.20521259307861328 seconds
