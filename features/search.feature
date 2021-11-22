Feature: Perform advanced Search on GitHub for specified repository
  Scenario: Verify GitHub Page
    Given Launch the browser and navigate to Github web site
    Then verify the page title

  Scenario: Verify initial Search Results
    Given GitHub Search Page is open
    When search for value <react>
    Then expected result page is displayed