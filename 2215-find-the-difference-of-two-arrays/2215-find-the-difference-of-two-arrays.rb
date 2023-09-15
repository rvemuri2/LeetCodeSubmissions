def find_difference(nums1, nums2)
  a,b = nums1.uniq, nums2.uniq
  [a-b,b-a]
end