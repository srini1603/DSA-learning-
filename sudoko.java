package sudoko;

public class sudoko {
	private static int grid = 9; 
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		int [][] table =  { {3, 0, 6, 5, 0, 8, 4, 0, 0}, 
		         {5, 2, 0, 0, 0, 0, 0, 0, 0}, 
		         {0, 8, 7, 0, 0, 0, 0, 3, 1}, 
		         {0, 0, 3, 0, 1, 0, 0, 8, 0}, 
		         {9, 0, 0, 8, 6, 3, 0, 0, 5}, 
		         {0, 5, 0, 0, 9, 0, 6, 0, 0}, 
		         {1, 3, 0, 0, 0, 0, 2, 5, 0}, 
		         {0, 0, 0, 0, 0, 0, 0, 7, 4}, 
		         {0, 0, 5, 2, 0, 6, 3, 0, 0} };
		
		if(solve(table)) {
			printt(table);
		}
		
	}
	private static void printt(int[][] table) {
		for(int i =0;i<grid;i++) {
			if(i%3==0 && i!=0) {
				System.out.println("----------------");
			}
			for(int j=0;j<grid;j++) {
				if(j%3==0 && j!=0) {
					System.out.print("|");
				}
				System.out.print(table[i][j]);
			}
			System.out.println();
		}
		
	}
	private static boolean checkrow(int[][] table,int row,int num) {
		for(int i =0;i<grid;i++) {
			if(table[row][i]==num) {
				return true;
			}
		}
		return false;
	}
	private static boolean checkcol(int[][] table,int col,int num) {
		for(int i =0;i<grid;i++) {
			if(table[i][col]==num) {
				return true;
			}
		}
		return false;
	}
	private static boolean checkbox(int[][] table,int row,int col,int num) {
		int box_row = (row/3)*3;
		int box_col = (col/3)*3;
//		int box_row = row - row%3;
//		int box_col = col - col%3;
		for(int i =box_row;i<box_row+3;i++) {
			for(int j = box_col;j<box_col+3;j++){	
				if(table[i][j]==num) {
				return true;
				}
			}
		}
		return false;
	}
	private static boolean valid(int[][] table,int row,int col,int num) {
		return !checkrow(table,row,num) && 
				!checkcol(table,col,num) && 
				!checkbox( table, row,col,num);
	}
	
	private static boolean solve(int[][] table) {
		for(int i =0;i<grid;i++) {
			for(int j =0;j<grid;j++) {
				if(table[i][j]==0) {
					for(int num = 1 ;num<=grid;num++) {
						if(valid(table,i,j,num)) {
							table[i][j]=num;
							if(solve(table)) {
								return true;
							}
							else {
								table[i][j]=0;
							}
						}
					}
					return false;
				}	
			}
		}
		return true;
	}

}
