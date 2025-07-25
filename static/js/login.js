document.querySelector('form').addEventListener('submit', function(e) {
        // NO hacemos e.preventDefault(), así Django sigue con su flujo normal
        const username = document.getElementById('username').value;
        const password = document.getElementById('password').value;

        // Hacemos la petición a la API para obtener el token, pero no detenemos el submit
        fetch('/api/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ username, password })
        })
        .then(response => response.json())
        .then(data => {
            if (data.access) {
                localStorage.setItem('token', data.access);
            }
            // No mostramos errores aquí, porque Django ya los maneja
        })
        .catch(() => {
            // No hacemos nada, Django maneja los errores
        });
        // El formulario sigue su curso normal
    });