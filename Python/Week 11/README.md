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
# main.py
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

We first need to create a `templates` folder within our project directory in order to store our HTML pages.  For the index route, we will create an `index.hmtl` file and modify the index function slightly.
```
# index.html
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

@app.route('/hello')
def hello():
    return 'Hello World!'
```

### Routes vs Endpoints
In Flask, routes and endpoints are closely related but serve different purposes:

- A route defines the URL pattern that maps to a specific view function. For example, `@app.route('/hello')` defines a route for the '/hello' URL.
- An endpoint is the unique identifier for a view function, often used internally by Flask or when generating URLs. By default, the endpoint is the name of the view function, but it can be explicitly named using the endpoint parameter in the route.

**Key Concepts:**
- A single route (e.g., `/hello`) can support multiple HTTP methods such as `GET`, `POST`, `PUT`, and `DELETE`. Each HTTP method can trigger different behaviors in the same view function, allowing a route to handle multiple CRUD operations.
- While a route refers to the URL, the combination of the route and an HTTP method can be thought of as a more granular "endpoint."

#### Creating A Form - Handling A POST Request
We will create a form within the index HTML to prompt the user to enter their name and age, which will be handled through a `POST` request.
```
# index.html
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

    <form action="/about" method="POST">
        <h1>Please complete the form</h1>
        <input name="username" type="text" placeholder="Enter your name..." required>
        <input name="age" type="number" placeholder="Enter your age..." required>
        <button type="submit">Submit Form</button>
    </form>
</body>
</html>
```
Here we have created a `form` HTML tag with `action` and `method` attributes. 
- The `action` attribute specifies that the form data will be sent to the `/about` route.
- The method attribute specifies how the data will be transmitted. Using a `POST` request means the data will be included in the request body instead of appended to the URL, making it more secure for handling sensitive information.
Inside the form we have two `input` tags which will have 4 attributes:
- `name`: This acts as a key for the data submitted, where the value entered by the user becomes the associated value. For example, name="username" maps the inputted name to the key username in the request data. This will become important to us later on when we are extracting data from the form.
- `type`: This defines the expected type of input to expect from the user. A `text` type specifies that the input must be a string, and any numbers (integers) will be converted to a string format. `number` specifies that the input should expect a numeric input, which may include decimals.  There are other types we can specify - like `email`, `password` and many more - but for now `text` and `number` are all we need!
- `placeholder`: Provides a short hint inside the input box to guide the user (e.g., `"Enter your name..."`).
- `required`: Ensures the user cannot submit the form without providing input for the field. The browser will display a warning if a required field is left blank.

Finally, to handle the submitted data, we need to update the main.py file to include an additional route for the `/about` endpoint that processes a `POST` request.
```
# main.py
from flask import Flask, render_template, request, url_for

app = Flask(__name__)           

@app.route('/', methods=['GET'])                 
def index():
    if request.method == 'GET':
        title = 'Any Page'
        name = 'Yaw'
        message = 'Welcome to my first Flask app!'
        show_message = True
        return render_template('index.html', title=title, name=name, message=message, show_message=show_message )     

@app.route('/hello')
def hello():
    return 'Hello World!'

@app.route('/about', methods=['POST']) # this sends information from the form to another URL/route 
def about():
    if request.method == 'POST':
        username = request.form.get('username')
        age = request.form.get('age')
        return render_template('about.html', username=username, age=age)


# running the application
if __name__ == '__main__':
    app.run(debug=True)
```
In this updated version of `main.py`, we have imported the `request` object from Flask. This is essential for handling the HTTP requests sent to our endpoints. Specifically, it allows us to access form data submitted via a POST request.

In the `/about` route, we define a `POST` method to process the form submission. We include a check with if `request.method == 'POST'` to ensure that the logic inside this route executes only for POST requests. While this may seem redundant with the `methods=['POST']` restriction in the route decorator, **it can serve as an additional layer of validation**.

To extract the data submitted from the form, we use:

- `request.form['username']` or
- `request.form.get('username')`.
Both methods retrieve the value associated with the name attribute of the corresponding input field in the form:

- `request.form['username']` *raises a KeyError if the key (`username`) is missing*.
- `request.form.get('username')` is safer, as it *returns `None` by default if the key is not found*.

The extracted values are stored in variables `username` and `age`. These variables are then passed to the `about.html` template to dynamically display the submitted data back to the user.
```
# about.html
<!DOCTYPE html>
<html>
<head>
    <title>About</title>
</head>
<body>
    <h1>Welcome, {{ username }}!</h1>
    <p>Hello {{ username }}, your age is {{ age }}.</p>
</body>
</html>
```
Now when we run the updated app using `python main.py`, we can complete the form in the `/` route, where the data will get sent to the `/about` page where the data will be displayed back to the user.

