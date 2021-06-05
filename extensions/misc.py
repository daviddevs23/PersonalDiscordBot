# Allows us to grab the data from the token.txt file
def get_token(index):
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[index].strip()
