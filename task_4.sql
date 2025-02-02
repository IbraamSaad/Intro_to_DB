USE alx_book_store;

SELECT 
    book_id INT PRIMARY KEY AUTO_INCREMENT, -- Added AUTO_INCREMENT
    title VARCHAR(130) NOT NULL,
    author_id INT,
    price DOUBLE,
    publication_date DATE,
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
FROM
    books;