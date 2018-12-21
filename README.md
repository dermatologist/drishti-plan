# :eyes: Drishti-plan | mHealth Machine Learning module for Drishti framework

## About
Drishti is a conceptual extension of the [open mHealth](http://www.openmhealth.org/) model to behaviour intervention technology adopting the sense-plan-act paradigm from robotics. [:eyes: Drishti](https://github.com/E-Health/drishti) is also a reference implementation with the following components: 

* Drishti-sense  is open mhealth [shimmer](https://github.com/openmhealth/shimmer) that interfaces with various mobile frameworks and provides a uniform API.
* [Drishti-plan](https://github.com/dermatologist/drishti-plan) is a python flask API that provides a (FHIR) careplan based on aggregate data using AI.
* [Drishti-act](https://github.com/dermatologist/drishti-act) is a SMART-ON-FHIR application in Vue.js that can deliver the careplan to the mobile device as alerts and messages
* [Drishti-cog](https://github.com/dermatologist/drishti-cog) is the central hub and repository, integrating various services using FHIR as the interface standard.
* [Drishti-EMR](https://github.com/dermatologist/openmrs-module-drishti)  (openmrs-module-drishti) is an [OpenMRS module](https://wiki.openmrs.org/display/docs/Creating+Modules) that provide the user interface for clinicians.
* [Drishti-PHR](https://github.com/dermatologist/openmrs-module-drishti)  (openmrs-owa-drishti) is an [OpenMRS OWA](https://wiki.openmrs.org/display/docs/Open+Web+Apps+Module) that provide the user interface for patients, including authorizing access to their cloud services.

[![Drishti](https://raw.github.com/E-Health/drishti/develop/notes/drishti.png)](http://canehealth.com)

## Instructions

* ***Drishti is not ready for use. The following instructions are only for those who want to contribute/join the project.***
* Currently working on [Drishti-cog](https://github.com/dermatologist/drishti-cog), [Drishti-PHR](https://github.com/dermatologist/openmrs-module-drishti) and [Drishti-EMR](https://github.com/dermatologist/openmrs-owa-drishti)

## Work in progress. Part of Drishti mHealth Framework. [Contact](https://nuchange.ca/contact)

This starter kit is designed to allow you to create very fast your Flask API.

The primary goal of this project is to remain as **unopinionated** as possible. Its purpose is not to dictate your project structure or to demonstrate a complete sample application, but to provide a set of tools intended to make back-end development robust, easy, and, most importantly, fun.

This starter kit comes with a [tutorial](https://github.com/antkahn/flask-api-starter-kit/blob/tutorial/doc/installation.md).
Check it out if you want a quick tutorial on how to use Flask with this architecure.

## Table of Contents
1. [Dependencies](#dependencies)
1. [Getting Started](#getting-started)
1. [Commands](#commands)
1. [Database](#database)
1. [Application Structure](#application-structure)
1. [Development](#development)
1. [Testing](#testing)
1. [Lint](#lint)
1. [Swagger](#swagger)

## Dependencies

You will need [docker](https://docs.docker.com/engine/installation/) and [docker-compose](https://docs.docker.com/compose/install/).

## Getting Started

First, clone the project:

```bash
$ git clone https://github.com/antkahn/flask-api-starter-kit.git <my-project-name>
$ cd <my-project-name>
```

Then install dependencies and check that it works

```bash
$ make install      # Install the pip dependencies on the docker container
$ make start        # Run the container containing your local python server
```
If everything works, you should see the available routes [here](http://127.0.0.1:3000/application/spec).

The API runs locally on docker containers. You can easily change the python version you are willing to use [here](https://github.com/antkahn/flask-api-starter-kit/blob/master/docker-compose.yml#L4), by fetching a docker image of the python version you want.

## Commands

While developing, you will probably rely mostly on `make start`; however, there are additional scripts at your disposal:

|`make <script>`|Description|
|------------------|-----------|
|`install`|Install the pip dependencies on the server's container.|
|`start`|Run your local server in its own docker container.|
|`daemon`|Run your local server in its own docker container as a daemon.|
|`db/connect`|Connect to your docker database.|
|`db/migrate`|Generate a database migration file using alembic, based on your model files.|
|`db/upgrade`|Run the migrations until your database is up to date.|
|`db/downgrade`|Downgrade your database by one migration.|
|`tests`|Run unit tests with unittest in its own container.|
|`lint`|Run flake8 on the `src` directory.|

## Database

The database is in [PostgreSql](https://www.postgresql.org/).

Locally, you can connect to your database using :
```bash
$ make db/connect
```

However, you will need before using this command to change the docker database container's name [here](https://github.com/antkahn/flask-api-starter-kit/blob/master/package.json#L6).

This kit contains a built in database versioning using [alembic](https://pypi.python.org/pypi/alembic).
Once you've changed your models, which should reflect your database's state, you can generate the migration, then upgrade or downgrade your database as you want. See [Commands](#commands) for more information.

The migration will be generated by the container, it may possible that you can only edit it via `sudo` or by running `chown` on the generated file.

## Application Structure

The application structure presented in this boilerplate is grouped primarily by file type. Please note, however, that this structure is only meant to serve as a guide, it is by no means prescriptive.

```
.
├── devops                   # Project devops configuration settings
│   └── deploy               # Environment-specific configuration files for shipit
├── migrations               # Database's migrations settings
│   └── versions             # Database's migrations versions generated by alembic
├── src                      # Application source code
│   ├── models               # Python classes modeling the database
│   │   ├── abc.py           # Abstract base class model
│   │   └── user.py          # Definition of the user model
│   ├── repositories         # Python classes allowing you to interact with your models
│   │   └── user.py          # Methods to easily handle user models
│   ├── resources            # Python classes containing the HTTP verbs of your routes
│   │   └── user.py          # Rest verbs related to the user routes
│   ├── routes               # Routes definitions and links to their associated resources
│   │   ├── __init__.py      # Contains every blueprint of your API
│   │   └── user.py          # The blueprint related to the user
│   ├── swagger              # Resources documentation
│   │   └── user             # Documentation of the user resource
│   │       └── GET.yml      # Documentation of the GET method on the user resource
│   ├── util                 # Some helpfull, non-business Python functions for your project
│   │   └── parse_params.py  # Wrapper for the resources to easily handle parameters
│   ├── config.py            # Project configuration settings
│   ├── manage.py            # Project commands
│   └── server.py            # Server configuration
└── test                     # Unit tests source code
```

## Development

To develop locally, here are your two options:

```bash
$ make start           # Create the containers containing your python server in your terminal
$ make daemon          # Create the containers containing your python server as a daemon
```

The containers will reload by themselves as your source code is changed.
You can check the logs in the `./server.log` file.

## Testing

To add a unit test, simply create a `test_*.py` file anywhere in `./test/`, prefix your test classes with `Test` and your testing methods with `test_`. Unittest will run them automaticaly.
You can add objects in your database that will only be used in your tests, see example.
You can run your tests in their own container with the command:

```bash
$ make tests
```

## Lint

To lint your code using flake8, just run in your terminal:

```bash
$ make lint
```

It will run the flake8 commands on your project in your server container, and display any lint error you may have in your code.

## Swagger

Your API needs a description of it's routes and how to interact with them.
You can easily do that with the swagger package included in the starter kit.
Simply add a docstring to the resources of your API like in the `user` example.
The API description will be available [here](http://127.0.0.1:3000/application/spec).
