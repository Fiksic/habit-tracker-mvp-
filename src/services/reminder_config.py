
import json
import os

class ReminderConfig:
    def __init__(self):
        self.reminders: Dict[str, Dict[str, Any]] = {}  # habit_id -> config

    def set_reminder(self, habit_id: str, enabled: bool, time: Optional[str] = None):
        self.reminders[habit_id] = {
            "enabled": enabled,
            "time": time
        }

    def get_active_reminders_for_today(self, current_time: str) -> List[Dict[str, str]]:
        # В MVP просто возвращаем все активные напоминания; в реальном приложении можно фильтровать по времени
        active = 
        for habit_id, config in self.reminders.items():
            if config["enabled"]:
                active.append({
                    "habit_id": habit_id,
                    "time": config["time"] or "любое время"
                })
        return active
