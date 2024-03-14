-- Users Table
CREATE TABLE
  IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW (),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW ()
  );

-- Prompts Table
CREATE TABLE
  IF NOT EXISTS prompts (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    prompt TEXT NOT NULL,
    user_id INTEGER REFERENCES users (id),
    is_flagged BOOLEAN DEFAULT FALSE,
    is_validated BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW (),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW ()
  );

-- Likes Table
CREATE TABLE
  IF NOT EXISTS likes (
    user_id INTEGER REFERENCES users (id),
    prompt_id INTEGER REFERENCES prompts (id),
    PRIMARY KEY (user_id, prompt_id),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW (),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW ()
  );

-- Votes Table
CREATE TABLE
  IF NOT EXISTS votes (
    user_id INTEGER REFERENCES users (id),
    prompt_id INTEGER REFERENCES prompts (id),
    vote_type VARCHAR(50) CHECK (vote_type IN ('upvote', 'downvote', 'report')),
    PRIMARY KEY (user_id, prompt_id),
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW (),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW ()
  );