# app.py

"""Main app"""

# Retic
from retic import App as app

# Settings
import settings

# Apps
from apps import urls

# Routes
from routes import router

# Agregar las rutas a la aplicación
app.use(router)

if __name__ == "__main__":
    # Create web server
    app.listen(
        hostname=app.env("APP_HOSTNAME"),
        port=app.env.int("APP_PORT", 1801),
    )
