from homework2.score_keeper import ScoreKeeper


def test_add_points() -> None:
    # Step 1: Instantiate
    score_keeper_object = ScoreKeeper()

    ###############################
    ## Specify inputs from domain #
    ###############################
    # Step 3: Specity the input
    input = 2
    # Step 4: Set state in the object
    score_keeper_object.total_score = 10
    score_keeper_object.multiplier = 3

    #########################################
    ## Specify expected outputs in codomain #
    #########################################
    # Step 5: Specify expected number of points returned by function
    expected_return = 6
    # Step 6: Specify expected change in internal state
    expected_total_score = 16

    # Step 7: Call object method
    returned = score_keeper_object.add_points(input)

    #######################################
    ## Check values returned by function ##
    #######################################
    # Step 8: Check return value
    assert returned == expected_return
    # Step 9: Check modified state
    assert score_keeper_object.total_score == expected_total_score