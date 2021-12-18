input = open("16-input.txt").read()

b = format(int(input, base=16), "0"+str((4*len(input)))+"b")

def toInt(a):
  t=0
  for bit in a:
    t = (t<<1) | int(bit)
  return t

def processPacket(b):
  # read version and store count
  var[0] += toInt(b[:3:])

  # read type
  t = toInt(b[3:6:])

  # print(f"version: {tmp}\ntype: {t}")

  # cut version and type
  b = b[6::]

  # literal value
  lv = ""
  if t == 4:

    while True:
      lv += b[1:5:]
      if b[0] == '1':
        b = b[5::]
      else:
        b = b[5::]
        break
    value = toInt(lv)
    # print(f"literal value of: {value}")

  # operator
  else:
    # length type 0, 15 bits = number of bits in subpackets
    if b[0] == '0':
      bcount = toInt(b[1:16:])

      b = b[16::]
      v = []
      while bcount > 0:
        # print(f"calling recursion for bit count {bcount}, current count: {len(b)}")
        lena = len(b)
        b, a = processPacket(b)
        v.append(a)
        bcount -= (lena - len(b))

    # length type 1, 11 bits = number of subpackets
    else:
      subCount = toInt(b[1:12:])

      b = b[12::]
      v = []
      for i in range(subCount):
        # print(f"calling {i+1} recursion out of {subCount} packets")
        b, a = processPacket(b)
        v.append(a)
  
  # count values
  if t == 0:
    print("sum of ",v)
    value = sum(v)
  elif t == 1:
    print("product of ",v)
    value = 1
    for x in v:
      value = value * x
  elif t == 2:
    print("min of ",v)
    value = min(v)
  elif t == 3:
    print("max of ",v)
    value = max(v)
  elif t == 5:
    print("greater than ",v)
    if v[0] > v[1]:
      value = 1
    else:
      value = 0
  elif t == 6:
    print("less then ",v)
    if v[0] < v[1]:
      value = 1
    else:
      value = 0
  elif t == 7:
    print("equal to ",v)
    if v[0] == v[1]:
      value = 1
    else:
      value = 0

  return b, value

var=[0]
b, value = processPacket(b)

print(f"\nfinal value: {value}\nsummed version: {var[0]}")