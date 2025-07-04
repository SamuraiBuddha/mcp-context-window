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

├── mcp_context_window_remaining.py # core service
├── requirements.txt # tiktoken, fastapi (optional), uvicorn
└── README.md # you are here

yaml
Copy
Edit

---

## 🔧 Installation

```bash
# Clone your tool-combo-chains repo (or wherever you keep MCPs)
git clone https://github.com/YourOrg/tool-combo-chains
cd tool-combo-chains

# Add the file and dependency
cp path/to/mcp_context_window_remaining.py .
echo "tiktoken>=0.5.0" >> requirements.txt

# (Optional) for the HTTP façade
echo "fastapi>=0.111 uvicorn[standard]>=0.30" >> requirements.txt

pip install -r requirements.txt
🚀 Quick Start (Std-IO mode)
bash
Copy
Edit
echo '{
  "messages":[
    {"role":"system","content":"You are..."},
    {"role":"user","content":"Hello!"}
  ],
  "model":"gpt-4o-mini"
}' \
| python -m mcp_context_window_remaining
Sample response:

json
Copy
Edit
{
  "model": "gpt-4o-mini",
  "max_context": 128000,
  "used": 37,
  "remaining": 127963,
  "percent_full": 0.03
}
🐋 Docker / mcpServers Stanza
Add this block to the mcpServers object in your JSON:

jsonc
Copy
Edit
"context-window-remaining": {
  "command": "python",
  "args": ["-m", "mcp_context_window_remaining"],
  "cwd": "C:\\Users\\JordanEhrig\\Documents\\GitHub\\tool-combo-chains",
  "env": {
    "MCP_MODEL": "gpt-4o-mini",
    "MCP_MAX_TOK": "128000",
    "INSTANCE_ID": "Melchior-ContextWin-001",
    "LOG_LEVEL": "INFO"
  }
}
Now any MCP client can run:

bash
Copy
Edit
mcp context-window-remaining < payload.json
🌐 Optional HTTP Façade
Add fastapi & uvicorn to requirements.txt.

Launch with:

bash
Copy
Edit
uvicorn mcp_context_window_remaining:app --host 0.0.0.0 --port 8008
POST to http://hostname:8008/remaining with the same payload structure.

⚙️ Environment Variables
Variable	Purpose	Default
MCP_MODEL	Model name for tiktoken	gpt-4o-mini
MCP_MAX_TOK	Max context length for that model	128000
LOG_LEVEL	DEBUG, INFO, WARNING…	INFO
INSTANCE_ID	Free-form tag for logging/metrics	unset

📈 Integrating into an Agent Loop
Count tokens before every model call.

If remaining < threshold → summarise/prune oldest messages.

Pass the trimmed history to the model; repeat.

pseudo
Copy
Edit
history = load_messages()
stats   = call_mcp_context_window_remaining(history)

if stats.remaining < 2000:
    history = summarise_oldest(history)

reply = openai.chat(history + [user_msg])
📝 License
MIT — do what you like; attribution appreciated.

🙏 Credits
Token counting algorithm from OpenAI’s official examples.

README template inspired by Jordan Ehrig’s relentless quest for clean, modular MCPs.

“Praeparate, ne contextu sit exhaustum!”
Prepare, lest the context run dry.
