# AirDNA Take-home Interview Exercise -- OTA
As part of the interview process at AirDNA, we would like 
you to complete the following exercise. We’ll review your 
work with you during a follow-up interview session.

## Task
Build a simple Python service that simulates the back end 
of an online travel booking site (known as an "OTA"). We’re 
providing the basic application structure for you, and asking 
you to add the API endpoints and anything else you think is 
necessary to address the requirements and objectives. 

## Requirements
* Add an HTTP endpoint that searches for available properties
  * Request
    * Accepts a start date and a number of nights as parameters
    * Accepts a mock access token, which simulates authorization of the request
    * A valid access token is a UUID
  * Response
    * On success
      * Returns HTTP 200
      * Returns a list of property IDs and descriptions, for properties that 
        are available over the requested time period
      * A property is "available" when it has no reservations that intersect 
        the requested date range of [start date, start date + number of nights]
    * An unauthorized request generates an HTTP 401 response
    * If no properties are available for the given date range, this returns HTTP 404
* Add an HTTP endpoint to make a reservation
  * Request
    * Accepts a property ID, start date and number of nights as parameters
    * Accepts a mock access token, which simulates authorization of the request
    * A valid token is a UUID
  * Response
    * On success
      * Returns HTTP 200
      * Returns a reservation ID
    * An unauthorized request generates an HTTP 401 response
    * An invalid request returns HTTP 400
* Reserverations need IDs
  * Make sure each existing reservation, and each new reservation is assigned a unique ID
  * The system needs to be able to support hundreds of millions of reservations
* Supports 100 simultaneous requests
* Assume this will eventually be run on a kubernetes cluster, and needs to 
  be horizontally scalable 

## Delivery
We will provide a github or gitlab repository for you to contribute code to.
* Clone the repo
* Create a branch
* Make your commits to the branch
* When you’re ready to submit, push your commit(s) and raise a pull request (github) or merge request (gitlab)

## Our Objectives
We’re trying to assess how you approach the solution to a real-world problem:
* Can you translate requirements into functional code?
* Do you produce readable, well organized and extensible code?
* Are you familiar with Python, Flask, Postgres and APIs?
* Can your code be easily tested?
* Is your code performant?
* Can the service scale well?
* How are you handling observability?
* Do you handle errors gracefully?

## If You Have Questions
This is meant to simulate a real project that you would be working on at
AirDNA. If you have any questions, please do not hesitate to ask them.
Furthermore, if you feel something is missing from the requirements, go
ahead and add it in and document what you did (code comments are fine).

## Running the Service
The service will be delivered via Docker. Running the following command will 
start a PostgreSQL database, load sample data into it and start the Python 
service. 

```
docker-compose up
```

You can connect to the database using the default user `postgres` with no password.

If you change data in your database in a significant way ```rm -rf ./pg_data && docker-compose up```


Note that the service container will hot-reload changes as you make them.


