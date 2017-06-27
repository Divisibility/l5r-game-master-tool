Legend of the Five Rings - Game Master Tool
===========================================

Legend of the Five Rings - Game Master Tool (l5r-gmt) provides the
game master with a character generator for PCs and NPCs. It also has
the capability to manage every generated character and add notes to
them.

Setup
-----

Install required python packages:

	pip install -r requirements.txt

Create the sqlite3 database:

       sqlite3 gmt.sqlite < data/setup.sql

Run the game master tool:

    python run.py