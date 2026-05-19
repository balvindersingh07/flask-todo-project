from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["todoDB"]
collection = db["todoItems"]

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    data = {
        "itemName": request.json.get("itemName"),
        "itemDescription": request.json.get("itemDescription")
    }

    collection.insert_one(data)

    return jsonify({
        "message": "Todo item saved successfully"
    })

if __name__ == '__main__':
    app.run(debug=True)