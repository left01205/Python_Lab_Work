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
  print("CONCATENATION : ",l1+l2) # output -> [1,2,3,4,5,6,1.0,2.5,3.6,54.3]
  print("REPETITION : ",l1*2)  # output -> [1,2,3,4,5,6,1,2,3,4,5,6]

def Tuples():
  l1=(1,2,3,4,5,6)
  l2=(1.0,2.5,3.6,54.3)
  print("INDEXING: ",l1[0],l2[1]) # output -> 1 2.5
  print("SLICING : ",l1[0:3])   # output -> (1,2,3)
  print("CONCATENATION : ",l1+l2) # output -> (1,2,3,4,5,6,1.0,2.5,3.6,54.3)
  print("REPETITION : ",l1*2)  # output -> (1,2,3,4,5,6,1,2,3,4,5,6)
def Dictionary():
  d1={'A':10,'B':20,'C':30}
  d2={'D':40,'E':50,'F':60}
  print("INDEXING: ",d1['B'],d2['F']) # output -> 20 60
  '''
  DICTIONARY DOESN'T SUPPORT SLICING, CONCATENATION  OR REPETITION
  IT DOES HAVE update() METHOD.
  '''
  def Sets():
    s1={1,2,3,4,5}
    s2={6,7,8,9,10}
    '''
    DOESN'T SUPPORT EITHER OF 'EM
    '''

Strings()
Lists()
Tuples()
Dictionary()
Sets()
