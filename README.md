
# Evo-World

Evo-World es un simulador simple de ecosistemas evolutivos escrito en Python. Permite modelar criaturas, alimentos y un mundo donde las criaturas interactúan, se reproducen y evolucionan con el tiempo.

## Características

- Simulación de entidades con genomas (`src/evoworld/domain/genome.py`).
- Mundo y reglas de interacción (`src/evoworld/domain/world.py`).
- Motores de simulación (`src/evoworld/simulation/engine.py`).
- Representación básica/renderer (`src/evoworld/rendering/renderer.py`).

## Requisitos

- Python 3.10 o superior
- Dependencias gestionadas vía `pyproject.toml`

## Instalación

1. Clona el repositorio:

```bash
git clone <repo-url>
cd evo-world
```

2. Instala en modo editable (opcionalmente en un entorno virtual):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Ejecución

Ejecuta la entrada principal del paquete:

```bash
python -m evoworld.main
```

O usa el script dentro de `src/evoworld/main.py` durante el desarrollo.

## Estructura del proyecto

- `src/evoworld/main.py` - Punto de entrada de la aplicación.
- `src/evoworld/config/settings.py` - Parámetros y constantes de configuración.
- `src/evoworld/domain/` - Modelos de dominio: `creature.py`, `food.py`, `genome.py`, `world.py`.
- `src/evoworld/simulation/engine.py` - Lógica del bucle de simulación.
- `src/evoworld/rendering/renderer.py` - Código relacionado con la visualización.

## Cómo contribuir

1. Crea un fork y una rama de trabajo.
2. Añade tests cuando sea posible.
3. Abre un Pull Request describiendo los cambios.

## Licencia

Licencia MIT — ver archivo `LICENSE` si está presente.

---

Si quieres, puedo añadir ejemplos de configuración, badges CI, o una guía rápida para desarrollar y probar cambios localmente.
