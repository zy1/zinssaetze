#!/usr/bin/python

for line in open("watchlist.csv").readlines():
	entries = [ e.replace("\"", "").replace(",", ".").replace for e in line.split(";") ]
	if len(entries) == 0: continue
	if entries[0] != "Aktien": continue
	entries[3]

	print entries[2], entries[3], entries[5], entries[9], entries[10]

