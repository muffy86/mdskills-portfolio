# muffy86 mdskills Portfolio

A curated collection of production-grade AI agent skills in the open
[`SKILL.md`](https://agentskills.io/specification) format. Each skill
is a self-contained folder with `SKILL.md` (frontmatter + main
instructions) plus optional `reference/`, `scripts/`, and `assets/`
bundles.

These skills work with any agent that supports the open standard
(Claude Code, Cursor, Codex, Gemini CLI, VS Code, Copilot, Amp,
Roo Code, Goose, Windsurf, Continue, and 20+ others).

## Browse

| Skill | What it does |
|-------|--------------|
| `account-research` | Build a complete account picture before sales outreach — web search, enrichment, CRM context |
| `competitive-intelligence` | Research a competitor and produce an interactive HTML battlecard |
| `daily-briefing` | Get a prioritized, scannable briefing of what matters today |
| `domain-research` | RDAP/WHOIS-based domain availability and ownership checks (no API keys) |
| `hermes-tweet` | Use Hermes Agent for read-first X/Twitter workflows and approved account actions |
| `legal-writer` | Draft contracts, memos, briefs, ToS, NDAs with Bluebook citation and DOCX output |
| `openalex-paper-search` | Free academic search across 240M+ scholarly works via OpenAlex |
| `pdf` | Create, edit, extract, OCR, fill, and convert PDF documents |
| `presentations` | Create, validate, and export HTML presentation slides (1920x1080) |
| `vercel-ai-gateway` | Route OpenAI-compatible calls through Vercel's AI Gateway |
| `whisper` | Transcribe audio and video to text (Whisper via Groq or OpenAI) |

## Install any skill

```bash
npx mdskills install muffy86/mdskills-portfolio/<skill-name>
# or copy the folder into your agent's skills directory
```

## Format

Every skill follows the [open `SKILL.md` spec](https://agentskills.io/specification):

```yaml
---
name: <kebab-case-name>            # required, ≤ 64 chars, matches folder
description: <third-person, ≤ 1024 chars, with trigger keywords>  # required
license: MIT                       # optional
compatibility:                     # optional
  - Claude Code
  - Cursor
  - Codex
allowed-tools: Bash(python:*) Read  # optional
---
```

## Compatibility

Tested with Claude Code, Cursor, OpenAI Codex CLI, and Gemini CLI.

## License

MIT — see each skill's `LICENSE` file.
