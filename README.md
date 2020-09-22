Install dependencies

pip install csv
pip install requests
pip install re
pip install datetime
pip install beautifulsoup4

Run the python script to scrape avid gym counter and put data into a csv

Run the shell script if you want to put the csv into a database, remember to change $home with the directory path

You can run the shell script as a cronjob as well

*/5 * * * * ./path/to/script/cronjob
