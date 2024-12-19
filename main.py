import matplotlib.pyplot as plt

def plot_line_graph(x, y, title="Line Graph", xlabel="X-axis", ylabel="Y-axis"):
    # Функция для создания линейного графика.
    # :param x: Список или массив значений по оси X.
    # :param y: Список или массив значений по оси Y.
    # :param title: Заголовок графика.
    # :param xlabel: Название оси X.
    # :param ylabel: Название оси Y.

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



def create_pie_chart(data, labels, title='Круговая диаграмма'):
    # Создает круговую диаграмму с заданными данными и метками.
    # :param data: Список значений для круговой диаграммы.
    # :param labels: Список меток для каждого сегмента диаграммы.
    # :param title: Заголовок диаграммы.
    # Создаем круговую диаграмму

    plt.figure(figsize=(8, 8))  # Устанавливаем размер фигуры
    plt.pie(data, labels=labels, autopct='%1.1f%%', startangle=90)

    # Устанавливаем равные оси, чтобы круговая диаграмма была кругом
    plt.axis('equal')

    # Устанавливаем заголовок диаграммы
    plt.title(title)

    # Показываем диаграмму
    plt.show()

# Пример данных
data = [30, 20, 25, 25]
labels = ['Категория A', 'Категория B', 'Категория C', 'Категория D']

# Создаем круговую диаграмму
create_pie_chart(data, labels, title='Пример круговой диаграммы')