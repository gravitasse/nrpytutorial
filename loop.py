def loop1D(idxvar="i0",lower="0",upper="Nx0",incr="1",OpenMPpragma="#pragma omp parallel for",prefix=""):
    if not (isinstance(idxvar, str) and isinstance(lower, str) and
            isinstance(upper, str) and isinstance(incr, str) and isinstance(OpenMPpragma, str)):
        print("Error: all inputs to loop1D() must be STRINGS, and to loop() must be LISTS OF STRINGS")
        exit(1)
    OMPheader = ""
    if OpenMPpragma != "":
        OMPheader = OpenMPpragma + "\n"
    incrstr = "++"
    if incr != "1":
        incrstr = "+="+incr
    loopbody = prefix+"for(int "+idxvar+"="+lower+"; "+idxvar+"<"+upper+"; "+idxvar+incrstr+")"
    return OMPheader+loopbody+" {\n", prefix+"} // END LOOP: "+loopbody.replace(prefix,"")+"\n"

def loop(idxvar,lower,upper,incr,OpenMPpragma):
    if not (isinstance(idxvar,list) and isinstance(lower,list) and
            isinstance(upper, list) and isinstance(incr, list) and isinstance(OpenMPpragma, list)):
        print("Error: loop(idxvar,lower,upper,incr,OpenMPpragma) requires all inputs be lists")
        exit(1)
    if len(idxvar) != len(lower) or len(lower) != len(upper) or len(upper) != len(incr) or len(incr) != len(
            OpenMPpragma):
        print("Error: loop(idxvar,lower,upper,incr,OpenMPpragma) requires all inputs be lists OF THE SAME LENGTH")
        exit(1)
    prefix = ""
    header = ""
    footerarray = []
    for i in range(len(idxvar)):
        headerstr,footerstr = loop1D(idxvar[i],lower[i],upper[i],incr[i],OpenMPpragma[i],prefix)
        header += headerstr
        footerarray.append(footerstr)
        prefix += "    "
    footer = ""
    for i in range(len(idxvar)-1,-1,-1):
        footer += footerarray[i]
    return header,footer

loopheader,loopfooter = loop(idxvar=["i0","i1"],lower=["0","0"],upper=["Nx0","Nx1"],incr=["1","1"],
                             OpenMPpragma=["", "#pragma omp parallel for"])
loopheader,loopfooter = loop(idxvar=["i0","i1"],lower=["0","0"],upper=["Nx0","Nx1"],incr=["1","1"],
                             OpenMPpragma=["", "#pragma omp parallel for"])
print(loopheader+loopfooter)