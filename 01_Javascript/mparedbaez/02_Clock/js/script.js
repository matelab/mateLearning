
//Obtenemos las agujas de los segundos
const secondHand = document.querySelector('.second-hand');
//Obtenemos las agujas de los minutos
const minsHand = document.querySelector('.min-hand');
//Obtenemos las agujas de las Horas
const hourHand = document.querySelector('.hour-hand');
function setDate() {
    //Fecha actual
    const now = new Date();
    //Segundos 
    const seconds = now.getSeconds();
    //Pasamos a grados los segundos
    const secondsDegrees = ((seconds /60) * 360);
    //Genera el movimiento
    secondHand.style.transform = `rotate(${secondsDegrees}deg)`;

    //Minutos
    const mins = now.getMinutes();
    //Pasamos a grados los minutos
    const minsDegrees = ((mins / 60) * 360) + ((seconds/60)*6) + 90;
    //Genera el movimiento
    minsHand.style.transform = `rotate(${minsDegrees}deg)`;3

    //Horas
    const hour = now.getHours();
    //Pasamos a grados los minutos
    const hourDegrees = ((hour / 12) * 360) + ((mins/60)*30) + 90;
    //Genera el movimiento
    hourHand.style.transform = `rotate(${hourDegrees}deg)`;

}

setInterval(setDate, 1000);
