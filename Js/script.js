async function sendMessage() {
    const inputField = document.getElementById('userInput');
    const chatBox = document.getElementById('chatBox');
    const userMessage = inputField.value.trim();

    if (userMessage === '') return;

    // Display user's message
    const userMessageElement = document.createElement('div');
    userMessageElement.className = 'message user';
    userMessageElement.textContent = userMessage;
    chatBox.appendChild(userMessageElement);
    inputField.value = '';

    // Scroll to the bottom
    chatBox.scrollTop = chatBox.scrollHeight;

    // Fetch bot's response from the server
    const response = await fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: userMessage }),
    });

    const data = await response.json();

    // Display bot's message
    const botMessageElement = document.createElement('div');
    botMessageElement.className = 'message bot';
    botMessageElement.textContent = data.reply;
    chatBox.appendChild(botMessageElement);

    // Scroll to the bottom
    chatBox.scrollTop = chatBox.scrollHeight;
}