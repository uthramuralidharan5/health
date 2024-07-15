// Add event listeners to login buttons
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("patientLoginButton").addEventListener("click", function() {
        // Show patient login modal
        $("#patientLoginModal").modal("show");
    });

    document.getElementById("adminLoginButton").addEventListener("click", function() {
        // Show admin login modal
        $("#adminLoginModal").modal("show");
    });

    document.getElementById("doctorLoginButton").addEventListener("click", function() {
        // Show doctor login modal
        $("#doctorLoginModal").modal("show");
    });
});