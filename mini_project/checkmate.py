# checkmate.py
def checkmate(board):
    rows = board.strip().splitlines()
    size = len(rows)

    # ตรวจ error: ต้องเป็นสี่เหลี่ยมจัตุรัส
    if size == 0 or any(len(r) != size for r in rows):
        print("Error")
        return

    # หา King
    kings = [(r, c) for r in range(size) for c in range(size) if rows[r][c] == 'K']
    if len(kings) != 1:
        print("Error")
        return
    kr, kc = kings[0]

    # 1) Pawn
    for dc in (-1, 1):
        r, c = kr + 1, kc + dc
        if 0 <= r < size and 0 <= c < size and rows[r][c] == 'P':
            print("Success")
            return

    # 2) ทิศทางของ Bishop/Rook/Queen
    diagonals = [(-1,-1), (-1,1), (1,-1), (1,1)]
    straights = [(-1,0), (1,0), (0,-1), (0,1)]

    def scan(directions, attackers):
        for dr, dc in directions:
            r, c = kr + dr, kc + dc
            while 0 <= r < size and 0 <= c < size:
                if rows[r][c] in attackers:
                    return True
                if rows[r][c] in "PBRQK":   # ติดตัวขวาง
                    break
                r += dr
                c += dc
        return False

    if scan(diagonals, "BQ") or scan(straights, "RQ"):
        print("Success")
    else:
        print("Fail")