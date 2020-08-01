class MyNumList:
    def __init__(self, nums):
        assert isinstance(nums, list), "nums必须是一个数组"
        self.nums = nums

    # +=
    def __iadd__(self, other):
        self.nums += other.nums
        return self

    def __imul__(self, other):
        min_len = min(len(self.nums), len(other.nums))

        for i in range(min_len):
            self.nums[i] *= other.nums[i]

        return self

    def __repr__(self):
        return "NumList( {} )".format(self.nums)


nums1 = MyNumList([1, 2])
nums2 = MyNumList([3, 4])

nums1 += nums2
"""
    before iadd : NumList( [1, 2] )
    after  iadd : NumList( [1, 2, 3, 4] )
"""
print(nums1)

nums2 *= MyNumList([2, 5])
"""
    before mul : NumList( [3, 4] )
    after mul :  NumList( [6, 20] )
"""
print(nums2)
