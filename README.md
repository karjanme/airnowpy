[codecov-image]: https://codecov.io/gh/jnsnkrllive/airnowpy/branch/master/graph/badge.svg
[codecov-url]: https://codecov.io/gh/jnsnkrllive/airnowpy
[downloads-image]: https://pepy.tech/badge/airnowpy
[downloads-url]: https://pepy.tech/project/airnowpy
[github-actions-image]: https://github.com/jnsnkrllive/airnowpy/workflows/Main%20Workflow/badge.svg?branch=master
[github-actions-url]: https://github.com/jnsnkrllive/airnowpy/actions?query=workflow%3A%22Main+Workflow%22+branch%3Amaster
[pypi-image]: https://badge.fury.io/py/airnowpy.svg
[pypi-url]: https://badge.fury.io/py/airnowpy

[![PyPi][pypi-image]][pypi-url]
[![GitHub Actions][github-actions-image]][github-actions-url]
[![Downloads][downloads-image]][downloads-url]
[![Code Coverage][codecov-image]][codecov-url]

# AirNowPy

A Python library to facilitate interactions with the [AirNow API](https://docs.airnowapi.org/) web service.

## Prerequisites

### Supported Python Version

* 3.7, 3.8

### Secrets

In order to use this library an API key is required. Get one [here](https://docs.airnowapi.org/account/request/).

## Installation

```
pip install airnowpy
```

## Usage

### Initialize the API Connector
```
from airnowpy import API

api = API('secret_api_key')
```

### Current Observation by Lat/Lon
```
from airnowpy import Observation

observations = api.getCurrentObservationByLatLon(47.562, -122.3405)

for observation in observations:
// TODO: format
  print("At " + observation.timestamp + " in reporting area " + observation.reportingArea + " the air quality category for parameter " + observation.parameterName + " was " + observation.category.getLabel())
```

### Current Observation by Zip Code
```
from airnowpy import Observation

observations = api.getCurrentObservationByZipCode("98185")

for observation in observations:
  // Do something
```

## License

[MIT License](https://github.com/jnsnkrllive/airnowpy/blob/master/LICENSE)
