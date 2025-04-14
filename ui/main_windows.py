import tkinter as tk
from core.data_manager import DataManager
from ui.dialog import AddVehicleDialog, DeleteVehicleDialog, EditVehicleDialog, AddMaintenanceDialog, AddFuelDialog, ViewLogsDialog


class MainWindow(tk.Frame):
    def __init__(self, master, data_manager: DataManager):
        super().__init__(master)
        self.data_manager = data_manager
        self.pack()

        self.vehicle_listbox = tk.Listbox(self, width=50, height=15)
        self.vehicle_listbox.pack(pady=10)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=5)

        self.add_vehicle_button = tk.Button(button_frame, text="Add Vehicle", command=self.add_vehicle)
        self.add_vehicle_button.pack(side=tk.LEFT, padx=5)

        self.delete_vehicle_button = tk.Button(button_frame, text="Delete Vehicle", command=self.delete_vehicle)
        self.delete_vehicle_button.pack(side=tk.LEFT, padx=5)

        self.update_button = tk.Button(button_frame, text="Edit Vehicle", command=self.edit_vehicle)
        self.update_button.pack(side=tk.LEFT, padx=5)

        self.add_maintenance_button = tk.Button(button_frame, text="Add Maintenance", command=self.add_maintenance)
        self.add_maintenance_button.pack(side=tk.LEFT, padx=5)

        self.add_fuel_button = tk.Button(button_frame, text="Add Fuel", command=self.add_fuel)
        self.add_fuel_button.pack(side=tk.LEFT, padx=5)

        self.view_logs_button = tk.Button(button_frame, text="View Logs", command=self.view_logs)
        self.view_logs_button.pack(side=tk.LEFT, padx=5)


        self.refresh_vehicle_list()

    def refresh_vehicle_list(self):
        self.vehicle_listbox.delete(0, tk.END)
        for vehicle in self.data_manager.vehicles:
            self.vehicle_listbox.insert(tk.END, f"[{vehicle.plate_number}] - {vehicle.make} {vehicle.model} ({vehicle.year}) {vehicle.mileage}Km")
        self.vehicle_listbox.selection_clear(0, tk.END)

    # Add vehicle
    def add_vehicle(self):
        def handle_new_vehicle(vehicle):
            try:
                self.data_manager.add_vehicle(vehicle)
                self.data_manager.save_all("data/garage_data.json")
                self.refresh_vehicle_list()
            except ValueError as e:
                tk.messagebox.showerror("Error", str(e))

        AddVehicleDialog(self, handle_new_vehicle)

    # Delete vehicle
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

    # Edit vehicle
    def edit_vehicle(self):
        selected = self.vehicle_listbox.curselection()
        if not selected:
            tk.messagebox.showwarning("Warning", "Please select a vehicle to edit.")
            return

        vehicle_index = selected[0]
        vehicle = self.data_manager.vehicles[vehicle_index]

        def handle_edit_vehicle(updated_vehicle):
            try:
                self.data_manager.edit_vehicle(updated_vehicle)
                self.data_manager.save_all("data/garage_data.json")
                self.refresh_vehicle_list()
            except ValueError as e:
                tk.messagebox.showerror("Error", str(e))

        EditVehicleDialog(self, vehicle, handle_edit_vehicle)

    # Add a maintenance
    def add_maintenance(self):
        selected = self.vehicle_listbox.curselection()
        if not selected:
            tk.messagebox.showwarning("Warning", "Please select a vehicle to add an maintenance.")
            return

        vehicle_index = selected[0]
        vehicle = self.data_manager.vehicles[vehicle_index]

        def handle_add_maintenance(maintenance):
            try:
                self.data_manager.add_log(maintenance)
                self.data_manager.save_all("data/garage_data.json")
                self.refresh_vehicle_list()
            except ValueError as e:
                tk.messagebox.showerror("Error", str(e))

        AddMaintenanceDialog(self, vehicle, handle_add_maintenance)

    # Add a fuel
    def add_fuel(self):
        selected = self.vehicle_listbox.curselection()
        if not selected:
            tk.messagebox.showwarning("Warning", "Please select a vehicle to add a fuel.")
            return

        vehicle_index = selected[0]
        vehicle = self.data_manager.vehicles[vehicle_index]

        def handle_add_fuel(new_fuel):
            try:
                self.data_manager.add_log(new_fuel)
                self.data_manager.save_all("data/garage_data.json")
                self.refresh_vehicle_list()
            except ValueError as e:
                tk.messagebox.showerror("Error", str(e))

        AddFuelDialog(self, vehicle, handle_add_fuel)

    def view_logs(self):
        selected = self.vehicle_listbox.curselection()
        if not selected:
            tk.messagebox.showwarning("Warning", "Please select a vehicle to add a fuel.")
            return

        vehicle_index = selected[0]
        vehicle = self.data_manager.vehicles[vehicle_index]

        ViewLogsDialog(self, vehicle, self.data_manager.logs)











