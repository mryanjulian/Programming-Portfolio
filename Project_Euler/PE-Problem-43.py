#This problem computes the sum of all 0 to 9 pandigital numbers with the property that d2d3d4 is divisible by 2, d3d4d5 is divisible by 3, d4d5d6 is divisible by 5, ..., d8d9d10 is divisible by 17, where dk denotes the kth digit.

sum = 0
for d1 in range(0,10):
	for d2 in range(0,10):
		if d2 not in {d1}:
			for d3 in range(0,10):
				if d3 not in {d1,d2}:
					for d4 in range(0,10):
						if d4 not in {d1,d2,d3} and d4%2 == 0:
							for d5 in range(0,10):
								if d5 not in {d1,d2,d3,d4} and (d3+d4+d5)%3 == 0:
									for d6 in range(0,10):
										if d6 not in {d1,d2,d3,d4,d5} and d6%5 == 0:
											for d7 in range(0,10):
												if d7 not in {d1,d2,d3,d4,d5,d6} and (100*d5+10*d6+d7) % 7 == 0:
													for d8 in range(0,10):
														if d8 not in {d1,d2,d3,d4,d5,d6,d7} and (100*d6+10*d7+d8) % 11 == 0:
															for d9 in range(0,10):
																if d9 not in {d1,d2,d3,d4,d5,d6,d7,d8} and (100*d7+10*d8+d9) % 13 == 0:
																	for d10 in range(0,10):
																		if d10 not in {d1,d2,d3,d4,d5,d6,d7,d8,d9} and (100*d8+10*d9+d10) % 17 == 0:
																			sum += d10+10*d9+100*d8+1000*d7+10000*d6+100000*d5+1000000*d4+10000000*d3+100000000*d2+1000000000*d1

print sum
