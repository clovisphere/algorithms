package jump

import (
	"fmt"
	"testing"
)

func TestCharacterJump(t *testing.T) {
	cases := []struct {
		n        int
		s        []int
		expected bool
	}{
		{3, []int{0, 1, 0, 0, 0, 1, 0}, true},
		{1, []int{0, 1}, false},
		{4, []int{0, 1, 1, 0, 1, 0, 0, 0, 0}, false},
		{0, []int{}, false},
		{2, []int{0, 0}, true},
	}

	for _, tt := range cases {
		t.Run(fmt.Sprintf("when given %v and %v", tt.n, tt.s), func(t *testing.T) {
			got := characterJump(tt.n, tt.s)
			if got != tt.expected {
				t.Errorf("got: %v; expected: %v", got, tt.expected)
			}
		})
	}
}
