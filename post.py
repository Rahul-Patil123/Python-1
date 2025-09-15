class Post:
    def __init__(self, message, author):
        self.message = message
        self.author = author
    def get_post(self):
        print(f"Message : {self.message}\n                             - by {self.author}")
        