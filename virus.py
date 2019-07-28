#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
from hashlib import md5
from virus_total_apis import PublicApi
def analizar():
	API_KEY = "a9089095456a6c812626239b837c894abcea66938853813118ebf16a5fff1690"
	api = PublicApi(API_KEY)
	with open(sys.argv[1], "rb") as f:
		file_hash = md5(f.read()).hexdigest()
	response = api.get_file_report(file_hash)
	if response["response_code"] == 200:
		if response["results"]["positives"] > 0:
			print("Archivo malicioso.")
		else:
			print("Archivo seguro.")
	else:
		print("No ha podido obtenerse el análisis del archivo.")

if __name__ == "__main__":
	analizar()