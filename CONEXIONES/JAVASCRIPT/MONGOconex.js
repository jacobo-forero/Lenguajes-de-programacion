const { MongoClient } = require('mongodb');

const uri = "mongodb://localhost:27017";
const client = new MongoClient(uri);

async function run() {
    try {
        await client.connect();
        console.log("Conexión exitosa");
    } catch (err) {
        console.error(err);
    } finally {
        await client.close();
    }
}

run().catch(console.dir);