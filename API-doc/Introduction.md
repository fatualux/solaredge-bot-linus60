## General Purpose And Scope

The purpose of this document is to outline the Application Programming Interface (API) available via SolarEdge Cloud-Based Monitoring Platform. The web services allow access to data saved in the monitoring server while keeping the data secured for authorized users. 

This document provides information about the technical features of the API, and describes each API with its parameters formats and other details. 

## Acronyms And Abbreviations

The following table lists acronyms used in this document 

| Abbreviation    | Meaning                           |
|-----------------|-----------------------------------|
| API             | Application Programming Interface |
| WS              | Web Services                      |
| REST            | Representational State Transfer   |
| CSV             | Comma Separated Values            |
| JSON            | JavaScript Object Notation        |
| XML             | Extensible Mark-up Language       |

## Revision History

-  August 2022 - updated documentation of the Inverter Technical Data endpoint
-  January 2019 - Addition of Meters API - Updated Storage Information API and Inverter Technical Data API
-  February 2018 - addition of disable/enable site access by associated account
-  September 2017 - various parameter updates
-  June 2016 - addition of StorEdge profiles API
- April 2016- addition of status filter for alerts API

## Introduction
The SolarEdge API allows other software applications to access its monitoring system database for data analysis purposes, fleet management, displaying system data in other applications, etc. The following is a list of available APIs:

| API Name                            | API Output                                                                                             |
|-------------------------------------|--------------------------------------------------------------------------------------------------------|
| Site List                           | A list of sites for a given account, with the information on each site. This list allows convenient search, sort and paginationx |
| Site Details                        | Details of a chosen site                                                                              |
| Site Data: Start and End Dates      | The site energy production start and end dates                                                         |
| Site Energy                         | Site energy measurements                                                                               |
| Site Energy - Time Period           | Site energy for a requested timeframe                                                                 |
| Site Power                          | Site power measurements in a 15-minute resolution                                                       |
| Site Overview                       | Site current power, energy production (today, this month, lifetime) and lifetime revenue consumption, export (feed-in), import (purchase), etc. |
| Site Energy                         | Detailed site energy measurements including meters such as consumption, export (feed-in), import (purchase), etc. |


## Introduction

| API Name                                                                                          | API Output                                                                 |
|---------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Site Power Flow                                                                                   | Get the power flowchart of the site                                        |
| Storage                                                                                           |                                                                            |
| Get detailed storage information from batteries including the state of energy, power and lifetime |                                                                            |
| energy                                                                                            |                                                                            |
| Site Image                                                                                        | The site image as uploaded to the server, either scaled or original size   |
| Site Environmental Benefits                                                                       | Summary of site's positive impact on the environment                       |
| Installer Logo Image                                                                              | The installer logo image as uploaded to the server.                        |
| Components List                                                                                   | List of inverters with name, model, manufacturer, serial number and status |
| Inventory                                                     | Information about the SolarEdge equipment, including: inverters/SMIs, batteries, meters, gateways and sensors  |
| Inverter Technical Data                                                                           | Technical data on the inverter performance for a requested period of time  |
| Equipment Change Log                                                                              | List of replacements for a given component                                 |
| Account List API                                                                                  | The account details and list of all sub-accounts                           |
| Get Sensor List                                                                                   | The list of sensors installed in the site                                  |
| Get Sensor Data                                                                                   | The measurements of the sensors installed in the site                      |
| Get Meters Data                                   | Information about each meter in the site including: lifetime energy, metadata and the device to which it's connected to.   |
| API Versions                                                                                      | The current and supported version numbers                                  |

An API key must be used in order to submit API requests. Account users should generate an Account Level API Key, and system owners should generate a Site level API Key. 

The API link is https://monitoringapi.solaredge.com Please review the API terms and conditions at this link: https://monitoring.solaredge.com/solaredge-web/p/license Display requirements: When displaying information from the API, place the SolarEdge logo where it is clear to the user that the information source is SolarEdge's monitoring system. 

The logo should link to http://solaredge.com For any assistance with display, send an email to support@solaredge.com 

## Technical Information

The SolarEdge API is built as RESTful service: 

