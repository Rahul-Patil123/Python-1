from user import User
from post import Post
rahul = User("rahulpatilccis@gmail.com","Rahul Ganeshwar Patil", "changeme", "SRE")
rahul.get_user_details()
rahul.change_job_title("DevOps Engineer")
rahul.get_user_details()
new_post = Post("I have successfully learned Classes and objects in python", rahul.name)
new_post.get_post()