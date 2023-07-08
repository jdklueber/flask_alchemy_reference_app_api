from db import db


class ChecklistItemModel(db.Model):
    __tablename__ = "checklist_item"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    desc = db.Column(db.String(255))
    checklist_id = db.Column(
        db.Integer, db.ForeignKey("checklist.id"), unique=False, nullable=False
    )
