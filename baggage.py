import sys
ll=[[2,5,3],[6,3,0,7],[8,3,6,0,9],[10,7,2,6,0,11],[8,5,12,3,9,0,13]]#,[10,3,14,7,0,11,4,15]]
def makemeans(start,end,ans,n):
	if n<8:
		for i in xrange(len(ll[n-3])):
			ans.append(ll[n-3][i]+start-1)
	else:
		ans.append(end-2)
		ans.append(start+2)
		makemeans(start+4,end-4,ans,n-4)
		ans.append(start-1)
		ans.append(end-1)
n=int(raw_input())
ans=[-1]
makemeans(1,2*n,ans,n)

for i in xrange(1,len(ans)):
	print ans[i],"to",ans[i-1]
"""
#Code for testing
for n in xrange(4,101):
	ans=[-1]
	makemeans(1,2*n,ans,n)
	ini=list('..'+'ba'*n)
	fini='a'*n+'b'*n+'..'

	for i in xrange(1,len(ans)):
			ini[ans[i]+1], ini[ans[i-1]+1] = ini[ans[i-1]+1], ini[ans[i]+1]
			ini[ans[i]+2], ini[ans[i-1]+2] = ini[ans[i-1]+2], ini[ans[i]+2]
	if ''.join(ini)!=fini or len(ans)!=n+1:
		print ''.join(ini),fini,len(ans)
		print n,"culprit"
		break
	else:
		print "YES" 
"""


