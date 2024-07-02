// static/carrito/js/carrito.js

document.addEventListener('DOMContentLoaded', function() {
    const carritoData = document.getElementById('carrito-data');
    const modificarUrl = carritoData.dataset.modificarUrl;
    const eliminarUrl = carritoData.dataset.eliminarUrl;
    const csrfToken = carritoData.dataset.csrfToken;

    window.cambiarCantidad = function(productoId, cambio) {
        fetch(modificarUrl, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrfToken
            },
            body: JSON.stringify({ productoId: productoId, cambio: cambio })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                location.reload();  // Recarga la página para ver los cambios
            } else {
                alert(data.message);  // Muestra un mensaje si hay un error
            }
        });
    };

    window.eliminarProducto = function(productoId) {
        fetch(eliminarUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({productoId: productoId})
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                location.reload();  // Recarga la página para reflejar los cambios
            } else {
                alert(data.message);  // Muestra un mensaje si hay un error
            }
        });
    };

    window.comprar = function() {
        alert('Compra realizada con éxito!');
    };
});
