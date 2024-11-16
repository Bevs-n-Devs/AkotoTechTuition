# Week 11: Introduction to Flask

Flask is a lightweight web framework written in Python, that allows you to create web applications.

Flask is often referred to as a **microframework**. It is designed to keep the core of the application simple and scalable.

Instead of an abstraction layer for database support, Flask supports extensions to add such capabilities to the application.

You can read more on Flask [here](https://pythonbasics.org/what-is-flask-python/).

## Getting Started

### Install Virtual Environment
To get started we need to create a virtual environment then install the Flask web framework.
```
python -m venv virtual_env
```
`virtual_env` is the name of the virtual environment that you will install onto your local machine. *This can be called anything you want*.
After creating the virtual environment, we can run the virtual environment in order to install Flask to our project.
```
# activate virtual enviornment
venv\Script\activate                                # Windows
source venv/bin/activate                            # MacOS / Linux
```

### Install Flask
Once the virtual environment is running, we can install the Flask web framework to our project.
```
pip install Flask
```

### Creating Our First Route
Now we have Flask installed, we can create our first route.
```
from flask import Flask

app = Flask(__name__)           # initialise the Flask application

@app.route('/')                 # define a route for the root URL
def index():
    return 'My first page'      # response sent when the route is accessed


@app.route('/hello')
def hello():
    return 'Hello world!'

# running the application
if __name__ == '__main__':
    app.run(debug=True)
```
This code creates a route after initializing the app with `app = Flask(__name__)`. The index function is executed whenever the `/` route (the root URL) is accessed.

The `@app.route('/')` decorator binds the URL route `/` to the index function, making it the view function for the root URL of our Flask application. When you run the application and visit `http://localhost:5000/`, the index function will handle the request and return the response `'My first page'`.

To run the app we do the following in the terminal:
```
python filename.py
```
This starts the Flask development server and makes the application accessible at `http://localhost:5000/`.

Since the index route is bound to the root URL (`/`), visiting `http://localhost:5000/` in the browser will display the response from the index function:
```
My first page
```
You can access the hello route by navigating to `http://localhost:5000/hello`, which will display:
```
Hello world!
```

### Introduction to Jinja Templates
Jinja is a powerful templating engine used with Flask to generate dynamic HTML content. It allows you to embed Python-like expressions and logic directly into your HTML files. Jinja templates make it easy to separate the logic of your application from its presentation layer, enabling cleaner and more maintainable code.

**Key Features:**
- Dynamic Content: Insert variables into templates using {{ variable }} syntax.
- Control Structures: Use loops and conditional statements ({% for %}, {% if %}) for dynamic rendering.
- Reusable Components: Include and extend templates for consistent layouts.

We first need to create a `templates` folder within our project directory in order to store our HTML pages.  For the index route, we will create a `template.hmtl` file and modify the index function slightly.
```
# template.html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>Welcome, {{ name }}!</h1>
    {% if show_message %}
        <p>{{ message }}</p>
    {% endif %}
</body>
</html>
```
This template uses Jinja syntax to dynamically render values for `title`, `name`, and `message`. It also includes an if condition (`{% if show_message %}`) to control the display of the message.
We now need to modify our Flask app to import the `render_template` and use it in the index route to render the template and pass dynamic data.
```
from flask import Flask, render_template

app = Flask(__name__)           # initialise the Flask application

@app.route('/')                 # define a route for the root URL
def index():
    # Pass dynamic data to the template
    return render_template('template.html', title='Home Page', name='Alice', show_message=True, message='Hello, Alice!')
```

### Routes vs Endpoints
In Flask, routes and endpoints are closely related but serve different purposes:

- A route defines the URL pattern that maps to a specific view function. For example, `@app.route('/hello')` defines a route for the '/hello' URL.
- An endpoint is the unique identifier for a view function, often used internally by Flask or when generating URLs. By default, the endpoint is the name of the view function, but it can be explicitly named using the endpoint parameter in the route.

**Key Concepts:**
- A single route (e.g., `/hello`) can support multiple HTTP methods such as `GET`, `POST`, `PUT`, and `DELETE`. Each HTTP method can trigger different behaviors in the same view function, allowing a route to handle multiple CRUD operations.
- While a route refers to the URL, the combination of the route and an HTTP method can be thought of as a more granular "endpoint."

### Build Portfolio Page [WEEK 12]
We will use [w3 Schools](https://www.w3schools.com/w3css/w3css_templates.asp) to build our own portfolio with a selection of free HTML templates they have.