def sell()

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
