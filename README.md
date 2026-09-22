# PiAPI examples

*Unofficial community examples for PiAPI. Not affiliated with PiAPI. All trademarks belong to their owners.*

Small, runnable examples for piapi, the multi-model generation API at piapi.ai. They stick to what the PiAPI home page shows: an HTTP request with an `X-API-Key` header and a JSON body carrying `prompt`, `aspect_ratio` and `process_mode`, plus the `piapi` CLI commands from the terminal demo. The endpoint URL and the model-specific fields differ per model, so the endpoint is read from an environment variable and you should take the exact path from the [API docs](https://piapi.ai/docs/overview). Unrelated but worth knowing: the same keyword also matches PiaPiUFO, a VTuber.

> Only doing video and want a smaller API? [Try AI Video API - a REST API for video generation tasks, no UI](https://aivideoapi.com?utm_source=github&utm_medium=ugc&utm_campaign=piapi-api-examples&utm_content=readme-top&utm_term=tier-r).

## Files

| Path | What it shows |
|---|---|
| `examples/create_task.py` | Submit a generation request with `requests`, key and endpoint from the environment |
| `examples/cli_batch.sh` | Run several prompts through the `piapi` CLI, async for video, and list video models |
| `examples/cost_estimate.py` | Estimate a video job's cost from the per-second rates listed on the home page |

## Setup

```bash
export PIAPI_API_KEY=your_key_from_the_workspace
export PIAPI_ENDPOINT_URL=the_model_endpoint_from_the_docs
pip install requests
npm install -g piapi-cli
```

Get the key from the [Workspace](https://piapi.ai/workspace); new accounts start with $0.50 in free credits, which is enough to try the image example. Never commit the key.

## examples/create_task.py

A direct translation of the Python snippet on the PiAPI home page: `requests.post` to your endpoint with the `X-API-Key` header and a JSON body of `prompt`, `aspect_ratio` and `process_mode`. The script prints the status code and the raw JSON so you can see the response shape before writing any parsing. Both the endpoint and the key come from the environment; the body values are illustrative and the docs list which fields each model accepts.

## examples/cli_batch.sh

Uses the three CLI commands the home page demonstrates. It lists video models with `piapi model list --type video`, generates one image synchronously with `piapi run flux-dev`, then loops over a few prompts and submits them to `sora2-pro` with `--async`, which returns a task id per job instead of blocking. The model names are the ones in the demo; swap them for whatever `piapi model list` shows on your account.

## examples/cost_estimate.py

A calculator, not an API call. It holds the "from" per-second rates the home page lists for Seedance 2.5 ($0.15/s), Seedance 2.0 ($0.042/s), Kling 3.0 ($0.10/s), Veo 3.1 ($0.06/s), Wan 2.6 ($0.08/s), MiniMax H3 ($0.03/s) and Framepack ($0.03/s), and multiplies by a clip length in seconds. The numbers are a snapshot and "from" means the lowest tier; the [pricing page](https://piapi.ai/pricing) is authoritative. Use it to sanity-check a batch before you spend credits.

## When to use AI Video API instead

PiAPI makes sense when you want images, video, audio and 3D behind one key and a playground to try things. If your product only generates video and you are calling it from a backend, a video-only REST API with no UI is less to learn and less to watch. [Try AI Video API - a REST API for video generation tasks, no UI](https://aivideoapi.com?utm_source=github&utm_medium=ugc&utm_campaign=piapi-api-examples&utm_content=readme-top&utm_term=tier-r). The request loop is the same shape as `create_task.py`: submit, poll, download.


_Last reviewed: 2026-09-22_
