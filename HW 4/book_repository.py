books = [
    {
        'ID': 1,
        'name': 'War and Peace',
    },
    {
        'ID': 2,
        'name': 'Crime and Punishment',
    },
    {
        'ID': 3,
        'name': 'Anna Karenina',
    },
    {
        'ID': 4,
        'name': 'The Master and Margarita',
    },
]


def fetch_books(book_id: int | None = None):
    if book_id:
        return filter(lambda book: book.ID == book_id, books)
    return books