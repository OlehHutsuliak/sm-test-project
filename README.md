Project was created to download an ebook from salesmanago.pl page and then make sure that correct file was downloaded.

Before running Tests, parametrize it

In case, when you run Tests from console: Use created option '--book' with a name of book, which you want to download. (List of books is added to project directory).

!!! Don't forget about double quotes symbols ("") !!!

example: pytest -v -s --book="Engagement Marketing" download_book.py

In case, when you run Tests from IDE: Change a value of 'book_option' variable (default=None).

example: book_option = "Engagement Marketing"
