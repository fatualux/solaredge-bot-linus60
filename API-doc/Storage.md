## Storage Information

**Description:** Get detailed storage information from batteries: the state of energy, power, and lifetime energy.  
**Note:** Applicable to systems with batteries.  
**URL:** `/site/{siteId}/storageData`  
**Method:** GET  
**Accepted response formats:** JSON (default), XML  

**Usage limitation:** This API is limited to a one-week period. Specifying a period longer than 7 days will generate error 403 with a proper description.

### Parameters:

| Parameter  | Type   | Mandatory | Description                                                   |
|------------|--------|-----------|---------------------------------------------------------------|
| siteId     | number | Yes       | The site identifier                                           |
| startTime  | String | Yes       | Storage power measured start time in yyyy-MM-DD hh:mm:ss format |
| endTime    | String | Yes       | Storage power measured end time in yyyy-MM-DD hh:mm:ss format   |
| serials    | Comma-separated list of Strings |           | Return data only for specific battery serial numbers; the list is comma-separated. If omitted, the response includes all the batteries in the site |

**Sample URL:** `https://monitoringapi.solaredge.com/site/1/storageData?serials=1111,2222&startTime=2015-05-22%2011:00:00&endTime=2015-05-25%2013:00:00&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O`

**Response:** The response includes the following:

- `storageData` - Root element
- `batteryCount` - Number of batteries included in the response
- `batteries` - A list of battery objects, each containing the following:
  1. `serialNumber` - String - The battery serial number
  2. `nameplate` - number - The nameplate (nominal) capacity of the battery
  3. `modelNumber` - Battery model number
  4. `telemetryCount` - number - The number of telemetries for this battery in the response
  5. `telemetries` - A list of storage data telemetries, each entry contains:
     - `timeStamp` - String - Telemetry timestamp in the format of YYYY-MM-DD HH:MM:SS
     - `power` - number - Positive power indicates the battery is charging, negative is discharging.
     - `batteryState` - number - can be one of the following: 0 (Invalid), 1 (Standby), 2 (Thermal Mgmt.), 3 (Enabled), 4 (Fault)
     - `lifeTimeEnergyCharged` - number - The energy charged from the battery in Wh, during the battery's lifetime.
     - `lifeTimeEnergyDischarged` - number - The energy discharged from the battery in Wh, during the battery's lifetime.
     - `fullPackEnergyAvailable` - The maximum energy (Wh) that can currently be stored in the battery. Note that the battery state of health (SoH) can be calculated from this value. SoH is defined as Full Pack Energy available today / Full Pack Energy available on day one. Full pack energy available on day one can be extracted from the battery nameplate value or battery model information. Both the battery nameplate value and model number are provided by the storageData method.
     - `internalTemp` - Battery internal temperature in Celsius.
     - `ACGridCharging` - Amount of AC energy used to charge the battery from the grid within a specified date range in Wh.
     - `stateOfCharge` - number (percentage) - the battery state of charge as a percentage of the available capacity. Values are in the range of 0 to 100.
## Disclaimers:

1. As LG battery does not provide lifetime charge/discharge data, the monitoring system aggregates the delta charge/discharge values. In cases where telemetries containing delta energy values are lost or not sent, the calculated lifetime energy values will be incomplete. Values provided are not revenue grade.
2. AC coupling is not supported with 3rd party inverters.

## Site Image

**Description:** Display the site image as uploaded by the user.  
**URL:** `/site/{siteId}/siteImage/{name}`  
**Example URL:** `https://monitoringapi.solaredge.com/site/1/siteImage/myname.jpg?hash=123456789&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O`  
**Method:** GET

**Performance:** The image element returns with a hash element, which is consistent as long as the image is not changed. When executing the Site Image API while using the hash element, the server matches the image hash and the hash sent in the URL. If a match is found, the API returns an HTTP 304 code. In case the image hash that appears in the URL is different than the one stored in the server, the image will be downloaded. When using the maxWidth and MaxHeight parameters, the hash element will be ignored.

**Image sizes:** By default, the API returns the same image that was uploaded to the monitoring portal. If an image in a different scale is required, the API supports it via the maxWidth and maxHeight parameters. The system will scale the image while keeping the aspect ratio of the original image, so the returned image will be smaller.

**Request:** The following are parameters to include in the request:

| Parameter | Type    | Mandatory | Description                                            |
|-----------|---------|-----------|--------------------------------------------------------|
| siteId    | Integer | Yes       | The site identifier                                    |
| name      | String  | No        | It is recommended to enter the site image name so the user can save the new image based on the name in the URL. |
| maxWidth  | Integer | No        | The maximum width to scale this image                  |
| maxHeight | Integer | No        | The maximum height to scale this image                 |
| hash      | Integer | No        | The image hash                                         |

**Response:** The response includes one of the following:
- The requested image
- Error 404 - not found, if the site has no image
- Error 304 - unmodified, if a hash attribute was specified

## Site Environmental Benefits

**Description:** Returns all environmental benefits based on site energy production: CO2 emissions saved, equivalent trees planted, and light bulbs powered for a day.  
**URL:** `/site/{siteId}/envBenefits`  
**Example:** `https://monitoringapi.solaredge.com/site/2/envBenefits?systemUnits=Imperial&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O`  
**Method:** GET  
**Accepted formats:** JSON

**Request:** The following parameters are included in the request:

| Parameter   | Type    | Mandatory | Description                                           |
|-------------|---------|-----------|-------------------------------------------------------|
| siteId      | Integer | Yes       | The site identifier                                   |
| systemUnits | String  | No        | Valid Values: Metrics, Imperial - note systemUnits are case sensitive. If systemUnits are not specified, the logged in user system units are used. |

**Response:** Returns the list of environmental benefits associated with the site energy production:
- gasEmissionSaved: quantity of CO2 emissions that would have been generated by an equivalent fossil fuel system
- treesPlanted: equivalent planting of new trees for reducing CO2 levels
- lightBulbs: number of light bulbs that could have been powered by the site for a day
