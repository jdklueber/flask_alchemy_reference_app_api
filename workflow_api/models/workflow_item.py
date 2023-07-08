from db import db


class WorkflowItemModel(db.Model):
    __tablename__ = "workflow_item"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    desc = db.Column(db.String(255))
    workflow_id = db.Column(
        db.Integer, db.ForeignKey("workflow.id"), unique=False, nullable=False
    )
