# Galton Board

This a simple python script implementation that mimics the behaviour of experiments executed in a Galton Board.

The Galton Board is a device invented by Francis Galton1 to prove the central limit theorem, in particular that the binomial distribution is an approximation to the normal distribution.

The machine consists of a vertical board with several rows of nails. The balls fall from the top, bouncing randomly and deposit, as they fall, in the boxes at the bottom. Forming a bell surface.

## Ball distribution
The x amount of balls will hit the first nail having a probability of 1/2 of going to the left or to the right, and as they continue they will have more ways to go, that is, more possibilities for the balls to deviate. Throughout this structure, the balls take random paths until they fall into one of the channels placed at the base. In the end, inner channels will be more likely than outer channels, forming a probability distribution known as the gaussian distribution.
