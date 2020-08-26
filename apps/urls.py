# apps/urls.py

# Retic
from retic import App as app

"""Define otras aplicaciones"""
BACKEND_EXAMPLE= {
    u"base_url": app.config.get('APP_BACKEND_JSONPLACEHOLDER'),
    u"users": "/users",
}

"""Crea el objeto referencia de las apps"""
APP_BACKEND = {
    u"example": BACKEND_JSONPLACEHOLDER,
}

"""Agrega las aplicaciones a Retic"""
app.use(APP_BACKEND, "backend")
