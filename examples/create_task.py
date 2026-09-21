"""Submit one generation request to a PiAPI model endpoint.

Mirrors the Python snippet on the PiAPI home page: X-API-Key header, JSON body.
The endpoint URL is model-specific; take it from https://piapi.ai/docs/overview.
"""
import json
import os
import sys

import requests

API_KEY = os.environ.get('PIAPI_API_KEY')
ENDPOINT = os.environ.get('PIAPI_ENDPOINT_URL')

if not API_KEY or not ENDPOINT:
    sys.exit('set PIAPI_API_KEY and PIAPI_ENDPOINT_URL first')

headers = {
    'X-API-Key': API_KEY,
    'Content-Type': 'application/json',
}

# Illustrative body: the home page shows prompt, aspect_ratio and process_mode.
# Each model accepts its own fields; check the docs for the one you call.
data = {
    'prompt': sys.argv[1] if len(sys.argv) > 1 else 'a cute cat',
    'aspect_ratio': '4:3',
    'process_mode': 'fast',
}

resp = requests.post(ENDPOINT, headers=headers, json=data, timeout=60)
print('status:', resp.status_code)
try:
    print(json.dumps(resp.json(), indent=2))
except ValueError:
    print(resp.text)
