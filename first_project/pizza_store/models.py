from django.db import models


class Pizza(models.Model):
    pizza_name = models.CharField(max_length=200)
    cooked_date = models.DateTimeField('date cooked')
    slices = models.IntegerField(default=8)

    def __str__(self):
        return "I'm a %s pizza, and I have %d slices" % (self.pizza_name, self.slices)

    def how_many_slices(self):
        if self.slices > 4:
            return 'a lot!'
        return 'Not enough :('


class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    topping_name = models.CharField(max_length=200)
