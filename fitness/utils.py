from .models import Register

# users = ["{name:}", {"email": 'email'}]
# Get all the data that comes via database.
db_data = Register.objects.all().values("email", "password", "contact", "name")


# users = []  # temp db


# -----------------------To check new user----------------
def userExist(user_data):
    email = user_data["email"]
    # contact = user_data["contact"]
    for user in db_data:
        print(user)
        if user["email"] == email:
            # print('matched user:', user)
            # print("greet already registered user.")
            return {"response": True, "users": user}

    # print("hello new user.")
    return {"response": False, "users": {}}


# -----------------------To register a new user----------------
def registerUser(user_data):
    # call userExist() To check that user is registered or not.
    checkUser = userExist(user_data)
    try:
        if checkUser["response"]:
            return {"statusCode": 503, "msg": "Already Registered"}
        else:
            user = Register(name=user_data['name'], contact=user_data["contact"], email=user_data["email"],
                            password=user_data["password"],
                            address=user_data["address"])
            # user.save()

            # users.append(user_data)  # (In memory concept)
            return {"statusCode": 200, "msg": "Successfully Registered"}
    except Exception as e:
        print("Error", e)


# -----------------------To Login a user----------------
def loginUser(user_data):
    password = user_data["password"]
    # call userExist() To check that user is registered or not.
    checkUser = userExist(user_data)
    print('THis is a login:', checkUser)
    if checkUser["response"]:
        if checkUser["users"]["password"] == password:
            return {"statusCode": 200, "msg": "Successfully Logged In."}
        else:
            return {"statusCode": 503, "msg": "Password Incorrect."}
    else:
        return {"statusCode": 503, "msg": "Not Registered Please Register First."}
