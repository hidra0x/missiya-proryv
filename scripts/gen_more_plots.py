import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Загружаем данные
df = pd.read_csv(r"C:\Users\Артем\gwtc2_all.csv", decimal=",")

# --- ГРАФИК 1: Масса-Масса ---
fig, ax = plt.subplots(figsize=(10, 7))
ax.scatter(df["mass_1_source"], df["mass_2_source"], s=df["network_matched_filter_snr"]*5, 
           c="steelblue", alpha=0.7, edgecolors="black", label="События GWTC-2.1")
anom_names = ["GW190814", "GW190521", "GW190403_051519", "GW190426_190642"]
anom_df = df[df["commonName"].isin(anom_names)]
ax.scatter(anom_df["mass_1_source"], anom_df["mass_2_source"], s=anom_df["network_matched_filter_snr"]*10, 
           c="red", marker="*", edgecolors="black", label="Аномалии")

for _, r in anom_df.iterrows():
    ax.annotate(r["commonName"], (r["mass_1_source"], r["mass_2_source"]), 
                textcoords="offset points", xytext=(10, 5), fontsize=9, color="darkred", fontweight="bold")

ax.plot([0, 150], [0, 150], 'k--', alpha=0.3, label="m1 = m2")
ax.set_xlabel("Масса компонента 1 (M☉)", fontsize=12)
ax.set_ylabel("Масса компонента 2 (M☉)", fontsize=12)
ax.set_title("Миссия «Прорыв»: Диаграмма масс слияний", fontsize=14, fontweight="bold")
ax.set_xlim(0, 120)
ax.set_ylim(0, 100)
ax.grid(True, linestyle="--", alpha=0.5)
ax.legend()
plt.tight_layout()
plt.savefig(r"C:\Users\Артем\mass_diagram.png", dpi=150)
print("Готово: mass_diagram.png")

# --- ГРАФИК 2: 3D-Карта ---
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
np.random.seed(42)
x = df["luminosity_distance"] * np.cos(np.random.uniform(0, 2*np.pi, len(df)))
y = df["luminosity_distance"] * np.sin(np.random.uniform(0, 2*np.pi, len(df)))
z = df["network_matched_filter_snr"]
ax.scatter(x, y, z, c=df["mass_1_source"], cmap="viridis", s=50, alpha=0.7, edgecolors="black")
ax.set_xlabel("X (Мпк)")
ax.set_ylabel("Y (Мпк)")
ax.set_zlabel("SNR")
ax.set_title("Миссия «Прорыв»: 3D-облако событий", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.savefig(r"C:\Users\Артем\3d_sky_map.png", dpi=150)
print("Готово: 3d_sky_map.png")

# --- ГРАФИК 3: Гистограмма масс ---
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(df["mass_1_source"], bins=20, color="skyblue", edgecolor="black", alpha=0.7, label="Компонент 1")
ax.hist(df["mass_2_source"], bins=20, color="salmon", edgecolor="black", alpha=0.5, label="Компонент 2")
ax.axvline(2.6, color="red", linestyle="dashed", linewidth=2, label="GW190814 (аномалия, 2.6 M☉)")
ax.set_xlabel("Масса (M☉)")
ax.set_ylabel("Количество событий")
ax.set_title("Миссия «Прорыв»: Распределение масс", fontsize=14, fontweight="bold")
ax.legend()
ax.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig(r"C:\Users\Артем\mass_histogram.png", dpi=150)
print("Готово: mass_histogram.png")
