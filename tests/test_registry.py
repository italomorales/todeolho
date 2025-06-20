from todeolho.registry import TASK_REGISTRY
import todeolho  # noqa: F401


def test_tasks_registered():
    assert "http_monitor" in TASK_REGISTRY
    assert "db_monitor" in TASK_REGISTRY
    assert "api_db_compare" in TASK_REGISTRY
