# GitEz 🚀

[![tests](https://github.com/AAMoralesC/GitEz/actions/workflows/tests.yml/badge.svg)](https://github.com/AAMoralesC/GitEz/actions/workflows/tests.yml)
[![PyPI](https://img.shields.io/pypi/v/git-ez.svg)](https://pypi.org/project/git-ez/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)

> **Generador interactivo, ultrarrápido y local de mensajes de commit — en español.**

`GitEz` analiza los archivos que agregaste a *staging* (`git add .`) y te sugiere mensajes
estandarizados bajo **Conventional Commits**, redactados en español. Se ejecuta en milisegundos,
funciona 100% offline y no requiere API keys.

---

## 📸 Demo

![Demo de GitEz en acción](./gitez_demo.png)

---

## ⚡ Características

- 🚀 **Ultra rápido:** sin llamadas a servicios externos ni LLMs de pago.
- 🔒 **100% privado:** todo el análisis ocurre en tu máquina.
- 🇪🇸 **Mensajes en español:** nativo, no traducciones automáticas.
- 🎯 **Sugerencias por contexto:** infiere el tipo de commit (`feat`, `fix`, `docs`, `test`, `chore`) según extensiones, documentación, tests y configuración.
- 🏷️ **Integración con tickets:** detecta el ID en el nombre de la rama (`feature/PROJ-42-login` → `PROJ-42`).
- ⌨️ **TUI fluida:** flechas y `Enter`, o escribe tu propio mensaje.

---

## 🧠 Sin IA, a propósito

GitEz no usa LLMs y es una decisión de diseño, no una limitación:

- **Privacidad:** tu código y tus nombres de archivo no salen de tu máquina.
- **Velocidad:** responde al instante, sin red ni latencia de modelo.
- **Determinismo:** el mismo staging produce la misma sugerencia, siempre.

Para un commit message el contexto útil son las rutas y extensiones de archivo, así que un LLM
añade costo, latencia y una dependencia externa sin mejorar el resultado.

---

## 📦 Instalación

```bash
pipx install git-ez
```

También con `pip`:

```bash
pip install git-ez
```

### Desarrollo local

```bash
git clone https://github.com/AAMoralesC/GitEz.git
cd GitEz
pip install -e .
python -m unittest discover -s tests
```

### Actualización

```bash
pipx upgrade git-ez
```

---

## 💻 Uso

1. Agrega tus cambios al staging como siempre:

   ```bash
   git add .
   ```

2. Ejecuta GitEz:

   ```bash
   git ez
   ```

   También funciona como `git-ez`, como `git ez commit`, o como `python -m git_ez`.

3. Navega con `↑`/`↓`, elige una sugerencia o escribe tu propio mensaje, y presiona `Enter`.
   El commit se ejecuta solo.

Ejemplo de mensajes generados:

| Tipo | Ejemplo |
|------|---------|
| `feat` | `feat: actualizar main.py, utils.py` |
| `fix` | `fix: resolver problema en auth.py` |
| `docs` | `docs: actualizar documentación (README.md)` |
| `test` | `test: agregar o actualizar pruebas unitarias` |
| `chore` | `chore: actualizar dependencias y configuración del proyecto` |

Con ticket en la rama (`feature/PROJ-42-login`):

```
feat: [PROJ-42] actualizar main.py, utils.py
```

**Requisitos:** Python 3.10+ y Git en el `PATH`. Probado en 3.10, 3.12 y 3.13.

---

## 🛠️ Stack

Python · [Typer](https://typer.tiangolo.com/) · [Questionary](https://questionary.readthedocs.io/) · [Rich](https://rich.readthedocs.io/)

---

## 🤝 Contribuciones

Issues y PRs son bienvenidos. Para cambios grandes, abre primero un issue.

```bash
git checkout -b feature/mi-aporte
# ...cambios y tests...
git ez   # 😉
```

---

## 📄 Licencia

MIT — ver [LICENSE](./LICENSE).
