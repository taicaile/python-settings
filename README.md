# README

To install the latest package,

```bash
pip install git+https://github.com/taicaile/python-settings
```

To install specific version,

```bash
pip install git+https://github.com/taicaile/python-settings@v0.1.0
```

To perform test,

```bash
python tests/test.py
```

Usage,

```bash
from settings import settings
# if set module
from . import defaults
settings.setmodule(defaults)

# get value
settings.get(KEY)
```
