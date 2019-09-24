from typing import Dict, List

import_classes = [
    "user",
    "device",
    "link",
    "pool",
    "service",
    "workflow",
    "workflow_edge",
    "task",
]

dont_track_changes = [
    "configurations",
    "current_configuration",
    "current_device",
    "current_job",
    "last_modified",
    "positions",
    "state",
]

dont_migrate[str, List[str]] = {
    "device": [
        "id",
        "configurations",
        "current_configuration",
        "jobs",
        "source",
        "destination",
        "pools",
    ],
    "link": ["id", "pools"],
    "pool": ["id", "jobs", "object_number"],
    "service": [
        "id",
        "sources",
        "destinations",
        "tasks",
        "workflows",
        "tasks",
        "start_workflows",
    ],
    "task": [
        "id",
        "job_name",
        "next_run_time",
        "is_active",
        "time_before_next_run",
        "status",
    ],
    "user": ["id", "pools"],
    "workflow": ["edges", "id", "sources", "destinations", "workflows", "tasks"],
    "workflow_edge": ["id", "source_id", "destination_id", "workflow_id"],
}
