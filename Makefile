main: 
	echo "Nothing"

imdb:
	python easy_parser.py imdb.json imdb.csv -d ../foo_html_pages/IMDB_html

rotten:
	python easy_parser.py rotten.json rotten.csv -d ../foo_html_pages/rottentomatoes_html

push:
	git add .
	git commit -m "testcsv"
	git push