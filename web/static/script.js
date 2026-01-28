function sendCommand(route, statusText) {
    document.getElementById('status-bar').innerText = "Status: " + statusText;

    fetch(route)
        .then(response => response.json())
        .then(data => {
            for (const [id, state] of Object.entries(data)) {
                const led = document.getElementById(id);
                if (led) {
                    if (state) led.classList.add('on');
                    else led.classList.remove('on');
                }
            }
        })
        .catch(error => console.error("Error:", error));
}
