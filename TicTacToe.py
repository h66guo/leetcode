class TicTacToe:

    def __init__(self, n: int):
        self.row=[0 for i in range(n)]
        self.col= [0 for i in range(n)]
        self.diag=0
        self.anti=0
        self.size=n
        

    def move(self, row: int, col: int, player: int) -> int:
    
        if player!=1: 
            player=-1
        self.row[row]+= player
        self.col[col]+=player
        if row==col: 
            self.diag+=player
            
        if col==self.size- row-1: 
            self.anti+=player
            
        if abs(self.row[row])==self.size or abs(self.col[col])==self.size or abs(self.diag)==self.size or abs(self.anti)==self.size:
            if player==1:
                return 1
            if player==-1: 
                return 2
        else:
            return 0
    

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
