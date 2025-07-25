#  Proyecto Django

Este proyecto es una aplicación web construida con **Django** que implementa autenticación de usuarios (login, registro y perfil) y cuenta con documentación de la API utilizando **Swagger**.

---

##  Tecnologías utilizadas

- [Python 3.13](https://www.python.org/)
- [Django 5.2.4](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/)
- [drf-yasg / drf-spectacular] para documentación de API
- SQLite (base de datos por defecto)

---

## Estructura del proyecto

La estructura principal del proyecto es la siguiente:

```
PythonProject/
 API/                 # Configuración global (settings, urls, wsgi, asgi)
 usuarios/            # Aplicación de usuarios (vistas, urls, modelos)
 templates/           # Plantillas HTML (login, register, profile)
 static/              # Archivos estíticos (css, js)
 staticfiles/         # Archivos estíticos recolectados
 db.sqlite3           # Base de datos SQLite
 manage.py
 requirements.txt     # Dependencias del proyecto
```

---

##  Rutas principales

**Login:**  
[http://127.0.0.1:8000/login/](http://127.0.0.1:8000/login/)

**Registro:**  
[http://127.0.0.1:8000/register/](http://127.0.0.1:8000/register/)

**Swagger (documentación de API):**  
[http://127.0.0.1:8000/api/swagger/](http://127.0.0.1:8000/api/swagger/)

---

##  Instalación y ejecución

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Nelsonguardo/API.git
   cd tu-proyecto
   ```

2. **Crear y activar entorno virtual:**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instalar dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Migrar la base de datos:**
   ```bash
   python manage.py migrate
   ```

5. **Crear superusuario:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Correr el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

---

## Comandos útiles

| Comando | Descripción                   |
|---------|-------------------------------|
| `python manage.py makemigrations` | Crear nuevas migraciones      |
| `python manage.py migrate` | Aplicar migraciones           |
| `python manage.py test` | Ejecutar tests                |
| `python manage.py collectstatic` | Recolectar archivos est谩ticos |
| `python manage.py shell` | Abrir shell interactivo       |

---

## Características

- Autenticación de usuarios (login y registro)
- Gestión de sesiones
- Documentación de la API en Swagger
- Uso de Django REST Framework y SimpleJWT

---

## Licencia

Este proyecto estuvo bajo la licencia MIT.  
Puedes usarlo, adaptarlo y mejorarlo libremente! 
