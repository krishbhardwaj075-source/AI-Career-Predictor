import requests

def git_analyze(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        return []

    repos = response.json()
    skills = []

    for repo in repos:
        language = repo.get("language")
        if language and language not in skills:
            skills.append(language)

    return skills
