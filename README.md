# TODO Flask
A simple Flask tech-demo running on Docker.

## Running the example
```
docker build -t todo-flask:latest .
docker run -d -p 5000:5000 todo-flask
```

or, if you want to give your container a specific name:

```
docker build -t todo-flask:latest .
docker run --name todo-flask -d -p 5000:5000 todo-flask
```