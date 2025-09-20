/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
     let result = 0;
    for (let numb of nums) {
        result ^= numb; 
    }
    return result;
    
};