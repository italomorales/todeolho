from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from .registry import get_registered_tasks
from .logging import get_logger


class Scheduler:
    def __init__(self) -> None:
        self.logger = get_logger()
        self.scheduler = BackgroundScheduler()

    def start(self) -> None:
        for task in get_registered_tasks():
            # default: run every minute
            self.scheduler.add_job(task, CronTrigger.from_crontab('* * * * *'))
        self.scheduler.start()
        self.logger.info("Scheduler started", extra={"jobs": len(get_registered_tasks())})

    def shutdown(self) -> None:
        self.scheduler.shutdown()
        self.logger.info("Scheduler stopped")
