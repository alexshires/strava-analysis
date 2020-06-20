# Strava Analysis

## Data

Timestamp, Lat/Lon, Heart Rate, Elevation

The data is collected over time (either smart of per-second Garmin sampling). https://support.garmin.com/en-GB/?faq=s4w6kZmbmK0P6l20SgpW28 
* If smart - need to weight measurements by time
* If every second, can average over without weighting

In order to provide an accurate measurement, need to average over time

### Speed 
* GPS dependent (although errors should cancel in delta?)
### Elevation
* GPS errors (percentage of satellite numbers?)
### Heart rate
Considerations
* environment dependent
* physiology dependent
* heart rate drift for long term
### Timestamp 
* Assume true


## Metrics
 
* Pace  
* Pace (Gradient-adjusted)  
* Heart rate
* Heart rate (Gradient-adjusted)
* X v.s distance delta 
* X v.s. time delta

### Averaging

* metrics should be averaged over a suitably short time delta
* 





