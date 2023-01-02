#dictionary of drinks
#item = i, stock=st, price = p

d1={"i": "Iced tea", "st":10, "p":3.5}
d2={"i": "Coffee", "st":15,"p":5}
d3={"i": "Carbonated drinks", "st":15, "p":4.5}
d4={"i": "Beer", "st":15, "p" :9}
d5={"i": "Water", "st":15, "p" :1}
d6={"i": "Juice", "st":15, "p" :2}

#dictionary of chips
cps1={"i": "Potato chips", "st":15, "p":2.5}
cps2={"i":"Corn chips", "st":15, "p":3.5}
cps3={"i": "Flavoured chips", "st":15, "p" :1}
cps4={"i": "Oven baked chips", "st":15, "p" :5}

#dictionary of snacks
s1={"i":"Mixed nuts","st":15, "p" :2.5}
s2={"i": "Popcorn", "st":15, "p":2.5}
s3={"i": "Pretzels", "st":15, "p" :2}
s4={"i": "Candy", "st":10, "p":1.5}

#dictionary of chocolates
c1={"i": "Milk chocolate", "st":15, "p":4.5}
c2={"i": "Dark chocolate", "st":15, "p" :6}
c3={"i": "White chocolate", "st":15, "p":5}
c4={"i": "Mixed nuts chocolate", "st":15, "p":2.5}

d=[d1,d2,d3,d4,d5,d6]
c=[cps1,cps2,cps3,cps4]
s=[s1,s2,s3,s4]
ch=[c1,c2,c3,c4]
vm=[d,c,s,ch]
total=0 #input
stock_input=0
stock=270


#greeting the user when pressing the insert button
print("WECLOME TO ALWAYS HUNRGY SNACK MACHINE VENDING MACHINE!")


