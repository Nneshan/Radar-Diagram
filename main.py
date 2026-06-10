import tkinter as tk
import numpy as np

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sympy.printing.pretty.pretty_symbology import line_width

FACTIONS = ["Война", "Разрушение", "Магия", "Порядок", "Могущество", "Машины"]

buttons = []

def select_faction(index):
    # Снятие подсветки
    for button in buttons:
        button.config(relief=tk.RAISED)

    buttons[index].config(relief=tk.SUNKEN)

    print(f"Выбрана фракция: {FACTIONS[index]}")

    draw_faction(FACTIONS[index])

def draw_faction(name):
    ax.clear()

    values = FACTION_STATS[name].copy()
    color = FACTION_COLORS[name]

    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()

    values += values[:1]
    angles += angles[:1]

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    ax.plot(angles, values, color=color, linewidth=2)
    ax.fill(angles, values, color=color, alpha=0.25)

    ax.set_ylim(0, 10)

    canvas.draw()

# Окно
root = tk.Tk()
root.title("Radar-diagram")
root.geometry("800x600")

# Контейнер какой-то
top_frame = tk.Frame(root)
top_frame.pack(pady=20)

# Кнопки
for i, faction in enumerate(FACTIONS):
    button = tk.Button(top_frame, text=faction, width=12, command=lambda idx=i: select_faction(idx))
    button.pack(side=tk.LEFT, padx=5)
    buttons.append(button)

# График
figure = Figure(figsize=(5,5))
ax = figure.add_subplot(111, polar=True)

labels = ["Агрессия", "Контроль", "Гибкость", "Автономность", "Синергия", "Потенциал"]

FACTION_STATS = {
    "Война": [8, 3, 4, 9, 5, 6],
    "Разрушение": [7, 2, 3, 8, 3, 9],
    "Магия": [3, 9, 10, 2, 9, 7],
    "Порядок": [4, 8, 4, 6, 8, 6],
    "Могущество": [5, 2, 5, 9, 4, 8],
    "Машины": [6, 5, 8, 6, 8, 7]
}

FACTION_COLORS = {
    "Война": "#C62828",
    "Разрушение": "#EF6C00",
    "Магия": "#00ACC1",
    "Порядок": "#FDD835",
    "Могущество": "#43A047",
    "Машины": "#78909C"
}

canvas = FigureCanvasTkAgg(figure, master=root)
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

draw_faction("Война")

# Запуск
root.mainloop()