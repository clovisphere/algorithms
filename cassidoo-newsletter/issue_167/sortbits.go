// Given an integer array arr, sort the integers in arr in ascending
// order by the number of 1's in their binary representation and return
// the sorted array

package sortbit

import (
	"sort"
	"strconv"
	"strings"
)

func sortBits(arr []int) []int {
	sort.SliceStable(arr, func(i, j int) bool {
		return strings.Count(
			strconv.FormatInt(int64(arr[i]), 2), "1") < strings.Count(
			strconv.FormatInt(int64(arr[j]), 2), "1")
	})
	return arr
}
