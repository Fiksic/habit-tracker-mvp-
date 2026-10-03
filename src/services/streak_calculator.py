
from collections import defaultdict
from datetime import timedelta

class StreakCalculator:
    @staticmethod
    def calculate_streaks(entries: List[CheckInEntry], target_date: str) -> Dict[str, int]:
        # Сортируем по дате
        sorted_entries = sorted(entries, key=lambda e: e.date)
        dates_with_status = {e.date: e.status for e in sorted_entries}

        current_streak = 0
        best_streak = 0

        # Идём назад от target_date
        current_date = datetime.strptime(target_date, "%Y-%m-%d")
        while True:
            date_str = current_date.strftime("%Y-%m-%d")
            status = dates_with_status.get(date_str)
            if status == "completed":
                current_streak += 1
                best_streak = max(best_streak, current_streak)
            else:
                break
            current_date -= timedelta(days=1)

        return {
            "current_streak": current_streak,
            "best_streak": best_streak
        }

    @staticmethod
    def calculate_monthly_success_rate(entries: List[CheckInEntry], year: int, month: int) -> float:
        # Считаем количество дней в месяце
        if month == 12:
            next_month = datetime(year + 1, 1, 1)
        else:
            next_month = datetime(year, month + 1, 1)
        first_day = datetime(year, month, 1)
        total_days = (next_month - first_day).days

        completed_days = 0
        for e in entries:
            entry_date = datetime.strptime(e.date, "%Y-%m-%d")
            if entry_date.year == year and entry_date.month == month and e.status == "completed":
                completed_days += 1

        if total_days == 0:
            return 0.0
        return round((completed_days / total_days) * 100, 2)
