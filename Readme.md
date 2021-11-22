#Automation project for WebPage UI testing
This project is a sample solution for web page automation using Phyton, Behave, Selenium Webdriver.
It provides clear defined test scenarios that in plain English language using Gherkin format (Given, When, Then).
BDD scenarios are stored in `features` package and have extensions `.feature`

#Test Data
At this moment test data is stored xls file, that can be found in  `testdata` folder.
This data layer can be easily reconfigured to any other source.
Due to time limitation test data stored in the file is only related to initial interview task, however can be extended
to all fields in `Advanced Search` form to support full scale of testing of this functionality.

#Test Results
Test results are directed into log file in folder `logs` in the file `GitHubAutomationLog.log`.
Screenshots are stored under folder `screenshots`.
This project also is hooked to allure reports, however did not have enough time to tune it up.
Another option is to store results in Excel spreadsheet.

#How to run
If this is very first time in project root folder execute command `./install.bat`
After all packages are installed to start scenarios execute command `./run.bat`

I hope you like it :)
