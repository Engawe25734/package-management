"""
ChatMe Backend Server

Features:
- User registration
- User login
- JWT authentication
- REST API routes
- WebSocket realtime chat
- File uploads
- WebRTC signaling
- Group calls
"""


from fastapi import (
    FastAPI,
    WebSocket,
    WebSocketDisconnect,
    UploadFile,
    File,
    HTTPException,
    Request
)


from fastapi.staticfiles import StaticFiles

from fastapi.templating import Jinja2Templates


from fastapi.middleware.cors import CORSMiddleware


import json


from database import (
    initialize_database,
    save_message,
    get_user_by_username,
    get_or_create_chat
)


from auth import (
    register_user,
    authenticate_user,
    create_access_token
)


from models import (
    RegisterRequest,
    LoginRequest
)


from websocket_manager import manager


from api_routes import router


from file_manager import (
    initialize_storage,
    validate_file,
    save_file
)





# =====================================
# CREATE APP
# =====================================


app = FastAPI(

    title="ChatMe API",

    version="1.0"

)





# =====================================
# CORS
# =====================================


app.add_middleware(

    CORSMiddleware,

    allow_origins=["*"],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"]

)





# =====================================
# DATABASE
# =====================================


initialize_database()





# =====================================
# ROUTES
# =====================================


app.include_router(router)





# =====================================
# STATIC FILES
# =====================================


templates = Jinja2Templates(

    directory="templates"

)



app.mount(

    "/static",

    StaticFiles(directory="static"),

    name="static"

)





# =====================================
# FILE STORAGE
# =====================================


initialize_storage()



app.mount(

    "/uploads",

    StaticFiles(directory="uploads"),

    name="uploads"

)







# =====================================
# HOME PAGE
# =====================================


@app.get("/")
async def home(request: Request):


    return templates.TemplateResponse(

        "index.html",

        {

            "request": request

        }

    )








# =====================================
# REGISTER
# =====================================


@app.post("/register")
def register(

    user:RegisterRequest

):


    return register_user(

        user.username.strip(),

        user.phone.strip(),

        user.password

    )








# =====================================
# LOGIN
# =====================================


@app.post("/login")
def login(

    user:LoginRequest

):


    account = authenticate_user(

        user.phone.strip(),

        user.password

    )



    if not account:


        raise HTTPException(

            status_code=401,

            detail="Invalid phone number or password"

        )



    token = create_access_token(

        account["id"],

        account["username"]

    )



    return {


        "access_token": token,


        "token_type":"bearer",


        "username":account["username"]

    }









# =====================================
# FILE UPLOAD
# =====================================


@app.post("/upload")
async def upload_file(

    file:UploadFile = File(...)

):


    content = await file.read()



    valid, message = validate_file(

        file.filename,

        file.content_type,

        len(content)

    )



    if not valid:


        raise HTTPException(

            status_code=400,

            detail=message

        )



    result = save_file(

        content,

        file.filename

    )



    return {


        "filename":file.filename,


        "url":"/uploads/" + result["stored_name"],


        "type":file.content_type

    }









# =====================================
# ONLINE USERS
# =====================================


@app.get("/online")
def online_users():


    return {


        "users":manager.online_users()

    }









# =====================================
# WEBSOCKET CHAT SERVER
# =====================================


@app.websocket("/ws/{username}")
async def websocket_endpoint(

    websocket:WebSocket,

    username:str

):


    username=username.strip()



    await manager.connect(

        username,

        websocket

    )



    try:


        while True:


            raw = await websocket.receive_text()



            data=json.loads(raw)



            msg_type=data.get("type")





            # -----------------------------
            # PRIVATE MESSAGE
            # -----------------------------


            if msg_type=="message":


                receiver=data["receiver"]

                text=data["message"]



                sender_user = get_user_by_username(

                    username

                )


                receiver_user = get_user_by_username(

                    receiver

                )



                message_id=None



                if sender_user and receiver_user:


                    chat_id=get_or_create_chat(

                        sender_user["id"],

                        receiver_user["id"]

                    )



                    message_id=save_message(

                        chat_id,

                        sender_user["id"],

                        text

                    )





                await manager.send_private_message(

                    receiver,

                    {

                    "type":"message",

                    "sender":username,

                    "message":text,

                    "message_id":message_id

                    }

                )







            # -----------------------------
            # FILE MESSAGE
            # -----------------------------


            elif msg_type=="file":


                await manager.send_private_message(

                    data["receiver"],

                    data

                )







            # -----------------------------
            # TYPING
            # -----------------------------


            elif msg_type=="typing":


                await manager.send_typing_status(

                    data["receiver"],

                    username,

                    data["typing"]

                )







            # -----------------------------
            # WEBRTC PRIVATE SIGNAL
            # -----------------------------


            elif msg_type in [

                "offer",

                "answer",

                "candidate"

            ]:


                await manager.send_private_message(

                    data["receiver"],

                    {

                    **data,

                    "sender":username

                    }

                )







            # -----------------------------
            # CREATE GROUP CALL
            # -----------------------------


            elif msg_type=="create_call":


                await manager.join_call_room(

                    data["room"],

                    username

                )


                await websocket.send_text(

                    json.dumps({

                    "type":"call_created",

                    "room":data["room"]

                    })

                )







            # -----------------------------
            # JOIN GROUP CALL
            # -----------------------------


            elif msg_type=="join_call":


                await manager.join_call_room(

                    data["room"],

                    username

                )


                await manager.broadcast_call_signal(

                    data["room"],

                    username,

                    {

                    "type":"user_joined",

                    "user":username

                    }

                )







            # -----------------------------
            # GROUP WEBRTC
            # -----------------------------


            elif msg_type in [

                "group_offer",

                "group_answer",

                "group_candidate"

            ]:


                await manager.broadcast_call_signal(

                    data["room"],

                    username,

                    data

                )







            # -----------------------------
            # END CALL
            # -----------------------------


            elif msg_type=="end_call":


                await manager.broadcast_call_signal(

                    data["room"],

                    username,

                    data

                )





    except WebSocketDisconnect:


        await manager.disconnect(

            username,

            websocket

        )








# =====================================
# START SERVER
# =====================================


if __name__=="__main__":


    import uvicorn



    uvicorn.run(

        "server:app",

        host="0.0.0.0",

        port=8000,

        reload=True

    )
