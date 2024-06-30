const cuadroTalla = document.getElementsByClassName('cuadro-tallas');
const warnTalla = document.getElementById('warnTalla');
const btnAgregar = document.getElementById('btnAgregar');

for (let i = 0; i < cuadroTalla.length; i++){
    cuadroTalla[i].addEventListener('click', ()=>{
        let talla = cuadroTalla[i].textContent;
        warnTalla.textContent = `Talla escogida: ${talla}`;
    });
};

