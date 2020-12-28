package find

import "testing"

func TestFind2020(t *testing.T) {
	testCases := []struct {
		pattern  string
		expected int
	}{
		{"2020", 0},
		{"200020", -1},
		{"2220000202220020200", 14},
		{"", -1},
		{"0002020", 3},
	}
	for _, tc := range testCases {
		got := find2020(tc.pattern)
		if got != tc.expected {
			t.Errorf("got: %v; expected: %v", got, tc.expected)
		}
	}
}
