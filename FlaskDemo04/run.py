from flask import Flask, request, render_template
import datetime, os 

app = Flask(__name__)

@app.route("/01-form", methods=["GET","POST"])
def form_views():
    if request.method == "GET":
        return render_template("01-form.html")
    else:
        uname = request.form.get('uname')
        hobby = request.form.getlist("hobby")
        country = request.form.getlist("country")
        print(uname)
        print(hobby)
        print(country)
        return "data recv OK"



@app.route("/02-file", methods=["GET", "POST"])
def file_views():
    if request.method == "GET":
        return render_template("02-file.html")
    else:
        uname = request.form["uname"]
        uimg = request.files["uimg"]
        now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        new_name = now_time + uimg.filename
        try:
            basedir = os.path.dirname(__file__)
            name = os.path.join(basedir,"static",new_name)
            uimg.save(name)
        except Exception as e:
            print("update fail...")
            print(e)
        return "update OK..."

@app.route("/03-release", methods=["GET","POST"])
def release_views():
    if request.method == "GET":
        return render_template("03-release.html")
    else:
        utitle = request.form["utitle"]
        utype = request.form["utype"]
        uwrite = request.form["uwrite"]
        print("utitle:",utitle)
        print("utype:", utype)
        print("uwrite:",uwrite)
        if request.files["uimg"]:
            filename = request.files["uimg"]
            generate_filename(filename)
            return "Img saved ok."
        return "No img."

def generate_filename(filename):
    basedir = os.path.dirname(__file__)
    now_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
    new_name = now_time + filename.filename
    img_url = os.path.join(basedir,"static",new_name)
    filename.save(img_url)


if __name__ == "__main__":
    app.run(debug=True)





