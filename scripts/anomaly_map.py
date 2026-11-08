import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\Артем\gwtc2_all.csv", decimal=",")
anom_names = ["GW190814", "GW190521", "GW190403_051519", "GW190426_190642"]
df["is_anom"] = df["commonName"].isin(anom_names)

fig, ax = plt.subplots(figsize=(11, 6))
normal = df[~df["is_anom"]]
anom = df[df["is_anom"]]

ax.scatter(normal["luminosity_distance"], normal["network_matched_filter_snr"],
           s=normal["mass_1_source"]*3, c="steelblue", alpha=0.6, edgecolors="black", label="обычные события")
ax.scatter(anom["luminosity_distance"], anom["network_matched_filter_snr"],
           s=anom["mass_1_source"]*3, c="red", alpha=0.9, edgecolors="black", marker="*", label="аномалии")

for _, r in anom.iterrows():
    ax.annotate(r["commonName"], (r["luminosity_distance"], r["network_matched_filter_snr"]),
                textcoords="offset points", xytext=(8, 8), fontsize=9, color="darkred", fontweight="bold")

ax.set_xlabel("Расстояние (Мпк)")
ax.set_ylabel("SNR")
ax.set_title("Миссия «Прорыв»: карта аномалий GWTC-2.1\nкрасные звёзды = необъяснённые события")
ax.grid(True, linestyle="--", alpha=0.4)
ax.legend()
plt.tight_layout()
plt.savefig(r"C:\Users\Артем\anomaly_map.png", dpi=150)
print("Готово: C:\\Users\\Артем\\anomaly_map.png")
