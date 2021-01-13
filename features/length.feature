Feature: Length checking
    Checking if the lengths of elements are equal

    @length
    Scenario: All of two Elements are the same
        Given two inputs
        """
        miszczu,miszczu
        """
        When they are the same
        Then returns True

    @length
    Scenario: All of two Elements are words and letters
        Given two inputs
        """
        mit5ub1sh1,sasin70mln
        """
        When word with letters
        Then returns True

    @length
    Scenario: Three Elements and one is shorter
        Given three inputs
        """
        linux,macos,windows
        """
        When one word is shorter
        Then returns False

    @length
    Scenario: Three Elements with equal lengths
        Given three inputs
        """
        king,kong,jane
        """
        When their lengths are equal
        Then returns True

    @length
    Scenario: Elements are none
        Given Nones
        """
        None,None,None
        """
        When they are null
        Then Enter correct words

    @length
    Scenario: Elements are just letters
        Given two numbers
        """
        134,245
        """
        When their lengths are the same
        Then returns True


    @length
    Scenario: All Elements are words with different length
        Given two words
        """
        hyundai,audi
        """
        When their lengths are different
        Then returns False

    @length
    Scenario: No words inputed
        Given nothing
        Then Enter correct words