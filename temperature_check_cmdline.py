import requests


def continue_question(question = "[y/n]", strict = True):
    """ Asks the question specified and if the user input is 'yes' or 'y', returns 'yes'.
    If the user input is 'no' or 'n', it returns no.
    If strict is False, many other answers will be acceptable."""

    question = question.strip(" ")
    reply = input("%s " % question)
    reply = reply.lower()
    if (reply == "yes") or (reply == "y") or (not strict and reply in ["yep", "yeah", "sure", "okay", "ok", "definitely", "certainly", "of course"]): 
        return True 
    elif (reply == "no") or (reply == "n") or (not strict and reply in ["nope", "no way", "definitely not", "certainly not", "nah", "of course not"]):
        return False
    else:
         
        return continue_question(strict = strict)
    
def get_weather():
    API_key = "12549cfffc93587bf8216ce33e6739c5"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = "Sydney" 
    Final_url = base_url + "appid=" + API_key + "&q=" + city_name

    weather_data = requests.get(Final_url).json()

    #convert Kelvin to Celsius and round 2 decimals
    curTempC = round(weather_data['main']['temp'] - 273.15)

    return (curTempC)    

def threshold_check(temp):
    #Threshold
    minTemp = 30
    maxTemp = 90
    if int(temp) < minTemp:
        print ("WARNING : Temperature below a threshold (30C) !!! ")
    elif int(temp) > maxTemp:
        print ("WARNING : Temperature is above a threshold (90C) !!! ")
    else:
        print (">>>>> Temperature entered within range 30C - 90C <<<<<")        


def dec_inc_check(newtemp, prevtemp):
    print ("\nCurent Temperature : " + str(newtemp) + "C   ||  " + "Previous Temperature : " + str(prevtemp) + "C")
    
    if prevtemp > (newtemp + 20) :
        print ("########## ALARM!! :  DECREASE > 20C !!! ##########")
    elif prevtemp < (newtemp - 20) :
        print ("########## ALARM!! :  INCREASE > 20C !!! ##########")
    else:
        print (">>>>> ACCEPTABLE Increase/Decrease : No more than 20C <<<<<")

def process_temp():
    curTemp = 0
    again = True
    items = []
    
    inputTemp =  int(input("Please enter initial temperature: "))
    items = [inputTemp]
    print ("Initial Temperature entered: " + str(items[0]) + "C")
    print ("Actual Temperature : " + str(get_weather()) + "C")

    # Verify initial inputTemp threshold 
    threshold_check(inputTemp)
    
    while again:
        curTemp = int(input("\nEnter comparison temperature: "))
        print ("Comparison Temperature entered: " +  str(curTemp)  + "C")
        items.append(curTemp)

        # Verify threshold    
        threshold_check(curTemp)

        # Verify increase/decreas from previous temperature             
        if curTemp != 0:
            dec_inc_check(curTemp, items[-2])

        # Prompt user to continue?
        again = continue_question("\nWould you like to try again? ", strict=False)

 
process_temp()
