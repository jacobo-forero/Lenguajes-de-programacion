<?php
$conn = new mysqli("localhost", "root", "", "");

if ($conn->connect_error) {
    die("Error de conexión: " . $conn->connect_error);
}

echo "Conexión exitosa";
$conn->close();
?>