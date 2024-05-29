## Site Overview

Description: Display the site overview data. URL: /site/{siteId}/ overview Example URL: https://monitoringapi.solaredge.com/ site/{siteId}/overview?api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O Method: GET Accepted formats: JSON and XML 

##  **Request**: The Following Parameter Is Included In The Request:

| Parameter    | Type    | Mandatory    | Description         |
|--------------|---------|--------------|---------------------|
| siteId       | Integer | Yes          | The site identifier |

**Response**: The Response Includes The Site Current Power, Daily Energy, Monthly Energy, Yearly Energy And Life Time Energy

## Site Overview: Bulk Version

Description: This section describes the use of that the above API for a bulk call. URL: /sites/{siteId 1},{siteId 2},…,{siteId n}/overview Example URL: https://monitoringapi.solaredge.com/sites/1,4/overview&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O 

 **Response**: The response includes the last update time, current power, and daily, monthly, yearly and life time energy and 
revenue measurements for each of the sites in the list 
Note that if the list contains site IDs for which the user has no permission to view, the system will generate a 403 Forbidden error with a proper description. 
