    // Get modal elements
    var modal = document.getElementById("instructionsModal");
    var btn = document.getElementById("instructionsButton");
    var span = document.getElementById("closeModal");

    // Open the modal when the button is clicked
    btn.onclick = function() {
        modal.style.display = "block";
    }

    // Close the modal when the "X" is clicked
    span.onclick = function() {
        modal.style.display = "none";
    }

    // Close the modal if the user clicks outside of it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }