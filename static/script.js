const chatMessages = document.querySelector('.chat-messages');
const messageInput = document.getElementById('message-input');
const sendBtn = document.getElementById('send-btn');

// Dummy data for demo
const messages = [
    { sender: 'User1', content: 'Hello, everyone!' },
];


messages.forEach(message => {
    const messageElement = createMessageElement(message.sender, message.content);
    chatMessages.appendChild(messageElement);
});

// Send message

/*
sendBtn.addEventListener('click', () => {
    const messageContent = messageInput.value.trim();
    if (messageContent) {
        const newMessage = { sender: 'You', content: messageContent };
        const messageElement = createMessageElement(newMessage.sender, newMessage.content);
        chatMessages.appendChild(messageElement);
        messageInput.value = '';
        // Here, you would typically send the message to the server
        // and handle the response from other users
    }
});
*/
$(document).ready(function() {
    $("#send-btn").click(function() {
      var messageContent = $("#message-input").val();
      $.post("/post-message", { message: messageContent }, function(data) {
        console.log("Message posted successfully!");
      });
    });
  });

// Create message element
function createMessageElement(sender, content) {
    const messageElement = document.createElement('div');
    messageElement.classList.add('chat-message');
    messageElement.innerHTML = `<strong>${sender}:</strong> ${content}`;
    return messageElement;
}