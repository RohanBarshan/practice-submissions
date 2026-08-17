class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        # Max heap of task frequencies
        # Python has a min heap, so use negative frequencies
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0

        # Queue stores:
        # [remaining_count, time_when_cooldown_finishes]
        q = deque()

        while maxHeap or q:
            time += 1

            # Execute the most frequent available task
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)

                # If this task still has executions remaining,
                # put it into cooldown
                if cnt:
                    q.append([cnt, time + n])

            # If the task at the front has finished cooling down,
            # make it available again
            if q and q[0][1] == time:
                cnt, available_time = q.popleft()
                heapq.heappush(maxHeap, cnt)

        return time