const inputs = document.querySelectorAll('.controls input');

function handleUpdate(){
    console.log(this.value);
}

// We loop over all the inputs
inputs.forEach(input => input.addEventListener('change', handleUpdate));