import requests

def list_github_user_repos(username):
    api_url = f"https://api.github.com/users/{username}/repos"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status() 
        
        repositories = response.json()
        
        if repositories:
            print(f"Repositories for {username}:")
            for repo in repositories:
                print(f"- {repo['name']} (URL: {repo['html_url']})")
        else:
            print(f"No public repositories found for {username}.")
github_username = "Rahul-Patil123"  
list_github_user_repos(github_username)