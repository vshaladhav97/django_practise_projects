var URL = "classproduct/";

$(document).ready(function() {
    $("#adding").click(function() {
        location.href = "/loan/";
    })
});

function getCourses() {
    $.getJSON(URL, {}, showCourses);
}

function getCourse() {
    $.getJSON(URL + $("#user_id").val())
        .done(showCourse) // on success - 200
        .fail(function() // on failure - 404
            {
                alert("Sorry! Course Not Found!");
            }
        );
}

function showCourse(course) {

    $("#user_id").val(course.user_id)
    $("#loan_amount").val(course.loan_amount)
    $("#loan_duration").val(course.loan_duration)
    $("#rate_of_interest").val(course.rate_of_interest)
    $("#interest_amount").val(course.interest_amount)
    $("#final_amount").val(course.final_amount)
}

function showCourses(courses) {


    $("#courserows").html("");
    $.each(courses,
        function(idx, course) {

            $("#courserows").append(
                "<tr><td>" +
                course.user_id +
                "</td><td>" +
                course.username +
                "</td><td>" +
                course.dob +
                "</td><td>" +
                course.mobile_no +
                "</td><td>" +
                course.pan_no +
                "</td><td>" +
                course.address +
                "</td><td>" +
                course.city +
                "</td><td>" +
                course.state +
                "</td><td>" +
                course.loan_amount +
                "</td><td>" +
                course.loan_duration +
                "</td><td>" +
                course.rate_of_interest +
                "</td><td>" +
                course.interest_amount +
                "</td><td>" +
                course.final_amount +
                "</td><td>" +
                course.loan_limit +
                "</td><td>" +
                course.due_date +
                "</td><td>" +
                course.transaction_date +
                "</td><td>" +
                course.amt_paid_by_the_bank +
                "</td><td>" +
                course.user_has_to_pay +
                "</td></tr>"
            );
        }
    );
    $("#courses").show();
    $("table_id").show();
    $(document).ready(function() {
        $('#table_id').DataTable({
            ajax: {
                url: URL,
                dataSrc: ""
            },
            columns: [{
                    data: 'user_id'
                }, {
                    data: 'username'
                }, {
                    data: 'dob'
                }, {
                    data: 'mobile_no'
                }, {
                    data: 'pan_no'
                }, {
                    data: 'address'
                }, {
                    data: 'city'
                }, {
                    data: 'state'
                }, {
                    data: 'loan_amount'
                }, {
                    data: 'loan_duration'
                }, {
                    data: 'rate_of_interest'
                }, {
                    data: 'interest_amount'
                }, {
                    data: 'final_amount'
                }, {
                    data: 'loan_limit'
                }, {
                    data: 'due_date'
                }, {
                    data: 'transaction_date'
                }, {
                    data: 'amt_paid_by_the_bank'
                }, {
                    data: 'user_has_to_pay'
                },



            ],


        });

    })
}
getCourses();