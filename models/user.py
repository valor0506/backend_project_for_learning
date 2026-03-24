from os import name


class User:
    def __init__(self,user_id:str,name:str):
        self.user_id = user_id
        self.name = name

    def to_dict(self):
        return{
            "user_id":self.user_id,
            "name":self.name,
        }

    def __repr__(self):
        return f"User(user_id={self.user_id},name={self.name})"

# if __name__ == "__main__":
#     member = User("123","Suvan")
#     print(repr(member))
#     print(member.to_dict())
#     print(member.__repr__())