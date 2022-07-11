# create image
docker build -t <name>

# run tests
sudo docker run <name> pytest -s -v tests/web_test.py