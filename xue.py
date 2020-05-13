for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if (i != k) and (i != j) and (j != k):
                print i, j, k
                print str(i+k)
                
def get_picsearch_imgpath(imagepath):
    picsearch_imgpath=os.path.join(path, imagepath)
    picname=picsearch_imgpath.split('/')[-1]

    return picsearch_imgpath
