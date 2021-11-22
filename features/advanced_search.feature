Feature: Advanced Search on GitHub for specified repository <https://github.com/mvoloskov/decider> using Chrome browser should be successful
  Scenario: Expected repository can be found by performing advanced search on github website
    Given github home page is open using Chrome browser
    When search is performed for keyword <react>
    Then page with multiple results is displayed
    When user clicks on <Advanced Search>
    Then advanced search page is displayed
    When user selects 'Javascript' in <Written in this language> dropbox under <Advanced options>
    And user enters value '>45' in <With this many stars> field under <Repositories options>
    And user selects value 'Boost Software License 1.0' in <With this license> dropbox under <Repositories options>
    And user enters value '>50' in <With this many followers> field under <Users options>
    And user clicks on <Search> button
    Then <mvoloskov/decider> repository is found as a single result
    When user clicks on found repository link
    Then repository page is displayed
    And First three hundred characters match expected and printed in automation log file


