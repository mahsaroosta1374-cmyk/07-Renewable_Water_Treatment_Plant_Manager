# Renewable Water Treatment Plant Manager

## Overview

A Python-based management system for organizing and analyzing renewable energy-powered water treatment plants.

The program uses Object-Oriented Programming to represent water treatment plants and provides functionality for adding, editing, removing, searching, filtering, and analyzing treatment plants based on their country, technology, water source, capacity, and operational status.

Project data is stored in a CSV file, allowing the information to be saved between program executions and loaded again when the application starts.

This project was developed as part of a Python programming practice series and focuses on **Object-Oriented Programming, CSV file handling, data validation, searching, filtering, aggregation, and basic data analysis**.

---

## Features

* Add a water treatment plant
* Edit existing plant information
* Remove a plant
* Search for a plant by name
* Display plants by country
* Display plants by technology
* Display plants by water source
* Calculate total treatment capacity
* Find the largest treatment plant
* Count plants by operational status
* Find plants above a specified capacity
* Calculate average capacity for a selected technology
* Save plant data to a CSV file
* Load existing plant data from a CSV file
* Prevent duplicate plants based on plant name and country
* Validate plant capacity before adding or editing

---

## Plant Data

Each treatment plant contains the following information:

| Field        | Description                            | Unit |
| ------------ | -------------------------------------- | ---- |
| Plant Name   | Name of the water treatment plant      | -    |
| Country      | Country where the plant is located     | -    |
| Technology   | Treatment technology used by the plant | -    |
| Capacity     | Treatment capacity of the plant        | MW   |
| Water Source | Source of water treated by the plant   | -    |
| Status       | Operational status of the plant        | -    |

---

## Main Analysis Functions

### Plants by Country

Displays all treatment plants located in a selected country and reports the total number of plants in that country.

### Plants by Technology

Displays plants using a selected treatment technology and reports how many plants use that technology.

### Plants by Water Source

Displays plants associated with a selected water source and reports the total number of plants using that source.

### Total Capacity

Calculates the combined capacity of all treatment plants.

### Largest Plant

Identifies the treatment plant with the highest capacity.

### Plants by Status

Counts the number of plants with a selected operational status.

### High-Capacity Plants

Displays plants whose capacity is greater than a user-defined minimum capacity.

### Average Capacity by Technology

Calculates the average treatment capacity of plants using a selected technology.

---

## Data Validation

The program performs basic validation before adding or editing plants.

Validation includes:

* Treatment plant capacity must not be negative.
* Duplicate plants with the same plant name and country are not allowed.
* A plant must exist before it can be edited or removed.

---

## Project Structure

```text
Renewable-Water-Treatment-Plant-Manager/
│
├── my_package/
│   ├── __init__.py
│   └── renewable_water_treatment_plant_manager.py
│
├── main.py
├── renewable_water_treatment_plant_manager.csv
└── README.md
```

---

## CSV File Handling

The project uses Python's built-in `csv` module to store and retrieve plant information.

### Saving Data

The `save_plant()` method writes all treatment plant records to:

```text
renewable_water_treatment_plant_manager.csv
```

The data is stored using `csv.DictWriter`.

### Loading Data

The `load_plant()` method reads existing records using `csv.DictReader`.

The program also handles the case where the CSV file does not exist by catching `FileNotFoundError`.

---

## Concepts Practiced

### Object-Oriented Programming

The project uses two classes:

#### `TreatmentPlant`

Represents an individual water treatment plant and stores its attributes.

#### `PlantManager`

Manages the collection of treatment plants and provides methods for data management and analysis.

Concepts practiced include:

* Classes
* Objects
* Constructors
* Instance attributes
* Instance methods
* `__str__()` method

### Lists

A list is used to store all treatment plant objects:

```python
self.plants = []
```

Plants can then be added, removed, searched, and analyzed through this collection.

### Loops

`for` loops are used extensively to:

* Search for plants
* Filter plants
* Calculate totals
* Count plants
* Find the largest plant
* Calculate average capacity
* Save plant records to CSV

### Dictionaries

Dictionaries are used when saving plant information to CSV and also provide a structured way to map field names to project attributes.

For example:

```python
dict_plant = {
    "Plant Name": existing_plant.plant_name,
    "Country": existing_plant.country,
    "Technology": existing_plant.technology,
    "Capacity": existing_plant.capacity,
    "Water Source": existing_plant.water_source,
    "Status": existing_plant.status
}
```

### Conditional Statements

`if` statements are used for:

* Data validation
* Duplicate detection
* Searching
* Filtering
* Capacity comparisons
* Status comparisons
* Handling empty collections

### Exception Handling

The project uses `try/except` when loading the CSV file:

```python
except FileNotFoundError:
    pass
```

This prevents the program from crashing when the data file has not yet been created.

---

## Data Flow

The basic workflow of the program is:

```text
Create Treatment Plant
          ↓
Validate Plant Data
          ↓
Add to Plant List
          ↓
Save to CSV
          ↓
Load Existing Data
          ↓
Search / Filter / Analyze
          ↓
Display Results
```

---

## Example Questions the Manager Can Answer

The program can be used to answer questions such as:

* How many treatment plants are located in a specific country?
* Which plants use a particular treatment technology?
* How many plants use a specific water source?
* What is the total treatment capacity?
* Which treatment plant has the largest capacity?
* How many plants have a specific operational status?
* Which plants have a capacity greater than a selected value?
* What is the average capacity of plants using a particular technology?

---

## Learning Outcomes

Through this project, I practiced building a small management system using Python and Object-Oriented Programming.

The project provided practical experience with managing a collection of objects, validating data, searching and filtering records, performing calculations, and storing structured information in CSV files.

It also helped reinforce the connection between **data management and basic engineering-oriented analysis**, particularly for water treatment and renewable-energy-related applications.

---

## Future Improvements

Possible future improvements include:

* Adding more water treatment technologies
* Adding predefined country and technology lists
* Adding more advanced data validation
* Adding sorting and ranking functions
* Adding additional statistical analysis
* Adding data visualization
* Adding filtering using multiple criteria simultaneously
* Generating analytical reports
* Improving the command-line user interface
* Adding support for larger datasets

---

## How to Run

Make sure Python is installed on your system.

Run the main program:

```bash
python main.py
```

The program can then be used to manage and analyze renewable water treatment plant data.

---

## Author

Mahsa Rousta