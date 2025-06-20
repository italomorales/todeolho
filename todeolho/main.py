from .scheduler import Scheduler


def main() -> None:
    sched = Scheduler()
    sched.start()

    try:
        import time
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        sched.shutdown()


if __name__ == "__main__":
    main()
