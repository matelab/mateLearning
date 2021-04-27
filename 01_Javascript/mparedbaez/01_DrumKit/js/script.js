/**Función para reproducir sonido */
function playSound(e) {
    const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);
    const key = document.querySelector(`.key[data-key="${e.keyCode}"]`);
    //para la función 
    if (!audio) return;
    audio.currentTime = 0;
    audio.play();
    key.classList.add('playing');
}
/**Para Remover la clases */
function removeTransition(e) {
    //para saltear si no hay transición
    if (e.propertyName !== 'transform') return;
    this.classList.remove('playing');
}
/**Seleccionamos todas las keys */
const keys = document.querySelectorAll('.key');

keys.forEach(key => key.addEventListener('transitionend', removeTransition));

/** */
window.addEventListener('keydown',playSound)