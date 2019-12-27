# Locust Plain Sample project
Plain project to run load testing on API's using locust in python


## Installation

Install python 3 and pip3 in your machine, all the steps are available in this [link](https://docs.locust.io/en/stable/installation.html)


## To Run

To run in a single mode,
```
locust -f locust_load.py
```
then go to `http://localhost:8089/` and then enter the number of users and the rampup time to get started


To run in a master slave mode, run as much slave as possible with,
```
locust -f locust_load.py --slave
```
and then run the master node by,
```
locust -f locust_load.py --master
```
After which go to `http://localhost:8089/` and then enter the number of users and the rampup time to get started

Other details are available at this [link](https://docs.locust.io/en/stable/quickstart.html)
