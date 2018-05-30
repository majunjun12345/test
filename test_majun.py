from random import randint,sample

s1={x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
s2={x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
s3={x:randint(1,4) for x in sample('abcdefg',randint(3,6))}

m = reduce(lambda a,b : a & b,map(dict.viewkeys,[s1,s2,s3]))
print m