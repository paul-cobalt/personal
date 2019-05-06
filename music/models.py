import os
from datetime import datetime

from django.db import models
from django.utils.safestring import mark_safe
import markdown2

from website.settings import BASE_DIR


def convert_name_to_directory_format(name):
    """Returns human-readable names to a format that is friendlier for Unix directories."""
    name = name.lower()
    return name.replace(" ", "_")


class Musician(models.Model):
    """Represents one musician or band."""
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(db_index=True,
                                      auto_now=True,  # Updates each time save() is called
                                      )

    name = models.CharField(max_length=100, unique=True)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.name


class Music(models.Model):
    """Represents one album or piece of music."""
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(db_index=True,
                                      auto_now=True,  # Updates each time save() is called
                                      )
    album_released_date = models.DateTimeField(null=True, blank=True)
    reviewed_at = models.DateTimeField(default=datetime.now)

    name = models.CharField(max_length=200)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    rating = models.SmallIntegerField()

    album_of_the_month = models.BooleanField(default=False)

    def __str__(self):
        return str(self.musician) + ": " + str(self.name)

    def review(self):
        path_to_review = os.path.join(BASE_DIR,
                                      'music/reviews/',
                                      convert_name_to_directory_format(self.musician.name),
                                      convert_name_to_directory_format(self.name) + '.md')
        try:
            with open(path_to_review, encoding='utf-8') as review_file:
                review_as_markdown = review_file.read()
        except IOError:
            return None

        review_as_html = markdown2.markdown(review_as_markdown)
        # We mark this as safe because we want Django to render it as HTML. This is obviously safe since I am going to
        # be the one writing the markdown. :)
        return mark_safe(review_as_html)

    def image_src(self):
        path = os.path.join('music', 'images', convert_name_to_directory_format(self.musician.name),
                            convert_name_to_directory_format(self.name) + '.jpg')
        if os.path.exists(os.path.join(BASE_DIR, 'music/static', path)):
            return path
        else:
            return None


class Tag(models.Model):
    """Encapsulates a tag that can be applied to musicians to classify their work."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
