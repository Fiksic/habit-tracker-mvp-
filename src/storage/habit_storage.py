
import json
import os

class HabitStorage:
    def __init__(self, filepath: str = "habits_data.json"):
        self.filepath = filepath
        self.habits: List[Habit] = 
        self.log: HabitLog = HabitLog()
        self.reminders: ReminderConfig = ReminderConfig()

    def save(self):
        data = {
            "habits": [h.to_dict() for h in self.habits],
            "check_ins": [e.to_dict() for e in self.log.entries],
            "reminders": {k: v for k, v in self.reminders.reminders.items()}
        }
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(self):
        if not os.path.exists(self.filepath):
            return
        with open(self.filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.habits = [Habit.from_dict(h) for h in data.get("habits", )]
        self.log.entries = [CheckInEntry.from_dict(e) for e in data.get("check_ins", )]
        self.reminders.reminders = data.get("reminders", {})

    def sync_with_services(self, habit_service: HabitService, habit_log: HabitLog, reminder_config: ReminderConfig):
        self.habits = habit_service.habits
        self.log.entries = habit_log.entries
        self.reminders.reminders = reminder_config.reminders
