#Check for status code: 200:
def checkStatusCode(status):
    if status != 200:
        return False
    return True


# ---------------------------------------------------------------------------- #
if __name__ == "__main__":
    checkStatusCode()