from recycle_system import RecycleSystem

def display_menu():
    print("\nRecycle Reward System")
    print("1. Add Item")
    print("2. View Total Reward")
    print("3. Reset System")
    print("4. Exit")

def main():
    system = RecycleSystem()
    
    while True:
        display_menu()
        choice = input("Choose an option: ")
        
        if choice == '1':
            item_type = input("Enter item type (A, B, or C): ").upper()
            print(system.add_item(item_type))
        elif choice == '2':
            print(f"Total reward: INR {system.get_total_reward():.2f}")
        elif choice == '3':
            print(system.reset_system())
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
