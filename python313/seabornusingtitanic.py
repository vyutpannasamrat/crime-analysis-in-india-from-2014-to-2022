import seaborn as sns
import matplotlib.pyplot as plt
print
titanic = sns.load_dataset("titanic")
sns.barplot(x="class", y="fare",data = titanic)
xlabel = ("axis a")
ylabel = ("axis b")
plt.show()
