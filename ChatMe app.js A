/*
ChatMe app.js

Connected with:
- server.py
- auth.py
- api_routes.py

Features:
- Authentication
- JWT session
- WebSocket messaging
- Message history
*/


// =====================================
// CONFIGURATION
// =====================================


const API_URL = "http://localhost:8000";

const WS_URL = "ws://localhost:8000";



let username =
localStorage.getItem("username") || "";


let token =
localStorage.getItem("access_token") || "";


let socket = null;


let selectedUser = "";


let localStream = null;









// =====================================
// REGISTER USER
// Matches server.py /register
// =====================================


async function register(){


    const usernameInput =
    document
    .getElementById("username")
    .value
    .trim();



    const phone =
    document
    .getElementById("phone")
    .value
    .trim();



    const password =
    document
    .getElementById("password")
    .value;



    try{


        const response =
        await fetch(

            `${API_URL}/register`,

            {

            method:"POST",

            headers:{

                "Content-Type":
                "application/json"

            },


            body:JSON.stringify({

                username:usernameInput,

                phone:phone,

                password:password

            })

            }

        );



        const data =
        await response.json();



        document
        .getElementById("authMessage")
        .innerText =
        data.message;



    }

    catch(error){

        console.log(error);

    }


}









// =====================================
// LOGIN USER
// Matches server.py /login
// =====================================


async function login(){


    const phone =
    document
    .getElementById("phone")
    .value
    .trim();



    const password =
    document
    .getElementById("password")
    .value;



    try{


        const response =
        await fetch(

            `${API_URL}/login`,

            {

            method:"POST",

            headers:{

                "Content-Type":
                "application/json"

            },


            body:JSON.stringify({

                phone:phone,

                password:password

            })


            }

        );



        const data =
        await response.json();




        if(response.ok){



            username =
            data.username;



            token =
            data.access_token;




            localStorage.setItem(

                "username",

                username

            );



            localStorage.setItem(

                "access_token",

                token

            );



            openChat();



        }

        else{


            document
            .getElementById("authMessage")
            .innerText =
            data.detail ||
            "Login failed";


        }



    }

    catch(error){

        console.log(error);

    }


}









// =====================================
// OPEN CHAT APPLICATION
// =====================================


function openChat(){


    document
    .getElementById("auth-page")
    .classList
    .add("hidden");



    document
    .getElementById("chat-page")
    .classList
    .remove("hidden");



    document
    .getElementById("status")
    .innerText =
    "Connecting...";



    connectSocket();


}









// =====================================
// WEBSOCKET CONNECTION
// Matches server.py
// /ws/{username}
// =====================================


function connectSocket(){



    socket =
    new WebSocket(

        `${WS_URL}/ws/${username}`

    );





    socket.onopen=function(){


        console.log(
            "ChatMe connected"
        );



        document
        .getElementById("status")
        .innerText =
        "Online";


    };






    socket.onmessage=function(event){


        const data =
        JSON.parse(event.data);



        console.log(data);




        if(data.type==="message"){


            displayMessage({

                sender:data.sender,

                message:data.message

            });


        }




        else if(data.type==="file"){


            displayMessage({

                sender:data.sender,

                message:
                "📎 " + data.filename

            });


        }




        else if(data.type==="typing"){


            document
            .getElementById("typing")
            .innerText =
            data.typing
            ?
            "Typing..."
            :
            "";

        }




        else if(data.type==="offer"){


            receiveOffer(data);


        }




        else if(data.type==="answer"){


            receiveAnswer(data);


        }




        else if(data.type==="candidate"){


            receiveCandidate(data);


        }



    };






    socket.onclose=function(){


        document
        .getElementById("status")
        .innerText =
        "Offline";


    };


}









// =====================================
// SEND MESSAGE
// WebSocket message
// =====================================


function sendMessage(){


    const input =
    document
    .getElementById("message");



    const text =
    input.value.trim();




    if(!text || !selectedUser){

        return;

    }




    socket.send(

        JSON.stringify({

            type:"message",

            receiver:selectedUser,

            message:text


        })

    );




    displayMessage({

        sender:username,

        message:text

    });



    input.value="";


}









// =====================================
// LOAD MESSAGE HISTORY
// API: /messages/user1/user2
// =====================================


async function loadMessages(){


    selectedUser =
    document
    .getElementById("receiver")
    .value
    .trim();




    if(!selectedUser){

        return;

    }




    document
    .getElementById("chatUser")
    .innerText =
    selectedUser;





    const response =
    await fetch(

        `${API_URL}/messages/${username}/${selectedUser}`

    );




    const data =
    await response.json();




    const list =
    document
    .getElementById("messages");



    list.innerHTML="";




    data.messages.forEach(msg=>{


        displayMessage({

            sender:msg.sender,

            message:msg.message


        });


    });



}









function displayMessage(data){


    const list =
    document
    .getElementById("messages");



    const item =
    document
    .createElement("li");



    item.innerHTML =

    `
    <strong>${data.sender}</strong>
    :
    ${data.message}
    `;



    list.appendChild(item);



}









function enterSend(event){


    if(event.key==="Enter"){

        sendMessage();

    }


}
