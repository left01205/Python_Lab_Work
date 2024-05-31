# Perform Creation, indexing, slicing, concatenation and repetition operations on Python built-in  datatypes: Strings, List, Tuples, Dictionary, Set.
def Strings():
  A="HAKUNAMATATA"
  B="ABRACADABRA"
  print("INDEXING: ",A[0],A[-1]) # output -> H A
  print("SLICING : ",A[0:5])   # output -> HAKUN
  print("CONCATENATION : ",A+B) # output -> HAKUNAMATATAABRACADABRA
  print("REPETITION : ",A*2)  # output -> HAKUNAMATATAHAKUNAMATATA

def Lists():
  l1=[1,2,3,4,5,6]
  l2=[1.0,2.5,3.6,54.3]
  print("INDEXING: ",l1[0],l2[1]) # output -> 1 2.5
  print("SLICING : ",l1[0:3])   # output -> [1,2,3]
  print("CONCATENATION : ",l1+lb) # output -> [1,2,3,4,5,6,1.0,2.5,3.6,54.3]
  print("REPETITION : ",l1*2)  # output -> [1,2,3,4,5,6,1,2,3,4,5,6]

def Tuples():
  l1=(1,2,3,4,5,6)
  l2=(1.0,2.5,3.6,54.3)
  print("INDEXING: ",l1[0],l2[1]) # output -> 1 2.5
  print("SLICING : ",l1[0:3])   # output -> (1,2,3)
  print("CONCATENATION : ",l1+lb) # output -> (1,2,3,4,5,6,1.0,2.5,3.6,54.3)
  print("REPETITION : ",l1*2)  # output -> (1,2,3,4,5,6,1,2,3,4,5,6)

