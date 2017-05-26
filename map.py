# -*- coding: utf-8 -*-

import string

def trans(s):
  intab = string.ascii_lowercase
  outab = string.ascii_lowercase[2:] + string.ascii_lowercase[0:2]
  tab = string.maketrans(intab, outab)
  return s.translate(tab)


if __name__ == "__main__":
    s = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    print trans(s)
    print trans("map")