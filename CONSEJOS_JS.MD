
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