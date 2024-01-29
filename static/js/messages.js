document.addEventListener('DOMContentLoaded', function () {
    var messagesContainer = document.getElementById('messages-container');

    if (messagesContainer) {
        // Add fade-in effect
        messagesContainer.classList.add('fade-in');

        // Add fade-out effect after 5 seconds (adjust as needed)
        setTimeout(function () {
            // Remove fade-in class and add fade-out class
            messagesContainer.classList.remove('fade-in');
            messagesContainer.classList.add('fade-out');

            // Wait for the fade-out animation to complete before removing the element
            setTimeout(function () {
                messagesContainer.remove();
            }, 500); // Adjust the duration to match your CSS transition duration
        }, 5000); // Adjust the delay before fade-out
    }
});