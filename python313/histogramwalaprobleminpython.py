import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")
df.dropna(subset=["Age", "Fare"], inplace=True)
plt.scatter(df["Age"], df["Fare"], alpha=0.5, color='blue')

plt.xlabel("Age")
plt.ylabel("Fare (Total Bill)")
plt.title("Scatter Plot of Fare vs Age on Titanic")
plt.show()
