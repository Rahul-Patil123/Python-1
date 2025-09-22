import requests
api_url = requests.get("http://github.com/Rahul-Patil123?tab=repositories")
print(api_url.status_code)