// Reto 5: Buscar listas de números en un texto usando regex en Java
// Paso a paso:
// 1. Leer el texto de entrada.
// 2. Definir una expresión regular para encontrar listas de números (ej: [1, 2, 3]).
// 3. Buscar todas las listas en el texto.
// 4. Imprimir los resultados.

import java.util.regex.*;

public class Reto5 {
    public static void main(String[] args) {
        String texto = "Hoy en clase nos dividieron en grupos, el mío estaba formado por [3, 5, 7], mientras que el de mi amigo tenía a [2, 4, 6, 8]. Al final, todos terminamos trabajando juntos y el profesor nos calificó con [9, 10].";
        // Expresión regular para listas de números
        String patron = "\\[\\s*\\d+(?:\\s*,\\s*\\d+)*\\s*\\]";
        Pattern pattern = Pattern.compile(patron);
        Matcher matcher = pattern.matcher(texto);
        System.out.print("Listas encontradas: ");
        while (matcher.find()) {
            System.out.print(matcher.group() + " ");
        }
        System.out.println();
        // Paso a paso:
        // 1. Cambia el texto de prueba.
        // 2. Modifica la expresión regular si es necesario.
        // 3. Ejecuta el programa y observa los resultados.
    }
}
