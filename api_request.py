import requests

def list_github_user_repos(username):
    """
    Lists all public repositories for a given GitHub username.
    """
    api_url = f"https://api.github.com/users/{username}/repos"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        
        repositories = response.json()
        
        if repositories:
            print(f"Repositories for {username}:")
            for repo in repositories:
                print(f"- {repo['name']} (URL: {repo['html_url']})")
        else:
            print(f"No public repositories found for {username}.")
            
    except requests.exceptions.RequestException as e:
        print(f"Error fetching repositories: {e}")

# Example usage:
github_username = "Rahul-Patil123"  # Replace with the desired GitHub username
list_github_user_repos(github_username)