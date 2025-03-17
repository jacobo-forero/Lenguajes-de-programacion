const { Client } = require('pg');

const client = new Client({
    host: 'localhost',
    user: 'postgres',
    password: '1234',
});

client.connect()
    .then(() => {
        console.log("Conexión exitosa");
    })
    .catch(err => {
        console.error("Error de conexión", err.stack);
    })
    .finally(() => {
        client.end();
    });