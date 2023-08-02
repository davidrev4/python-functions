nums1 = {
    "number1" : 1500,
    "number2" :1400,
    "number3" : 1300,
}
nums2 = []
for keys,values in nums1.items():
    if values > 1000:
        nums2.append(f"the result is now : {values - 1000}")
print(nums2)