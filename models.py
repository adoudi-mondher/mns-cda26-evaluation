from app import db
from datetime import date
from enum import Enum

class TypeEvent(Enum):
    CONFERENCE = "Conférence"
    TEAM_BUILDING = "Team Building"
    SORTIE = "Sortie"
    REPAS_EQUIPE = "Repas d'équipe"
    AUTRE = "Autre"

class Event(db.Model):      
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    type_event = db.Column(db.Enum(TypeEvent))
    date_event = db.Column(db.Date)
    locality = db.Column(db.String(100))
    description = db.Column(db.String(500))
    created_at = db.Column(db.Date, default=date.today)

    def __repr__(self):        
        return f"Event({self.title} - {self.type_event} - {self.date_event} - {self.locality} - {self.description})"

    def to_dict(self):         
        return {
            "id": self.id,
            "title": self.title,
            "type_event" : self.type_event.value,
            "date_event": self.date_event.strftime("%d/%m/%Y") if self.date_event else None,
            "locality" : self.locality,
            "description" : self.description,
            "created_at" : self.created_at.strftime("%d/%m/%Y") if self.created_at else None
        }
    