class User:
    def __init__(self,email,name,password,current_job_title):
        self.email = email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title
    def change_password(self,new_password):
        self.password = new_password
        
    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title
    
    def get_user_details(self):
        print(f"User name is {self.name}\nUser Email is {self.email}\nCurrent Job title is {self.current_job_title}")
        
rahul = User("rahulpatilccis@gmail.com","Rahul Ganeshwar Patil", "changeme", "SRE")
rahul.get_user_details()