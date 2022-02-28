INSERT INTO beach (name) VALUES
    ('Sunny Beach'),
    ('Sandy Shorline'),
    ('Surf-and-Sand'),
    ('this beach is trash'),
    ('Stay Away!');

INSERT INTO beach_image (beach_id, url) VALUES
    (1, 'url-1'),
    (1, 'url-2'),
    (2, 'url-3'),
    (2, 'url-4'),
    (3, 'url-5'),
    (3, 'url-6'),
    (4, 'url-7'),
    (4, 'url-8'),
    (5, 'url-9'),
    (5, 'url-10');

INSERT INTO beach_comment (beach_id, user_id, comment) VALUES
    (1, 'beachgoer', 'this is a great beach!'),
    (1, 'ALICE', '@user-1 I will check it out.'),
    (1, 'beachgoer', 'you should!'),
    (4, 'bob', 'lives up to the name'),
    (5, 'eve', 'dangerous, stay away');

INSERT INTO beach_rating (beach_id, user_id, rating) VALUES
    (1, 'user-1', 5),
    (1, 'user-2', 5),
    (2, 'user-1', 4),
    (2, 'user-2', 4),
    (3, 'user-1', 5),
    (3, 'user-2', 4),
    (4, 'user-1', 2),
    (4, 'user-2', 2),
    (5, 'user-1', 1),
    (5, 'user-2', 1);