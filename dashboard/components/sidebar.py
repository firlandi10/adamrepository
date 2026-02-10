import streamlit as st

MENU = ["Dashboard", "Analitik", "Roadmap TA"]


def render_sidebar() -> str:
    with st.sidebar:
        st.markdown(
            """
            <div class="brand">
                <h3>Keday 70 Intelligence</h3>
                <p>Financial dashboard prototype</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        selected = st.selectbox("Menu", options=MENU, index=0, label_visibility="collapsed")
        st.caption("Prototype • Streamlit + n8n + LLM")
        return selected
