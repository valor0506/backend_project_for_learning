from services.user_service import UserService


def main():
    user_service = UserService()

    while True:
        print("\n1. Create User")
        print("2. View Users")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            user_id = input("Enter User ID: ")
            name = input("Enter Name: ")

            try:
                user = user_service.create_user(user_id, name)
                print("User Created:", user)
            except ValueError as e:
                print("Error:", e)

        elif choice == "2":
            users = user_service.get_all_users()
            print("All Users:", users)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
