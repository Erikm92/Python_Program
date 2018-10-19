#Data Analytics using an csv file pulled from Yahoo ranging from the date of 4/6/2017 to 5/5/2017

#Objectives: To compare the vix with Dow Jones, s%p500, and Nasdaq so see the effects it has had on these indexes
# based on volatitly and percentage increase or decrease along with volume traded. 

#%%
import pandas
import matplotlib.pyplot as plt

data=pandas.read_csv('^VIX.csv')
datad=pandas.read_csv('^DJI.csv')
datas=pandas.read_csv('^GSPC.csv')
datan=pandas.read_csv('^IXIC.csv')

print("data for vix")
print(data)
print("data for dow")
print(datad)
print("data for s%p")
print(datas)
print("data for nasdaq")
print(datan)
#print(datan)
#print(len(data))
#print(len(data.columns))
#print(data.columns)


dfb=pandas.DataFrame(data,columns=["Date","Open","Close"])
#vix file
dfb1=pandas.DataFrame(datad,columns=["Date","Open","Close","Volume"])
#dow file
dfb2=pandas.DataFrame(datas,columns=["Date","Open","Close","Volume"])
#s&p500
dfb3=pandas.DataFrame(datan,columns=["Date","Open","Close","Volume"])
#nasdaq


dfb["Open"]=pandas.to_numeric(dfb["Open"])
dfb["Close"]=pandas.to_numeric(dfb["Close"])

dfb1["Open"]=pandas.to_numeric(dfb1["Open"])
dfb1["Close"]=pandas.to_numeric(dfb1["Close"])

dfb2["Open"]=pandas.to_numeric(dfb2["Open"])
dfb2["Close"]=pandas.to_numeric(dfb2["Close"])

dfb3["Open"]=pandas.to_numeric(dfb3["Open"])
dfb3["Close"]=pandas.to_numeric(dfb3["Close"])

dfb1["Volume"]=pandas.to_numeric(dfb1["Volume"])
dfb2["Volume"]=pandas.to_numeric(dfb2["Volume"])
dfb3["Volume"]=pandas.to_numeric(dfb3["Volume"])


# This is for finding % of vix (dfb)

vixOpenList=[]
for y in dfb["Open"]:
    vixOpenList.append((y))

vixCloseList=[]
for y in dfb["Close"]:
    vixCloseList.append((y))

per=[]
amt = 21                 
for y in range((amt)):  
    per.append(float((vixCloseList[y]*100)/vixOpenList[y]-100)) #convert into %


#This is for finding % of dow jones (dfb1)

dowOpenList=[]
for y in dfb1["Open"]:
    dowOpenList.append((y))

dowClosedList=[]
for y in dfb1["Close"]:
    dowClosedList.append((y))

amt1=21
perDow=[]  
for y in range((amt1)):   
    perDow.append(float((dowClosedList[y]*100)/dowOpenList[y]-100)) #convert into %


#This finds % of s&p 500 (dfb2)

snpOpenList=[]
for y in dfb2["Open"]:
    snpOpenList.append((y))

snpClosedList=[]
for y in dfb2["Close"]:
    snpClosedList.append((y))

amt2=21
perSnP=[]  
for y in range((amt2)):   
    perSnP.append(float((snpClosedList[y]*100)/snpOpenList[y]-100))


#This is for finding % of nasdaq (dfb3)

nasdaqOpen=[]
for y in dfb3["Open"]:
    nasdaqOpen.append((y))

nasdaqClosed=[]
for y in dfb3["Close"]:
    nasdaqClosed.append((y))

amt3=21
perNasdaq=[]  
for y in range((amt3)):   
    perNasdaq.append(float(nasdaqClosed[y]*100)/nasdaqOpen[y]-100)


#--------This ends finding %s------------
#--------This starts to use graphs-------
import seaborn 

y=0

dow=[]
nas=[]
sandp=[]
dowstr="DowJones"
nasstr="Nasdaq"
sandpstr="S%P500"
#creating a list of 21 elements for each index(dow,ect)
for x in range(amt):
    dow.append(dowstr)
    nas.append(nasstr)
    sandp.append(sandpstr)
    
#print(dow)
#print(nas)
#print(sandp)

#this adds list/column index to a dataframe 
inp1=pandas.Series(dow)
dfb1['Index']=inp1.values

inp2=pandas.Series(sandp)
dfb2['Index']=inp2.values

inp3=pandas.Series(nas)
dfb3['Index']=inp3.values


#this addes percent to dataframes
se=pandas.Series(per)
dfb['Percent']=se.values

se1=pandas.Series(perDow)
dfb1['Percent']=se1.values

se2=pandas.Series(perSnP)
dfb2['Percent']=se2.values

se3=pandas.Series(perNasdaq)
dfb3['Percent']=se3.values

print("Data frame for VIX after updates on Percentage")
print(dfb)
print("")
print("Data Frame for DOW after updates on index and Percentage ")
print(dfb1)
print("")
print("Data Frame for S&P500 after updates on index and Percentage ")
print(dfb2)
print("")
print("Data Frame for Nasdaq after updates on index and Percentage ")
print(dfb3)


#graphs based on volume vs Percent change 
seaborn.distplot(dfb["Percent"]) 


plt.xlabel("Percentage change")
plt.title("Distribution Plot for VIX % change")

seaborn.lmplot(x='Volume',y='Percent',hue="Index",data=dfb1) 

seaborn.lmplot(x='Volume',y='Percent',hue="Index",data=dfb2) 

seaborn.lmplot(x='Volume',y='Percent',hue="Index",data=dfb3) 




newdf=pandas.concat([dfb1,dfb2,dfb3],ignore_index=True) #concatinates data onto one dataframe** 



seaborn.lmplot(x='Volume',y='Percent',hue="Index",data=newdf) 

#Based on the findings, it would seem that the Vix has had a higher increase in volatility in the last 21 days
#which is shown in the DowJones as a positive effect,
#the S&p500 has shown a neutral effect, and the Nasdaq500 has shown a negative effect

#the s&p500 has a neutral volume change based on % variation throughout 
#the dowjones has the most volume change based on % variation
#the nasdaq500 has the least volume change based on % variation