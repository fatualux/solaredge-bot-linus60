## Inventory

**Description:** Return the inventory of SolarEdge equipment in the site, including inverters/SMIs, batteries, meters, gateways, and sensors.

**URL:** `/site/{siteId}/inventory`  
**Example URL (with all options):** `https://monitoringapi.solaredge.com/site/2/inventory?api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O`  
**Method:** GET  
**Accepted formats:** JSON, XML

## Request:

The Following Parameter Is Included In The Request:

| Parameter | Type    | Mandatory | Description         |
|-----------|---------|-----------|---------------------|
| siteId    | Integer | Yes       | The site identifier |

## Response:

The response includes a list equipment installed on site:

### Inverters - SolarEdge inverters

- `name` - the inverter name e.g., Inverter 1 
- `manufacturer` - manufacturer name (SolarEdge) 
- `model` - model name e.g., SE16K 
- `CPU Firmware version` e.g., 2.52.311 
- `DSP 1 Firmware version`
- `DSP 2 Firmware version`
- `communicationMethod` - the communication interface used to connect to the server. E.g., Ethernet. 
- `serialNumber` - the equipment serial number e.g., 7F123456-00 
- `connectedOptimizers` - number of optimizers connected to the inverter 

### Third Party Inverters

- `name` - the inverter name, e.g.: Inverter 1 
- `manufacturer` - manufacturer name 
- `model` - model name 
- `SN` - serial number 

### SMI List - List of SMI devices

- `name` - the inverter name e.g., Inverter 1 
- `manufacturer` - manufacturer name (SolarEdge) 
- `model` - model name e.g., SE16K 
- `Firmware version` e.g., 2.52.311 
- `communicationMethod` - the communication interface used to connect to the server. e.g., Ethernet. 
- `serialNumber` - the equipment serial number e.g., 7F123456-00 
- `connectedOptimizers` - number of optimizers connected to the inverter 

### Meters

- `name` - the inverter name e.g., "Feed In Meter" 
- `Manufacturer` - e.g., "WattNode" 
- `Model` - meter model number 
- `SN` - serial number (if applicable) 
- `Type` - meter type, e.g., "Production" 
- `FirmwareVersion` (if applicable) 
- `ConnectedTo` - Name of SolarEdge device the meter is connected to 
- `connectedSolaredgeDeviceSN` - serial number of the inverter / gateway the meter is connected to 
- `form` - physical for a HW meter or virtual if calculated by arithmetic between other meters 

### Sensors - Irradiance / wind / temperature sensors

- `connectedSolaredgeDeviceSN` - the S/N of the device it is connected to e.g., 12345678-00 
- `Id` - e.g., "SensorDirectIrradiance" 
- `connectedTo` - name of the device it is connected to e.g., "Gateway 1" 
- `Category` - e.g., IRRADIANCE 
- `Type` - e.g., "Plane of array irradiance" 

### Gateways

- `name` - the inverter name e.g., Inverter 1 
- `serialNumber` - the equipment serial number e.g., 7F123456-00 
- `Firmware version` 

### Batteries

- `Name` 
- `Serial Number` 
- `Manufacturer` - the battery manufacturer name 
- `Model` - the battery model name 
- `Nameplate capacity` - the nameplate capacity of the battery as provided by the manufacturer 
- `Firmware version` 
- `ConnectedTo` - Name of SolarEdge device the battery is connected to 
- `connectedSolaredgeDeviceSN` - serial number of the inverter / gateway the battery is connected to
