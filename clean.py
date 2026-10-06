import pandas as pd

df=pd.read_csv("data/project8_ab_testing_conversion.csv")
c=['User_ID', 'Group', 'Device', 'Country', 'Age', 'Visits', 'Pages_Viewed', 'Session_Duration', 'Converted', 'Revenue']
df.columns=df.columns.str.strip().str.title()
df=df.drop_duplicates()
device_fill = df['Device'].mode()
df['Country']=df['Country'].fillna("Unknown")
df['Device']=df['Device'].fillna("Mobile")
df['Pages_Viewed']=df['Pages_Viewed'].fillna(df['Pages_Viewed'].median())
df['Session_Duration']=df['Session_Duration'].fillna(df['Session_Duration'].median())

fill_age=df['Age'].median()
df.loc[772,'Age']=fill_age
df.loc[4998,'Age']=fill_age
df.loc[8606,'Age']=fill_age
       
print(df[df['Device'].isnull()])
print(device_fill)
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)
print(df.isnull().sum())
print(df.duplicated().sum())
#print(df['Group'].value_counts())
#print(df['Converted'].value_counts())
print(df[df['Age']<=0])
print(df[df['Age']>=100])
print(df['Age'].describe())
print(df['Device'].value_counts())
print(df['Country'].value_counts())
df.to_csv('data/ab_cleaned.csv',index=False)

