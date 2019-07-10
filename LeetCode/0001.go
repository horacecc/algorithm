package solutions

// TwoSum return []int or nil
func TwoSum(nums []int, target int) []int {
	m := make(map[int]int)
	for key, value := range nums {
		if idx, ok := m[target-value]; ok {
			return []int{idx, key}
		}
		m[value] = key
	}
	return nil
}

// // TwoSum return []int or nil
// func TwoSum(nums []int, target int) []int {
// 	count := len(nums)
// 	for idx1 := 0; idx1 < count; idx1++ {
// 		for idx2 := idx1 + 1; idx2 < count; idx2++ {
// 			if nums[idx1]+nums[idx2] == target {
// 				return []int{idx1, idx2}
// 			}
// 		}
// 	}
// 	return nil
// }

