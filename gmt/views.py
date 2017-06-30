from gmt import app, db
from flask import render_template, url_for, request, flash
import gmt
from gmt.models import Forename, Clan, Family, School, Samurai
from sqlalchemy.sql.expression import func
import random

@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/help')
def help():
    return render_template("help.html")

@app.route('/generator', methods=['GET', 'POST'])
def generator():
    clan = Clan.query.all()
    family = Family.query.all()
    school = School.query.all()
    forename = Forename.query.all()
    
    dummy = {'dclan': int(request.form.get('clan') or -1),
             'dfamily': int(request.form.get('family') or -1),
             'dschool': int(request.form.get('school') or -1),
             'dgender': (request.form.get('gender') or -1),
             'dforename': int(request.form.get('forename') or -1),
             'dhonor': int(request.form.get('honor') or -1),
             'dglory': int(request.form.get('glory') or -1),
             'dstatus': int(request.form.get('status') or -1),
             'dtaint': int(request.form.get('taint') or -1)}

    if request.method == 'POST':
        if request.form.get('generate') == 'Generate':
            if dummy['dclan'] == -1:
                print "change"
                dummy['dclan'] = Clan.query.order_by(func.random()).first().id

            family = Family.query.filter(Family.clan_id==dummy['dclan'])
            if dummy['dfamily'] == -1 and family.all():
                dummy['dfamily'] = family.order_by(func.random()).first().id

            school = School.query.filter(School.clan_id==dummy['dclan'])
            if dummy['dschool'] == -1 and school.all():
                dummy['dschool'] = school.order_by(func.random()).first().id

            if dummy['dgender'] == -1:
                dummy['dgender'] = random.choice(['Male', 'Female'])

            forename = Forename.query.filter(Forename.gender==dummy['dgender'])
            if dummy['dforename'] == -1 and forename.all():
                dummy['dforename'] = forename.order_by(func.random()).first().id

            if dummy['dhonor'] == -1:
                dummy['dhonor'] = int(random.gammavariate(8.0, 4.5)) % 100

            if dummy['dglory'] == -1:
                dummy['dglory'] = int(random.gammavariate(8.0, 3.0)) % 100

            if dummy['dstatus'] == -1:
                dummy['dstatus'] = int(random.gammavariate(3.5, 6.0)) % 100

            if dummy['dtaint'] == -1:
                dummy['dtaint'] = int(random.gammavariate(1.0, 0.5)) % 100

                
        if request.form.get('reset') == 'Reset':
            dummy['dclan'] = -1
            dummy['dfamily'] = -1
            dummy['dschool'] = -1
            dummy['dgender'] = -1
            dummy['dforename'] = -1
            dummy['dhonor'] = -1
            dummy['dglory'] = -1
            dummy['dstatus'] = -1
            dummy['dtaint'] = -1


        if request.form.get('save') == 'Save':
            success = True
            if any(v == -1 for v in dummy.itervalues()):
                flash("Choose everything manually or use 'Generate'!", "error")
                success = False

            family = Family.query.filter(Family.clan_id==dummy['dclan'])
            if all(v.id != dummy['dfamily'] for v in family.all()):
                flash("Family or Clan does not fit!", "error")
                is_success = False

            school = School.query.filter(School.clan_id==dummy['dclan'])
            if all(v.id != dummy['dschool'] for v in school.all()):
                flash("School or Clan does not fit!", "error")
                success = False

            forename = Forename.query.filter(Forename.gender==dummy['dgender'])
            if all(v.id != dummy['dforename'] for v in forename.all()):
                flash("Gender or Name does not fit!", "error")
                success = False

            if success:
                flash("Everything is fine!", "success")
                samurai = Samurai(dummy['dgender'], dummy['dhonor'], dummy['dglory'],\
                                  dummy['dstatus'], dummy['dtaint'], dummy['dclan'],\
                                  dummy['dfamily'], dummy['dschool'], dummy['dforename'])
                db.session.add(samurai)
                db.session.commit()
        
    return render_template("generator.html", \
                           clans=clan, families=family, schools=school, forenames=forename, **dummy)

@app.route('/manager', methods=['GET', 'POST'])
def manager():
    samurai = Samurai.query.all()
    dsamurai = int(request.form.get('samurai') or -1)
    marked_samurai = Samurai.query.filter(Samurai.id==dsamurai).first()
    display = False
    edit = False
    
    if request.method == 'POST':
        if request.form.get('edit') == 'Edit':
           if marked_samurai:
               display = True
               edit = True
        elif request.form.get('edit') == 'Save':
            if marked_samurai:
                display = True
                marked_samurai.notes = request.form.get('notes')
                marked_samurai.honor = int(float(request.form.get('honor')) * 10)
                marked_samurai.glory = int(float(request.form.get('glory')) * 10)
                marked_samurai.status = int(float(request.form.get('status')) * 10)
                marked_samurai.taint = int(float(request.form.get('taint')) * 10)
                db.session.add(marked_samurai)
                db.session.commit()

        if request.form.get('load') == 'Load':
           if marked_samurai:
               display = True

        if request.form.get('delete') == 'Delete':
            if marked_samurai:
                db.session.delete(marked_samurai)
                db.session.commit()
                samurai = Samurai.query.all()
            
            
    return render_template("manager.html", display=display, edit=edit, \
                           dsamurai=dsamurai, marked_samurai=marked_samurai, samurais=samurai)
