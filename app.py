from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")  # Render your CV webpage

@app.route("/download")
def download_cv():
    return send_from_directory(directory=".", path="cv.pdf", as_attachment=True)  # Allow CV download

if __name__ == "__main__":
    app.run(debug=True)
