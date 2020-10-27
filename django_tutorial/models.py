from django.db import models

# Create your models here.


class Bear(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return "name: {name}, age: {age}".format(name=self.name, age=self.age)


class PicnicBasket(models.Model):
    sandwiches = models.BooleanField()
    bear = models.ForeignKey(Bear, related_name='picnicbaskets', on_delete=models.CASCADE)

class Language(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Framework(models.Model):
    name = models.CharField(max_length=10)
    language = models.ForeignKey(Language, related_name='Frameworks', on_delete=models.CASCADE)

    def __str__(self):
        return self.name















    # objects = BearManager()




    # class Meta:
    #     unique_together = [["name", "age"]]

    # def natural_key(self):
    #     return (self.name, self.age)


    # def __str__(self):
    #     return  "id": str(self.id) "Sandwiches": str(self.sandwiches) 
        # return  "id: " + str(self.id) + ", Sandwiches: " + str(self.sandwiches)



# class BearManager(models.Manager):
#     def get_by_natural_key(self, name, age):
#         return self.get(name=name, age=age)