/* jshint esversion: 6 */
document.addEventListener('DOMContentLoaded', function () {
    var messagesContainer = document.getElementById('messages-container');

    if (messagesContainer) {
        messagesContainer.classList.add('fade-in');

        setTimeout(function () {
            messagesContainer.classList.remove('fade-in');
            messagesContainer.classList.add('fade-out');

            setTimeout(function () {
                messagesContainer.remove();
            }, 500); 
        }, 5000);
    }
});