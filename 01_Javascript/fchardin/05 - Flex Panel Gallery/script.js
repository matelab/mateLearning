const panels = document.querySelectorAll('.panel');

function toggleOpen() {
    this.classList.toggle('open');
}

function toggleActive(e) {
    //chequea si tiene la propiedad contiene la palabra flex (en safari se llama flex y en otros navegadores flex-grow)
    if(e.propertyName.includes('flex')) {
        this.classList.toggle('open-active');
    }
}
//Escucha el click y ejecuta toggleOpen
panels.forEach(panel => panel.addEventListener('click', toggleOpen));
//Espera que termine la transición y ejecuta toggleActive
panels.forEach(panel => panel.addEventListener('transitionend', toggleActive));