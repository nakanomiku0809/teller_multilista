from flask import Flask, jsonify, render_template
from files import Files

app = Flask(__name__)

files = Files()
multilist = files.read_divipola()
multilist.print_multilist()


@app.route("/")
def index():
    markers = files.get_markers(multilist)
    return render_template("index.html", markers=markers)


@app.route("/api/divipola")
def api_divipola():
    return jsonify(files.to_json(multilist))


@app.route("/api/municipalities")
def api_municipalities():
    return jsonify(files.get_markers(multilist))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)