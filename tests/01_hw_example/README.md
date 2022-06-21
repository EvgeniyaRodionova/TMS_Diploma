### Environment Variables

Please ensure to read through all the environment variables [defined here](./framework/common/env_vars.py)
to understand what they control. Default configurations for pytest can be setup so that these do not
need adding each time you run a specific test in PyCharm:

- Click `Run -> Edit Configurations...`
- Click `Edit configuration templates...`
- Expand the `Python` option on the left-hand side
- Click `pytest`
- Add the necessary environment variables here so all new pytest configurations inherit them for free

# Running Tests

### Via PyCharm
- Confirm that PyCharm has been configured correctly: project interpreter and environment variables
- Navigate to any of the `test_task_<number>` files and use the PyCharm UI to run the test
It should pass first time. 

### Via CLI

To run all the tasks, it's advisable to do that via the command line. This can be done via the following command
from the `selenium-webdriver` folder:

```shell
export RUN_HEADLESS=False
export AUT_IS_INSIDE_WSL=True # if running inside WSL
poetry run pytest
```

### Via Docker

To run the tests inside a container using the image [built here](./README.md#docker):

```shell
docker run --env AUT_IS_INSIDE_WSL=True \
           --env RUN_HEADLESS=False \
           aut:local \
           /bin/bash -c "poetry run pytest"
```
