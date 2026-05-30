class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    @classmethod
    def valid_user(cls):
        return cls("tomsmith", "SuperSecretPassword!")

    def __repr__(self):
        return f"User(username={self.username}, password=***)"