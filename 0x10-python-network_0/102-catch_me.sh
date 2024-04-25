#!/bin/bash
# makes requests to cause specific responses
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -H "Origin:HolbertonSchool"
