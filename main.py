from flask import Flask, render_template, url_for

app= Flask(__name__)

@app.route("/")
def test():
    return render_template("index3.html")

if __name__ == '__main__':
    app.run(debug=True)

