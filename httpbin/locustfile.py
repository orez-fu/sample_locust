from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task(1)
    def get_status_200(self):
        self.client.get("/status/200")

    @task(1)
    def get_status_404(self):
        self.client.get("/status/404")

    @task(1)
    def get_delayed_response(self):
        self.client.get("/delay/3")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
    host = "http://httpbin.org"
