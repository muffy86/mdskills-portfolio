---
name: hermes-tweet
description: "Use Hermes Tweet when an agent needs Hermes Agent X/Twitter search, social listening, trend checks, launch monitoring, support triage, or approved posting through the native Hermes Tweet plugin. It installs from Xquik-dev/hermes-tweet and keeps reads first, credentials in the runtime environment, and write-like actions gated by explicit user approval."
license: MIT
compatibility:
  - Claude Code
  - Cursor
  - Codex
  - Gemini CLI
  - VS Code
  - Copilot
  - Amp
  - Roo Code
  - Goose
  - Windsurf
  - Continue
---

# Hermes Tweet

Hermes Tweet is a native Hermes Agent plugin for X/Twitter workflows. Use this
skill when an agent needs current X/Twitter context, social listening, launch
monitoring, support triage, trend checks, or user-approved account actions.

Source package: <https://github.com/Xquik-dev/hermes-tweet>

## Install

Install and enable Hermes Tweet on the Hermes runtime host:

```bash
hermes plugins install Xquik-dev/hermes-tweet --enable
```

For an existing Hermes Python environment:

```bash
uv pip install --python ~/.hermes/hermes-agent/venv/bin/python hermes-tweet
hermes plugins enable hermes-tweet
```

Set `XQUIK_API_KEY` where Hermes executes plugin tools, such as the runtime
environment or `~/.hermes/.env`. Keep `HERMES_TWEET_ENABLE_ACTIONS` unset or
`false` unless the user has approved a write-like operation.

## Tools

- `tweet_explore` searches the bundled endpoint catalog without a network call.
- `tweet_read` calls catalog-listed read-only endpoints and requires
  `XQUIK_API_KEY`.
- `tweet_action` calls private or write-like endpoints and requires both
  `XQUIK_API_KEY` and `HERMES_TWEET_ENABLE_ACTIONS=true`.

## Workflow

1. Start with `tweet_explore` for endpoint or capability discovery.
2. Use only endpoint paths returned by the catalog.
3. Use `tweet_read` for search, account, tweet, reply, follower, trend, and
   monitoring reads.
4. Before any post, reply, like, follow, DM, monitor change, webhook change,
   extraction job, or draw action, state the exact endpoint and payload.
5. Call `tweet_action` only after the user approves that exact action.
6. Summarize the result and note whether the workflow stayed read-only.

## Common Uses

### Social Listening

Search mentions, accounts, tweets, replies, trends, and public activity with
`tweet_explore`, then call read-only catalog routes through `tweet_read`.

### Launch Monitoring

Keep actions disabled. Use `tweet_read` for trends, search, public mentions,
and account checks. Escalate replies, follows, DMs, webhooks, and monitor
changes for explicit approval.

### Controlled Publishing

Enable `HERMES_TWEET_ENABLE_ACTIONS=true` only for an approved runtime session.
State the endpoint and payload before calling `tweet_action`, then verify with a
read route when available.

## Safety Rules

- Never put API keys, cookies, tokens, or account secrets in prompts, issues,
  comments, or tool arguments.
- Never guess Xquik endpoint paths. Use `tweet_explore`.
- Never treat plugin installation as authorization for write-like actions.
- In Hermes Desktop with a remote gateway profile, install and configure Hermes
  Tweet on the remote Hermes host because plugin tools execute there.

## Verification

After installation or upgrade:

- [ ] `hermes plugins list` shows `hermes-tweet` installed and enabled.
- [ ] `tweet_explore` is available without `XQUIK_API_KEY`.
- [ ] `tweet_read` appears after `XQUIK_API_KEY` is configured and Hermes is
      reloaded or restarted.
- [ ] `tweet_action` stays hidden or disabled unless
      `HERMES_TWEET_ENABLE_ACTIONS=true`.
