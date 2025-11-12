#!/bin/bash
# Helper script: move Web_Dev contents into repo root
set -e
cd "$(dirname "$0")"
echo "Moving files from Web_Dev/ to repo root..."
mv Web_Dev/* ./
echo "Done."
