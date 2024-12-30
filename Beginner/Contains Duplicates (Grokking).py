def containsDuplicate(nums):    
      k = set(nums)

      if len(nums) == len(k) :
            return False
            
      return True

#------------------------------------

def containsDuplicate(nums):

      counts = {}
      for num in nums:
            if num not in counts:
                  counts[num] = 1
            else:
                  return True
                  # counts[num] += 1

      # for count in counts:
      #       if counts[count] > 1:
      #             return True

      return False


nums = [1,2,3,4,7,2,8,9]


print(containsDuplicate(nums))

#---------------------------------------
def containsDuplicate(nums):
      unique_set = set() # Use set to store unique elements

      for x in nums:
            if x in unique_set: # If the set already contains the current element, return True
                  return True
            unique_set.add(x) # Add the current element to the set
      
      return False

#----------------------------------------
def contains_duplicate(nums):
      # this takes O(n logn) time so others are better since they only take O(n) time
      nums.sort() # sort the array
      # use a loop to compare each element with its next element
      for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]: # if any two elements are the same, return true
                  return True
      return False # if no duplicates are found, return false
