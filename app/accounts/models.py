import os

from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User)
    title = models.CharField(max_length=100)


def upload_path(self, filename):
    return "%d/%s" % (self.user.pk, filename)


class UploadedFile(models.Model):
    FILETYPE_CHOICES = (
        ('P', 'Picture'),
        ('A', 'Audio'),
        ('V', 'Video'),
    )
    user = models.ForeignKey(User, related_name="files")
    file_type = models.CharField(max_length=1, choices=FILETYPE_CHOICES, default='P')
    upload = models.FileField(upload_to=upload_path)
    upload_dt = models.DateTimeField(auto_now_add=True)

    def filename(self):
        return os.path.basename(self.upload.name)


# These two auto-delete files from filesystem when they are unneeded:
@receiver(models.signals.post_delete, sender=UploadedFile)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `UploadedFile` object is deleted.
    """
    if instance.upload:
        if os.path.isfile(instance.upload.path):
            os.remove(instance.upload.path)

@receiver(models.signals.pre_save, sender=UploadedFile)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `UploadedFile` object is changed.
    """
    if not instance.pk:
        return False

    try:
        old_file = UploadedFile.objects.get(pk=instance.pk).upload
    except UploadedFile.DoesNotExist:
        return False