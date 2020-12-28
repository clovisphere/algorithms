//You’re given a string of characters that are only 2s and 0s.
//Return the index of the first occurrence of “2020” without using
//the indexOf (or similar) function, and -1 if it’s not found in the string.
package find

func find2020(s string) int {
	for index, _ := range s {
		if index+4 <= len(s) && s[index:index+4] == "2020" {
			return index
		}
	}
	return -1 // if we get here, it means '2020' is not found in 's'
}
