from django.utils.functional import cached_property

class myModel(Model):
	# Model definition...

	@cached_property
	def fullName(self):
		return self.first_name + self.last_name


from django.db import models

class Topping(models.Model):
    name = models.CharField(max_length=30)

class Pizza(models.Model):
    name = models.CharField(max_length=50)
    toppings = models.ManyToManyField(Topping)

    def __str__(self):              # __unicode__ on Python 2
        return "%s (%s)" % (self.name, ", ".join(topping.name
                                                 for topping in self.toppings.all()))


# >>> Pizza.objects.all().prefetch_related('toppings')
# >>> pizza_count = len(Pizza.objects.all())






		