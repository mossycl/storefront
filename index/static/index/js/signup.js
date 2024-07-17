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
const warnDiv = document.getElementById('warnDiv');
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

const showAlert = (message) =>{
    const warn = document.createElement('p');
            warn.classList.add('alert');
            warn.classList.add('error');
            warn.classList.add('kanit-regular');
            warn.textContent = message;
            warnDiv.appendChild(warn);

            setTimeout(() =>{
                warn.remove();
            },5000);
}

btnSubmit.addEventListener('click', (e) =>{
    for (let i = 0; i< elm.length; i++){
        if (elm[i].value === ""){
            e.preventDefault();
            elm[i].style.borderColor = "#ff416c";
            showAlert("Tiene campos sin completar");
            return
        } else {
            elm[i].style.borderColor = "";
        };
    };
    if (password.value != rPassword.value) {
        e.preventDefault();
        showAlert("Las contraseñas no coinciden");
        return
    };
    if (rut.value.indexOf('-') == -1){
        e.preventDefault();
        showAlert("Debe agregar el guión '-'")
        return
    };
    if (rut.value.length < 9) {
        e.preventDefault();
        showAlert("El RUN no es válido")
        return
    };
});
