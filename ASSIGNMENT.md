# Exercise: Creating a Django Project with JWT Auth and Middleware

## Objective: 

Your task is to set up a base Django project with a REST API using Django Rest Framework (DRF). The project will include a JWT based authentication system, and you will create a middleware to intercept all incoming requests. The middleware will validate the JWT tokens and, if valid, add the user object to the request object of the request.

## Specifications:

### Part 1: Django Project, DRF Setup & Django Admin

Set up a new Django project and app following Django's standard project structure.
1. Install and configure Django Rest Framework. 
2. Create a User model in Django if the default User model does not meet the requirements. Define the fields as per your preference, ensuring to include fields like username, password, first_name and last_name. 
3. Set up a Django admin view for the User model. Ensure you can create, read, update, and delete users via the admin interface. You do not need to create an endpoint to create a user.

### Part 2: JWT Based Authentication

1. Configure JWT based authentication in your Django project. For this, you can use libraries such as djangorestframework-simplejwt. 
2. Develop an API endpoint /api/user/login where users can pass in their username and password. If the user credentials are correct, return a JWT token in the response. This endpoint should not require a JWT token for access. 
3. Develop another API endpoint /api/user/profile that requires a valid JWT token for access. This route should return the user's first_name and last_name in the response if the JWT token is valid. 
4. Configure the JWT settings as per your preference.

### Part 3: Middleware for Incoming Requests

1. Create a custom middleware that intercepts all incoming requests. 
2. In this middleware, check the authorization header for a JWT token. If a token is present, validate the token. 
3. If the token is valid, extract the user information from the token, fetch the user object, and add it to the request object. 
4. If the token is invalid or not present, allow the request to process as usual.

### Part 4 (Optional - if time allows): User API and Serializer

1. Create a DRF Serializer for the User model. 
2. Create a UserViewSet and wire it up with the Django URL configuration.

## Deliverable:

You need to submit the following:

1. The entire Django project codebase pushed to a new public GitHub repository. 
2. Postman collection (or equivalent) for testing the API endpoints. Please include this in the repository. 
3. Share the link of the GitHub repository before the end of the call.

## Evaluation:

Your exercise will be evaluated on:
1. Code Quality: Your code should be clean, easy to read, and well-structured. This includes proper use of variables, classes, functions, and modules. 
2. Django and DRF Best Practices: You should follow the recommended best practices for Django and DRF projects. 
3. JWT Authentication: Your implementation of JWT authentication, including the login and profile API endpoints, will be evaluated. 
4. Middleware: Your implementation of the middleware for intercepting requests and modifying the request object will be evaluated. 
5. Django Admin: Your setup of the Django admin interface for the User model will be assessed. 
6. Use of GitHub: Your ability to create and manage a public GitHub repository and commit your changes to it will be evaluated.
