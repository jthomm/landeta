# landeta
A SQLite database builder for NFL Game Center data

## Usage
Assuming the Game Center JSON object for game [2014092800](http://www.nfl.com/gamecenter/2014092800/2014/REG4/panthers@ravens) is stored in the file `gamecenter.json` in the current directory:

```sh
git clone https://github.com/jthomm/landeta.git ~/Projects/Github/landeta-master
python ~/Projects/Github/landeta-master/landeta.py -d mydatabase.sqlite3 -f gamecenter.json -g 2014092800
```

If the database `mydatabase.sqlite3` does not exist (or, more precisely, does not contain any objects), the script will create it for you and initialize all of the tables first.  It will then walk through the JSON object and insert the data.

### Bulk loading all the games
If you have a lot of Game Center files in the current directory, and each file is named after the Game Center ID of the game whose data it contains (e.g. "2014092800.json"), you can bulk load them quickly and efficiently using the following script:

```sh
for g in $(ls *.json | cut -d '.' -f -1);
do
  python ~/Projects/Github/landeta-master/landeta.py -d mydatabase.sqlite3 -f "${g}.json" -g ${g};
done
```

##Data model
The "data model" mirrors the bananas structure of the Game Center JSON object: highly non-normalized and often repetitive.  This script does not attempt to deal with any of that that, preferring to extract and load the data as-is.  (The idea is that transformation and data quality can be done via a series of SQL statements once the data is in a RDMS.)

![here it is](https://raw.githubusercontent.com/jthomm/landeta/master/gc.png)
