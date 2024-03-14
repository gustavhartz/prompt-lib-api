INSERT INTO
    users (username, email)
VALUES
    ('user1', 'user1@example.com'),
    ('user2', 'user2@example.com'),
    ('user3', 'user3@example.com'),
    ('user4', 'user4@example.com'),
    ('user5', 'user5@example.com') ON CONFLICT (username) DO NOTHING;

INSERT INTO
    prompts (
        title,
        description,
        prompt,
        user_id,
        is_flagged,
        is_validated
    )
VALUES
    (
        'The Lost Civilization',
        'Discover an ancient civilization untouched by time.',
        'You stumble upon...',
        (
            SELECT
                id
            FROM
                users
            WHERE
                username = 'user1'
        ),
        FALSE,
        TRUE
    ),
    (
        'Journey to the Center of Earth',
        'A daring adventure to the center of the earth begins.',
        'As you descend...',
        (
            SELECT
                id
            FROM
                users
            WHERE
                username = 'user1'
        ),
        FALSE,
        TRUE
    ),
    (
        'Life on Mars',
        'Imagine the first colony on Mars and its challenges.',
        'The red dust settles...',
        (
            SELECT
                id
            FROM
                users
            WHERE
                username = 'user2'
        ),
        FALSE,
        TRUE
    ),
    (
        'A.I. Uprising',
        'Artificial Intelligence has surpassed human intelligence.',
        'The machines woke up...',
        (
            SELECT
                id
            FROM
                users
            WHERE
                username = 'user3'
        ),
        FALSE,
        TRUE
    ),
    (
        'The Last Library',
        'In a future where books are banned, the last library stands.',
        'Hidden from the world...',
        (
            SELECT
                id
            FROM
                users
            WHERE
                username = 'user4'
        ),
        FALSE,
        TRUE
    );