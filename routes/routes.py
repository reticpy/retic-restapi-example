# routes/routes.py

# Retic
from retic import Router

# Controllers
import controllers.users as users

"""Definir la instancia Router"""
router = Router()

"""Definir las rutas de la apliación"""
router\
    .get("/", lambda res, req, next: req.ok({u"msg": "Hello world!"})) \
    .post("/", lambda res, req, next: req.ok({u"msg": "Hello world!"}))

"""Definir las rutas de la apliación - users"""
router\
    .get("/users/:id", users.get_by_id)
