from django.db import models
from master_app.models import TimeStampedModel
from master_app.stub_models import User


class Plan(TimeStampedModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    status = models.BooleanField(default=False)

    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="added_plan")
    updated_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="updated_plan")

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = "plan"
        verbose_name = "Plan"
        verbose_name_plural = "Plans"


