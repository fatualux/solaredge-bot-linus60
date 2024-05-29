## Site Data: Bulk Version

Description: This section describes the use of the above API for a bulk call. URL: /sites/{siteId 1},{siteId 2},…,{siteId n}/dataPeriod Example: https://monitoringapi.solaredge.com/sites/1,4/dataPeriod?api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O 

 **Response**: The response includes a list of <start, end> data transmission dates for the requested sites.
The value "null" will be displayed for sites that have no data (not transmitting). 

Note that if the list contains site IDs for which the user has no permission to view, the system will generate a 403 Forbidden error with a proper description. 

## Site Energy

Description: Return the site energy measurements. 
- Note: this API returns the same energy measurements that appear in the Site Dashboard.
- URL: /site/{siteId}/energy
- Example: https://monitoringapi.solaredge.com/site/1/energy?timeUnit=DAY&endDate=2013-05-30&startDate=2013-05-01&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O
-- Method: GET Accepted formats: JSON, XML and CSV 


 **Usage limitation**: This API is limited to one year when using timeUnit=DAY (i.e., daily resolution) and to one month when 
using timeUnit=QUARTER_OF_AN_HOUR or timeUnit=HOUR. This means that the period between endTime and startTime 
should not exceed one year or one month respectively. If the period is longer, the system will generate error 403 with proper description. 
 **Request**: The following are parameters to include in the request: 

| Parameter       | Type    | Mandatory | Description                                 |
|-----------------|---------|-----------|---------------------------------------------|
| siteId          | Integer | Yes       | The site identifier                         |
| startDate       | String  | Yes       | The start date to return energy measurement |
| endDate         | String  | Yes       | The end date return energy measurement      |
| timeUnit        | String  |           | Aggregation granularity, see on page 53.   |
|                 |         |           | Default: DAY. Allowed values are: - QUARTER_OF_AN_HOUR - HOUR - DAY - WEEK - MONTH - YEAR. |

**Response**: The response includes the requested time unit, the units of measurement (e.g. Wh), and the pairs of date and 
energy for every date ({"date":"2013-06-01 00:00:00","value":null}). 
The date is calculated based on the time zone of the site. "null" means there is no data for that time. 

## Site Energy: Bulk Version

Description: This section describes the use of that the above API for a bulk call.
- URL: /sites/{siteId 1},{siteId 2},…,{siteId n}/ energy
- Example: https://monitoringapi.solaredge.com/sites/1,4/energy?timeUnit=DAY&startDate=2013-05-01&endDate=2013-05-30&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O 

 **Response**: The response includes the requested time unit, the units of measurement (e.g. Wh), and the list of sites. For each 
site there is a list of items whichinclude a time stamp and the energy produced in that period. Example: ({"date":"2013-06- 01 00:00:00","value":1500.12}). The date is calculated based on the time zone of every site; if there is no value for the selected time, "null" will be displayed for the value. 
Note that if the list contains site IDs for which the user has no permission to view, the system will generate a 403 Forbidden error with a proper description. 

## Site Energy - Time Period

Description: Return the site total energy produced for a given period.
- Note: This API only returns on-grid energy for the requested period. In sites with storage/backup, this may mean that results can differ from what appears in the Site Dashboard. Use the regular Site Energy API to obtain results that match the Site Dashboard calculation.  
- Url: /Site/{Siteid}/Timeframeenergy
- Example: https://monitoringapi.solaredge.com/site/1/timeFrameEnergy?startDate=2013-05-01&endDate=2013-05-06&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O
- Method: GET Accepted formats: JSON and XML 

 **Usage limitation**: This API is limited to one year when using timeUnit=DAY (i.e., daily resolution). This means that the period 
between endTime and startTime should not exceed one year). If the period is longer, the system will generate error 403 with proper description 
 **Request**: The following are parameters to include in the request: 

| Parameter    | Type    | Mandatory    | Description                                   |
|--------------|---------|--------------|-----------------------------------------------|
| siteId       | Integer | Yes          | The site identifier                           |
| startDate    | String  | Yes          | The start date to calculate energy generation |
| endDate      | String  | Yes          | The end date to calculate energy generation   |

 **Response**: The response includes the energy summary for the given time period with units of measurement (e.g. Wh) 
The date is calculated based on the time zone where the site is located. 

## Site Energy - Time Period: Bulk Version
Description: This section describes the use of that the above API for a bulk call.
- URL: /sites/{siteId 1},{siteId 2},…,{siteId n}/timeFrameEnergy
- Example: *https://monitoringapi.solaredge.com/sites/1,4/energy?timeFrameEnergy*?startDate=2013-05-01&endDate=2013-05-06&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O

**Response**:
 - The response includes the units of measurement (e.g. Wh), and the list of sites that include energy summary for the given time period. The date is calculated based on the time zone of every site; if no data exists for the requested period, "null" will be displayed for the value field. Note that if the list contains site IDs for which the user has no permission to view, the system will generate a 403 Forbidden error with a proper description.

# Site Energy - Detailed

**Description:** 
Detailed site energy measurements from meters such as consumption, export (feed-in), import (purchase), etc.

**Note:** 
Calculated meter readings (also referred to as "virtual meters"), such as self-consumption, are calculated using the data measured by the meter and the inverters.

**URL:** 
`/site/{siteId}/energyDetails`

**Method:** 
GET 

**Accepted response formats:**
JSON (default), XML

## Usage Limitation

This API is limited to:

- A year when using daily resolution (timeUnit=DAY)
- A month when using hourly resolution or higher (timeUnit=QUARTER_OF_AN_HOUR or timeUnit=HOUR)
- Lower resolutions (weekly, monthly, yearly) have no period limitation
In case the requested resolution is not allowed for the requested period, error 403 with proper description will be returned.

## Parameters

| Parameter | Type   | Mandatory | Description                                                |
|-----------|--------|-----------|------------------------------------------------------------|
| siteId    | number | Yes       | The site identifier                                       |
| startTime | String | Yes       | The energy measured start time in yyyy-MM-DD hh:mm:ss format |
| endTime   | String | Yes       | The energy measured end time in yyyy-MM-DD hh:mm:ss format |
| timeUnit  | String | No        | Aggregation granularity. Default: DAY. Allowed values are: QUARTER_OF_AN_HOUR, HOUR, DAY, WEEK, MONTH, YEAR |
| meters    | String | No        | Select specific meters only. If omitted, all meter readings are returned. Values: Production, Consumption, SelfConsumption, FeedIn, Purchased |

[https://monitoringapi.solaredge.com/site/1/energyDetails?meters=PRODUCTION,CONSUMPTION&timeUnit=DAY&startTime=2013-05-15%2011:00:00&endTime=2013-05-25%2013:00:00&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O](https://monitoringapi.solaredge.com/site/1/energyDetails?meters=PRODUCTION,CONSUMPTION&timeUnit=DAY&startTime=2013-05-15%2011:00:00&endTime=2013-05-25%2013:00:00&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O)

 **Response**: The response includes the following: 
energyDetails - root element 
- timeUnit - the requested time unit 
- unit - The measurement units (e.g. Wh) 
- meters - List of meters. For each meter: 
- type - The meter type (Production/Consumption/SelfConsumption/FeedIn (export)/Purchased 
(import)) 
- values - Pairs of date and power for every date ({"date":"2013-06-04 14:00:00" , 
"value":7722.3896}). For dates in which no data exists the value will be committed (see sample) 
