# Sites Monitoring Utility

A script from the specified text file with a list of URLs, checks the existence of the URL and the expiration date is longer than 30 days.

# How to use

The script requires the installed Python interpreter version 3.5 To call the help, run the script with the -h or --help option.

```Bash
$python check_sites_health.py
usage: check_sites_health.py [-h] path
check_sites_health.py: error: the following arguments are required: path
```

To start executing the script, you must specify the path to the file with the URL list.

```Bash
$python check_sites_health.py url.txt
http://yandex.ru
Responce from URL: <Response [200]>
Expiration date: 2018-09-30 21:00:00
Days before expiration: 293
----------------------------------------------------------
http://www.google.ru
Responce from URL: <Response [200]>
Expiration date: 2018-03-04 21:00:00
Days before expiration: 83
----------------------------------------------------------
http://mail.ru
Responce from URL: <Response [200]>
Expiration date: 2018-09-30 21:00:00
Days before expiration: 293
----------------------------------------------------------
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
