from django.db import models

class Table1(models.Model):
    id = models.CharField(primary_key=True, max_length=10)
    question_text = models.CharField(max_length=200, blank=True, null=True)
    pub_data = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'table1'


class Table2(models.Model):
    question = models.ForeignKey(Table1, models.DO_NOTHING, db_column='question', blank=True, null=True)
    choice_text = models.CharField(max_length=200, blank=True, null=True)
    votes = models.CharField(max_length=10, blank=True, null=True)    

    class Meta:
        managed = False
        db_table = 'table2'