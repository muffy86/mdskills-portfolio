#!/usr/bin/env python3
"""
notte_agent.py — Notte browser agent CLI and importable module.

Usage:
    python notte_agent.py --task "Find the CTO of Stripe on LinkedIn"
    python notte_agent.py --task "List top posts" --url https://news.ycombinator.com --max-steps 10
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import Any


def run_browser_task(
    task: str,
    url: str | None = None,
    max_steps: int = 20,
    reasoning_model: str = "gemini/gemini-2.5-flash",
) -> Any:
    """Start a Notte browser session, run a task, return the answer."""
    try:
        from notte_sdk import NotteClient  # type: ignore
    except ImportError as exc:
        raise ImportError("notte-sdk not installed. Run: pip install notte-sdk") from exc

    api_key = os.getenv("NOTTE_API_KEY")
    if not api_key:
        raise ValueError("NOTTE_API_KEY not set. Get one at https://console.notte.cc")

    client = NotteClient(api_key=api_key)
    with client.Session() as session:
        agent = client.Agent(
            session=session,
            reasoning_model=reasoning_model,
            max_steps=max_steps,
        )
        kwargs: dict[str, Any] = {"task": task}
        if url:
            kwargs["url"] = url
        return agent.run(**kwargs).answer


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Notte AI browser agent")
    parser.add_argument("--task", required=True, help="Natural-language task to perform")
    parser.add_argument("--url", help="Starting URL (optional)")
    parser.add_argument("--max-steps", type=int, default=20)
    parser.add_argument("--model", default="gemini/gemini-2.5-flash",
                        help="Reasoning model (gemini/gemini-2.5-flash, openai/gpt-4o, ...)")
    args = parser.parse_args()
    try:
        print(run_browser_task(args.task, args.url, args.max_steps, args.model))
    except (ImportError, ValueError) as err:
        print(f"ERROR: {err}", file=sys.stderr)
        sys.exit(1)
