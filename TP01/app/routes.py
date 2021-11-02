from app import app
from flask import render_template, request
from app.model import dict_tasks


@app.route("/")
def index():
    return render_template("page.html",tasks = dict_tasks)

@app.route("/add", methods=["GET", "POST"])
# methode d'ajout d'une tache
def addTask():
    if request.method == "GET":
        return render_template("page.html",tasks = dict_tasks)
    else:
        _task = {'text': request.form["todoitem"]}

        # dans le cas d'un input vide
        if request.form["todoitem"] == "" :
            return render_template("page.html",tasks = dict_tasks)

        # initialisation du compteur de tache
        if not dict_tasks.keys():
            num_task = 1

        # incrementation du compteur de tache
        else :  
           num_task = len(dict_tasks) + 1

        # ajout de la tache
        dict_tasks[num_task] = _task
        return render_template("page.html", tasks = dict_tasks)
        


@app.route("/delete/<int:key>")
def delTask(key):
    # suppression de la tache dans le dictionnaire
    if key in dict_tasks:
        del dict_tasks[key]
    
    else:
        return 'the key doesn\'t exist'
    return render_template("page.html",tasks = dict_tasks)


    