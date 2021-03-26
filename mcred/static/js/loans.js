var URL = "classproduct/";

var loan_amount
var loan_duration
var reate_of_interest
var amount
var interest
var loan_duration_converted
var loan_limit = 100000
var dues
var loan_duration_dues
var bank_paid
var user_has_to_pay

$(document).ready(function() {
    $("#back-update").click(function() {
        location.href = "/show/";
    })
});

function calculate_interest() {
    loan_amount = $("#loan_amount").val();
    if (loan_amount > 100000) {
        alert("please enter valid amount");
        $("#loan_amount").val("");
    }
    loan_duration = ($("#loan_duration").val()) / 365;
    loan_duration_dues = $("#loan_duration").val()
    rate_of_interest = ($("#rate_of_interest").val());

    console.log(loan_duration_dues)
    amount = Math.round(loan_amount * (Math.pow((1 + (rate_of_interest / 100)), (loan_duration))));
    // amount = loan_amount * Math.pow(1 + (rate_of_interest / 1, 1 * loan_duration))
    // amount = loan_amount * Math.pow(1 + rate_of_interest / 1, 1 * loan_duration);
    interest = Math.round(amount - loan_amount)
    console.log(amount)
    console.log(interest)
    console.log(loan_amount)
    console.log(loan_duration)
    console.log(rate_of_interest)
    loan_duration_converted = Math.round(loan_duration)
    Date.prototype.addDays = function(days) {

        let date = new Date(this.valueOf());
        date.setDate(date.getDate() + days);
        return date;
    }

    function addDays(myDate, days) {
        return new Date(myDate.getTime() + days * 24 * 60 * 60 * 1000);
    }
    let date = new Date();
    var days = 15
    console.log(addDays(date, days))
    console.log(date.addDays(days));


    dues = addDays(date, loan_duration_dues)

    var month = dues.getMonth() + 1;
    var day = dues.getDate();

    var output = dues.getFullYear() + '-' +
        (('' + month).length < 2 ? '0' : '') + month + '-' +
        (('' + day).length < 2 ? '0' : '') + day;

    console.log(output);
    dues = output;


    $("#calculated_sum").text(interest)
    $("#calculated_amt").text(amount)
    $("#calculated_due_date").text(dues)

    console.log("after calculation:" + dues)
    bank_paid = loan_amount - interest
    user_has_to_pay = bank_paid + interest

    $("#bank_paid_money").text(bank_paid)
    $("#user_to_pay").text(user_has_to_pay)

}

function addCourse() {

    console.log(interest)
    loan_limit = loan_limit - loan_amount;

    $.ajax({
        "url": URL,
        "data": {

            "interest_amount": interest,
            "final_amount": amount,
            "loan_amount": loan_amount,
            "loan_duration": loan_duration_converted,
            "rate_of_interest": rate_of_interest,
            "loan_limit": loan_limit,
            "due_date": dues,
            "amt_paid_by_the_bank": bank_paid,
            "user_has_to_pay": user_has_to_pay,
            'csrfmiddlewaretoken': $(".add_loan").find('input[name=csrfmiddlewaretoken]').val()


        },
        "type": "post",
        "headers": {
            "X-CSRFToken": $(".add_loan").find('input[name=csrfmiddlewaretoken]').val()
        },

        "success": add_success,
        "error": add_error

    }); // ajax()
    function add_success() {
        alert("Added loan details Successfully");
    }

    function add_error() {
        alert("Could not add loan details!");
    }

}