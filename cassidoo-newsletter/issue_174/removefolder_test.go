package rm

import (
	"reflect"
	"testing"
)

func TestRemoveFolder(t *testing.T) {
	testCases := []struct {
		folders  []string
		name     string
		expected []string
	}{
		{[]string{"/a", "/a/b", "/c/d", "/c/d/e", "/c/f", "/c/f/g"}, "c", []string{"/a", "/a/b"}},
		{[]string{"/a", "/a/b", "/c/d", "c/d/e", "c/f", "c/f/g"}, "d", []string{"/a", "/a/b", "/c", "c/f", "c/f/g"}},
	}
	for _, tt := range testCases {
		got := removeFolder(tt.folders, tt.name)
		if !reflect.DeepEqual(got, tt.expected) {
			t.Errorf("got: %v; expected: %v", got, tt.expected)
		}
	}
}
