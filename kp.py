import os
import requests

def unlock_repository(repo_name):
    # Get GitHub token from environment variable
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print("GitHub token not found. Please set the GITHUB_TOKEN environment variable.")
        return

    # Construct the API endpoint URL
    api_url = f"https://api.github.com/repos/{repo_name}/branches/main/protection"

    # Prepare headers
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    # Send DELETE request to remove branch protection
    response = requests.delete(api_url, headers=headers)

    if response.status_code == 204:
        print("Repository unlocked successfully.")
    else:
        print(f"Failed to unlock repository. Status code: {response.status_code}")
        print(response.text)

# Example usage:
repo_name = "owner/repo"  # Replace with your repository name
unlock_repository(repo_name)
