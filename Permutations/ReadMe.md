### When to use a for loop in recursion
Use a for loop in recursion when you want to:

process a list of items at each depth

Good example
If you’re exploring every possible seat assignment for a seating chart, a for loop is useful because you want to test each person in each position.

### When not to use a for loop
Don’t use a for loop when:

you’re branching into two clear choices
you only need to choose “include” or “skip” the current item
the recursive structure is better expressed as a direct call on the next index
For example, the power set problem is better with no loop

###
Rule of thumb
Use a for loop when you are iterating through options at a level.
Use recursion without a loop when the decision is “do this” or “don’t do this” on the next step.