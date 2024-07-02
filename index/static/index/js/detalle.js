const cuadroTalla = document.getElementsByClassName('cuadro-tallas');
const warnTalla = document.getElementById('warnTalla');
const btnAgregar = document.getElementById('btnAgregar');

for (let i = 0; i < cuadroTalla.length; i++){
    cuadroTalla[i].addEventListener('click', ()=>{
        let talla = cuadroTalla[i].textContent;
        warnTalla.textContent = `Talla escogida: ${talla}`;
    });
};

// btnAgregar.addEventListener('click', () =>{
//     const xhr = new XMLHttpRequest();
//     const nombreProd = document.getElementById('detalleNombre').textContent;
//     xhr.open("POST", "")
//     xhr.setRequestHeader("Content-Type", "application/json");
//     xhr.send(JSON.stringify(nombreProd));

// })
