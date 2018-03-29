import pandas as pd

df = pd.read_csv("titanic_data_set.csv")
df.head()
#df.shape
#print df.describe()
#print(df.describe(include=['O']))
#print df.isnull().sum()

survived = df[df['Survived']==1]
not_survived = df[df['Survived']==0]
#print 'Survived',survived.head(), '\n\n Not Survived ',not_survived.head()
# print "Survived: %i (%f%%)" % (len(survived), float(len(survived))/len(df)*100.0)
# print "Not Survived: %i (%f%%)" % (len(not_survived), float(len(not_survived))/len(df)*100.0)
# print "Total : %i" % len(df)

# print df.Pclass.value_counts()

# print df.groupby('Pclass').Survived.value_counts()

#print df.groupby('Survived').Sex.value_counts()