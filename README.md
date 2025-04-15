# Garage Tracker

A Python desktop application for tracking vehicle maintenance and fuel consumption.

## Features

- Manage multiple vehicles (add, edit, delete)
- Record maintenance activities with costs and details
- Track fuel refills with consumption statistics
- View maintenance and fuel history for each vehicle
- Data persistence with JSON storage

## Technical Overview

Garage Tracker is built with Python and Tkinter, following a Model-View-Controller architecture pattern:

### Models

- `Vehicle`: Stores vehicle information (plate number, make, model, year, mileage)
- `LogEntry`: Base class for all log entries
- `Maintenance`: Child class for maintenance records
- `Fuel`: Child class for fuel refill records

### Core

- `DataManager`: Central component handling data operations (CRUD operations, data loading/saving)

### UI

- `MainWindow`: Main application interface
- Multiple dialog classes for adding/editing vehicles and logs

## Installation

1. Clone the repository
2. Ensure Python 3.6+ is installed
3. Run `main_app.py`:
   ```
   python main_app.py
   ```

## Usage

### Adding a Vehicle

1. Click the "Add Vehicle" button
2. Enter the required information:
   - Plate number (format: letters, numbers, dashes, 4-10 chars)
   - Make
   - Model
   - Year
   - Current mileage
3. Click "Add"

### Recording Maintenance

1. Select a vehicle from the list
2. Click "Add Maintenance"
3. Enter maintenance details:
   - Date (DD-MM-YYYY)
   - Updated mileage
   - Maintenance type
   - Cost
   - Optional notes
4. Click "Add"

### Recording Fuel

1. Select a vehicle from the list
2. Click "Add Fuel"
3. Enter fuel details:
   - Date (DD-MM-YYYY)
   - Fuel type
   - Volume in liters
   - Total cost
   - Location
4. Click "Add"

### Viewing Vehicle Logs

1. Select a vehicle from the list
2. Click "View Logs"
3. A dialog will show maintenance and fuel history for the selected vehicle

## Data Structure

Data is stored in a JSON file at `data/garage_data.json` with the following structure:

```json
{
  "vehicles": [
    {
      "id": "uuid-string",
      "plate_number": "AB-123-CD",
      "make": "Toyota",
      "model": "Corolla",
      "year": 2018,
      "mileage": 45000
    }
  ],
  "logs": [
    {
      "id": "uuid-string",
      "type": "maintenance",
      "vehicle_id": "uuid-string",
      "date": "12-04-2024",
      "mileage": 42000,
      "maintenance_type": "Oil Change",
      "cost": 85.5,
      "notes": "Changed oil filter as well"
    },
    {
      "id": "uuid-string",
      "type": "fuel",
      "vehicle_id": "uuid-string",
      "date": "10-04-2024",
      "mileage": 41500,
      "fuel_type": "Unleaded",
      "liters": 45.2,
      "price": 1.75,
      "total_cost": 79.1,
      "location": "Shell Station"
    }
  ]
}
```

## Testing

The application includes unit tests for core functionality:
- `test_manager/data_manager_test.py`: Tests for the DataManager class
- `test_models/vehicle_test.py`: Tests for the Vehicle model

Run tests using unittest:
```
python -m unittest discover tests
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
