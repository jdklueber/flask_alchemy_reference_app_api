from db import db


class ChecklistModel(db.Model):
    __tablename__ = "checklist"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    desc = db.Column(db.String(255))
    items = db.relationship("ChecklistItemModel")
