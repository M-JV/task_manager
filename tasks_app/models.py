from django.db import models


# Category Table
class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    # to return name when object is printed
    def __str__(self):
        return self.name

    # Making the name in admin panel from Categorys to Categories
    class Meta:
        verbose_name_plural = 'Categories'

# Task Table
class Task(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)

    STATUS_CHOICE = [
        ('Pending','Pending'),
        ('In Progress','In Progress'),
        ('Completed','Completed'),
    ]

    status = models.CharField(max_length=15, choices=STATUS_CHOICE, default='Pending')


    PRIORITY_CHOICE = [
        ('Low','Low'),
        ('Medium','Medium'),
        ('High','High'),
    ]

    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICE, default='High')

    # Foreign Key to link tasks to a category
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='tasks')


    # to return the title when object is printed
    def __str__(self):
        return self.title

