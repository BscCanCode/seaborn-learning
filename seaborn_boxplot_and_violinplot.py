import seaborn as sns
import matplotlib.pyplot as plt

print(sns.get_dataset_names())

#loadset

df = sns.load_dataset("iris")
print(df)

sns.boxplot(x = "species", y = "sepal_length", data=df)
plt.xlabel("Species")
plt.ylabel("Sepal_length")
plt.title("species vs sepal_length")
plt.show()


sns.violinplot(x = "species", y = "sepal_length", data=df)
plt.xlabel("Species")
plt.ylabel("Sepal_length")
plt.title("species vs sepal_length")
plt.show()