#!/usr/bin/env python
import sys, json, os
import tiktoken  # pip install tiktoken

# --- configuration -----------------------------------------------------------
MODEL          = os.getenv("MCP_MODEL",        "gpt-4o-mini")   # default
MAX_CONTEXT    = int(os.getenv("MCP_MAX_TOK",  128_000))        # for 4-o-mini
# -----------------------------------------------------------------------------


def tokens_used(messages, model):
    enc = tiktoken.encoding_for_model(model)
    # OpenAI chat format: 4 “overhead” tokens per message, 2 for system
    used = 0
    for m in messages:
        used += 4 + len(enc.encode(m.get("role", ""))) + len(enc.encode(m.get("content", "")))
        if "name" in m:
            used -= 1  # name hack; see OpenAI docs
    used += 2
    return used


def main():
    payload = json.load(sys.stdin)
    model   = payload.get("model", MODEL)
    msgs    = payload["messages"]

    used = tokens_used(msgs, model)
    remaining = MAX_CONTEXT - used
    out = {
        "model": model,
        "max_context": MAX_CONTEXT,
        "used": used,
        "remaining": max(remaining, 0),
        "percent_full": round(used / MAX_CONTEXT * 100, 2)
    }
    print(json.dumps(out))


if __name__ == "__main__":
    main()
