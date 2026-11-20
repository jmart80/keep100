#!/usr/bin/env bash
set -eu
cp -R "$(cd "$(dirname "$0")" && pwd)/../../examples/b2b/." .
sed -i.bak "s/^Kit version: 1.1.0/Kit version: 1.0.0/" progress.md
rm -f progress.md.bak
