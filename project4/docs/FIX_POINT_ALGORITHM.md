# Fix-point Algorithm

Use a fixed-point algorithm to repeatedly evaluate the rules. If an iteration over the rules changes the database by adding at least one new tuple to at least one relation in the database, the algorithm evaluates the rules again. If an iteration over the rules does not add a new tuple to any relation in the database, then the fixed-point algorithm terminates.

An easy way to tell if any tuples were added to the database is to count the number of tuples in the database both before and after evaluating the rules. If the two counts are different, something changed, and the rules need to be evaluated again. However, this is computationally inefficient. A more efficient way is to use the return value of `set.insert`, which includes a boolean that is true if the inserted element was new to the set.
