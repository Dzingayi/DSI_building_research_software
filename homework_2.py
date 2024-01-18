#Written in VS Code with the assistance of ChatGPT

import requests
import json
import matplotlib.pyplot as plt
from pprint import pprint

#Function to retrieve data from GitHub API
def get_github_data(token):
    # Set the GitHub API endpoint for repository search
    url = 'https://api.github.com/search/repositories?q=followers:>1&sort=followers&per_page=20'
    headers = {'Authorization': 'Bearer ' + token}

    try:
        # Send request to GitHub
        response = requests.get(url, headers=headers)
        response.raise_for_status()  #Check for HTTP errors
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error in API request: {e}")
        return None

#Function to plot GitHub repositories data
def plot_github_repos(repos):
    if 'items' in repos:
        #Extract repository information
        repos = repos['items']
        repos.sort(key=lambda x: x['stargazers_count'])
        repo_names = [repo['name'] for repo in repos]
        followers_count = [repo['stargazers_count'] for repo in repos]

        #Determine the repository with the most followers
        max_followers_repo = max(repos, key=lambda x: x['stargazers_count'])

        #Color the bars grey for all repositories and bright blue for the repository with most followers
        colors = ['grey' if repo != max_followers_repo else 'blue' for repo in repos]

        #Plot the data as an h-bar 
        bars = plt.barh(repo_names, followers_count, color=colors)
        plt.xlabel('Number of Followers')
        plt.ylabel('Repository Name')
        plt.title('Top 20 GitHub Repositories With Most Followers')
        plt.tight_layout()

        #Find the bar corresponding to the repository with most followers
        max_followers_bar_index = repo_names.index(max_followers_repo['name'])
        max_followers_bar = bars[max_followers_bar_index]

        #Set the color and weight of the bar and its associated text label
        max_followers_bar.set_color('blue')
        plt.gca().get_yticklabels()[max_followers_bar_index].set_color('blue')
        plt.gca().get_yticklabels()[max_followers_bar_index].set_weight('bold')

        #Show the plot
        plt.show()
    else:
        print("Unexpected response format. Check the structure of the response.")


if __name__ == "__main__": #Ensure the code below only runs if this script is the main program.
    #GitHub token
    token = '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'

    #Extract GitHub data
    github_data = get_github_data(token)

    #Plot the data
    if github_data:
        plot_github_repos(github_data)
