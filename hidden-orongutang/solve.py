import chess, chess.pgn

class TransposeBord:
    def __init__(self):
        self.grid = {c: [] for c in 'abcdefgh'}
        self.cls = 'abcdefgh'

    def load_text(self, data):
        idx = 0
        for _ in range(8):
            for col in self.cls:
                char = data[idx] if idx < len(data) else ' '
                self.grid[col].insert(0, char)
                idx += 1

    def display(self):
        for rank in range(7, -1, -1):
            print(' '.join(self.grid[c][rank] for c in self.cls))
        print()

    def board_to_text(self):
        return ''.join(
            self.grid[c][r]
            for r in range(7, -1, -1)
            for c in self.cls
        )

    def swap(self, src, dst):
        sc, sr = src[0], int(src[1]) - 1
        dc, dr = dst[0], int(dst[1]) - 1
        self.grid[sc][sr], self.grid[dc][dr] = self.grid[dc][dr], self.grid[sc][sr]

    def apply_moves(self, seq):
        for mv in seq:
            self.swap(mv[:2], mv[2:])

    def revert(self, seq):
        self.apply_moves(reversed(seq))


def main():
    pgn_path = './2025-05-09_Alice_vs_Bob.pgn'
    txt_path = './message.txt'

    board = chess.Board()
    moves_list = []
    with open(pgn_path) as p:
        game = chess.pgn.read_game(p)
        for m in game.mainline_moves():
            board.push(m)
            moves_list.append(str(m))

    tb = TransposeBord()
    with open(txt_path) as f:
        tb.load_text(f.read())

    tb.display()
    tb.revert(moves_list)
    tb.display()
    print(tb.board_to_text())

if __name__ == '__main__':
    main()
