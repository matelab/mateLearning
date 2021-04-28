/**Seleccionamos los inputs */
const inputs = document.querySelectorAll('.controls input');

/**Actualizar*/
function handleUpdate() {
    /**Guardamos la unidad desde datasets */
    const suffix = this.dataset.sizing || '';
    /**Seteamos el valor a la propiedad de style */
    document.documentElement.style.setProperty(`--${this.name}`, this.value + suffix)
}

/**Recorrer todos los inputs  y agregamos un Listener al cambiar el valor y al mover*/
inputs.forEach(input => input.addEventListener('change', handleUpdate));
inputs.forEach(input => input.addEventListener('mousemove', handleUpdate));