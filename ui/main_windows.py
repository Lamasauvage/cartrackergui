import tkinter as tk
from core.data_manager import DataManager
from ui.dialog import AddVehicleDialog, DeleteVehicleDialog


class MainWindow(tk.Frame):
    def __init__(self, master, data_manager: DataManager):
        super().__init__(master)
        self.data_manager = data_manager
        self.pack()

        self.vehicle_listbox = tk.Listbox(self, width=50, height=15)
        self.vehicle_listbox.pack(pady=10)

        self.add_vehicle_button = tk.Button(self, text="Add Vehicle", command=self.add_vehicle)
        self.add_vehicle_button.pack(pady=5)

        self.delete_vehicle_button = tk.Button(self, text="Delete Vehicle", command=self.delete_vehicle)
        self.delete_vehicle_button.pack(pady=5)

        self.refresh_vehicle_list()

    def refresh_vehicle_list(self):
        self.vehicle_listbox.delete(0, tk.END)
        for vehicle in self.data_manager.vehicles:
            self.vehicle_listbox.insert(tk.END, f"{vehicle.plate_number} - {vehicle.make} {vehicle.model} ({vehicle.year})")
        self.vehicle_listbox.selection_clear(0, tk.END)


    def add_vehicle(self):
        def handle_new_vehicle(vehicle):
            try:
                self.data_manager.add_vehicle(vehicle)
                self.data_manager.save_all("data/garage_data.json")
                self.refresh_vehicle_list()
            except ValueError as e:
                tk.messagebox.showerror("Error", str(e))

        AddVehicleDialog(self, handle_new_vehicle)


    def delete_vehicle(self):
        selected = self.vehicle_listbox.curselection()
        if not selected:
            tk.messagebox.showwarning("Warning", "Please select a vehicle to delete.")
            return

        vehicle_index = selected[0]
        vehicle = self.data_manager.vehicles[vehicle_index]

        confirm = tk.messagebox.askyesno("Confirm Deletion", f"Delete {vehicle.plate_number}?")
        if confirm:
            try:
                self.data_manager.remove_vehicle(vehicle)
                self.data_manager.save_all("data/garage_data.json")
                self.refresh_vehicle_list()
            except ValueError as e:
                tk.messagebox.showerror("Error", str(e))

