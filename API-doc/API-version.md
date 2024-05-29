## API Versions

As the monitoring API evolves over time, users of the monitoring API need to ensure their code is interacting with the formally supported version.

The monitoring API supports previous versions to some extent. This can be verified by executing the **Supported Version** API (see below). The version format is `<major.minor.release>` where:

- **Major**: The main version number. This number increases when the version includes significant changes, which might not be backward compatible with previous versions in terms of API calls and returned results.
- **Minor**: The sub-version number. This number increases when the version includes some changes, which might not affect the APIs; however, the returned results can contain more information than the previous minor version.
- **Release**: Bug fixes.

The user should optionally specify the version as a parameter for each API (except this API) e.g. `version=1.0.0`. If it is omitted, the current version is assumed (see **Current Version** below).

**Current Version**

- **Description**: Return the most updated version number in `<major.minor.revision>` format.
- **URL**: `/version/current`
- **Example URL**: [https://monitoringapi.solaredge.com/version/current](https://monitoringapi.solaredge.com/version/current)
- **Method**: GET
- **Accepted formats**: JSON and XML

  - **Request**: No parameters
  - **Response**: The current version
  - **Example**: JSON output: `{"version":"1.0.0"}`

**Supported Version**

- **Description**: Return a list of supported version numbers in `<major.minor.revision>` format.
- **URL**: `/version/supported`
- **Example URL**: [https://monitoringapi.solaredge.com/version/supported](https://monitoringapi.solaredge.com/version/supported)
- **Method**: GET
- **Accepted formats**: JSON and XML

  - **Request**: No parameters
  - **Response**: A list of supported versions
  - **Example**: JSON output: `{"supported":["0.9.5","1.0.0"]}`

**Data Types Time Unit**

Allowed values: DAY, WEEK, MONTH, and YEAR

**Site Status**

- Active: The site is active
- Pending Communication: The site was created successfully; however, there is no communication yet from its inverters/SMI.

**Site Type**

- Optimizers and inverters
- Safety and monitoring interface
- Monitoring combiner boxes
