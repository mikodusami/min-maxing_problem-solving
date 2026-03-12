class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {


        /**
        state: sorted_vector of pairs, totalCarFleets, longestTimeToGetToDestination
        transitions:
        - sorted_vector_of_pairs: used to hold the pos and speed of a single car together
        - totalCarFleets: changes when the next car takes a longer time to get to the target (++). a new fleet is formed only if the current car takes longer than the fleet in front of it because since we are only worried about new fleet creations, a car that takes longer time than the last one cannot possibly catch up to the next fleet so a new one is formed
        - longestTimeToGetToDestination: initialized as the time it takes the current car to reach the target. Updates when the next car takes a longer time than the currentLongestTime to reach the destination.

        ERR IN THINKING: ended up thinking about how a car would join a car fleet instead of thinknig how a car won't need any cars to join it.
        **/

        int n = position.size();
        int totalCarFleets = 1; // there will always be a car fleet
        vector<pair<int, int>> cars;
        for (int i = 0; i < n; i++) cars.push_back({position[i], speed[i]});
        sort(cars.rbegin(), cars.rend());
        double longestTimeToGetToDest = (double)(target - cars[0].first) / cars[0].second;
        for (int i = 1; i < n; i++){
            double currLongTimeToDest = (double)(target - cars[i].first) / cars[i].second; 
            if (currLongTimeToDest > longestTimeToGetToDest){
                // the current car cant catch up and another fleet needs to be created
                totalCarFleets += 1;
                longestTimeToGetToDest = currLongTimeToDest;
            }

        }
        
        return totalCarFleets;

    }

};