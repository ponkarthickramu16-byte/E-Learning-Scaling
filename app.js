// 1. Express module-ai import panrom
const express = require('express'); 
const app = express();
const port = 3000;

// 2. Express Routing (Idhudhaan Express-oda main velai)
app.get('/', (req, res) => {
    res.send('<h1>E-Learning Scaling Monitor (Node.js + Express)</h1>');
});

// 3. Status path - Scaling data-vukku
app.get('/status', (req, res) => {
    let load = Math.floor(Math.random() * 100);
    res.json({
        "server_status": "Running",
        "current_load": load + "%",
        "action": load > 75 ? "Scaling Up" : "Stable"
    });
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});