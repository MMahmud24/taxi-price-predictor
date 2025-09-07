const express = require("express");
const { spawn } = require("child_process");
const cors = require("cors");

const app = express();
app.use(express.json());
app.use(cors());

app.post("/predict", (req, res) => {
  const { pickup, dropoff } = req.body;

  const python = spawn("python3", ["backend/predict.py", JSON.stringify(pickup), JSON.stringify(dropoff)]);

  python.stdout.on("data", (data) => {
    const result = JSON.parse(data.toString());
    res.json(result);
  });

  python.stderr.on("data", (data) => {
    console.error(`error: ${data}`);
    res.status(500).json({ error: "script failed" });
  });``
});

app.listen(5000, () => console.log("Server running on http://localhost:5000"));
