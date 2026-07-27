/*
ChatMe Frontend Controller

Connected to:
- server.py
- auth.py
- api_routes.py

*/


// =====================================
// CONFIG
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
// REGISTER
// =====================================


async function register(){


    const usernameInput =
    document.getElementById("username")
    .value.trim();



    const phone =
    document.getElementById("phone")
    .value.trim();



    const password =
    document.getElementById("password")
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
// LOGIN
// =====================================


async function login(){


    const phone =
    document.getElementById("phone")
    .value.trim();



    const password =
    document.getElementById("password")
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
            data.detail || "Login failed";


        }



    }

    catch(error){

        console.log(error);

    }


}









// =====================================
// OPEN CHAT
// =====================================


function openChat(){


    document
    .getElementById("auth-page")
    .classList.add("hidden");



    document
    .getElementById("chat-page")
    .classList.remove("hidden");



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

            "ChatMe WebSocket connected"

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



        switch(data.type){


            case "message":


                displayMessage({

                    sender:data.sender,

                    message:data.message

                });


            break;





            case "file":


                displayMessage({

                    sender:data.sender,

                    message:
                    "📎 "+data.filename

                });


            break;





            case "typing":


                document
                .getElementById("typing")
                .innerText =
                data.typing
                ?
                "Typing..."
                :
                "";

            break;





            case "offer":

                receiveOffer(data);

            break;



            case "answer":

                receiveAnswer(data);

            break;



            case "candidate":

                receiveCandidate(data);

            break;


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
// =====================================


function sendMessage(){



    const input =
    document
    .getElementById("message");



    const text =
    input.value.trim();



    if(!text || !selectedUser)
    return;



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
// =====================================


async function loadMessages(){


    selectedUser =
    document
    .getElementById("receiver")
    .value.trim();



    if(!selectedUser)
    return;



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
    document.getElementById("messages");



    const item =
    document.createElement("li");



    item.innerHTML =

    `
    <strong>
    ${data.sender}
    </strong>
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









// =====================================
// FILE UPLOAD
// =====================================


async function uploadFile(){


    const file =
    document
    .getElementById("file")
    .files[0];



    if(!file)
    return;



    const form =
    new FormData();



    form.append(

        "file",

        file

    );



    const response =
    await fetch(

        `${API_URL}/upload`,

        {

        method:"POST",

        body:form

        }

    );



    const data =
    await response.json();



    socket.send(

        JSON.stringify({

            type:"file",

            receiver:selectedUser,

            filename:data.filename,

            url:data.url,

            file_type:data.type


        })

    );


}









// =====================================
// EMOJI
// =====================================


function toggleEmoji(){


    document
    .getElementById("emoji-panel")
    .classList.toggle("hidden");


}



function addEmoji(emoji){


    document
    .getElementById("message")
    .value += emoji;


}









// =====================================
// DARK MODE
// =====================================


function toggleTheme(){


    document.body
    .classList.toggle("dark");


}









// =====================================
// AUDIO CALL
// =====================================


async function startAudioCall(){


    localStream =
    await navigator
    .mediaDevices
    .getUserMedia({

        audio:true

    });



    alert(
        "Audio call started"
    );


}









// =====================================
// VIDEO CALL
// =====================================


async function startVideoCall(){


    localStream =
    await navigator
    .mediaDevices
    .getUserMedia({

        video:true,

        audio:true

    });



    document
    .getElementById("localVideo")
    .srcObject =
    localStream;



    document
    .getElementById("call-area")
    .classList
    .remove("hidden");


}









// =====================================
// GROUP CALL
// =====================================


function createGroupCall(){


    document
    .getElementById("group-call-modal")
    .classList
    .remove("hidden");


}





function joinGroupCall(){


    const room =
    document
    .getElementById("roomId")
    .value;



    socket.send(

        JSON.stringify({

            type:"join_call",

            room:room


        })

    );


}





function closeModal(){


    document
    .getElementById("group-call-modal")
    .classList
    .add("hidden");


}









// =====================================
// WEBRTC PLACEHOLDERS
// =====================================


function receiveOffer(data){

    console.log(
        "Offer received",
        data
    );

}



function receiveAnswer(data){

    console.log(
        "Answer received",
        data
    );

}



function receiveCandidate(data){

    console.log(
        "Candidate received",
        data
    );

}









// =====================================
// START APPLICATION
// =====================================


window.onload=function(){


    if(username){


        openChat();


    }


};
