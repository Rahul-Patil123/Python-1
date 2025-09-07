import datetime

user_input = input("Enter your goal with a deadline seperated by colon:\n")
input_list = user_input.split(":")
goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline,"%d.%m.%Y")
today_date = datetime.datetime.today()
time_remaining = deadline_date - today_date
print(f"Time remaining till your deadline is : {time_remaining}")