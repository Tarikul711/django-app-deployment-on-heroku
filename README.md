# django-app-deployment-on-heroku

In this project, I am trying to deploy a simple Django project on the live Heroku server. Here I will mention all commands that I have to use to deploy the project.

### Heroku installation commend on mac

    ```python
        brew install heroku/brew/heroku
    ```

Then please check, Is Heroku properly installed on your pc. For hacking please run this commends.

```python
    heroku --version
```

If properly install the Heroku on your device, you have to init git and add all repository on the git and commit it. Here is all git commit

```python
    git init
    git add .
    git status
    git commit -m "message"
```

Then you have to add a file on your project. Must be you have to follow the file name and you have to place it on the root repository.

```python
    Procfile
```

You have to install the `gunicorn` on your device. For installation run this command.

```python
    pip3 install gunicorn
```

Then you have to add this line in your `Procfile` file.

```python
    web: gunicorn APPLICATION_NAME    —log-file -
```

You will get the `APPLICATION_NAME` in the project settings.py file. Inside settings.py `WSGI_APPLICATION` is your APPLICATION_NAME. For this project I had to add this line.

```python
    web: gunicorn djangoheroku.wsgi    —log-file -
```

Then you have to chnage the `ALLOWED_HOSTS` value.

```python
    ALLOWED_HOSTS = ['*']
```

You have to log in to publish the app using command prompts. Then you have to run `heroku create` to create the app in Heroku. Then you have to run `heroku git:remote -a HEROKU_PROJECT_NAME`this command to add your project in the Heroku.

```python
    heroku git:remote -a thawing-wave-03752
```

Then you have to configer heroku using this command

```python
    heroku config:set DISABLE_COLLECSTATIC=1
```

Then you have to push the project on the heruko server.

```python
    git push heroku master
```
