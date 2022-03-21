-- Genres: Children's Film, Comedy, Animation, Action, Adventure, Fantasy

    INSERT INTO Customer(customer_id, customer_name, customer_email)
    VALUES('sare_bear', 'Sarah', 'testemail0@purdue.edu');

    INSERT INTO Customer(customer_id, customer_name, customer_email)
    VALUES('noops','Nupur', 'testemail1@purdue.edu');

    INSERT INTO Customer(customer_id, customer_name, customer_email)
    VALUES('chiquita', 'Nikita', 'testemail2@purdue.edu');

    INSERT INTO Customer(customer_id, customer_name, customer_email)
    VALUES('soops', 'Sahana', 'testemail3@purdue.edu');

    INSERT INTO Movie(movie_id, movie_name, genre, director_name, rating, cast_list)
    VALUES(1, "Madagascar", "Children's Film, Comedy, Animation",
    'Tom McGrath, Eric Darnell', 4.9, 'Ben Stiller, Chris Rock, David Schwimmer, Jada Pinkett Smith');

    INSERT INTO Movie(movie_id, movie_name, genre, director_name, rating, cast_list)
    VALUES(3, "Madagascar: Escape 2 Africa", "Children's Film, Comedy, Animation",
    'Tom McGrath, Eric Darnell', 4.9, 'Ben Stiller, Chris Rock, Alec Baldwin, Jada Pinkett Smith');

    INSERT INTO Movie(movie_id, movie_name, genre, director_name, rating, cast_list)
    VALUES(2, "Madagascar 3: Europe's Most Wanted", "Children's Film, Comedy, Animation",
    'Tom McGrath, Eric Darnell', 4.9, 'Ben Stiller, Chris Rock, Alec Baldwin, Jada Pinkett Smith');

    INSERT INTO Store(store_id, zip_code, location_name)
    VALUES(1, "55598", "Los Angeles, CA");

    INSERT INTO Store(store_id, zip_code, location_name)
    VALUES(2, "55200", "Fremont, CA");

    INSERT INTO Store(store_id, zip_code, location_name)
    VALUES(3, "52034", "San Francisco, CA");

    INSERT INTO Catalog(movie_id, store_id, total_quantity, quantity_available, times_rented)
    VALUES(1, 2, 10, 3, 8);

    INSERT INTO Catalog(movie_id, store_id, total_quantity, quantity_available, times_rented)
    VALUES(3, 2, 10, 10, 2);

    INSERT INTO Catalog(movie_id, store_id, total_quantity, quantity_available, times_rented)
    VALUES(3, 1, 1, 1, 50);

    INSERT INTO Catalog(movie_id, store_id, total_quantity, quantity_available, times_rented)
    VALUES(3, 3, 4, 2, 10);

    INSERT INTO Catalog(movie_id, store_id, total_quantity, quantity_available, times_rented)
    VALUES(2, 3, 5, 4, 1);