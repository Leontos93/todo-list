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

    def add_task(self):
        if self.tasks:
            id = max(task["id"] for task in self.tasks) + 1
        else:
            id = 1
        text = input("Введіть текст задачі: ")
        if not text:
            print("⚠️ Назва задачі не може бути порожньою")
            return
        created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        task_info = {
            "id": id,
            "text": text,
            "completed": False,
            "created_at": created_at,
        }
        self.tasks.append(task_info)
        self.save_tasks()
        print("✅ Задача додана")
