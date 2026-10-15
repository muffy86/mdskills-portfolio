---
name: notte-browser
description: "Use Notte to control a real browser. This skill triggers when the user wants to navigate web pages, fill forms, click buttons, log into websites, scrape live data from pages that require interaction, or automate any web-based workflow that plain web search cannot handle. Trigger keywords: browser, click, scroll, fill form, login, screenshot, scrape live page, navigate to, web automation, notte."
license: MIT
compatibility:
  - Claude Code
  - Cursor
  - Codex
  - Gemini CLI
allowed-tools: Bash(python:*) Read Write
---

# Notte Browser

Control a real browser with AI. Use this skill when you need to navigate pages, click buttons, fill forms, log into websites, extract data from live pages, or automate web workflows that plain web search cannot reach.

## Prerequisites

```bash
pip install notte-sdk
export NOTTE_API_KEY="your-key"  # from console.notte.cc
```

## Quick Start

```python
from notte_sdk import NotteClient
import os

client = NotteClient(api_key=os.getenv("NOTTE_API_KEY"))

with client.Session() as session:
    agent = client.Agent(session=session, max_steps=20)
    result = agent.run(task="YOUR TASK HERE")
    print(result.answer)
```

## Common Tasks

### Research / Live Data Extraction
```python
result = agent.run(task="Go to linkedin.com and find the current CTO of Stripe")
result = agent.run(task="Navigate to producthunt.com and list today's top 5 products")
```

### Login & Authenticated Actions
```python
# Attach credentials from your Notte vault
agent = client.Agent(session=session, vault_id="your-vault-id")
result = agent.run(task="Log into github.com and list my open pull requests")
```

### Form Filling
```python
result = agent.run(
    task="Fill the contact form at example.com/contact: name=Test, email=test@example.com"
)
```

### Structured Output
```python
from pydantic import BaseModel

class CompanyData(BaseModel):
    name: str
    description: str
    employee_count: str

result = agent.run(
    task="Go to stripe.com and extract company info",
    response_format=CompanyData
)
print(result.answer)  # typed CompanyData instance
```

## CLI

```bash
python notte-browser/scripts/notte_agent.py --task "Research the CEO of Notion" --max-steps 15
python notte-browser/scripts/notte_agent.py --task "List top posts" --url https://news.ycombinator.com
```

## Integration with Other Skills

| Pair with | What you get |
|-----------|-------------|
| **account-research** | Live LinkedIn + company page scraping instead of cached search |
| **competitive-intelligence** | Real-time competitor site + pricing analysis |
| **daily-briefing** | Pull data from paywalled or login-gated sources |

## API Key

```bash
export NOTTE_API_KEY="notte-..."        # env var
echo "NOTTE_API_KEY=notte-..." >> .env  # .env file
notte auth login                         # CLI (if installed)
```

Get a free key at https://console.notte.cc

## Verify

```bash
notte sessions list
```
