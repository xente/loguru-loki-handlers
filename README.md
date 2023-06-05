# loguru-loki-handlers

Handler created for Loguru that sends logs to Grafana Loki in JSON format

## Features

* Logs pushed in JSON format
* Custom labels definition
* Allows defining loguru and logger extra keys as labels
* Logger extra keys added automatically as keys into pushed JSON

## How to use

```python
from loguru_loki_handler import loki_handler
from loguru import logger
import os 

os.environ["LOKI_URL"]="https://USER:PASSWORD@logs-prod-eu-west-0.grafana.net/loki/api/v1/push"

logger.configure(handlers=[{"sink":  loki_handler(os.environ["LOKI_URL"],{"application":"Test", "envornment":"Develop"}), "serialize": True}])
logger.info("Starting service")
logger.info("Response code {code} HTTP/1.1 GET {url}", code=200, url="https://loki_handler.io")

```

## Loki messages samples

### Without extra

```json
{
  "message": "Starting service",
  "timestamp": 1681638266.542849,
  "process": 48906,
  "thread": 140704422327936,
  "function": "run",
  "module": "test",
  "name": "__main__"
}

```

### With extra

```json
{
  "message": "Request return 200 HTTP/1.1 GET https://loki_handler.io",
  "timestamp": 1681638225.877143,
  "process": 48870,
  "thread": 140704422327936,
  "function": "run",
  "module": "test",
  "name": "__main__",
  "code": 200,
  "url": "https://loki_handler.io"
}
```

### Exceptions

```json
{
  "message": "name 'plan' is not defined",
  "timestamp": 1681638284.358464,
  "process": 48906,
  "thread": 140704422327936,
  "function": "run",
  "module": "test",
  "name": "__main__",
  "file": "test.py",
  "path": "/test.py",
  "line": 39
}
```

## Loki Query Sample

Loki query sample :

 ```
 {envornment="Develop"} |= `` | json
 ```

Filter by level:

```
{envornment="Develop", level="INFO"} |= `` | json
```
Filter by extra:

```
{envornment="Develop", level="INFO"} |= `` | json | code=`200`
```

## License
The MIT License