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

    def show_tasks(self):
        if not self.tasks:
            print("📝 Список задач порожній")
            return

        print("\n" + "=" * 60)
        print("📋 СПИСОК ЗАДАЧ")
        print("=" * 60)

        for task in self.tasks:
            status = "✅" if task["completed"] else "⬜"
            print(f"{status} [{task['id']:3}] {task['text']}")
            print(f"        Створено: {task['created_at']}")
            print("-" * 60)

        completed = sum(1 for task in self.tasks if task["completed"])
        print(
            f"\n📊 Всього: {len(self.tasks)} | Виконано: {completed} | Залишилось: {len(self.tasks) - completed}"
        )

    def complete_task(self):
        try:
            task_id = int(input("Введіть ID задачі для виконання: "))
        except ValueError:
            print("⚠️ ID має бути числом")
            return
        for task in self.tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print("ℹ️ Ця задача вже виконана")
                else:
                    task["completed"] = True
                    self.save_tasks()
                    print(f"✅ Задача #{task_id} відмічена як виконана")
                return
        print(f"❌ Задача з ID {task_id} не знайдена")

    def delete_task(self):
        try:
            task_id = int(input("Введіть ID задачі для видалення: "))
        except ValueError:
            print("⚠️ ID має бути числом")
            return
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print(f"🗑️ Задача #{task_id} видалена")
                return
        print(f"❌ Задача з ID {task_id} не знайдена")
