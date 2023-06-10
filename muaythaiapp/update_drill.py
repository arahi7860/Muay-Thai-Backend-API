from muaythaiapp.models import TrainingDrill

def update_drills_with_ids(drills_data):
    existing_drills = TrainingDrill.objects.all()

    for drill_data in drills_data:
        # Find the corresponding existing training drill
        existing_drill = existing_drills.get(name=drill_data['name'])

        # Update the data with the existing drill's ID
        drill_data['id'] = existing_drill.id

    return drills_data
