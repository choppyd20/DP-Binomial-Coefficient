# DP-Binomial-Coefficient
This program is computing binomial coefficients by using three different methods:
- Divide-and-conquer
-  Dynamic Programming ("bottom-up" approach)
-  Memoization (a special form of dynamic programming)

## Divide-and-conquer
This approach can be used to compute binomial coefficients, but it is very slow due to redundant calculations performed by the recursive calls.
The following code snippet is an example of the divide-and-conquer approach:
![image](https://user-images.githubusercontent.com/74651145/155374719-098b820e-7f7b-4ad4-9b79-fae50d6a2807.png)

## Dynamic Programming ("bottom-up" approach)
  This type of DP approach is known as the "bottom-up" approach. It is the basic dynamic programming approach. It solves subproblems in order from smallest to largest until the original problem is solved.
  
## Memoization (a special form of dynamic programming)
  This a dynamic programming tecchnique that uses the "top-down" recursive definition to solve only the needed smalller problems and avoids redundant calculations by solving smaller-problems once and storing their solutions.
  The following code uses memoization to compute Fibonacci numbers:
  
  ![image](https://user-images.githubusercontent.com/74651145/155374487-56973ef7-b078-4cd0-961e-51d3e0ec6883.png)
