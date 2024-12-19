# Google Form Auto-Fill Script

### Description
This script automates the filling of a Google Form using Selenium. It locates and interacts with form fields such as Full Name, Contact Number, Email ID, and others, submitting the data automatically.

### Prerequisites
- Python 3.x
- Selenium Python Library
- Chrome WebDriver compatible with the installed Chrome version

### Installation
1. Clone the repository:
   ```bash
   git clone git@github.com:AVINASH0052/googleForm.git
   ```
2. Install dependencies:
   ```bash
   pip install selenium
   ```
3. Download ChromeDriver:
   - Ensure it matches the installed version of Chrome.
   - Place the executable in a known directory.

### Configuration
1. Update the `webdriver_path` variable in the script to the location of ChromeDriver.
2. Modify the `form_data` dictionary with the required input values.

### Usage
1. Run the script:
   ```bash
   python main.py
   ```
2. The browser will open and interact with the Google Form.
3. The form will be filled and submitted automatically.

### Features
- Automates form interaction using Selenium.
- Configurable input fields through a Python dictionary.
- Includes error handling for element loading issues.

### Limitations
- Designed for static Google Forms.
- May require updates if the form structure changes.

### License
This project is open-source and available under the MIT License.

