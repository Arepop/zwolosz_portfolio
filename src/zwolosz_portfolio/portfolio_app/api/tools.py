

def update_mutation(instance, model, kwargs):
    for key, value in kwargs.items():
        if not getattr(model, key).field.null:
            setattr(instance, key, value)
    instance.save()