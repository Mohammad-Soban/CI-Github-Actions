## Continuous Integration (CI) Tutorials

### Why Continuous Integration (CI)
- While working on the project, changes are bound to happen, so dont you think there must be a testing protocol or service which checks if the coding standards are followed, there are no bugs, it gives a proper output or not? This is where Continuous Integration (CI) comes into play.


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