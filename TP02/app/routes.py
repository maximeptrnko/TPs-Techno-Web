from app import app
from flask import render_template, request, redirect, url_for,flash,json
import uuid

from app.model import dict_tasks

app.secret_key = "hello"


@app.route("/")
def index():
    return render_template("page.html",tasks = dict_tasks)


# @app.route("/add/<int:id>", methods=["GET", "POST"])

@app.route("/add", methods=["GET", "POST"])
# methode d'ajout d'une tache
def addTask():
    if request.method == "POST":

        _task = {'text': request.form["todoitem"]} 

        # dans le cas d'un input vide
        if request.form["todoitem"] == "" :
            return render_template("page.html",tasks = dict_tasks)

        # id de la tache
        num_task = int(uuid.uuid4().int & (1 << 32) - 1)
        

        if num_task in dict_tasks['tasks_to_do'].keys() and num_task in dict_tasks['tasks_done'].keys():
            num_task = int(uuid.uuid4().int & (1 << 32) - 1)

    


        # ajout de la tache
        dict_tasks['tasks_to_do'][num_task] = _task
        return render_template("page.html", tasks = dict_tasks)


    if request.method == "GET":
        return render_template("page.html",tasks = dict_tasks)
    else:
        return 'Sorry there a problem, return to the Homepage please.'
    

@app.route("/modify/<int:key>", methods=["GET", "POST"])
def modifyTask(key):

    print('MODIFY CALLED ---------------------')

    if request.method == "POST":
        new_input = {'text': request.form["modifitem"]}


        dict_tasks['tasks_to_do'][key] = new_input
        return render_template("page.html", tasks = dict_tasks)
    if request.method == "GET":
        return render_template("page.html",tasks = dict_tasks)
    else:
        return 'Sorry there a problem, return to the Homepage please.'



@app.route("/done/<int:key>")
def doneTask(key):

    if key in dict_tasks['tasks_to_do']:
        dict_tasks['tasks_done'][key] = dict_tasks['tasks_to_do'][key]
        del dict_tasks['tasks_to_do'][key]    
    else:
        flash("the key doesn\'t exist")
        return redirect('page.html',tasks = dict_tasks)

    return render_template("page.html",tasks = dict_tasks)



@app.route("/undo/<int:key>")
def undoTask(key):
    # suppression de la tache dans le dictionnaire

    if key in dict_tasks['tasks_done']:
        dict_tasks['tasks_to_do'][key] = dict_tasks['tasks_done'][key]
        del dict_tasks['tasks_done'][key]    
    else:
        flash("the key doesn\'t exist")
        return redirect('page.html',tasks = dict_tasks)

    return render_template("page.html",tasks = dict_tasks)



@app.route("/delete/<int:key>")
def delTask(key):
    # suppression de la tache dans le dictionnaire
    if key in dict_tasks['tasks_done']:
        del dict_tasks['tasks_done'][key]

    else:
        flash("the key doesn\'t exist")
        return redirect('page.html',tasks = dict_tasks)

    return render_template("page.html",tasks = dict_tasks)


@app.route("/delete_tasks_done")
def delAllTask():
    dict_tasks['tasks_done'].clear()
    return render_template("page.html",tasks = dict_tasks)



@app.route("/done_all_tasks")
def doneAllTask():

    for key in dict_tasks['tasks_to_do']:
        if key in dict_tasks['tasks_to_do']:
            dict_tasks['tasks_done'][key] = dict_tasks['tasks_to_do'][key]
                

    dict_tasks['tasks_to_do'].clear()
    return render_template("page.html",tasks = dict_tasks)





