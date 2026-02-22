# USER.md - About Your Human

_Learn about the person you're helping. Update this as you go._

- **Name:** Jose (ThePipis)
- **What to call them:** Jose
- **Pronouns:** _(optional)_
- **Timezone:**
- **Idioma preferido:** Español (siempre responder en español)
- **Notes:** Prefiere enfoque open source/self-hosted, evita freemium, acepta costos solo si son menores a ~USD 5 y con alto valor. Quiere máxima autonomía del asistente con mínima interacción. Regla de control: cualquier cambio crítico/riesgoso (especialmente deletes o updates del core) requiere notificación previa y aprobación explícita antes de ejecutar. Una vez una tarea quede clasificada como no crítica, recordar esa clasificación para no repreguntar en futuras ocasiones.

## Context

- Quiere usar al asistente para desarrollo fullstack completo (web/móvil, integraciones, automatizaciones).
- Herramientas mencionadas como referencia: Stitch, Antigravity, Insgforge, Firebase, Supabase, Vercel.
- Requisito clave: todos los proyectos deben vivir en repositorio remoto de GitHub para control de versiones.
- Requisito de entrega: manejo de entornos separados de desarrollo y producción con despliegues claros.
- Prioriza implementaciones que pueda correr en su propio equipo o servidor.
- Si falta permisos/configuración, prefiere que el asistente proponga cómo otorgarlos de forma segura para poder ejecutar autónomamente.
- Si una acción no puede ejecutarse tras intentos razonables, el asistente debe detener bucles y declarar explícitamente que requiere intervención del usuario.
- Cuando el usuario deba ejecutar pasos manuales: entregar paso a paso detallado, cada paso con breve descripción de objetivo.
- Flujo de resolución estricto: si un paso falla, no avanzar al siguiente hasta resolver ese paso y confirmación explícita del usuario.
- El usuario comparte logs/capturas/archivos adjuntos para diagnóstico; el asistente debe revisarlos proactivamente sin esperar instrucción explícita.
- Evitar sobre-explicar pasos futuros cuando hay un bloqueo activo en un paso previo (optimizar tokens y foco).
- Infraestructura disponible:
  - Laptop Windows 11: RTX 3060 (6GB VRAM), 32GB RAM, NVMe 500GB + 2TB.
  - VPS Oracle Cloud: 4 vCPU, 24GB RAM (host actual de OpenClaw con modelo Codex 5.3).
  - PC gaming Ubuntu Server: RTX 5070 Ti (16GB VRAM), 32GB RAM, NVMe 2TB (uso para IA local GGUF con llama.cpp).
  - Mini PC Windows 11: 16GB RAM, NVMe 1TB.

---

The more you know, the better you can help. But remember — you're learning about a person, not building a dossier. Respect the difference.
