class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        /**
        pattern recognition: substring => sliding window
            - what type of window? fixed or dynamic => dynamic (must be a condition)
        pattern recognition: duplictaes => hashset or hashmap
        time constraints: 10^4 == linear solution
        goal: find the longest substring without duplicate characters
        intput: a string of chars
        output: the length of a substring
        state: maxLength, hashset, leftPointer, rightPointer
        transitions (when do we change the state):
        - alter the hashset when we see a new number to add to the set
        - alter the hashset when we see an old number that is in the set (we must remove it)
        - maxLength updates every iteration between left and right pointer
        - leftPointer only updates based on windwo condition: which is while the number[right] is in set, we must increment leftPointer and remove the number[left] from the set in order to maintain a window. 
        - window: the window shall only include unique letters
        **/

        unordered_set<char> seen;
        int maxL = 0;
        int left = 0;

        for (int right = 0; right < s.size(); right++){
            
            while (seen.count(s[right])){
                seen.erase(s[left]);
                left += 1;
            }
            seen.insert(s[right]);
            maxL = max(maxL, right - left + 1);
        }

        return maxL;
    }
};