import heapq


class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        meetingCounts = [0] * n

        roomsAvailable = list(range(n))
        heapq.heapify(roomsAvailable)

        currentMeetings = []
        meetingMap = {}

        min_heap = list(map(lambda m: (m[0],tuple(m)), meetings))
        heapq.heapify(min_heap)

        t = 0

        while min_heap:
            while currentMeetings and currentMeetings[0][0] <= t:
                _, meeting = heapq.heappop(currentMeetings)
                room = meetingMap[meeting]
                heapq.heappush(roomsAvailable, room)
                del meetingMap[meeting]

            while roomsAvailable and min_heap and min_heap[0][0] <= t:
                _, meeting = heapq.heappop(min_heap)
                room = heapq.heappop(roomsAvailable)
                meetingCounts[room] += 1

                meeting = (t, meeting[1] - meeting[0] + t)
                heapq.heappush(currentMeetings, (meeting[1], meeting))
                meetingMap[meeting] = room

            t += 1

        return meetingCounts.index(max(meetingCounts))



if __name__ == "__main__":
    print(Solution().mostBooked(2, [[0,10],[1,5],[2,7],[3,4]]))