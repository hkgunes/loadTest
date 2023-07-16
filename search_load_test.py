from locust import HttpUser, TaskSet, task, constant
from readtestData import CsvRead

class SearchBehavior(TaskSet):
    def on_start(self):
        pass

    @task
    def perform_search(self):
     search_term = "Xiomi+Redmi"  # Update with desired search term
     self.client.get(f"/arama?q={search_term}")



class MySeqTest(HttpUser):
    wait_time = constant(1)
    host = "https://www.n11.com"
    tasks = [SearchBehavior]
