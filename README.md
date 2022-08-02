# FastAPI Project Example
In this tutorial, we covered how to develop and test an asynchronous API with FastAPI, Postgres, pytest, and Docker using Test-driven Development.

See also

-  [Developing and Testing an Asynchronous API with FastAPI and Pytest](https://testdriven.io/blog/fastapi-crud/).

<!--  DELETE THE LINES ABOVE THIS AND WRITE YOUR PROJECT README BELOW -->

---

## Install

from source
```bash
git clone https://github.com/matheuslfarias/fastapi_crud.git
cd fastapi_crud

```
You have to install docker and docker-compose, then
```bash
docker-compose up -d --build

```
and finally do the tests:.
```bash
docker-compose exec web pytest

```
Test out the following routes:
1. [http://localhost:8002/ping](http://localhost:8002/ping)
2. [http://localhost:8002/docs](http://localhost:8002/docs)
3. [http://localhost:8002/notes](http://localhost:8002/notes)
