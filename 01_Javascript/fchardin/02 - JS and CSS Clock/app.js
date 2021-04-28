const secondsHand = document.querySelector('.second-hand')
const minutesHand = document.querySelector('.min-hand')
const hoursHand = document.querySelector('.hour-hand')
const secondDig = document.querySelector('.second-dig')
const minutesDig = document.querySelector('.min-dig')
const hoursDig = document.querySelector('.hour-dig')
// faltaría debuggear cuando las agujas pasan por las 12

function setDate() {
      const now = new Date();
      const seconds = now.getSeconds();
      const minutes = now.getMinutes();
      const hours = now.getHours();

      // reloj digital
      secondDig.textContent = (seconds < 10) ? "0" + seconds : seconds;
      minutesDig.textContent = minutes + " :";
      hoursDig.textContent = hours + " :";

      // reloj analógico 

      // transformamos los segundos a grados y sumamos 90 grados para acomodar el offset que dimos en la clase hand para pasarl las agujas de las 9 a las 12
      const secondsDegrees = ((seconds / 60) * 360) + 90;
      secondsHand.style.transform = `rotate(${secondsDegrees}deg`;

      
      const minutesDegrees = (( minutes / 60 ) * 360) + 90;
      minutesHand.style.transform = `rotate(${minutesDegrees}deg`; 

      const hoursDegrees = (( hours / 12) * 360) + 90;
      hoursHand.style.transform = `rotate(${hoursDegrees}deg`;

    }
    setInterval(setDate, 1000);
