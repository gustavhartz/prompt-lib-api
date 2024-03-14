-- init_db.sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE prompts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    prompt TEXT NOT NULL,
    user_id INTEGER REFERENCES users(id),
    is_flagged BOOLEAN DEFAULT FALSE,
    is_validated BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE likes (
    user_id INTEGER REFERENCES users(id),
    prompt_id INTEGER REFERENCES prompts(id),
    PRIMARY KEY (user_id, prompt_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE votes (
    user_id INTEGER REFERENCES users(id),
    prompt_id INTEGER REFERENCES prompts(id),
    vote_type VARCHAR(50) CHECK (vote_type IN ('upvote', 'downvote', 'report')),
    PRIMARY KEY (user_id, prompt_id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Note: PostgreSQL before version 12 does not support the ON UPDATE CURRENT_TIMESTAMP syntax.
-- You might need to create a trigger to update the updated_at field or manually update it in your application logic.
