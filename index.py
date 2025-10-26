import tkinter as tk
from tkinter import messagebox

def check_winner():
    global winner
    for combo in [[0,1,2],[3,4,5],[6,7,8],[1,4,7],[0,3,6],[2,5,8],[0,4,8],[2,4,6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]]["bg"] = "green"
            buttons[combo[1]]["bg"] = "green"
            buttons[combo[2]]["bg"] = "green"
            messagebox.showinfo("Winner",f"Winner is {buttons[combo[0]]['text']}")
            winner = True
            disable_buttons()
            return
    
    if all(button["text"] != "" for button in buttons) and not winner:
        messagebox.showinfo("Draw", "It's a draw!")
        disable_buttons()

def button_click(index):
    global winner
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        buttons[index]["bg"] = "blue"
        check_winner()
        if not winner:
            toggle_player()

def disable_buttons():
    for button in buttons:
        button.config(state="disabled")

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

root = tk.Tk()
root.title("Tic Tac Toe")

current_player = "X"
winner = False

buttons = []
for i in range(9):
    button = tk.Button(root, text="", font=("Helvetica", 20), width=4, height=2,
                       command=lambda index=i: button_click(index))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

label = tk.Label(root, text="Player X's turn", font=("Helvetica", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()