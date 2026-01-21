require('dotenv').config();
const express = require('express');
const axios = require('axios');
const app = express();

const port = process.env.FRONTEND_PORT || 3000;
const backendUrl = process.env.BACKEND_URL || 'http://backend:5001';

app.use(express.json());

app.get('/api/users', async (req, res) => {
  try {
    const response = await axios.get(`${backendUrl}/api/users`);
    res.json(response.data);
  } catch (err) {
    console.error(err);
    res.status(500).send('Erreur lors de la récupération des utilisateurs');
  }
});

app.get('/', (req, res) => {
  res.send(`
    <h1>Frontend</h1>
    <p>Backend URL: ${backendUrl}</p>
    <p><a href="/api/users" target="_blank">Tester le backend</a></p>
  `);
});

app.listen(port, () => console.log(`Frontend running on port ${port}`));
