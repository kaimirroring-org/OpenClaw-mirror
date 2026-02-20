# MEMORY.md

## 2026-02-20
- Flujo validado para mirror automático GitHub entre cuentas (`ThePipis` -> `kaimirroring/kaimirroring-org`) usando GitHub Actions.
- Frecuencia estándar definida: cada 30 minutos (`*/30 * * * *`) + trigger manual.
- Playbook operativo local: `memory/github-mirroring-playbook.md`.
- Documentación completa del sistema final (Notion + GitHub App + mirror-controller): `memory/github-mirroring-system-complete.md`.
- Tabla Notion `GitHub Mirror Control` definida como fuente de verdad para onboarding y estado de mirrors.
- Plantilla de endurecimiento guardada para reutilización: `memory/security-hardening-control-table-template.md`.
- Estado actual de hardening OL9 documentado en `memory/security-hardening-ol9-current-status-2026-02-20.md`.
- Regla operativa acordada: al pedir un `SEC-0XXX`, responder primero con diagnóstico estructurado (Resultado general, Evidencia clave, Comparativo vs objetivo, Conclusión) y esperar aprobación antes de implementar.
- SEC-000 cerrado: backup fail2ban creado en `/root/sec-backups/fail2ban.2026-02-20-085720`.
- SEC-009 automatizado: cron diario root (`10 6 * * * /usr/local/sbin/openclaw-sec-daily.sh`) con logs en `/var/log/openclaw-security/`.
- SEC-006B implementado: acceso SSH privado por Tailscale y cierre de SSH público en firewall (origen tailnet `100.64.0.0/10`).
- Manual operativo Tailscale (Windows laptop <-> VPS OL9) en `memory/tailscale-vps-laptop-secure-connection-manual.md`.
- Checklist rápido de contingencia (60s post-reinicio) guardado en `memory/contingency-checklist-60s-vps-laptop-tailscale.md`.
- SEC-004.1 cerrado (tailnet-only): eliminado fallback de SSH público por IP; se mantiene acceso SSH solo por Tailscale (`100.64.0.0/10`).
- Manual de fallback túnel SSH Windows (SEC-006A) en `memory/ssh-tunnel-fallback-windows-manual.md`.
