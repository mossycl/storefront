const selectEnvio = document.getElementById('selectEnvio');
const totalPrice = document.getElementById('totalPrice');
const btnComprar = document.getElementById('btnComprar');
const metodoEnvio = document.getElementById('metodoEnvio');
const listaPreciosEnvio = {
    1 : 3500,
    2 : 5000,
    3 : 4500,
    4 : 7000};
let intPrice = 0;
let envioPrice = listaPreciosEnvio[selectEnvio.value];
let precioProd = document.getElementsByClassName('precioProd');
metodoEnvio.setAttribute('value', selectEnvio.value)
let valList = Object.values(precioProd);

for (let i = 0; i < valList.length;i++) {
    const delChar = valList[i].textContent.replace('$','');
    const intVal = parseInt(delChar)
    intPrice += intVal
    intPrice += envioPrice
    totalPrice.textContent = `$ ${intPrice}`
};

selectEnvio.addEventListener('change', ()=>{
    if (intPrice != 0){
        intPrice -= envioPrice
        envioPrice = listaPreciosEnvio[selectEnvio.value]
        intPrice += envioPrice
        totalPrice.textContent = `$ ${intPrice}`
        metodoEnvio.setAttribute('value', selectEnvio.value)
    }
});

if (intPrice == 0) {
    btnComprar.disabled = true;
    selectEnvio.disabled = true;
}