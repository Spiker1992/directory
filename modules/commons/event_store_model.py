from django.db import models

class EventStoreModel(models.Model):
    event_type = models.CharField(max_length=50)
    event_payload = models.JSONField()
    stream_id = models.UUIDField(editable=False, blank=False, null=False)
 
    def save(self, *args, **kwargs):
       if not self._state.adding:
           return
       
       super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        Delete the model instance from the database.
        """
        pass

    class Meta:
        abstract = True