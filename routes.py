from flask import request, render_template, flash, redirect, url_for, jsonify
from app import app, db
from models import Event, TypeEvent
from datetime import datetime, date

@app.route("/")
def list_events():
    events = Event.query.all()

    return render_template("list_event.html", events=events)

@app.route("/add", methods=["GET", "POST"])
def add_event():
    if request.method == "POST":
        title = request.form.get('title')
        type_event = request.form.get('type_event')
        date_event = request.form.get('date_event')
        locality = request.form.get('locality')
        description = request.form.get('description')

        if not all([title, type_event, date_event, locality, description]):
            flash("Tous les champs sont obligatoires !", "error")
            return redirect(url_for('add_event'))
        
        date_obj = datetime.strptime(date_event, '%Y-%m-%d').date()
        type_enum = TypeEvent[type_event]

    new_event = Event(
        title=title,
        type_event=type_enum,
        date_event=date_obj,
        locality=locality,
        description=description
    )

    db.session.add(new_event)
    db.session.commit()

    flash("Évènement créé avec succès !", "success")

    return redirect(url_for("list_event"))

@app.route("/api/events")
def get_upcoming_events():
    events = Event.query.filter(
        Event.date_event >= date.today()
    ).order_by(
        Event.date_event
    ).limit(5).all()
    
    events_list = [event.to_dict() for event in events]
    
    return jsonify(events_list)

@app.route("/delete/<int:event_id>")
def delete_event(event_id):
    event =  Event.query.get(event_id)
    if not event:
        flash("Évènement introuvable !", "error")
        return redirect(url_for('list_events'))

    db.session.delete(event)
    db.session.commit()
    flash("Évènement supprimé avec succès !", "success")

    return redirect(url_for('list_events'))
