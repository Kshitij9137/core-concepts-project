"""Mini project 2: To-Do list - lists, dictionaries, loops, and a simple class."""


class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, title: str) -> dict:
        if not title.strip():
            raise ValueError("Task title cannot be empty")
        task = {"id": len(self.tasks) + 1, "title": title.strip(), "done": False}
        self.tasks.append(task)
        return task

    def complete(self, task_id: int) -> None:
        for task in self.tasks:
            if task["id"] == task_id:
                task["done"] = True
                return
        raise KeyError(f"No task with id {task_id}")

    def pending(self) -> list:
        return [t for t in self.tasks if not t["done"]]


if __name__ == "__main__":
    todo = TodoList()
    todo.add("Learn Git")
    todo.add("Finish Phase 2 report")
    todo.complete(1)
    for t in todo.tasks:
        print(("[x] " if t["done"] else "[ ] ") + t["title"])
