async function cargarPerfil() {
        const token = localStorage.getItem('token');
        if (!token) {
            document.getElementById('welcomeTitle').textContent = 'No autenticado';
            document.getElementById('profileMessage').textContent = 'Por favor, inicia sesión.';
            return;
        }
        try {
            const resp = await fetch('/api/perfil/', {
                headers: {
                    'Authorization': 'Bearer ' + token
                }
            });
            if (!resp.ok) {
                document.getElementById('welcomeTitle').textContent = 'Error de autenticación';
                document.getElementById('profileMessage').textContent = 'Token inválido o expirado. Inicia sesión de nuevo.';
                localStorage.removeItem('token');
                return;
            }
            const perfil = await resp.json();
            document.getElementById('welcomeTitle').textContent = `¡Bienvenido ${perfil.username}!`;
            document.getElementById('username').textContent = perfil.username;
            document.getElementById('firstName').textContent = perfil.first_name;
            document.getElementById('lastName').textContent = perfil.last_name;
            document.getElementById('email').textContent = perfil.email;
            document.getElementById('profileData').style.display = 'block';
            document.getElementById('profileMessage').textContent = '';
        } catch (err) {
            document.getElementById('welcomeTitle').textContent = 'Error de conexión';
            document.getElementById('profileMessage').textContent = 'No se pudo cargar el perfil.';
        }
    }
    window.onload = cargarPerfil;