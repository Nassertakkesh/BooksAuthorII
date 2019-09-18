from django.db import models

class Books(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Book object: {self.title} {self.desc}({self.id})>"


class Authors(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    notes = models.TextField()
    books = models.ManyToManyField(Books, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #  Books.objects.create(title="Java", desc="a book about java")
    def __repr__(self):
        return f"<Authors object:({self.id}) {self.first_name} ({self.last_name})>"
# this_book = Books.objects.get(id=5)	# retrieve an instance of a book
# this_author = Authors.objects.get(id=5)	# retrieve an instance of a publisher
# this_author.books.add(this_book)	