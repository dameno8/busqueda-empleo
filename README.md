# Búsqueda de empleo con Codex

Plantilla para buscar trabajo con [Codex](https://chatgpt.com/codex) (OpenAI): evalúa ofertas contra tu perfil, adapta el CV y la carta a cada una, y lleva el seguimiento. Pensada para perfiles de farmacia en Granada, pero se adapta editando `perfil/` y `config/`.

👉 **Si eres quien va a usarla, empieza por [GUIA.md](GUIA.md).**

## Cómo funciona

- `AGENTS.md`: instrucciones que Codex lee automáticamente (modos de trabajo y reglas).
- `perfil/`: qué buscas y tu CV maestro (fuente única de tu experiencia).
- `scripts/buscar_ofertas.py`: busca en Indeed España y en la búsqueda pública de LinkedIn con [JobSpy](https://github.com/speedyapply/JobSpy), sin usar tu cuenta. Parámetros en `config/busqueda.toml`.
- `scripts/generar_docx.py`: convierte el CV y la carta adaptados a Word.
- `ofertas/`: una carpeta por oferta (texto, evaluación, CV, carta).
- `seguimiento.csv`: estado de cada candidatura.

Inspirado en [career-ops](https://github.com/santifer/career-ops), simplificado para alguien sin experiencia técnica.

## Privacidad

Tu copia debe ser un **repositorio privado**. No se guardan datos sensibles (DNI, fecha de nacimiento) en los CV salvo que lo pidas.
