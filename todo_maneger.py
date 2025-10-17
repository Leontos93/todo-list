import json
import datetime
import os


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        try:
            if os.path.exists(self.filename):
                with open(self.filename, "r", encoding="utf-8") as file:
                    self.tasks = json.load(file)
                    print(f"✅ Завантажено {len(self.tasks)} задач")
            else:
                self.tasks = []
                print("📝 Створено новий список задач")
        except (json.JSONDecodeError, FileNotFoundError) as e:
            self.tasks = []
            print(f"⚠️ Помилка читання файлу: {e}")

    def save_tasks(self):
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(self.tasks, file, indent=4, ensure_ascii=False)
            print(f"💾 Збережено {len(self.tasks)} задач")
        except Exception as e:
            print(f"⚠️ Помилка збереження: {e}")
