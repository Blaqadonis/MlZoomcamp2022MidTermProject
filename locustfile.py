import numpy as np
from locust import task
from locust import between
from locust import HttpUser


sample = {
  "location": "albury",
 "mintemp": 13.4,
 "maxtemp": 22.9,
 "rainfall": 0.6,
 "evaporation": 5.469824216349109,
 "sunshine": 7.624853113193594,
 "windgustdir": "w",
 "windgustspeed": 44.0,
 "winddir9am": "w",
 "winddir3pm": "wnw",
 "windspeed9am": 20.0,
 "windspeed3pm": 24.0,
 "humidity9am": 71.0,
 "humidity3pm": 22.0,
 "pressure9am": 1007.7,
 "pressure3pm": 1007.1,
 "cloud9am": 8.0,
 "cloud3pm": 4.503166899728551,
 "temp9am": 16.9,
 "temp3pm": 21.8,
 "raintoday": "no",
 "month": 12,
 "day": 1}



class RainTomorrowTestUser(HttpUser):
    """
    Usage:
        Start locust load testing client with:

            locust -H http://localhost:3000

        Open browser at http://0.0.0.0:8089, adjust desired number of users and spawn rate for the load test from the Web UI and start swarming.
    """

    @task
    def classify(self):
        self.client.post("/classify", json=sample)

    wait_time = between(0.01, 2)
