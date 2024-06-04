from locust import HttpUser, task, between
from bs4 import BeautifulSoup

class UserBehavior(HttpUser):
    wait_time = between(5, 15)
    # host = "http://django-loadbalancer-871454742.ap-south-1.elb.amazonaws.com"

    def on_start(self):
        # Retrieve CSRF token from the login page
        response = self.client.get("/login/")
        soup = BeautifulSoup(response.content, "html.parser")
        csrf_token = soup.find("input", {"name": "csrfmiddlewaretoken"})["value"]
        self.csrf_token = csrf_token

    @task
    def login(self):
        # Send POST request with CSRF token in headers
        headers = {"X-CSRFToken": self.csrf_token}
        response = self.client.post("/login/", {
            "email": "vishaldasani1999@gmail.com",
            "password": "1234"
        }, headers=headers)
        
        if response.status_code == 200:
            print("Login successful!")
        else:
            print("Login failed:", response.text)
