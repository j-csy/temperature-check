#def user_input():
  # Prompt for a value
    #inputValue = int(input("1.Please provide a temperature measurement : >> "))
    #items = list(range(3))
    #items = [inputTemp]
    #print (items) 
    #return items;

def main():
    #Threshold

    user1 = 30
    user2 = 90
    
    inputTemp = int(input("1.Please provide a temperature measurement : >> "))
   
    items = []
    items = [inputTemp]
    curTemp = 0
    

    #user_input()
    
    while True:
        try:
            

            #print ("Last value : " + str(items[-1])) 
            #print ("List length : " + str(len(items)) )
            #print (items)
            #print (inputTemp)
            
            if int(items[-1]) < user1:
                print ("WARNING : Temperature below a threshold (30C) !!! ")
                #items = []
                #curTemp = 0
                break
            elif int(items[-1]) > user2:
                print ("WARNING : Temperature is above a threshold (90C) !!! ")
                #items = []
                #curTemp = 0
                break

            else:  
                #print ("     value - 20 = " + str(int(items[-1]) - 20))
                #print ("     value + 20 = " + str(int(items[-1]) + 20))
                
                print ("     value -1 = " + str(items[-1]) )
                print ("     value curTemp = " + str(curTemp))
                if curTemp != 0 : 
                    print ("     value -2 = " + str(items[-2]) )
                #print ("___Temperature within acceptable range___\n" )
                if curTemp != 0:
                    if int(items[-2]) > (curTemp + 20) :
                        print ("ALARM!! :  DECREASE more than 20C !!! ")
                        #break
                    elif int(items[-2]) < (curTemp - 20) :
                        print ("ALARM!! :  INCREASE more than 20C !!! ")
                        #break
            
        
                    
            curTemp = int(input("Please provide a temperature measurement : >> "))
            print ("Curent Temperature is " + str(curTemp) + "C")
            items.append(curTemp)
            #print (items)
            
        except KeyboardInterrupt:
            print("Hard Exit Initiated. Goodbye!")
 
main()
