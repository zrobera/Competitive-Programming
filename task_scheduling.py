class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1

        task_freq = sorted(freq.values(), reverse=True)

        max_freq = task_freq[0]
        num_slots = (max_freq - 1) * n

        for freq in task_freq[1:]:
            num_slots -= min(max_freq - 1, freq)

        num_slots = max(0, num_slots)

        total_intervals = len(tasks) + num_slots

        return total_intervals
