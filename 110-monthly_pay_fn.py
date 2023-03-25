def calculate_pay(hours_worked, pay_per_hour):
  if hours_worked > 40:
    overtime_hours = hours_worked - 40
    regular_pay = 40 * pay_per_hour
    overtime_pay = overtime_hours * pay_per_hour * 2
    return regular_pay + overtime_pay 
  else:
    return hours_worked * pay_per_hour

def calculate_monthly_pay(wk1_hours, wk2_hours, wk3_hours, wk4_hours, pay_per_hour):
  week1_pay = calculate_pay(wk1_hours, pay_per_hour)
  week2_pay = calculate_pay(wk2_hours, pay_per_hour)
  week3_pay = calculate_pay(wk3_hours, pay_per_hour)
  week4_pay = calculate_pay(wk4_hours, pay_per_hour)
  #return week1_pay, week2_pay, week3_pay, week4_pay
  return week1_pay + week2_pay + week3_pay + week4_pay
  
print(calculate_monthly_pay(40, 50, 35, 40, 50))
    
# worked X hours at Y pay per hour
#print(calculate_pay(42.53, 10))    
# Worked 40 hours at $20 an hour
#print(calculate_pay(40, 20))
# Worked 50 hours at $20 an hour
#print(calculate_pay(50, 20))
# Worked 40 hours at $12 an hour
#print(calculate_pay(40, 12))
