package sortbit

import (
	"reflect"
	"testing"
)

var testCases = []struct {
	given    []int
	expected []int
}{
	{[]int{0, 3, 4}, []int{0, 4, 3}},
	{[]int{0, 1, 2, 3, 4, 5, 6, 7, 8}, []int{0, 1, 2, 4, 8, 3, 5, 6, 7}},
}

func TestSortBits(t *testing.T) {
	for _, test := range testCases {
		ans := sortBits(test.given)
		if !reflect.DeepEqual(ans, test.expected) {
			t.Errorf("SortBits(%v) = %v; expected: %v", test.given, ans, test.expected)
		}
	}
}
