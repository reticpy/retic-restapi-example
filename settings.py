# settings.py

# Retic
from retic import App as app

"""Asignar ruta de variables de entorno"""
app.env.read_env('.env.development', override=True)