#!/bin/bash

set -euo pipefail

sqlite3 app/portals.db < schema/portals.sql
cd app && python3 create_test_world.py
