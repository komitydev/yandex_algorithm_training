pupils = int(input())
vars = int(input())
row = int(input()) - 1
posinrow = int(input()) - 1 # if 0 then right

first_pos = (row) * 2 + posinrow

sec_pos1 = first_pos + vars
sec_pos2 = first_pos - vars

if sec_pos1 >= pupils and sec_pos2 < 0:
    sec_pos = -1
elif sec_pos1 < pupils and sec_pos2 >= 0:
    rows1 = sec_pos1 // 2
    rows2 = sec_pos2 // 2
    
    if (rows1 - row) <= (row - rows2):
        sec_pos = sec_pos1
    else:
        sec_pos = sec_pos2
elif sec_pos1 < pupils:
    sec_pos = sec_pos1
else:
    sec_pos = sec_pos2

if sec_pos == -1:
    print(-1)
else:
    final_row = (sec_pos // 2) + 1
    print(final_row)
    print(1 if (sec_pos % 2) == 0 else 2)
