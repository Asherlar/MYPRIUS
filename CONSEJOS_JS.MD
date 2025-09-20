
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Una forma más limpia y eficiente sería definir clases CSS en el <head> y luego simplemente cambiar las clases de los elementos que van a ser requeridas.

¿POR QUÉ LAS IMÁGENES DE RUEDAS SE LLAMAN DESDE EL JS MEDIANTE .className EN VEZ DE .style?

El uso de .className en lugar de .style tiene varias ventajas importantes:

Eficiencia:
    Con .className modificamos todas las propiedades CSS de una vez
    Con .style tendríamos que modificar cada propiedad individualmente

Mantenibilidad:
    /* Un solo cambio de clase */
    element.className = "rueda-delantera-green";

    /* Versus múltiples cambios de estilo */
    element.style.backgroundImage = "url('images/rd_green.jpg')";
    element.style.width = "97px";
    element.style.height = "97px";
    element.style.position = "relative";
    element.style.left = "177px";
    element.style.top = "182px";

Separación de concerns:
    Los estilos se mantienen en el CSS
    La lógica se mantiene en el JavaScript
    Más fácil de mantener y modificar

Rendimiento:
    El navegador optimiza mejor los cambios de clase
    Reduce la cantidad de manipulaciones del DOM

Reutilización:
    Las clases pueden ser reutilizadas en diferentes elementos
    Los estilos están centralizados en un solo lugar

Por estas razones, usar .className es considerada una mejor práctica que manipular directamente los estilos con .style.

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

En HTML los comentarios deben usar la sintaxis <!-- para abrir y --> para cerrar, no // como en JavaScript.

Los comentarios en HTML:

✅ Correctos: <!-- comentario -->
❌ Incorrectos: // comentario
La sintaxis // solo funciona dentro de las etiquetas <script> o <style> porque ahí el contenido se interpreta como JavaScript o CSS respectivamente.

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

Operador Ternario vs IF-ELSE
El operador ternario (?:) es una forma más concisa de escribir una estructura if-else simple. Ambas formas son válidas:

Usando operador ternario (forma concisa):
Usando if-else (forma tradicional):
Ventajas del operador ternario:
Más corto: Ocupa menos líneas de código
Más legible: En casos simples de una sola asignación
Permite asignación directa: Se puede usar en una declaración const
Expresivo: Comunica claramente que es una decisión entre dos valores
Cuándo usar cada uno:
Operador ternario: Para asignaciones simples con solo dos opciones
if-else: Para lógica más compleja o cuando necesitas ejecutar múltiples líneas de código

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

