# Microservices_APZ
Continuing the tasks, 
Code for task 4 from apz, featuring a simple microservice

Additional tasks: using Kafka

facade_service.py - facade service for client-server communication. Receives get or post requests from the client and manages them (runs on localhost: 8080)

logging_service.py - stores all messages that are snt by facade_service via grpc protocol, sends back all the messages when receives a GET request (runs on localhost: 8082, 8083, 8084), stores data by running a hazelcast client

and storing everything in a distributed map

messages_service - currently not implemented, sends back "not implemented" message when receives a GET request (runs on localhost: 8081)

config_service.py - handles storing of ip addresses for instances of logging-services and messages-service

test_requests_get.sh - test file with bash code for sending a GET request

test_requests_post.sh - test file with bash code for sending POST request

config.txt - if you decide to change the ports in code for messages or logging service, modify this file too. Config example for stating the service addresses

Usage:

start kafka zookeper

[./images/5.jpg](./images/5.jpg)

start 2 kafka servers

[./images/6.jpg](./images/6.jpg)


[./images/7.jpg](./images/7.jpg)


create a kafka topic messages with 2 replication factor and 2 partiotions,

[./images/8.jpg](./images/8.jpg)


start hazelcast

run all 4 microservices in separate terminals

Here I tried posting some messages

[./images/1.jpg](./images/1.jpg)

here is the response, as you can see I encountered some errors so i had to shut messages service down and try again

[./images/2.jpg](./images/2.jpg)

But! When I fixed the code - i posted ten more messages and retrieved them. As you can see no info was lost

[./images/3.jpg](./images/3.jpg)

Here's what the messages service "consumed" from the kafka

[./images/4.jpg](./images/4.jpg)

Other instances of messages service retrieve only what hasn't been retrieved:


[./images/9.jpg](./images/9.jpg)









