
import os
import sys
from datetime import datetime
from os.path import expanduser
import urllib


def main():

    # API parameters
    options = {}
    options["url"] = "https://airnowapi.org/aq/data/"
    options["start_date"] = "2021-06-1"
    options["start_hour_utc"] = "1"
    options["end_date"] = "2021-06-17"
    options["end_hour_utc"] = "23"
    options["parameters"] = "o3,pm25,pm10,co,no2,so2"
    options["bbox"] = "-74.5,40,-73.5,41"
    options["data_type"] = "c"
    options["format"] = "text/csv"
    options["ext"] = "csv"
    options["api_key"] = "A780977F-BDE6-46CA-A13A-1D50C0E5C20D"

    # API request URL
    REQUEST_URL = options["url"] \
                  + "?startdate=" + options["start_date"] \
                  + "t" + options["start_hour_utc"] \
                  + "&enddate=" + options["end_date"] \
                  + "t" + options["end_hour_utc"] \
                  + "&parameters=" + options["parameters"] \
                  + "&bbox=" + options["bbox"] \
                  + "&datatype=" + options["data_type"] \
                  + "&format=" + options["format"] \
                  + "&api_key=" + options["api_key"]

    try:
        # Request AirNowAPI data
        print "Requesting AirNowAPI data..."

        # User's home directory.
        home_dir = expanduser("~")
        download_file_name = "AirNowAPI" + datetime.now().strftime("_%Y%M%d%H%M%S." + options["ext"])
        download_file = os.path.join(home_dir, download_file_name)

        # Perform the AirNow API data request
        api_data = urllib.URLopener()
        api_data.retrieve(REQUEST_URL, download_file)

        # Download complete
        print "Download URL: %s" % REQUEST_URL
        print "Download File: %s" % download_file

    except Exception as e:
        print "Unable perform AirNowAPI request. %s" % e
        sys.exit(1)

if __name__ == "__main__":
    main()