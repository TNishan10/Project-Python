from datetime import datetime
print("\n")
print("\n")
print("\t \t \t \t \t \t  Nishan Electronics")
print("\n")
print("\t \t \t \t Kamalpokhari, Kathmandu | Phone No 9821326444 ")
print("\n")

print("---------------------------------------------------------------------")
print("\t \t \t \t  Welcome to system Admin! I hope you have a good day!")
print("---------------------------------------------------------------------")    

file = open("laptop.txt","r")
laptop_id=1
mydict={}
for line in file:
     line = line.replace("\n","")
     mydict.update({laptop_id: line.split(",")})
     laptop_id+=1

file.close()
print(mydict)
continueLoop = True

while continueLoop == True:
    print("Press 1 to buy from Manufacturer ")
    print("Press 2 to sell to customer ")
    print("Press 3 to exit from system 1 ")
    
    userinput = int(input("Enter from option "))
    print("----------------------------------------------------------------------")
    if userinput == 1:
        print("Thank you for buying ")
        print("----------------------------------------------------------------------")
        print("We will need your name and number to print bill")
        print("\n")
        name=input("Enter your name: ")
        phone=int(input("Enter your phone number: "))
        print("S.N \t\t Laptop Name        Company Name       Price\t   Quantity")
        print("----------------------------------------------------------------------")

        file= open("laptop.txt","r")
        a=1
        for line in file:
            print(a,"\t\t"+line.replace(",","\t\t"))
            a+=1
        print("----------------------------------------------------------------------")
        file.close()
        print("\n")

        valid_id = int(input("Please provide the ID of the Laptop you want to buy: "))
        print("\n")

        #Valid_ID

        while valid_id <= 0 or valid_id > len(mydict):
            print("Please provide a valid Laptop ID!!")
            print("\n")

            valid_id = int(input("Please provide the ID of the Laptop you want to buy: "))
            
        user_quantity = int(input("Please provide the quantity of the Laptop you want to buy: "))
        print("\n")


        #Valid_Quantity

        get_quantity=mydict[valid_id][3]

        while user_quantity <= 0 or user_quantity > int(get_quantity):

            print("Dear Admin, the quantity you looking for is not available. Please provide a valid number: ")

            print("\n")

            user_quantity = int(input("Please provide the quantity of the Laptop you want to buy: "))
        print("\t")

        #Update the text file

        mydict[valid_id][3] = int(mydict[valid_id][3])-int(user_quantity)

        file = open("laptop.txt","w")

        for values in mydict.values():
            file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4]))
            file.write("\n")
        file.close()


        #getting user purchased items

        productko_naam = mydict[valid_id][0]
        quantity_userle_deko = user_quantity
        unit_price_eutako = mydict[valid_id][2]
        price_of_itemkunai_eutako = mydict[valid_id][2].replace("$","")
        jammaprice = int(price_of_itemkunai_eutako)*int(quantity_userle_deko)

        userle_kineko_dictionary = []
        userle_kineko_dictionary.append([productko_naam, quantity_userle_deko, unit_price_eutako, price_of_itemkunai_eutako, jammaprice])
        
        shipping_cost = (input("Do you want your laptop to be shipped? "))

        if shipping_cost == "yes":
            print("Yes! Its Shipped")
        else:
            print("No Shipping required")
    elif userinput == 2:
        print("Thank you for selling ")
        print("\n")
       
        
        #shipping

        userle_kineko = []
        userle_kineko.append([laptopko_naam, userle_deko_quantity, eutako_price, total_price])
        shipping_cost = input("Dear user do you want your laptop to be shipped?")
        if shipping_cost == "Y":
            total = 0
            shipping_cost = 1500
        for i in userle_kineko:
            total+=int(i[3])
        grand_total = total + shipping_cost
        today_date_and_time = datetime.now()
        print("\n")
        print("\t \t \t laptop, Shop Bill ")
        print("\n")
        print("\t \t Kamalpokhari, Kathmandu | Phone No: 9811112255")
        print("\n")
        print("-------------------------------------------------------------------")
        print("Laptop Details are: ")
        print("-------------------------------------------------------------------")
        print("Name of the customer: "+ str(name))
        print("Contact number: "+ str(phone))
        print("Date and time of purchase: "+ str(today_date_and_time))
        print("-------------------------------------------------------------------")
        print("\n")
        print("Purchase Detail are: ")











        
