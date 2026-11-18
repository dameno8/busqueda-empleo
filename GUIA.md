# Guía: tu asistente de búsqueda de empleo con Codex

Codex es el ChatGPT "que trabaja con archivos". Le hablas igual que a ChatGPT, pero además lee y escribe en tu proyecto: tu CV, tus ofertas, tu seguimiento. Todo vive en **GitHub** (en la nube), así que no instalas nada y no pierdes nada si el portátil falla.

---

## Parte 1 · Preparación (una sola vez, ~15 min)

### 1. Cuenta de GitHub y tu copia privada
1. Crea una cuenta gratuita en <https://github.com/signup>.
2. Abre <https://github.com/dameno8/busqueda-empleo> y pulsa **Use this template → Create a new repository**.
3. Nombre: `busqueda-empleo`. Marca **Private** (aquí estará tu CV). Pulsa **Create repository**.

### 2. Conecta Codex con tu GitHub
1. Entra en <https://chatgpt.com/codex> con tu cuenta de ChatGPT.
2. Cuando te lo pida, pulsa **Conectar GitHub** y da acceso al repositorio `busqueda-empleo`.

### 3. Crea el "entorno" (dónde trabaja Codex)
En Codex web: **Configuración → Entornos → Crear entorno** y elige `busqueda-empleo`. Luego:
- **Script de configuración** (setup script): pega `pip install -r requirements.txt`
- **Acceso a internet del agente**: **Activado**, con lista de dominios permitidos. Añade:
  `indeed.com`, `es.indeed.com`, `apis.indeed.com`, `linkedin.com`, `www.linkedin.com`
- Guarda.

### 4. Primera conversación
1. En Codex, elige el entorno `busqueda-empleo` y escribe: **"Empecemos: configura mi perfil"**.
2. Cuando te pida el CV, abre tu CV, selecciona todo (Ctrl+A), copia (Ctrl+C) y pégalo en el chat (Ctrl+V).
3. Responde a sus preguntas. Al final, **guarda** (ver abajo).

### 5. Activa alertas por correo (el buscador no llega a todo)
- **InfoJobs**: alerta con "farmacéutico" + Granada.
- **Colegio Oficial de Farmacéuticos de Granada**: bolsa de trabajo (cofgranada.com).
- **Portal de empleo del Consejo General** (farmaceuticos.com).
- **LinkedIn**: alerta de empleo desde tu cuenta.

Cuando te llegue algo interesante, pega el enlace a Codex.

---

## Cómo se guarda (importante)

Cada vez que Codex termina una tarea, sus cambios quedan "pendientes". Para guardarlos:
1. Pulsa **Crear PR** (arriba a la derecha).
2. Pulsa **Ver PR**: se abre GitHub.
3. Pulsa **Merge pull request** y luego **Confirm merge**.

Hazlo **siempre antes de pedirle otra cosa**: si no, la siguiente tarea no verá lo anterior.

---

## Parte 2 · Uso diario

Cada petición es una tarea nueva en Codex. Ejemplos:

| Quieres… | Escribe |
|---|---|
| Ver ofertas nuevas | "Busca ofertas" |
| Saber si una oferta te encaja | "Mira esta oferta: [enlace]" (si no puede abrirla, pega el texto) |
| Preparar la candidatura | "Prepárame el CV y la carta para la oferta de [empresa]" |
| Apuntar que la has enviado | "Ya he enviado la de Farmacia X" |
| Ver cómo vas | "¿Cómo voy?" |
| Preparar una entrevista | "Tengo entrevista con X el jueves, ayúdame a prepararla" |
| Cambiar lo que buscas | "Ahora también quiero ver ofertas de industria en Málaga" |

**Descargar tu CV en Word**: después de guardar, ve a tu repositorio en GitHub → carpeta `ofertas` → carpeta de la oferta → `cv.docx` → botón de descarga (flecha ↓). **Revísalo siempre antes de enviarlo.** Desde Word: Archivo → Guardar como → PDF.

Codex **nunca** envía nada por ti ni entra en tu LinkedIn: él prepara, tú decides y envías.

---

## Si algo falla

- **El buscador no encuentra nada o da error**: los portales a veces bloquean. Tira de las alertas de correo y pega los enlaces.
- **Codex no ve algo que hiciste antes**: seguramente no guardaste (Merge). Revisa en GitHub → **Pull requests** si hay alguno abierto y haz Merge.
- **En enero, cuando cambies de cuenta de ChatGPT**: entra en chatgpt.com/codex con la cuenta nueva, conecta GitHub y vuelve a crear el entorno (paso 3). Tus archivos siguen en GitHub.
