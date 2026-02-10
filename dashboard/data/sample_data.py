import numpy as np
import pandas as pd


def build_dataset(days: int = 60) -> pd.DataFrame:
    rng = np.random.default_rng(70)
    dates = pd.date_range(end=pd.Timestamp.today().normalize(), periods=days)

    omzet = rng.integers(1_800_000, 4_500_000, size=days)
    hpp = (omzet * rng.uniform(0.50, 0.62, size=days)).astype(int)
    operasional = rng.integers(350_000, 950_000, size=days)
    transaksi = rng.integers(65, 155, size=days)

    data = pd.DataFrame(
        {
            "Tanggal": dates,
            "Omzet": omzet,
            "HPP": hpp,
            "Biaya Operasional": operasional,
            "Total Transaksi": transaksi,
        }
    )
    data["Laba Kotor"] = data["Omzet"] - data["HPP"]
    data["Laba Bersih"] = data["Laba Kotor"] - data["Biaya Operasional"]
    return data
