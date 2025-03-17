package main

import (
    "context"
    "fmt"
    "go.mongodb.org/mongo-driver/mongo"
    "go.mongodb.org/mongo-driver/mongo/options"
)

func main() {
    clientOptions := options.Client().ApplyURI("mongodb://localhost:27017")
    client, err := mongo.Connect(context.TODO(), clientOptions)
    if err != nil {
        panic(err)
    }

    err = client.Ping(context.TODO(), nil)
    if err != nil {
        panic(err)
    }

    fmt.Println("Conexión exitosa")
}