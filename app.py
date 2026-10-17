"""
Streamlit Web Application: GenAI-Based Technical Learning Content Generator.
Provides an interactive, professional web interface for generating, practicing,
and downloading technical learning materials using open-source models.
"""

import streamlit as st
import time

from generator import ContentGenerator
from knowledge_base import get_curated_subjects, get_curated_topics
from utils import (
    validate_inputs,
    format_as_markdown,
    format_as_text,
    export_as_json,
    validate_python_code
)

# Page Configuration
st.set_page_config(
    page_title="GenAI Technical Learning Content Generator",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for rich aesthetics and clean typography
st.markdown("""
<style>
    /* Main container styling */
    .main-header {
        font-size: 2.2rem;
        font-weight: 700;
        background: linear-gradient(135deg, #1E3A8A, #3B82F6, #06B6D4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .badge-card {
        padding: 0.8rem 1.2rem;
        border-radius: 10px;
        background-color: #F3F4F6;
        border: 1px solid #E5E7EB;
        margin-bottom: 1rem;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 48px;
        font-weight: 600;
        border-radius: 6px 6px 0px 0px;
    }
    .callout-box {
        background-color: #FEF3C7;
        border-left: 4px solid #F59E0B;
        padding: 0.8rem 1rem;
        border-radius: 4px;
        margin-bottom: 1rem;
        color: #92400E;
        font-size: 0.95rem;
    }
    .verified-badge {
        background-color: #DEF7EC;
        color: #03543F;
        padding: 0.25rem 0.6rem;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_resource(show_spinner=False)
def load_cached_generator(model_name: str) -> ContentGenerator:
    """Cached singleton loader for the AI generator."""
    gen = ContentGenerator(model_name=model_name)
    gen.load_model()
    return gen


def main():
    # Application Title and Tagline
    st.markdown('<div class="main-header">🧠 GenAI Technical Learning Content Generator</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sub-header">Generate structured technical explanations, code examples, interactive practice questions, and revision summaries using open-source models.</div>',
        unsafe_allow_html=True
    )

    # Educational Disclaimer Alert
    st.markdown(
        '<div class="callout-box">⚠️ <b>Educational Notice:</b> AI-generated technical materials may occasionally contain inaccuracies. Always review and verify code snippets in a safe environment before using them in software systems.</div>',
        unsafe_allow_html=True
    )

    # Sidebar: Configurations and Inputs
    with st.sidebar:
        st.header("⚙️ Generator Settings")

        # Model Selector
        model_choice = st.selectbox(
            "AI Model (Open-Source)",
            options=["google/flan-t5-small", "google/flan-t5-base"],
            index=0,
            help="Free, open-source instruction-following Seq2Seq model from Google."
        )

        # Subject Selection
        available_subjects = get_curated_subjects()
        selected_subject = st.selectbox("1. Technical Subject", options=available_subjects, index=0)

        # Curated Topics or Custom Topic
        curated_topics = get_curated_topics(selected_subject)
        use_custom = st.checkbox("Enter custom topic instead", value=False)

        if use_custom:
            selected_topic = st.text_input("Enter Technical Topic", placeholder="e.g., Recursion, Redis, Joins, etc.")
        else:
            options_list = curated_topics + ["Custom..."]
            topic_pick = st.selectbox("2. Select Topic", options=options_list, index=0)
            if topic_pick == "Custom...":
                selected_topic = st.text_input("Enter Technical Topic", placeholder="e.g., Generators, B-Trees, etc.")
            else:
                selected_topic = topic_pick

        # Difficulty Level
        difficulty = st.select_slider(
            "3. Difficulty Level",
            options=["Beginner", "Intermediate", "Advanced"],
            value="Beginner"
        )

        # Content Type Selector
        content_type = st.selectbox(
            "4. Content Type",
            options=[
                "Complete learning pack",
                "Concept explanation",
                "Code example",
                "Practice questions",
                "Revision summary"
            ],
            index=0
        )

        st.markdown("---")
        generate_clicked = st.button("🚀 Generate Learning Content", type="primary", use_container_width=True)

        st.markdown("---")
        st.caption("Hardware: CPU-optimized inference. Free & open-source tools only.")

    # Initialize Session State
    if "current_pack" not in st.session_state:
        st.session_state["current_pack"] = None
    if "pack_metadata" not in st.session_state:
        st.session_state["pack_metadata"] = None
    if "quiz_submitted" not in st.session_state:
        st.session_state["quiz_submitted"] = False
    if "user_quiz_choice" not in st.session_state:
        st.session_state["user_quiz_choice"] = None

    # Handle Generation Trigger
    if generate_clicked:
        is_valid, err_msg = validate_inputs(selected_subject, selected_topic, difficulty)
        if not is_valid:
            st.error(f"❌ {err_msg}")
        else:
            with st.spinner(f"Generating technical pack for '{selected_topic}' ({difficulty})..."):
                try:
                    generator = load_cached_generator(model_choice)
                    pack = generator.generate_learning_pack(
                        subject=selected_subject,
                        topic=selected_topic.strip(),
                        difficulty=difficulty,
                        content_type=content_type
                    )
                    st.session_state["current_pack"] = pack
                    st.session_state["pack_metadata"] = {
                        "subject": selected_subject,
                        "topic": selected_topic.strip(),
                        "difficulty": difficulty,
                        "content_type": content_type
                    }
                    st.session_state["quiz_submitted"] = False
                    st.session_state["user_quiz_choice"] = None
                    st.success(f"✨ Successfully generated learning content in {pack.get('generation_time_sec', 0)}s!")
                except Exception as e:
                    st.error(f"Generation error occurred: {str(e)}")

    # Display Generated Content
    pack = st.session_state["current_pack"]
    meta = st.session_state["pack_metadata"]

    if pack and meta:
        # Overview Metadata Header
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Subject", meta["subject"])
        col2.metric("Topic", meta["topic"])
        col3.metric("Difficulty", meta["difficulty"])
        col4.metric("Latency", f"{pack.get('generation_time_sec', 0)}s")

        st.caption(f"Source: **{pack.get('source', 'Model generation')}** | Model: `{pack.get('model_used', 'N/A')}`")
        st.markdown("---")

        # Tabbed Output Interface
        tab_explanation, tab_code, tab_quiz, tab_summary, tab_export = st.tabs([
            "📖 Concept Explanation",
            "💻 Code Example",
            "✍️ Practice Quiz",
            "💡 Revision Summary",
            "📥 Export & Download"
        ])

        # TAB 1: Concept Explanation
        with tab_explanation:
            if "definition" in pack:
                st.subheader(f"📌 What is {meta['topic']}?")
                st.write(pack.get("definition", "No definition available."))

                if "how_it_works" in pack:
                    st.markdown("#### ⚙️ How It Works Internally")
                    st.write(pack.get("how_it_works", ""))

                if "important_points" in pack and pack["important_points"]:
                    st.markdown("#### 🔑 Core Principles & Key Points")
                    for pt in pack["important_points"]:
                        st.markdown(f"- {pt}")

                if "common_mistakes" in pack and pack["common_mistakes"]:
                    st.markdown("#### ⚠️ Common Pitfalls & Misconceptions")
                    for m in pack["common_mistakes"]:
                        st.markdown(f"- **Warning:** {m}")
            else:
                st.info("Concept explanation was not requested for this content type.")

        # TAB 2: Practical Code Example
        with tab_code:
            if "code" in pack:
                lang = "sql" if meta["subject"].lower() == "sql" else "python"
                st.subheader(f"💻 Practical Implementation ({lang.upper()})")

                # Code block
                st.code(pack["code"], language=lang)

                # AST Syntax Validation Alert
                if "code_validation" in pack:
                    val_info = pack["code_validation"]
                    if val_info["is_valid"]:
                        st.success(f"✅ {val_info['message']}")
                    else:
                        st.warning(f"⚠️ {val_info['message']}")

                # Code walkthrough
                if "code_explanation" in pack and pack["code_explanation"]:
                    st.markdown("#### 🔍 Step-by-Step Code Walkthrough")
                    for line in pack["code_explanation"]:
                        st.markdown(f"- {line}")
            else:
                st.info("Code example was not requested for this content type.")

        # TAB 3: Practice & Knowledge Check (Interactive Quiz)
        with tab_quiz:
            if "mcq" in pack:
                mcq = pack["mcq"]
                st.subheader("🎯 Multiple Choice Question")
                st.markdown(f"**{mcq.get('question')}**")

                user_selection = st.radio(
                    "Select your answer:",
                    options=mcq.get("options", []),
                    key=f"mcq_radio_{meta['topic']}"
                )

                submit_col1, submit_col2 = st.columns([1, 4])
                with submit_col1:
                    if st.button("Submit Answer", type="secondary"):
                        st.session_state["quiz_submitted"] = True
                        st.session_state["user_quiz_choice"] = user_selection

                if st.session_state.get("quiz_submitted"):
                    chosen_opt = st.session_state["user_quiz_choice"]
                    correct_opt_letter = mcq.get("correct_answer", "").strip().upper()
                    chosen_letter = chosen_opt[:1].upper() if chosen_opt else ""

                    if chosen_letter == correct_opt_letter:
                        st.success(f"🎉 **Correct!** You selected Option {chosen_letter}.")
                    else:
                        st.error(f"❌ **Incorrect.** You selected Option {chosen_letter}, but the correct answer is **Option {correct_opt_letter}**.")

                    st.info(f"💡 **Explanation:** {mcq.get('explanation')}")

            if "short_question" in pack:
                sq = pack["short_question"]
                st.markdown("---")
                st.subheader("📝 Conceptual Short-Answer Question")
                st.markdown(f"**Q: {sq.get('question')}**")
                with st.expander("👁️ Click to Reveal Suggested Answer & Explanation"):
                    st.markdown(f"**Answer:** {sq.get('answer')}")

            if "mcq" not in pack and "short_question" not in pack:
                st.info("Practice questions were not requested for this content type.")

        # TAB 4: Revision Summary
        with tab_summary:
            if "summary" in pack and pack["summary"]:
                st.subheader(f"💡 Fast Revision Summary: {meta['topic']}")
                for bullet in pack["summary"]:
                    st.markdown(f"- {bullet}")
            else:
                st.info("Revision summary was not requested for this content type.")

        # TAB 5: Export & Download Hub
        with tab_export:
            st.subheader("📥 Download Learning Material")
            st.write("Save your generated learning material in your preferred format for offline study or documentation:")

            md_content = format_as_markdown(pack, meta["topic"], meta["subject"], meta["difficulty"])
            txt_content = format_as_text(pack, meta["topic"], meta["subject"], meta["difficulty"])
            json_content = export_as_json(pack, meta["topic"], meta["subject"], meta["difficulty"])

            col_d1, col_d2, col_d3 = st.columns(3)
            with col_d1:
                st.download_button(
                    label="📄 Download as Markdown (.md)",
                    data=md_content,
                    file_name=f"{meta['topic'].lower().replace(' ', '_')}_{meta['difficulty'].lower()}.md",
                    mime="text/markdown",
                    use_container_width=True
                )
            with col_d2:
                st.download_button(
                    label="📝 Download as Plain Text (.txt)",
                    data=txt_content,
                    file_name=f"{meta['topic'].lower().replace(' ', '_')}_{meta['difficulty'].lower()}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
            with col_d3:
                st.download_button(
                    label="📊 Download as JSON (.json)",
                    data=json_content,
                    file_name=f"{meta['topic'].lower().replace(' ', '_')}_{meta['difficulty'].lower()}.json",
                    mime="application/json",
                    use_container_width=True
                )

            with st.expander("👀 Preview Raw Markdown"):
                st.code(md_content, language="markdown")

    else:
        # Friendly Landing Placeholder
        st.info("👈 Select a subject, topic, and difficulty from the sidebar, then click **Generate Learning Content** to begin.")

        # Quick Subject Highlights Cards
        st.markdown("### 📚 Supported Subjects")
        c1, c2, c3 = st.columns(3)
        with c1:
            st.markdown("""
            **🐍 Python Programming**
            - List Comprehensions
            - Decorators & Generators
            - Concurrency & AsyncIO
            """)
            st.markdown("""
            **🗄️ SQL & Databases**
            - Inner, Left & Self Joins
            - Aggregations & Grouping
            - Window Functions
            """)
        with c2:
            st.markdown("""
            **🧩 Object-Oriented (OOP)**
            - Polymorphism & Duck Typing
            - Inheritance & Composition
            - Encapsulation & Dunder Methods
            """)
            st.markdown("""
            **🌲 Data Structures**
            - Binary Search Trees
            - Stacks & Queues
            - Graphs & Hash Maps
            """)
        with c3:
            st.markdown("""
            **🤖 Machine Learning**
            - Bias-Variance Tradeoff
            - Regularization (L1/L2)
            - Confusion Matrix & Metrics
            """)
            st.markdown("""
            **✨ Generative AI**
            - Transformers & Self-Attention
            - Tokenization & Embeddings
            - Prompt Engineering & RAG
            """)


if __name__ == "__main__":
    main()
