/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let map = new Map();
    for (let i = 0; i < nums.length; i++) {
        const para = target - nums[i];
           if (map.has(para)) {
         return [map.get(para), i];
        }

        
        map.set(nums[i], i);
    }
};









