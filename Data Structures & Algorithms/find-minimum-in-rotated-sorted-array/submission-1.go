import "slices"

func findMin(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	return slices.Min(nums)
}