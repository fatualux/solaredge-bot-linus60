## Meters API: Get Meters Data

**Description:** Returns, for each meter on the site, its lifetime energy reading, metadata, and the device to which it's connected.

**URL:** `/site/{siteId}/meters`  
**Example:** `https://monitoringapi.solaredge.com/site/2/meters?meters=Production,Consumption&startTime=2013-05-05%2011:00:00&endTime=2013-05-05%2013:00:00&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O`  
**Method:** GET  
**Accepted formats:** JSON, XML (default)  

### Request:

The following parameters are to be included in the request:

| Parameter           | Type     | Mandatory | Description                                                                                                                |
|---------------------|----------|-----------|----------------------------------------------------------------------------------------------------------------------------|
| site                | number   | Yes       | Site identifier                                                                                                            |
| timeUnit            | String   | No        | Aggregation granularity. Default: DAY. Allowed values: QUARTER_OF_AN_HOUR, HOUR, DAY, WEEK, MONTH, YEAR.                 |
| startTime           | String   | Yes       | The start time of the power measurement in yyyy-MM-DD hh:mm:ss format.                                                     |
| endTime             | String   | Yes       | The end time of the power measurement in yyyy-MM-DD hh:mm:ss format.                                                       |
| meters              | String   | No        | Select specific meters only. If omitted, all meter readings are returned. Value options: Production, Consumption, FeedIn, Purchased. |

### Response:

The response parameters include lifetime energy readings at the defined granularity within the specified date range, along with the following parameters:

| Original name              | Comment                                      | Data divided per meter |
|----------------------------|----------------------------------------------|------------------------|
| timeUnit                   | Aggregation granularity                      | no                     |
| Unit                       |                                              |                        |
| Wh                         |                                              |                        |
| no                         |                                              |                        |
| meterSerialNumber          |                                              |                        |
|                            |                                              |                        |
| yes                        |                                              |                        |
| connectedSolaredgeDeviceSN | Inverter to which the meter is connected     | yes                    |
| model                      | Meter model                                  | yes                    |
| meterType                  | Type of meter (Production, Consumption, etc.) | yes                    |
