import matplotlib.pyplot as plt

def plot_line_graph(x, y, title="Line Graph", xlabel="X-axis", ylabel="Y-axis"):
    """
    Функция для создания линейного графика.

    :param x: Список или массив значений по оси X.
    :param y: Список или массив значений по оси Y.
    :param title: Заголовок графика.
    :param xlabel: Название оси X.
    :param ylabel: Название оси Y.
    """
    plt.figure(figsize=(10, 6))  # Установка размера графика
    plt.plot(x, y, marker='o', linestyle='-', color='b')  # Построение графика
    plt.title(title)  # Установка заголовка графика
    plt.xlabel(xlabel)  # Установка названия оси X
    plt.ylabel(ylabel)  # Установка названия оси Y
    plt.grid(True)  # Включение сетки
    plt.show()  # Отображение графика

# Пример использования функции
x_values = [1, 2, 3, 4, 5]
y_values = [2, 3, 5, 7, 11]
plot_line_graph(x_values, y_values, title="Пример линейного графика", xlabel="Время", ylabel="Значение")