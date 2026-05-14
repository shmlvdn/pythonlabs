import tkinter as tk # tkinter это встроенная библиотека для создания окон и кнопок
from tkinter import ttk, messagebox # ttk стильные виджеты, messagebox всплывающие окошки с ошибками или предупреждениями
from openpyxl import Workbook 
from datetime import datetime 
import os # Для работы с путями к папкам

from car_base import PassengerCar, Truck, Bus
from fuel_calc import calculate_fuel
from time_calc import calculate_time

# создаем шаблоны машин и пустую папку для результата
cars = {
    "Легковой": PassengerCar(),
    "Грузовой": Truck(),
    "Пассажирский": Bus()
}
last_result = None 

# Функция расчёта
def calculate():
    global last_result
    
    try:
        # программа смотрит что вписал пользователь и превращает это в числа для высчета
        car_type = car_var.get()
        distance = float(dist_entry.get())
        load = float(load_entry.get())
        price = float(price_entry.get())
        speed = float(speed_entry.get())
        
        # проверяем
        if distance <= 0 or price <= 0 or speed <= 0 or load < 0:
            messagebox.showerror("Ошибка", "Расстояние, цена и скорость > 0, загрузка >= 0")
            return
        
        car = cars[car_type] #чтоб ыпо названию автомобьиля программа брала его характеристики
        
        if load > car.max_load:
            messagebox.showerror("Ошибка", f"Перегруз! Максимум {car.max_load} кг")
            return
        
        # вызываем функции, котррые считают топливовремя и сохраняем результаты
        fuel, cost = calculate_fuel(car, distance, load, price)
        hours = calculate_time(distance, speed)
        
        # Сохраняем результат
        last_result = {
            "Автомобиль": car.name,
            "Расстояние (км)": distance,
            "Загрузка (кг)": load,
            "Цена (руб/л)": price,
            "Скорость (км/ч)": speed,
            "Топливо (л)": round(fuel, 2),
            "Стоимость (руб)": round(cost, 2),
            "Время (ч)": round(hours, 2)
        }
        
        # Выводим результат
        result_text.config(state="normal")
        result_text.delete(1.0, tk.END)
        for key, val in last_result.items():
            result_text.insert(tk.END, f"{key}: {val}\n")
        result_text.config(state="disabled")
        
    except ValueError:
        messagebox.showerror("Ошибка", "Введи числа во все поля")


def save_to_excel():
    if last_result is None:
        messagebox.showwarning("Нет данных", "Сначала нажми 'Рассчитать'")
        return
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Отчёт"
    ws.append(["Параметр", "Значение"])
    
    for key, val in last_result.items():
        ws.append([key, val])
    
    filename = f"report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    wb.save(os.path.join(desktop, filename))
    
    messagebox.showinfo("Сохранено", f"Файл на рабочем столе:\n{filename}")


root = tk.Tk()
root.title("Расчёт топлива")
root.geometry("450x500")

tk.Label(root, text="Тип автомобиля:").grid(row=0, column=0, padx=10, pady=5)
car_var = tk.StringVar(value="Легковой")
car_menu = tk.OptionMenu(root, car_var, "Легковой", "Грузовой", "Пассажирский")
car_menu.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Расстояние (км):").grid(row=1, column=0, padx=10, pady=5)
dist_entry = tk.Entry(root)
dist_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Загрузка (кг):").grid(row=2, column=0, padx=10, pady=5)
load_entry = tk.Entry(root)
load_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Цена топлива (руб/л):").grid(row=3, column=0, padx=10, pady=5)
price_entry = tk.Entry(root)
price_entry.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Средняя скорость (км/ч):").grid(row=4, column=0, padx=10, pady=5)
speed_entry = tk.Entry(root)
speed_entry.grid(row=4, column=1, padx=10, pady=5)

tk.Button(root, text="Рассчитать", command=calculate, bg="lightblue").grid(row=5, column=0, columnspan=2, pady=10)

result_text = tk.Text(root, height=10, width=45, state="disabled")
result_text.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

tk.Button(root, text="Сохранить в Excel", command=save_to_excel, bg="lightgreen").grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()