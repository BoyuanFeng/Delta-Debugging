import commands
import string
import subprocess
import os

###########################
# For different input, we need to change to error_message in test function and the filename in the last section.
###########################


###########################
#Prepare for ddmin
###########################
# Print the test case
def coerce(deltas):
    # Pretty-print the configuration
    input = ""
    for (index, character) in deltas:
        input = input + character
    return input
# Test the case
def test(deltas):
    test.counter += 1
    print("Counter is %d" % test.counter)

    # Build input
    input = ""
    for (index, character) in deltas:
        input = input + character

    FileName = ''
    FileName = 'input.c'
    # Write input to `input.c'
    out = open(FileName, 'w')
    out.write(input)
    out.close()


    cmd = ''
    cmd = "(gcc -c -O3 input.c)"

    status = os.system(cmd)
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    error_message = ''
    for line in proc.stdout.readlines():
        error_message = error_message + line

    # Determine outcome
    if status == 0:
        return 0
    elif string.find(error_message, "internal compiler error: in print_reg") >= 0:
        return 1
    return 2            #0 for pass, 1 for fail and 2 for unresolved


test.counter = 0


def listminus(c1, c2):
    """Return a list of all elements of C1 that are not in C2."""
    s2 = {}
    for delta in c2:
        s2[delta] = 1

    c = []
    for delta in c1:
        if not s2.has_key(delta):
            c.append(delta)

    return c

def split(c, n):
    """Stub to overload in subclasses"""
    subsets = []
    start = 0
    for i in range(n):
        subset = c[start:start + (len(c) - start) / (n - i)]
        subsets.append(subset)
        start = start + len(subset)
    return subsets

def AllComplement(cx, a):
    subsets = []
    for i in a:
        subset = listminus(cx, i)
        subsets.append(subset)
    return subsets

#########################################
#ddmin
#########################################
def ddmin(cx):
    return ddmin2(cx, 2)

def ddmin2(cx, n):
    cxLenth = len(cx)
    size = cxLenth/n
    a = split(cx,n)
    b = AllComplement(cx,a)
    for i in a:
        if(test(i) == 1):
            return ddmin2(i, 2)
    for i in b:
        if(test(i) == 1):
            return ddmin2(i,max(n-1,2))
    if(n < len(cx)):
        return ddmin2(cx,min(len(cx),2*n))
    return cx

###################################################
# Run the algorithm and find the minimal difference
###################################################
deltas = []
index = 1

fname = 'shrink-wrap-separate-0.c'


###### Use lines as deltas
with open(fname) as f:
    content = f.readlines()

# bug.c should be replaced by the specific file name
for line in content:
    deltas.append((index, line))
    index = index + 1

print("Simplifying failure-inducing input...")
c = ddmin(deltas)  # Invoke DDMIN
print("The 1-minimal failure-inducing input is", coerce(c))
print("Removing any element will make the failure go away.")