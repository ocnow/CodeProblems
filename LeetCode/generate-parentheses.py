class Solution:
	def bfs_genParanthesis(self,left:int,right:int,st:str,ans:list,size:int):

		if(left == 0 and right == 0):
			ans.append(st)
			return

		if(right < left or left <0 or right <0):
			return
		
		#st.append("(")
		self.bfs_genParanthesis(left-1,right,st + "(",ans,size)

		self.bfs_genParanthesis(left,right-1,st + ")",ans,size)
	
	def generateParenthesis(self, n: int) -> list[str]:
		ans = []
		self.bfs_genParanthesis(n,n,"",ans,n)
		return ans