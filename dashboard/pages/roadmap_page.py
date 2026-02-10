import streamlit as st


def render_roadmap() -> None:
    st.subheader("Roadmap Implementasi Produk TA")

    stages = [
        "Studi Literatur dan Pendahuluan",
        "Pengumpulan dan Pra-pemrosesan Data",
        "Analisis dan Perancangan Sistem",
        "Implementasi Sistem (Coding)",
        "Pengujian dan Evaluasi",
        "Penyusunan Laporan",
    ]

    for idx, stage in enumerate(stages, 1):
        st.markdown(f"**{idx}. {stage}**")

    st.markdown("---")
    st.markdown("### Metode Perancangan (Prototyping)")
    st.markdown(
        """
        - **Listen to Customer:** wawancara pemilik Keday 70 untuk identifikasi kebutuhan inti.
        - **Build/Revise Mock-up:** rancang layout dashboard yang mudah dipahami.
        - **Customer Test Drives Mock-up:** lakukan uji coba langsung dengan data asli.
        - **Evaluasi dan Perbaikan:** revisi berulang sampai sesuai kebutuhan operasional.
        """
    )
