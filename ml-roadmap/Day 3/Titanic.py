import os
import pandas as pd
import matplotlib.pyplot as plt
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'train.csv')
df = pd.read_csv(csv_path)
df.fillna(df['Age'].median(), inplace=True)
df.to_csv('cleaned_data.csv', index=False)
print(df[['Age']])
print(df.info())
df["Age"].isna()
print(df[["Age","Survived"]].agg(['mean','median']))
def my_cleaning(x):
    x['Age'] = df['Age'].median()
    return x
def my_creation(x):
    x['FamilySize'] = x['SibSp'] + x['Parch'] + 1
    x['IsAlone'] = x['FamilySize'] == 1
    return x
plt.hist([df[df['Survived']==1]['Age'],df[df['Survived']==0]['Age']], bins=40,stacked=True, alpha=0.5, label=['Survived','Not Survived'],density=True)
plt.xlabel('Age')
plt.ylabel('Survial Percentage')
plt.title('Survival Percentage by Age')
plt.legend(['Survived','Not Survived'])
yticks = plt.gca().get_yticks()
plt.gca().set_yticklabels(['{:.0f}%'.format(y*100) for y in yticks])
plt.savefig('Age_Distribution.png')
plt.tight_layout()
plt.show()







