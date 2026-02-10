import plotly.express as px
import streamlit as st
import pandas as pd


def render_dashboard(data: pd.DataFrame) -> None:
    st.markdown(
        """
        <div class="hero">
            <h2>Dashboard Keuangan Keday 70</h2>
            <p>Ringkasan performa toko dengan KPI, grafik tren, dan tabel operasional harian.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    total_omzet = int(data["Omzet"].sum())
    total_laba_kotor = int(data["Laba Kotor"].sum())
    total_transaksi = int(data["Total Transaksi"].sum())
    avg_ticket = int(total_omzet / total_transaksi) if total_transaksi else 0

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Omset", f"Rp {total_omzet:,.0f}".replace(",", "."))
    c2.metric("Laba Kotor", f"Rp {total_laba_kotor:,.0f}".replace(",", "."))
    c3.metric("KPI / Total Transaksi", f"{total_transaksi:,}".replace(",", "."))
    c4.metric("Rata-rata Transaksi", f"Rp {avg_ticket:,.0f}".replace(",", "."))

    st.markdown("<div class='block-title'>📈 Ringkasan Visual</div>", unsafe_allow_html=True)
    left, right = st.columns((2, 1))

    with left:
        trend = px.line(
            data,
            x="Tanggal",
            y=["Omzet", "Laba Kotor", "Laba Bersih"],
            markers=True,
            title="Tren Omset & Profit",
        )
        trend.update_layout(margin=dict(l=10, r=10, t=46, b=10), legend_title_text="Metrik")
        st.plotly_chart(trend, width="stretch")

    with right:
        composition = px.pie(
            values=[data["HPP"].sum(), data["Biaya Operasional"].sum(), data["Laba Bersih"].sum()],
            names=["HPP", "Biaya Operasional", "Laba Bersih"],
            title="Komposisi Keuangan",
            hole=0.58,
        )
        composition.update_layout(margin=dict(l=10, r=10, t=46, b=10))
        st.plotly_chart(composition, width="stretch")

    st.markdown("<div class='block-title'>📋 Tabel Rangkuman Harian</div>", unsafe_allow_html=True)
    st.dataframe(
        data[
            [
                "Tanggal",
                "Omzet",
                "HPP",
                "Laba Kotor",
                "Biaya Operasional",
                "Laba Bersih",
                "Total Transaksi",
            ]
        ]
        .sort_values("Tanggal", ascending=False)
        .reset_index(drop=True),
        width="stretch",
        hide_index=True,
    )
