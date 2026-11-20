#!/usr/bin/env bash
set -eu
python3 "$(cd "$(dirname "$0")" && pwd)/../../scripts/eval_scaffold.py" b2b
