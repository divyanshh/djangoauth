# Creating a Django Project with JWT Auth and Middleware

## Objective: 

The task is to set up a base Django project with a REST API using Django Rest Framework (DRF). The project will include a JWT based authentication system, and you will create a middleware to intercept all incoming requests. The middleware will validate the JWT tokens and, if valid, add the user object to the request object of the request.

## Solution:

### Part 1: Django Project, DRF Setup & Django Admin

1. Used the default User model from Django, as it supports all the required fields (In case we do want to add some fields, we can override the django auth model, extend AbstractUser and add new fields and add it to `AUTH_USER_MODEL` in settings.py)
2. Django Admin View, we can create/update/read/delete users from here only. (In case we implement a new user model, we can add it to admin panel by adding it in admin.py)
    ![img.png](./images/img.png)

### Part 2: JWT Based Authentication

1. /api/user/login
   1. Correct creds
      ![img_1.png](./images/img_1.png)
   2. Wrong creds
      ![img_2.png](./images/img_2.png)

2. /api/user/profile
   1. Valid token
      ![img_3.png](./images/img_3.png)
   2. Invalid token
      ![img_4.png](./images/img_4.png)

3. JWT settings
   ```json
   SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
    "SLIDING_TOKEN_LIFETIME": timedelta(days=2),
    "SLIDING_TOKEN_REFRESH_LIFETIME_ALTERNATIVE": timedelta(days=7),
    "SLIDING_TOKEN_ALTERNATIVE": timedelta(days=14),
}
    ```

### Part 3: Middleware for Incoming Requests

1. Middleware: `JWTMiddleware`, adds a field custom_user to the request, as shown
   ![img_5.png](./images/img_5.png)

### Part 4 (Optional): User API and Serializer

1. DRF Serializer for the User model - resides in the file serializers.py
2. UserViewSet - in views.py
   
   Examples of routers:
   1. Get user
      ![img_6.png](./images/img_6.png)
   2. Get all users
      ![img_7.png](./images/img_7.png)

## Deliverables:

1. The postman collection contains examples and usage for all the scenarios for the apis shown above
   ![img_8.png](./images/img_8.png)
2. Postman collection is at the root of this project
