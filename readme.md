Py-Hexagon
==========

A (non-web specific) python version of the [Smaller Web Hexagon](https://github.com/totheralistair/SmallerWebHexagon/) 
by Alistair Cockburn.

- For a full description, you can refer to:  [About Py-Hexagon](docs/about_py-hexagon.md).
- An overview of hexagonal architecture can be read here: [Hexagonal Architecture](docs/hexagonal_architecture.md).

![Alt text](docs/hexagon.png?raw=true "Hexagonal-Architecture")


### Running  code

Either using python 3:

    python -m py_hexagon

Or with docker: 

    docker compose run --rm app

### Running tests

Either run:

    python -m unittest discover tests

or alternatively: 

    docker compose run --rm app unittest discover tests

