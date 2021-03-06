class Library:
    def __init__(self):
        self.user_records = []
        self.books_available = {}
        self.rented_books = {}

    def add_user(self, user):
        if user in self.user_records:
            return f"User with id = {user.user_id} already registered in the library!"
        self.user_records.append(user)

    def remove_user(self, user):
        if user not in self.user_records:
            return "We could not find such user to remove!"
        self.user_records.remove(user)
        # TODO

    def change_username(self, user_id, new_username):
        try:
            is_in = [u for u in User if u.user_id == user_id][0]
            if is_in.username == new_username:
                return f"Please check again the provided username - " \
                       f"it should be different than the username used so far!"
            is_in.username = new_username
            return f"Username successfully changed to: {new_username} for userid: {is_in.user_id}"
        except IndexError:
            return f"There is no user with id = {user_id}!"
