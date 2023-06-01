# ---------------------------------------------------------------------------- #
# Title: Assignment 07
# Description: Demonstrates how Pickling and Structured error handling work
# ChangeLog (Who,When,What):
# JUNYANLU,5.31,Modified code to complete assignment 07
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
import pickle
def save_data():
    try:
        intId = int(input("Enter an ID: "))
        strName = input("Enter a Name: ")
        lstCustomer = [intId, strName]

        with open("AppData.dat", "wb") as file:
            pickle.dump(lstCustomer, file)

        print("Data saved successfully.")

    except ValueError:
        print("Error: Invalid input. ID must be an integer.")
    except Exception as e:
        print("An error occurred:", str(e))
def load_data():
    try:
        with open("AppData.dat", "rb") as file:
            objFileData = pickle.load(file)

        print("Loaded data:", objFileData)

    except FileNotFoundError:
        print("Error: Data file not found.")
    except pickle.UnpicklingError:
        print("Error: Invalid data format.")
    except Exception as e:
        print("An error occurred:", str(e))


# Main program
while True:
    print("Menu:")
    print("1. Save data")
    print("2. Load data")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        save_data()
    elif choice == "2":
        load_data()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.\n")