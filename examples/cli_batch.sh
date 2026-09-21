#!/usr/bin/env bash
# Batch a few prompts through the piapi CLI.
# Install once: npm install -g piapi-cli
# The CLI reads your key from its own login/config; see https://piapi.ai/cli
set -euo pipefail

echo '== video models available on this account =='
piapi model list --type video

echo '== one synchronous image (from the home page demo) =='
piapi run flux-dev prompt="a corgi astronaut"

echo '== async video jobs, one task id each =='
prompts=(
  "waves"
  "a slow pan over a foggy harbour at dawn"
  "paper boats drifting down a rain gutter"
)
for p in "${prompts[@]}"; do
  # --async returns immediately with a task id instead of waiting for the render
  piapi run sora2-pro prompt="$p" --async
done

echo 'Poll the task ids above with the CLI or the API; see the docs for the task endpoint.'
