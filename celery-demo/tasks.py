from celery import Celery
import time

app = Celery(
    "demo",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@app.task
def send_email(name):
    print("Sending email...")
    time.sleep(5)
    print(f"Welcome {name}")
    return "Done"


@app.task
def generate_report(report_id):
    print(f"Generating report {report_id}...")
    time.sleep(10)
    print(f"Report {report_id} generated")
    return f"Report {report_id} ready"