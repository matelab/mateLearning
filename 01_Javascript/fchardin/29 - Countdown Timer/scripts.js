let countdown
const timerDisplay = document.querySelector('.display__time-left')
const endTime = document.querySelector('.display__end-time')
let am = true
const timeFormatToggle = document.getElementById('timeFormatToggle')
const buttons = document.querySelectorAll('[data-time]')



function timer(seconds) {
    // limpiamos otros timers existentes
    clearInterval(countdown)

    const now = Date.now()
    const then = now + seconds * 1000
    //llamamos una vez el display sino empieza de un segundo más tarde de lo indicado por el setInterval
    displayTimeLeft(seconds)
    displayEndTime(then)
    
    countdown = setInterval(() => {
        const secondsLeft = Math.round((then - Date.now()) / 1000)
        //chequeamos si tiene que frenar (sino se va a negativos)
        if(secondsLeft < 0) {
            clearInterval(countdown)
            return
        }
        displayTimeLeft(secondsLeft)
    }, 1000)
    
}
//mostrarlo
function displayTimeLeft(seconds) {
    const minutes = Math.floor(seconds / 60)
    const remainderSeconds = seconds % 60
    const display = `${minutes} : ${remainderSeconds < 10 ? '0' : ''}${remainderSeconds}`
    document.title =  display

    timerDisplay.textContent = display
    //console.log({minutes}, {remainderSeconds})
}

function displayEndTime(timestamp) {
    //date.now son milisegundos desde el año 0 hasta ahora
    //con  new.Date(numerodems) tenemos la fecha de hoy
    const end = new Date(timestamp)
    const hour = end.getHours()
    const minutes = end.getMinutes()

    //para horas con am/pm
    const adjustedHour = hour > 12 ? hour - 12 : hour
    
    if(am == true) {
        endTime.textContent = 
        `Be back at ${adjustedHour} : ${minutes < 10 ? '0' : ''}${minutes} ${hour < 12 ? 'AM' : 'PM'}`
    } else {
        endTime.textContent = `Be back at ${hour} : ${minutes < 10 ? '0' : ''}${minutes}`
    }

    
}
// terminar funcion para que se pueda cambiar el formato de horario del 
// endTime y que cambie el display 
// revisar la función de arriba
function handleClick() {
    am = !am
    this.textContent  == '12' ? this.textContent = '24' : this.textContent  = '12';
    console.log(am)
    
    //this.textContent = '12H'
    //this.classList.remove('H24')
}
timeFormatToggle.addEventListener('click', handleClick)


function startTimer() {
    const seconds =  parseInt(this.dataset.time)
    //console.log(this.dataset.time)
    timer(seconds)
}

buttons.forEach(button => button.addEventListener('click', startTimer))

document.customForm.addEventListener('submit', function(e) {
    e.preventDefault()
    const mins = this.minutes.value
    console.log(mins)
    timer(mins * 60)
    this.reset()
})