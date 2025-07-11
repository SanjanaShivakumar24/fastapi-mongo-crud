FastAPI MongoDB CRUD Application – Local Setup Guide

Project Struture

fastapi-mongo-crud/
├── app/
│   ├── main.py             # Entry point
│   ├── models.py           # Pydantic models
│   ├── crud.py             # CRUD operations
│   └── database.py         # MongoDB connection
│
├── .env                    # Environment variables
├── requirements.txt        # Python dependencies
└── README.md               # Documentation (this file)

## Prerequisites

Installations:
   -    Python 3.10+
   -  pip (Python package manager)
   - [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register) account
   -  Git 

 
  Steps :
 1. Clone the Project
>     git clone https://github.com/your-username/fastapi-mongo-crud.git 
>     cd fastapi-mongo-crud

2. Create & Activate Virtual Environment

> python -m venv venv\Scripts\activate

3. Install Dependencies

> pip install -r requirements.txt

4. Create `.env` File
We can use either MongoDB Atlas (cloud) or local MongoDB.
Option A: MongoDB Atlas (Cloud)

> MONGO_URI=mongodb+srv://sanjanashivakumar:k9dweZUoYmMAazIx@cluster0.d0cecdx.mongodb.net/sample_mflix?retryWrites=true&w=majority&authSource=admin

Initially, I attempted to use MongoDB Atlas by setting the URI as shown above. However, due to authentication or connection issues (e.g., "bad auth"), I chose to use a local MongoDB instance for smoother development.

Option B: MongoDB (Local)
If Atlas doesn't connect, we can use our local MongoDB:

> MONGO_URI=mongodb://localhost:27017

5. Database Configuration
Our code should use the `.env` variable like so:

> from  motor.motor_asyncio  import  AsyncIOMotorClient from  dotenv 
> import  load_dotenv import  os load_dotenv() MONGO_URI  = 
> os.getenv("MONGO_URL") client  =  AsyncIOMotorClient(MONGO_URI) db  = 
> client["mydatabase"] collection  =  db["users"] # or items, based on
> your use case
>
6. Run the Application
> uvicorn app.main:app --reload

-   Visit Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
  
  ## API Endpoints

All endpoints are prefixed with the root URL:  
`http://localhost:8000`

## API Endpoints (Point-wise Format)

Base URL: `http://localhost:8000`

1.  **GET /**
    
    -   Description: Root endpoint – returns a welcome message or status check.
        
2.  **POST /user**
    
    -   Description: Adds a new user to the MongoDB database.
   

>  - {   "name": "Alice",   "email": "alice@example.com" }

3.  **GET /users**
    
    -   Description: Retrieves a list of all users stored in the database.
        
4.    **GET /user/{name}**
    
    -   Description: Retrieves a specific user by their name.
        
    -   Example: `/user/Alice`
        
5.   **PUT /user/{name}**
    
    -   Description: Updates the details of an existing user by their name.
        
    -   Example JSON body:
 

>    - {   "email": "newalice@example.com" }

6.    **DELETE /user/{name}**

-   Description: Deletes a user by their name.
    
-   Example: `/user/Alice`

