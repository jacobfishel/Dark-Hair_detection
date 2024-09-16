# from flask import Blueprint, render_template, request, jsonify, redirect, url_for
# '''Imports:
#     flask: a web dev framework
#     Blueprint: '''

# views = Blueprint("views", __name__)

# @views.route("/")
# def home():
#     return render_template("index.html")

# @views.route("/profile")
# def profile():
#     return render_template("profile.html")

# @views.route("/json")
# def get_json():
#     return jsonify({'name': 'tim', 'coolness': 10})

# @views.route("/data")
# def get_data():
#     data = request.json
#     return jsonify(data)

# @views.route("/go-to-home")
# def go_to_home():
#     return redirect(url_for("views.home"))








from flask import Blueprint, render_template, redirect, url_for

views = Blueprint("views", __name__) #creating a views blueprint

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/core_operations/")
def core_operations():
    return render_template("core_operations.html")

@views.route("/drawing_shapes_and_text_on_images/")
def drawing_shapes_and_text_on_images():
    return render_template("drawing_shapes_and_text_on_images.html")

@views.route("/image_thresholding/")
def image_thresholding():
    return render_template("image_thresholding.html")

@views.route("/edge_detection/")
def edge_detection():
    return render_template("edge_detection.html")