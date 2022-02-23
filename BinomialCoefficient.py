import time
start_time = time.time()

#divide and conquer approach
def binomialCoefficient(n,k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1

    #this is the recursive part of the function
    return (binomialCoefficient((n-1),(k-1)) + binomialCoefficient((n-1), k))

print("(This is the divide and conquer approach)")
#input commands for the values of n and k
n = int(input("Enter a value for n: "))
k = int(input("Enter a value for k: "))

#Prints final value
print("Value of C[" + str(n) + "][" + str(k) + "] is " + str(binomialCoefficient(n,k)))
print("Process finished --- %s seconds ---" % (time.time() - start_time))
print("\n")

#bottoms up dynamic programming 
def bottoms_up_binomialCoefficient(n,k):
  #declaring an empty array
  C = [[0 for x in range(k+1)] for x in range(n+1)]

  for i in range(n+1):
    for j in range(min(i,k) + 1):
      #base cases
      if j == 0 or j == i:
        C[i][j] = 1
      else:
        C[i][j] = C[i-1][j-1] + C[i-1][j]
  return C[n][k]

print("(This is the bottoms up dynamic programming approach)")
#input commands for the values of n and k
n = int(input("Enter a value for n: "))
k = int(input("Enter a value for k: "))

#Prints final value
print("Value of C[" + str(n) + "][" + str(k) + "] is " + str(bottoms_up_binomialCoefficient(n,k)))
print("Process finished --- %s seconds ---" % (time.time() - start_time))
print("\n")

#memoization approach
def binomialCoeffUtil(n, k, dp):
  #check if value is in lookup table then return
  if dp[n][k] != -1:
    return dp[n][k]

  #stores value in a table before returning
  if k == 0:
    dp[n][k] = 1
    return dp[n][k]

  #stores value in a table before returning
  if k == n:
    dp[n][k] = 1
    return dp[n][k]

  #saves value in the lookup table before returning
  dp[n][k] = (binomialCoeffUtil(n - 1, k - 1, dp) + binomialCoeffUtil(n - 1, k, dp))
  
  return dp[n][k]

def memo_binomialCoefficient(n,k):
  #create a temporary lookup table for stored values
  dp = [[-1 for y in range(k + 1)] for x in range(n + 1)]
  return binomialCoeffUtil(n, k, dp)

print("(This is the memoization dynamic programming approach)")
#input commands for the values of n and k
n = int(input("Enter a value for n: "))
k = int(input("Enter a value for k: "))

#Prints final value
print("Value of C[" + str(n) + "][" + str(k) + "] is " + str(memo_binomialCoefficient(n,k)))
print("Process finished --- %s seconds ---" % (time.time() - start_time))
print("\n")
print("This is the end of the program.")