## Installer Logo Image

**Description:** Return the site installer logo image as uploaded by the user. If such an image does not exist, the account installer logo is returned.

**URL:** `/site/{siteId}/installerImage/{name}`  
**Example URL:** `https://monitoringapi.solaredge.com/site/1/installerImage/myname.jpg?hash=123456789&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O`  
**Method:** GET

**Request:** The following are parameters to include in the request:

| Parameter | Type    | Mandatory | Description         |
|-----------|---------|-----------|---------------------|
| siteId    | Integer | Yes       | The site identifier |
| name      | String  | No        | The user can save the new image based on the name in the URL. |

**Response:** The response includes the requested image.

## Site Equipment Api Components List

**Description:** Return a list of inverters/SMIs in the specific site.  
**URL:** `/equipment/{siteId}/list`  
**Example URL (with all options):** `https://monitoringapi.solaredge.com/equipment/2/list?api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O`  
**Method:** GET  
**Accepted formats:** JSON, XML, and CSV  

**Request:** The following parameter is included in the request:

| Parameter | Type    | Mandatory | Description         |
|-----------|---------|-----------|---------------------|
| siteId    | Integer | Yes       | The site identifier |

**Response:** The response includes a list of inverters/SMIs with their name, model, manufacturer, and serial number.

- `name` - the inverter/SMI name
- `manufacturer` - the equipment manufacturer e.g., SolarEdge
- `model` - the inverter/SMI model e.g., SE16K
- `serialNumber` - the equipment short serial number

## Inverter Technical Data

**Description:** Return specific inverter data for a given timeframe.  
**URL:** `/equipment/{siteId}/{serialNumber}/data`  
**Example URL (with all options):** `https://monitoringapi.solaredge.com/equipment/2/12345678-90/data?startTime=2013-05-05%2011:00:00&endTime=2013-05-05%2013:00:00&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O`  
**Method:** GET  
**Accepted formats:** JSON, XML, and CSV  
**Usage limitation:** This API is limited to a one-week period. The period between `endTime` and `startTime` should not exceed one week. If the period is longer, the system will generate error 403 with a proper description.

### Request:

The following parameters are included in the request:

| Parameter    | Type    | Mandatory | Description                                  |
|--------------|---------|-----------|----------------------------------------------|
| siteId       | Integer | Yes       | The site identifier                          |
| serialNumber | String  | Yes       | The inverter short serial number             |
| startTime    | String  | Yes       | The start (date + time) to get inverter data |
| endTime      | String  | Yes       | The end (date + time) to get inverter data   |

### Response:

The response includes technical parameters for the inverter's performance, inverter type (1ph or 3ph), and software version. If an attribute is not supported based on the inverter version or type, it will be omitted from the response.

| Original name       | Comment                          |
|---------------------|----------------------------------|
| timestamp           |                                  |
| AC current          |                                  |
| AC voltage          |                                  |
| AC frequency        |                                  |
| QRef                |                                  |
| CosPhi              |                                  |
| Total Active Power  |                                  |
| apparentPower       | Supported starting communication |
| board version 2.474 |                                  |

### Data divided per phase:

| Original name   | Comment                        |
|-----------------|--------------------------------|
| activePower     | Supported starting communication |
| board version 2.474 |                                  |
| reactivePower   | Supported starting communication |
| board version 2.474 |                                  |
| DC voltage      |                                |
| groundFaultResistance |                                |
| powerLimit %    |                                |
| Lifetime energy | Supported starting communication |
| board version 2.474 |                                  |
| totalEnergy     |                                |
| temperature     | Celsius                        |
| inverterMode    |                                |
| operationMode   |                                |
| apparentPower   | VA                             |
| activePower     | VA                             |
| reactivePower   | VAR                            |
| cosPhi          |                                |

### Data divided per phase (for 3ph only):

| Original name   | Comment                        |
|-----------------|--------------------------------|
| vL1ToN          |                                |
| vL2ToN          |                                |
| vL1To2          |                                |
| vL2To3          |                                |
| vL3To1          |                                |

## Equipment Change Log

**Description:** Returns a list of equipment component replacements ordered by date. This method is applicable to inverters, optimizers, batteries, and gateways.  
**URL:** `/equipment/{siteId}/{serialNumber}/changeLog`  
**Example URL (with all options):** `https://monitoringapi.solaredge.com/equipment/2/1234567-38/changeLog?api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O`  
**Method:** GET  
**Accepted formats:** JSON, XML, and CSV  

### Request:

The following parameter is included in the request:

| Parameter     | Type    | Mandatory | Description                                    |
|---------------|---------|-----------|------------------------------------------------|
| siteId        | Integer | Yes       | Site identifier                                |
| serialNumber  | String  | Yes       | Inverter, battery, optimizer, or gateway short|

### Response:

The response includes a list of replacements by the specified equipment component, ordered by date. The list contains the component serial number, model, and date of replacement.

- `count`: number of replacements of the specified component
- `list`: list of replacements where each replacement contains:
  - `serialNumber`: equipment short serial number
  - `partNumber`: inverter/battery/optimizer/gateway model
  - `date`: date of replacement of that equipment component
## Account List API

**Description:** Return the account and list of sub-accounts related to the given token. This API accepts parameters for convenient search, sorting, and pagination.  
**URL:** `/accounts/list`  
**Example URL (with all options):** `https://monitoringapi.solaredge.com/accounts/list?size=5&searchText=someText&sortProperty=name&sortOrder=ASC&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O`  
**Method:** GET  
**Accepted formats:** JSON, XML, and CSV  

### Request:

The following are parameters to include in the request:

| Description                   | Parameter   | Type     | Mandatory |
|-------------------------------|-------------|----------|-----------|
| Default                       |             |          |           |
| Value                         |             |          |           |
| size                          | Integer     | No       | 100       |
|                               |             |          |           |
| startIndex                    | Integer     | No       | 0         |
|                               |             |          |           |
| searchText                    | String      | No       |           |
| Search text for this account. Searchable properties: Name, Notes, Email, Country, State, City, Zip, Full address | | | |
| sortProperty                  | String      | No       |           |
| A sorting option for this account list, based on one of its properties. Available sort properties: Name, country, city, address, zip, fax, phone, notes | | | |
| sortOrder                     | String      | No       | ASC       |

### Response:

The returned data is the account data, including sub-accounts. For each entry, the following information is displayed:

- `id`: account ID
- `name`: account name
- `location`: includes country, state, city, address, address2 (secondary address), zip
- `companyWebSite`: the company website
- `contactPerson`: the account contact person first name and surname
- `email`: the contact person email
- `phoneNumber`: account phone number
- `faxNumber`: account fax number
- `notes`: account notes
- `parentId`: account parent identifier
