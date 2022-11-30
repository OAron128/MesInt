# struktúrába definiált változók:
# muvT = műveleti idő
# indT = indítási idő
# befT = befejezési idő

from struct import *
import time
import Tkinter
#packed_date = pack('muvT',i)

class Struct: # most ez lehet hülyeség és csak simán változo kell
    muvT = 0
    indT = 0
    befT = 0



def gepszerintGant(mat, n, m,s): #gépek alapján figyelt
    i,r=0
    for r in range(len(m)):
        print("\n munkahely: "+ r)
        print("\n # \t munka \t kezd \t muv \t bef.")
        for i in range(len(n)):
            print("\n"+i+"\t"+s[i]+"\t"+job[s[i]].StartT[r]+"\t"+mat[s[i]].ProcT[r]+"\t"+mat[s[i]].EndT[r]+"\t")


def munkaszerintGant(mat,n,m,s): #munkák alapján figyelt
    Struct.indT = time.time()
    i,r=0
    for i in range(len(n)):
        print("\n munka:"+i)
        print("\n # \t gep \t kezd \t muv \t bef.")
        for r in range(len(m)):
            print("\n"+i+"\t"+s[i]+"\t"+mat[s[i]].StartT[r]+"\t"+mat[s[i]].ProcT[r]+"\t"+mat[s[i]].EndT[r]+"\t")
    Struct.befT = time.time()

    Struct.muvT = indT - befT
        

#lehet grafikusan kéne
foablak = tkinter.Tk()

foablak.geometry("400x200")
foablak.title("Grafikus Gantt diagram")

cim=tkinter.Label(foablak, text="OK", font=("Arial",12),pady=10)
cim.pack()
    
foablak.mainloop()
