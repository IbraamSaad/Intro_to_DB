SELECT 
    b.book_id, b.title, b.author_id, b.price, b.publication_date, c.COLUMN_NAME
FROM
    books b
JOIN
    INFORMATION_SCHEMA.COLUMNS c
ON
    b.book_id = c.COLUMN_NAME
WHERE
    c.TABLE_SCHEMA = 'alx_book_store'
    AND c.TABLE_NAME = 'books';
