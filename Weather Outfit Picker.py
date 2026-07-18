#Ask for Today's Temperature
temperature = int(input("Enter Today's temperature in Celsius: "))

#Decide between a Jacket and a T-shirt
if temperature < 20:
    outfit = "Jacket"
    print("You should wear a Jacket today.")
    print("Don't forget to wear a warm jacket!")
else:
    outfit = "T-shirt"
    print("You should wear a T-shirt today.")
    print("Don't forget to stay cool!")

#Ask Weather it is Raining
is_raining = input("Is it raining today? (yes/no): ")

#Add an umbrella remder only if it is raining
if is_raining== "yes": 
    print("Don't forget to take an umbrella with you!")
    print("You should take an umbrella today.")

#Ask for the Wind Speed
wind_speed = int(input("Enter today's wind speed in km/h: "))
#Decide whether is windbreaker is needed or not
if wind_speed > 30:
    need_windbreaker = True
    print("It's quite windy today. You should wear a windbreaker.")
    print("Don't forget to wear a windbreaker to stay protected from the wind!")
else:
    need_windbreaker = False
    print("The wind speed is moderate. A windbreaker is not necessary today.")
    print("You can go without a windbreaker today.")

#Ask whether there are puddles on the ground
has_puddles = input("Are there puddles on the ground? (yes/no): ")

#Decide between boots and sneakers
if has_puddles == "yes":
    footwear = "boots"
    print("Since there are puddles, you should wear boots today.")
    print("Don't forget to wear waterproof boots to keep your feet dry!")
else:
    footwear = "sneakers"
    print("Since there are no puddles, you can wear sneakers today.")
    print("You can wear comfortable sneakers today.")

#This message always print, no matter what the weather is like
print("")
print("Weather check compleded")

#Print the final outfit summary
print("=====WEATHER OUTFIT PICKER=====")
print("Temperature:",temperature)
print("Outfit Check:",outfit)
print("Raining:",is_raining)
print("Windbreaker Needed:",need_windbreaker)
print("Shoes Chosen:", footwear)
print("=======================================================")
