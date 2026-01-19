CREATE TABLE IF NOT EXISTS classes (
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS names (
  id SERIAL PRIMARY KEY,
  value TEXT NOT NULL,
  class_id INTEGER NOT NULL REFERENCES classes(id) ON DELETE RESTRICT,
  CONSTRAINT uq_name_per_class UNIQUE (class_id, value)
);

CREATE INDEX IF NOT EXISTS idx_names_class_id ON names(class_id);
