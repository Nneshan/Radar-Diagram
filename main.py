import tkinter as tk

FACTIONS = ["Война", "Разрушение", "Магия", "Порядок", "Могущество", "Машины"]

buttons = []

def select_faction(index):
    # Снятие подсветки
    for button in buttons:
        button.config(relief=tk.RAISED)

    buttons[index].config(relief=tk.SUNKEN)

    print(f"Выбрана фракция: {FACTIONS[index]}")

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

# Запуск
root.mainloop()