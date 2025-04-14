import tkinter as tk
import re

from tkinter import messagebox
from models.vehicle import Vehicle
from models.maintenance import Maintenance
from models.fuel import Fuel

class AddVehicleDialog(tk.Toplevel):
    def __init__(self, master, on_submit):
        super().__init__(master)
        self.title("Add New Vehicle")
        self.geometry("350x300")
        self.resizable(True, True)
        self.on_submit = on_submit

        tk.Label(self, text="Plate Number").pack()
        self.entry_plate = tk.Entry(self)
        self.entry_plate.pack()

        tk.Label(self, text="Make").pack()
        self.entry_make = tk.Entry(self)
        self.entry_make.pack()

        tk.Label(self, text="Model").pack()
        self.entry_model = tk.Entry(self)
        self.entry_model.pack()

        tk.Label(self, text="Year").pack()
        self.entry_year = tk.Entry(self)
        self.entry_year.pack()

        tk.Label(self, text="Mileage").pack()
        self.entry_mileage = tk.Entry(self)
        self.entry_mileage.pack()

        tk.Button(self, text="Add", command=self.submit).pack(pady=10)

    def submit(self):
        try:
            plate = self.entry_plate.get()
            make = self.entry_make.get()
            model = self.entry_model.get()
            year = int(self.entry_year.get())
            mileage = int(self.entry_mileage.get())


            if not re.match(r"^[A-Z0-9-]{4,10}$", plate):
                messagebox.showerror("Invalid plate", "Plate must be 4–10 characters: letters, numbers, dashes only.")
                return

            vehicle = Vehicle(plate, make, model, year, mileage)
            self.on_submit(vehicle)
            self.destroy()

        except ValueError:
            messagebox.showerror("Input Error", "Year and mileage must be numbers.")


class DeleteVehicleDialog(tk.Toplevel):
    def __init__(self, master, on_delete):
        super().__init__(master)
        self.title("Delete Vehicle")
        self.geometry("300x250")
        self.resizable(True, True)
        self.on_delete = on_delete

        # Champs de saisie
        tk.Label(self, text="Plate Number").pack()
        self.entry_plate = tk.Entry(self)
        self.entry_plate.pack()

        tk.Button(self, text="Delete", command=self.delete).pack(pady=10)

    def delete(self):
        plate = self.entry_plate.get()
        if not plate:
            messagebox.showerror("Input Error", "Please enter a plate number.")
            return

        if not re.match(r"^[A-Z0-9-]{4,10}$", plate):
            messagebox.showerror("Invalid plate", "Plate must be 4–10 characters: letters, numbers, dashes only.")
            return

        self.on_delete(plate)
        self.destroy()


class EditVehicleDialog(tk.Toplevel):
    def __init__(self, master, vehicle, on_edit):
        super().__init__(master)
        self.title("Edit Vehicle")
        self.geometry("350x300")
        self.resizable(True, True)
        self.on_edit = on_edit
        self.vehicle = vehicle

        tk.Label(self, text="Plate Number").pack()
        self.entry_plate = tk.Entry(self)
        self.entry_plate.insert(0, vehicle.plate_number)
        self.entry_plate.pack()

        tk.Label(self, text="Make").pack()
        self.entry_make = tk.Entry(self)
        self.entry_make.insert(0, vehicle.make)
        self.entry_make.pack()

        tk.Label(self, text="Model").pack()
        self.entry_model = tk.Entry(self)
        self.entry_model.insert(0, vehicle.model)
        self.entry_model.pack()

        tk.Label(self, text="Year").pack()
        self.entry_year = tk.Entry(self)
        self.entry_year.insert(0, vehicle.year)
        self.entry_year.pack()

        tk.Label(self, text="Mileage").pack()
        self.entry_mileage = tk.Entry(self)
        self.entry_mileage.insert(0, vehicle.mileage)
        self.entry_mileage.pack()

        tk.Button(self, text="Update", command=self.submit).pack(pady=10)

    def submit(self):
        try:
            plate = self.entry_plate.get()
            make = self.entry_make.get()
            model = self.entry_model.get()
            year = int(self.entry_year.get())
            mileage = int(self.entry_mileage.get())

            updated_vehicle = Vehicle(
                plate_number=plate,
                make=make,
                model=model,
                year=year,
                mileage=mileage,
                id=str(self.vehicle.id)
            )

            self.on_edit(updated_vehicle)
            self.destroy()
        except ValueError:
            messagebox.showerror("Input Error", "Year and mileage must be numbers.")


