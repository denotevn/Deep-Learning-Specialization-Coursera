## **It's basic of Logistic Regression and numpy tutorial**
1.  Which of the following best expresses what we want yhat to tell us? 
    + P(y= 1|x)
2. Which of these is the "Logistic Loss"?
   + This link : **[Logistics Loss](https://developers.google.com/machine-learning/crash-course/logistic-regression/model-training)**
3. Suppose x is a (8, 1) array. Which of the following is a valid reshape?
   + x.reshape(2,2,2)
   + It's basic of matrix
4. Consider the following random arrays a and b, and c:
    + a=np.random.randn(3,3) # a.shape = (3, 3)
    + b=np.random.randn(2,1) # b.shape = (2, 1)
    + c = a + b
    > **answer:** The computation cannot happen because it is not possible to broadcast more than one dimension
5. Consider the two following random arrays a and B:
    + a=np.random.randn(4,3) # a.shape=(4,3)
    + b=np.random.randn(3,2) # b.shape=(3,2)
    + c=a∗b
    > **Answer:** The computation cannot happen because the sizes don't match. It's going to be "Error"
    + Indeed! In numpy the "*" operator indicates element-wise multiplication. It is different from "np.dot()". If you would try "c = np.dot(a,b)" you would get c.shape = (4, 2)
6. Suppose you have nx input features per example.  If we decide to use row vectors x(i) for the features and X  = [[x1],[x2], ... [xn]]. What the dimension of X?
    + (m, nx)
7. Consider the following array: a=np.array([[2,1],[1,3]]). What is the result of a*a?
    + [[4,1], [1,9]]
8. Consider the following code snippet:
    + a.shape=(4,3)
    + b.shape = (4, 1)
    + for i in range(3):
 > for j in range(4): c[i][j] = a[j][i] + b[j]
 > How do you vectorize this?
 + **Answer:** c = a.T + b.T
9. + a.shape = (3,3)
   + b.shape = (3,3)
   + c=a∗∗2+b.T∗∗2
   + Which of the following gives an equivalent output for c?
        + for i in range(3):
            + for j in range(3):
                + c[i][j] = a[i][j]**2 + b[j][i]**2
10. Consider the following computational graph.
    + a^2 - c^2