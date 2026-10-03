
import uuid
from datetime import datetime
from typing import List, Optional, Dict, Any

class Habit:
    def __init__(self, name: str, description: str = "", periodicity: str = "daily", desired_time: Optional[str] = None):
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.periodicity = periodicity  # "daily" или список дней, например ["Mon", "Wed", "Fri"]
        self.desired_time = desired_time
        self.created_at = datetime.now().isoformat()
        self.is_archived = False

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "periodicity": self.periodicity,
            "desired_time": self.desired_time,
            "created_at": self.created_at,
            "is_archived": self.is_archived
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Habit":
        habit = cls(
            name=data["name"],
            description=data.get("description", ""),
            periodicity=data.get("periodicity", "daily"),
            desired_time=data.get("desired_time")
        )
        habit.id = data["id"]
        habit.created_at = data.get("created_at", datetime.now().isoformat())
        habit.is_archived = data.get("is_archived", False)
        return habit
