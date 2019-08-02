from django.db import models

class FoodData(models.Model):
    name                 = models.TextField(blank=True, null=True)
    calorie              = models.FloatField(blank=True, null=True)
    lipid                = models.FloatField(blank=True, null=True)
    calcium              = models.FloatField(blank=True, null=True)
    vitamina             = models.FloatField(db_column='vitaminA', blank=True, null=True)  # Field name made lowercase.
    vitaminb1            = models.FloatField(db_column='vitaminB1', blank=True, null=True)  # Field name made lowercase.
    vitaminc             = models.FloatField(db_column='vitaminC', blank=True, null=True)  # Field name made lowercase.
    saturated_fatty_acid = models.FloatField(blank=True, null=True)
    protein              = models.FloatField(blank=True, null=True)
    carbohydrate         = models.FloatField(blank=True, null=True)
    iron                 = models.FloatField(blank=True, null=True)
    vitamine             = models.FloatField(db_column='vitaminE', blank=True, null=True)  # Field name made lowercase.
    vitaminb2            = models.FloatField(db_column='vitaminB2', blank=True, null=True)  # Field name made lowercase.
    dietary_fiber        = models.FloatField(blank=True, null=True)
    salt                 = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name
        
    class Meta:
        managed = False
        db_table = 'food_data'
