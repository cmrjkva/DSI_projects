# Fire Risk Prediction Analysis

### Project 5: A group project focused on prediction of fire risk based on meteorological data.

## Table of contents
* [Tech Stack](###Tech-Stack)
* [Problem Statement](###Problem-Statment)
* [Summary](###Summary)
* [Data](###Data)
* [Modeling](###Modeling)
* [Conclusions](###Conclusions)
* [Recommendations](###Recommendations)
* [Next Steps](###Next-Steps)

----------
### Tech Stack
This Project is created with:
* Amazon AWS S3
* Amazon CLI
* Boto3
* Matplotlib
* Mpl_toolkits
* Python3
* Seaborn
* Sklearn
* Sqlite
* Statsmodels
* Streamlit
* Tensorflow

---------
### Problem Statement

This project uses weather data in a classification model to determine which of the Western US states are at high risk of large fires, in order to improve local preparedness.

![](/visuals/fire_size_vs_temp_precip_by_month.png)

--------
### Summary

Our project focused on the following 11 States in the US: 
|States| | 
|---|---|
|Arizona|Montana |
|California|New Mexico |
|Colorado|Nevada|
|Idaho|Utah |
|Oregon|Washington |
|Wyoming||

2020 was the most active fire season in the Western United States’s recorded history. California had the single worst fire season in it’s history, while Arizona had the worst in a decade. Oregon had its most destructive fire season meanwhile Washington and Colorado had several of their all time largest wildfires. Overall 10.2 million acres of land went up in flame and 46 people lost their lives. 13,887 buildings were destroyed and the total cost is upwards of 19.88 billion USD. It is evident that fire is a clear and present danger in the western united states. 

The global atmospheric monitoring satellite Copernicus has recorded CO2 emissions from the 2020 fires and noted that “The fires are also emitting lots of smoke and pollution into the atmosphere; those in California and Oregon have already emitted far more carbon in 2020 than in any other year since CAMS records begin in 2003” - [CAMS monitors smoke release from devastating US wildfires | Copernicus](https://atmosphere.copernicus.eu/cams-monitors-smoke-release-devastating-us-wildfires). We decided to investigate the relationship between weather data (precipitation, temperatures, and drought) and the occurrence of fires, and to attempt building a model which would predict the destructive sizes of wildfire to help prevent the associated damage for our communities.

Following National Wildfire Coordinating Group's convention which groups fires into ranges of fire size based on the number of acres within the final fire perimeter, we chose to set up our model as a a multi-classification where class "A" corresponds to fires smaller than 0.01 acres, "B" - 0.225 acres, "C" - 10 acres, "D" - 100 acres , "E" - 300 acres , "F" - 1000 acres, and "G" - fires larger than that.

----------------
### Data

We used two sources of data which were studied through EDA and then combined into a single data frame which informed the modeling phase:
- Meteorological dataset covering 120 years of weather information for the 11 western US states of: AZ, CA, CO, ID, NM, NV, MT, OR, UT, WA, and WY, including metrics and indexes describing precipitation, temperatures, and droughts;
- A spatial database of 1.88 million wildfires that occurred in the United States from 1992 to 2015 and burned 140 million acres burned during the 24-year period. This data was originally generated to support the national Fire Program Analysis (FPA) system and is currently obtainable from Kaggle.com. The data set includes: discovery date, final fire size, and a point location (latitude and longitude) among many other features.

The two datasets were combined by matching weather information and fire data on the combination of month-year-state for each of the fires that burned from 1992 to 2015 in the eleven states of interest. Due to the cumulative nature of meteorological affects on drought severity, we chose to include drought, temperature and precipitation trailing averages over 12-, 9-, 6-, and 3-months.

We also took a deep dive into NOAA wind data but discovered that the combined datasets were far too large to add to our existing dataframe.  Wind direction is a great weather predictor, and because wind speed can feed fires, we believe that adding wind data, such as wind speed, gusts and potentially wind direction would have added significant value to our models.

Another interesting data set we encountered was foliage data from Google Earth Engine. This required setting up an account with Google and being accepted to use their engine, and then exploring data using Javascript. It became too cumbersome for our efforts.

![](/visuals/fire_size_vs_temp_precip_by_month.png)

---------
### Modeling

The project ultimately uses two main models. Neural network for predictive power and Random Forest Classifier for feature importance. We optimized the neural network on recall score focusing on true positive rate and capturing large fires over small fires. Large fires being more destructive and being more in line with the scope of the project at the expense of smaller fires. The final chosen neural network model topology optimizes recall over accuracy. When we focused on accuracy, we were predicting the majority class (small fires) over the minority (large fires) which missed the most destructive wildfires. 

To improve our models, we employed the modeling technique of bootstrapping which gave us a more normal distribution of wildfire classes. This way, we were able to capture our larger fires. It greatly improved recall which is ultimately the target we wanted to pursue, as this helped us predict  larger and more destructive wildfires. 

The second modeling breakthrough we had was harnessing geospatial data through KMeans clustering of longitude and latitudinal data. We then One-Hot-Encoded it which gave us a sparse matrix that was the most important predictive element of our model. We believe that this is because terrain features matter immensely when determining the potential size of a wildfire. (See confusion matrix below)

The third major breakthrough was the trailing averages as noted in the summary above. Adding that data essentially doubled our recall scores for medium sized fires, which improved our overall model recall. Next, since our Neural Network is a blackbox model, we were not able to glean as much insight into features. We utilized Random Forest Classification to compliment insights from our Neural Network model by providing top features and weights.

**Top 3 features (excluding location clusters):**
|Feature|Importance|Feature Description|  
|---|---|---|  
|tavg_t3m|0.05085|Average Temperature Past 3 Months|  
|pcp|0.04720|Month Precipitation|  
|tavg_t6m|0.04633|Average Temperature Past 6 Months|


![](/visuals/confusion_matrix_fire.png)

---------------------------
### Conclusions

1. Wildfires are extremely complex phenomena. While the NOAA data offered a set of independent variables which fairly comprehensively described weather history, we were not able to include in our model other important factors which also affect final fire size, such as wind or terrain features (e.g. land cover or incline).

2. Switching our target variable from a continuous one (fire size, in acres) to a multi-class problem improved the score from an R2 of under 10% to accuracy of over 60%. Further, re-defining the problem as a binary classification of "large" vs "small" fires drove accuracy up to 62-77%, depending on the threshold chose to delineate between the two classes.

3. Because our goal was to improve preparedness and help contain damage from wildfires without putting efforts into preventing fires which weren't likely to spread, our ultimate focus was on increasing the recall of our model, and moreover - to increase its recall with regards to large fires.

4. Each of the seven-class classifications requires sklearn's estimators to perform 7 x (7-1) / 2 = 21 separate classifications - fitting some of the estimators we evaluated (e.g. SVM) was very computationally expensive.

5. Despite being computationally expensive, we were able to create a model that gave us a significant increase in our recall score. We can confidently predict very large fires and some mid range fires with our current model.

--------------------------------
**Classes and model improvements:**
|Class| Size Acres|Baseline (% of dataset)|Final Model|
|---|---|---|---|
|A| >0<=0.25|62%|59%|
|B|0.26-9.9|29%|1%|
|C|10.0-99.9|6%|20%|
|D|100-299|2%|50%||
|E|300 to 999|1%|58%|
|F|1000 to 4999|2%|59%|
|G|5000+|0.07%|86%|

-----------------------
### Recommendations

For further research we recommend extracting NOAA wind data such as wind speed, gusts and potentially wind directionality. Furthermore, vegetation data and environmental composition data which is available on Google’s Earth Engine’s LANDFIRE databases potentially play a significant part in telling a deeper story on a wildfire destructive ability. Merging those features into our datasets was unfortunately out of reach due to the time restraints thus we did not include them. However we believe these features merged into our current dataset could expand in a worthwhile manner.

-----------------------
### Data Dictionary 
[Kaggle Fire Data]([https://www.kaggle.com/rtatman/188-million-us-wildfires/notebooks](https://www.kaggle.com/rtatman/188-million-us-wildfires/notebooks)) 

[NOAA Climate Data]([https://www7.ncdc.noaa.gov/CDO/CDODivisionalSelect.jsp#](https://www7.ncdc.noaa.gov/CDO/CDODivisionalSelect.jsp#))

**Trailing Average Features:**
|Feature|Description|
|---|---|
|tavg_t12m| Average Temp 12mos Trailing|
|tavg_t9m|Average Temp 9mos Trailing|
|tavg_t6m|Average Temp 6mos Trailing|
|tavg_t3m|Average Temp 3mos Trailing|
|pcp_t12m|Average Precipitation 12mos Trailing|
|pcp_t9m|Average Precipitation 9mos Trailing|
|pcp_t6m|Average Precipitation 6mos Trailing|
|pcp_t3m|Average Precipitation 3mos Trailing|
|pmdi_t12m|Avg. Palmer Drought Severity Index 12mos Trailing|
|pmdi_t9m|Avg. Palmer Drought Severity Index 9mos Trailing|
|pmdi_t6m|Avg. Palmer Drought Severity Index 6mos Trailing|
|pmdi_t3m|Avg. Palmer Drought Severity Index 3mos Trailing|
|pdsi_t12m|Avg. Hydrological Drought Index 12mos Trailing|  
|pdsi_t9m|Avg. Hydrological Drought Index 9mos Trailing|
|pdsi_t6m|Avg. Hydrological Drought Index 6mos Trailing|
|pdsi_t3m|Avg. Hydrological Drought Index 3mos Trailing|
|cluster_0 - cluster_199|KMeans Latitude/Longitude Clusters|

<br>

**Features used from original data sets:**
|Feature|Description|
|---|---|
|pcp|Precipitation|
|tavg|Average Tempurature|
|pdsi|Hydrological Drought Index|
|phdi|Palmer Hydrological Drought Index|
|zndx|Palmer Zindex Data|
|pmdi|Palmer Drought Severity Index|
|sp02 - sp24|Precipitation|
|tmin|Minimum Temperature|
|tmax|Maximum Temperature|
|month_2 - month_12|Dummy Month Variables|

