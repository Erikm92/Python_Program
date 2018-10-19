#Google Finance--Table Updates (Data Preparation) //works on the old version of google finance webpage

#Objective: To retrieve world stocks, currencies and bonds from google.com/finance
#           by uploading data into strings and converting it into lists and outputting them 
#           in a specific order. 


from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests
import datetime



#this will open the url

r = requests.get('https://www.google.com/finance')
c=r.text

soup = BeautifulSoup(c, 'html.parser')

#finds tag tables under class=quotes
getTags=soup.find_all("table", class_="quotes")


#implementing a menu for user

print("Hello, this program allows you to view the following: ")
print("Live World Markets       Type 1")
print("Live World Currencies    Type 2")
print("Live Bonds               Type 3")
print("If you wish to view them all Type 4")

validate="x"
while validate=="x" :
    userinput=int(input("Please enter the number for which you wish to view: "))
    if (userinput==1 or userinput==2 or userinput==3 or userinput==4):
        print("you have chosen, ", userinput)
        validate="y"
    else:
        print("you have not chosen a correct input, please try again: ")
        #if userinput 1 then show world markets 
        #if userinput 2 then show world currencies
        #if userinput 3 then show live bonds
        #if userinput 4 then show all 

    
    if userinput==1 or userinput==4:


        todaytime=datetime.datetime.now().strftime("%I:%M:%S")
        todaydate=datetime.datetime.now().strftime("%d/%m/%Y")
        print("World Market based on Todays date", todaydate, "and time: ", todaytime)
        print("Current Market        Value          Percent(1day change) ")

    
        aString=""
        for element in getTags[0]: #The element of 0 retrieves the world market data table
       

            aString+=(element.get_text()) #This turns data findings into a full string 

        print("---------------------------------------------------")

    
        strtry=""
        for char in aString:        # For each element 'char' in the string 'aString', the data will be split
            strtry=aString.split() 
        
        splitStr=[]
        for char in strtry:         # This adds each split element into a new string all together 
            splitStr.append(char)   # The order is based on the way they were found from the website

                                    # SplitStr.remove: removes a specific index from the list to make them match in order
        splitStr.remove("Seng")     # With that, each world market can have the order of: 
        splitStr.remove("Index")    # 1-- name, 2--price, 3--change in perentage & 4--overall change
                                    # The next world market would have the same order
        splitStr.remove("225")      # This also allows for us to split the lists into 4 different lists
        splitStr.remove("100")      
        splitStr.remove("STOXX")
        splitStr.remove("50")
        splitStr.remove("40")
        splitStr.remove("TSX")
        splitStr.remove("200")
        splitStr.remove("Sensex")
        splitStr.remove("Composite")
   

        marketName=[]                    # The next 4 statements seperate split data into 4 different lists.
        for ti in (splitStr[0:83:4]):    # To be able to manipulate them accordingly, this means:             
            marketName.append(ti)        # marketName, price, priceChange, perChange will give us 
                                         # the market name, price, change in price and change in percentage
        price=[]
        for ti in (splitStr[1:83:4]):    # This statement is a list of world mkt. prices
            price.append(ti)
    
        priceChange=[]
        for ti in (splitStr[2:83:4]):    # This statement is a list of changes in market prices
            priceChange.append(ti)

        perChange=[]
        for ti in (splitStr[3:84:4]):    # This statement is a list of world mkt. percent changes)

            perChange.append(ti)
    
        rows=21                          # 21 rows for the table
        for chars in range((rows)):      # This allows for specific spacing in our print statement
            if (len(marketName[chars]))==6:
                spacing="              "
            elif(len(marketName[chars]))==7:
                spacing="             "
            elif(len(marketName[chars]))==8:
                spacing="            "
            elif(len(marketName[chars]))==4:
                spacing="                "
            elif(len(marketName[chars]))==3:
                spacing="                 "
            if (len(price[chars]))==8:
                spacing2="     "
            else:
                spacing2="    "
    
            print((marketName[chars]),spacing,(price[chars]),spacing2,(priceChange[chars]),(perChange[chars]))
    

    #The start of currencies

    if userinput==2 or userinput==4:
        a2ndString=""
        for element in getTags[1]:
            a2ndString+=(element.get_text())

        strtry1=""
    
        for char in a2ndString:          # Same process as before but, in this case, we don't need to
            strtry1=a2ndString.split()   # delete elements due to having a perfect ratio of 4 for each

        splitStr1=[]
        for char in strtry1:
            splitStr1.append(char)

        countryName=[]
        for ti in (splitStr1[0:32:4]):  # List of country names
            countryName.append(ti)

        moneyPrice=[]
        for ti in (splitStr1[1:32:4]):  # List of currency prices
            moneyPrice.append(ti)

        moneyChange=[]
        for ti in (splitStr1[2:32:4]):  # List of currency price changes
            moneyChange.append(ti)

        moneyPercent=[]
        for ti in (splitStr1[3:31:4]):  # List of currency price percent changes
            moneyPercent.append(ti)
            
        print("---------------------------------------------------")
        print("World Currencies based on Todays date", todaydate, "and time: ", todaytime)       
        print("Currencies            Value        (1day)%change  ")
        print("---------------------------------------------------")

        currencies=6                    # 6 currencies in total, printed in order
        for y in range(currencies):
            print(countryName[y],"             ",moneyPrice[y],"     ",moneyChange[y], moneyPercent[y]) 


    #this starts off bonds
    if userinput==3 or userinput==4:
        print("  ")
    #This starts bonds
        a3rdString=""
        for element in getTags[2]:
            a3rdString+=(element.get_text())
    
        strtry3=""
    
        for char in a3rdString:       # for each element in the string, a3rdString they will be split
            strtry3=a3rdString.split() 

        splitStr2=[]
        for char in strtry3:        
            splitStr2.append(char) 

        num=[]
        time=[]
        bondPer=[]
        bondChange=[]
        bondPerChange=[]

        for u in (splitStr2[0:30:5]):
            num.append(u)
        for u in (splitStr2[1:30:5]):
            time.append(u)
        for u in (splitStr2[2:30:5]):
            bondPer.append(u)

        for u in (splitStr2[3:30:5]):
            bondChange.append(u)
        for u in (splitStr2[4:30:5]):
            bondPerChange.append(u)



        print("---------------------------------------------------")
        print("Bonds based on Todays date", todaydate, "and time: ", todaytime)       
        print("Time            Value Change        (1day)%change  ")
        print("---------------------------------------------------")
        rows1= 6
        for n in range(rows1):
            print(num[n], time[n],"       ",bondPer[n],"             ", bondChange[n], bondPerChange[n])
        