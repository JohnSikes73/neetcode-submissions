class TimeMap:

    def __init__(self):
        self.stack = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.stack[key].append((timestamp, value))
        # print(f'Adding key = {key}, timestamp = {timestamp}, value = {value}')
        # print(self.stack)

    def get(self, key: str, timestamp: int) -> str:

        # print(f'Searching in key = {key} for timestamp = {timestamp}')
        
        n = len(self.stack[key])
        # print(f'Current length of stack = {n}')
        if n == 0:
            return ''

        l = 0
        r = n - 1
        
        while l <= r:
            m = l + (r - l)//2
            t = self.stack[key][m][0]
            if timestamp == t:
                return self.stack[key][m][1]
            elif timestamp < t:
                r = m - 1
            else:
                l = m + 1
        
        return self.stack[key][r][1] if r >= 0 else ''
        
