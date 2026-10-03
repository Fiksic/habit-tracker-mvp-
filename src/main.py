
def main():
    # Инициализация
    habit_service = HabitService()
    habit_log = HabitLog()
    reminder_config = ReminderConfig()
    storage = HabitStorage()

    # Загрузка данных
    storage.load()
    if not storage.habits:
        # Создадим тестовую привычку, если данных нет
        habit = habit_service.create_habit(
            name="Читать 20 минут",
            description="Ежедневное чтение для развития",
            periodicity="daily",
            desired_time="08:00"
        )
        reminder_config.set_reminder(habit.id, enabled=True, time="07:45")

    # Пример отметки выполнения
    today = datetime.now().strftime("%Y-%m-%d")
    habit = habit_service.get_all_habits()
    habit_log.add_check_in(habit.id, today, "completed", note="Прочитал главу про алгоритмы")

    # Пример расчёта метрик
    entries = habit_log.get_entries_for_habit(habit.id)
    streaks = StreakCalculator.calculate_streaks(entries, today)
    rate = StreakCalculator.calculate_monthly_success_rate(entries, datetime.now().year, datetime.now().month)

    print(f"Привычка: {habit.name}")
    print(f"Текущий стрик: {streaks['current_streak']} дней")
    print(f"Лучший стрик: {streaks['best_streak']} дней")
    print(f"Успешность за месяц: {rate}%")

    # Активные напоминания на сегодня
    active_reminders = reminder_config.get_active_reminders_for_today("08:00")
    print(f"Напоминания на сегодня: {active_reminders}")

    # Синхронизация и сохранение
    storage.sync_with_services(habit_service, habit_log, reminder_config)
    storage.save()
    print("Данные сохранены в habits_data.json")

if __name__ == "__main__":
    main()
