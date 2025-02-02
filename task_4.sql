USE alx_book_store;

SELECT 
    book_id, title, author_id, price, publication_date
    INT, VARCHAR, INT, DOUBLE, DATE
    NOT NULL, NULL, NULL, NULL, NULL
    PRIMARY KEY
    FOREIGN KEY
FROM
    Books.COLUMNS
WHERE
    TABLE_SCHEMA = alx_book_store()
    AND TABLE_NAME = 'books';
