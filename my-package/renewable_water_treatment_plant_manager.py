import csv

class TreatmentPlant():
    def __init__(self, plant_name, country, technology, capacity, water_source, status):
        self.plant_name = plant_name
        self.country = country
        self.technology = technology
        self.capacity = capacity
        self.water_source = water_source
        self.status = status
        
    def __str__(self):
        return f"Plant Name: {self.plant_name}, Country: {self.country}, Technology: {self.technology}, Capacity: {self.capacity}, Water Source: {self.water_source}, Status: {self.status}"
    
class PlantManager():
    def __init__(self):
        self.plants = []
    
    def add_plant(self, plant):
        if plant.capacity < 0:
            print("Capacity must be greater than 0.")
            return
        for existing_plant in self.plants:
            if existing_plant.plant_name == plant.plant_name and existing_plant.country == plant.country:
                print("This Plant is Already Existed!")
                return
        self.plants.append(plant)
        self.save_plant()
        
    def remove_plant(self, plant_name):
        for existing_plant in self.plants:
            if existing_plant.plant_name == plant_name:
                self.plants.remove(existing_plant)
                self.save_plant()
                return
        print("The Plant was not found!")
                
    def search_plant(self, plant_name):
        for existing_plant in self.plants:
            if existing_plant.plant_name == plant_name:
                return (existing_plant)
        return None
        
    def edit(self, current_name, current_country, new_name, new_country, new_technology, new_capacity, new_water_source, new_status):
        if new_capacity < 0:
            print("Capacity must be greater than 0.")
            return
        for existing_plant in self.plants:
            if existing_plant.plant_name == current_name and existing_plant.country == current_country:
                existing_plant.plant_name = new_name
                existing_plant.country = new_country
                existing_plant.technology = new_technology
                existing_plant.capacity = new_capacity
                existing_plant.water_source = new_water_source
                existing_plant.status = new_status
                self.save_plant()
                return
        print("The Plant was not Found!")
            
    def show_plants_by_country(self, user_country):
        if not self.plants:
            print("There are no Plants!")
            return
        count = 0
        for existing_plant in self.plants:
            if existing_plant.country == user_country:
                count += 1
                print(existing_plant)
        print(f"Total plants in {user_country}: {count}")
            
    def show_plants_by_technology(self, user_technology):
        if not self.plants:
            print("There are no Plants!")
            return
        count = 0
        for existing_plant in self.plants:
            if existing_plant.technology == user_technology:
                count += 1
                print(existing_plant)
        print(f"Total plants with {user_technology} technology: {count}")
    
    def show_plants_by_water_source(self, user_water_source):
        if not self.plants:
            print("There are no Plants!")
            return
        count = 0
        for existing_plant in self.plants:
            if existing_plant.water_source == user_water_source:
                count += 1
                print(existing_plant)
        print(f"Total plants with {user_water_source} as their water source: {count}")
    
    def total_capacity(self):
        if not self.plants:
            print("There are no Plants!")
            return
        total_capacity = 0
        for existing_plant in self.plants:
            total_capacity += existing_plant.capacity
        print(f"Total capacity: {total_capacity} MW")
    
    def largest_plant(self):
        if not self.plants:
            print("There are no Plants!")
            return
        largest = self.plants[0].capacity
        name = self.plants[0].plant_name
        for existing_plant in self.plants:
            if existing_plant.capacity > largest:
                largest = existing_plant.capacity
                name = existing_plant.plant_name
        print(f"The largest plant is {name} with {largest:.2f} MW capacity")
    
    def count_plants_by_status(self, user_status):
        if not self.plants:
            print("There are no Plants!")
            return
        count = 0
        for existing_plant in self.plants:
            if existing_plant.status == user_status:
                count += 1
        print(f"Total plants with {user_status} status: {count}")
    
    def show_high_capacity_plants(self, min_capacity):
        if not self.plants:
            print("There are no Plants!")
            return
        count = 0
        for existing_plant in self.plants:
            if existing_plant.capacity > min_capacity:
                count += 1
                print(existing_plant)
        print(f"The number of plants with capacity greater than {min_capacity} MW: {count}")
    
    def average_capacity_by_technology(self, user_technology):
        if not self.plants:
            print("There are no Plants!")
            return
        total = 0
        total_capacity = 0
        for existing_plant in self.plants:
            if existing_plant.technology == user_technology:
                total += 1
                total_capacity += existing_plant.capacity
        if total == 0:
            print("There are no plants with this technology.")
            return
        avg_capacity = total_capacity / total
        print(f"Average capacity of plants with {user_technology} technology: {avg_capacity:.2f} MW")
                
    def save_plant(self):
        fieldnames = ("Plant Name", "Country", "Technology", "Capacity", "Water Source", "Status")
        with open("renewable_water_treatment_plant_manager.csv", mode = "w", newline = "") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for existing_plant in self.plants:
                dict_plant = {"Plant Name": existing_plant.plant_name, "Country": existing_plant.country, "Technology": existing_plant.technology, "Capacity": existing_plant.capacity, "Water Source": existing_plant.water_source, "Status": existing_plant.status}
                writer.writerow(dict_plant)
    
    def load_plant(self):
        self.plants = []
        try:
            with open("renewable_water_treatment_plant_manager.csv", mode = "r", newline = "") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    plant = TreatmentPlant(row["Plant Name"], row["Country"], row["Technology"], float(row["Capacity"]), row["Water Source"], row["Status"])
                    self.plants.append(plant)
        except FileNotFoundError:
            pass
            
    
if __name__ == "__main__":
    print("you should use me as a package.")