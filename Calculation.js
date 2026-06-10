/*
    Name: Irving Peress
    Date: June 10, 2026

    Purpose:
    Validate user input and calculate
    tip amount, total bill, and
    per-person cost.
*/

const billAmount = document.getElementById("billAmount");
const tipPercentage = document.getElementById("tipPercentage");
const peopleCount = document.getElementById("peopleCount");

tipPercentage.addEventListener("input", function () {

    const tip = Number(tipPercentage.value);

    if (tip < 0 || tip > 100) {
        document.getElementById("tipError").textContent =
            "Tip must be a number from 0 to 100.";
    } else {
        document.getElementById("tipError").textContent = "";
    }
});

function calculateBill() {

    let valid = true;

    document.getElementById("billError").textContent = "";
    document.getElementById("tipError").textContent = "";
    document.getElementById("peopleError").textContent = "";

    const bill = parseFloat(billAmount.value);
    const tip = parseFloat(tipPercentage.value);
    const people = parseInt(peopleCount.value);

    if (isNaN(bill) || bill < 0) {
        document.getElementById("billError").textContent =
            "Enter a bill amount ≥ 0.";
        valid = false;
    }

    if (isNaN(tip) || tip < 0 || tip > 100) {
        document.getElementById("tipError").textContent =
            "Tip must be a number from 0 to 100.";
        valid = false;
    }

    if (isNaN(people) || people < 1) {
        document.getElementById("peopleError").textContent =
            "People count must be a whole number ≥ 1.";
        valid = false;
    }

    if (!valid) {
        document.getElementById("summary").style.display = "none";
        return;
    }

    const tipAmount = bill * (tip / 100);
    const total = bill + tipAmount;
    const perPerson = total / people;

    document.getElementById("tipResult").textContent =
        "$" + tipAmount.toFixed(2);

    document.getElementById("totalResult").textContent =
        "$" + total.toFixed(2);

    document.getElementById("personResult").textContent =
        "$" + perPerson.toFixed(2) + " (" + people + " people)";

    document.getElementById("summary").style.display = "block";
}
