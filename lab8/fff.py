import sqlite3 # Чтобы сохранять задачи между запусками программы
import tkinter as tk # Создаёт окна, кнопки, списки
from tkinter import messagebox # Чтобы показывать всплывающие окна с ошибками и сообщениями

class TaskError(Exception): # Создаёт базовый класс для всех ошибок приложения
# Чтобы можно было ловить все ошибки одной конструкцией except TaskError
    pass


class TaskNotFoundError(TaskError): # ошибка "задача не найдена"
    pass

class EmptyTaskError(TaskError): # ошибка "пустая задача"
    pass

class Task:
    def __init__(self, id, title, completed):
        self.id = id # self указывает на сам объект
        self.title = title 
        self.completed = completed
    
    def __str__(self):
        if self.completed:
            status = "+"
        else:
            status = "-"
        return f"{status} {self.title}"

class Database: 
    def __init__(self): 
        self.conn = sqlite3.connect("todo.db") # создает подключение к файлу
        self.cursor = self.conn.cursor() # курсор создаем для обработки данных по одной строке за раз
        # Выполняет SQL-запрос на создание таблицы:
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks ( 
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER DEFAULT 0
            )
        ''')
        self.conn.commit() # сохраняет в файл
    
    def add_task(self, title): 
        self.cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        self.conn.commit()
        return self.cursor.lastrowid
    
    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()
    
    def complete_task(self, task_id):
        self.cursor.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
        self.conn.commit()
    
    def get_tasks(self): # запрашиваем все задачи, сортируем по ID
        self.cursor.execute("SELECT id, title, completed FROM tasks ORDER BY id")
        return [Task(id, title, bool(completed)) for id, title, completed in self.cursor.fetchall()]
    
    def close(self):
        self.conn.close()

class TodoApp: 
    def __init__(self):
        self.db = Database() # Создаём объект базы данных
        self.root = tk.Tk()
        self.root.title("✅ ToDo List")
        self.root.geometry("400x450")
        
        # Заголовок
        tk.Label(self.root, text="Мои задачи", font=("Arial", 16, "bold")).pack(pady=10)
        
        # Список задач
        self.listbox = tk.Listbox(self.root, height=12, font=("Arial", 11))
        self.listbox.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)
        
        # Поле ввода
        self.entry = tk.Entry(self.root, font=("Arial", 11))
        self.entry.pack(fill=tk.X, padx=20, pady=5)
        
        # Кнопки
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)
        
        tk.Button(btn_frame, text="➕ Добавить", command=self.add_task,
                 bg="lightgreen", width=12).pack(side=tk.LEFT, padx=5)
        
        tk.Button(btn_frame, text="✔️ Выполнить", command=self.complete_task,
                 bg="lightblue", width=12).pack(side=tk.LEFT, padx=5)
        
        tk.Button(btn_frame, text="🗑️ Удалить", command=self.delete_task,
                 bg="lightcoral", width=12).pack(side=tk.LEFT, padx=5)
        
        self.refresh_list() # Загружаем задачи из БД и показываем в списке
    
    def refresh_list(self): 
        self.listbox.delete(0, tk.END) # Очищаем список
        tasks = self.db.get_tasks()
        for task in tasks:
            self.listbox.insert(tk.END, str(task)) # Получаем задачи из БД и добавляем каждую в список
    
    def get_selected_task(self):
        selection = self.listbox.curselection() # curselection() возвращает кортеж с индексом выбранного элемента
        if not selection:
            raise TaskNotFoundError() # если нчиего не выбрано, то вызываем ошибку
        return self.db.get_tasks()[selection[0]] # Берём первую позицию выбора и получаем объект задачи из БД
    
    def add_task(self):
        title = self.entry.get().strip() # Получаем текст из поля ввода и удаляем пробелы по краям
        if not title:
            messagebox.showerror("Ошибка", "Задача не может быть пустой")
            return # Если пусто - показываем всплывающую ошибку и выходим из метода
        
        try:
            self.db.add_task(title)
            self.refresh_list()
            self.entry.delete(0, tk.END)
        except Exception as e:                              # Пытаемся добавить, обновить список и очистить поле
            messagebox.showerror("Ошибка", str(e))          # При любой ошибке показываем сообщение
    
    def delete_task(self):
        try:
            task = self.get_selected_task()
            self.db.delete_task(task.id)
            self.refresh_list()
        except TaskNotFoundError:
            messagebox.showerror("Ошибка", "Выберите задачу")
    
    def complete_task(self):
        try:
            task = self.get_selected_task()
            if task.completed:
                messagebox.showinfo("Инфо", "Задача уже выполнена")
                return
            self.db.complete_task(task.id)
            self.refresh_list()
        except TaskNotFoundError:
            messagebox.showerror("Ошибка", "Выберите задачу")
    
    def run(self):
        self.root.mainloop()
        self.db.close()

if __name__ == "__main__": # тут проверка , что файл запущен не из модуля , а на прямую
    app = TodoApp() # создаём объект приложение
    app.run() # и вот тут запускаем его