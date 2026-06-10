/*
Name: Elvis ngawe
Date: June 10, 2026

Purpose:
This script validates all form fields using
jQuery and validator.js. Live feedback is
provided while the user types.
*/

$(document).ready(function(){

    function validateName(){

        let name = $("#fullname").val().trim();

        if(name.length < 2){
            $("#nameError").text("Enter a valid full name.");
            return false;
        }

        $("#nameError").text("");
        return true;
    }

    function validateEmail(){

        let email = $("#email").val().trim();

        if(
            !validator.isEmail(email) ||
            !(email.endsWith(".com") || email.endsWith(".edu"))
        ){
            $("#emailError").text("Enter a valid email address ending in .com or .edu.");
            return false;
        }

        $("#emailError").text("");
        return true;
    }

    function validatePassword(){

        let password = $("#password").val();

        let pattern =
        /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$/;

        if(!pattern.test(password)){

            $("#passwordError").text(
            "Password must be 8+ chars with upper, lower, and number."
            );

            return false;
        }

        $("#passwordError").text("");
        return true;
    }

    function validateWebsite(){

        let website = $("#website").val().trim();

        if(
            !validator.isURL(
                website,
                {
                    protocols:['http','https'],
                    require_protocol:true
                }
            )
        ){

            $("#websiteError").text(
            "Enter a valid URL starting with http:// or https://"
            );

            return false;
        }

        $("#websiteError").text("");
        return true;
    }

    function validateAge(){

        let age = parseInt($("#age").val());

        if(isNaN(age) || age <= 0){

            $("#ageError").text(
            "Enter a valid age (must be 1 or higher)."
            );

            return false;
        }

        $("#ageError").text("");
        return true;
    }

    $("#fullname").on("keyup blur", validateName);
    $("#email").on("keyup blur", validateEmail);
    $("#password").on("keyup blur", validatePassword);
    $("#website").on("keyup blur", validateWebsite);
    $("#age").on("keyup blur", validateAge);

    $("#signupForm").submit(function(event){

        event.preventDefault();

        let valid =
            validateName() &&
            validateEmail() &&
            validatePassword() &&
            validateWebsite() &&
            validateAge();

        if(valid){

            alert("Form submitted successfully!");

            $("#signupForm")[0].reset();

            $(".error").text("");
        }
    });

});