- It uses predictable, resource oriented URLs 
- It has built-in HTTP capabilities for passing parameters via the API 
- It responds with standard HTTP codes 
- It can return results in XML, JSON (including JSONP support) or CSV format. 

## Api Access

 The API can be accessed via HTTPS protocol only. SolarEdge monitoring server supports both HTTPS/1.0 and HTTPS/1.1 
protocols. 
 All APIs are secured via an access token: every access to the API requires a valid token as a URL parameter named api_key. 
For example: api_key= L4QLVQ1LOKCQX2193VSEICXW61NP6B1O 
 An API key can be generated to enable access to specific sites (via Site API key) or to all sites within a specific account (via 
Account API key). 

## ► To Generate A Site Api Key:

In the Site Admin > **Site Access** tab **> Access Control** tab > **API Access** section: 

1. A0knowledge reading and agreeing to the SolarEdge API Terms & Conditions. 
2. Click Generate API key. 
3. Copy the key. 
4. Click **Save**. 
5. Use the key in all API requests 

## Security Guidelines

To help keep your data secure from unauthorized access, make sure to adhere to the following guidelines: 

 - **Don't share your API key**. Remember, gaining access to an API key is equivalent to obtaining a user's login credentials.
 - Never store your API key in publicly accessible locations, including shared documents, code repositories (such as GitHub) and shared network drives.
- Avoid sharing your API keys with third parties whenever possible. If you're using a third party service that asks you for your SolarEdge Monitoring API key, it is your responsibility to ensure the provider stores and handles your API key in a secure 
manner. 
- Do not make API requests directly from browser applications (JavaScript code). If you store your API key in your publicly accessible JavaScript code, it can be easily copied by anyone visiting your site. API requests should only be made from a 
secure backend server. 
 **Use Site API keys whenever possible**, particularly if you're allowing a third-party application or service to access the API on
your behalf. 
 **Rotate your API keys periodically**. SolarEdge recommends updating your API keys every 6 months. To generate a new API key:
- Account Key -  1. Navigate to the Account Admin > **Company Details** tab > **API Access** section 2. Uncheck the checkbox under "API Access" 3. Check the checkbox again - a new key will be generated 4. Click **Save**

## Site Key
1. Navigate to the Site Admin > **Site Access** tab > **Access Control** tab > **API Access** section 2. Click **New Key** 3. Click **Save**

## Language And Time Encoding
-  When using special characters or spaces in URL, they must be **url encoded**.  The monitoring server data can be in different languages therefore data is retrieved using UTF-8.  Date and time formats in all APIs are:
Date and time: YYYY-MM-DD hh:mm:s

## Introduction 

- Date only: YYYY-MM-DD 
 Dates are always in the time zone of the site.  All physical measures are in the metric units system.  Temperature values are always in Celsius degrees. 

## Request Format

The request format and parameters are specified per each API, and conform to the HTTP and REST standards. Parameter order in the request is not significant. 

## Response Formats

The user can request data in the following formats: 

- JSON (application/json) 
- XML(application/xml) 
- CSV (text/csv). 
See specific APIs in the next sections for supported format in each API. 

If a specific format is not requested, the data will be retrieved via JSON. If the requested format is invalid, the system will generate HTTP error "Media not supported". 

The API user can request the response format in one of the methods below. The system handles the response format as follows: 

- URL format Parameter - …&format=application/json 
- Path extension - the name of the API will be followed by the requested format 
name ../details.json&… 
- HTTP header - based on 'Accept' header e.g. Accept application/json 

## Jsonp Support

The API supports JSONP calls by appending a callback parameter with the name of a callback method at the end of the request. 

As JSONP content type is application/javascript, make sure the client sends this content type in the Accept header, otherwise HTTP 406 error may occur. 

## Introduction

The following example shows a JSON call VS. JSONP call: 

 JSON: 
- Request: 
http://monitoringapi.solaredge.com/1/details.json?api_key=[your_api_key] 

- Response body: 
{"details":{..}} 

 JSONP: 
- Request: http://monitoringapi.solaredge.com/1/details.json?api_key=[your_api_key]&callback=myFunction 

- Response body: 
myFunction({"details":{..}}); 

