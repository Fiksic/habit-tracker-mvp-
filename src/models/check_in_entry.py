class CheckInEntry:
    def __init__(self, habit_id: str, date: str, status: str, note: str = ""):
        # status: "completed" или "missed"
        self.habit_id = habit_id
        self.date = date  # формат YYYY-MM-DD
        self.status = status
        self.note = note
        self.recorded_at = datetime.now().isoformat()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "habit_id": self.habit_id,
            "date": self.date,
            "status": self.status,
            "note": self.note,
            "recorded_at": self.recorded_at
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "CheckInEntry":
        entry = cls(
            habit_id=data["habit_id"],
            date=data["date"],
            status=data["status"],
            note=data.get("note", "")
        )
        entry.recorded_at = data.get("recorded_at", datetime.now().isoformat())
        return entry


class HabitLog:
    def __init__(self):
        self.entries: List[CheckInEntry] = 

    def add_check_in(self, habit_id: str, date: str, status: str, note: str = "") -> CheckInEntry:
        entry = CheckInEntry(habit_id, date, status, note)
        self.entries.append(entry)
        return entry

    def get_entries_for_habit(self, habit_id: str) -> List[CheckInEntry]:
        return [e for e in self.entries if e.habit_id == habit_id]

    def get_entries_for_date(self, date: str) -> List[CheckInEntry]:
        return [e for e in self.entries if e.date == date]

