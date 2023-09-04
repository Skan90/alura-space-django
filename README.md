# Alura Space Django Course

Welcome to my personal repository for the Alura course on [Django - Templates and Good Practices](https://www.alura.com.br/curso-online-django-templates-boas-praticas). Here, I've documented the code and resources related to the course for my reference. 

## Course Overview

In this Python web course, I will: 

- Learn practical aspects of how Django works. 
- Create environment variables efficiently using Python. 
- Understand the concepts of Templates and page rendering in Django. 
- Maintain good programming practices in Django projects. 
- Build my own web applications using the Python language. 

## Course Content

### Getting Started

- Introduction to Django 4, its history, and key framework aspects. 
- Setting up a virtual development environment with virtualenv. 
- Creating a Django project using the `django-admin startproject setup` command. 
- Launching the development server with the `python manage.py runserver` command. 
- Configuring project timezone and language in the `settings.py` file. 
- Enhancing project security by protecting the SECRET_KEY and using the `python-dotenv` package with a `.env` file. 
- Uploading the project to a remote GitHub repository and creating a `.gitignore` file to exclude sensitive data. 

### Building My First App

- Understanding the difference between projects and apps in Django. 
- Creating my first app using the `python manage.py startapp galeria` command. 
- Creating a custom web page by configuring routes in the `views.py` and `urls.py` files. 
- Implementing the best practice of creating a separate `urls.py` file for each app. 
- Isolating the template for the `galeria` app by creating a new folder called `templates` and reconfiguring `settings.py`. 

### Organizing Static Files and Improving UI

- Organizing static files better by creating indicator folders for each app within the `templates` folder. 
- Using embedded Python code within HTML files with Jinja2. 
- Implementing a new custom HTML template along with various static files to improve my site's appearance. 

### Embracing the DRY Principle

- Learning about the DRY (Don't Repeat Yourself) principle and applying it by creating a `base.html` file to avoid code repetition in multiple templates. 
- Using Partial templates to further follow the DRY principle, reducing code duplication. 

## Getting Started

To get started clone this repository to your local machine, make sure you have Python installed on your system. Any other requirements (including Django) can be installed using the requirements.txt in the root directory from this project with the command:

```shell
pip install -r requirements.txt
```

After all requirements are installed, you can run the project server from the root directory with the command:

```shell
python manage.py runserver
```

## License
This code is provided under the MIT License. Feel free to use it for your learning and development purposes. 
Happy learning!