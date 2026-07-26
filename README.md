# GitEz 🚀

> **Un generador interactivo, ultrarrápido y local de mensajes para commits en Git.**

`GitEz` analiza los archivos que agregaste a *staging* (`git add .`) y te sugiere automáticamente mensajes estandarizados bajo la convención de **Conventional Commits**. Se ejecuta en milisegundos, funciona 100% offline y no requiere API keys.

---

## ⚡ Características

- 🚀 **Ultra rápido:** Latencia prácticamente nula, sin dependencias de servicios externos ni LLMs de pago.
- 🔒 **100% Privado:** Todo el análisis se ejecuta de forma local en tu máquina.
- 🎯 **Sugerencias inteligentes:** Detecta extensiones de archivos, documentación, tests y configuraciones para inferir el tipo de commit (`feat`, `fix`, `docs`, `test`, `chore`).
- 🏷️ **Integración con tickets:** Infiere automáticamente el ID de Jira o ticket a partir del nombre de tu rama Git.
- ⌨️ **Interfaz TUI fluida:** Selecciona el mensaje de forma sencilla utilizando las flechas del teclado.

---

## 📦 Instalación

La forma recomendada de instalarlo para que quede disponible como comando global en tu terminal es mediante `pipx`:

```bash
pipx install git+[https://github.com/AAMoralesC/GitEz.git](https://github.com/AAMoralesC/GitEz.git)