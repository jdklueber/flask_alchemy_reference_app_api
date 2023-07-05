from sqlalchemy import create_engine
from workflow_api.entities.base import Base
from workflow_api.entities.workflow import Workflow, WorkflowItems
from workflow_api.entities.checklist import Checklist, ChecklistItems

# Making some hard coded effort here to test out how the ORM works
data_file = r"/C:\data\test.db"
engine = create_engine(f"sqlite://{data_file}", echo=True)
# Base.metadata.create_all(engine)
# print(Base.metadata.tables)


def main():
    print("Hello, world")
