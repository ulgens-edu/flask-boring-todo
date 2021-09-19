# Boring Todo Tutorial

Output from freeCodeCamp.org's ["Learn Flask for Python - Full Tutorial"](https://www.youtube.com/watch?v=Z1RJmh_OqeA)  
Preview: https://ulgens-flask-boring-todo.herokuapp.com/

### Notes:
* A buildpack should be added before the first deployment.
  * [Python Poetry Buildpack](https://github.com/moneymeets/python-poetry-buildpack/)
  * `POETRY_VERSION` env var is set to `1.1.8` 
* The application uses SQLite and doesn't keep the file between deployments.
* The deployment experience can be improved by usign [heroku.yml](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml) file.
