
def get_token(index):
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[index].strip()
