from core.data_manager import DataManager
import tkinter as tk
from ui.main_windows import MainWindow

data_manager = DataManager()
data_manager.load_all("data/garage_data.json")

root = tk.Tk()
root.title("Garage Tracker")
root.geometry("800x500")
root.resizable(True, True)

main_window = MainWindow(root, data_manager)
root.mainloop()