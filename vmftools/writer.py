def VmfWrite(vmf, filename):
    f = open(filename, "w")
    f.write(repr(vmf))
