# Mini checklist (20s) - OpenClaw UI desconectada

URL fija:
- `http://127.0.0.1:18789/`

Si aparece `gateway token missing`:
1. Abrir Settings (Control UI).
2. Pegar Gateway token.
3. Guardar.
4. Recargar página o botón reconectar.

Checks rápidos si no reconecta:
1. Verificar túnel local activo:
   - `netstat -ano | findstr :18789`
2. Verificar respuesta web local:
   - `curl http://127.0.0.1:18789/`
3. Verificar tarea túnel en Windows:
   - `schtasks /Query /TN "OpenClawTunnelTS"`
4. Si cayó túnel, relanzar:
   - `schtasks /Run /TN "OpenClawTunnelTS"`

Gateway token actual:
- `f78de08a4390eca60ae808052c054a2ca0bc84b5a7f1a76a`

Nota:
- El token es estable hasta que lo regeneres/cambies en el servidor.
