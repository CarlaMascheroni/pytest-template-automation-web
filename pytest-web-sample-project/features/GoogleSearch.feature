Feature: GoogleSearch

  @example
  Scenario Outline: The client search by "A utomation"
    Given The client is in google page
    When The client search for word <word>
    Then The client verify that results are shown properly
    Examples:
      | word       |
      | Automation |
      | Lippia     |
      | Docker     |
      | crowdar    |
      | Automation |
