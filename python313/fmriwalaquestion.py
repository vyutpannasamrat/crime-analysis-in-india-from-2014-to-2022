import matplotlib.pyplot as plt
import seaborn as sns
fmri = sns.load_dataset("fmri")
print(fmri.info())
sns.lineplot(x="timepoint",y="signal",data=fmri,hue="event", style="region",markers =True)
plt.show()