class AddMaintenanceDialog(tk.Toplevel):
    def __init__(self, master, vehicle, on_add):
        super().__init__(master)
        self.title("Add Maintenance")
        self.geometry("350x350")
        self.resizable(False, False)

        self.vehicle = vehicle
        self.on_submit = on_add

        tk.Label(self, text=f"Vehicle : {vehicle.model}").pack(pady=5)

        tk.Label(self, text="Date (DD-MM-YYYY)").pack()
        self.entry_date = tk.Entry(self)
        self.entry_date.pack()

        tk.Label(self, text="Mileage").pack()
        self.entry_mileage = tk.Entry(self)
        self.entry_mileage.pack()

        tk.Label(self, text="Type").pack()
        self.entry_type = tk.Entry(self)
        self.entry_type.pack()

        tk.Label(self, text="Cost (€)").pack()
        self.entry_cost = tk.Entry(self)
        self.entry_cost.pack()

        tk.Label(self, text="Notes (optional)").pack()
        self.entry_notes = tk.Entry(self)
        self.entry_notes.pack()

        tk.Button(self, text="Add", command=self.submit).pack(pady=10)

    def submit(self):
        try:
            date = self.entry_date.get()
            mileage = int(self.entry_mileage.get())
            maintenance_type = self.entry_type.get()
            cost = float(self.entry_cost.get())
            notes = self.entry_notes.get()

            if not re.match(r"^\d{2}-\d{2}-\d{4}$", date):
                messagebox.showerror("Invalid date", "Format attendu : DD-MM-YYYY")
                return

            maintenance = Maintenance(
                vehicle_id=self.vehicle.id,
                date=date,
                mileage=mileage,
                maintenance_type=maintenance_type,
                cost=cost,
                notes=notes
            )
            self.on_submit(maintenance)
            self.destroy()

        except ValueError:
            messagebox.showerror("Input Error", "Mileage must be an integer and cost must be a number.")


class AddFuelDialog(tk.Toplevel):
    def __init__(self, master, vehicle, on_add):
        super().__init__(master)
        self.title("Add Fuel")
        self.geometry("350x350")
        self.resizable(False, False)

        self.vehicle = vehicle
        self.on_submit = on_add

        tk.Label(self, text=f"Vehicle : {vehicle.model}").pack(pady=5)

        tk.Label(self, text="Date (DD-MM-YYYY)").pack()
        self.entry_date = tk.Entry(self)
        self.entry_date.pack()

        tk.Label(self, text="Fuel Type").pack()
        self.entry_fuel_type = tk.Entry(self)
        self.entry_fuel_type.pack()

        tk.Label(self, text="Liters").pack()
        self.entry_liters = tk.Entry(self)
        self.entry_liters.pack()

        tk.Label(self, text="Total Cost (€)").pack()
        self.entry_total_cost = tk.Entry(self)
        self.entry_total_cost.pack()

        tk.Label(self, text="Location").pack()
        self.entry_location = tk.Entry(self)
        self.entry_location.pack()

        tk.Button(self, text="Add", command=self.submit).pack(pady=10)

    def submit(self):
        try:
            date = self.entry_date.get()
            fuel_type = self.entry_fuel_type.get()
            liters = float(self.entry_liters.get())
            total_cost = float(self.entry_total_cost.get())
            location = self.entry_location.get()

            if not re.match(r"^\d{2}-\d{2}-\d{4}$", date):
                messagebox.showerror("Invalid date", "Format attendu : DD-MM-YYYY")
                return

            fuel = Fuel(
                vehicle_id=self.vehicle.id,
                date=date,
                mileage=self.vehicle.mileage,
                fuel_type=fuel_type,
                liters=liters,
                price=total_cost,
                location=location
            )

            self.on_submit(fuel)
            self.destroy()

        except ValueError:
            messagebox.showerror("Input Error", "Liters and price must be numbers.")


class ViewLogsDialog(tk.Toplevel):
    def __init__(self, master, vehicle, logs):
        super().__init__(master)
        self.title(f"Logs for {vehicle.plate_number}")
        self.geometry("600x400")
        self.resizable(False, False)

        tk.Label(self, text="Maintenance Logs", font=("Arial", 12, "bold")).pack(pady=5)
        self.maintenance_list = tk.Listbox(self, width=80)
        self.maintenance_list.pack()

        tk.Label(self, text="Fuel Logs", font=("Arial", 12, "bold")).pack(pady=5)
        self.fuel_list = tk.Listbox(self, width=80)
        self.fuel_list.pack()

        for log in logs:
            if str(log.vehicle_id) != str(vehicle.id):
                continue
            if isinstance(log, Maintenance):
                self.maintenance_list.insert(tk.END, f"{log.date} - {log.maintenance_type} - ({log.notes}) - {log.cost:.2f}€ ")
            elif isinstance(log, Fuel):
                self.fuel_list.insert(tk.END, f"{log.date} - {log.liters}L @ {log.price:.2f}€/L ({log.location})")