while True:
    opt=int(input('''PLEASE SELECT ONE OF THE CATEGORY'S. MENU:
1 - DRINKS
2 - CHIPS
3 - SNACKS
4 - CHOCOLATES
0 - FINISH ORDER
Please enter your choice : '''))
    if opt==1: #option
            print('''HERE'S THE MENU OF THE DRINKS THAT ARE AVAILABLE:
 ________________________________
| NO |       ITEM        | PRICE |
|____|___________________|_______|
|1   |ICE TEA            |3.5    |
|2   |COFFEE             |5      |
|3   |CARBONATED DRINKS  |4.5    |
|4   |BEER               |9      |
|5   |WATER              |1      |
|6   |JUICE              |2.5    |
|____|___________________|_______|''')

          

            def choose():
                inp=0
                cho=int(input("Please enter the Item id: ")) #choice
                if cho==1:
                    st=d1.get("st")
                    if st<=0:
                        print("Sorry, item is out of stock.")
                    else:
                        inp+=d1.get("p")                  
                        d1.update({"st":st-1})
                        
                elif cho==2:
                    st=d2.get("st")
                    if st<=0:
                        print("Sorry, item is out of stock.")
                    else:
                        inp+=d2.get("p")                  
                        d2.update({"st":st-1})
                        
                elif cho==3:
                    st=d3.get("st")
                    if st<=0:
                        print("Sorry, item is out of stock.")
                    else:
                        inp+=d3.get("p")                  
                        d3.update({"st":st-1})
                        
                elif cho==4:
                    st=d4.get("st")
                    if st<=0:
                        print("Sorry, item is out of stock.")
                    else:
                        inp+=d4.get("p")                  
                        d4.update({"st":st-1})
                        
                elif cho==5:
                    st=d5.get("st")
                    if st<=0:
                        print("Sorry, item is out of stock.")
                    else:
                        inp+=d5.get("p")                  
                        d5.update({"st":st-1})
                        
                elif cho==6:
                    st=d6.get("st")
                    if st<=0:
                        print("Sorry, item is out of stock.")
                    else:
                        inp+=d6.get("p")                  
                        d6.update({"st":st-1})
                        
                else:
                    print("Option unavailable.")
                return inp
            total+=choose()

            while True:
                opt2=input("Any more drinks? (y/n) ==> ") #option 2 
                if opt2.lower()=="y":
                    total+=choose()
                elif opt2.lower()=="n":
                    break
                else:
                    print("Please enter a valid option.")
                

    elif opt==2:
        print('''HERE'S THE MENU OF THE CHIPS THAT ARE AVAILABLE:
 ________________________________
| NO |       ITEM        | PRICE |
|____|___________________|_______|
|1   |POTATO CHIPS       |1.5    |
|2   |CORN CHIPS         |3.5    |
|3   |FLAVOURED CHIPS    |1      |
|4   |OVEN BAKED CHIPS   |5      |
|____|___________________|_______|''')

       
        def choose():
            inp=0
            cho=int(input("Enter item id of the chips you'd like to order: ")) #choice
            if cho==1:
                st=cps1.get("st")
                if st<=0:
                    print("Sorry, item is out of stock.")
                else:
                    inp+=cps1.get("p")                  
                    cps1.update({"st":st-1})

            elif cho==2:
                st=cps2.get("st")
                if st<=0:
                    print("Sorry, item is out of stock.")
                else:
                    inp+=cps2.get("p")                  
                    cps2.update({"st":st-1})

            elif cho==3:
                st=cps3.get("st")
                if st<=0:
                    print("Sorry, item is out of stock.")
                else:
                    inp+=cps3.get("p")                  
                    cps3.update({"st":st-1})

            elif cho==4:
                st=cps4.get("st")
                if st<=0:
                    print("Sorry, item is out of stock.")
                else:
                    inp+=cps4.get("p")                  
                    cps4.update({"st":st-1})

            else:
                print("Option unavailable.")
            return inp
        total+=choose()

        while True:
            opt2=input("Any more chips? (y/n) ==> ")
            if opt2.lower()=="n":
                break
            elif opt2.lower()=="y":
                total+=choose()
            else:
                print("Please enter a valid option.")

    elif opt==3:
        print('''HERE'S THE MENU OF THE SNACKS THAT ARE AVAILABLE:
 ________________________________
| NO |       ITEM        | PRICE |
|____|___________________|_______|
|1   |MIXED NUTS         |2.5    |
|2   |POPCORN            |2.5    |
|3   |PRETZELS           |2      |
|4   |CANDY              |1.5    |
|____|___________________|_______|''')

       
        def choose():
            inp=0
            cho=int(input("Enter NO. of the snack you'd like to order: ")) #choice
            if cho==1:
                st=s1.get("st")
                if st<=0:
                    print("Sorry, item is out of stock.")
                else:
                    inp+=s1.get("p")                  
                    s1.update({"st":st-1})

            elif cho==2:
                st=s2.get("st")
                if st<=0:
                    print("Sorry, item is out of stock.")
                else:
                    inp+=s2.get("p")                  
                    s2.update({"st":st-1})

            elif cho==3:
                st=s3.get("st")
                if st<=0:
                    print("Sorry, item is out of stock.")
                else:
                    inp+=s3.get("p")                  
                    s3.update({"st":st-1})

            elif cho==4:
                st=s4.get("st")
                if st<=0:
                    print("Sorry, item is out of stock.")
                else:
                    inp+=s4.get("p")                  
                    s4.update({"st":st-1})
            else:
                print("Option unavailable.")
            return inp
        total+=choose()

        while True:
            opt2=input("Any more snacks? (y/n) ==> ")
            if opt2.lower()=="n":
                break
            elif opt2.lower()=="y":
                total+=choose()
            else:
                print("Please enter a valid option.")

    elif opt==4:
        print('''HERE'S THE MENU OF THE CHOCOLOATES THAT ARE AVAILABLE:
 ___________________________________
| NO |       ITEM           | PRICE |
|____|______________________|_______|
|1   |MILK CHOCOLATE        |5.5    |
|2   |DARK CHOCOLATE        |6      |
|3   |WHITE CHOCOLATE       |4.5    |
|4   |MIXED NUTS CHOCOLATE  |2.5    |
|____|______________________|_______|''')

       
        def choose():
            inp=0
            cho=int(input("Enter NO. of the chocolate you'd like to order: ")) #choice
            if cho==1:
                st=c1.get("st")
                if st<=0:
                    print("Sorry, item is out of stock.")
                else:
                    inp+=c1.get("p")                  
                    c1.update({"st":st-1})

            elif cho==2:
                st=c2.get("st")
                if st<=0:
                    print("Sorry, item is out of stock.")
                else:
                    inp+=c2.get("p")                  
                    c2.update({"st":st-1})

            elif cho==3:
                st=c3.get("st")
                if st<=0:
                    print("Sorry, item is out of stock.")
                else:
                    inp+=c3.get("p")                  
                    c3.update({"st":st-1})

            elif cho==4:
                st=c4.get("st")
                if st<=0:
                    print("Sorry, item is out of stock.")
                else:
                    inp+=c4.get("p")                  
                    c4.update({"st":st-1})

            else:
                print("Option unavailable.")
            return inp

        total+=choose()

        while True:
            opt2=input("Any more chocolates? (y/n) ==> ")
            if opt2.lower()=="n":
                break
            elif opt2.lower()=="y":
                total+=choose()
            else:
                print("Please enter a valid option.")

    elif opt==0:
        print("Processing order...")
        break
    
    else:
        print("Option Unavailable.")
            
print("Total = ", total)
pay=float(input("Insert money : "))
if pay<total:
    print("Insufficient funds.")
elif total<pay:
    change=pay-total
    print("Here's your change : ",change)
    print("Please collect your purchases from the box below.")
    print("Thank you, Goodbye!!")
else:
    print("Please collect your purchases from the box below.")
    print("Thank you, Goodbye!!")
    



        
        
                    
            

            









