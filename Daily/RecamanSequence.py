def iHit(nToHit,maxItr):
    pad = 0
    itr = 'Not hit'
    hits = [0]
    for i in range(1,maxItr+1):
        mx = pad - i
        px = pad + i
        if mx not in hits and mx > 0:
            hits.append(mx)
            pad = mx
        else:
            hits.append(px)
            pad = px
        if pad == nToHit:
            itr = i
            break
    return pad,itr,hits
                    
