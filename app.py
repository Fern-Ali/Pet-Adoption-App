"""Pet Adoption application."""

from flask import Flask, request, render_template, redirect, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import addPetForm
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///pets'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "itsefsefsefefesesefsef!!"

debug = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
db.create_all()


@app.route('/', methods=["GET"])
def redirect_list_users():
    flash("Redirected to available pets!", "success")
    return redirect('/pets/available')

@app.route('/pets/available', methods=["GET"])
def list_pets():
    """Return homepage, list all users."""
    pets = Pet.query.all()
    
    
    return render_template('home.html', pets=pets,  )


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""

    form = addPetForm()
    #raise
    
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data       
        age = form.age.data
        
        if form.photo_url.data and form.notes.data and form.age.data:
            photo_url = form.photo_url.data
            notes = form.notes.data
            new_pet = Pet(name=name, species=species, photo_url=photo_url, notes=notes, age=age)
        elif form.notes.data or form.age.data and form.photo_url.data == None:
            notes = form.notes.data
            new_pet = Pet(name=name, species=species, notes=notes, age=age)
        else:
            new_pet = Pet(name=name, species=species, image_url=image_url)
        db.session.add(new_pet)
        db.session.commit()
        flash(f"Added {name}, a {species}", "success")
        return redirect("/pets/available")

    else:
        return render_template(
            "add_pet.html", form=form)


@app.route('/pets/<int:id>', methods=["GET", "POST"])
def list_specific_pet(id):
    """Return pet details page, based on user ID."""
    
    pets = Pet.query.all()
    #import pdb; pdb.set_trace()
    specified_pet = Pet.query.filter_by(id=id).all()
    name = specified_pet[0].name
    species = specified_pet[0].species
    photo_url = specified_pet[0].photo_url
    age = specified_pet[0].age
    avail = specified_pet[0].available
    notes = specified_pet[0].notes

    #title=""
    #content=""
    #thumbnail=""

    #if request.method == 'POST':
    #    post = request.form
    #    title = post['title']
    #    content = post['content']
    #    thumbnail = post['image_url']
    
 
    
    return render_template('pet_page.html', name=name, specified_pet=specified_pet, species = species, photo_url=photo_url, id=id, notes=notes, avail=avail, age=age)

@app.route('/pets/<int:id>/edit', methods=["GET", "POST"])
def edit_specified_pet(id):
    """Edit user details, based on user ID."""
    specified_pet = Pet.query.filter_by(id=id).all()
    specified_pet1 = Pet.query.get_or_404(id)
    form = addPetForm(obj=specified_pet1)
    name=specified_pet[0].name
    if request.method == 'POST':
        
        
        our_request = request.form
        name=our_request['name']
        specified_pet[0].name = name
        if our_request['species']:
            species=our_request['species']
            specified_pet[0].species = species

        if our_request['age']:
            age=our_request['age']
            specified_pet[0].age = age

        if our_request['photo_url']:
            photo_url=our_request['photo_url']
            specified_pet[0].photo_url = photo_url

        if our_request['notes']:
            notes=our_request['notes']
            specified_pet[0].notes = notes
        
        
        updated_pet = specified_pet[0]
        db.session.add(updated_pet)
        db.session.commit()
        flash(f"You updated {name}!", "success")
        return redirect(f'/pets/{id}')
    return render_template('pet_edit.html', id=id, specified_pet=specified_pet, form=form, name=name)