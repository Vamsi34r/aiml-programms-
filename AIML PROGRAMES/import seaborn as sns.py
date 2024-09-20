import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('iris')
df.head()

sns.boxplot( y=df["sepal_length"] );
sns.boxplot( x=df["species"], y=df["sepal_length"] )
iris = sns.load_dataset("iris")
sns.catplot(data=iris, orient="h", kind="box");