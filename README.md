# 🧮 Context-Window-Remaining MCP

A micro-service ( *MCP* ) that tells you **how many tokens are still available in the current conversation** for any OpenAI-style chat model.  
Drop it into your *mcpServers* array, feed it a JSON payload, and it replies with token counts so your agent can decide when to summarise or prune history.

---

## ✨ Features
* **Model-agnostic** — works with any chat model as long as you supply its max-context length.  
* **Accurate tokenisation** — uses `tiktoken`, the same tokenizer OpenAI employs.  
* **Zero-state micro-service** — reads JSON on `stdin` (or over HTTP) and emits JSON on `stdout`.  
* **Config via env-vars** — switch models or context limits without editing code.  
* **Tiny footprint** — one <100-line Python file; no database.

---

## 📂 Repository Layout
