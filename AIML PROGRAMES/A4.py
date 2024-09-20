import seaborn as sns
tips = sns.load_dataset('tips')
tips.head()
tips.plot()

tips['total_bill'].plot()