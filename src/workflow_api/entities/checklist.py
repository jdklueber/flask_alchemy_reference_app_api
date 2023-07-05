from workflow_api.entities.base import Base
from typing import List
from sqlalchemy import String, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Checklist(Base):
    __tablename__ = "checklist"
    id: Mapped[int] = mapped_column(primary_key=True)
    workflow_name: Mapped[str] = mapped_column(String(50))
    workflow_desc: Mapped[str] = mapped_column(String(255))
    identifier: Mapped[str] = mapped_column(String(50))
    archived: Mapped[bool] = mapped_column(Boolean)
    checklist_items: Mapped[List["ChecklistItems"]] = relationship()

    def __repr__(self):
        return (
            f"<Checklist> id: {self.id} workflow_name: {self.workflow_name} "
            f"workflow_desc: {self.workflow_desc} identifier: {self.identifier} "
            f"archived: {self.archived}"
        )


class ChecklistItems(Base):
    __tablename__ = "checklist_items"
    id: Mapped[int] = mapped_column(primary_key=True)
    checklist_id: Mapped[int] = mapped_column(ForeignKey("checklist.id"))
    name: Mapped[str] = mapped_column(String(50))
    desc: Mapped[str] = mapped_column(String(255))
    done: Mapped[bool] = mapped_column(Boolean)

    def __repr__(self):
        return (
            f"<ChecklistItem> id: {self.id} checklist_id: {self.checklist_id} "
            f"name: {self.name} desc: {self.desc} "
            f"done: {self.done}"
        )
