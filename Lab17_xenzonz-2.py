"""
Docstring for Lab17_xenzonz-2.py
i. Lab 17: Plot GitHub Repositories for a New Language
ii. Sam Cocquyt
iii.  Uses the GitHub API to find the most-starred JavaScript
    repositories on GitHub.

iv. python_repos_visual.py on Chapter 17 of the textbook
v. 5/15/2026
"""

import requests
import plotly.express as px

def main():
    
    # Make an API call and check the response.
    url = "https://api.github.com/search/repositories"
    url += "?q=language:javascript+sort:stars+stars:>10000"

    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    print(f"Status code: {r.status_code}")

    # Process overall results.
    response_dict = r.json()
    print(f"Complete results: {not response_dict['incomplete_results']}")

    # Process repository information.
    repo_dicts = response_dict['items']
    repo_names, stars = [], []
    for repo_dict in repo_dicts:
        repo_names.append(repo_dict['name'])
        stars.append(repo_dict['stargazers_count'])

    # Make visualization.
    fig = px.bar(
    x=repo_names,
    y=stars,
    color=stars,
    color_continuous_scale="Viridis",
    title="Most-Starred JavaScript Projects on GitHub",
    template="plotly_dark"
    )

    fig.show()

if __name__ == "__main__":
    main()