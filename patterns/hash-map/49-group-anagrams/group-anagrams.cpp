class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        /***
        pattern recognition: hashmap
        constraint: linear solution / nested
        output: 2d array
        state variables: hashmap
        transition:
        IF sorted word is in hashmap => pushback word into vector value
        IF sorted word is not => create new one
        **/

        unordered_map<string, vector<string>> freq;
        for (string s: strs){
            string temp = s;
            sort(s.begin(), s.end());
            freq[s].push_back(temp);
        }

        vector<vector<string>> bucket;
        for (const auto& kv: freq){
            bucket.push_back(kv.second);
        }

        return bucket;
    }
};