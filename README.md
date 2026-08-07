# 🧭 Nexus — AI Research Agency

A small team of AI agents that work together to research a topic for you: they search the web, read the best sources, write a structured report, and critique their own work.

Built with **LangChain**, **Streamlit**, and a multi-agent pipeline.

---

## 🤖 How it works

Nexus runs four agents in sequence:

1. **🔍 Scout** — Searches the web for fresh, relevant sources on your topic.
2. **📖 Reader** — Picks the best result and scrapes it for deeper detail.
3. **✍️ Writer** — Synthesizes everything into a structured report.
4. **🧐 Critic** — Reviews the report, scores it, and flags what could be improved.

You type a topic, hit **Run the Agents**, and watch each stage complete before getting a final report with critic feedback.

---

## 🖥️ Tech stack

- **Streamlit** — frontend / UI
- **LangChain** — agent orchestration
- **Python** — pipeline logic (`agents.py`, `pipeline.py`, `tools.py`)

---

## 🚀 Getting started (local setup)

This project is **not deployed** yet — right now it only runs locally. To try it:

### 1. Clone the repo
```bash
git clone https://github.com/AsadHamzaZahid/nexus-ai-research-agency.git
cd nexus-ai-research-agency
```

### 2. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # macOS/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your environment variables
Create a `.env` file in the project root with any API keys the agents need (e.g. search API, LLM provider key). This file is **not included** in the repo for security reasons — you'll need to create your own.

```
# Example
OPENAI_API_KEY=your_key_here
SEARCH_API_KEY=your_key_here
```

### 5. Run the app
```bash
streamlit run app.py
```

The app will open automatically at `http://localhost:8501`.

---

## 📌 Status

🚧 **Work in progress** — this is a local prototype, not yet deployed publicly. Deployment (e.g. via Streamlit Community Cloud or a similar platform) is planned for a future update.

---

## 📂 Project structure

```
├── app.py             # Streamlit UI + pipeline trigger
├── agents.py           # Agent definitions (Scout, Reader, Writer, Critic)
├── pipeline.py          # Orchestrates the multi-agent research flow
├── tools.py             # Helper tools used by agents (search, scraping, etc.)
├── requirements.txt      # Python dependencies
└── .gitignore
```

---

## 🙋 Author

Built by **Asad Hamza Zahid**
[GitHub](https://github.com/AsadHamzaZahid) · [LinkedIn](https://linkedin.com/in/asad-hamzazahid)
