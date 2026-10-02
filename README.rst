Faker Demo
----------
A demo of the Faker module, which generates realistic data such as names, emails, and date of births.

Installation
------------
Faker is not part of the standard library, so install it with pip::
    
  pip install faker

Download or clone this repository, extract it if it is a ZIP file, open a terminal in the project folder, then run the demo script::

    python demo.py

What the demo does
------------------
    * Prints five fake students with a name, email, date of birth, sex, and race/ethnicity.
    * Prints three rows formatted as SQL INSERT values.

Example output
--------------
Running the demo prints output like this. The seed makes the results repeatable, so you should see the same output::

    Five fake students
    Alexander Hill donaldgarcia@example.net 1971-09-01 Male Middle Eastern or North African
    Amanda Davis williamjohnson@example.org 1994-04-20 Female Middle Eastern or North African
    Jerry Ramirez blakeerik@example.com 1984-08-29 Male Hispanic or Latino
    Daniel Gallagher daviscolin@example.com 1983-10-02 Male Middle Eastern or North African
    Nicholas Herrera smiller@example.net 1990-05-12 Male Middle Eastern or North African
    Three SQL rows
    ('Michael', 'Williams', 'kendragalloway@example.org', 'White', 'Male'),
    ('Jody', 'Flowers', 'mitchellclark@example.com', 'White', 'Female'),
    ('Joseph', 'Sanchez', 'ogray@example.net', 'Middle Eastern or North African', 'Male'),

Requirements
------------
Python 3 or newer.
Tested with Python 3.14 and Faker 40.40.0.

Notes
-----
* Sex and race/ethnicity are assigned randomly so the data does not reflect real population percentages.
* Email addresses are generated independently of the names, so they do not match. 
