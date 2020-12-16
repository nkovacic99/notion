from datetime import date
import datetime
from notion.client import NotionClient

token = '9254ab6068d2093cd44654916a31390ebff80f8e8b23b3651ea171bf4178bd256c966a86e6e0b754f631b5076dd9a585b4e0b3309dc254b1cb66679f34e9427bc4c9aa552f5cf6c03d23f8de287f'

client = NotionClient(token_v2=token)

PRITRDILNO = ["y", "Y", "", " "]
NEGATIVNO = ["n", "N"]

def set_date():
    bo_danes = input("Should the task be completed today? (y/n)\n")
    if bo_danes in PRITRDILNO:
        return date.today()
    elif bo_danes in NEGATIVNO:
        datum = input("Set the date (DD/MM/YYYY)\n")
        datum = datum.split("/")
        return datetime.date(int(datum[2]), int(datum[1]), int(datum[0]))

def set_name():
    return input("What should this task be called?\n")

def set_priority():
    PRIORITIES = ["🔥", "🔥🔥", "🔥🔥🔥"]
    input_priority =input("Priority level:\n1=🔥, 2=🔥🔥, 3=🔥🔥🔥\n")
    try:
        if int(input_priority) > 3 or int(input_priority) < 0:
            return "invalid"
        else:
            return PRIORITIES[int(input_priority) - 1]
    except ValueError:
        return "invalid"

def tasks():
    TASKS = 'https://www.notion.so/c3c6fefa597e4c5a87ee969c32e83e16?v=98b92b4d83d5402a9504b9024f0896c3'
    cv = client.get_collection_view(TASKS)
    new_task = cv.collection.add_row()
    # sets the "Done" checkbox to unchecked
    new_task.Done = False
    new_task.Name = set_name()
    new_task.Priority = set_priority()
    date = set_date()
    new_task.Date = date
    new_task.Day = date.strftime("%A")
    while input("Continue?(y/n)\n") in PRITRDILNO:
        new_task = cv.collection.add_row()
        # sets the "Done" checkbox to unchecked
        new_task.Done = False
        new_task.Name = set_name()
        new_task.Priority = set_priority()
        date = set_date()
        new_task.Date = date
        new_task.Day = date.strftime("%A")

def main():
    tasks()

main()

