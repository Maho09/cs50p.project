from flask import Flask, render_template, request
from tempfile import mkdtemp
import os
from werkzeug.utils import secure_filename
import favicon

# Configure application
app = Flask(__name__)

if __name__ == 'main': 
  app.run(debug=True)

UPLOAD_FOLDER = "static/uploads/"
app.config['SECRET_KEY'] = '#$%^&*'



# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024* 1024* 1024
app.config["SESSION_TYPE"] = "filesystem"


ALLOWED_EXTENSIONS = ["png", "jpg", "jpeg"]
filename = 0
exps = []
exp = 0
skills = []
skill = 0
others = {}
name = 0
Address = 0
email = 0
Phone = 0
school = 0
higher_edu = 0
higher_edu_detail = 0
skill_f = 0
objective = 0
facebook = 0
linkedin = 0
twitter = 0

# Configure CS50 Library to use SQLite database
def allowed_file(filename):
    return r"." in filename and filename.rsplit(".", 1) in ALLOWED_EXTENSIONS

def new():
    return 5
    
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/start", methods=["GET", "POST"])
def start():
    exps = []
    exp = 0
    skills = []
    skill = 0
    others = {}
    other = 0
    if request.method == "POST" :
        name = request.form.get("Full name")
        Address = request.form.get("Address")
        job = request.form.get("job")
        email = request.form.get("Email")
        Phone = request.form.get("Phone")
        school = request.form.get("school")
        grade = request.form.get("grade")
        higher_edu = request.form.get("Higher education")
        higher_edu_detail = request.form.get("Higher education detail")
        gpa = request.form.get("gpa")
        skill_f = request.form.get("skill")
        skill_detail = request.form.get("skill_detail")
        objective = request.form.get("objective")
        facebook = request.form.get("Facebook")
        linkedin = request.form.get("linkedin")
        twitter = request.form.get("twitter")
        file = request.files["file"]
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))
        
        
        while True:
            exp_head = request.form.get(f"exp{exp}")
            exp_title = request.form.get(f"exp_title{exp}")

            exp_date = request.form.get(f"exp_date{exp}")
            man = type(exp_date)
            #.split("-")[0] +"/"+ request.form.get(f"exp_date{exp}").split("-")[1] 
            exp_date1 = request.form.get(f"exp_date1{exp}")
            exp_info = request.form.get(f"exp_info{exp}")
            #.split("-")[0] +"/"+ request.form.get(f"exp_date1{exp}").split("-")[1]

            
            if not exp_head:
                break
            exps.append([exp_head, exp_date, exp_info, exp_date1, exp_title])
            exp += 1

        while True:
            skill_0 = request.form.get(f"skill{skill}")
            skill_detail = request.form.get("skill_detail")

            if not skill_0:
                break
            skills.append([skill_0,skill_detail])
            skill += 1

        while True:
            other_0 = request.form.get(f"sec{other}")
            other_0_info = request.form.get(f"sec_info{other}")
            if not other_0:
                break
            others[other_0] = other_0_info
            other += 1
        
    # return True on success and False on errors
        return render_template("CV.html",
        name = name, Address=Address,
        email = email, Phone = Phone, gpa=gpa, job=job, exps=exps, school = school, grade=grade, higher_edu = higher_edu, higher_edu_detail = higher_edu_detail, skill_f = skill_f, skill_detail=skill_detail, others=others, objective = objective, facebook = facebook, linkedin = linkedin, twitter = twitter, filename=filename)

    else:
        return render_template('create.html')

            
def main():
    return True

main()