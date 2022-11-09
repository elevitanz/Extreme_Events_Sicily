# Extreme_Events_Sicily
The repository contains the code used in the paper: "A multi-modal machine learning approach to detect Extreme Rainfall Events in Sicily", Vitanza et al. Please cite the paper when using the code.

Data have been obtained thanks to the kind permission of SIAS: "Servizio Informativo Agrometeorologico Siciliano".

Below a detailed description of the repository:
- In the 'preprocessing' folder you will find a script with the stations selection
  procedure.

  After the excel table was created, we selected all the stations with more than three years
  resulting "True" from the algorithm, plus the provincial capitals. 

  At the end of the work we re-run the algorithm including the 2021 data and computing by hand the
  annual variables starting from the 10-minutes records. This brought to different results, maybe
  due to some inaccuracy. For this reason we decided to mantain the common results between the two
  procedures, so that there are 4 stations that we did not consider: Canicattì, Castellammare,
  Calatafimi, Lentini.

- In the 'clustering' folder we report the clustering algorithms applied in both the geographical
  ('geo_cl_to_excel' folder) and temporal ('temp_cl_to_excel' folder) settings. 
  We also report the transition of geographical clusters into the Sicily map ('geo_cl_to_map'
  folder).
Note: unzip the files in the 'global_stations' folder.

	- In the 'geo_cl_to_excel' folder we report the geographical clustering scripts.
	  Both the Euclidean and Correlation metrics were used. 
	  In the case of Euclidean distance and C. A, we have several levels, as reported
	  in the paper. For this reason we collect all the levels in new complete excel files.
	  In any case, all the results are excel files with the different obtained
	  clusters.

	- In the 'geo_cl_to_map' folder we report the script transforming the excel clusters files
	  (created in the scripts of the 'geo_cl_to_excel' folder) into clusters located in the
	  Sicily map. In the 'sicilia' subfolder there are the necessary files to plot the Sicily
	  map by using 'Geopandas'. The 'anomalies_by_stations.py' file plots the final Sicily map
	  in the global case reporting the counters of anomalies by stations.

	- In the 'temp_cl_to_excel' folder we report the scripts related to the temporal
	  clustering. Both the Euclidean and Correlation metrics were used.
	
	- The scripts "annual_mean_stations.py", "mean_stations.py" and "glow_years.py" let to create the "annual_mean_stations", "mean_stations" and
	  "global_stations" folders, respectively.

- In the 'statistical validation' folder we report the Kruskal-Wallis implementation
  ('kruskal_wallis' folder) and the scripts related to the indicators histograms both temporal-
  based ('temp_cl_histograms') and geographical-based ('geo_heatmaps').

	- In the 'excel_recap' folder we group indicators and clusters in single excel files, in
	  order to plot the indicators histograms. Here we also add in any excel file an
	  'intensity' and a 'wet hours' column.
	
	- In the 'geo_heatmaps' folder we report the scripts related to the computation of
	  indicators and the related heatmaps (we report in the 'results' folder the heat-maps of
	  only two indicators, but the algorithm works with any indicator).

	- In the 'temp_cl_histograms' folder we report the scripts related to year-by-year
	  anomalies histograms, as well as to the heavy rain mean histograms.

	- In the 'kruskal_wallis' folder we report the scripts of the Kruskal-Wallis algorithm and
	  the relative p values obtained in all the cases.

- In the 'SI' folder we report the scripts related to the SI document.
	
	- In the 'stations' folder we report the Augusta 10-minutes-frequency records.
	  No other station was loaded due to memory constraints, but we have similar data of other
	  33 stations (the so-called Collection A in the paper).

	- In the 'initial_histograms' folder we report the python codes of some initial station
	  analysis: Catania, Messina, Palazzolo Acreide, Palermo, Siracusa, Trapani Fontanasalsa

	- In the 'augusta_full_view' folder we report the codes for the global temporal view of
	  Augusta data, both with the original records and with the weekly means.
	  We considered Augusta as an example, but we could do the same for any rain gauge.

	- In the 'augusta_annual_view' folder we report the codes for the annual temporal view of
	  Augusta data. The scripts will create several images: take the last one as the most up
	  to-date, involving all the months of the considered year. We considered Augusta as an
	  example, but we could do the same for any rain gauge. Change the annual file in input to
	  have the annual view of other years. Use the 'annual_bis.py' script for leap years,
	  namely: 2012, 2016, 2020. The scripts will create several images: take the last one as
	  the most up-to-date, involving all the months of the year.

	- In the 'augusta_monthly_view' folder we report the codes for the monthly temporal view
	  of Augusta data. We considered Augusta as an example, but we could do the same for any
	  rain gauge. Change the annual file in input to have the monthly view of other years. Use
	  the 'monthly_bis.py' script for leap years, namely: 2012, 2016, 2020.
	
	- All the annual clustering results reported in the SI document are available in the
	  'clustering' folder above.
	  
REQUIREMENTS: 
- Python programming language (V. 3)
- Scikit-learn library (V. 1.0.2)
- NumPy (V. 1.21.4)
- SciPy (V. 1.8.0)
- Pandas (V. 1.3.5)
- Matplotlib (V. 3.5.1)
- Geopandas (V. 0.10.2)
- os
