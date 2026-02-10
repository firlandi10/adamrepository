import streamlit as st

from dashboard.components.sidebar import render_sidebar
from dashboard.data.sample_data import build_dataset
from dashboard.pages.analytics_page import render_analytics
from dashboard.pages.dashboard_page import render_dashboard
from dashboard.pages.roadmap_page import render_roadmap
from dashboard.styles.theme import apply_theme


st.set_page_config(
    page_title="Dashboard Keuangan Keday 70",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

apply_theme()
data = build_dataset(days=60)

menu = render_sidebar()

if menu == "Dashboard":
    render_dashboard(data)
elif menu == "Analitik":
    render_analytics(data)
else:
    render_roadmap()
