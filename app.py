import datetime
import os
import sys
# print(sys.path)
from flask import Flask, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    client = MongoClient(os.getenv("MONGODB_URI"))
    db = client.microblog1


    entries = []

    @app.route("/", methods=["POST","GET"])
    def Home():
        print([e for e in db.entries.find({})])
        if request.method == "POST":
            entry_content = request.form.get("content")
            format_date = datetime.datetime.today().strftime("%Y-%m-%d")
            entries.append((entry_content,format_date))

        entry_with_date = [(
            entry[0], entry[1], datetime.datetime.strptime(entry[1], "%Y-%m-%d").strftime("%b %d"))
            
            for entry in entries
        ]
        return render_template("Microblog.html", entries=entry_with_date)

    return app

