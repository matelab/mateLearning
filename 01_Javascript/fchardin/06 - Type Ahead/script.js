const endpoint = 'https://gist.githubusercontent.com/Miserlou/c5cd8364bf9b2420bb29/raw/2bf258763cdddd704f8ffd3ea9a3e81d25e2c6f6/cities.json';

const cities = [];
//trayendo data con fetch, es nativo del navegador
//traemos blob (datos, puede ser cualquier nombre)
//usamos el método json para cambiar el formato. esto nos devuelve otra promesa
//
const prom = fetch(endpoint)
    .then(blob => blob.json())
//hacemos spread para poder pushear el array deconstruido y que no se anide un array dentro de otro
    .then(data => cities.push(...data))

function findMatches(wordToMatch, cities) {
    return cities.filter(place => {
        //acá nos fijamos si la ciudad o estado coincide con lo que se buscó
        //primero armamos una constante para revisar coincidencias
        // g singifica global e i que es insensible a mayúsculas y minúsculas
        const regex = new RegExp(wordToMatch, 'gi')
        return place.city.match(regex) || place.state.match(regex)
    })
}

function numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',');
}

function displayMatches() {
    const matchArray = findMatches(this.value, cities)
    //console.log(matchArray)
    const html = matchArray.map(place => {
        const regex = new RegExp(this.value, 'gi');
        const cityName = place.city.replace(regex, `<span class="hl">${this.value}</span>`)
        const stateName = place.state.replace(regex, `<span class="hl">${this.value}</span>`);
        return `
        <li>
            <span class="name">${cityName}, ${stateName}</span>
            <span class="population">${numberWithCommas(place.population)}</span>
        </li>
        `
        //juntamos el array en un solo string
    }).join('');
    //pasamos la data a suggestions
    suggestions.innerHTML = html;
}

const searchInput = document.querySelector('.search');
const suggestions = document.querySelector('.suggestions');

//dispara la función cuando se dispara el evento de clickear fuera del campo de búsqueda
searchInput.addEventListener('change', displayMatches)
//también llama la función cuando se deja de presionar una tecla del teclado al tipear
searchInput.addEventListener('keyup', displayMatches)
