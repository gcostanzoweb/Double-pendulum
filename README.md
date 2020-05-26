# Double Pendulum w/ Backend Integration
This repo is a fork of the [LukeTheWalker/Double-pendulum](https://github.com/LukeTheWalker/Double-pendulum "LukeTheWalker/Double-pendulum") repo, leaving most of the code unchanged but integrating it with a Python backend using Flask.

The original project featured a JS script containing an array of coordinates, or *"angles"* of the double pendulum, generated by a Python script, and later included in an HTML file.

The addition proposed in this fork is that of generating the angles array in a Flask app backend, and obtaining it in the frontend via a JS fetch.

## Installation 

This repo uses **pipenv** to manage its dependencies.

```
cd Double-pendulum
pipenv install
pipenv shell
```

To start running the Flask app, set the `my_app.py` file in the PATH:
`export FLASK_APP=my_app.py`
or
`set FLASK_APP=hello.py`
depending on your OS, and then type
`flask run`
to start the server.

Finally, open `index.html` in your browser to watch the Double Pendulum animation.

## Context

This exercise is part of a tutoring / teaching job for the **"HOUR of CODE"** 2019/20 course in Catania, an introduction course to computer science and programming aimed at a team of high school students.

While proposing a very basic program of 25 lessons, both theoretical and practical, the students were also provided with one-on-one tutoring for their personal projects.