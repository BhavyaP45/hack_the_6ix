DROP TABLE IF EXISTS announcements;
DROP TABLE IF EXISTS tasks;
CREATE TABLE announcements (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    announcementText TEXT NOT NULL
);


CREATE TABLE tasks(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    descriptionText TEXT NOT NULL,
    subTaskOne TEXT NOT NULL,
    subTaskTwo TEXT NOT NULL
);