polymersim:
	python3 polymersim.py polymer.csv

plot-polymersim: polymersim
	gnuplot -e "filename='polymer.csv'" -p plotrandomwalk.gnuplot
