from locust import HttpLocust, TaskSet, task, events, between
import json
import time

class UserBehaviour(TaskSet):

  def on_start(self):
    print("*** on_start block ***\nRuns before task set is started")

  def on_stop(self):
    print("*** on_stop block ***\nRuns after task set is stopped")

  def setup(self):
    print("*** setup block ***\nRuns before starting taskset only once")
    global headers
    headers = {'content-type': 'application/json',
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36",
        'Accept': "text/html,application/json,text/javascript,application/vnd.api+json,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        'Accept-Encoding': "gzip, deflate, br",
        'Accept-Language': "en-GB,en-US;q=0.9,en;q=0.8"}

  def teardown(self):
    print("*** teardown block ***\nRuns only once after all taskset is done")

  # @seq_task(1)
  @task(1)
  def SearchUser(self):
    response = self.client.get("/api/v1/employees",name='List Employees',headers=headers)
    # print("Response status code:", response.status_code)
    # print("Response content:", response.text)

  # @seq_task(2)
  @task(2)
  def AllUsersList(self):
    response = self.client.get("/api/v1/employee/1",name='Individual Employee Detail',headers=headers)
    # print("Response status code:", response.status_code)
    # print("Response content:", response.text)

  # @seq_task(3)
  @task(4)
  def SecondEmployeeDetail(self):
    with self.client.get("/api/v1/employee/2",name='Another Employee Detail',headers=headers, catch_response=True) as response:
        if response.status_code == 200:
            response.success()
        else:
            response.failure("Wrong response")
    # print("Response content code:", response.content)
    # print("Response status code:", response.status_code)
    # print("Response content:", response.text)

  # @seq_task(4)
  @task(1)
  def PostExample(self):
    response = self.client.post("api/v1/create", {"name":"Helloo","salary":"123","age":"23"}, name='Create Employee',headers=headers)
    # print("Response status code:", response.status_code)
    # print("Response content:", response.text)



class MyLocust(HttpLocust):
  task_set = UserBehaviour
  wait_time = between(5, 15)
  host = "http://dummy.restapiexample.com"
