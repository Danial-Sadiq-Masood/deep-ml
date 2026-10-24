
def orthogonal_projection(v, L):
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	dot = sum([p1 * p2 for p1,p2 in zip(v,L)])
	l_norm_sq = sum([p1 * p2 for p1,p2 in zip(L,L)])

	proj = [dot/l_norm_sq * l for l in L]

	return proj
