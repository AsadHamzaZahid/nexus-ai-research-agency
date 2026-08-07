import time
import streamlit as st
from pipeline import run_research_pipeline

st.set_page_config(page_title="Nexus — AI Research Agency",
                   page_icon="🧭", layout="wide")

# ---------------------------------------------------------------------------
# Custom styling
# ---------------------------------------------------------------------------
st.markdown("""
<style>
    #MainMenu, footer, header {visibility: hidden;}

    .stApp {
        background: radial-gradient(circle at 20% -10%, #1b1037 0%, #0b0b18 45%, #07070f 100%);
        color: #f1eefc;
    }

    .nexus-hero {
        padding: 2.5rem 2rem 1.5rem 2rem;
        text-align: center;
    }
    .nexus-badge {
        display: inline-block;
        padding: 0.3rem 0.9rem;
        border-radius: 999px;
        background: linear-gradient(90deg, #7c3aed, #ec4899);
        font-size: 0.75rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .nexus-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(90deg, #c4b5fd, #f9a8d4, #fcd34d);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.4rem;
    }
    .nexus-subtitle {
        color: #b7b2cf;
        font-size: 1.05rem;
        max-width: 640px;
        margin: 0 auto;
    }

    .agent-row {
        display: flex;
        gap: 1rem;
        justify-content: center;
        flex-wrap: wrap;
        margin: 2rem 0 2.5rem 0;
    }
    .agent-card {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 1.1rem 1.3rem;
        width: 200px;
        text-align: left;
        transition: 0.2s;
    }
    .agent-card:hover {
        border-color: rgba(196,181,253,0.5);
        transform: translateY(-3px);
    }
    .agent-icon { font-size: 1.6rem; }
    .agent-name { font-weight: 700; margin: 0.4rem 0 0.2rem 0; font-size: 0.95rem; }
    .agent-role { font-size: 0.8rem; color: #a8a3c4; line-height: 1.3; }
    .agent-arrow { align-self: center; color: #6d6890; font-size: 1.4rem; }

    .stTextInput > div > div {
        background: rgba(255,255,255,0.06) !important;
        border-radius: 12px !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
    }

    .stTextInput input {
        background: transparent !important;
        color: #ffffff !important;
        padding: 0.8rem 1rem !important;
        caret-color: #ffffff !important;
    }

    .stTextInput input::placeholder {
        color: #8b87a8 !important;
        opacity: 1 !important;
    }

    .stButton button {
        background: linear-gradient(90deg, #7c3aed, #ec4899) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.7rem 1.6rem !important;
        font-weight: 700 !important;
        letter-spacing: 0.02em;
    }

    .report-box {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 1.8rem;
    }

    div[data-baseweb="tab-list"] { gap: 1.5rem; }

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Hero
# ---------------------------------------------------------------------------
st.markdown("""
<div class="nexus-hero">
    <div class="nexus-badge">Multi-Agent Intelligence</div>
    <div class="nexus-title">🧭 Nexus</div>
    <div class="nexus-subtitle">
        A small team of AI agents that search the web, read the best sources,
        write a structured report, and critique their own work — so you don't have to.
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Agent pipeline showcase
# ---------------------------------------------------------------------------
agents = [
    ("🔍", "Scout", "Searches the web for fresh, relevant sources on your topic."),
    ("📖", "Reader", "Picks the best result and scrapes it for deeper detail."),
    ("✍️", "Writer", "Synthesizes everything into a structured report."),
    ("🧐", "Critic", "Scores the report and flags what to improve."),
]

cards_html = '<div class="agent-row">'
for i, (icon, name, role) in enumerate(agents):
    cards_html += f"""
    <div class="agent-card">
        <div class="agent-icon">{icon}</div>
        <div class="agent-name">{name}</div>
        <div class="agent-role">{role}</div>
    </div>"""
    if i < len(agents) - 1:
        cards_html += '<div class="agent-arrow">→</div>'
cards_html += "</div>"
st.markdown(cards_html, unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Input
# ---------------------------------------------------------------------------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    with st.form("research_form"):
        topic = st.text_input(
            "Research topic",
            placeholder="e.g. The future of fusion energy",
            label_visibility="collapsed",
        )
        submitted = st.form_submit_button(
            "🚀 Run the Agents", use_container_width=True)

# ---------------------------------------------------------------------------
# Pipeline execution
# ---------------------------------------------------------------------------
if submitted:
    if not topic.strip():
        st.warning("Give Nexus a topic to investigate first.")
    else:
        progress_box = st.container()
        with progress_box:
            steps = st.empty()
            stage_labels = [
                "🔍 Scout is searching the web...",
                "📖 Reader is scraping the best source...",
                "✍️ Writer is drafting the report...",
                "🧐 Critic is reviewing the work...",
            ]
            for label in stage_labels:
                steps.info(label)
                time.sleep(0.4)

            try:
                state = run_research_pipeline(topic)
                steps.success(
                    "✅ All agents finished — here's what they found.")
            except Exception as e:
                steps.error(f"Pipeline failed: {e}")
                state = None

        if state:
            tab_report, tab_feedback, tab_raw = st.tabs(
                ["📄 Report", "🧐 Critic Feedback", "🔬 Raw Research"])

            with tab_report:
                st.markdown(
                    f'<div class="report-box">{state.get("report", "_No report generated._")}</div>', unsafe_allow_html=True)

            with tab_feedback:
                st.markdown(
                    f'<div class="report-box">{state.get("feedback", "_No feedback generated._")}</div>', unsafe_allow_html=True)

            with tab_raw:
                with st.expander("🔍 Scout's search results"):
                    st.write(state.get("search_results", ""))
                with st.expander("📖 Reader's scraped content"):
                    st.write(state.get("scraped_content", ""))

st.markdown(
    '<div style="text-align:center; color:#6d6890; margin-top:3rem; font-size:0.85rem;">'
    'Nexus — powered by LangChain agents, orchestrated by you.</div>',
    unsafe_allow_html=True,
)
