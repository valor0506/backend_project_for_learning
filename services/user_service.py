from models.user import User
from storage.file_handler import FileHandler


class UserService:
    def __init__(self):
        self.file_handler = FileHandler("data/users.json")

    def create_user(self, user_id: str, name: str):
        users = self.file_handler.read_data()

        # Basic validation
        for user in users:
            if user["user_id"] == user_id:
                raise ValueError("User already exists")

        new_user = User(user_id, name)
        users.append(new_user.to_dict())

        self.file_handler.write_data(users)

        return new_user

    def get_all_users(self):
        return self.file_handler.read_data()