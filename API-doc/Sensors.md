## Sensors API: Get Sensor List

**Description:** Returns a list of all the sensors in the site, and the device to which they are connected.

**URL:** `/equipment/{siteId}/sensors`  
**Example:** `https://monitoringapi.solaredge.com/equipment/2/sensors?api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O`  
**Method:** GET  
**Accepted formats:** JSON  

### Request:

The following parameters are to be included in the request:

| Parameter | Type    | Mandatory | Description          |
|-----------|---------|-----------|----------------------|
| siteId    | Integer | Yes       | The site identifier |

## Get Sensor Data

**Description:** Returns the data of all the sensors in the site, by the gateway they are connected to.

**URL:** `/site/{siteId}/sensors?{startDate}=<timestamp>&{endDate}=<timestamp>`

**Example:** [https://monitoringapi.solaredge.com/site/2/sensors?startDate=2013-05-5%2011:00:00&endDate=2013-05-05%2013:00:00&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O](https://monitoringapi.solaredge.com/site/2/sensors?startDate=2013-05-5%2011:00:00&endDate=2013-05-05%2013:00:00&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O)

**Method:** GET

**Accepted formats:** JSON

**Usage limitation:** This API is limited to a one-week period. This means that the period between `endDate` and `startDate` should not exceed one week. If the period is longer, the system will generate error 403 with a description.

**Request:** The following are parameters to include in the request:

| Parameter | Type    | Mandatory | Description                                |
|-----------|---------|-----------|--------------------------------------------|
| siteId    | Integer | Yes       | The site identifier                        |
| startDate | String  | Yes       | The start (date + time) to get sensor data |
| endDate   | String  | Yes       | The end (date + time) to get sensor data   |

**Response:** Returns the telemetries reported by all sensors in the site, by the device they are connected to. Each entry will include the following parameters:

- `connectedTo`: name of the gateway the sensor is connected to
- `count`: the number of telemetries
- `date`: timestamp of the telemetries
- `measurement`: (e.g. ambientTemperature) and its numerical value (metric system)
