# checkmate.py

def checkmate(board): # ตรวจสอบว่ามีการเช็คหรือไม่
    rows = board.strip("\n").splitlines() # ลบ newline หน้าและหลังของsting แล้วแปลง string เป็น list
    size = len(rows)

    # ตรวจ error บอร์ดต้องเป็นสี่เหลี่ยมจัตุรัส
    if  1 > size or any(len(r) != size for r in rows): # กระดานน้อยกว่า 1 หรือ cols ไม่เท่ากับ rows 
        print("Error")
        return

    # หา King
    kings = []
    for r in range(size): # วนทีละแถว บนไปล่าง
        for c in range(size): # วนทีละคอลัมน์ในแถวนั้น ซ้ายไปขวา
            if rows[r][c] == 'K':
                kings.append((r, c)) # เก็บตำแหน่งเป็น (แถว, คอลัมน์) 
                
    if not len(kings) == 1: # เช็คว่ามี King ตัวเดียว
        print("Error")
        return
    kr, kc = kings[0] 

    # Pawn
    for dc in (-1, 1):
        r, c = kr + 1, kc + dc # r, c ของ pawn ที่กิน King ได้
        if 0 <= r < size and 0 <= c < size and rows[r][c] == 'P': # ตรวจสอบว่า pawn อยู่ในตำแหน่งที่กิน King ได้และอยู่ในกระดาน
            print("Success")
            return

    # Bishop, Rook, Queen
    diagonals = [(-1,-1), (-1,1), (1,-1), (1,1)] # ซ้ายบน, ขวาบน, ซ้ายล่าง, ขวาล่าง
    straights = [(-1,0), (1,0), (0,-1), (0,1)] # บน, ล่าง, ซ้าย, ขวา
    # ตวรจแต่ละทิศทาง
    def scan(directions, attackers):
        for dr, dc in directions:
            r = kr + dr,c = kc + dc # ตำแหน่งของking + ทิศทางที่ต้องการตรวจ
            while 0 <= r < size and 0 <= c < size:
                if rows[r][c] in attackers: # เจอตัวที่สามารถกิน King ได้
                    return True
                if rows[r][c] in "PBRQK":   # ติดตัวขวางที่กินkingไม่ได้
                    break
                r += dr # ก้าวไปช่องถัดไปในทิศเดิม row r(ใหม่) = r(เดิม) + dr
                c += dc # ก้าวไปช่องถัดไปในทิศเดิม column c(ใหม่) = c(เดิม) + dc
        return False

    if scan(diagonals, "BQ") or scan(straights, "RQ"):
        print("Success")
    else:
        print("Fail")