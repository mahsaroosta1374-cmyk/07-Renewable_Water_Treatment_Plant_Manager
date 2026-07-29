from my_package.renewable_water_treatment_plant_manager import TreatmentPlant, PlantManager

manager = PlantManager()
manager.load_plant()

while True:
    print("\n========== Renewable Water Treatment Plant Manager ==========")
    print("1. Add New Plant")
    print("2. Remove Plant")
    print("3. Show All Plants")
    print("4. Search Plant")
    print("5. Edit Plant")
    print("6. Show Plants by Country")
    print("7. Show Plants by Technology")
    print("8. Show Plants by Water Source")
    print("9. Total Installed Capacity")
    print("10. Show Largest Plant")
    print("11. Count Plants by Status")
    print("12. Show High Capacity Plants")
    print("13. Average Capacity by Technology")
    print("14. Exit")

    choice = input("Please Enter Your Choice: ")

    if choice == "1":
        plant_name = input("Please Enter Plant Name: ")
        country = input("Please Enter Country: ")
        technology = input("Please Enter Technology: ")
        capacity = float(input("Please Enter Capacity (MW): "))
        water_source = input("Please Enter Water Source: ")
        status = input("Please Enter Status: ")

        plant = TreatmentPlant(
            plant_name,
            country,
            technology,
            capacity,
            water_source,
            status
        )
        manager.add_plant(plant)

    elif choice == "2":
        plant_name = input("Please Enter Plant Name: ")
        manager.remove_plant(plant_name)

    elif choice == "3":
        manager.show_all_plants()

    elif choice == "4":
        plant_name = input("Please Enter Plant Name: ")
        plant = manager.search(plant_name)

        if plant is None:
            print("The Plant was not Found!")
        else:
            print(plant)

    elif choice == "5":
        current_name = input("Please Enter Current Plant Name: ")
        current_country = input("Please Enter Current Country: ")

        plant = manager.search(current_name)

        if plant is None:
            print("The Plant was not Found!")
        else:
            new_name = input("Please Enter New Plant Name: ")
            new_country = input("Please Enter New Country: ")
            new_technology = input("Please Enter New Technology: ")
            new_capacity = float(input("Please Enter New Capacity (MW): "))
            new_water_source = input("Please Enter New Water Source: ")
            new_status = input("Please Enter New Status: ")

            manager.edit(
                current_name,
                current_country,
                new_name,
                new_country,
                new_technology,
                new_capacity,
                new_water_source,
                new_status
            )

    elif choice == "6":
        country = input("Please Enter Country: ")
        manager.show_plants_by_country(country)

    elif choice == "7":
        technology = input("Please Enter Technology: ")
        manager.show_plants_by_technology(technology)

    elif choice == "8":
        water_source = input("Please Enter Water Source: ")
        manager.show_plants_by_water_source(water_source)

    elif choice == "9":
        manager.total_capacity()

    elif choice == "10":
        manager.largest_plant()

    elif choice == "11":
        status = input("Please Enter Status: ")
        manager.count_plants_by_status(status)

    elif choice == "12":
        min_capacity = float(input("Please Enter Minimum Capacity (MW): "))
        manager.show_high_capacity_plants(min_capacity)

    elif choice == "13":
        technology = input("Please Enter Technology: ")
        manager.average_capacity_by_technology(technology)

    elif choice == "14":
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
