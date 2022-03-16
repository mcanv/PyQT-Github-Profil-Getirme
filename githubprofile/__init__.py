import requests
import json

from pprint import pprint

class GithubProfile:
    def __init__(self, profile_name):
        self.name = None
        self.location = None
        self.repos = None
        self.followers = None
        self.url = None
        response = requests.get(f"https://api.github.com/users/{profile_name}")
        if response.status_code == 200:
            data = json.loads(response.text)
            pprint(data)
            self.name = data["name"]
            self.location = data["location"]
            self.repos = data["public_repos"]
            self.followers = data["followers"]
            self.url = data["html_url"]

        
