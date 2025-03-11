def add_genres():
    from apps.books.models import BookGenre

    # add genres
    arr = [
        "Engineering & Technology",
        "Law",
        "Medical & Health Sciences",
        "Mathematics",
        "Computer Science & IT",
        "Physics & Chemistry",
        "Social Sciences",
        "Language & Linguistics",
        "Economics & Finance",
        "Research & Journals",
    ]
    genres = [BookGenre(name=genre) for genre in arr]
    BookGenre.objects.bulk_create(genres)
