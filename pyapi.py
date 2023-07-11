from flask import Flask, request, jsonify

app = Flask(__name__)

# GET ROUTE
# Add decorator @ to make this accessible
@app.route("/get-user/<user_id>") # <user_id> path parameter
def get_user(user_id): # same variable as the path parameter
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "email": "john@doe.com"
    }

    # extra variable passed on the url, called query parameter
    # like "get-user/123?extra=hello world"
    extra = request.args.get("extra")
    if extra: user_data["extra"] = extra

    return jsonify(user_data), 200

@app.route("/create-user", methods=["POST"])
def create_user():
    # If additional methods were accepted, 
    # we could perform a condition on the methods
    #if request.method == "POST":

    # Get the data in JSON format
    data = request.get_json()

    # Here we could add this to a database, for example

    return jsonify(data), 201

if __name__ == "__main__":
    app.run(debug=True)