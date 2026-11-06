class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # Build adjacency list:
        # course -> list of prerequisites it needs
        adj = {}

        # Create an empty list for every course
        for i in range(numCourses):
            adj[i] = []

        # [src, dst] means src requires dst
        # Example: [0, 1] means 0 -> 1
        for src, dst in prerequisites:
            adj[src].append(dst)

        # visit = courses we have COMPLETELY finished checking
        visit = set()

        # path = courses in our CURRENT DFS path
        # Used to detect cycles
        path = set()

        def dfs(src):

            # If src is already in our CURRENT path,
            # we came back to the same course -> CYCLE
            if src in path:
                return False

            # If we already completely checked src before,
            # we know it is safe
            if src in visit:
                return True

            # We are now currently exploring src
            path.add(src)

            # Check every prerequisite of src
            for neighbor in adj[src]:

                # If any prerequisite leads to a cycle,
                # we cannot finish all courses
                if not dfs(neighbor):
                    return False

            # We finished exploring src, so remove it
            # from the CURRENT DFS path
            path.remove(src)

            # src is now completely checked and safe
            visit.add(src)

            # No cycle was found from src
            return True

        # Run DFS from every course
        # This is important because the graph
        # could have disconnected components
        for i in range(numCourses):

            # If any course leads to a cycle,
            # we cannot finish all courses
            if not dfs(i):
                return False

        # Checked every course and found no cycle
        return True