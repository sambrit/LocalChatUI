document.getElementById("send-btn").addEventListener("click", async () => {
    const userInput = document.getElementById("user-input").value;
    const responseContainer = document.getElementById("response-container");

    // Check for empty input
    if (!userInput.trim()) {
        responseContainer.innerText = "Please enter a message.";
        return;
    }

    responseContainer.innerText = "Loading..."; // Display loading state

    try {
        const response = await fetch("http://127.0.0.1:8000/respond", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: userInput })
        });

        if (!response.ok) {
            throw new Error("Failed to fetch response from server.");
        }

        const data = await response.json();
        responseContainer.innerText = data.response;
    } catch (error) {
        console.error(error);
        responseContainer.innerText = "Error: Unable to connect to the AI server.";
    }
});
