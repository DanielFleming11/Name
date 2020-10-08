

#Boolean while loop to ask for temp. until 999 is inputed 
while True :


#Temp input and conversion
    temp = input("Please enter the current temperature: ")
    temp = int(temp)
    

#Break Statement
    if temp == 999 :
        break


#Reponses
    elif temp > 90 :
        print("Wear Shorts")
        
    elif temp > 70 :
        print("Short sleeves are fine")
        
    elif temp > 50 :
        print("Wear a jacket")
        
    elif temp > 32 :
        print("Wear a heavy coat")
        
    else:
        print("Stay Inside")
        
    

    
        



         
