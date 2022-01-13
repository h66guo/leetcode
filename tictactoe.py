class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        row=[0]*3
        col=[0]*3
        dig=0
        anti=0
        size=3
        player=1
        for i in range(len(moves)): 
            
            row[moves[i][0]]+=player
            col[moves[i][1]]+=player
            
            if moves[i][0]==moves[i][1]: 
                dig+=player
                
            if moves[i][0]+moves[i][1]==size-1:
                anti+=player
         
            
            if abs(row[moves[i][0]])==size or abs(col[moves[i][1]])==size or abs(dig)==size or abs(anti)==size: 
                if player==1: 
                    return "A"
                else:
                    return "B"
            player*=-1
        if len(moves)==size*size:
            return "Draw"
        else:
            return "Pending"
