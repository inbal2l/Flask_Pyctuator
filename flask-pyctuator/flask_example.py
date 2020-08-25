import flask-pyctuator

app = Flask("Flask Example Server")

@app.route("/")
def hello():
    my_logger.debug(f"{datetime.datetime.now()} - {str(random.randint(0, 100))}")
    print("Printing to STDOUT")
    return "Hello World!"

example_app_address = "host.docker.internal"
example_sba_address = "localhost"

pyctuator(
    app,
    "Flask Pyctuator",
    app_url=f"http://{example_app_address}:5000",
    pyctuator_endpoint_url=f"http://{example_app_address}:5000/pyctuator",
    registration_url=f"http://{example_sba_address}:8080/instances",
    app_description="Demonstrate Spring Boot Admin Integration with Flask",
)

app.run(port=5000, host="0.0.0.0")