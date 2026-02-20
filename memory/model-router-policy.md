# Model Router Policy (OpenClaw)

Last updated: 2026-02-20
Status: active by operator approval

## Objective
Auto-select the best model tier per task, reduce premium token burn, and fail over safely when quotas/errors happen.

## Tiers
- Tier A (critical): `openai-codex/gpt-5.3-codex`
- Tier B (technical daily): `Qwen 3 Code 30B` (local)
- Tier C (economical cloud): `MiniMax` (promo period)
- Tier D (stable cloud backup): `Gemini Pro`
- Tier E (ultra-lite preprocessor): `PicoLM 1.1B`

## Routing rules
1. Security/infra/destructive/complex multi-step => Tier A.
2. Normal coding/refactor/tests/docs => Tier B.
3. Text/data transforms and non-critical generation => Tier C.
4. If Tier C unavailable => Tier D.
5. Classification/extraction/routing microtasks => Tier E.

## Failover rules
- A: no automatic downgrade for critical tasks without explicit user approval.
- B: fallback order B -> C -> D.
- C: fallback to D.
- E: fallback to B if JSON/quality fails.

## Usage guardrails
- Always present plan + explicit approval before critical/risky changes.
- If fallback/degradation occurs, report it in final response.
- If precision risk is high and only weak backup is available, pause and request user confirmation.

## Token/usage safety trigger
- If premium short-window remaining <= 20%:
  - switch non-critical tasks from A to B/C automatically.
  - keep A only for critical tasks.
- If premium short-window remaining <= 10%:
  - default non-critical to B/C/D and ask confirmation before consuming A.

## Operational note
Current OpenClaw runtime does not provide native global auto-router identical to ChatGPT UI.
This policy is enforced operationally by the assistant (decision layer) and documented as source-of-truth.
