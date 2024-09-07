//Module 3 - Python - UCD Professional Academy - Alan Maizon

document.addEventListener("DOMContentLoaded", function() {
    var timeLeft = 15;
    var timerInterval = setInterval(function() {
        timeLeft--;
        document.getElementById('timer').textContent = timeLeft;

        if (timeLeft <= 0) {
            clearInterval(timerInterval);
            document.getElementById('quiz-form').submit();
        }
    }, 1000);
});
