const region = document.getElementById('region');
const comunas = document.getElementsByClassName('comuna');

region.addEventListener('change', () =>{
    filterCitiesbyRegion(region.value);
});


const filterCitiesbyRegion = (region) =>{
    for (let i = 0; i < comunas.length;i++){
        if (comunas[i].getAttribute('name') === region) {
            comunas[i].style.display = "";
        } else {
            comunas[i].style.display = "none";
        };
    };
};

// Checks de datos del formulario

const email = document.getElementById('email');
const password = document.getElementById('password');
const rPassword = document.getElementById('rPassword');
const rut = document.getElementById('rut');
const pNombre = document.getElementById('pNombre');
const sNombre = document.getElementById('sNombre');
const aPaterno = document.getElementById('aPaterno');
const aMaterno = document.getElementById('aMaterno');
const direccion = document.getElementById('direccion');
const comList = document.getElementById('comuna');
const btnSubmit = document.getElementById('btnSubmit');
const warn = document.getElementById('warn');
let elm = [];

elm.push(email);
elm.push(password);
elm.push(rPassword);
elm.push(rut);
elm.push(pNombre);
elm.push(sNombre);
elm.push(aPaterno);
elm.push(aMaterno);
elm.push(direccion);
elm.push(region);
elm.push(comList);

btnSubmit.addEventListener('click', (e) =>{
    for (let i = 0; i< elm.length; i++){
        if (elm[i].value === ""){
            e.preventDefault();
            elm[i].style.borderColor = "#ff416c";
            warn.style.color = "#ff416c"
            warn.textContent = "Tiene campos sin completar";
            return
        } else {
            elm[i].style.borderColor = "";
            warn.style.color = "";
        };
    };
    if (password.value != rPassword.value) {
        e.preventDefault();
        warn.textContent = "Las contraseñas no coinciden";
        return
    };
    if (rut.value.indexOf('-') == -1){
        e.preventDefault();
        warn.textContent = "Debe agregar el guión '-'"
        return
    };
    if (rut.value.length < 9) {
        e.preventDefault();
        warn.textContent = "El RUN no es válido";
        return
    };
});
