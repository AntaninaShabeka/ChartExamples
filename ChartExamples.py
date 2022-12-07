# Примеры построения графиков

import tkinter as tk

#Импорт внешних файлов
import chart1

# Функция закрытия программы
def do_close():
    window.destroy()

# Создание главного окна
window = tk.Tk()
window.geometry("450x450")
window.title("Примеры построения графиков")

# Добавление метки заголовка
lblTitle = tk.Label(text = "Примеры построения графиков", font = ('Helvetica', 18, 'bold'), fg = '#6600CC')
lblTitle.place(x=25, y=35)

# Добавление кномки и метки для графика 1
btnChart1 = tk.Button(window, text="График 1", font = ('Helvetica', 10, 'bold'), command=chart1.plot_chart)
btnChart1.place(x=30, y=100, width=120, height=40)

lblChart1 = tk.Label(text = "График синуса matplotlib", font = ('Helvetica', 14), fg = '#6600CC')
lblChart1.place(x=200, y=100)

# Добавление кнопки закрытия программы
btnClose = tk.Button(window, text="Закрыть", font = ('Helvetica', 10, 'bold'), command=do_close)
btnClose.place(x=300, y=400, width=90, height=30)

# Запуск цикла mainloop
window.mainloop()
