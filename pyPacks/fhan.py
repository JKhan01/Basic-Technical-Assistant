

class fhan:
    def  __init__(self,t):
        self.t=t
    def f_handle(self):
        try:
            if (("open") or ("open file")) in self.t:
                r=self.t.replace("open file","")
                if "read mode" in r:    
                    y_01=r.replace("in read mode","")
            
                    f=open(y_01 + ".txt","rt")
                elif ("write mode") in self.t:
                    #r=self.t.replace("open file","")
                    y_02=r.replace("in write mode","")
                    f=open(y_02 + ".txt","wt")
                else:
                    print("check out conditions!!")
            elif ("create file") in self.t:
                f=open(self.t.replace("create file","")+".txt","x")
            else :
                print ("work not done!")
        except:
            ob.say("file does not exist!")
            ob.runAndWait()

