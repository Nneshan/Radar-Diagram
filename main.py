import tkinter as tk
import numpy as np

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

BG_COLOR = "#1E1E1E"
PANEL_COLOR = "#252526"
TEXT_COLOR = "#FFFFFF"

FACTIONS = ["Война", "Разрушение", "Магия", "Порядок", "Могущество", "Машины"]

ICON_FILES = {
    "Война": "War.png",
    "Разрушение": "Destruction.png",
    "Магия": "Magic.png",
    "Порядок": "Order.png",
    "Могущество": "Might.png",
    "Машины": "Machines.png"
}

buttons = []
icons = []

def select_faction(index):
    # Снятие подсветки
    for button in buttons:
        button.config(relief=tk.FLAT, borderwidth=0)

    buttons[index].config(relief=tk.RIDGE, borderwidth=3)

    print(f"Выбрана фракция: {FACTIONS[index]}")

    draw_faction(FACTIONS[index])

def draw_faction(name):
    ax.clear()

    ax.set_facecolor(BG_COLOR)
    ax.tick_params(colors=TEXT_COLOR)
    ax.spines["polar"].set_color(TEXT_COLOR)

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

    ax.set_yticks([2, 4, 6, 8, 10])
    ax.set_yticklabels([])

    stats_text = ""

    for label, value in zip(labels, FACTION_STATS[name]):
        stats_text += f"{label}: {value}\n"
    stats_label.config(text=stats_text)

    canvas.draw()

# Окно
root = tk.Tk()
root.title("Radar-diagram")
root.geometry("800x600")
root.configure(bg=BG_COLOR)

stats_label = tk.Label(root, text="", bg=BG_COLOR, fg=TEXT_COLOR, justify=tk.LEFT)
stats_label.pack(pady=10)

# Контейнер какой-то
top_frame = tk.Frame(root, bg=PANEL_COLOR)
top_frame.pack(pady=(30, 40))

# Кнопки
for i, faction in enumerate(FACTIONS):
    icon = tk.PhotoImage(file=f"icons/{ICON_FILES[faction]}")
    icons.append(icon)

    button = tk.Button(top_frame, image=icon, borderwidth=0, highlightthickness=0, bg=PANEL_COLOR, activebackground=PANEL_COLOR, command=lambda idx=i: select_faction(idx))
    button.pack(side=tk.LEFT, padx=40)
    buttons.append(button)

# График
figure = Figure(figsize=(5,5))
ax = figure.add_subplot(111, polar=True)
figure.patch.set_facecolor(BG_COLOR)
ax.set_facecolor(BG_COLOR)
ax.tick_params(colors=TEXT_COLOR)
ax.spines["polar"].set_color(TEXT_COLOR)

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

buttons[0].config(
    relief=tk.RIDGE,
    borderwidth=3
)

# Запуск
root.mainloop()