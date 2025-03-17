<?php
$conn = pg_connect("host=localhost user=postgres password=1234");

if ($conn) {
    echo "Conexión exitosa";
} else {
    echo "Error de conexión";
}
?>