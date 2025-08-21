## Continuous Integration (CI) Tutorials

### Why Continuous Integration (CI)
- While working on the project, changes are bound to happen, so dont you think there must be a testing protocol or service which checks if the coding standards are followed, there are no bugs, it gives a proper output or not? This is where Continuous Integration (CI) comes into play.
- So CI can help in early detection of errors, automation of testing, faster development cycles and reduced integration problems. Python Library named `pylint` can be used for checking coding standards and detecting errors in Python code and `pytest` can be used for writing and running tests.


### How practically Continuous Integration Works
- Developers commit their code to shared repository (Version control systems)
- A CI Server monitors the repository for changes and automatically triggers a set of predefined actions, such as building the application and running tests.
- The code is then built, which includes compiling the code, resolving dependencies, packaging the application for deployment and artifact creation.
- Finally, automated tests are executed to ensure that the code behaves as expected and meets the defined quality standards.


### What is Continuous Integration (CI)
- Continuous Integration (CI) is a software development practice where developers frequently integrate their code changes into a shared repository. Each integration is automatically verified by building the application and running tests to detect errors as early as possible.


### Tools For Continuous Integration (CI)
- **Github Actions**
- **Jenkins**
- **Travis CI**


### What is Github Actions
- An automated service which is smart enough to detect the changes in the codebase, automatically run tests, and provide feedback to the developers is Github Actions.
- This checks can be given in the form of a YAML File. The Github actions executes the defined workflows from the YAML file.


### Configuring Github Actions
- The first and foremost step to work with Github Actions is to create a `.github` directory in your root directory and a `workflows` subdirectory inside it.
- Inside the workflows directory, you can create YAML files to define your workflows. Note the YAML file can have any name, but it must have a `.yml` or `.yaml` extension. Also the .github and workflows directories should have the same name as specified
- The contents of the YAML file is described as follows:
    1. `name`: `Name_of_the_Workflow` specifies the name you want to give to your workflow.
    2. `on`: This defines the events that trigger the workflow. For example:
       ```
        on:
            push:
                branches:
                    - main
                    - dev
            pull_request:
                branches:
                    - main
       ```
        The above yaml configuration triggers the workflow on push events to the main and dev branches, as well as on pull requests targeting only the main branch. Note that you can add more branches or events as needed.
    3. jobs: This section defines the jobs that will be run as part of the workflow. Each job runs in its own environment and can have multiple steps. For example:
       ```
    jobs:
        tests:
            runs-on: ubuntu-latest
               
            steps:
                - name: Checkout code
                uses: actions/checkout@v2

                - name: Set up Python
                uses: actions/setup-python@v2
                with:
                    python-version: '3.10'

                - name: Install dependencies
                run: |
                    python -m pip install --upgrade pip
                    pip install pytest streamlit


                - name: Run tests
                run: |
                    pytest _test.py
       ```
        The above code defines a job named "tests" that runs on the latest version of Ubuntu. It checks out the code, sets up Python 3.10, installs the required dependencies, and runs the tests using pytest. The _test.py file is the test file that contains the test cases.


### Creation of the `_test.py`
- The `_test.py` file contains the test cases for the functions defined in the main application code. It uses the `pytest` framework to define and run the tests.
- An example of the tests can be found in the repository.


### What is Pytest
- Pytest is a testing framework for Python that allows you to write test cases for your code in a simple and scalable way. It provides powerful features such as fixtures, parameterized testing, and easy integration with other tools.
- In the yaml file, the command will execute all the tests on our python code. `pytest` is a testing framework that automatically discovers and runs tests in your codebase. When we run that it looks for files with `_test` or `test_` prefixes and executes all the tests present in those files.


### Types Of Tests
1. **Unit Test**
- It checks the individual components or functions of your code to ensure they work as intended.
- They help catching the errors early by verifying that each part of code behaves as expected.
- For example, a unit test for a function that adds two numbers might check that `add(2, 3)` returns `5`.

2. **Integration Test**
- It checks the interaction between multiple components or systems to ensure they work together correctly.
- For example, an integration test for a web application might check that the frontend and backend communicate properly by simulating a user login.

3. **End-to-End Test**
- It simulates the real user scenarios to verify that the application works as expected from the user's perspective from start to finish, so that the product can be tested in production-like environment
- For example, an end-to-end test for a web application might check that a user can successfully log in, navigate to a specific page, and perform a certain action like purchasing a product.

4. **Static-Code Analysis**
- It ensures that our code follows the best practices and is free from common errors, improves readability and maintainablity.
- Tools like `Pylint`, `Flake8` or `black` helps in identifying and fixing issues in the code.
- This type of testing helps maintain code quality and adherence to coding standards. For example, it can catch unused variables, incorrect imports, and other common issues before they become bigger problems.

5. **Performance Testing**
- It checks the application’s performance under various conditions, such as load, stress, and scalability. It includes measuring response times, resource usage, and throughput.
- It ensures your application can handle high traffic and performs well under stress.
- For example, a performance test might simulate a large number of users accessing the application simultaneously to see how it handles the load.

6. **Security Testing**
- It identifies vulnerabilities and security flaws in the application to ensure that user data is protected and the application is secure from attacks such as SQL Injection, XSS Attacks or insecure dependencies.
- Tools like `Bandit` or `Snyk` can be used to perform security testing in python.

7. **Smoke Tests**
- Smoke Tests are a subset of tests which check the basic functionality of the application to ensure that it is working as expected.
- It quickly identifies whether the application is stable enough for further testings.
- For example, verifying that a web server is running and responding to HTTP Requests.

8. **Regression Testing**
- Regression Testing ensures that the new code changes don't negatively affect existing functionality.
- It prevents bugs from being reintroduced after the application has been modified.
- For example, running a suite tests after a bug fix to ensure the bug doesnt reappear. 

9. **Cross-Browser/Platform Tests**
- These tests verify that your application works correctly accross different platforms or browsers. It ensures a consistent performance and user experience regardless of the browser or device being used.
- For example, testing a website on chrome and then on Firefox and then on Safari to ensure compatibilty.


### Note
- Now as and when we push or pull something from the main or dev branch, the defined workflows in the YAML file will be triggered automatically, running the tests and providing feedback on the code changes.