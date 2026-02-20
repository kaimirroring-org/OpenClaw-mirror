# GitHub Mirroring Automation (Complete System)

Last updated: 2026-02-20

## Goal
Automate mirroring from source repos in `ThePipis/*` to backup repos in `kaimirroring-org/*-mirror`, controlled from Notion with a checkbox (`Mirror Enabled`).

## Final Architecture
1. **Control plane (Notion)**
   - Database: `GitHub Mirror Control`
   - DB ID: `5a5d8653-8edc-4cff-bd66-9411a3fc242a`
   - Key fields:
     - `Name` (source repo, e.g. `ThePipis/OpenClaw`)
     - `Repo Mirror` (destination repo, e.g. `kaimirroring-org/OpenClaw-mirror`)
     - `Mirror Enabled` (checkbox)
     - `Status` (`Pending setup`, `Active`, `Paused`, `Error`)
     - `Last Sync` (date-time)
     - `Cron`, `Workflow URL`, `Source Visibility`, `Notes`

2. **Execution plane (GitHub Actions)**
   - Repo: `kaimirroring-org/mirror-controller`
   - Workflow: `.github/workflows/mirror-all.yml`
   - Trigger: `*/30 * * * *` + `workflow_dispatch`
   - Reads Notion table and mirrors enabled rows.

3. **Auth plane (GitHub App)**
   - App: `openclaw-mirror-bot`
   - Uses GitHub App installation tokens (short-lived), not PAT per repo.
   - Installed in:
     - `ThePipis` (read source repos)
     - `kaimirroring-org` (write/create mirror repos)

## Required Secrets
### In `kaimirroring-org` org/repo scope (Actions)
- `MIRROR_APP_ID`
- `MIRROR_APP_PRIVATE_KEY`

### In `kaimirroring-org/mirror-controller` repo secrets
- `NOTION_API_KEY`
- `NOTION_MIRROR_DB_ID` = `5a5d8653-8edc-4cff-bd66-9411a3fc242a`

## Runtime Behavior
- Every 30 min, workflow queries Notion database.
- For each row with `Mirror Enabled = true`:
  - Ensures destination repo exists (`<repo>-mirror` if needed).
  - Runs `git clone --mirror` source -> `git push --mirror` destination.
  - Removes hidden refs `refs/pull/*` before push to avoid GitHub rejection.
  - Updates Notion row:
    - `Status = Active`
    - `Last Sync = run timestamp`
- If `Mirror Enabled = false`:
  - Row is skipped from mirroring.
  - Status auto-set to `Paused`.

## Current Mirrors
- `ThePipis/OpenClaw` -> `kaimirroring-org/OpenClaw-mirror`
- `ThePipis/fiestapp` -> `kaimirroring-org/fiestapp-mirror`

## Known Gotchas
- If GitHub App is not installed in destination org, token creation fails.
- If Notion secrets are missing in `mirror-controller`, discover job fails.
- Force-mirroring PR refs fails unless `refs/pull/*` are removed first.

## Token Expiry Reminder
- Ops PAT reminder tracked in `memory/token-expiry-reminders.md`
- Reminder date: 2027-02-13 (for token expiring 2027-02-20)
