import uuid
from datetime import datetime
from typing import List, Optional, Dict, Any

class HabitService:
    def __init__(self):
        self.habits: List[Habit] = 

    def create_habit(self, name: str, description: str = "", periodicity: str = "daily", desired_time: Optional[str] = None) -> Habit:
        habit = Habit(name, description, periodicity, desired_time)
        self.habits.append(habit)
        return habit

    def get_all_habits(self, include_archived: bool = False) -> List[Habit]:
        if include_archived:
            return self.habits
        return [h for h in self.habits if not h.is_archived]

    def get_habit_by_id(self, habit_id: str) -> Optional[Habit]:
        for habit in self.habits:
            if habit.id == habit_id:
                return habit
        return None

    def archive_habit(self, habit_id: str) -> bool:
        habit = self.get_habit_by_id(habit_id)
        if habit:
            habit.is_archived = True
            return True
        return False

    def delete_habit(self, habit_id: str) -> bool:
        habit = self.get_habit_by_id(habit_id)
        if habit:
            self.habits.remove(habit)
            return True
        return False
