from locust import HttpUser, between
from tasks.user_tasks import UserTasks

class WebsiteUser(HttpUser):
    wait_time = between(5, 15)
    tasks = [UserTasks]
