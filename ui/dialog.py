import tkinter as tk
import re
from tkinter import messagebox
from models.vehicle import Vehicle


class AddVehicleDialog(tk.Toplevel):
    def __init__(self, master, on_submit):
        super().__init__(master)
        self.title("Add New Vehicle")
        self.geometry("300x250")
        self.resizable(False, False)
        self.on_submit = on_submit

        # Champs de saisie
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
        self.geometry("300x150")
        self.resizable(False, False)
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
