# Niland API Python Wrapper

Setup
-------------
To setup your project, follow these steps:

1. Install Niland API Client using pip: `pip install pyniland` .
  Alternatively, you could clone this repository and then run the following command : `python setup.py install`

2. Next you'll have to initialize the client with your API-Key. You can find it on [your Niland API account](https://api.niland.io/2.0/dashboard/your-account).

```python
from pyniland.client import Client

client = Client('YourAPIKey')
```

Quick Start
-------------

List tracks using pagination
```python
data = client.get('tracks', {'page_size': 10, 'page': 2})
```

Retrieve a track by its reference
```python
data = client.get('tracks/reference/YOUR_REFERENCE')
```

Find tracks by similarity and/or tags
```python
data = client.get('tracks/search', {
    'similar_ids': [1234],
    'tag_ids': [21, 41]
})
```

Post a track
```python
data = client.post('tracks', {
    'title': 'foobar',
    'artist': 'foobar',
    'reference': 'foobar',
    'tags': [21, 41],
    'audio': open('/path/to/your/audio/file.mp3', 'rb')
})
```
