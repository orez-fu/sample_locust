from locust import SequentialTaskSet, HttpUser, task


class UserBehaviour(SequentialTaskSet):
  @task
  def create_project_api(self):
    with self.client.post("/", name="Access Website", catch_response=True) as response:
      if response.status_code == 200:
        response.success()
      else:
        response.failure(response.status_code)


class WebsiteUser(HttpUser):
  tasks = [UserBehaviour]
  host = "https://dantri.com.vn"
