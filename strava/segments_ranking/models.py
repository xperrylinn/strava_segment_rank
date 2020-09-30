from django.db import models


class SegmentRank(models.Model):
    segment_name = models.CharField(200)
    segment_rank = models.IntegerField()
    segment_rank = models.IntegerField()
