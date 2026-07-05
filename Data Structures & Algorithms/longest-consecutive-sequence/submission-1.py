class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        # Set longest sequence to 0
        longest_seq = 0
        
        # For each element, Check whether the left most element exists (ele - 1)
        for number in nums_set:
            # if left most element does not exists (ele - 1)
            if (number - 1) not in nums_set:
                # Initialize current sequence length
                current_seq_length = 1
                while (number + current_seq_length) in nums_set:
                    current_seq_length += 1
            
                # Check whether the current sequence length is greater than longest length 
                longest_seq = max(longest_seq, current_seq_length)
            
        return longest_seq
