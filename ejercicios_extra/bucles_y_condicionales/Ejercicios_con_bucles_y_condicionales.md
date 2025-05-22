## Sección 1: Primeros Pasos con Bucles (for y while)

1. Contar hasta 10: Imprime los números del 1 al 10 usando un bucle for.
2. Cuenta regresiva: Imprime los números del 10 al 1 usando un bucle for.
3. Números pares: Imprime todos los números pares del 0 al 20 usando un bucle for.
4. Suma básica: Calcula la suma de los números del 1 al 5 usando un bucle for y una variable acumuladora.
5. Multiplicación simple: Imprime la tabla de multiplicar del 5 (del 1 al 10) usando un bucle for.
6. Saludo repetido: Pide al usuario que ingrese su nombre y luego imprime "¡Hola, [nombre]!" tres veces usando un bucle for.
7. Contador con while: Imprime los números del 1 al 5 usando un bucle while.
8. Usuario y contraseña (intento único): Pide un nombre de usuario y una contraseña. Si ambos son "admin", imprime "Acceso concedido". Si no, imprime "Acceso denegado".
9. Entrada numérica: Pide al usuario que ingrese un número. Si el número es mayor que 10, imprime "Es un número grande". Si no, imprime "Es un número pequeño".
10. Par o impar: Pide al usuario un número. Determina si es par o impar y imprime el resultado.

---

## Sección 2: Combinando Bucles y Condicionales

1. Números positivos y negativos: Recorre los números del -5 al 5 usando un bucle for. Si el número es positivo, imprímelo con el mensaje "Es positivo". Si es negativo, imprímelo con "Es negativo". Si es cero, imprime "Es cero".
2. Contar vocales: Dada una palabra (puedes predefinirla, por ejemplo, "programacion"), cuenta cuántas vocales tiene usando un bucle for y condicionales.
3. Adivina el número (simple): Elige un número secreto (por ejemplo, 7). Pide al usuario que adivine el número. Si acierta, imprime "¡Correcto!". Si no, imprime "Incorrecto". (Usa un bucle while para que pueda intentar varias veces hasta acertar).
4. Validación de edad: Pide al usuario su edad. Si es menor de 18, imprime "Eres menor de edad". Si es 18 o más, imprime "Eres mayor de edad".
5. Días de la semana: Pide al usuario un número del 1 al 7. Imprime el día de la semana correspondiente (1 para Lunes, 2 para Martes, etc.). Si el número no está en el rango, imprime "Número inválido".
6. Cálculo de promedio: Pide al usuario que ingrese 5 números. Calcula el promedio de esos números usando un bucle for y una variable acumuladora.
7. Divisibles por 3 y 5: Imprime los números del 1 al 30. Si un número es divisible por 3, imprime "Fizz". Si es divisible por 5, imprime "Buzz". Si es divisible por ambos (3 y 5), imprime "FizzBuzz". Si no es divisible por ninguno, imprime el número.
8. Pirámide de asteriscos: Imprime una pirámide de asteriscos de 5 filas. La primera fila tendrá 1 asterisco, la segunda 2 con un espacio entre cada asterisco, y así sucesivamente. (Usa bucles anidados, si es necesario).
9. Contar elementos en una lista: Dada una lista de números (por ejemplo, [1, 5, 8, 12, 3]), cuenta cuántos números son mayores que 5 usando un bucle for y un condicional.
10. Búsqueda en una lista: Dada una lista de palabras (por ejemplo, ["manzana", "banana", "cereza"]), pide al usuario que ingrese una palabra. Si la palabra está en la lista, imprime "¡La encontré!". Si no, imprime "No está en la lista".

---

## Sección 3: Desafíos Adicionales (Un poco más de lógica)

1. Menú de opciones: Presenta al usuario un menú con opciones (ejemplo: "1. Saludar", "2. Despedirse", "3. Salir"). Usa un bucle while para que el menú se repita hasta que el usuario elija "3. Salir". Usa condicionales para ejecutar la acción correspondiente.
2. Contador regresivo con mensaje: Pide al usuario un número. Realiza una cuenta regresiva desde ese número hasta 0. Cuando llegue a 0, imprime "¡Despegue!".
3. Suma de números impares: Calcula la suma de todos los números impares del 1 al 100 usando un bucle for y un condicional.
4. Validación de número positivo: Pide al usuario que ingrese un número. Usa un bucle while para seguir pidiendo el número hasta que el usuario ingrese un número positivo.
5. Generador de contraseñas simple: Pide al usuario la longitud deseada para una contraseña (entre 6 y 12). Genera una contraseña aleatoria de esa longitud usando caracteres predefinidos (letras minúsculas, mayúsculas y números). (Este puede ser un poco más avanzado si no se han visto módulos, pero se puede hacer de forma simplificada).
6. Fibonacci (primeros N números): Pide al usuario un número N. Imprime los primeros N números de la secuencia de Fibonacci. (0, 1, 1, 2, 3, 5...).
7. Palíndromo: Pide al usuario una palabra. Determina si la palabra es un palíndromo (se lee igual de adelante para atrás que de atrás para adelante, ejemplo: "reconocer").
8. Factorial: Pide al usuario un número. Calcula su factorial. El factorial de un número n es el producto de todos los enteros positivos menores o iguales a n. (Ejemplo: 5! = 5 × 4 × 3 × 2 × 1 = 120).
9. Juego "Piedra, Papel o Tijera" (básico): Haz un juego básico donde el usuario elija "piedra", "papel" o "tijera", y el programa elija aleatoriamente. Luego, determina el ganador. (Necesitará el módulo random).
10. Cajero automático simple: Simula un cajero automático. Ten un saldo inicial. Permite al usuario "depositar" y "retirar" dinero. Valida que no se pueda retirar más dinero del que hay en el saldo. Usa un bucle while para que el cajero esté activo hasta que el usuario decida salir.
