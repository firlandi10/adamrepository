import streamlit as st


def apply_theme() -> None:
    st.markdown(
        """
        <style>
        :root {
            --slate-900: #0f172a;
            --slate-700: #334155;
            --slate-500: #64748b;
            --sky-500: #0ea5e9;
            --indigo-600: #4f46e5;
            --white: #ffffff;
        }

        .stApp {
            background:
                radial-gradient(circle at 0% 0%, rgba(79, 70, 229, 0.18), transparent 35%),
                radial-gradient(circle at 100% 0%, rgba(14, 165, 233, 0.18), transparent 35%),
                linear-gradient(180deg, #f8fafc 0%, #eef2ff 100%);
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0b1220 0%, #0f172a 100%);
            border-right: 1px solid rgba(148, 163, 184, 0.18);
        }

        [data-testid="stSidebar"] * {
            color: #e2e8f0 !important;
        }

        [data-testid="stSidebarNav"] {
            display: none;
        }

        .brand {
            background: linear-gradient(135deg, #4f46e5 0%, #0ea5e9 100%);
            border-radius: 14px;
            padding: 0.9rem 1rem;
            margin-bottom: 1rem;
            box-shadow: 0 12px 26px rgba(79, 70, 229, 0.28);
        }

        .brand h3 {
            margin: 0;
            color: #fff;
            font-size: 1.02rem;
        }

        .brand p {
            margin: 0.3rem 0 0;
            color: #e0f2fe;
            font-size: 0.78rem;
        }

        .hero {
            padding: 1rem 1.2rem;
            border-radius: 16px;
            background: linear-gradient(130deg, #1d4ed8 0%, #0891b2 100%);
            color: #ffffff;
            box-shadow: 0 14px 30px rgba(15, 23, 42, 0.18);
            margin-bottom: 0.85rem;
        }

        .hero h2 {
            margin: 0;
            font-size: 1.35rem;
            font-weight: 700;
        }

        .hero p {
            margin: 0.45rem 0 0;
            font-size: 0.9rem;
            opacity: 0.95;
        }

        .block-title {
            margin-top: 0.2rem;
            margin-bottom: 0.55rem;
            color: var(--slate-900);
            font-weight: 700;
        }

        .stMetric {
            background: rgba(255, 255, 255, 0.85);
            border: 1px solid rgba(148, 163, 184, 0.2);
            border-radius: 14px;
            padding: 0.7rem 0.8rem;
            box-shadow: 0 8px 20px rgba(15, 23, 42, 0.08);
        }

        .stDataFrame, .stPlotlyChart {
            background: #ffffff;
            border-radius: 14px;
            border: 1px solid rgba(148, 163, 184, 0.2);
            padding: 0.2rem;
            box-shadow: 0 10px 18px rgba(15, 23, 42, 0.05);
        }

        [data-testid="stSidebar"] .stSelectbox label {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
