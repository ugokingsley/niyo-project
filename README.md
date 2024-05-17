# niyo-project
Project Description

**1. About Project**

   To demonstrate CRUD operations, the project consists of an Authentication system
   and a Books Inventory Application with neccessary validations and user Authorization.

**2. Stack**
   - Python (Django Framework)
   - Docker / Docker Compose
   - RabbitMQ (Event Streaming)
   - PostGreSQL
     
**3. Installation Instructions**
   - Download Docker here: https://www.docker.com/products/docker-desktop
   - clone this repo and in the project root go to your terminal and run this command:
     **docker-compose build** and  **docker-compose up -d** to run the container and services
   - Create a .env file in the project root and provide the necessary credential information
     as seen in env.example file (DB credentials and Cloudampq credentials from **https://www.cloudamqp.com/**)
   - Import Niyo_Group.postman_collection.json into POSTMAN to test APIs. View POSTMAN example files to
     see success and failure responses
