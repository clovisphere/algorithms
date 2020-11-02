package jump

//return true or false if you can jump n times
//to the end of s without hitting an obstacle.
func characterJump(n int, s []int) bool {
	if len(s) < 1 || n > len(s) {
		return false
	}
	for len(s) > n {
		s = s[n:]
		if s[0] == 1 {
			return false
		}
	}
	return true
}
