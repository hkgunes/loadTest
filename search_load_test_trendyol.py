from locust import HttpUser, TaskSet, task, constant
from readtestData import CsvRead

class SearchBehavior(TaskSet):
    def on_start(self):
        pass

    @task
    def perform_search(self):
     search_term = "Xiomi"  # Update with desired search term
     res = self.client.get(f"/sr?q={search_term}&qt={search_term}&st={search_term}&os=1")
     print("get search mothod status is", res.status_code)

    @task
    def get_method(self):
        res = self.client.get("/")
        print("get mothod status is", res.status_code)


class MySeqTest(HttpUser):
    wait_time = constant(1)
    host = "https://www.trendyol.com"
    tasks = [SearchBehavior]
