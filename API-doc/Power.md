## Site Power

### Description
This API returns the site power measurements in 15-minute resolution.

- URL: `/site/{siteId}/power`
- Example :[https://monitoringapi.solaredge.com/site/1/power?startTime=2013-05-05%2011:00:00&endTime=2013-05-05%2013:00:00&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O]( https://monitoringapi.solaredge.com/site/1/power?startTime=2013-05-05%2011:00:00&endTime=2013-05-05%2013:00:00&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O)
- Method: GET
- Accepted formats: JSON, XML, and CSV

### Usage Limitation
This API is limited to a one-month period. If the period between `endTime` and `startTime` exceeds one month, the system will generate a 403 error with a proper description.

### Request Parameters
| Parameter | Type    | Mandatory | Description                                        |
|-----------|---------|-----------|----------------------------------------------------|
| siteId    | Integer | Yes       | The site identifier                                |
| startTime | String  | Yes       | The start (date + time) to get power measurements |
| endTime   | String  | Yes       | The end (date + time) to get power measurements   |

### Response
The response includes:
- Time unit (e.g., QUARTER_OF_AN_HOUR)
- Measurement unit (e.g., Watt)
- Pairs of date and power (in Watts) for every date (`{"date":"2013-06-04 14:00:00","value":7722.3896}`)

# Site Power: Bulk Version

## Description
This section describes how to use the API for bulk calls. 

- URL /sites/{siteId1},{siteId2},...,{siteIdn}/power

- Example [https://monitoringapi.solaredge.com/sites/1,4/power?startTime=2013-06-04%2011:00:00&endTime=2013-06-04%2014:00:00&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O](https://monitoringapi.solaredge.com/sites/1,4/power?startTime=2013-06-04%2011:00:00&endTime=2013-06-04%2014:00:00&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O)

### Response
The response includes:
- Resolution of time measurements (e.g. QUARTER_OF_AN_HOUR)
- Units of measurement (e.g. W)
- List of sites with date and power in the given resolution. 

The date is calculated in ticks starting from 1-1-1970 and presented based on the time zone of the site. If no data exists for the requested period, "null" will be displayed for the value field. 

Note: If the list contains site IDs for which the user has no permission to view, the system will generate a 403 Forbidden error with a proper description.

# Site Power - Detailed

## Description
Detailed site power measurements from meters such as consumption, export (feed-in), import (purchase), etc.

**Note:** Calculated meter readings (also referred to as "virtual meters"), such as self-consumption, are calculated using the data measured by the meter and the inverters.

**URL:** `/site/{siteId}/powerDetails`  
**Method:** GET  
**Accepted response formats:** JSON (default), XML

### Usage limitation
This API is limited to a one-month period. The period between `endTime` and `startTime` should not exceed one month. If the period is longer, the system will generate error 403 with a proper description.

### Parameters

| Parameter   | Type   | Mandatory | Description                                              |
|-------------|--------|-----------|----------------------------------------------------------|
| siteId      | number | Yes       | The site identifier                                      |
| startTime   | String | Yes       | The power measured start time in `yyyy-MM-DD hh:mm:ss` format |
| endTime     | String | Yes       | The power measured end time in `yyyy-MM-DD hh:mm:ss` format   |
| meters      | String | No        | Select specific meters only. If this value is omitted, all meter readings are returned. Value shall include entries from the following list separated by comma: Production (AC production power meter / inverter production AC power), Consumption (Consumption meter), SelfConsumption (virtual self-consumption calculated), FeedIn (Export to GRID meter), Purchased (Import power from GRID meter) |

### Response
The response provides 15-minute resolution data series for each of the requested meters. The response includes the following:
- `powerDetails` - Root element
- `timeUnit` - The time unit of the data (e.g., QUARTER_OF_AN_HOUR)
- `unit` - Power measurement units (e.g., Watt)
- `meters` - List of meters. For each meter:
- `type` - The meter type (Production/Consumption/SelfConsumption/FeedIn (export)/Purchased (import))
- `values` - Pairs of date and power for every date (`{"date":"2013-06-04 14:00:00", "value":7722.3896}`). For dates in which no data exists, the value will be omitted.

### Sample response
- Example: [https://monitoringapi.solaredge.com/site/1/powerDetails?meters=PRODUCTION,CONSUMPTION&startTime=2015-11-21%2011:00:00&endTime=2015-11-22%2013:00:00&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O](https://monitoringapi.solaredge.com/site/1/powerDetails?meters=PRODUCTION,CONSUMPTION&startTime=2015-11-21%2011:00:00&endTime=2015-11-22%2013:00:00&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O)
- **Response**: The response provides 15 minute resolution data series for each of the requested meters. 
The response includes the following: 
powerDetails - Root element 
- timeUnit - The time unit of the data (i.e. QUARTER_OF_AN_HOUR) 
- unit - Power measurement units (e.g. Watt) 
- meters - List of meters. For each meter: 
- type - The meter type (Production/Consumption/SelfConsumption/FeedIn (export)/Purchased 
(import)) 
- values - Pairs of date and power for every date 
({"date":"2013-06-04 14:00:00" , "value":7722.3896}) For dates in which no data exists the value will be committed
## Site Power Flow

**Description:** Retrieves the current power flow between all elements of the site including PV array, storage (battery), loads (consumption), and grid.

**Note:** Applies when export, import, and consumption can be measured.

**URL:** `/site/{siteId}/currentPowerFlow`  
**Method:** GET  
**Accepted response formats:** JSON (default), XML

## Parameters:

| Parameter | Type   | Mandatory | Description         |
|-----------|--------|-----------|---------------------|
| siteId    | number | Yes       | The site identifier |

**Example URL:**  
**Response:** The response returns power flow for each of the elements in the system and their state. In case the site does not support this information, the response should be an empty object. Otherwise, the response includes the following:

- `siteCurrentPowerFlow` - Root element
- `unit` - The measurement units (e.g. Watt)
- `connections` - A table including all the relationships between the elements, and the power flow directions (producing element and consuming element)
- `from element` - The element providing power
- `to element` - The element consuming power
- A list of elements - Element per entity type in the specific site
  - `GRID` - always included in response
  - `LOAD` - always included in response
  - `PV` - included if the site has a PV array (measurement of PV produced power)
  - `STORAGE` - included if the site has storage installed and enabled

**Parameters for each element:**

1. For all included elements, the following parameters are provided:
   - `status` - The current status of the element (Active / Idle / **Disabled**)
   - `currentPower` - The current power of the element. All numbers are positive; power direction is determined by the "connections" section above:

     - For **STORAGE** - Check the "connection" section for the direction. From storage to load = discharge. From PV to storage or from load to storage = charge.
     - For **GRID** - Check the "connection" section for the direction. From grid to load = import (purchase), from load to grid = export (feed-in).

2. For Storage, the following additional properties are included:
   - `chargeLevel` - The accumulated state of energy (% of charge) for all batteries
   - `critical` - If the accumulated storage charge level drops below a configurable level (currently 10%), this flag is returned
   - `timeLeft` - In Backup mode (GRID is **Disabled**), this property is returned to specify the time left before the storage energy runs out (estimated according to current load level).
