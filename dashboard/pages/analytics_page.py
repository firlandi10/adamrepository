import pandas as pd
import plotly.express as px
import streamlit as st


def render_analytics(data: pd.DataFrame) -> None:
    st.subheader("Analitik Penjualan & Operasional")

    daily = data[["Tanggal", "Omzet", "Biaya Operasional", "Laba Bersih"]].copy()
    cash_fig = px.bar(
        daily,
        x="Tanggal",
        y=["Omzet", "Biaya Operasional", "Laba Bersih"],
        barmode="group",
        title="Arus Kas Harian",
    )
    st.plotly_chart(cash_fig, width="stretch")

    product = pd.DataFrame(
        {
            "Produk": ["Ayam Geprek", "Es Teh Jumbo", "Nasi Goreng", "Mie Goreng", "Kopi Susu"],
            "Qty Terjual": [420, 380, 310, 260, 190],
            "Omset": [12_600_000, 3_800_000, 9_300_000, 7_280_000, 4_940_000],
        }
    )
    prod_fig = px.bar(
        product,
        x="Produk",
        y="Qty Terjual",
        color="Qty Terjual",
        title="Top Produk Berdasarkan Kuantitas",
    )
    st.plotly_chart(prod_fig, width="stretch")

    cols = st.columns(2)
    with cols[0]:
        st.markdown("<div class='block-title'>Tabel Arus Kas</div>", unsafe_allow_html=True)
        st.dataframe(daily.sort_values("Tanggal", ascending=False), width="stretch", hide_index=True)
    with cols[1]:
        st.markdown("<div class='block-title'>Tabel Produk</div>", unsafe_allow_html=True)
        st.dataframe(product, width="stretch", hide_index=True)
