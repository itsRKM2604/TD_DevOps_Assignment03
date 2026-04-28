from flask import Flask, request, jsonify
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

client = MongoClient(MONGO_URI)
db = client.test
collection = db['user-data']

app = Flask(__name__)

@app.route("/submit", methods=['POST'])
def handleFormSubmit():
    try:
        formdata = dict(request.json)
        collection.insert_one(formdata)

        return jsonify({
            "success": True,
            "message": "Data inserted successfully"
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=9090)