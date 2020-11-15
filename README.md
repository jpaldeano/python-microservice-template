# python-service-template

## Best Practices 
We follow PEP8 - Style Guide for Python Code: `https://www.python.org/dev/peps/pep-0008/`.

### Modules and Packages names

 Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. Python packages should also have short, all-lowercase names, although the use of underscores is discouraged.

### Assumptions
1. app.py contains the service start and we should create all the middleware that is common to the routes here and pass it to each route (Eg: database connections, loggers, etc...).
2. (almost) every python file should have a unit test and these should not be using a database but a mock instead and external resources should be stubbed.
3. e2e tests should use a local database and the db should be purged after the tests run.

### Tips
1. Install Python packages for VSCode.
2. In case you want to run the app locally for some reason you can load the environment variables with the following command:

> export $(grep -v '^#' .env | xargs)