from core.data_manager import DataManager
import tkinter as tk

from ui.main_windows import MainWindow

data_manager = DataManager()
data_manager.load_all("data/garage_data.json")

root = tk.Tk()
root.title("Garage Tracker")
root.geometry("800x500")
root.resizable(True, True)

label = tk.Label(root, text="Welcome to Garage Tracker !", font=("Arial", 14))
label.pack(pady=50)

main_window = MainWindow(root, data_manager)
main_window.mainloop()