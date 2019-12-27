from locust import HttpLocust, TaskSet, task, events, between
import json
import time

class UserBehaviour(TaskSet):

  def setup(self):
    print("*** setup block ***\nRuns before starting taskset only once")
    global headers
    headers = {'content-type': 'application/json',
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
        'Accept': "text/html,application/json,text/javascript,application/vnd.api+json,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "en-GB,en-US;q=0.9,en;q=0.8"}

  @task(1)
  def SearchUser(self):
    response = self.client.get("/api/v1/employees",name='List Employees',headers=headers)

  @task(2)
  def AllUsersList(self):
    response = self.client.get("/api/v1/employee/1",name='Individual Employee Detail',headers=headers)

  @task(4)
  def SecondEmployeeDetail(self):
    with self.client.get("/api/v1/employee/2",name='Another Employee Detail',headers=headers, catch_response=True) as response:
        if response.status_code == 200:
            response.success()
        else:
            response.failure("Wrong response")


class MyLocust(HttpLocust):
  task_set = UserBehaviour
  wait_time = between(5, 15)
  host = "http://dummy.restapiexample.com"
