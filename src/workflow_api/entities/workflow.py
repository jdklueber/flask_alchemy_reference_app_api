from workflow_api.entities.base import Base
from typing import List
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Workflow(Base):
    __tablename__ = "workflow"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    desc: Mapped[str] = mapped_column(String(255))
    workflow_items: Mapped[List["WorkflowItems"]] = relationship()

    def __repr__(self):
        return f"<Workflow> id: {self.id} name: {self.name} " f"desc: {self.desc}"


class WorkflowItems(Base):
    __tablename__ = "workflow_items"
    id: Mapped[int] = mapped_column(primary_key=True)
    workflow_id: Mapped[int] = mapped_column(ForeignKey("workflow.id"))
    name: Mapped[str] = mapped_column(String(50))
    desc: Mapped[str] = mapped_column(String(255))

    def __repr__(self):
        return (
            f"<ChecklistItem> id: {self.id} checklist_id: {self.workflow_id} "
            f"name: {self.name} desc: {self.desc} "
        )
