from pprint import pprint
import requests
import json

class GithubProile:
    def __init__(self, profile_name) -> None:
        self.name = None
        self.location = None
        self.reposCount = None
        self.followerCount = None
        self.url = None
        response = requests.get(f"https://api.github.com/users/{profile_name}")
        if response.status_code == 200:
            data = json.loads(response.text)
            pprint(data)
            self.name = data["name"]
            self.location = data["location"]
            self.reposCount = data["public_repos"]
            self.followerCount = data["followers"]
            self.url = data["html_url"]