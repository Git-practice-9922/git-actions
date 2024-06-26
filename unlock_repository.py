name: Unlock Repository

on:
  workflow_dispatch:
    inputs:
      repository:
        description: 'Repository name with owner (e.g., owner/repo)'
        required: true

jobs:
  unlock-repo:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v2
      
    - name: Unlock repository
      env:
        GITHUB_TOKEN: ${{ secrets.WORK_GITHUB_TOKEN }}
        REPO_NAME: ${{ github.event.inputs.repository }}
      run: |
        # Construct the API endpoint URL
        API_URL="https://api.github.com/repos/$REPO_NAME/branches/main/protection"
        
        # Send DELETE request to remove branch protection using curl
        curl -X DELETE -H "Authorization: token $GITHUB_TOKEN" "$API_URL"
