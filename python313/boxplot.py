import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

# Sample dataset
np.random.seed(42)
data = pd.DataFrame({
    'Category': np.random.choice(['A', 'B', 'C', 'D'], 100),
    'Values': np.random.randint(1, 100, 100)
})

# Pie Chart Popup
def show_pie_chart(event):
    fig, ax = plt.subplots(figsize=(6, 6))
    data['Category'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
    ax.set_title('Pie Chart of Categories')
    plt.show()

fig, ax = plt.subplots()
ax.set_axis_off()
btn = Button(plt.axes([0.4, 0.4, 0.2, 0.1]), 'Show Pie')
btn.on_clicked(show_pie_chart)
plt.show()

# Diamond Plot (Tracing with line)
plt.figure(figsize=(8, 5))
plt.plot(data.index, data['Values'], marker='D', linestyle='-', color='purple')
plt.title('Diamond Plot of Values (Tracing)')
plt.xlabel('Index')
plt.ylabel('Values')
plt.show()