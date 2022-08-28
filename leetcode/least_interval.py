from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # count frequencies
        counter = Counter(tasks)
        counts = counter.values()
        # get most frequent
        max_count = max(counts)
        # get number of tasks that are the most frequent
        num_max_counts = sum([1 for i in counts if i == max_count])
        # max wait is (max_count - 1) * wait time + remaining tasks if we need idle time
        min_possible = num_max_counts + (max_count - 1) * (n + 1)
        # if no idle time it is just the length of tasks
        return max(len(tasks), min_possible)
    
if __name__ == "__main__":
    task = ["A","A","A","B","B","B"]
    n = 2
    print(Solution().leastInterval(task, n))
