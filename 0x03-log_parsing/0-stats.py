
#!/usr/bin/python3
"""
module contains a script that reads stdin line by line and computes metrics
"""
import sys


status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
