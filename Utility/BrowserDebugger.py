from seleniumwire import webdriver  # Import from seleniumwire


def debug_request(driver):
    for request in driver.requests:
        if request.response:
            print(
                request.path,
                request.response.status_code,
                request.response.headers['Content-Type']
            )