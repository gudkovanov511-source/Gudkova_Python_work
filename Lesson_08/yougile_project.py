import requests


class YougileProject:
    def __init__(self, url, token):
        self.url = url
        self.token = token

    def create(self, title, users):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        body = {
            "title": title,
            "users": users
        }
        resp = requests.post(f"{self.url}projects", json=body, headers=headers)
        return resp

    def get_project(self, p_id):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        resp = requests.get(f"{self.url}projects/{p_id}", headers=headers)
        return resp

    def update_project(self, p_id, new_title):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        body = {
            "title": new_title
        }
        resp = requests.put(f"{self.url}projects/{p_id}",
                            headers=headers, json=body)
        return resp

    def delete_project(self, p_id):
        headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }
        body = {
            "deleted": True
        }
        resp = requests.put(f"{self.url}projects/{p_id}",
                            headers=headers, json=body)
        return resp

    def get_projects(self):
        headers = {
            "Authorization": f"Bearer {self.token}"
        }
        resp = requests.get(f"{self.url}projects", headers=headers)
        return resp
