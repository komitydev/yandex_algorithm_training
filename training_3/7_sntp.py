start = list(map(int, input().split(':')))
s_start = list(map(int, input().split(':')))
end = list(map(int, input().split(':')))

sec_in_day = 24*60*60

start = start[0] * 3600 + start[1] * 60 + start[2]
s_start = s_start[0] * 3600 + s_start[1] * 60 + s_start[2]
end = end[0] * 3600 + end[1] * 60 + end[2]

if start > end:
    end += sec_in_day

diff = (end - start) / 2
if diff - int(diff) >= 0.5:
    diff = int(diff) + 1
else:
    diff = int(diff)

s_end = s_start + diff

if s_end > sec_in_day:
    s_end -= sec_in_day

hours = s_end // 3600
minutes = (s_end - (hours * 3600)) // 60
hours = hours % 24
seconds = s_end % 60

if hours < 10:
    hours = '0' + str(hours)
if minutes < 10:
    minutes = '0' + str(minutes)
if seconds < 10:
    seconds = '0' + str(seconds)

print(f"{hours}:{minutes}:{seconds}")
