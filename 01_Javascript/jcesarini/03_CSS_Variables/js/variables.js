const inputs = document.querySelectorAll('.controls input');

function handlelUpdate(){
    const suffix =this.dataset.sizing||'';
    document.documentElement.style.setProperty(`--${this.name}`, this.value + suffix);

}

inputs.forEach(input => input.addEventListener('change', handlelUpdate));
inputs.forEach(input => input.addEventListener('mousemove', handlelUpdate));