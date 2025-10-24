def two_in_love(petals_one, petals_two):
	return (petals_one % 2 == 0 and petals_two % 2 != 0) or (petals_one % 2 != 0 and petals_two % 2 == 0)