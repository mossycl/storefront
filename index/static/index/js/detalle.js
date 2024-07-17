const cuadroTalla = document.getElementsByClassName('cuadro-tallas');
const warnTalla = document.getElementById('warnTalla');
const tallaForm = document.getElementById('tallaForm');
const btnAgregar = document.getElementById('btnAgregar');
const cantidadItem = document.getElementById('cantidadItem');

for (let i = 0; i < cuadroTalla.length; i++){
    cuadroTalla[i].addEventListener('click', ()=>{
        let talla = cuadroTalla[i].textContent;
        tallaForm.setAttribute('value',parseInt(talla));
        warnTalla.style.color = "";
        warnTalla.textContent = `Talla escogida: ${talla}`;
    });
};

btnAgregar.addEventListener('click', (e)=>{
    if (tallaForm.getAttribute('value') === null){
        e.preventDefault()
        warnTalla.style.color = 'red';
        warnTalla.textContent = 'Por favor escoja una talla';
    }
})