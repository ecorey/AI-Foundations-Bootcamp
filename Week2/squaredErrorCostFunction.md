# Squared Error Cost Function

**Given a table of values such as the following for a table of circles:**

![Table Image](./table.JPG)

**If trying to find the ??? value using a NN the weights and constant values can be trainied or adjusted using a SQUARED ERROR COST VALE**

    import numpy

    def NN(m1, m2, w1, w2, b):
    z = m1 + w1 + m2 + w2 + b
    return sigmoid(z)

    def sigmoid(x):
    return 1/(1 + numpy.exp(-1))

    w1 = numpy.random.randn()
    w2 = numpy.random.randn()
    b = numpy.random.randn()

**To get the correct weights and constant for the w values and b value use a cost value, such as:**

    (prediction - target)^2

**This will identify where in a bellcurve the correct value is found on the intersection with the x axis line. To find the correct values the slope of the cost function is used.**

![Squared Error Cost Image](./squared_error.JPG)

---

[giant_neural_network](https://www.youtube.com/watch?v=c6NBkkKNZXw&list=PLxt59R_fWVzT9bDxA76AHm3ig0Gg9S3So&index=5)
