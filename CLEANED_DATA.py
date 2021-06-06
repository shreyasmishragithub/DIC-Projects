import pandas as pd
df1=pd.read_csv('st.csv')


date=[]
df2=pd.DataFrame(df1,columns=["Date","Status","MH"])
print(df2.tail(10))
days=[]
confirmed=[]
recovered=[]
deceased=[]
c=0
for i in df2["Date"]:

    days.append(c)
    c = c + 1

newday=[]
d=0
print(len(days))
for i in days:
    if df2.iloc[i]["Status"] == "Confirmed":
        confirmed.append(df2.iloc[i]["MH"])
    if df2.iloc[i]["Status"]=="Recovered":
        recovered.append(df2.iloc[i]["MH"])
    if df2.iloc[i]["Status"]=="Deceased":
        deceased.append(df2.iloc[i]["MH"])
        d=d+1
        newday.append(d)
print(len(confirmed))
print(len(recovered))
print(len(deceased))

print(len(newday),len(recovered))
raw_dictionary={
    "days":newday,
    "confirmed":confirmed,
    "recovered":recovered,
    "deceased": deceased,
}

df4=pd.DataFrame(raw_dictionary,columns=["days","confirmed","recovered","deceased"])

df4.to_csv("Maharashtra.csv")
