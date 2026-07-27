"""
ChatMe Authentication System

Features:
- Password hashing
- User registration
- User login
- JWT token creation
- JWT token verification
"""


from datetime import datetime, timedelta, timezone


from passlib.context import CryptContext


from jose import jwt, JWTError



from database import (

    create_user,

    get_user_by_phone

)





# =====================================
# SECURITY CONFIGURATION
# =====================================


# Replace this before production deployment
SECRET_KEY = "CHANGE_THIS_TO_A_LONG_RANDOM_SECRET_KEY"


ALGORITHM = "HS256"


TOKEN_EXPIRE_MINUTES = 60





# Password hashing

password_context = CryptContext(

    schemes=["bcrypt"],

    deprecated="auto"

)









# =====================================
# PASSWORD FUNCTIONS
# =====================================


def hash_password(password:str):


    return password_context.hash(

        password

    )







def verify_password(

    plain_password:str,

    hashed_password:str

):


    return password_context.verify(

        plain_password,

        hashed_password

    )









# =====================================
# REGISTER USER
# =====================================


def register_user(

    username:str,

    phone:str,

    password:str

):


    existing_user = get_user_by_phone(

        phone

    )



    if existing_user:


        return {


            "status":"error",


            "message":
            "Phone number already registered"


        }






    password_hash = hash_password(

        password

    )



    user_id = create_user(

        username,

        phone,

        password_hash

    )



    return {


        "status":"success",


        "message":
        "Account created successfully",


        "user_id":
        user_id


    }









# =====================================
# LOGIN USER
# =====================================


def authenticate_user(

    phone:str,

    password:str

):


    user = get_user_by_phone(

        phone

    )



    if not user:


        return None





    password_correct = verify_password(

        password,

        user["password_hash"]

    )



    if not password_correct:


        return None





    return user











# =====================================
# CREATE JWT TOKEN
# =====================================


def create_access_token(

    user_id:int,

    username:str

):


    expire = datetime.now(

        timezone.utc

    ) + timedelta(

        minutes=TOKEN_EXPIRE_MINUTES

    )



    payload = {


        "user_id":
        user_id,


        "username":
        username,


        "exp":
        expire


    }



    token = jwt.encode(

        payload,

        SECRET_KEY,

        algorithm=ALGORITHM

    )



    return token










# =====================================
# VERIFY JWT TOKEN
# =====================================


def verify_token(

    token:str

):


    try:


        payload = jwt.decode(

            token,

            SECRET_KEY,

            algorithms=[ALGORITHM]

        )


        return payload



    except JWTError:


        return None











# =====================================
# TEST AUTHENTICATION
# =====================================


if __name__=="__main__":


    from database import initialize_database



    initialize_database()



    print(

        "Creating test user..."

    )



    result = register_user(

        "Alex",

        "5551234567",

        "password123"

    )



    print(result)



    print(

        "Testing login..."

    )



    user = authenticate_user(

        "5551234567",

        "password123"

    )



    if user:


        token=create_access_token(

            user["id"],

            user["username"]

        )



        print(

            "Login successful"

        )


        print(token)



    else:


        print(

            "Login failed"

        )
