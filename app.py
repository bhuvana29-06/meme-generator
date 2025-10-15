from flask import Flask, render_template, request
from meme_generator import generate_meme

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        image = request.files['image']
        top_text = request.form.get('top_text')
        bottom_text = request.form.get('bottom_text')
        output_path = "static/generated_meme.png"
        generate_meme(image, top_text, bottom_text, output_path)
        return render_template("index.html", meme_path=output_path)
    return render_template("index.html", meme_path=None)

if __name__ == "__main__":
    app.run(debug=True)
