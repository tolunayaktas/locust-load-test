from locust import task, SequentialTaskSet
from data.payloads import Payloads  # Dizin içi import

class UserTasks(SequentialTaskSet):

    @task
    def post_user_create(self):
        payload = Payloads.user_create()
        response = self.client.post("/v2/user", json=payload)
        assert response.status_code == 200, f"Failed to create user: {response.text}"

    @task
    def get_user_info(self):
        response = self.client.get("/v2/user/tolunay12345")
        assert response.status_code == 200, f"Failed to get user info: {response.text}"

    @task
    def get_user_login(self):
        payload = Payloads.user_login()
        response = self.client.get("/v2/user/login", params=payload)
        assert response.status_code == 200, f"Failed to login: {response.text}"

    @task
    def put_user_update(self):
        payload = Payloads.user_update()
        response = self.client.put("/v2/user/tolunay12345", json=payload)
        assert response.status_code == 200, f"Failed to update user: {response.text}"

    @task
    def get_user_logout(self):
        response = self.client.get("/v2/user/logout")
        assert response.status_code == 200, f"Failed to logout: {response.text}"

    @task
    def create_user_with_array(self):
        payload = Payloads.user_array()
        response = self.client.post("/v2/user/createWithArray", json=payload)
        assert response.status_code == 200, f"Failed to create user with array: {response.text}"

    @task
    def delete_user(self):
        payload = Payloads.user_delete()
        self.client.post("/v2/user", json=payload)
        response = self.client.delete("/v2/user/tolunay1234del")
        assert response.status_code == 200, f"Failed to delete user: {response.text}"
