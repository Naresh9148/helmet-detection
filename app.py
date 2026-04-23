from flask import Flask, render_template, request
from ultralytics import YOLO
import os

app = Flask(**name**)

# Load model

model = YOLO("yolov8n.pt")

UPLOAD_FOLDER = "static/uploads"
OUTPUT_IMAGE = "static/output.jpg"

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Ensure upload folder exists

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
if request.method == "POST":
file = request.files["file"]

```
    if file:
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
        file.save(filepath)

        # Run detection
        results = model(filepath)
        results[0].save(filename=OUTPUT_IMAGE)

        return render_template("index.html", output="output.jpg")

return render_template("index.html", output=None)
```

if **name** == "**main**":
app.run(debug=True)
