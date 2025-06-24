import numpy as np
from PIL import Image


def eigen(A,k):
    #Menghitung nilai eigen dan vektor eigen dengan QR decomposistion dan Power Iteration
    n, m = A.shape
    Q = np.random.rand(n, k)
    Q, _ = np.linalg.qr(Q)
    Q_prev = Q
 
    for i in range(10):
        Z = np.dot(A,Q)
        Q, R = np.linalg.qr(Z)

        err = ((Q - Q_prev) ** 2).sum()
        Q_prev = Q

        if err < 1e-3:
            break

    return np.diag(R), Q


def svd(A,ratio):
    #Memfaktorkan matriks A dengan metode SVD
    #Return nilai matriks SVD yang sudah dikompresi dan sudah dikalikan kembali

    # Copy ukuran matriks
    m,n = A.shape
    
    # Menghitung AtA untuk mencari nilai singular dan vektor V
    AtA = np.dot(np.transpose(A), A)

    # Mendapatkan eigen value dan eigen vektor
    Sv, V = eigen(AtA,n)

    # Mengurutkan eigen value dan eigen vector
    Sv = np.sqrt(np.abs(Sv))
    idx = Sv.argsort()[::-1]
    Sv = Sv[idx]
    V = V[:,idx]
    Sv = Sv[Sv != 0.0]
    k = len(Sv)
    
    #Membentuk matriks U
    U = np.dot(A,V[:,:k])
    for i in range (k):
        U[:,i] = U[:,i]/Sv[i]
            
    # Membentuk matriks V transpose  
    Vt = np.transpose(V)[:k,:]

    # Membentuk matriks sigma
    S = np.zeros((k, k))
    S[:k, :k] = np.diag(Sv)

    #Membuat matriks untuk image baru dari tiga matriks yang sudah dikompresi
    U,S,Vt,diff = compress(U,S,Vt,ratio)
    reconimage = np.dot(U, np.dot(S, Vt))
    return reconimage,diff
    

def compress(u,sigma,v,ratio):
    #Memperkecil ukuran matriks sesuai rasio terhdap banyaknya nilai eigen
    m = len(u)
    n = len(v[0])
    k = len(sigma)
    ratio = (ratio*k)//100
    uNow = u[:,:ratio]
    sigmaNow = sigma[:ratio,:ratio]
    vNow = v[:ratio,:]
    diff = ratio*(m+n+1)*100/(m*n)
    return uNow,sigmaNow,vNow,diff

def pixelDifference(img1, img2):
    dif = 0
    pairs = zip(img1.getdata(), img2.getdata())
    if len(img1.getbands()) == 1:
        for p1,p2 in pairs :
            if p1 != p2 :
                dif = dif + 1
    else:
        for p1,p2 in pairs :
            for c1,c2 in zip(p1,p2):
                if c1 != c2 :
                    dif = dif + 1
    ncomponents = img1.size[0] * img1.size[1] * 3
    print ("Difference (percentage):", (dif * 100) / ncomponents)


def compressImagePNG(filename,ratio):

    img = Image.open(filename)
    img = img.convert("RGBA")
    data = np.asarray(img)
    data = data.astype(float)


    r, g, b, s = data[:, :, 0], data[:, :, 1], data[:, :, 2], data[:, :, 3]

    rNow,rdiff = svd(r,ratio)
    rNow = np.clip(rNow,0,255)
    rNow = Image.fromarray(rNow)
    rNow = rNow.convert("L")
    gNow,gdiff = svd(g,ratio)
    gNow = np.clip(gNow,0,255)
    gNow = Image.fromarray(gNow)
    gNow = gNow.convert("L")
    bNow,bdiff = svd(b,ratio)
    bNow = np.clip(bNow,0,255)
    bNow = Image.fromarray(bNow)
    bNow = bNow.convert("L")
    s = Image.fromarray(s)
    s = s.convert("L")

    newImg = Image.merge("RGBA", (rNow,gNow,bNow,s))
    print ("Pixel Difference (percentage):", bdiff)
    #pixelDifference(img, newImg)
    return newImg, round(bdiff, 2)


def compressImagenonPNG(filename,ratio):

    img = Image.open(filename)
    img = img.convert("RGB")
    data = np.asarray(img)
    data = data.astype(float)


    r, g, b = data[:, :, 0], data[:, :, 1], data[:, :, 2]

    rNow,rdiff = svd(r,ratio)
    rNow = np.clip(rNow,0,255)
    rNow = Image.fromarray(rNow)
    rNow = rNow.convert("L")
    gNow,gdiff = svd(g,ratio)
    gNow = np.clip(gNow,0,255)
    gNow = Image.fromarray(gNow)
    gNow = gNow.convert("L")
    bNow,bdiff = svd(b,ratio)
    bNow = np.clip(bNow,0,255)
    bNow = Image.fromarray(bNow)
    bNow = bNow.convert("L")

    newImg = Image.merge("RGB", (rNow,gNow,bNow))
    print ("Pixel Difference (percentage):", bdiff)
    #pixelDifference(img, newImg)
    return newImg, round(bdiff, 2)


def compressImage(filename, fileExt, ratio):
    if fileExt == ".png":
        compressedName, diff = compressImagePNG(filename, ratio)
    else:
        compressedName, diff = compressImagenonPNG(filename, ratio)
    return compressedName, diff

# file = 
# filenameonly, fileExt = os.path.splitext(filename)
# hasil, r = compressImage("/Users/arikrayi/Downloads/logo-ig-instagram-windows-phone-all-you-need-know-9.png",5)
# hasil.show()
