from apscheduler.schedulers.blocking import BlockingScheduler
from main import main

scheduler = BlockingScheduler()

# Run every day at 10 AM
scheduler.add_job(main, 'cron', hour=10, minute=0)

print("Scheduler started. Press Ctrl+C to exit.")
scheduler.start()
