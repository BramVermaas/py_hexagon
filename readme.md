Py-Hexagon
==========

A (non-web) python version of the [Smaller Web Hexagon](https://github.com/totheralistair/SmallerWebHexagon/) 
by Alistair Cockburn.

![Alt text](docs/hexagon.png?raw=true "Rating Hexagon")


Like the original by Alistair, this is an example of a simple hexagon 
with one **driving** (also called inbound or left-side) port 
and one **driven** (outgoing or right-side) port.


- The application simply calculates the formula: `result = input * rate`.
- The driving port is connected to either a user input prompt or to a fake input (test double).
- The driven port looks up the rate from either a file or a fake (test double).

*To keep the example short, input sanitization and error handling have been left out.*
*Also, the directory structure and module names have been chosen for illustrative purposes.*
*This is not production ready code,*
*it merely serves to convey the concept of hexagonal architecture.*


## Running the application

If you have python 3 installed, you can run:

    python -m py_hexagon

Otherwise, you can use docker: 

    docker compose run --rm app

## Running tests

Either run:

    python -m unittest discover tests

or alternatively: 

    docker compose run --rm app unittest discover tests



## Further reading
- [Alistair Cockburn, hexagonal-architecture](https://alistair.cockburn.us/hexagonal-architecture/)
- [A color coded guide to ports and adapters](https://8thlight.com/insights/a-color-coded-guide-to-ports-and-adapters)

