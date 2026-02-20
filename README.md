# OpenClaw Workspace (Respaldo + Automatizaciones)

Este repositorio guarda configuración, memoria y playbooks operativos del asistente para restauración rápida, continuidad y operación autónoma.

## Objetivo

- Versionar configuración relevante del workspace.
- Mantener backups automáticos con commits periódicos.
- Crear tags semanales como puntos de recuperación.
- Mantener espejos (mirrors) automáticos de repositorios desde `ThePipis` hacia `kaimirroring-org`.
- Usar Notion como fuente de verdad para habilitar/pausar mirrors.

## Estructura principal

### Archivos raíz

- `AGENTS.md` → reglas operativas del asistente (memoria, seguridad, estilo de trabajo).
- `SOUL.md` → identidad/tono del asistente.
- `USER.md` → preferencias y contexto técnico del usuario.
- `TOOLS.md` → notas locales del entorno.
- `IDENTITY.md` → identidad declarativa del asistente.
- `HEARTBEAT.md` → checklist de tareas periódicas (si está vacío, no agrega trabajo extra).
- `MEMORY.md` → memoria de largo plazo curada.
- `README.md` → este documento.

### Carpeta `memory/`

- `memory/YYYY-MM-DD-*.md` → memoria diaria cronológica.
- `memory/github-mirroring-playbook.md` → procedimiento operativo corto de mirrors.
- `memory/github-mirroring-system-complete.md` → documentación completa del sistema Notion + GitHub App + mirror-controller.
- `memory/token-expiry-reminders.md` → recordatorios de rotación/expiración de tokens.

### Carpeta `.openclaw/`

- `.openclaw/auto-backup.sh` → backup automático (`git add/commit/push`).
- `.openclaw/weekly-tag.sh` → tag semanal `weekly-YYYY-Www`.
- `.openclaw/auto-backup.log` → log de tareas automáticas.
- `.openclaw/workspace-state.json` → estado interno de OpenClaw.

### Carpeta `scripts/`

- `scripts/notion_mirror_upsert.py` → crea/actualiza registros de mirror en Notion.

## Automatizaciones activas

### 1) Backup automático del workspace (cada 30 min)

```cron
*/30 * * * * /home/jose/.openclaw/workspace/.openclaw/auto-backup.sh >> /home/jose/.openclaw/workspace/.openclaw/auto-backup.log 2>&1
```

### 2) Tag semanal automático

```cron
15 3 * * 1 /home/jose/.openclaw/workspace/.openclaw/weekly-tag.sh >> /home/jose/.openclaw/workspace/.openclaw/auto-backup.log 2>&1
```

### 3) Mirroring automático (ThePipis -> kaimirroring-org)

Controlado por GitHub Actions en:
- `kaimirroring-org/mirror-controller`
- Workflow: `.github/workflows/mirror-all.yml`
- Frecuencia: `*/30 * * * *` + ejecución manual (`workflow_dispatch`)

## Notion como fuente de verdad

Base de datos: **GitHub Mirror Control**

Campos principales:
- `Name` (repo origen, ej. `ThePipis/OpenClaw`)
- `Repo Mirror` (repo destino, ej. `kaimirroring-org/OpenClaw-mirror`)
- `Mirror Enabled` (checkbox)
- `Status` (`Pending setup`, `Active`, `Paused`, `Error`)
- `Last Sync` (fecha/hora)
- `Cron`, `Workflow URL`, `Source Visibility`, `Notes`

Comportamiento:
- Si `Mirror Enabled = true` → el repo se sincroniza.
- Si `Mirror Enabled = false` → se omite y pasa a `Paused`.
- En éxito de sync → `Status = Active` y actualización de `Last Sync`.

## Seguridad y acceso

- GitHub App para auth de mirroring (tokens temporales), evitando PAT por repo en operación normal.
- Secrets requeridos en `mirror-controller`:
  - `MIRROR_APP_ID`
  - `MIRROR_APP_PRIVATE_KEY`
  - `NOTION_API_KEY`
  - `NOTION_MIRROR_DB_ID`

## Restauración rápida (resumen)

1. Clonar este repo.
2. Verificar secrets y acceso de GitHub App.
3. Restaurar cron jobs de backup/tag.
4. Validar ejecución manual de scripts y workflows.
5. Confirmar sincronización en Notion + GitHub Actions.
