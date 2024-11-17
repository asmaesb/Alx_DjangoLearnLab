from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request):
    # Logic to edit a book
    pass