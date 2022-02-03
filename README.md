# Overview

This project was an attempt to familiarize myself with the basics of Django web development.

The projects consists of the standard Django web server with an addition of my own sqlite3 database model, and my own views that create two different html webpages.

To be specific, it's a blog in journal format with a new post submission form.

To run the server, navigate to the **/web_apps/ directory in CMD or powershell and use the command 'python manage.py runserver'. You can then navigate to localhost:8000/startle_dreams in a browser to access the webpages.

DISCLAIMER: This projects actually contains a couple of apps (namely blog and projects) created from a tutorial series (listed under 'Useful Websites'), but the startle_dreams app was my own creation.

[Software Demo Video](https://youtu.be/wCgYKGaQ2Ls)

# Web Pages

Note - It should be assumed that 'localhost:8000/' comes before each of the following webpages:

* 'startle_dreams/' --> This is main index of my startle dreams blog/journal. From here you can access startle_dreams/form either via the URL or by clicking the 'Post Submission Form' button on the index webpage.

* 'startle_dreams/form/' --> This is the post submission for used to create new posts for the startle dream index page.

* 'blog/' --> This is the blog index I created while following the tutorial. This blog uses Lorem Ipsum sample text. You can navigate to individual blog listing's detailed pages by clicking on the respective blog index titles.

* 'blog/[n]' --> Each blog listing has a unique number which gets passed into the URL to navigate to it. The detail view shows the blog post and a working comment section.

* 'projects/' --> This is a simple project showcase I created by following the tutorial. This webpage shows the project index.

* 'projects/[n]' --> Each project has a unique number which gets passed into the URL to navigate to it. This is the detailed view of the project.

# Development Environment

* Visual Studio Code
* Python 3.9.7
    * Django

# Useful Websites

* [Real Python](https://realpython.com/get-started-with-django-1/)
* [Learning About Electronics](http://www.learningaboutelectronics.com/Articles/How-to-save-data-from-a-form-to-a-database-table-in-Django.php)

# Future Work

* Make the startle_dreams post submission form redirect you to the index upon post submission.