## Error Handling

The API system uses standard HTTP error codes for reporting errors that occurred while calling the API. The monitoring server API supports standard HTTP error codes, for example: if the user access is of an unknown resource, an HTTP 404 error will be returned. 

## Usage Limitations

Usage limitations are enforced to prevent abuse of the monitoring server API, and these limitations may be changed in the future without notice. Additionally, a request rate limit is applied to prevent abuse of the service. If you exceed the limitations, an error message appears in the monitoring server API. If the limitation is further exceeded, the system may temporarily be nonoperational, or your access to the monitoring server API may be blocked. 

## Specific Api Usage Limitations

Specific APIs may enforce different usage limitations based on parameters sent by the client. Refer to the next sections for details on specific API usage limitations. 

If there is a violation of a specific API validation, the HTTP 403 - forbidden status code is returned. 

## Daily Limitation

Use of the monitoring server API is subject to a query limit of 300 requests for a specific account token and a parallel query limit of 300 requests for each specific site ID from the same source IP. 

APIs that do not have a specific ID (e.g. Site List, Account List) will be counted as part of the account query limit. Any additional site or account level request will result in HTTP 429 error - too many requests. 

## Concurrency Limitation

The monitoring server API allows up to 3 concurrent API calls from the same source IP. Any additional concurrent calls will return HTTP 429 error - too many requests. To execute APIs concurrently without exceeding the above limitation, it is the client responsibility to implement a throttling mechanism on the client side. 

## Bulk Use

Some of the APIs offer a bulk form, that is, they take multiple site IDs as an input. The list is separated by a comma and should contain up to 100 site IDs. 

A bulk call for multiple sites consumes 1 call from the daily quota allowed for each of the sites included in the call. 

## Api Description Site Data Api Site List

Description: Returns a list of sites related to the given token, which is the account api_key. This API accepts parameters for convenient search, sort and pagination. 

Example URL (with all options):
- https://monitoringapi.solaredge.com/sites/list?size=5&searchText=Lyon&sortProperty=name&sortOrder=ASC&api_key=L4QLVQ1LOKCQX2193VSEICXW61NP6B1O
- Method: GET Formats: JSON, XML and CSV 
 **Request**: The following are parameters to include in the request. 

| Parameter      | Type    | Mandatory | Default Value | Description                                                                                   |
|----------------|---------|-----------|---------------|-----------------------------------------------------------------------------------------------|
| size           | Integer | No        | 100           | Number of results to return                                                                  |
| startIndex     | Integer | No        | 0             | Index of the first result to return                                                          |
| searchText     | String  | No        |               | Text to search for within the site. Searchable site properties: Name, Notes, Address, City, Zip code, Full address, Country |
| sortProperty   | String  | No        |               | Property to sort the results by. Options: Name, Country, State, City, Address, Zip, Status, PeakPower, InstallationDate, Amount, MaxSeverity, CreationTime |
| sortOrder      | String  | No        | ASC           | Sort order for the sort property. Options: ASC (ascending), DESC (descending)                  |
| Status         | String  | No        | Active,Pending | Site status                                                                                   |

The maximum number of sites returned by this call. The maximum number of sites that can be returned by this call is 100. If you have more than 100 sites, just request
another 100 sites with startIndex=100.This will fetch sites 100-199.
Select the sites to be included in the list by their status: Active  Pending  Disabled  All
Default list will include Active and Pending sites.

 **Response**:
- The returned data is the site list, including the sites that match the given search criteria. For each entry, the following information is displayed:
- id - the site ID
- name - the site name
- account id -the account this site belongs to
- status - the site status (see *Site Status* on page 53)
- peak power - site peak power
- CURRENCY
- installationDate - site installation date (format: yyyy-MM-DD hh:mm:ss )
- ptoDate - permission to operate date
- notes
- type - site type (see *Site Type* on page 53)
- location - includes country, state, city, address, secondary address, time zone and zip
- alertQuantity - number of open alerts in this site
- alertSeverity - the highest alert severity in this site
- publicSettings - includes if this site is public and its public name
- Alert information is only available when using an API_KEY generated by an account. API_KEY generated at the site level does not return this information.