#### Dynamic HTML Pages With Jinja Templates
When creating new HTML pages, we repeatedly use the same structure, including tags like `<html>`, `<head>`, `<body>`, etc. While this is fine for a small number of pages, it can become time-consuming and error-prone, especially if many pages share common elements, such as headers, footers, or styles. Making changes across multiple pages can also lead to inconsistencies.

With Flask's Jinja2 templating engine, we can solve this problem by creating a base template. A base template allows us to define a common structure for all our pages. Other pages, such as `/about`, `/hello`, and any future pages, can extend this base layout, inheriting its structure and dynamically updating only the parts that need to change. This approach ensures consistency and reduces redundancy, making it easier to manage and update the website.

We will create a `layout.html` file to act as the base template. This file will define the overall structure of the website, including shared elements like the navigation bar, header, and footer. Other pages will inherit this layout and replace or add content in specific sections.
```
# layout.html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
        <h1>Welcome, {{ name }}!</h1>
        {% if message %}
            <p>{{ message }}</p>
        {% endif %}

    {% block content %} {% endblock %}
</body>
</html>
```
To enhance our Flask application with dynamic page titles, headers, and descriptions, we can pass these variables from `main.py` to the respective templates. Here's how to update the `main.py` file:
```
from flask import Flask, render_template, request, url_for

app = Flask(__name__)          

@app.route('/', methods=['GET'])                
def index():
    if request.method == 'GET':
        title = 'Main Page'
        name = 'Yaw'
        message = 'Welcome to my first Flask app!'
        show_message = True
        return render_template('index.html', title=title, name=name, message=message, show_message=show_message )      # response sent when the route is accessed
    

@app.route('/about', methods=['POST']) # this sends information from the form to another URL/route 
def about():
    if request.method == 'POST':
        username = request.form.get('username')
        age = request.form.get('age')
        title = 'About Me'
        name = username
        message = 'Welcome to the About Page'
        return render_template('about.html', username=username, age=age, title=title, name=name, message=message)
        
        

@app.route('/hello') #  this defaults to a GET request
def hello():
    title = 'Hello'
    name = 'Yaw'
    message = 'Welcome to the Hello World Page!'
    return render_template('hello.html', name=name, message=message, title=title)

# running the application
if __name__ == '__main__':
    app.run(debug=True)
```
We can now update both the `index.html` and `about.html` templates to extend the base layout defined in `layout.html`. This allows the pages to inherit the shared structure, such as the header, navigation bar, and footer, while defining unique content within the `{% block content %}` block.
```
# index.html
{% extends "layout.html" %}

{% block content %}
    <form action="{{ url_for('about') }}" method="POST">
        <h1>Please complete the form</h1>
        <input name="username" type="text" placeholder="Enter your name...">
        <input name="age" type="number" placeholder="Enter your age...">
        <button type="submit">Submit Form</button>
    </form>
{% endblock %}
```
Notice that we have updated the action attribute from `action="/"` to `action="{{ url_for('about') }}"`. While they may seem similar, there is a key difference:

- Using `action="/"` explicitly points to the root route (`/`) of the application. **This is static and does not adapt if the route or function name changes**.
- By using `action="{{ url_for('about') }}"`, we are dynamically generating the URL for the about route. **This is tied to the about function, which is associated with the `/about` decorator in `main.py`**.

**Why Use url_for?**
- `url_for('about')` ensures that the form always points to the correct route, even if the route URL or function name is modified later.
- Hardcoding URLs like `"/about"` can lead to maintenance issues if the route structure evolves, whereas url_for automatically adapts.
- Referring to the function name directly (about) provides clarity, as it links the form's action to the corresponding function in `main.py`.

This small change increases flexibility and aligns with best practices in Flask applications, ensuring maintainable and error-resistant routing.

```
# about.html
{% extends "layout.html" %}

{% block content %}
        {% if username %}
            <p>Hello {{ username }}, your age is {{ age }}</p>
        {% endif %}

        <p>Click <a href="{{ url_for('hello') }}">here</a> to go to the hello page</p>
{% endblock %}
```
We have added an `anchor` (`<a>`) tag with a `href` attribute that points to the `/hello` route. This allows users on the `/about` page to click the here hyperlink and navigate to the `/hello` route seamlessly.

Now all we need to do is create a `hello.html` template to extend the base layout defined in `layout.html`.
```
# hello.html
{% extends "layout.html" %}

{% block content %}
        <p>Hello to all my friends!</p>
{% endblock %}
```
Now we have all the routes set up, we can runt he app with the following: `python main.py`

### Build Portfolio Page [WEEK 12]
We will use [w3 Schools](https://www.w3schools.com/w3css/w3css_templates.asp) to build our own portfolio with a selection of free HTML templates they have.