from greeting import greet

def test_greet_devuelve_saludo_con_nombre():
    assert greet("Ana") == "Hola, Ana"

def test_greet_incluye_el_nombre_pasado():
    resultado = greet("Beto")
    assert "Beto" in resultado
