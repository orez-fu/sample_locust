from locust import HttpUser, task, between
import json

class RandomUserApiUser(HttpUser):
    wait_time = between(1, 5)

    @task(1)
    def get_random_female_name(self):
        with self.client.get("/api/?gender=female", catch_response=True) as response:
            if response.status_code == 200:
                data = response.json()
                if 'results' in data:
                    female_name = data['results'][0]['name']
                    print(f"Random Female Name: {female_name['title']} {female_name['first']} {female_name['last']}")
                    response.success()
                else:
                    response.failure("No results key in response")
            else:
                response.failure(f"Unexpected status code: {response.status_code}")

    @task(1)
    def get_random_password(self):
        with self.client.get("/api/?password=upper,lower,1-16", catch_response=True) as response:
            if response.status_code == 200:
                data = response.json()
                if 'results' in data:
                    password = data['results'][0]['login']['password']
                    print(f"Random Password: {password}")
                    response.success()
                else:
                    response.failure("No results key in response")
            else:
                response.failure(f"Unexpected status code: {response.status_code}")

    def on_start(self):
        self.client.base_url = "https://randomuser.me"

