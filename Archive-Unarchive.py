import os
import requests

os.environ["GITHUB_TOKEN"] = "${{ secrets.WORK_GITHUB_TOKEN  }}"
# Function to archive a repository
def archive_repo(repo_name):
    response = requests.patch(
        f"https://api.github.com/repos/Git-practice-9922/{repo_name}",
        headers={"Authorization": f"Bearer {os.environ.get['GITHUB_TOKEN']}"},
        json={"archived": True}
    )
    return response

# Function to unarchive a repository
def unarchive_repo(repo_name):
    response = requests.patch(
        f"https://api.github.com/repos/Git-practice-9922/{repo_name}",
        headers={"Authorization": f"Bearer {os.environ.get['GITHUB_TOKEN']}"},
        json={"archived": False}
    )
    return response
# Read repository names from input.txt file
with open("input.txt", "r") as file:
    repo_names = [line.strip() for line in file]
    print(repo_names)

# Prompt the user for an action
#action = input(f'Want to archive or unarchive the repositories? Type "archive" or "unarchive": ')
action = os.getenv('ACTION')

    # Perform action based on user input
if action == "archive":
    # Loop through each repository
    for repo_name in repo_names:     
        response = archive_repo(repo_name)
        print(f"Response code for archiving {repo_name}: {response.status_code}")
elif action == "unarchive":
    for repo_name in repo_names:    
        response = unarchive_repo(repo_name)
        print(f"Response code for unarchiving {repo_name}: {response.status_code}")
else:
    print("Invalid action. Please provide 'archive' or 'unarchive'.")