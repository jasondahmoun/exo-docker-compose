require('dotenv').config();
const express = require('express');
const { Pool } = require('pg');
const axios = require('axios');
const { SocksProxyAgent } = require('socks-proxy-agent');

const app = express();
const port = process.env.BACKEND_PORT;

const pool = new Pool({
  user: process.env.DB_USER,
  host: process.env.DB_HOST, 
  database: process.env.DB_NAME,
  password: process.env.DB_PASSWORD,
  port: Number(process.env.DB_PORT)
});


const torAgent = new SocksProxyAgent(`socks5h://${process.env.TOR_HOST}:${process.env.TOR_PORT}`);
const torAxios = axios.create({
  httpAgent: torAgent,
  httpsAgent: torAgent,
  timeout: 20000
});


app.get('/api/db', async (req, res) => {
  const result = await pool.query('SELECT NOW()');
  res.json({ status: 'ok', time: result.rows[0].now });
});

app.get('/api/users', async (req, res) => {
  try {
    const response = await torAxios.get('https://randomuser.me/api/?results=5');
    const users = response.data.results.map(u => ({
      name: `${u.name.first} ${u.name.last}`,
      picture: u.picture.medium
    }));
    res.json(users);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.get('/api/tor-ip', async (req, res) => {
  const response = await torAxios.get('https://check.torproject.org/api/ip');
  res.json(response.data);
});

app.listen(port, () => console.log(`Backend running on port ${port}`));
