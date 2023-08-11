#function for printing bill

def print_new_bill(laptop_directory,name,phone,):

        filename =  str(name) + ".txt"
                    
        with open(filename,'w') as file_purchase:
                        file_purchase.write("\n\n\n----------------------------------------------------------------------------------\n")
                        file_purchase.write("\t\t\t\tInvoice\n")
                        file_purchase.write("----------------------------------------------------------------------------------\n")
                        print("\t \t \t TechExchange: The Laptop Trading Co.")
                        print("\n")
                        print("\t Machapokhari, Kathmandu    |   Phone No 9821326444 ")
                        print("\n")
                        file_purchase.write("\nName of customer: "+str(name)+"\n")
                        file_purchase.write("Phone number of customer: "+str(phone)+"\n")
                        file_purchase.write("\n")
                        file_purchase.write("----------------------------------------------------------------------------------\n")
                        
                        file_purchase.write("----------------------------------------------------------------------------------\n")
                        file_purchase.write("\n\nProduct name\t quantity  Unit Price  net amount   Total\n")
                        file_purchase.write("\n")
                        for i in laptop_directory.values():
                                file_purchase.write(str(i[0])+"\t    "+str(i[1])+"\t      "+str(i[2])+"\t    "+str(i[3])+"\t      "+str(i[4])+"\n")
                                 