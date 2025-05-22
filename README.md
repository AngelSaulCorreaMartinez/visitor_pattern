# Patrón Visitor - Ejemplo con Personajes de Juego

Este proyecto demuestra el patrón de diseño Visitor utilizando un ejemplo de personajes de juego (Magos y Guerreros).

## ¿Qué es el Patrón Visitor?

El patrón Visitor permite agregar nuevas operaciones a objetos existentes sin modificar su código. Es como tener un "visitante" que puede realizar diferentes acciones según el tipo de objeto que visita.

## Estructura del Proyecto

- `Visitable.py`: Define la interfaz para objetos que pueden ser "visitados"
- `Visitante.py`: Define la interfaz para los "visitantes"
- `Mago.py` y `Guerrero.py`: Clases de personajes que pueden ser visitados
- `EquiparArma.py` y `EquiparEncantamiento.py`: Visitantes que equipan objetos a los personajes

## Flujo de Funcionamiento

1. Se crean personajes (Magos y Guerreros)
2. Se crea un visitante (por ejemplo, EquiparArma)
3. El visitante recorre la lista de personajes
4. Cada personaje "acepta" al visitante
5. El visitante ejecuta diferentes acciones según el tipo de personaje

## Ejemplo de Flujo

```python
# Crear personajes y visitante
mago = Mago()
ea = EquiparArma()

# El visitante visita al personaje
ea.visitar_personajes([mago])
# Internamente:
# 1. mago.aceptar(ea)
# 2. ea.visitar_mago(mago)
# 3. mago recibe una daga
```

## Ventajas

- Separa las operaciones de los objetos
- Facilita agregar nuevas operaciones sin modificar las clases existentes
- Mantiene el código organizado y modular

## Casos de Uso

En este ejemplo:
- `EquiparArma`: Equipa diferentes armas según el tipo de personaje
  - Magos → Dagas
  - Guerreros → Espadas
- `EquiparEncantamiento`: Solo afecta a los magos
  - Nivel ≤ 5 → Bola de Fuego
  - Nivel > 5 → Rayo de Hielo
