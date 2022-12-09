# Примеры построения графиков

import tkinter as tk

#Импорт внешних файлов
import chart1
import chart2
import chart3

# Функция закрытия программы
def do_close():
    window.destroy()

# Создание главного окна
window = tk.Tk()
window.geometry("450x550")
window.title("Примеры построения графиков")

# Добавление метки заголовка
lblTitle = tk.Label(text = "Примеры построения графиков", font = ('Helvetica', 18, 'bold'), fg = '#6600CC')
lblTitle.place(x=25, y=35)

# Добавление кнопки и метки для графика 1
btnChart1 = tk.Button(window, text="График 1", font = ('Helvetica', 10, 'bold'), command=chart1.plot_chart)
btnChart1.place(x=30, y=100, width=120, height=40)

lblChart1 = tk.Label(text = "Cинус matplotlib", font = ('Helvetica', 10), fg = '#6600CC')
lblChart1.place(x=165, y=100)

# Добавление кнопки и метки для диаграммы 1
btnChart1 = tk.Button(window, text="Диаграмма 1", font = ('Helvetica', 10, 'bold'), command=chart2.plot_chart)
btnChart1.place(x=30, y=150, width=120, height=40)

lblChart1 = tk.Label(text = "Горизонтальная столбчатая диаграмма", font = ('Helvetica', 10), fg = '#6600CC')
lblChart1.place(x=165, y=150)

# Добавление кнопки и метки для графика 2
btnChart1 = tk.Button(window, text="График 2", font = ('Helvetica', 10, 'bold'), command=chart3.plot_chart)
btnChart1.place(x=30, y=200, width=120, height=40)

lblChart1 = tk.Label(text = "Нормальное распределение", font = ('Helvetica', 10), fg = '#6600CC')
lblChart1.place(x=165, y=200)

# Добавление кнопки и метки для графика 3
btnChart1 = tk.Button(window, text="График 3", font = ('Helvetica', 10, 'bold'), command=chart3.plot_chart2)
btnChart1.place(x=30, y=250, width=120, height=40)

lblChart1 = tk.Label(text = "Нормальное распределение - 3 графика", font = ('Helvetica', 10), fg = '#6600CC')
lblChart1.place(x=165, y=250)

# Добавление кнопки и метки для графика 4
btnChart1 = tk.Button(window, text="График 4", font = ('Helvetica', 10, 'bold'), command=chart3.plot_chart2)
btnChart1.place(x=30, y=300, width=120, height=40)

# Добавление кнопки и метки для графика 5
btnChart1 = tk.Button(window, text="График 5", font = ('Helvetica', 10, 'bold'), command=chart3.plot_chart2)
btnChart1.place(x=30, y=350, width=120, height=40)

# Добавление кнопки и метки для графика 6
btnChart1 = tk.Button(window, text="График 6", font = ('Helvetica', 10, 'bold'), command=chart3.plot_chart2)
btnChart1.place(x=30, y=400, width=120, height=40)

# Добавление кнопки и метки для графика 7
btnChart1 = tk.Button(window, text="График 7", font = ('Helvetica', 10, 'bold'), command=chart3.plot_chart2)
btnChart1.place(x=30, y=400, width=120, height=40)


# Добавление кнопки закрытия программы
btnClose = tk.Button(window, text="Закрыть", font = ('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(x=300, y=500, width=90, height=30)

# Запуск цикла mainloop
window.mainloop()
