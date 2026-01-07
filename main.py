import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

SLEEP_TIME = 1800

# Hide mouse cursor using css
def hide_cursor(driver_instance):
    try:
        script = """
            var style = document.createElement('style');
            document.head.appendChild(style);
            style.sheet.insertRule('* { cursor: none !important; }', 0);
        """
        driver_instance.execute_script(script)
    except Exception as e:
        print(f"Failed to hide cursor: {e}")

def main():
    # Get url from desktop
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop", "url.txt")

    # Read URL
    try:
        with open(desktop_path, "r") as file:
            target_url = file.read().strip()
    except FileNotFoundError:
        print(f"File not found: {desktop_path}")
        exit()

    # Chrome Options
    chrome_options = Options()
    chrome_options.add_argument("--kiosk")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    # Launch chromium to webpage in kiosk mode
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(target_url)

    hide_cursor(driver)

    print("Kiosk running. Press CTRL+C or ALT+F4 to stop")

    # Refresh Loop
    while True:

        time.sleep(SLEEP_TIME)

        print("Refreshing page")
        driver.refresh()

        hide_cursor(driver)


if __name__ == "__main__":
    main()
