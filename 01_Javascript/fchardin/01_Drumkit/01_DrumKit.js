function playSound(e) {
    const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`)
    const key = document.querySelector(`.key[data-key="${e.keyCode}"]`)
    const body = document.querySelector('body')

    if(!audio) return; // Termina la función si el elemento no coincide con una tecla asociada a un sonido
    audio.currentTime= 0; // Revobina el audio 
    audio.play() // Reproduce el audio
    key.classList.add('playing') // agrega la clase playing
    body.classList.add('keyDown')
    
}

function removeTransition(e) {
    const body = document.querySelector('body')
    if(e.propertyName !== 'transform') return; // salta esa parte de la funcion si no es transform
    this.classList.remove('playing')
    body.classList.remove('keyDown')
}

const keys = document.querySelectorAll('.key')
keys.forEach(key => key.addEventListener('transitionend', removeTransition))

window.addEventListener('keydown', playSound)