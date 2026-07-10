CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,

    username VARCHAR(50) NOT NULL UNIQUE,

    email VARCHAR(255) NOT NULL UNIQUE,

    hashed_password VARCHAR(255) NOT NULL,

    created_at TIMESTAMP NOT NULL
        DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE books (
    id INT AUTO_INCREMENT PRIMARY KEY,

    api_id VARCHAR(50) UNIQUE,

    source ENUM('OpenLibrary', 'Manual') NOT NULL,

    title VARCHAR(255) NOT NULL,

    author VARCHAR(255) NOT NULL,

    description TEXT,

    cover_url VARCHAR(500),

    publication_year YEAR,

    total_pages INT,

    total_chapters INT,

    total_volumes INT,

    created_at TIMESTAMP NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP NOT NULL
        DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE library (
    id INT AUTO_INCREMENT PRIMARY KEY,

    user_id INT NOT NULL,

    book_id INT NOT NULL,

    status ENUM(
        'Want to Read',
        'Reading',
        'Re-reading',
        'On Hold',
        'Read',
        'Dropped'
    ) NOT NULL,

    rating INT
        CHECK (rating BETWEEN 1 AND 10),

    current_pages INT,

    current_chapters INT,

    current_volumes INT,

    re_read_count INT NOT NULL
        DEFAULT 0,

    added_at TIMESTAMP NOT NULL
        DEFAULT CURRENT_TIMESTAMP,

    updated_at TIMESTAMP NOT NULL
        DEFAULT CURRENT_TIMESTAMP
        ON UPDATE CURRENT_TIMESTAMP,

    UNIQUE (user_id, book_id),

    CONSTRAINT fk_library_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE,

    CONSTRAINT fk_library_book
        FOREIGN KEY (book_id)
        REFERENCES books(id)
        ON DELETE CASCADE
);