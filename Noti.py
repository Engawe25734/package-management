def send_push_notification(

    token,

    title,

    body

):


    try:

        from firebase_admin import messaging



        notification = messaging.Notification(

            title=title,

            body=body

        )



        message = messaging.Message(

            notification=notification,

            token=token

        )



        response = messaging.send(

            message

        )



        return response



    except Exception as e:


        print(

            "Firebase Error:",

            e

        )


        return False
