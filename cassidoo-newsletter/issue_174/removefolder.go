//Given a list of folders in a filesystem and the
//name of a folder to remove, return the new list
//of folders after removal:-)
package rm

import (
	"fmt"
	"regexp"
	"strings"
)

func removeFolder(folders []string, name string) []string {
	var _new []string // the newly created list after removal
	validTopLevelFolder := map[string]bool{}
	r := regexp.MustCompile(fmt.Sprintf(`^\/[^%v]\/`, name))
	for _, folder := range folders {
		if !strings.Contains(folder, name) {
			_new = append(_new, folder)
		} else {
			// is 'name' a top-level folder?
			indices := r.FindStringIndex(folder)
			if indices != nil {
				tmp := folder[:indices[1]-1]
				if _, ok := validTopLevelFolder[tmp]; !ok {
					validTopLevelFolder[tmp] = true
					_new = append(_new, tmp)
				}
			}
		}
	}
	return _new
}
