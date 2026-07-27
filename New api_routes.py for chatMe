"""
ChatMe API Routes

Features:
- User profiles
- Profile updates
- Private messages
- Message history
- File uploads
- Attachments
- Health check
"""


from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException
)


import os

import shutil



from database import (

    get_user_by_username,

    get_profile,

    update_profile_bio,

    save_message,

    save_attachment,

    get_user_messages,

    get_or_create_chat

)





router = APIRouter()





UPLOAD_FOLDER = "uploads"


os.makedirs(

    UPLOAD_FOLDER,

    exist_ok=True

)








# =====================================
# USER PROFILE
# =====================================


@router.get("/profile/{username}")
def profile(username:str):


    user = get_profile(

        username.strip()

    )



    if not user:


        raise HTTPException(

            status_code=404,

            detail="User not found"

        )



    return {


        "username":
        user["username"],


        "phone":
        user["phone"],


        "profile_picture":
        user.get("avatar"),


        "bio":
        user.get("bio","")

    }









# =====================================
# UPDATE BIO
# =====================================


@router.put("/profile/{username}/bio")
def update_bio(

    username:str,

    bio:str

):


    user=get_user_by_username(

        username.strip()

    )



    if not user:


        raise HTTPException(

            status_code=404,

            detail="User not found"

        )



    update_profile_bio(

        user["id"],

        bio

    )



    return {


        "status":"success",

        "message":"Bio updated"

    }









# =====================================
# SEND MESSAGE API
# (REST alternative)
# =====================================


@router.post("/message")
def send_message_api(

    sender:str,

    receiver:str,

    message:str

):


    sender_user = get_user_by_username(

        sender.strip()

    )



    receiver_user = get_user_by_username(

        receiver.strip()

    )



    if not sender_user or not receiver_user:


        raise HTTPException(

            status_code=404,

            detail="User not found"

        )



    chat_id = get_or_create_chat(

        sender_user["id"],

        receiver_user["id"]

    )



    message_id = save_message(

        chat_id,

        sender_user["id"],

        message

    )



    return {


        "status":"sent",

        "message_id":message_id

    }









# =====================================
# MESSAGE HISTORY
# =====================================


@router.get("/messages/{user1}/{user2}")
def message_history(

    user1:str,

    user2:str

):


    first=get_user_by_username(

        user1.strip()

    )



    second=get_user_by_username(

        user2.strip()

    )



    if not first or not second:


        return {


            "messages":[]

        }




    messages=get_user_messages(

        first["id"],

        second["id"]

    )



    result=[]



    for msg in messages:


        result.append({

            "sender":
            msg["username"],


            "message":
            msg["message"],


            "type":
            msg.get("message_type"),


            "timestamp":
            msg.get("timestamp")

        })



    return {


        "messages":result

    }









# =====================================
# FILE UPLOAD
# =====================================


@router.post("/attachment/upload")
async def upload_attachment(

    file:UploadFile = File(...)

):


    filepath=os.path.join(

        UPLOAD_FOLDER,

        file.filename

    )



    with open(

        filepath,

        "wb"

    ) as buffer:


        shutil.copyfileobj(

            file.file,

            buffer

        )



    return {


        "filename":
        file.filename,


        "filepath":
        filepath,


        "url":
        "/uploads/" + file.filename,


        "type":
        file.content_type

    }









# =====================================
# SAVE ATTACHMENT
# =====================================


@router.post("/attachment/save")
def save_file_attachment(

    message_id:int,

    filename:str,

    filepath:str,

    url:str,

    filetype:str,

    filesize:int=0

):


    attachment_id = save_attachment(

        message_id,

        filename,

        filepath,

        url,

        filetype,

        filesize

    )



    return {


        "status":"saved",

        "attachment_id":attachment_id

    }









# =====================================
# HEALTH CHECK
# =====================================


@router.get("/health")
def health():


    return {


        "app":"ChatMe",

        "status":"running"

    }
