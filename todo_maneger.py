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
                    print(f"✅ Loaded {len(self.tasks)} tasks")
            else:
                self.tasks = []
                print("📝 Created new task list")
        except (json.JSONDecodeError, FileNotFoundError) as e:
            self.tasks = []
            print(f"⚠️ File reading error: {e}")

    def save_tasks(self):
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(self.tasks, file, indent=4, ensure_ascii=False)
            print(f"💾 Saved {len(self.tasks)} tasks")
        except Exception as e:
            print(f"⚠️ Saving error: {e}")

    def add_task(self):
        if self.tasks:
            id = max(task["id"] for task in self.tasks) + 1
        else:
            id = 1
        text = input("Enter task text: ")
        if not text:
            print("⚠️ Task name cannot be empty")
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
        print("✅ Task added")

    def show_tasks(self):
        if not self.tasks:
            print("📝 Task list is empty")
            return

        print("\n" + "=" * 60)
        print("📋 TASK LIST")
        print("=" * 60)

        for task in self.tasks:
            status = "✅" if task["completed"] else "⬜"
            print(f"{status} [{task['id']:3}] {task['text']}")
            print(f"        Created: {task['created_at']}")
            print("-" * 60)

        completed = sum(1 for task in self.tasks if task["completed"])
        print(
            f"\n📊 Total: {len(self.tasks)} | Completed: {completed} | Remaining: {len(self.tasks) - completed}"
        )

    def complete_task(self):
        try:
            task_id = int(input("Enter task ID to complete: "))
        except ValueError:
            print("⚠️ ID must be a number")
            return
        for task in self.tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print("ℹ️ This task is already completed")
                else:
                    task["completed"] = True
                    self.save_tasks()
                    print(f"✅ Task #{task_id} marked as completed")
                return
        print(f"❌ Task with ID {task_id} not found")

    def delete_task(self):
        try:
            task_id = int(input("Enter task ID to delete: "))
        except ValueError:
            print("⚠️ ID must be a number")
            return
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                self.save_tasks()
                print(f"🗑️ Task #{task_id} deleted")
                return
        print(f"❌ Task with ID {task_id} not found")


def main():
    manager = TaskManager()

    while True:
        print("\n" + "=" * 40)
        print("📋 TASK MANAGER")
        print("=" * 40)
        print("1. 📄 Show all tasks")
        print("2. ➕ Add new task")
        print("3. ✅ Mark task as completed")
        print("4. 🗑️  Delete task")
        print("0. 🚪 Exit")
        print("-" * 40)

        choice = input("Choose option: ")

        if choice == "1":
            manager.show_tasks()
        elif choice == "2":
            manager.add_task()
        elif choice == "3":
            manager.complete_task()
        elif choice == "4":
            manager.delete_task()
        elif choice == "0":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
