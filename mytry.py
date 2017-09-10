import svdRec
import numpy as np
# Data = svdRec.loadExData()
# U,Sigma,VT = np.linalg.svd(Data)
# print(Sigma)

# myMat = np.mat(svdRec.loadExData())
# print(svdRec.pearsSim(myMat[:,0],myMat[:,0]))
# print(svdRec.pearsSim(np.mat[:,0],myMat[:,0]))

# myMat = np.mat(svdRec.loadExData())
# myMat[0,1] = myMat[0,0] = myMat[1,0] = myMat[2,0] =4
# myMat[3,3] = 2
# print(myMat)
# print(svdRec.recommend(myMat,2))

myMat = np.mat(svdRec.loadExData2())
print(myMat)
print(svdRec.recommend(myMat,1,estMethod=svdRec.svdEst))

# svdRec.imgCompress(2)