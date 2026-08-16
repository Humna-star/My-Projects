def total_calc(bill_amount, tip_perc):
#define a function that calculates the tip on bill
   total = bill_amount*(1 + 0.01*tip_perc)
   total = round(total, 2)
   print(f"Please pay ${total}")

#specify only bill amount
#default value of tip percentage is used

total_calc(68579219987654567876745342344656798978564532, 2880)