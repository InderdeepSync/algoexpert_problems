import heapq

class Solution(object):

    def busiestServers(self, k, arrival, load): # TimeLimitExceeded butATM
        info = [False] * k
        r_count = [0] * k

        end_times = []

        i = 0
        while i < len(arrival):
            t = arrival[i]
            while end_times and end_times[0][0] <= t:
                _, server = heapq.heappop(end_times)
                info[server] = False

            r_load = load[i]

            if not all(info):
                temp = 0
                while info[(i + temp) % k]:
                    temp += 1

                server = (i + temp) % k
                heapq.heappush(end_times, (t + r_load, server))
                r_count[server] += 1
                info[server] = True

            i += 1


        max_val = max(r_count)
        result = []
        for index, val in enumerate(r_count):
            if val == max_val:
                result.append(index)
        return result


if __name__ == '__main__':
    print(Solution().busiestServers(3 ,[1,2,3], [10, 11, 12]))