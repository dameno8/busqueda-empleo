# Guía: tu asistente de búsqueda de empleo con Codex

Codex es el ChatGPT "que trabaja con archivos". Le hablas igual que a ChatGPT, pero además puede leer y escribir en una carpeta: tu CV, tus ofertas, tu seguimiento. Tú no tienes que tocar nada técnico: se lo pides con tus palabras.

Todo se guarda en **GitHub**, que funciona como una copia de seguridad en la nube: si el portátil falla, no pierdes nada.

---

## Parte 1 · Preparación (una sola vez, ~30 min)

### 1. Crea tu cuenta de GitHub
1. Entra en <https://github.com/signup> y crea una cuenta gratuita.
2. Pásale tu nombre de usuario a Daniel.

### 2. Haz tu copia privada del proyecto
1. Abre el enlace del proyecto que te pase Daniel.
2. Pulsa el botón verde **Use this template → Create a new repository**.
3. Nombre: `busqueda-empleo`. Marca **Private** (importante: aquí estará tu CV). Pulsa **Create repository**.

### 3. Instala los programas (todo desde la **Microsoft Store**, botón Obtener)
1. **Python 3.13**: busca "Python 3.13" en la Microsoft Store e instálalo.
2. **Git**: descárgalo de <https://git-scm.com/download/win> e instálalo dejando todas las opciones por defecto (Siguiente, Siguiente…).
3. **GitHub Desktop**: <https://desktop.github.com>. Al abrirlo, inicia sesión con tu cuenta de GitHub.
4. **Codex**: busca "Codex" en la Microsoft Store (de OpenAI) e inicia sesión con tu cuenta de ChatGPT.

### 4. Baja el proyecto a tu ordenador
1. En GitHub Desktop: **File → Clone repository**, elige `busqueda-empleo` y pulsa **Clone**.
   Se crea la carpeta `Documentos\GitHub\busqueda-empleo`.
2. En Codex: abre esa carpeta como proyecto.

### 5. Primera conversación con Codex
1. Copia tu CV (PDF o Word) dentro de la carpeta `perfil` del proyecto.
2. Escribe en Codex: **"Empecemos: configura mi perfil"**.
3. Codex leerá tu CV, te hará unas preguntas (qué buscas, dónde, salario, idiomas…) y lo dejará todo listo.
4. Después escribe: **"Busca ofertas"** para probar el buscador.

Codex a veces te pedirá permiso para hacer algo (instalar un programa, guardar en GitHub…). Lee la frase y acepta si tiene sentido.

### 6. Activa alertas por correo (el buscador no llega a todo)
- **InfoJobs**: crea una alerta con "farmacéutico" + Granada.
- **Colegio Oficial de Farmacéuticos de Granada**: bolsa de trabajo para colegiados (cofgranada.com).
- **Portal de empleo del Consejo General de Farmacéuticos** (farmaceuticos.com).
- **LinkedIn**: alerta de empleo desde tu propia cuenta.

Cuando te llegue algo interesante, pega el enlace a Codex.

---

## Parte 2 · Uso diario

Habla con Codex con naturalidad. Ejemplos:

| Quieres… | Escribe |
|---|---|
| Ver ofertas nuevas | "Busca ofertas" |
| Saber si una oferta te encaja | "Mira esta oferta: [enlace]" (si no puede abrirla, pega el texto) |
| Preparar la candidatura | "Prepárame el CV y la carta para esta" |
| Apuntar que la has enviado | "Ya he enviado la de Farmacia X" |
| Ver cómo vas | "¿Cómo voy?" |
| Preparar una entrevista | "Tengo entrevista con X el jueves, ayúdame a prepararla" |
| Cambiar lo que buscas | "Ahora también quiero ver ofertas de industria en Málaga" |
| Ofertas en inglés | "Busca también ofertas en inglés" |

Los CV y cartas se generan en Word dentro de `ofertas\<fecha_empresa_puesto>\`. **Revísalos siempre antes de enviarlos.** Desde Word: Archivo → Guardar como → PDF.

Codex **nunca** envía nada por ti ni entra en tu LinkedIn: él prepara, tú decides y envías.

---

## Parte 3 · Si algo falla

- **Codex dice que no ha podido guardar en GitHub**: abre GitHub Desktop y pulsa **Push origin** (arriba).
- **El portátil falla o estás en otro ordenador**: entra en <https://chatgpt.com/codex>, conecta tu GitHub y elige `busqueda-empleo`. Ahí puedes evaluar ofertas y preparar candidaturas. Cuando termine, pulsa **Create PR** y luego, en GitHub, **Merge** para que quede guardado. (El buscador automático puede no funcionar desde ahí; usa los enlaces de tus alertas.)
- **En enero, cuando cambies de cuenta de ChatGPT**: en Codex, cierra sesión e inicia con tu cuenta nueva. Tus archivos siguen igual; solo se pierde el historial de conversaciones, que no hace falta.
- **El buscador no encuentra nada o da error**: es normal de vez en cuando (los portales bloquean). Inténtalo otro día o tira de las alertas de correo.
