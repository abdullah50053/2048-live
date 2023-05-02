# 2048 Game
import tkinter as tk
import random

class Game(tk.Frame):
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("2048")
        self.main_grid = tk.Frame(
            self, bg="#92877d", bd=5, width=800, height=800
        )
        self.main_grid.grid(pady=(110, 0))

def main():
    print()

if __name__ == "__main__":
    main()