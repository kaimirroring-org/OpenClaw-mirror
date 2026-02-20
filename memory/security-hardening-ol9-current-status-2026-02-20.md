# Security Hardening Status - Oracle Linux 9 (2026-02-20)

| ID | Qué se debe hacer / qué resuelve | ¿Implementado en servidor actual? | Criticidad |
|---|---|---|---|
| SEC-000 | Backups de configs críticas antes de cambios (rollback rápido). | Sí: backup `sshd_config` presente y backup fail2ban creado en `/root/sec-backups/fail2ban.2026-02-20-085720`. | ⭐⭐⭐⭐☆ |
| SEC-001 | Asegurar panel OpenClaw no expuesto públicamente (`127.0.0.1:18789`) + firewall sin 18789 abierto. | Sí: OpenClaw escucha en `127.0.0.1:18789` y firewalld no expone 18789 ni SSH público. | ⭐⭐⭐⭐⭐ |
| SEC-002 | Permisos restrictivos en credenciales OpenClaw. | Sí: `/home/jose/.openclaw/credentials` en `700`, owner `jose`. | ⭐⭐⭐⭐☆ |
| SEC-003 | Hardening SSH sin romper túnel local (`-L`). | **Sí (implementado ahora)**: `00-hardening.conf` activo; `X11Forwarding no`, `AllowAgentForwarding no`, `MaxAuthTries 3`, `LoginGraceTime 30`. | ⭐⭐⭐⭐⭐ |
| SEC-004 | Firewall mínimo viable (sin servicios innecesarios en zona pública). | Sí: zona `public` con solo `dhcpv6-client`; sin puertos abiertos. | ⭐⭐⭐⭐⭐ |
| SEC-004.1 | Restringir SSH a IP pública fija (opcional). | Cerrado/No aplicable por decisión: fallback por IP pública removido; operación `tailnet-only` (sin SSH público). | ⭐⭐⭐⭐☆ |
| SEC-005 | Fail2ban activo para sshd (bloqueo de bruteforce). | Sí: jail `sshd` activo (stats y bans visibles). | ⭐⭐⭐⭐☆ |
| SEC-006A | Acceso al panel por túnel SSH (sin exposición pública). | Sí (fallback documentado y operativo): manual en `memory/ssh-tunnel-fallback-windows-manual.md`; servidor compatible (OpenClaw loopback + SSH controlado). | ⭐⭐⭐⭐☆ |
| SEC-006B | Acceso SSH privado por Tailscale (sin SSH público en internet). | Sí: Tailscale activo; firewall público sin `ssh`; acceso permitido por tailnet (`100.64.0.0/10`). | ⭐⭐⭐⭐⭐ |
| SEC-007 | Panel OpenClaw con token + pairing. | Sí: auth `token` y eventos de `pairing required` observados. | ⭐⭐⭐⭐⭐ |
| SEC-008 | Allowlist de WhatsApp. | Sí: `allowFrom` configurado para `+19512716200`. | ⭐⭐⭐⭐☆ |
| SEC-009 | Observabilidad diaria de seguridad. | Sí: cron root activo (`10 6 * * * /usr/local/sbin/openclaw-sec-daily.sh`) y logs en `/var/log/openclaw-security/`. | ⭐⭐⭐☆☆ |
| SEC-010 | Beneficio global (postura endurecida y controlada). | Sí: postura endurecida con acceso primario por Tailscale + fallback controlado por IP y túnel SSH. | ⭐⭐⭐⭐☆ |
| SEC-011 | Pendientes priorizados para cierre. | Sí: pendientes principales cerrados en esta fase. | ⭐⭐⭐⭐⭐ |

## Evidence highlights
- SSH hardening effective values:
  - `x11forwarding no`
  - `allowagentforwarding no`
  - `maxauthtries 3`
  - `logingracetime 30`
- Listener status:
  - `0.0.0.0:22` (sshd escuchando en host)
  - `127.0.0.1:18789` (OpenClaw)
- Firewall:
  - zona `public` sin `ssh` (solo `dhcpv6-client`)
  - zona `trusted` con source `100.64.0.0/10` (tailnet)
- Fail2ban:
  - jail `sshd` active, historical bans recorded.
- Observabilidad diaria:
  - cron root: `10 6 * * * /usr/local/sbin/openclaw-sec-daily.sh`
  - log: `/var/log/openclaw-security/daily-YYYY-MM-DD.log`
