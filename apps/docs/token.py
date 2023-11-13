import uuid

class TokenGenerator:
    @staticmethod
    def generate_token():
        return str(uuid.uuid4())