# 403 Bypass Tool
### Description

The 403 Bypass Tool is a Python script that helps you test different HTTP methods and payloads to potentially bypass the 403 Forbidden error on a target URL. The script uses the requests library to send various HTTP `requests` and checks the status codes to see if any of them can bypass the restriction.

**Requirements**
> Before running the script, make sure you have the following installed:

- Python 3.x
- `requests` library
- `pyfiglet` library

You can install the required libraries using `pip`:
```pip
pip install requests pyfiglet
```
**Usage**

    1. Run the script and it will prompt you to enter the target URL.
    2. The script will then test different HTTP methods (GET, POST, HEAD, PUT, DELETE, PATCH) and display the status codes for each request.
    3. Next, the script will use various payloads to attempt bypassing the 403 Forbidden error. It will display the status codes for each URL formed with different payloads.

**Example**
```
python 403_bypass.py -u https://www.hackerone.com/themes/
```

**Disclaimer**
- This tool is intended for educational and testing purposes only.
-  Unauthorized use against any website or service is illegal and unethical.
-   Use this tool responsibly and only on systems that you own or have permission to test.
  
**Author**
> [barathkumarjk](https://github.com/barathkumarjk)
