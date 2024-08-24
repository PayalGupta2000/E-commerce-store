# E-commerce-store
Set Up

# Clone the Repository: 
git clone https://github.com/PayalGupta2000/E-commerce store.git

# Create a virtual environment to install dependencies in and activate it:
Python -m venv env .\env\scripts\activate

# Then install the dependencies:
(env)$ pip install -r requirements.txt The (env) prefix in the prompt indicates the terminal session is operating in the virtual environment.

# Run the Development Server:
(env)$ python manage.py runserver

Features-

# Signup-
You can signup with provide following credentials- username,password,email,phone number and address. Signup API Url - 127.0.0.1:8000/signup/

# Signin-
You can sign in using your username or email, along with your password. Upon successful login, you will receive a token (alphanumeric) which will be required for placing orders and logging out. Signup API Url - 127.0.0.1:8000/signup/

# Product Browsing-
You can see all the product without sign in. Product Browse API Url- 127.0.0.1:8000/products/

# Order Creation-
You must be signed in to place an order. Provide user, product, and quantity. The total price will be automatically calculated based on the product price and quantity. Order Creation API Url- 127.0.0.1:8000/orders

Additional Information

# Token Handling-
After login,for create an order you have to pass the token like this- Authorization Token

# Migration-
before run the server,apply migrations. python manage.py migrate
