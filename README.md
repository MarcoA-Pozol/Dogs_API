# Dogs API

This small Dogs API is developed using FastAPI framework based on the RESTful architechture. 
This API is able to receive request of every most used HTTP methods like GET, PUT, POST, PATCH, DELET as principal CRUD operations to manage diferent endpoints to get and modify or add new data into it, and it can be connected to your diferent projects to get data, the creation or modifications endpoints are only available with permissions and authorization to avoid incorrect data that does not have any relation to the API purpose and to asure the data is securely and their usement too.

### Builded with
-FastAPI
-Python
-SQLAlchemy
-Pydantic
-Postgresql

## Features
-Allow to get dogs data using a GET request.
-Can be connected with your project to be used(the project language does not mean because it is made with RESTful architechture).

## Instalation
First: You have to move to your wished directory where you will clone the project repository (It is usual to do it in the Desktop).

'''bash
git clone https://github.com/MarcoA-Pozol/DogsAPI.git
cd DogsAPI.git
pip install -r requirements.txt'''

## Usage
Now you have installed all, it is time to run it using docker-compose file to turn on the containers by Docker and make it easily to use.

So in the same directory of the project at root type this in bash (you must have Docker desktop installed):

'''bash
docker-compose up -d'''

Once you had builded the containers, it is time to start to get data throught the endpoints for Dogs and Breeds, use whatever of these and try both them:
-localhost:10505/dogs (List all the dogs and return it as a Json)
-localhost:10505/dogs/<dog_id> (Retrieve a dog by their ID and if not exists so it raise an HTTP 404 error)
-localhost:10505/breeds (List all the breeds and return it as a Json)
-localhost:10505/breeds/<breed_id> (Retrieve a breed by their ID and if not exists so it raise an HTTP 404 error)

## Contributing 
For now our Team is very small, but feel free to use this API, we hope we could work together in the future. As another way you can contact us at hiitech@gmail.com

