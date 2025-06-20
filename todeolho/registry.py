from typing import Callable, Dict, List

TaskFunc = Callable[[], None]
TASK_REGISTRY: Dict[str, TaskFunc] = {}


def register_task(name: str) -> Callable[[TaskFunc], TaskFunc]:
    """Decorator to register a task function by name."""

    def decorator(func: TaskFunc) -> TaskFunc:
        TASK_REGISTRY[name] = func
        return func

    return decorator


def get_registered_tasks() -> List[TaskFunc]:
    return list(TASK_REGISTRY.values())
