# Making the perfect squares from two blocks
#  Two blocks have faces {0, 1, 2, 3, 6, 8} and {1, 4, 9, 5, _, _}
#  From these we can make the perfect squares under 100:
#   01, 02, 04, 09, 16, 25, 36, 49, 64, 81
#  How many unque block face value combinations
#   are there that allow us to do this?
#  Note: Treat 6 as 9 since you can flip the block.

# Approach:
# 1) Which numbers must be on different blocks?
# 2) Come up with the basic block options
#    as above, leave all un-required faces blank (_)
# 3) Use these 'primitives' to compute the unique blocks

