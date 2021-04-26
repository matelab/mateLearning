
function playSound(e){
    const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`); // Primer parametro es el evento. Luego la funcion
    const key = document.querySelector(`.key[data-key="${e.keyCode}"]`);
    if (!audio) return // para la función para que no comiencen todos juntos
    audio.currentTime = 0; // rebobina al comienzo
    audio.play();
    key.classList.add('playing');
        
}


function removeTransition(e){
    if(e.propertyName !== 'transform') return; // corta si no hay una transformación
    this.classList.remove('playing')
}
const keys = document.querySelectorAll('.key');


keys.forEach(key => key.addEventListener('transitioned', removeTransition));
window.addEventListener('keydown', playSound)
    
