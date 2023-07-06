#!/bin/bash
export PATH=$PATH:/Users/david/Library/Python/3.8/bin
scrapy crawl redis_io_links -o status_codes.json
clear
cat status_codes.json | grep 404
