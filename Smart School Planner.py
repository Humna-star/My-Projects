#Smart School Gay Planner

print("=====Smart School Day Planner=====")
print("Answer 3 quick questions and I will plan your day!\n")

day=input("What day is it (Monday to Sunday):").strip().capitalize()
weather=input("What is the weather? (Sunny / Rainny/ Cloudy):").strip().lower()
homework=input("Is there any homework? (Yes or No):").strip().lower()

print()
print(f"===Your Plan for {day}===")
print("-" * 35 )

#Topic:1 --if-elis-else:classify the day
if day in ("Saturday","Sunday"):
  print("Day time: WEEKEND - Enjoy your Weekend")
elif day =="Monday":
  print("Day Type: First Day of Week Pack your planner")
elif day =="Friday":
  print("Day Type: Last School Day Confirm all Tests")
elif day ==("Tuesday", "Wednesday", "Thursday"):
  print("Day Type: Regular School day Stay focused!")
else:
  print("Day Type:Do not Recognise. Please check the Spellings")

#Topic:2-- And Operator:Sunny AND Homework done
if weather== "sunny" and homework =="yes":
  print("AFTER SCHOOL: Head to the park - great weather and homework is done")

#Topic:3--Or Operator: Rainy OR Cloudy
if weather== "rainy" or weather =="cloudy":
  print("WEATHER TIP: Pack your Umbrella - it may get wet outside")

#Topic:3 NOT Operator: Homework NOT done
if not(homework=="yes"):
  print("HOMEWORK: Not done yet . Finish it before going out!")

#Topic:5--Combining AND + OR + NOT
if weather == "rainy" and not (homework == "yes"):
    print("Best plan   : Stay in, finish homework, then watch your favourite show.")
elif weather == "sunny" and homework == "yes" and not (day in ("Saturday", "Sunday")):
    print("Best plan   : All set for a great school day - you are prepared!")
elif day in ("Saturday", "Sunday") and weather == "sunny":
    print("Best plan   : Perfect weekend weather - head outside and have fun!")
else:
    print("Best plan   : Take it one step at a time - you have got this!")

print()
print("Plan complete! Have a wonderful day!")
