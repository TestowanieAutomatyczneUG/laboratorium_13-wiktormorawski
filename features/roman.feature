Feature: Roman

    Scenario: OutPut is III
        Given Roman is running
        When I input "3"
        Then I get "III"

    Scenario: OutPut is VII
        Given Roman is running
        When I input "7"
        Then I get "VII"


    Scenario: OutPut is XIII
        Given Roman is running
        When I input "13"
        Then I get "XIII"

    Scenario: OutPut is L
        Given Roman is running
        When I input "50"
        Then I get "L"

    Scenario: OutPut is XLIX
        Given Roman is running
        When I input "49"
        Then I get "XLIX"

    Scenario: OutPut is LXX
        Given Roman is running
        When I input "70"
        Then I get "LXX"

    Scenario: Input is negative int
        Given Roman is running
        When I input "-50"
        Then I get "Please pass positive number"

    Scenario: Input is not int
        Given Roman is running
        When I input "wiktor"
        Then I get "Please pass correct arabic number"



