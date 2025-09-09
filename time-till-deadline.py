from  datetime import datetime
user_input = input("Enter your goal with a deadline seperated by colon:\n")
input_list = user_input.split(":")
goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline,"%d.%m.%Y")
today_date = datetime.today()
time_remaining = deadline_date - today_date
print(f"Days remaining till your deadline is : {time_remaining.days} days")