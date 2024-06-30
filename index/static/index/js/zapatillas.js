    // Checks de marca
    const nikeCheck = document.getElementById('nikeCheck');
    const adidasCheck = document.getElementById('adidasCheck');
    const vansCheck = document.getElementById('vansCheck');
    const dcCheck = document.getElementById('dcCheck');
    const skechersCheck = document.getElementById('skechersCheck');
    const pumaCheck = document.getElementById('pumaCheck');

    nikeCheck.addEventListener('click', () =>{
        filterByBrand('Nike');
    });

    adidasCheck.addEventListener('click', () =>{
        filterByBrand('Adidas');
    });

    vansCheck.addEventListener('click', () =>{
        filterByBrand('Vans');
    });

    dcCheck.addEventListener('click', () => {
        filterByBrand('DC');
    });

    skechersCheck.addEventListener('click', () => {
        filterByBrand('Skechers');
    });

    pumaCheck.addEventListener('click', () =>{
        filterByBrand('Puma');
    });

    // Checks de Precio

    const precio1 = document.getElementById('precioRadio1');
    const precio2 = document.getElementById('precioRadio2');
    const precio3 = document.getElementById('precioRadio3');
    const precio4 = document.getElementById('precioRadio4');
    const precio5 = document.getElementById('precioRadio5');
    const precio6 = document.getElementById('precioRadio6');

    precio1.addEventListener('click', () =>{
        const range = [0,30000];
        filterByPrice(range);
    });

    precio2.addEventListener('click', () =>{
        const range = [30001,50000];
        filterByPrice(range);
    });

    precio3.addEventListener('click', () =>{
        const range = [50001,70000];
        filterByPrice(range);
    });

    precio4.addEventListener('click', () =>{
        const range = [70001,90000];
        filterByPrice(range);
    });

    precio5.addEventListener('click', () =>{
        const range = [90001,110000];
        filterByPrice(range);
    });

    precio6.addEventListener('click', () =>{
        const range = [110001,999999];
        filterByPrice(range);
    });

    const filterByBrand = (attribute) =>{
        let filter = document.getElementsByClassName('prod');
        let valList = Object.values(filter);

        for (let i = 0; i < valList.length; i++) {
            if (valList[i].getAttribute("name") != attribute){
                valList[i].style.display = "none";
            } else {
                valList[i].style.display = "";
            };
        };
    };

    const filterByPrice = (priceRange) =>{
        const prodFilter = document.getElementsByClassName('prod');
        let prodList = Object.values(prodFilter);
        let filter = document.getElementsByClassName('precio');
        let valList = Object.values(filter);

        for (let i = 0; i < valList.length;i++){
            let strPrice = valList[i].textContent.substring(1);
            let price = parseInt(strPrice);

            if (price >= priceRange[0] && price <= priceRange[1]){
                prodList[i].style.display = "";
            } else {
                prodList[i].style.display = "none";
            };
        };
    };